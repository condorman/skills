# Creational Patterns

Creational patterns abstract the instantiation process, decoupling *what* a client needs from *how* concrete objects get built, selected, or reused.

## Table of Contents

- [Abstract Factory](#abstract-factory)
- [Builder](#builder)
- [Factory Method](#factory-method)
- [Pool](#pool)
- [Prototype](#prototype)
- [Simple Factory](#simple-factory)
- [Static Factory](#static-factory)
- [Singleton](#singleton)
- [Dependency Injection](#dependency-injection)

## Abstract Factory

**Intent.** Provide an interface for creating *families* of related objects without specifying their concrete classes.

**Use when.**
- You must create a matched set of objects that only make sense together (a MySQL connection + MySQL query builder, never mixed with Postgres ones).
- The whole family must swap as a unit based on one runtime choice (driver, cloud provider, UI theme).
- You want the type system to guarantee clients cannot combine incompatible parts.
- The concrete product classes should stay hidden behind interfaces.

**Structure.** An *abstract factory* interface declares one creator method per product type. Each *concrete factory* returns a coherent family of *concrete products* conforming to shared *product interfaces*. Clients depend only on the abstract factory and product interfaces.

```php
<?php

declare(strict_types=1);

// Product interfaces — the family contract
interface Connection
{
    public function dsn(): string;
}

interface QueryBuilder
{
    public function limit(string $sql, int $n): string;
}

// Abstract factory — declares the family
interface DatabaseFactory
{
    public function createConnection(): Connection;
    public function createQueryBuilder(): QueryBuilder;
}

// Concrete products — MySQL family
final class MySqlConnection implements Connection
{
    public function dsn(): string
    {
        return 'mysql:host=localhost';
    }
}

final class MySqlQueryBuilder implements QueryBuilder
{
    public function limit(string $sql, int $n): string
    {
        return "$sql LIMIT $n";
    }
}

// Concrete products — Postgres family
final class PostgresConnection implements Connection
{
    public function dsn(): string
    {
        return 'pgsql:host=localhost';
    }
}

final class PostgresQueryBuilder implements QueryBuilder
{
    public function limit(string $sql, int $n): string
    {
        return "$sql FETCH FIRST $n ROWS ONLY";
    }
}

// Concrete factories — each builds one coherent family
final class MySqlFactory implements DatabaseFactory
{
    public function createConnection(): Connection
    {
        return new MySqlConnection();
    }

    public function createQueryBuilder(): QueryBuilder
    {
        return new MySqlQueryBuilder();
    }
}

final class PostgresFactory implements DatabaseFactory
{
    public function createConnection(): Connection
    {
        return new PostgresConnection();
    }

    public function createQueryBuilder(): QueryBuilder
    {
        return new PostgresQueryBuilder();
    }
}

// usage — client works against one family, never mixing drivers
function report(DatabaseFactory $factory): string
{
    $sql = $factory->createQueryBuilder()->limit('SELECT *', 10);

    return $factory->createConnection()->dsn() . ' | ' . $sql;
}

echo report(new MySqlFactory()), PHP_EOL;
echo report(new PostgresFactory()), PHP_EOL;
```

**Trade-offs.**
- **Gains:** Enforces consistency across a product family; swapping the whole family is a one-line change; concrete classes stay hidden.
- **Costs:** High class count; adding a *new product type* to the family forces a change to every factory and the interface.
- **Skip it when:** You only vary one product, not a family — a Simple Factory or Factory Method is lighter.

**Integrating.** Laravel: bind the abstract factory in a service provider and resolve the family through the container. Symfony: register concrete factories as services and autowire the interface. CodeIgniter 4: expose each family via a `Services` method. Custom: pick the concrete factory in the composition root.

**Related / not to be confused with.** Factory Method makes one product chosen by subclassing; Abstract Factory makes *several related products*. Unlike Builder, it produces objects in single calls, not step by step.

## Builder

**Intent.** Separate the construction of a complex object from its representation so the same process can produce different results.

**Use when.**
- An object needs many optional or ordered construction steps (an HTTP request with headers, body, timeout, auth).
- You want to avoid a telescoping constructor with 8+ positional arguments.
- The same build sequence should yield different products (an `HtmlReport` vs a `PdfReport`).
- You want a readable fluent API producing a validated, immutable result at `build()`.

**Structure.** A *builder* exposes step methods that accumulate state plus a `build()` returning the finished *product*. An optional *director* encapsulates a canonical build sequence. Fluent builders return `$this`.

```php
<?php

declare(strict_types=1);

// Product — immutable once built
final readonly class HttpRequest
{
    /** @param array<string, string> $headers */
    public function __construct(
        public string $method,
        public string $url,
        public array $headers,
        public ?string $body,
    ) {
    }
}

interface RequestBuilder
{
    public function withHeader(string $name, string $value): static;
    public function withBody(string $body): static;
    public function build(): HttpRequest;
}

// Concrete builder — accumulates state, validates at build()
final class JsonRequestBuilder implements RequestBuilder
{
    /** @var array<string, string> */
    private array $headers = ['Accept' => 'application/json'];
    private ?string $body = null;

    public function __construct(
        private readonly string $method,
        private readonly string $url,
    ) {
    }

    public function withHeader(string $name, string $value): static
    {
        $this->headers[$name] = $value;
        return $this;
    }

    public function withBody(string $body): static
    {
        $this->body = $body;
        $this->headers['Content-Type'] = 'application/json';
        return $this;
    }

    public function build(): HttpRequest
    {
        return new HttpRequest($this->method, $this->url, $this->headers, $this->body);
    }
}

// usage
$request = (new JsonRequestBuilder('POST', 'https://api.test/users'))
    ->withHeader('Authorization', 'Bearer xyz')
    ->withBody('{"name":"Ada"}')
    ->build();

echo $request->method, ' ', $request->url, PHP_EOL;
```

**Trade-offs.**
- **Gains:** Readable step-by-step construction; keeps the product immutable; isolates complex assembly and validation.
- **Costs:** Extra builder class per product; overkill for objects with few fields.
- **Skip it when:** A named constructor or promoted properties with defaults already reads clearly — YAGNI.

**Integrating.** Mostly framework-agnostic. Laravel's query and mail builders and Symfony's `FormBuilder` follow this pattern; you rarely register a builder in a container since it holds per-call state.

**Related / not to be confused with.** Builder assembles *one* object over many steps; Abstract Factory returns a *family* in single calls. Unlike a Factory, the client drives the steps and their order.

## Factory Method

**Intent.** Define an interface for creating an object, but let subclasses decide which class to instantiate.

**Use when.**
- A base class defines a workflow but each subclass must supply its own product (a `Logger` base whose subclasses create `FileWriter` vs `SyslogWriter`).
- The creating code and the created type should vary together through inheritance.
- You want a hook subclasses override to customize *what* gets built without touching the surrounding algorithm.
- The concrete product isn't known until a subclass is chosen.

**Structure.** An abstract *creator* declares an abstract `factoryMethod()` returning a *product* interface and usually contains logic that uses that product. *Concrete creators* override the factory method to return specific *concrete products*.

```php
<?php

declare(strict_types=1);

interface Notification
{
    public function send(string $message): string;
}

// Concrete products
final class EmailNotification implements Notification
{
    public function send(string $message): string
    {
        return 'Email: ' . $message;
    }
}

final class SmsNotification implements Notification
{
    public function send(string $message): string
    {
        return 'SMS: ' . $message;
    }
}

// Creator — defines the workflow, defers the product to subclasses
abstract class NotificationService
{
    abstract protected function createNotification(): Notification; // the hook

    public function notify(string $message): string
    {
        return $this->createNotification()->send(strtoupper($message));
    }
}

// Concrete creators
final class EmailService extends NotificationService
{
    protected function createNotification(): Notification
    {
        return new EmailNotification();
    }
}

final class SmsService extends NotificationService
{
    protected function createNotification(): Notification
    {
        return new SmsNotification();
    }
}

// usage
echo (new EmailService())->notify('hi'), PHP_EOL;
echo (new SmsService())->notify('hi'), PHP_EOL;
```

**Trade-offs.**
- **Gains:** Adds new product variants by subclassing without editing existing creators; keeps creation and use cohesive.
- **Costs:** Requires a class hierarchy; one subclass per variant can proliferate.
- **Skip it when:** Selection is a simple runtime `match` on a value — a Simple Factory is more direct.

**Integrating.** Symfony/Laravel: the abstract creator is a normal service; subclasses register as separate services. CodeIgniter 4: expose each concrete creator via `Services`. Nothing framework-specific beyond ordinary DI.

**Related / not to be confused with.** Factory Method uses *inheritance* (one product, chosen by subclass). Abstract Factory uses *composition* for a *family*. Simple Factory centralizes a `match` in one method and is not a true GoF pattern.

## Pool

**Intent.** Reuse a set of pre-initialized, expensive-to-create objects instead of allocating and destroying them repeatedly.

**Use when.**
- Object creation is costly and frequent (database connections, workers, large buffers, TCP sockets).
- You need to cap the number of live instances of a scarce resource.
- Instances are interchangeable and safe to reset and hand back out.
- Acquire/release lifecycles are short and bursty, so churn dominates.

**Structure.** A *pool* holds reusable *products*. `acquire()` returns a free instance (creating one if none is free and under the cap); `release()` returns it for reuse. Clients borrow and return rather than `new`.

```php
<?php

declare(strict_types=1);

// Reusable product
final class Worker
{
    private static int $counter = 0;
    public readonly int $id;

    public function __construct()
    {
        $this->id = ++self::$counter; // stands in for expensive setup
    }

    public function run(string $job): string
    {
        return "worker {$this->id} ran {$job}";
    }
}

final class WorkerPool
{
    /** @var list<Worker> */
    private array $free = [];
    /** @var array<int, Worker> */
    private array $inUse = [];

    public function __construct(private readonly int $max = 2)
    {
    }

    public function acquire(): Worker
    {
        $worker = array_pop($this->free) ?? $this->make();
        $this->inUse[spl_object_id($worker)] = $worker;

        return $worker;
    }

    public function release(Worker $worker): void
    {
        unset($this->inUse[spl_object_id($worker)]);
        $this->free[] = $worker; // returned for reuse
    }

    private function make(): Worker
    {
        if (count($this->inUse) >= $this->max) {
            throw new RuntimeException('Pool exhausted');
        }

        return new Worker();
    }
}

// usage
$pool = new WorkerPool(max: 2);
$a = $pool->acquire();
echo $a->run('build'), PHP_EOL;
$pool->release($a);
echo $pool->acquire()->run('deploy'), PHP_EOL; // reuses the same instance
```

**Trade-offs.**
- **Gains:** Amortizes expensive construction; bounds resource usage; smooths latency under bursts.
- **Costs:** You must reset borrowed state carefully; leaked (never-released) objects starve the pool; adds lifecycle bookkeeping.
- **Skip it when:** Objects are cheap, or your runtime/driver already pools (PDO persistent connections, PHP-FPM per-request lifecycle).

**Integrating.** Rarely needed in classic PHP-FPM (process-per-request). Relevant in long-running runtimes: Swoole/RoadRunner/Laravel Octane connection and worker pools; otherwise a plain service.

**Related / not to be confused with.** Not a Singleton — a Pool holds *many* interchangeable instances and lends ownership back and forth. Not Flyweight, which *shares* immutable state rather than lending exclusive instances.

## Prototype

**Intent.** Create new objects by cloning an existing configured instance rather than instantiating from scratch.

**Use when.**
- Constructing an object is expensive but you already have a suitable configured example (a pre-loaded template, a parsed document).
- You need many near-identical objects that differ in a few fields.
- The concrete class should be chosen at runtime by copying a registered prototype, not by naming a class.
- You want to snapshot an object's current state and branch from it.

**Structure.** A *prototype* is copied via `clone`. Clients hold a prototype and clone it — customizing `__clone` to deep-copy nested objects. A registry of named prototypes is common.

```php
<?php

declare(strict_types=1);

// Mutable nested object — must be deep-copied
final class Style
{
    public function __construct(public string $color)
    {
    }
}

// Prototype
final class Button
{
    public function __construct(
        public string $label,
        public Style $style,
    ) {
    }

    // Deep copy — clone nested references so variants stay independent
    public function __clone(): void
    {
        $this->style = clone $this->style;
    }
}

// usage
$prototype = new Button('OK', new Style('blue'));

$danger = clone $prototype; // cheap copy of a configured instance
$danger->label = 'Delete';
$danger->style->color = 'red';

echo $prototype->label, '/', $prototype->style->color, PHP_EOL; // OK/blue (untouched)
echo $danger->label, '/', $danger->style->color, PHP_EOL;        // Delete/red
```

**Trade-offs.**
- **Gains:** Skips costly initialization; produces variants from a live template; decouples clients from concrete classes.
- **Costs:** Deep vs shallow copy is easy to get wrong; cyclic references and resource handles complicate cloning.
- **Skip it when:** Construction is cheap or objects are immutable — just build a new one.

**Integrating.** Framework-agnostic. PHP clones are shallow by default, so nested mutable objects need an explicit `__clone`. No container involvement.

**Related / not to be confused with.** Prototype *is* `clone` elevated to a design decision (often with a registry of named templates). Unlike a Factory, it copies an existing instance rather than building from class definitions.

## Simple Factory

**Intent.** Centralize object creation behind a single method that returns a product, hiding `new` from the client.

**Use when.**
- Several call sites create the same object and you want one place to change how it's built.
- Construction has a little setup (wiring a couple of dependencies) you don't want duplicated.
- You want to return an interface and keep the concrete class swappable, without a full factory hierarchy.
- The set of products is small and mostly fixed.

**Structure.** A single *factory* class exposes an instance `create()` method returning a *product* interface. Any selection logic lives in that one method — no inheritance hierarchy.

```php
<?php

declare(strict_types=1);

interface Formatter
{
    public function format(array $data): string;
}

// Concrete products
final class JsonFormatter implements Formatter
{
    public function format(array $data): string
    {
        return json_encode($data, JSON_THROW_ON_ERROR);
    }
}

final class CsvFormatter implements Formatter
{
    public function format(array $data): string
    {
        return implode(',', array_map(strval(...), $data));
    }
}

// Fixed set of products
enum Format: string
{
    case Json = 'json';
    case Csv = 'csv';
}

// Simple factory — one method, one place for creation logic
final class FormatterFactory
{
    public function create(Format $format): Formatter
    {
        return match ($format) {
            Format::Json => new JsonFormatter(),
            Format::Csv => new CsvFormatter(),
        };
    }
}

// usage
$factory = new FormatterFactory();
echo $factory->create(Format::Json)->format(['a' => 1]), PHP_EOL;
echo $factory->create(Format::Csv)->format([1, 2, 3]), PHP_EOL;
```

**Trade-offs.**
- **Gains:** One place to change construction; clients depend on an interface; trivial to understand.
- **Costs:** The `match` grows with every new product (a mild Open/Closed violation).
- **Skip it when:** There's exactly one implementation and no setup — just `new` it or inject it.

**Integrating.** Laravel/Symfony/CI4: often unnecessary because the container *is* your factory (bind an interface to a resolver). Reach for an explicit factory when creation depends on runtime input the container can't supply.

**Related / not to be confused with.** Not a GoF pattern — a convenience. Unlike Factory Method it uses no subclassing; unlike Abstract Factory it makes one product, not a family. It differs from Static Factory only in that its `create()` is a normal, injectable, mockable instance method.

## Static Factory

**Intent.** Provide creation through a static method — typically a named constructor — as a readable alternative to `new`.

**Use when.**
- You want expressive named constructors (`Money::fromCents(500)`, `Uuid::v4()`) that reveal intent.
- A type needs several construction paths a single `__construct` can't express clearly.
- You want to validate or normalize inputs before an object exists, keeping the constructor private.
- Global, dependency-free construction is genuinely fine (value objects).

**Structure.** A class exposes one or more `static` factory methods returning instances (of itself or an interface). The real constructor is often `private` so all creation flows through the named entry points.

```php
<?php

declare(strict_types=1);

// Immutable value object with named constructors
final readonly class Money
{
    private function __construct(
        public int $cents,
        public string $currency,
    ) {
    }

    // Static factory methods — expressive, validating entry points
    public static function fromCents(int $cents, string $currency = 'EUR'): self
    {
        return new self($cents, $currency);
    }

    public static function fromEuros(float $euros): self
    {
        return new self((int) round($euros * 100), 'EUR');
    }

    public function format(): string
    {
        return number_format($this->cents / 100, 2) . ' ' . $this->currency;
    }
}

// usage
echo Money::fromCents(500)->format(), PHP_EOL; // 5.00 EUR
echo Money::fromEuros(2.5)->format(), PHP_EOL; // 2.50 EUR
```

**Trade-offs.**
- **Gains:** Self-documenting construction; can hide/validate the constructor; no factory object to pass around.
- **Costs:** Static calls are hard to mock/inject, so reserve for types with no external dependencies.
- **Skip it when:** Creation needs injected collaborators — use an instance factory or the container instead.

**Integrating.** Framework-agnostic and pervasive: value objects, DTOs, and Carbon-style dates (`Carbon::now()`) use static factories. Do not use them to build service objects that need dependencies.

**Related / not to be confused with.** Like Simple Factory, not a true GoF pattern. The distinction is *static method* (global, dependency-free) vs Simple Factory's *instance method* (injectable). Neither should be confused with Singleton, which restricts *how many* instances exist.

## Singleton

**Intent.** Ensure a class has exactly one instance and provide a global access point to it.

> **Caveat — usually an anti-pattern.** Singleton introduces global mutable state and hidden dependencies: a class that calls `Config::getInstance()` internally lies about what it needs, is hard to test (shared state leaks between tests, the instance can't be swapped for a fake), and creates invisible coupling. Prefer **Dependency Injection**: build the single instance once in your composition root and *inject* it, letting the container guarantee "one instance" rather than a static accessor. The code below is shown for completeness and recognition, not as a recommendation.

**Use when.** (Rarely — and only when DI genuinely cannot apply.)
- You truly need exactly one instance *and* cannot pass it in (e.g., a bootstrap constraint before any container exists).
- The state is effectively immutable after init, sidestepping shared-mutable-state hazards.
- You are recognizing/refactoring an existing Singleton rather than adding a new one.

**Structure.** A `private static` field holds the sole instance; a `public static getInstance()` lazily creates it; the constructor is `private` and `__clone`/`__wakeup` are blocked to prevent duplication.

```php
<?php

declare(strict_types=1);

final class Registry
{
    private static ?self $instance = null;

    /** @var array<string, mixed> */
    private array $items = [];

    private function __construct()
    {
    }

    public static function getInstance(): self
    {
        return self::$instance ??= new self(); // lazy, single creation
    }

    public function set(string $key, mixed $value): void
    {
        $this->items[$key] = $value;
    }

    public function get(string $key): mixed
    {
        return $this->items[$key] ?? null;
    }

    // Block the escape hatches that would create a second instance
    private function __clone(): void
    {
    }

    public function __wakeup(): void
    {
        throw new LogicException('Cannot unserialize a singleton');
    }
}

// usage
Registry::getInstance()->set('env', 'prod');
echo Registry::getInstance()->get('env'), PHP_EOL; // prod — same instance
```

**Trade-offs.**
- **Gains:** Guarantees one instance; convenient global reach.
- **Costs:** Global mutable state; hidden dependencies; hard to test and parallelize; the global accessor couples every caller to a concrete class.
- **Skip it when:** Almost always — inject a single shared instance via the container instead (see Dependency Injection).

**Integrating.** Laravel: `$this->app->singleton(Foo::class)` — one instance, *injected* rather than globally fetched. Symfony: services are shared (singleton lifetime) by default. CodeIgniter 4: `Services` returns shared instances via `getSharedInstance()`. All give singleton *lifetime* without the anti-pattern's global accessor.

**Related / not to be confused with.** "Singleton the lifetime" (one shared instance provided by a container) is fine and normal; "Singleton the pattern" (a static `getInstance()` accessor) is what to avoid. Not a Pool (many instances) and not Static Factory (which controls *construction*, not *count*).

## Dependency Injection

**Intent.** Supply an object's collaborators from the outside instead of having it construct or fetch them itself — the modern default for wiring dependencies.

**Use when.**
- A class needs collaborators (a logger, a repository, a mailer) — inject them rather than `new`-ing or calling a static accessor inside.
- You want to test a unit in isolation by passing fakes/mocks into the constructor.
- You reach for a Singleton or Service Locator to "get" a dependency — inject it instead.
- You want swappable implementations selected once, centrally, at the composition root.

**Structure.** Depend on *interfaces* and receive them via the *constructor* (preferred) so an object is always fully formed. A *composition root* (or a PSR-11 container) is the single place that instantiates concrete classes and wires the object graph. No class fetches its own dependencies.

```php
<?php

declare(strict_types=1);

// Abstractions — clients depend on these, not concretes
interface Mailer
{
    public function send(string $to, string $body): void;
}

interface UserRepository
{
    public function emailFor(int $id): string;
}

// Concrete collaborators
final class SmtpMailer implements Mailer
{
    public function send(string $to, string $body): void
    {
        echo "SMTP -> {$to}: {$body}", PHP_EOL;
    }
}

final class InMemoryUserRepository implements UserRepository
{
    public function emailFor(int $id): string
    {
        return "user{$id}@test";
    }
}

// Consumer — declares needs via constructor; fetches nothing itself
final class WelcomeService
{
    public function __construct(
        private readonly Mailer $mailer,
        private readonly UserRepository $users,
    ) {
    }

    public function welcome(int $userId): void
    {
        $this->mailer->send($this->users->emailFor($userId), 'Welcome!');
    }
}

// usage — composition root: the one place that wires concrete classes
$service = new WelcomeService(new SmtpMailer(), new InMemoryUserRepository());
$service->welcome(42);

// A PSR-11 container automates this wiring for large graphs:
// $service = $container->get(WelcomeService::class);
```

**Trade-offs.**
- **Gains:** Testable (inject fakes); explicit dependencies; swappable implementations; no hidden global state.
- **Costs:** Requires a composition root or container; the object graph must be assembled somewhere; abusing a container as a Service Locator reintroduces hidden dependencies.
- **Skip it when:** For trivial value objects or pure functions with no collaborators, injection is ceremony for nothing.

**Integrating.** Laravel: bind interfaces to implementations in a service provider (`$this->app->bind(Mailer::class, SmtpMailer::class)`), plus contextual binding for per-consumer variants. Symfony: autowiring resolves constructor type-hints automatically; tag and inject collections of services. CodeIgniter 4: the `Services` class is the composition root — request wired objects from it. WordPress: no container, so wire manually in a bootstrap file and pass dependencies into constructors. Custom: build a composition root or use any PSR-11 container (PHP-DI, League Container).

**Related / not to be confused with.** DI is what *replaces* Singleton and Service Locator for supplying dependencies: instead of a class *pulling* a global instance, the wiring code *pushes* it in. A container manages *lifetime* (shared/transient) and wiring; injecting the container everywhere and calling `$container->get()` inside classes is the Service Locator anti-pattern DI aims to avoid.
