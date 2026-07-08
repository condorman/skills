# Behavioral Patterns

Behavioral patterns concern how objects interact, communicate, and distribute responsibility among themselves — they capture the flow of control and the assignment of duties rather than the shape of the object graph.

## Table of Contents

- [Chain of Responsibilities](#chain-of-responsibilities)
- [Command](#command)
- [Iterator](#iterator)
- [Mediator](#mediator)
- [Memento](#memento)
- [Null Object](#null-object)
- [Observer](#observer)
- [Specification](#specification)
- [State](#state)
- [Strategy](#strategy)
- [Template Method](#template-method)
- [Visitor](#visitor)
- [Interpreter](#interpreter)

## Chain of Responsibilities

**Intent.** Pass a request along a chain of handlers, giving each the chance to handle it or forward it to the next, so the sender is decoupled from the receiver.

**Use when.**
- A request could be handled by one of several objects and you don't know which one up front (e.g. an approval that goes clerk → manager → director based on amount).
- You want to add, remove, or reorder processing steps without touching the caller.
- You have a growing `if/elseif` deciding which handler applies to an incoming request (auth, then rate-limit, then validation).
- Multiple handlers may each contribute, and processing should stop as soon as one succeeds.

**Structure.** A `Handler` interface with a `handle()` method and a reference to an optional successor. Each `ConcreteHandler` either processes the request or delegates to `$next`. The client builds the chain and drops the request at its head.

```php
<?php

declare(strict_types=1);

// Role: the request travelling down the chain
final readonly class PurchaseRequest
{
    public function __construct(
        public string $item,
        public int $amountCents,
    ) {}
}

// Role: handler contract
interface Approver
{
    public function setNext(Approver $next): Approver;

    public function approve(PurchaseRequest $request): string;
}

// Role: base handler holding the successor link
abstract class BaseApprover implements Approver
{
    private ?Approver $next = null;

    public function setNext(Approver $next): Approver
    {
        $this->next = $next;

        return $next; // fluent chaining
    }

    protected function passOn(PurchaseRequest $request): string
    {
        return $this->next?->approve($request)
            ?? 'No approver could authorise this request.';
    }
}

// Role: concrete handler
final class Clerk extends BaseApprover
{
    public function approve(PurchaseRequest $request): string
    {
        if ($request->amountCents <= 10_000) {
            return "Clerk approved {$request->item}.";
        }

        return $this->passOn($request);
    }
}

// Role: concrete handler
final class Manager extends BaseApprover
{
    public function approve(PurchaseRequest $request): string
    {
        if ($request->amountCents <= 100_000) {
            return "Manager approved {$request->item}.";
        }

        return $this->passOn($request);
    }
}

// usage
$clerk = new Clerk();
$clerk->setNext(new Manager());

echo $clerk->approve(new PurchaseRequest('stapler', 4_500)), PHP_EOL;   // Clerk
echo $clerk->approve(new PurchaseRequest('laptop', 90_000)), PHP_EOL;   // Manager
```

**Trade-offs.**
- **Gains:** Decouples sender from receiver; handlers are independently testable and reorderable; new steps slot in without editing existing ones.
- **Costs:** No guarantee a request is handled (needs a terminal fallback); harder to trace which handler acted; the chain is set up imperatively.
- **Skip it when:** There's exactly one receiver, or the routing is a stable two-branch decision — a method call or a `match` is clearer.

**Integrating.** Laravel/Symfony/CodeIgniter 4: this is exactly HTTP middleware (`$next($request)` pipelines) and Laravel's `Pipeline` helper. WordPress: less idiomatic; filter chains cover part of the intent.

**Related / not to be confused with.** Middleware is Chain of Responsibilities specialised for the request/response cycle — same shape, but middleware typically wraps `$next` (before/after) whereas classic CoR either handles or forwards. Unlike [Command](#command), a handler decides *whether* to act; a command already knows *what* to do. Unlike a [Decorator](structural.md), every handler shares one interface and the goal is routing, not augmenting behaviour.

## Command

**Intent.** Encapsulate a request as an object, so you can parameterise clients, queue or log requests, and support undo.

**Use when.**
- You want to queue, schedule, or defer work (send-email, generate-report) and run it later or elsewhere.
- You need undo/redo — each action must remember how to reverse itself.
- You want a uniform `execute()` API over heterogeneous operations (macro recording, a task runner, menu items + keyboard shortcuts triggering the same action).
- You're logging or replaying operations for audit or crash recovery.

**Structure.** A `Command` interface with `execute()`. Each `ConcreteCommand` holds a receiver plus its parameters and calls the right receiver method. An invoker triggers `execute()` without knowing the concrete command; the client wires command to receiver.

```php
<?php

declare(strict_types=1);

// Role: command contract
interface Command
{
    public function execute(): void;

    public function undo(): void;
}

// Role: receiver — does the real work
final class TextDocument
{
    private string $content = '';

    public function append(string $text): void
    {
        $this->content .= $text;
    }

    public function truncate(int $length): void
    {
        $this->content = substr($this->content, 0, $length);
    }

    public function render(): string
    {
        return $this->content;
    }
}

// Role: concrete command capturing enough state to reverse itself
final class AppendText implements Command
{
    private int $previousLength = 0;

    public function __construct(
        private readonly TextDocument $document,
        private readonly string $text,
    ) {}

    public function execute(): void
    {
        $this->previousLength = strlen($this->document->render());
        $this->document->append($this->text);
    }

    public function undo(): void
    {
        $this->document->truncate($this->previousLength);
    }
}

// Role: invoker keeping a history for undo
final class Editor
{
    /** @var Command[] */
    private array $history = [];

    public function run(Command $command): void
    {
        $command->execute();
        $this->history[] = $command;
    }

    public function undoLast(): void
    {
        (array_pop($this->history))?->undo();
    }
}

// usage
$doc = new TextDocument();
$editor = new Editor();
$editor->run(new AppendText($doc, 'Hello'));
$editor->run(new AppendText($doc, ' World'));
echo $doc->render(), PHP_EOL; // Hello World
$editor->undoLast();
echo $doc->render(), PHP_EOL; // Hello
```

**Trade-offs.**
- **Gains:** First-class, storable, queueable actions; clean undo; invoker fully decoupled from receiver.
- **Costs:** A class per operation; undo state can be fiddly; indirection for what might be a one-line call.
- **Skip it when:** You just need to call a method now and will never queue, log, or reverse it.

**Integrating.** Laravel: queued Jobs and `Artisan` console commands are the Command pattern; dispatch to run async. Symfony: Messenger message + handler, and Console commands. CodeIgniter 4: `spark` CLI commands and queued tasks. WordPress: WP-Cron events / WP-CLI commands.

**Related / not to be confused with.** [Strategy](#strategy) and Command share a one-method interface, but Strategy swaps *how* a single operation is computed (an algorithm you plug in), whereas Command packages *a whole request* (receiver + args) to run later or undo. Unlike [Chain of Responsibilities](#chain-of-responsibilities), a command doesn't decide whether to run — it just runs.

## Iterator

**Intent.** Provide sequential access to the elements of an aggregate without exposing its underlying representation.

**Use when.**
- You want `foreach` over a custom collection without leaking its internal array/tree/linked structure.
- Traversal is expensive or infinite and you want lazy, one-at-a-time production (streaming a large file, paginated API results).
- You need multiple independent cursors over the same collection.
- You want uniform iteration across different container types.

**Structure.** In PHP you rarely roll your own — implement the SPL `Iterator` interface directly, or `IteratorAggregate` to expose an inner iterator, or (simplest) return a **generator** using `yield`. Generators give you lazy iteration and constant memory for free.

```php
<?php

declare(strict_types=1);

// Role: an immutable element
final readonly class Book
{
    public function __construct(
        public string $title,
        public string $author,
    ) {}
}

// Role: aggregate. IteratorAggregate lets `foreach` work directly.
// A generator (yield) is the idiomatic PHP iterator — lazy and stateless.
final class Bookshelf implements \IteratorAggregate
{
    /** @var Book[] */
    private array $books = [];

    public function add(Book $book): void
    {
        $this->books[] = $book;
    }

    public function getIterator(): \Generator
    {
        foreach ($this->books as $book) {
            yield $book; // produced lazily, one at a time
        }
    }

    // A second, filtered traversal — cheap to add, still lazy.
    public function by(string $author): \Generator
    {
        foreach ($this->books as $book) {
            if ($book->author === $author) {
                yield $book;
            }
        }
    }
}

// usage
$shelf = new Bookshelf();
$shelf->add(new Book('Refactoring', 'Fowler'));
$shelf->add(new Book('UML Distilled', 'Fowler'));
$shelf->add(new Book('Clean Code', 'Martin'));

foreach ($shelf as $book) {            // uses getIterator()
    echo $book->title, PHP_EOL;
}

foreach ($shelf->by('Fowler') as $book) {
    echo 'Fowler: ', $book->title, PHP_EOL;
}
```

**Trade-offs.**
- **Gains:** Uniform `foreach` support; hides internal structure; generators make lazy/infinite sequences trivial and memory-cheap.
- **Costs:** A hand-rolled `Iterator` (five methods) is verbose and error-prone — prefer generators; separate cursor state to manage if you don't.
- **Skip it when:** A plain array or a generator function suffices — don't wrap an array in a full `Iterator` class for its own sake.

**Integrating.** Laravel: `Collection` and lazy `LazyCollection` are iterators; Eloquent cursors yield models lazily. Symfony: Finder and many components return iterators. Custom: return generators from repository methods for streaming.

**Related / not to be confused with.** Unlike [Visitor](#visitor), Iterator only *traverses* — it doesn't add operations to elements. In PHP the pattern is mostly subsumed by the language: reach for `yield` or `IteratorAggregate` before writing a bespoke cursor.

## Mediator

**Intent.** Define an object that encapsulates how a set of objects interact, so they refer to the mediator instead of to each other.

**Use when.**
- A set of components each hold references to many others and the wiring has become an n-to-n tangle (a dialog where every widget knows every other widget).
- Reusing a component is hard because it's coupled to specific siblings.
- Interaction logic is spread across many classes and you want it centralised (chat room routing messages between participants).
- You keep adding cross-component "when X changes, update Y and Z" rules.

**Structure.** A `Mediator` interface; colleagues hold a reference to the mediator and notify it of events instead of calling siblings directly. The `ConcreteMediator` knows all colleagues and coordinates them.

```php
<?php

declare(strict_types=1);

// Role: mediator contract
interface ChatMediator
{
    public function broadcast(User $from, string $message): void;

    public function join(User $user): void;
}

// Role: concrete mediator — the only place that knows all colleagues
final class ChatRoom implements ChatMediator
{
    /** @var User[] */
    private array $users = [];

    public function join(User $user): void
    {
        $this->users[] = $user;
    }

    public function broadcast(User $from, string $message): void
    {
        foreach ($this->users as $user) {
            if ($user !== $from) {
                $user->receive($from->name, $message);
            }
        }
    }
}

// Role: colleague — talks to the mediator, never to peers
final class User
{
    public function __construct(
        public readonly string $name,
        private readonly ChatMediator $room,
    ) {
        $room->join($this);
    }

    public function send(string $message): void
    {
        $this->room->broadcast($this, $message);
    }

    public function receive(string $from, string $message): void
    {
        echo "[{$this->name}] {$from}: {$message}", PHP_EOL;
    }
}

// usage
$room = new ChatRoom();
$alice = new User('Alice', $room);
$bob = new User('Bob', $room);
$alice->send('Hi all'); // Bob receives it; Alice does not
```

**Trade-offs.**
- **Gains:** Colleagues become reusable and loosely coupled; interaction logic lives in one place, easy to change.
- **Costs:** The mediator can swell into a god-object that knows everything; centralisation can just relocate complexity.
- **Skip it when:** Only two or three objects interact, or the collaboration is stable and simple — direct references are fine.

**Integrating.** Custom: an application "service" or coordinator that orchestrates several domain objects is a mediator. Symfony/Laravel: an event bus is a decentralised mediator (see Observer).

**Related / not to be confused with.** [Observer](#observer) is decentralised broadcast: publishers don't know subscribers and any object may subscribe. Mediator is centralised coordination: colleagues know the mediator, and it holds the *specific* interaction rules between named participants. Observer answers "who cares that this happened"; Mediator answers "given this happened, orchestrate the others".

## Memento

**Intent.** Capture and externalise an object's internal state without violating encapsulation, so it can be restored later.

**Use when.**
- You need undo/rollback or checkpoints (editor history, wizard "back", game save states).
- You want a snapshot of an object's state that outside code can hold but not tamper with.
- Producing state directly would expose internals you want to keep private.
- You need to restore a prior state after a speculative or failed operation.

**Structure.** The `Originator` creates a `Memento` holding a snapshot of its private state and can restore from one. A `Caretaker` stores mementos (the history) but treats them as opaque — it never inspects their contents.

```php
<?php

declare(strict_types=1);

// Role: memento — opaque, immutable snapshot
final readonly class EditorMemento
{
    public function __construct(
        private string $content,
    ) {}

    // Only the originator is meant to read this back.
    public function content(): string
    {
        return $this->content;
    }
}

// Role: originator — owns the state, makes and restores snapshots
final class Editor
{
    private string $content = '';

    public function type(string $words): void
    {
        $this->content = trim($this->content . ' ' . $words);
    }

    public function render(): string
    {
        return $this->content;
    }

    public function save(): EditorMemento
    {
        return new EditorMemento($this->content);
    }

    public function restore(EditorMemento $memento): void
    {
        $this->content = $memento->content();
    }
}

// Role: caretaker — keeps the history, never peeks inside a memento
final class History
{
    /** @var EditorMemento[] */
    private array $snapshots = [];

    public function push(EditorMemento $memento): void
    {
        $this->snapshots[] = $memento;
    }

    public function pop(): ?EditorMemento
    {
        return array_pop($this->snapshots);
    }
}

// usage
$editor = new Editor();
$history = new History();

$editor->type('The quick brown fox');
$history->push($editor->save());     // checkpoint
$editor->type('jumps over the dog');
echo $editor->render(), PHP_EOL;     // full sentence

$editor->restore($history->pop());   // undo
echo $editor->render(), PHP_EOL;     // The quick brown fox
```

**Trade-offs.**
- **Gains:** Undo/rollback without exposing internals; the originator keeps its encapsulation; history logic lives in the caretaker.
- **Costs:** Snapshots can be memory-heavy if state is large or saved often; deep copies needed for mutable state.
- **Skip it when:** State is trivial to reconstruct, or an immutable value object you can just re-assign already gives you "undo".

**Integrating.** Mostly framework-agnostic. Relates to DB transactions/savepoints as a persistence-level equivalent; pairs naturally with [Command](#command) for undo stacks.

**Related / not to be confused with.** Command stores *the operation* (and how to reverse it); Memento stores *the state* at a point in time. Undo is often built from Command; snapshot-based undo uses Memento. Unlike serialization, Memento is an in-process pattern focused on encapsulation, not a wire format.

## Null Object

**Intent.** Provide an object with neutral ("do nothing") behaviour as a drop-in substitute for a missing collaborator, so callers never check for null.

**Use when.**
- You keep writing `if ($logger !== null) { $logger->log(...); }` and want the guard gone.
- A dependency is optional and its absence has a well-defined harmless behaviour (a no-op logger, an anonymous/guest user, an empty cart).
- You want to avoid scattering null checks and the `NullPointerException`-style bugs they miss.
- A default "nothing happened" implementation is genuinely valid domain behaviour.

**Structure.** Both the real object and the `NullObject` implement the same interface. The null object's methods do nothing (or return neutral values). Callers depend on the interface and treat the null object like any other.

```php
<?php

declare(strict_types=1);

// Role: shared contract
interface Logger
{
    public function log(string $message): void;
}

// Role: real implementation
final class FileLogger implements Logger
{
    public function __construct(private readonly string $path) {}

    public function log(string $message): void
    {
        file_put_contents($this->path, $message . PHP_EOL, FILE_APPEND);
    }
}

// Role: null object — same type, neutral behaviour
final class NullLogger implements Logger
{
    public function log(string $message): void
    {
        // intentionally does nothing
    }
}

// Role: client that never checks for null
final class PaymentService
{
    public function __construct(private readonly Logger $logger) {}

    public function charge(int $cents): void
    {
        // ... charge ...
        $this->logger->log("Charged {$cents} cents"); // always safe
    }
}

// usage
$loud = new PaymentService(new FileLogger('/tmp/pay.log'));
$quiet = new PaymentService(new NullLogger()); // logging simply disabled
$loud->charge(500);
$quiet->charge(500);
```

**Trade-offs.**
- **Gains:** Eliminates null checks; simplifies callers; makes "absence" an explicit, testable type.
- **Costs:** Can hide bugs by silently swallowing operations that should have happened; one more class; misuse where an error was the correct response.
- **Skip it when:** Absence is genuinely exceptional and should fail loudly — a null object would mask a real error. PHP's `?->` and `??` already handle simple optional calls.

**Integrating.** PSR-3 ships `Psr\Log\NullLogger` — the canonical example. Laravel `null` cache/mail drivers and Symfony's `NullOutput` are null objects. Broadly framework-agnostic.

**Related / not to be confused with.** It's a special case of [Strategy](#strategy)/polymorphism where one implementation is deliberately inert. Distinct from an Optional/Maybe type: Null Object *is* a valid collaborator you call normally, not a wrapper you must unwrap.

## Observer

**Intent.** Define a one-to-many dependency so that when one object changes state, all its dependents are notified automatically.

**Use when.**
- One event should trigger several independent reactions and you don't want the source coupled to them (on order-placed: send email, decrement stock, notify analytics).
- The set of interested parties changes at runtime or is unknown to the source.
- You're building an event/hook system, or reacting to domain events.
- You catch yourself hardcoding a list of "and then also call…" side effects into a method.

**Structure.** A `Subject` maintains a list of `Observer`s and notifies them on change. Observers implement an `update()`/`handle()` method and subscribe/unsubscribe at will. The subject knows only the observer interface, never concrete listeners.

```php
<?php

declare(strict_types=1);

// Role: the event payload
final readonly class OrderPlaced
{
    public function __construct(
        public string $orderId,
        public int $totalCents,
    ) {}
}

// Role: observer contract
interface OrderObserver
{
    public function handle(OrderPlaced $event): void;
}

// Role: subject — broadcasts without knowing who listens
final class OrderPublisher
{
    /** @var OrderObserver[] */
    private array $observers = [];

    public function subscribe(OrderObserver $observer): void
    {
        $this->observers[] = $observer;
    }

    public function placeOrder(OrderPlaced $event): void
    {
        // ... persist the order ...
        foreach ($this->observers as $observer) {
            $observer->handle($event);
        }
    }
}

// Role: concrete observers, independent of each other
final class SendConfirmationEmail implements OrderObserver
{
    public function handle(OrderPlaced $event): void
    {
        echo "Emailing confirmation for {$event->orderId}", PHP_EOL;
    }
}

final class UpdateInventory implements OrderObserver
{
    public function handle(OrderPlaced $event): void
    {
        echo "Reserving stock for {$event->orderId}", PHP_EOL;
    }
}

// usage
$publisher = new OrderPublisher();
$publisher->subscribe(new SendConfirmationEmail());
$publisher->subscribe(new UpdateInventory());
$publisher->placeOrder(new OrderPlaced('A-100', 4_999));
```

**Trade-offs.**
- **Gains:** Loose coupling between source and reactions; listeners added/removed freely; open to extension without editing the subject.
- **Costs:** Notification order and cascades can be hard to reason about; silent listeners make control flow implicit; potential memory leaks if observers aren't detached.
- **Skip it when:** There's one fixed reaction — just call it. Debugging an over-eventful system is worse than a direct method call.

**Integrating.** Laravel: model Events & Observers, and the Event/Listener system — the textbook mapping. Symfony: EventDispatcher (`dispatch` + subscribers/listeners). WordPress: `do_action` / `add_action` hooks are the observer pattern. CodeIgniter 4: the Events service (`Events::on()` / `Events::trigger()`). Also PSR-14.

**Related / not to be confused with.** Versus [Mediator](#mediator): Observer is *decentralised* broadcast (source doesn't know or care who listens; any object may subscribe), while Mediator *centralises* interaction rules between known participants. Versus [Chain of Responsibilities](#chain-of-responsibilities): observers all react; a chain forwards until one handles.

## Specification

**Intent.** Encapsulate a business rule in a reusable predicate object that can be combined with boolean logic to test whether a candidate satisfies it.

**Use when.**
- The same business rule ("is this customer eligible for a discount?") is checked in multiple places and you want one source of truth.
- Rules must be combined (`and`/`or`/`not`) and recombined at runtime (filter builder, matching engine, validation).
- Selection criteria grow complex and you want to name and unit-test each rule in isolation.
- You want to separate *what* qualifies from *how* you fetch or iterate candidates.

**Structure.** A `Specification` interface with `isSatisfiedBy($candidate): bool`. Concrete specs implement one rule each; composite specs (`AndSpecification`, `OrSpecification`, `NotSpecification`) combine others. A base class can supply the combinators fluently.

```php
<?php

declare(strict_types=1);

final readonly class Customer
{
    public function __construct(
        public int $orderCount,
        public bool $newsletter,
    ) {}
}

// Role: specification contract with fluent combinators
interface Specification
{
    public function isSatisfiedBy(Customer $customer): bool;

    public function and(Specification $other): Specification;

    public function not(): Specification;
}

// Role: base class supplying combinators
abstract class BaseSpecification implements Specification
{
    abstract public function isSatisfiedBy(Customer $customer): bool;

    public function and(Specification $other): Specification
    {
        return new AndSpecification($this, $other);
    }

    public function not(): Specification
    {
        return new NotSpecification($this);
    }
}

// Role: leaf specifications — one rule each
final class IsLoyal extends BaseSpecification
{
    public function isSatisfiedBy(Customer $customer): bool
    {
        return $customer->orderCount >= 10;
    }
}

final class Subscribed extends BaseSpecification
{
    public function isSatisfiedBy(Customer $customer): bool
    {
        return $customer->newsletter;
    }
}

// Role: composite specifications
final class AndSpecification extends BaseSpecification
{
    public function __construct(
        private readonly Specification $left,
        private readonly Specification $right,
    ) {}

    public function isSatisfiedBy(Customer $customer): bool
    {
        return $this->left->isSatisfiedBy($customer)
            && $this->right->isSatisfiedBy($customer);
    }
}

final class NotSpecification extends BaseSpecification
{
    public function __construct(private readonly Specification $spec) {}

    public function isSatisfiedBy(Customer $customer): bool
    {
        return ! $this->spec->isSatisfiedBy($customer);
    }
}

// usage
$eligible = (new IsLoyal())->and(new Subscribed());
$customer = new Customer(orderCount: 12, newsletter: true);
var_dump($eligible->isSatisfiedBy($customer)); // true
```

**Trade-offs.**
- **Gains:** Named, reusable, individually testable rules; runtime composition; keeps domain logic out of query/loop code.
- **Costs:** Many small classes; combinator plumbing; in-memory specs don't automatically translate to efficient SQL.
- **Skip it when:** A rule is used once and won't be combined — an inline `fn()` or a method on the entity is simpler.

**Integrating.** Symfony/Doctrine: Criteria and repository specifications formalise this; some libraries translate specs to DQL. Laravel: query scopes cover simple cases; dedicated spec objects for reusable domain rules. Broadly a DDD tactical pattern.

**Related / not to be confused with.** It's a focused form of [Strategy](#strategy) whose algorithm is always "return a bool". Prefer it over [Interpreter](#interpreter) when you need composable rules rather than a full grammar. Don't confuse with a Validator: a spec answers a yes/no about a candidate; a validator collects error messages.

## State

**Intent.** Allow an object to alter its behaviour when its internal state changes — the object appears to change its class.

**Use when.**
- An object behaves very differently depending on a mode, and you have big `switch($this->status)` blocks in many methods (an order that is draft / paid / shipped / cancelled).
- Transitions between modes follow rules ("you can ship only after payment"), and you want those rules localised.
- The *object itself* decides when to move to the next mode as a result of its operations.
- Adding a new mode currently means editing conditionals scattered across the class.

**Structure.** A `State` interface declares the state-dependent operations. Each `ConcreteState` implements behaviour for one mode *and* decides the next state, calling back to the context to transition. The `Context` holds a current state and delegates to it.

```php
<?php

declare(strict_types=1);

// Role: state contract
interface OrderState
{
    public function pay(Order $order): void;

    public function ship(Order $order): void;

    public function label(): string;
}

// Role: context — delegates to the current state
final class Order
{
    private OrderState $state;

    public function __construct()
    {
        $this->state = new DraftState();
    }

    public function transitionTo(OrderState $state): void
    {
        echo "-> now {$state->label()}", PHP_EOL;
        $this->state = $state;
    }

    public function pay(): void { $this->state->pay($this); }
    public function ship(): void { $this->state->ship($this); }
}

// Role: concrete state — behaviour AND the transition it triggers itself
final class DraftState implements OrderState
{
    public function pay(Order $order): void
    {
        $order->transitionTo(new PaidState()); // the object advances itself
    }

    public function ship(Order $order): void
    {
        echo 'Cannot ship an unpaid order.', PHP_EOL;
    }

    public function label(): string { return 'draft'; }
}

final class PaidState implements OrderState
{
    public function pay(Order $order): void
    {
        echo 'Already paid.', PHP_EOL;
    }

    public function ship(Order $order): void
    {
        $order->transitionTo(new ShippedState());
    }

    public function label(): string { return 'paid'; }
}

final class ShippedState implements OrderState
{
    public function pay(Order $order): void { echo 'Already shipped.', PHP_EOL; }
    public function ship(Order $order): void { echo 'Already shipped.', PHP_EOL; }
    public function label(): string { return 'shipped'; }
}

// usage
$order = new Order();
$order->ship(); // rejected: unpaid
$order->pay();  // draft -> paid
$order->ship(); // paid -> shipped
```

**Trade-offs.**
- **Gains:** Removes sprawling status conditionals; each mode and its transitions are isolated and testable; illegal transitions are naturally rejected.
- **Costs:** A class per state; transition logic spread across states can obscure the overall state machine; more objects to track.
- **Skip it when:** There are two states and one flag, or transitions are trivial — a status enum + a `match` is plenty.

**Integrating.** Symfony: the Workflow component models states and guarded transitions declaratively — often better than hand-rolling. Laravel: packages like `spatie/laravel-model-states`. Elsewhere, an enum-backed status column plus a small transition table.

**Related / not to be confused with.** This is the crucial pairing with [Strategy](#strategy). **State: the object transitions between states itself, and behaviour follows; states often trigger their own transitions, and the states are aware of each other.** **Strategy: the client picks one interchangeable algorithm and the object never changes it on its own; strategies are mutually oblivious.** Same structure (context delegates to an interface), opposite intent: State is about *self-driven mode changes over time*, Strategy is about *externally chosen behaviour*.

## Strategy

**Intent.** Define a family of interchangeable algorithms, encapsulate each one, and make them swappable so the algorithm varies independently of the client that uses it.

**Use when.**
- You have a growing `if/elseif` choosing between algorithms — shipping cost (flat, weight-based, by-region), sort orders, pricing rules — and want to add more without touching the caller.
- Several classes differ only in *how* they do one thing; you want to hoist that variation into pluggable objects.
- The choice of algorithm should be made by the *client* (or config/DI) and stays fixed for the object's use.
- You want to test each algorithm in isolation.

**Structure.** A `Strategy` interface declares the algorithm. Each `ConcreteStrategy` implements one variant. The `Context` is configured (usually via constructor) with a strategy and delegates to it; it never changes the strategy on its own.

```php
<?php

declare(strict_types=1);

final readonly class Parcel
{
    public function __construct(
        public int $weightGrams,
        public string $region,
    ) {}
}

// Role: strategy contract
interface ShippingCost
{
    public function forParcel(Parcel $parcel): int; // cents
}

// Role: concrete strategies — interchangeable algorithms
final class FlatRate implements ShippingCost
{
    public function __construct(private readonly int $cents = 500) {}

    public function forParcel(Parcel $parcel): int
    {
        return $this->cents;
    }
}

final class ByWeight implements ShippingCost
{
    public function forParcel(Parcel $parcel): int
    {
        return (int) ceil($parcel->weightGrams / 1000) * 200;
    }
}

// Role: context — uses whichever strategy the client injected
final class Checkout
{
    public function __construct(private readonly ShippingCost $strategy) {}

    public function shippingFor(Parcel $parcel): int
    {
        return $this->strategy->forParcel($parcel);
    }
}

// usage — the CLIENT chooses the algorithm; the context won't change it
$parcel = new Parcel(weightGrams: 2_400, region: 'EU');
echo (new Checkout(new FlatRate()))->shippingFor($parcel), PHP_EOL;  // 500
echo (new Checkout(new ByWeight()))->shippingFor($parcel), PHP_EOL;  // 600
```

**Trade-offs.**
- **Gains:** Swaps algorithms without touching the client; each variant is isolated and testable; replaces conditional-heavy methods; open for extension.
- **Costs:** More classes and objects; the client must know enough to pick; overkill for a stable single algorithm.
- **Skip it when:** There's one algorithm, or the branches are two trivial cases — a `match` or a closure is lighter.

**Integrating.** Laravel/Symfony/CodeIgniter 4: config-driven "drivers" (cache, mail, session, filesystem) are Strategy — the manager resolves the concrete strategy. DI containers make injecting the chosen strategy natural. In PHP a single-method strategy is often just a first-class `callable`/closure.

**Related / not to be confused with.** Versus [State](#state): Strategy is chosen by the client and doesn't change itself; State transitions itself and drives behaviour over time. Versus [Template Method](#template-method): Strategy varies behaviour by *composition* (inject an object) — swappable at runtime; Template Method varies it by *inheritance* (override a hook) — fixed at compile time. Versus [Command](#command): Strategy plugs in *how* to compute one thing; Command packages *a whole request* to run/queue/undo.

## Template Method

**Intent.** Define the skeleton of an algorithm in a base method, deferring specific steps to subclasses so they can vary steps without changing the algorithm's structure.

**Use when.**
- Several routines share the same overall sequence but differ in a few steps (parse → validate → transform → export, where only parse/export differ per format).
- You want to enforce an invariant order of steps and let subclasses fill in the gaps.
- You have near-duplicate methods differing only in the middle — hoist the common shell into a base class.
- You want "hooks": optional steps subclasses may override, with sensible defaults.

**Structure.** An abstract base class defines a `final` template method that calls a fixed sequence of steps. Some steps are `abstract` (subclasses must supply them); some are hooks with defaults. Subclasses override only the varying steps.

```php
<?php

declare(strict_types=1);

// Role: abstract class holding the invariant algorithm skeleton
abstract class ReportBuilder
{
    // The template method — sequence is fixed and cannot be overridden.
    final public function build(array $rows): string
    {
        $out = $this->header();
        foreach ($rows as $row) {
            $out .= $this->formatRow($row); // primitive step (required)
        }

        return $out . $this->footer();      // hook (optional)
    }

    // Required step supplied by subclasses.
    abstract protected function formatRow(array $row): string;

    // Hooks with defaults — override only if needed.
    protected function header(): string
    {
        return '';
    }

    protected function footer(): string
    {
        return '';
    }
}

// Role: concrete class filling in the varying steps
final class CsvReport extends ReportBuilder
{
    protected function formatRow(array $row): string
    {
        return implode(',', $row) . PHP_EOL;
    }
}

// Role: another variant reusing the same skeleton
final class HtmlReport extends ReportBuilder
{
    protected function header(): string { return "<table>" . PHP_EOL; }
    protected function footer(): string { return "</table>" . PHP_EOL; }

    protected function formatRow(array $row): string
    {
        return '<tr><td>' . implode('</td><td>', $row) . '</td></tr>' . PHP_EOL;
    }
}

// usage
$rows = [['Alice', '30'], ['Bob', '25']];
echo (new CsvReport())->build($rows);
echo (new HtmlReport())->build($rows);
```

**Trade-offs.**
- **Gains:** Removes duplication in the shared skeleton; enforces step order; the "don't call super and forget a step" problem disappears (the base owns the sequence).
- **Costs:** Relies on inheritance — one base class only, tight coupling parent↔child; the flow is split across files; hard to vary at runtime.
- **Skip it when:** Steps vary at runtime or you'd otherwise want multiple axes of variation — prefer Strategy (composition).

**Integrating.** Common in framework base classes you extend (Symfony `Command::execute()`, abstract controllers/voters, Laravel abstract jobs/notifications, CodeIgniter `BaseController`). You're *using* Template Method whenever you subclass a framework base and override protected hooks.

**Related / not to be confused with.** Versus [Strategy](#strategy): Template Method uses inheritance (override a step), Strategy uses composition (inject an algorithm) — Strategy is swappable at runtime, Template Method is not. Versus [Factory Method](creational.md): Factory Method is often *a* step within a template method (a hook that returns the object to use).

## Visitor

**Intent.** Represent an operation to be performed on the elements of an object structure, letting you define a new operation without changing the classes of the elements.

**Use when.**
- You have a stable set of element classes (an AST, a document tree, a shape hierarchy) and keep needing to add *new operations* over all of them (render, export, price, validate).
- Related behaviour is currently scattered as a method-per-operation across many element classes and you want it gathered per-operation instead.
- The operation needs to behave differently per concrete element type and you'd otherwise write `instanceof` ladders.
- Element types rarely change but operations grow.

**Structure.** Elements accept a `Visitor` via an `accept(Visitor $v)` method that calls the type-specific `visitX($this)` — this **double dispatch** selects behaviour by both element and visitor. Each `ConcreteVisitor` implements one operation across all element types.

```php
<?php

declare(strict_types=1);

// Role: element contract — accepts a visitor (double dispatch)
interface Shape
{
    public function accept(ShapeVisitor $visitor): float;
}

// Role: visitor contract — one method per concrete element type
interface ShapeVisitor
{
    public function visitCircle(Circle $circle): float;

    public function visitSquare(Square $square): float;
}

// Role: concrete elements — each dispatches to its own visit method
final readonly class Circle implements Shape
{
    public function __construct(public float $radius) {}

    public function accept(ShapeVisitor $visitor): float
    {
        return $visitor->visitCircle($this); // second dispatch
    }
}

final readonly class Square implements Shape
{
    public function __construct(public float $side) {}

    public function accept(ShapeVisitor $visitor): float
    {
        return $visitor->visitSquare($this);
    }
}

// Role: concrete visitor — one operation across all element types
final class AreaVisitor implements ShapeVisitor
{
    public function visitCircle(Circle $circle): float
    {
        return M_PI * $circle->radius ** 2;
    }

    public function visitSquare(Square $square): float
    {
        return $square->side ** 2;
    }
}

// usage — add a new operation by writing a new visitor, not editing shapes
$shapes = [new Circle(2.0), new Square(3.0)];
$area = new AreaVisitor();
foreach ($shapes as $shape) {
    printf('%.2f%s', $shape->accept($area), PHP_EOL);
}
```

**Trade-offs.**
- **Gains:** Add operations without touching element classes; gathers one operation's logic in one place; avoids `instanceof` chains.
- **Costs:** **Heavy** — double dispatch is verbose, and adding a *new element type* forces a change to every visitor. Elements must expose enough state to visitors, weakening encapsulation.
- **Skip it when:** Element types change more often than operations, or there are few element types — a `match(true)` on type, or plain methods on the elements, is far simpler. Visitor is **frequently overkill**; reach for it only for a genuinely stable element hierarchy with many growing operations (compilers/interpreters are the classic fit).

**Integrating.** Rare in application code. Shows up inside PHP-Parser (AST node visitors), Doctrine's SQL walkers, and query/expression compilers. Mostly framework-agnostic.

**Related / not to be confused with.** Unlike [Iterator](#iterator), which only traverses, Visitor performs *type-specific operations* during traversal. Where Strategy varies one algorithm, Visitor varies an algorithm *across a family of types*. If you only have one element type, you don't need a visitor.

## Interpreter

**Intent.** Given a language, define a representation for its grammar along with an interpreter that uses the representation to evaluate sentences in that language.

**Use when.**
- You have a small, stable, well-defined grammar to evaluate repeatedly (boolean rule expressions, simple arithmetic, a search/filter mini-language).
- Sentences map naturally to an abstract syntax tree of composable terminal/non-terminal expressions.
- The grammar is simple enough that a full parser generator would be overkill, yet recurs enough to justify structure.

**Structure.** An `Expression` interface with `interpret(Context)`. Terminal expressions evaluate leaves (literals, variables); non-terminal expressions combine sub-expressions (and, or, plus). The client builds the AST (by hand or from a parser) and calls `interpret()` on the root.

```php
<?php

declare(strict_types=1);

// Role: context holding variable bindings
final class Context
{
    /** @param array<string,bool> $values */
    public function __construct(private array $values = []) {}

    public function get(string $name): bool
    {
        return $this->values[$name] ?? false;
    }
}

// Role: abstract expression
interface Expression
{
    public function interpret(Context $context): bool;
}

// Role: terminal expression — a variable lookup
final readonly class Variable implements Expression
{
    public function __construct(private string $name) {}

    public function interpret(Context $context): bool
    {
        return $context->get($this->name);
    }
}

// Role: non-terminal expressions — combine sub-expressions
final readonly class AndExpression implements Expression
{
    public function __construct(
        private Expression $left,
        private Expression $right,
    ) {}

    public function interpret(Context $context): bool
    {
        return $this->left->interpret($context)
            && $this->right->interpret($context);
    }
}

final readonly class NotExpression implements Expression
{
    public function __construct(private Expression $expression) {}

    public function interpret(Context $context): bool
    {
        return ! $this->expression->interpret($context);
    }
}

// usage — build the AST for: admin AND NOT suspended
$rule = new AndExpression(
    new Variable('admin'),
    new NotExpression(new Variable('suspended')),
);
$context = new Context(['admin' => true, 'suspended' => false]);
var_dump($rule->interpret($context)); // true
```

**Trade-offs.**
- **Gains:** Grammar rules map one-to-one to classes; easy to extend the grammar with new expression types; the AST is composable.
- **Costs:** A class per grammar rule — explodes for anything but a tiny grammar; you still need a *parser* to build the AST from text, which Interpreter does not give you.
- **Skip it when:** **Almost always.** This pattern is rarely needed. For real parsing use a parser library (e.g. a PEG/lexer-parser); for composable business rules use [Specification](#specification); for config-driven behaviour use data + Strategy. Reach for Interpreter only for a genuinely tiny, stable grammar you control end to end.

**Integrating.** Essentially framework-agnostic and uncommon in application code. Symfony's ExpressionLanguage component is the pragmatic replacement when you think you want Interpreter.

**Related / not to be confused with.** Structurally it's [Composite](structural.md) (an expression tree) plus evaluation, and evaluation is often done with a [Visitor](#visitor). For yes/no business rules prefer [Specification](#specification), which is the same idea trimmed to composable predicates without a grammar.
