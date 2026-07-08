---
name: php-design-patterns
description: Framework-agnostic catalog of 32 classic (GoF) and enterprise PHP design patterns — Creational, Structural, Behavioral, plus Repository, DataMapper, Service Locator, Registry and EAV. Use this whenever the user describes an architectural or design problem in PHP and needs to pick the right pattern, asks "which design pattern should I use for X", wants to refactor rigid, duplicated or tangled code, or needs a clean reference implementation of a specific pattern (Factory, Strategy, Observer, Decorator, Adapter, Repository, Command, State, etc.). Maps a described context to the most suitable pattern with an academic explanation and its trade-offs, then generates a vanilla PHP 8 implementation plus notes on integrating it into Laravel, Symfony, CodeIgniter, WordPress or custom code. Trigger even when the user never names a pattern but describes symptoms like "too many if/switch on a type", "swap the algorithm at runtime", "objects get created in dozens of places", "these two interfaces don't match", "notify many parts when something changes", "undo/redo", or "hide this messy subsystem".
---

# PHP Design Patterns

A pattern-selection advisor and reference-implementation generator for PHP. It exists to answer one question well: *given this concrete problem, which design pattern fits, why, and what does a clean implementation look like?*

The catalog is deliberately **framework-agnostic**. Patterns are architectural ideas, not framework features — the same Strategy or Repository works in Laravel, Symfony, CodeIgniter, WordPress or plain PHP. So the default output is vanilla PHP 8, with a short section on how the idea maps onto whatever framework or CMS the user is working in.

## When this applies

Use this skill when the user is choosing, explaining, or implementing a design pattern — including when they describe the *symptom* rather than naming the pattern. Also use it to argue **against** a pattern: recognizing when a problem needs plain code instead of a pattern is part of the job (see [YAGNI check](#step-0--is-a-pattern-even-warranted)).

It is *not* for framework-specific plumbing (routes, migrations, controllers as such) — for that, defer to the framework's own skill. This skill enters when the question is about the underlying *design*.

## The workflow

The value of a pattern recommendation is only as good as the framing behind it. Rushing to name a pattern from a keyword ("they said 'factory' → Factory Method") is how the wrong pattern gets picked. Work through the problem first.

### Step 0 — Is a pattern even warranted?

Before selecting anything, sanity-check that the problem has real *variation or complexity to absorb*. Patterns buy flexibility by adding indirection; if there is nothing that varies, the indirection is pure cost. Push back when:

- There is exactly one implementation and no concrete plan for a second → a plain class or function is better than a Strategy/Factory.
- The "complex object" has three fields → a constructor beats a Builder.
- The code is called from one place → a Facade wraps nothing.

Say so plainly and recommend the simpler design. A skill that only ever says "yes, add a pattern" is a liability. When in genuine doubt, name the trade-off and let the user decide.

### Step 1 — Frame the problem

Extract these from the user's context (ask 1–2 targeted questions only if a decisive fact is missing — otherwise proceed with stated assumptions):

- **What varies, and along which axis?** Algorithms? Object types being created? Behavior over an object's lifetime? The number of steps? Two independent axes at once?
- **What is the pain?** Rigidity (hard to extend), duplication (same branching everywhere), coupling (everything knows everything), poor testability, memory/creation cost, or an interface mismatch.
- **What is fixed vs. open?** What must stay stable for callers while the inside changes.

Name the axis of change explicitly — it is what selects the pattern. "The *algorithm* varies at runtime" → Strategy. "The *type created* varies" → a Factory. "Behavior varies by *state*" → State.

### Step 2 — Select the pattern

Use the [Quick Selection Index](#quick-selection-index) below to shortlist 1–3 candidates by matching the problem signal. Then read the detailed entry in the relevant reference file to confirm fit before committing:

- Creational (object creation) → `references/creational.md`
- Structural (composition & relationships) → `references/structural.md`
- Behavioral (interaction & responsibility) → `references/behavioral.md`

Patterns overlap. Decorator vs. Proxy, Strategy vs. State, Adapter vs. Facade, Factory Method vs. Abstract Factory are classic confusions — each reference entry has a **Related / not to be confused with** note. Read it before deciding.

### Step 3 — Recommend, with the reasoning shown

Don't just name the winner. Show the discrimination: why this pattern over the closest alternative, in terms of the axis of change from Step 1. A recommendation the user can't evaluate is one they'll misapply. If two patterns genuinely both fit, say so and give the tie-breaker.

### Step 4 — Explain, implement, integrate

Produce the structured answer using the [Output template](#output-template): the academic core, a clean vanilla PHP 8 implementation, the honest trade-offs, and how to wire it into the user's actual stack.

## Quick Selection Index

Match the user's situation to a signal, shortlist the pattern(s), then confirm in the reference file. Grouped by the axis of change, which is what actually drives the choice.

### Creating objects → `references/creational.md`

| The situation / signal | Pattern(s) | Note |
|---|---|---|
| Decide *which class* to instantiate without callers naming it; subclasses choose | **Factory Method** | The extensible default |
| Create a *family* of related objects that must stay mutually consistent (e.g. matching UI toolkit, matching DB driver set) | **Abstract Factory** | One factory, many products |
| Centralize simple creation of one product by a type flag, no subclassing | **Simple Factory** / **Static Factory** | Lightest; not truly a GoF pattern |
| Build a complex object step-by-step; many optional parts; avoid a telescoping constructor | **Builder** | Also enables immutable results |
| New object should be a *copy of an existing configured one*; construction is costly | **Prototype** | `clone` + deep-copy care |
| Objects are expensive to create/destroy and are reused in bursts (connections, workers) | **Pool** | Reuse over re-create |
| One shared instance, global access | **Singleton** | ⚠ Usually an anti-pattern — prefer DI. See entry |
| Dependencies supplied from outside instead of built inside | **Dependency Injection** | The modern replacement for Singleton/Service Locator |

### Structuring & composing objects → `references/structural.md`

| The situation / signal | Pattern(s) | Note |
|---|---|---|
| Two incompatible interfaces must work together; wrap a third-party/legacy API to the interface you want | **Adapter** | Conform an existing thing |
| Abstraction and implementation each vary independently (2 axes) — avoid a class explosion | **Bridge** | Composition over a matrix of subclasses |
| Part–whole tree; treat a single item and a group of items uniformly | **Composite** | Recursion over a tree |
| Add responsibilities to *one object* dynamically, stackably, without subclassing | **Decorator** | Same interface, wraps and augments |
| Provide a simple entry point over a complicated subsystem | **Facade** | Simplify, don't hide access control |
| Control access to an object — lazy-load, cache, guard, or stand in for a remote one | **Proxy** | Same interface, controls access |
| Huge number of similar objects blow up memory; share the invariant part | **Flyweight** | Intrinsic vs. extrinsic state |
| Want a readable, chainable configuration API | **Fluent Interface** | `return $this` |
| Central place to register and look up shared instances by key | **Registry** / **Service Locator** | ⚠ Global state — prefer DI |
| Map a domain object to/from persistence without the object knowing about the DB | **Data Mapper** | Domain stays persistence-ignorant |
| Collection-like abstraction over storage; hide query details behind add/find/remove | **Repository** | Enterprise pattern; pairs with Data Mapper |

### Behavior, interaction & responsibility → `references/behavioral.md`

| The situation / signal | Pattern(s) | Note |
|---|---|---|
| Swap an interchangeable *algorithm* at runtime; kill an `if/switch` selecting behavior | **Strategy** | Choice made by the client |
| Behavior changes as an object moves through *states*; a state machine | **State** | Object changes its own state |
| Encapsulate a request/action as an object — queue it, log it, undo it | **Command** | Decouples caller from receiver |
| One change must notify many interested parties, loosely coupled | **Observer** | Publish/subscribe |
| Pass a request along a chain until a handler takes it (middleware, validation stack) | **Chain of Responsibilities** | Decouple sender from handler |
| Traverse a collection uniformly without exposing its internals | **Iterator** | Often native (`Iterator`, generators) |
| Many objects communicate in a tangled many-to-many web; centralize the coordination | **Mediator** | Hub instead of mesh |
| Capture and later restore an object's state without breaking encapsulation (undo) | **Memento** | Snapshot + caretaker |
| Fixed algorithm skeleton, subclasses fill in specific steps | **Template Method** | Inheritance-based; hook methods |
| Add new operations over an object structure without editing those classes | **Visitor** | Double dispatch; ⚠ heavy |
| Encapsulate a business rule as a reusable, combinable object (and/or/not) | **Specification** | Composable predicates |
| Eliminate repetitive `null` checks with a neutral do-nothing object | **Null Object** | A polymorphic default |
| Interpret sentences of a small language/grammar | **Interpreter** | Rare; DSLs, expression eval |

## Output template

Structure the answer this way. It keeps the academic reasoning and the practical code together, so the user can both understand *and* apply. Skip a section only when it genuinely doesn't apply (say so briefly rather than padding).

```markdown
## Recommendation: <Pattern name> (<category>)

**Why this fits.** <1–3 sentences tying the pattern to the user's axis of change
from Step 1. Name the alternative considered and why it lost.>

### Intent
<The classic one-line intent — what the pattern accomplishes, abstractly.>

### The problem it solves
<The forces at play: what varies, what stays stable, why naive code hurts here.>

### Structure
<The participants and their relationships, in plain terms. A small ASCII sketch
or a bullet list of roles — Context, Strategy, ConcreteStrategy, etc.>

### Implementation (vanilla PHP 8)
<Clean, self-contained, framework-agnostic code. See code conventions below.>

### Trade-offs
**Gains:** <what flexibility/decoupling you bought>
**Costs:** <indirection, class count, learning curve — be honest>
**Skip it when:** <the conditions under which plain code wins>

### Integrating into your stack
<Short, concrete notes for the framework/CMS in play — Laravel, Symfony,
CodeIgniter, WordPress, or "custom". How the container, config, or lifecycle
carries this pattern. Only the frameworks relevant to the user.>

### Related patterns
<Combines-with and easily-confused-with, one line each.>
```

## Code conventions

The reference implementations aim to be textbook-clean so the user can lift and adapt them. Match this style:

- **PHP 8.1+**, `declare(strict_types=1);` at the top of standalone examples.
- **Program to interfaces.** The whole point of most patterns is that callers depend on an abstraction. Define the interface explicitly.
- Use modern PHP: constructor property promotion, enums for fixed state/type sets, `readonly` for immutable value objects, union/nullable types, first-class callable syntax where it reads well.
- **PSR-12** formatting; PSR-4-friendly namespacing (`App\Patterns\...`) in examples that need a namespace.
- Keep examples minimal but *complete and runnable* — a tiny `// usage` block at the end showing the pattern in action beats an abstract fragment. No framework imports in the core implementation.
- Comment the *role* each class plays in the pattern ("// Concrete strategy"), not the obvious mechanics.

## Framework integration cheatsheet

Most patterns don't need bespoke wiring — they're just classes. What changes per stack is *who constructs and injects them*. Keep integration notes anchored to these realities rather than repeating generic prose:

- **Laravel** — bind interfaces to implementations in a service provider (`$this->app->bind(Interface::class, Concrete::class)`); Factories/Strategies resolve via the container; Observer maps to model events/`Event`+`Listener`; Repository sits over Eloquent; contextual binding covers Abstract Factory families.
- **Symfony** — autowiring by type-hint in `services.yaml`; tagged services + service locators for Strategy/Chain collections; the `EventDispatcher` is Observer/Mediator; Repository is first-class in Doctrine (which itself *is* Data Mapper).
- **CodeIgniter 4** — `Services` factory methods are the composition root; register bindings there; model-as-repository is idiomatic; Events class for Observer. (A dedicated `codeigniter` skill exists — defer to it for CI4-specific mechanics.)
- **WordPress** — the hooks system (`add_action`/`add_filter`) is Observer/Chain in disguise; wrap the procedural API behind Adapters/Facades to make plugin code testable; no container by default, so DI is manual or via a small container.
- **Custom / no framework** — a hand-rolled composition root (one place that news up the graph) or a PSR-11 container (PHP-DI, League Container). Emphasize the composition root as the single wiring point.

## Reference files

Read the relevant one before finalizing a recommendation — the Quick Selection Index shortlists, but the entries carry the fit criteria, trade-offs, full PHP, and disambiguation.

- `references/creational.md` — Abstract Factory, Builder, Factory Method, Pool, Prototype, Simple Factory, Singleton, Static Factory, Dependency Injection.
- `references/structural.md` — Adapter, Bridge, Composite, Data Mapper, Decorator, Facade, Fluent Interface, Flyweight, Proxy, Registry, Repository, Service Locator.
- `references/behavioral.md` — Chain of Responsibilities, Command, Interpreter, Iterator, Mediator, Memento, Null Object, Observer, Specification, State, Strategy, Template Method, Visitor.
