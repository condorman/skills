# Structural Patterns

Structural patterns compose objects and classes into larger structures while keeping those structures flexible, so you can change composition without rewriting the parts.

## Table of Contents

- [Adapter](#adapter)
- [Bridge](#bridge)
- [Composite](#composite)
- [Decorator](#decorator)
- [Facade](#facade)
- [Fluent Interface](#fluent-interface)
- [Flyweight](#flyweight)
- [Proxy](#proxy)
- [Registry](#registry)
- [Data Mapper](#data-mapper)
- [Repository](#repository)
- [Service Locator](#service-locator)

## Adapter

**Intent.** Convert the interface of a class into another interface clients expect, so classes with incompatible interfaces can work together.

**Use when.**
- A third-party payment SDK exposes `charge($cents)` but your app is written against a `PaymentGateway::pay(Money)` interface.
- You want to swap a vendor library without touching every call site — the adapter absorbs the difference.
- You are integrating legacy code whose method names/shapes you cannot change.
- You need two independently designed subsystems (yours + theirs) to interoperate.

**Structure.** A `Target` interface your code depends on; an `Adaptee` (the incompatible existing class); an `Adapter` that implements `Target` and translates each call into one or more `Adaptee` calls.

```php
<?php

declare(strict_types=1);

// Target — the interface the client programs against
interface PaymentGateway
{
    public function pay(int $amountInCents): string;
}

// Adaptee — an incompatible third-party SDK we cannot change
final class StripeSdk
{
    public function createCharge(float $dollars, string $currency): array
    {
        return ['id' => 'ch_123', 'amount' => $dollars, 'currency' => $currency];
    }
}

// Adapter — implements Target, translates to the Adaptee
final class StripeGatewayAdapter implements PaymentGateway
{
    public function __construct(private readonly StripeSdk $sdk) {}

    public function pay(int $amountInCents): string
    {
        $charge = $this->sdk->createCharge($amountInCents / 100, 'usd');
        return $charge['id'];
    }
}

// usage
function checkout(PaymentGateway $gateway): void
{
    echo $gateway->pay(1999), PHP_EOL; // ch_123
}

checkout(new StripeGatewayAdapter(new StripeSdk()));
```

**Trade-offs.**
- **Gains:** Decouples your code from vendor specifics; makes third-party swaps a one-class change; keeps a clean domain interface.
- **Costs:** One extra class and layer of indirection per adapted type; can hide a leaky mapping if the two interfaces disagree semantically.
- **Skip it when:** You control both sides and can just align the interfaces, or there is only ever one implementation and no interface boundary is warranted (YAGNI).

**Integrating.**
- **Laravel:** Bind the `Target` interface to the adapter in a service provider; the container injects it everywhere.
- **Symfony:** Register the adapter as a service aliased to the interface for autowiring.

**Related / not to be confused with.** Adapter changes an interface without changing behavior; **Facade** simplifies a whole subsystem behind a new, smaller interface; **Decorator** keeps the same interface but adds behavior; **Proxy** keeps the same interface but controls access. **Bridge** looks similar in code but is designed up front to vary two dimensions, whereas Adapter retrofits an existing mismatch.

## Bridge

**Intent.** Decouple an abstraction from its implementation so the two can vary independently.

**Use when.**
- You have a class hierarchy exploding along two axes — e.g. `Notification` types (Alert, Reminder) times `Channel` (Email, SMS, Push) — and refuse to write N×M subclasses.
- You want to switch the implementation at runtime (swap the rendering backend on a live object).
- Both the abstraction and its implementation should be extensible by subclassing independently.
- You are designing up front and know two dimensions will grow separately.

**Structure.** An `Abstraction` holds a reference to an `Implementor` interface and delegates the primitive work to it. `RefinedAbstraction`s extend the abstraction; `ConcreteImplementor`s implement the primitives. The two hierarchies meet only at the `Implementor` interface — the "bridge."

```php
<?php

declare(strict_types=1);

// Implementor — the "how it is delivered" axis
interface Channel
{
    public function deliver(string $message): void;
}

// Concrete Implementors
final class EmailChannel implements Channel
{
    public function deliver(string $message): void
    {
        echo "[email] {$message}", PHP_EOL;
    }
}

final class SmsChannel implements Channel
{
    public function deliver(string $message): void
    {
        echo "[sms] {$message}", PHP_EOL;
    }
}

// Abstraction — the "what is sent" axis, bridged to a Channel
abstract class Notification
{
    public function __construct(protected readonly Channel $channel) {}

    abstract public function send(string $to): void;
}

// Refined Abstractions
final class AlertNotification extends Notification
{
    public function send(string $to): void
    {
        $this->channel->deliver("ALERT for {$to}: system down");
    }
}

final class ReminderNotification extends Notification
{
    public function send(string $to): void
    {
        $this->channel->deliver("Reminder for {$to}: meeting at 3pm");
    }
}

// usage — mix any abstraction with any implementor, no N×M classes
(new AlertNotification(new SmsChannel()))->send('ops');
(new ReminderNotification(new EmailChannel()))->send('alice@example.com');
```

**Trade-offs.**
- **Gains:** Two hierarchies evolve independently; runtime swap of implementation; avoids combinatorial subclass explosion.
- **Costs:** More upfront indirection; harder to grasp than a flat hierarchy; premature if the second axis never materializes.
- **Skip it when:** Only one dimension actually varies — a plain interface or strategy is enough.

**Integrating.** No framework-specific wiring; it is plain composition. In any DI container, register the `Implementor` and inject it into the abstraction's constructor.

**Related / not to be confused with.** **Adapter** makes two *existing* incompatible interfaces work together after the fact; Bridge is planned up front to let two dimensions vary. Structurally both hold a reference and delegate, but the intent differs: Adapter reconciles, Bridge separates.

## Composite

**Intent.** Compose objects into tree structures and let clients treat individual objects and compositions uniformly.

**Use when.**
- You model a part-whole hierarchy — a filesystem of files and folders, a UI of widgets and panels, nested order line-items.
- Client code should not care whether it holds a leaf or a branch; it calls the same method on both.
- You need a recursive operation (total size, render, price) that folds over the whole tree.
- The nesting depth is arbitrary and open-ended.

**Structure.** A `Component` interface declares the shared operation. `Leaf` implements it directly. `Composite` holds children (each a `Component`) and implements the operation by delegating to and aggregating over its children.

```php
<?php

declare(strict_types=1);

// Component — common interface for leaves and composites
interface FileSystemNode
{
    public function size(): int;
}

// Leaf
final class File implements FileSystemNode
{
    public function __construct(
        public readonly string $name,
        private readonly int $bytes,
    ) {}

    public function size(): int
    {
        return $this->bytes;
    }
}

// Composite — holds children and aggregates over them
final class Directory implements FileSystemNode
{
    /** @var FileSystemNode[] */
    private array $children = [];

    public function __construct(public readonly string $name) {}

    public function add(FileSystemNode $node): self
    {
        $this->children[] = $node;
        return $this;
    }

    public function size(): int
    {
        return array_sum(array_map(
            static fn (FileSystemNode $child): int => $child->size(),
            $this->children,
        ));
    }
}

// usage — leaves and composites answer size() identically
$root = (new Directory('root'))
    ->add(new File('a.txt', 100))
    ->add((new Directory('sub'))->add(new File('b.txt', 250)));

echo $root->size(), PHP_EOL; // 350
```

**Trade-offs.**
- **Gains:** Uniform client code; trivial to add new node types; recursion is encapsulated in the composite.
- **Costs:** The shared interface can become overly general (leaf-only methods leak onto branches); can make type constraints hard to enforce.
- **Skip it when:** The structure is flat or fixed-depth — a simple array/loop is clearer than a tree abstraction.

**Integrating.** Symfony's Form component and console command trees are composites; you rarely hand-roll this in a framework, but domain trees (nested categories, org charts) are a natural fit.

**Related / not to be confused with.** **Decorator** also has a recursive-looking structure but wraps a single component to add behavior; Composite groups many children to represent a whole. A Decorator is a one-child composite in shape only — its intent is augmentation, not aggregation.

## Decorator

**Intent.** Attach additional responsibilities to an object dynamically, providing a flexible alternative to subclassing for extending behavior.

**Use when.**
- You need to layer optional behaviors — a data stream that can be gzip-compressed, then encrypted, then logged — in any combination and order.
- Subclassing would explode (`GzipEncryptedLoggedStream`, `EncryptedLoggedStream`, ...) for every combination.
- You want to add behavior at runtime to specific instances, not the whole class.
- The added behavior wraps the same interface — callers should not know decoration happened.

**Structure.** A `Component` interface; a `ConcreteComponent` (the base object); a `Decorator` that implements `Component` and holds a wrapped `Component`, forwarding calls and adding behavior before/after. Multiple decorators nest.

```php
<?php

declare(strict_types=1);

// Component — shared interface
interface TextRenderer
{
    public function render(): string;
}

// Concrete Component — the base behavior
final class PlainText implements TextRenderer
{
    public function __construct(private readonly string $text) {}

    public function render(): string
    {
        return $this->text;
    }
}

// Base Decorator — same interface, wraps a Component
abstract class TextDecorator implements TextRenderer
{
    public function __construct(protected readonly TextRenderer $inner) {}
}

// Concrete Decorators — ADD responsibilities
final class UpperCaseDecorator extends TextDecorator
{
    public function render(): string
    {
        return strtoupper($this->inner->render());
    }
}

final class ExclaimDecorator extends TextDecorator
{
    public function render(): string
    {
        return $this->inner->render() . '!!!';
    }
}

// usage — stack decorators in any order
$text = new ExclaimDecorator(new UpperCaseDecorator(new PlainText('hello')));
echo $text->render(), PHP_EOL; // HELLO!!!
```

**Trade-offs.**
- **Gains:** Compose behaviors freely at runtime; each concern is a small single-purpose class; avoids subclass combinatorics.
- **Costs:** Many small classes; deep wrapping is hard to debug (long stack of delegations); identity checks (`instanceof` the concrete) break through the wrapper.
- **Skip it when:** There is exactly one fixed behavior or the combinations never vary — just put the code in the class.

**Integrating.**
- **Laravel/Symfony:** Middleware pipelines are decorator-like; a decorated service can be registered by binding the interface to a factory that wraps the base service. Symfony has explicit service decoration (`decorates:`).
- **PSR-7/PSR-15:** HTTP middleware wrapping a handler is a decorator chain.

**Related / not to be confused with.** **Proxy** shares the same-interface-wrapping shape but CONTROLS access (lazy-load, auth, cache) rather than adding domain responsibilities. **Adapter** changes the interface; Decorator keeps it. **Composite** aggregates many children; Decorator wraps exactly one. Rule of thumb: Decorator *adds*, Proxy *controls*, Adapter *converts*, Facade *simplifies*.

## Facade

**Intent.** Provide a unified, simplified interface to a set of interfaces in a subsystem, making the subsystem easier to use.

**Use when.**
- A common task requires orchestrating several low-level classes (open file, parse, validate, transform, persist) and callers keep repeating that dance.
- You want a simple entry point for the 80% use case while leaving the subsystem accessible for the 20%.
- You are wrapping a messy or sprawling library behind a small, task-focused API.
- You want to reduce coupling between clients and many subsystem classes.

**Structure.** A `Facade` class holds/creates the subsystem objects and exposes a few high-level methods that coordinate them. Clients talk only to the facade; the subsystem classes stay usable directly.

```php
<?php

declare(strict_types=1);

// Subsystem classes — each does one low-level job
final class VideoDecoder
{
    public function decode(string $file): string
    {
        return "raw({$file})";
    }
}

final class Transcoder
{
    public function toFormat(string $raw, string $format): string
    {
        return "{$raw}.{$format}";
    }
}

// Facade — one simple method orchestrating the subsystem
final class MediaConverter
{
    public function __construct(
        private readonly VideoDecoder $decoder = new VideoDecoder(),
        private readonly Transcoder $transcoder = new Transcoder(),
    ) {}

    public function convert(string $file, string $format): string
    {
        $raw = $this->decoder->decode($file);
        return $this->transcoder->toFormat($raw, $format);
    }
}

// usage — caller ignores the subsystem entirely
echo (new MediaConverter())->convert('clip.mov', 'mp4'), PHP_EOL; // raw(clip.mov).mp4
```

**Trade-offs.**
- **Gains:** Slashes coupling and boilerplate at call sites; gives newcomers an obvious entry point; lets you refactor the subsystem behind a stable API.
- **Costs:** Can grow into a god-object if it accretes responsibilities; hides capability, so power users may fight it.
- **Skip it when:** The subsystem is already one or two simple calls — a facade just adds a hop.

**Integrating.**
- **Laravel:** "Facades" (`Cache::get()`) are a *different* thing — static proxies to container services, not the GoF facade. The GoF facade is just a plain coordinating class.
- **WordPress:** Wrapping several `wp_*` functions behind one service class is a classic facade.

**Related / not to be confused with.** **Adapter** makes an incompatible interface usable (one class, interface conversion); Facade simplifies *many* classes behind a new, smaller interface (no requirement to match an existing one). Facade does not hide the subsystem — it just offers an easier road; **Proxy** stands in for one object and controls access to it.

## Fluent Interface

**Intent.** Provide a readable, chainable API by having methods return the object (or a context) so calls read like prose.

**Use when.**
- You build up a complex object or query step by step — `$query->select('id')->from('users')->where('active', true)`.
- You want configuration/construction code to read declaratively and left-to-right.
- A builder accumulates optional settings and you want to avoid a telescoping constructor or a bag of setters called separately.
- The order of calls is flexible and readability at the call site matters.

**Structure.** Each configuring method mutates (or returns a new) state and `return $this` (mutable) or `return new self(...)` (immutable). A terminal method returns the finished product.

```php
<?php

declare(strict_types=1);

// Fluent builder — each step returns $this for chaining
final class QueryBuilder
{
    private string $table = '';
    /** @var string[] */
    private array $columns = ['*'];
    /** @var string[] */
    private array $conditions = [];

    public function select(string ...$columns): self
    {
        $this->columns = $columns ?: ['*'];
        return $this;
    }

    public function from(string $table): self
    {
        $this->table = $table;
        return $this;
    }

    public function where(string $condition): self
    {
        $this->conditions[] = $condition;
        return $this;
    }

    // Terminal method — produces the result
    public function build(): string
    {
        $sql = 'SELECT ' . implode(', ', $this->columns) . " FROM {$this->table}";

        if ($this->conditions !== []) {
            $sql .= ' WHERE ' . implode(' AND ', $this->conditions);
        }
        return $sql;
    }
}

// usage — reads like a sentence
echo (new QueryBuilder())
    ->select('id', 'email')
    ->from('users')
    ->where('active = 1')
    ->build(), PHP_EOL;
// SELECT id, email FROM users WHERE active = 1
```

**Trade-offs.**
- **Gains:** Highly readable call sites; discoverable API via IDE autocomplete; natural for builders and query DSLs.
- **Costs:** Harder to debug (one long expression, unclear where it failed); mutable chaining can surprise if the object is shared; encourages doing too much in one statement.
- **Skip it when:** The object has two or three fields — a constructor or named arguments (`new Point(x: 1, y: 2)`) is clearer.

**Integrating.** Query builders in Laravel (Eloquent), Doctrine (`QueryBuilder`), and Symfony all use this. When building your own, prefer returning immutable copies for shared/config objects to avoid aliasing bugs.

**Related / not to be confused with.** Fluent Interface is a *style*, often paired with the **Builder** creational pattern. Builder is about constructing a complex object step by step; fluency is just how the steps read. You can have a Builder without fluency, and fluency on non-builders.

## Flyweight

**Intent.** Use sharing to support large numbers of fine-grained objects efficiently by separating intrinsic (shared) from extrinsic (per-use) state.

**Use when.**
- You are about to create millions of nearly identical objects — characters in a document, tiles on a map, particles — and memory is the constraint.
- Much of each object's state is identical across instances (the *intrinsic* part: glyph shape, tile texture) and can be shared.
- The varying part (the *extrinsic* part: position, color at a spot) can be passed in per operation instead of stored.
- Object identity does not matter — two "same" flyweights are interchangeable.

**Structure.** A `Flyweight` stores intrinsic state and takes extrinsic state as method arguments. A `FlyweightFactory` caches and returns shared instances keyed by intrinsic state so each distinct value exists once.

```php
<?php

declare(strict_types=1);

// Flyweight — stores only shared (intrinsic) state
final class Glyph
{
    public function __construct(public readonly string $char) {}

    // extrinsic state (position) is passed in, not stored
    public function renderAt(int $x, int $y): string
    {
        return "'{$this->char}' at ({$x},{$y})";
    }
}

// Flyweight Factory — guarantees one instance per intrinsic value
final class GlyphFactory
{
    /** @var array<string, Glyph> */
    private array $pool = [];

    public function get(string $char): Glyph
    {
        return $this->pool[$char] ??= new Glyph($char);
    }

    public function count(): int
    {
        return count($this->pool);
    }
}

// usage — "mississippi" reuses 4 shared glyphs, not 11 objects
$factory = new GlyphFactory();
$positions = [];
foreach (str_split('mississippi') as $i => $char) {
    $positions[] = $factory->get($char)->renderAt($i, 0);
}

echo $factory->count(), PHP_EOL; // 4  (m, i, s, p)
```

**Trade-offs.**
- **Gains:** Dramatic memory savings when the object count is huge and intrinsic state repeats.
- **Costs:** Complexity of splitting state; extrinsic state must be threaded through every call; premature optimization if counts are modest.
- **Skip it when:** You have thousands (not millions) of objects, or the objects are mostly unique — modern PHP memory rarely justifies it. Measure first.

**Integrating.** Rarely needed in typical web request/response apps (short-lived processes). Relevant in long-running workers, image/tile processing, or game/simulation loops.

**Related / not to be confused with.** Like a cache-backed **Factory**, but the point is *sharing immutable instances*, not just building them. Distinct from **Object Pool**, which reuses *mutable* objects and hands ownership back and forth; flyweights are immutable and freely shared.

## Proxy

**Intent.** Provide a surrogate or placeholder for another object to control access to it.

**Use when.**
- You want lazy initialization — a heavy `Report` object should only load its data when first read (virtual proxy).
- You need to add access control/authorization checks in front of a real object without changing it (protection proxy).
- You want transparent caching, logging, or rate-limiting around calls to a real service.
- The real object is remote and you want a local stand-in that hides the network (remote proxy).

**Structure.** A `Subject` interface implemented by both the `RealSubject` and the `Proxy`. The proxy holds a reference to (or lazily creates) the real subject and forwards calls, interposing control logic. Callers cannot tell the difference.

```php
<?php

declare(strict_types=1);

// Subject — shared interface, so the proxy is transparent
interface ImageLoader
{
    public function display(): string;
}

// Real Subject — expensive to create
final class HighResImage implements ImageLoader
{
    public function __construct(private readonly string $path)
    {
        // pretend this reads megabytes from disk
    }

    public function display(): string
    {
        return "showing {$this->path}";
    }
}

// Proxy — CONTROLS access: defers the costly load until needed
final class LazyImageProxy implements ImageLoader
{
    private ?HighResImage $real = null;

    public function __construct(private readonly string $path) {}

    public function display(): string
    {
        // create the real subject only on first use
        $this->real ??= new HighResImage($this->path);
        return $this->real->display();
    }
}

// usage — construction is cheap; loading happens on display()
$image = new LazyImageProxy('photo.raw');
echo $image->display(), PHP_EOL; // showing photo.raw (loaded now)
```

**Trade-offs.**
- **Gains:** Adds access control/laziness/caching transparently; the real object stays focused on its job; callers are unaffected.
- **Costs:** Extra indirection; a proxy that silently changes timing/behavior can surprise; can mask performance problems it was meant to solve.
- **Skip it when:** The real object is cheap and always needed — lazy loading buys nothing but a layer.

**Integrating.**
- **Doctrine:** Lazy-loaded entity associations are implemented with generated proxy classes.
- **Symfony:** Lazy services use proxies (ocramius/proxy-manager) to defer instantiation.
- **Laravel:** Deferred/lazy container bindings play a similar role.

**Related / not to be confused with.** **Decorator** and Proxy both implement the wrapped object's interface. The difference is intent: Decorator ADDS responsibilities (new behavior callers opt into); Proxy CONTROLS access to the same behavior (when/whether/who). **Adapter** changes the interface; **Facade** wraps many objects. A proxy typically manages the lifecycle of its real subject; a decorator is handed an already-built one.

## Registry

**Intent.** Provide a well-known global object that other objects use to find common services and objects by name.

**Use when.**
- You genuinely need one shared point of access to a small set of objects across an app (and cannot thread them through) — this is the *narrow* legitimate case.
- You are working in a legacy or procedural codebase where dependency injection is not yet feasible, and you need a controlled seam.
- You are caching lookups that are unambiguously process-global and read-mostly (e.g. a config registry populated once at boot).

**Structure.** A class with static (or singleton) storage exposing `set(key, value)` and `get(key)`. Everyone reads/writes the same store. Because it is global mutable state, keep it read-mostly and populate it in one place.

```php
<?php

declare(strict_types=1);

// Registry — global, well-known store keyed by name.
// WARNING: this is global mutable state; prefer DI (see trade-offs).
final class Registry
{
    /** @var array<string, object> */
    private static array $store = [];

    public static function set(string $key, object $value): void
    {
        self::$store[$key] = $value;
    }

    public static function get(string $key): object
    {
        return self::$store[$key]
            ?? throw new \OutOfBoundsException("No entry for '{$key}'");
    }

    public static function has(string $key): bool
    {
        return isset(self::$store[$key]);
    }
}

final class Clock
{
    public function now(): string
    {
        return '2026-07-08';
    }
}

// usage — populate once at boot, read anywhere
Registry::set('clock', new Clock());
/** @var Clock $clock */
$clock = Registry::get('clock');
echo $clock->now(), PHP_EOL; // 2026-07-08
```

**Trade-offs.**
- **Gains:** Trivial global access; no wiring; handy as a temporary seam in legacy code.
- **Costs:** Hides dependencies (a class's needs are invisible in its signature); global mutable state makes tests order-dependent and hard to isolate; encourages hidden coupling.
- **Skip it when:** Almost always in new code. Prefer **Dependency Injection** — pass what a class needs through its constructor so dependencies are explicit and testable.

**Integrating.** Frameworks provide a proper alternative: use the **service container** (Laravel, Symfony) and inject dependencies rather than reaching into a global registry. Reserve a hand-rolled registry for bridging legacy code toward DI.

**Related / not to be confused with.** **Service Locator** is a registry you *ask for services* (often typed lookups); **Singleton** ensures one instance of a *specific* class, whereas a Registry holds *many* named objects. All three are global-state patterns with the same core downside — hidden dependencies — and DI is the preferred alternative to each.

## Data Mapper

**Intent.** Move data between objects and a database while keeping the objects (and the database) independent of each other and of the mapper.

**Use when.**
- Your domain objects should be *persistence-ignorant* — a `User` entity has no idea a database exists, no `save()` method, no SQL.
- You want to test domain logic without a database, and swap storage without touching entities.
- The mapping between object shape and table shape is nontrivial (different names, computed fields, value objects).
- You are following DDD or a clean-architecture separation between domain and infrastructure.

**Structure.** A plain `Entity` (no persistence code); a `Mapper` that knows how to build entities from rows and rows from entities, and owns all DB access (`find`, `insert`, `update`). The entity never references the mapper.

```php
<?php

declare(strict_types=1);

// Entity — persistence-ignorant; no DB, no save()
final class User
{
    public function __construct(
        public readonly int $id,
        public string $email,
    ) {}
}

// Data Mapper — the only thing that knows how User maps to rows.
// The array stands in for a real DB connection.
final class UserMapper
{
    /** @var array<int, array{id:int,email:string}> */
    private array $rows = [];

    public function find(int $id): ?User
    {
        $row = $this->rows[$id] ?? null;

        // row -> entity translation lives here, not in User
        return $row === null ? null : new User($row['id'], $row['email']);
    }

    public function save(User $user): void
    {
        // entity -> row translation lives here, not in User
        $this->rows[$user->id] = ['id' => $user->id, 'email' => $user->email];
    }
}

// usage
$mapper = new UserMapper();
$mapper->save(new User(1, 'alice@example.com'));
echo $mapper->find(1)?->email, PHP_EOL; // alice@example.com
```

**Trade-offs.**
- **Gains:** Domain stays pure and testable; storage and object model evolve independently; complex mappings are centralized.
- **Costs:** More classes and ceremony than Active Record; you write/maintain mapping code (or lean on an ORM that does).
- **Skip it when:** Simple CRUD apps where the table *is* the model — Active Record is faster to write.

**Integrating.**
- **Doctrine ORM IS a Data Mapper:** entities are plain PHP objects; the `EntityManager` and metadata do the mapping; entities have no `save()`.
- **Eloquent (Laravel) is Active Record**, the *contrast*: the model extends a base class and carries its own `save()`/`find()`, coupling the object to persistence.
- **CodeIgniter 4:** its Model class is closer to a table gateway/Active-Record-ish helper, not a pure Data Mapper.

**Related / not to be confused with.** **Active Record** puts persistence *on* the object (`$user->save()`), coupling domain and DB; Data Mapper keeps them apart. **Repository** is a higher-level *collection* abstraction that often sits *on top of* a mapper — the mapper does row<->object translation, the repository offers `findByEmail()`-style domain queries.

## Repository

**Intent.** Mediate between the domain and data-mapping layers using a collection-like interface for accessing domain objects.

**Use when.**
- You want domain/application code to say `$users->add($u)` or `$users->ofEmail($e)` and never see SQL, query builders, or ORM specifics.
- You want to express queries in domain language (`activeSubscribers()`, `overdueInvoices()`) behind a stable interface.
- You want to swap the backing store (DB, in-memory, HTTP API) in tests or across environments by swapping the repository implementation.
- You are layering a clean boundary between application services and persistence.

**Structure.** A `Repository` interface phrased as a collection of domain objects (`add`, `remove`, `findById`, domain finders). A concrete implementation fulfills it using a data mapper / ORM / query builder underneath. Application code depends only on the interface.

```php
<?php

declare(strict_types=1);

final class Product
{
    public function __construct(
        public readonly string $sku,
        public readonly string $name,
        public readonly int $priceCents,
    ) {}
}

// Repository interface — a collection of domain objects, no storage detail
interface ProductRepository
{
    public function add(Product $product): void;

    public function ofSku(string $sku): ?Product;

    /** @return Product[] */
    public function cheaperThan(int $cents): array;
}

// Concrete implementation — could wrap a mapper/ORM; in-memory here
final class InMemoryProductRepository implements ProductRepository
{
    /** @var array<string, Product> */
    private array $products = [];

    public function add(Product $product): void
    {
        $this->products[$product->sku] = $product;
    }

    public function ofSku(string $sku): ?Product
    {
        return $this->products[$sku] ?? null;
    }

    public function cheaperThan(int $cents): array
    {
        return array_values(array_filter(
            $this->products,
            static fn (Product $p): bool => $p->priceCents < $cents,
        ));
    }
}

// usage — application code depends on the interface only
function listBargains(ProductRepository $repo): array
{
    return $repo->cheaperThan(1000);
}

$repo = new InMemoryProductRepository();
$repo->add(new Product('A1', 'Pen', 500));
$repo->add(new Product('B2', 'Desk', 20000));
echo count(listBargains($repo)), PHP_EOL; // 1
```

**Trade-offs.**
- **Gains:** Domain speaks its own language; storage is swappable; queries are named and reusable; excellent for testing with an in-memory implementation.
- **Costs:** Another layer over the ORM; risk of anemic pass-through repositories that just wrap the ORM one-to-one; interface can bloat with ad-hoc finders.
- **Skip it when:** A thin app where the ORM's own query API is already your data-access layer — wrapping Eloquent in a repository often adds ceremony without payoff.

**Integrating.**
- **Doctrine:** ships first-class repositories (`EntityRepository`, `#[ORM\Entity(repositoryClass: ...)]`) sitting on top of its data mapper — the canonical pairing.
- **Laravel:** no built-in repository; teams add one over Eloquent when they want to hide Active Record behind a domain interface (debated as often-unnecessary).
- **Symfony:** Doctrine repositories are the norm; inject the interface and bind it to the concrete repo.

**Related / not to be confused with.** **Data Mapper** does the low-level object<->row translation; **Repository** is the collection-like facade *above* it that application code talks to (a repository often uses a mapper internally). **Active Record** collapses both concerns onto the entity itself. Repository is about *querying/collection semantics*; Data Mapper is about *persistence mechanics*.

## Service Locator

**Intent.** Provide a central registry that returns service instances on request, decoupling clients from concrete construction.

**Use when.**
- You are maintaining legacy code without constructor injection and need a controlled central place to fetch services — the *narrow* legitimate case.
- A plugin/extension boundary must resolve services by name at runtime where compile-time wiring is impossible.
- You are inside framework internals implementing the container itself (the locator is the mechanism DI is built on).

**Structure.** A `ServiceLocator` maps identifiers to instances or factories and returns them via `get(id)`. Clients call the locator to *pull* dependencies, instead of having them *pushed* in via the constructor.

```php
<?php

declare(strict_types=1);

interface Logger
{
    public function log(string $message): void;
}

final class EchoLogger implements Logger
{
    public function log(string $message): void
    {
        echo "[log] {$message}", PHP_EOL;
    }
}

// Service Locator — clients PULL dependencies by id.
// WARNING: hides dependencies; prefer injecting them (see trade-offs).
final class ServiceLocator
{
    /** @var array<string, callable():object> */
    private array $factories = [];
    /** @var array<string, object> */
    private array $instances = [];

    public function register(string $id, callable $factory): void
    {
        $this->factories[$id] = $factory;
    }

    public function get(string $id): object
    {
        return $this->instances[$id] ??= ($this->factories[$id]
            ?? throw new \OutOfBoundsException("Unknown service '{$id}'"))();
    }
}

// usage
$locator = new ServiceLocator();
$locator->register('logger', static fn (): Logger => new EchoLogger());

// A client reaching into the locator — its real dependency (Logger) is hidden
/** @var Logger $logger */
$logger = $locator->get('logger');
$logger->log('service located'); // [log] service located
```

**Trade-offs.**
- **Gains:** Central construction; runtime resolution by name; a pragmatic seam in code that cannot yet do constructor injection.
- **Costs:** Hides real dependencies — a class's constructor no longer tells you what it needs; makes testing harder (must configure the locator); often called an anti-pattern for exactly this reason.
- **Skip it when:** Almost always in application code. Prefer **Dependency Injection**: let the container *inject* services into constructors so dependencies are explicit. Use a locator only inside infrastructure or legacy seams.

**Integrating.**
- **Symfony:** provides a scoped `ServiceLocator` for the legitimate lazy/named case (e.g. `#[TaggedIterator]`, service-subscriber pattern) — deliberately narrow, not the default.
- **Laravel:** `app('service')` / facades are service-locator-style access; idiomatic app code should prefer constructor injection instead.

**Related / not to be confused with.** **Dependency Injection** is the inversion of Service Locator: DI *pushes* dependencies in (explicit, testable); the locator makes clients *pull* them (hidden). **Registry** is the more general "named global store"; a Service Locator is a registry specialized for resolving *services* (often with factories/typing). **Singleton** guarantees one instance of one class. All three share global-state pitfalls — reach for DI first.
