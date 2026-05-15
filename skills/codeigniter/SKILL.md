---
name: codeigniter
description: Build high-performance PHP web applications using CodeIgniter 4. This skill covers MVC architecture, RESTful routing, database modeling with Entities and Models, built-in library usage, helper functions, and robust testing frameworks. Ideal for developing scalable APIs and monolithic web apps with a small footprint.
---

CodeIgniter 4 is a powerful PHP framework with a very small footprint, built for developers who need a simple and elegant toolkit to create full-featured web applications.

Official Documentation: https://codeigniter.com/user_guide/index.html

| Topic | Docs URL | Use for |
|-------|----------|---------|
| Installation | [Installation](https://codeigniter.com/user_guide/installation/index.html) | Project setup, Composer, manual install |
| Controllers | [Controllers](https://codeigniter.com/user_guide/incoming/controllers.html) | Handling incoming requests, logic flow |
| Routing | [URI Routing](https://codeigniter.com/user_guide/incoming/routing.html) | Mapping URLs to controllers/methods |
| Models | [Modeling Data](https://codeigniter.com/user_guide/models/index.html) | Database interaction, Entities, Validation |
| Libraries | [Library Reference](https://codeigniter.com/user_guide/libraries/index.html) | Sessions, Validation, CURLRequest, etc. |
| Helpers | [Helpers](https://codeigniter.com/user_guide/helpers/index.html) | Procedural utility functions (URL, Array, Text) |
| Testing | [Testing](https://codeigniter.com/user_guide/testing/index.html) | Unit, Feature, and Database testing |

## Capabilities
- **MVC Architecture** — Clear separation of logic, data, and presentation.
- **RESTful Routing** — Powerful and flexible routing for APIs and web pages.
- **Database Abstraction** — Query Builder and Model-based ORM with Entity support.
- **Form Validation** — Robust data validation with custom rules.
- **Security** — Built-in CSRF, XSS protection, and secure session management.
- **Testing Framework** — Deep integration with PHPUnit for unit and integration tests.
- **CLI Support** — `spark` command-line tool for scaffolding and maintenance.
- **Caching** — Support for multiple caching backends (File, Redis, Memcached).

## Quick Setup
```bash
# Install via Composer
composer create-project codeigniter4/appstarter my-project

# Start development server
php spark serve
```

## Controller Example
```php
<?php

namespace App\Controllers;

use CodeIgniter\Controller;

class Home extends Controller
{
    public function index()
    {
        return view('welcome_message');
    }
}
```

## Routing Example
```php
// app/Config/Routes.php
$routes->get('/', 'Home::index');
$routes->resource('photos'); // RESTful resource
```

## Model & Entity Example
```php
// app/Models/UserModel.php
namespace App\Models;
use CodeIgniter\Model;

class UserModel extends Model
{
    protected $table = 'users';
    protected $returnType = \App\Entities\User::class;
    protected $allowedFields = ['name', 'email'];
}

// app/Entities/User.php
namespace App\Entities;
use CodeIgniter\Entity\Entity;

class User extends Entity
{
    protected $datamap = [];
}
```

## Reference Documentation
- **[references/installation.md](references/installation.md)** — Project setup and environment configuration.
- **[references/controllers-and-routing.md](references/controllers-and-routing.md)** — Request handling and URI mapping.
- **[references/models.md](references/models.md)** — Data modeling, Entities, and database operations.
- **[references/libraries.md](references/libraries.md)** — Core system libraries and drivers.
- **[references/helpers.md](references/helpers.md)** — Utility functions and procedural tools.
- **[references/testing.md](references/testing.md)** — Quality assurance and testing strategies.
- **[references/cli.md](references/cli.md)** — Command-line interface and spark tools.
- **[references/extending.md](references/extending.md)** — Customizing core behavior and extending functionality.
