# Testing

CodeIgniter 4 is designed to be highly testable, with built-in support for **PHPUnit**.

## Getting Started

Tests are located in the `tests/` directory.

### Running Tests
```bash
vendor/bin/phpunit
```

## Unit Testing

You can test your own classes or core framework components.

```php
namespace Tests;

use CodeIgniter\Test\CIUnitTestCase;

class MyTest extends CIUnitTestCase
{
    public function testTrueIsTrue()
    {
        $this->assertTrue(true);
    }
}
```

## Database Testing

CodeIgniter provides tools to test database interactions without affecting your live data.

### Database Test Setup
Extend `CIUnitTestCase` and use the `DatabaseTestTrait`.
```php
namespace Tests;

use CodeIgniter\Test\CIUnitTestCase;
use CodeIgniter\Test\DatabaseTestTrait;

class UserTest extends CIUnitTestCase
{
    use DatabaseTestTrait;

    protected $refresh = true; // Refresh database before each test
    protected $namespace = 'App'; // Namespace for migrations/seeds

    public function testUserInsert()
    {
        $model = new \App\Models\UserModel();
        $model->insert(['name' => 'John', 'email' => 'john@example.com']);

        $this->seeInDatabase('users', ['name' => 'John']);
    }
}
```

## Controller Testing

You can simulate requests to your controllers and check the responses.

```php
namespace Tests;

use CodeIgniter\Test\CIUnitTestCase;
use CodeIgniter\Test\ControllerTestTrait;

class HomeTest extends CIUnitTestCase
{
    use ControllerTestTrait;

    public function testIndex()
    {
        $result = $this->withURI('http://example.com/')
                       ->controller(\App\Controllers\Home::class)
                       ->execute('index');

        $this->assertTrue($result->isOK());
        $this->assertTrue($result->see('Welcome to CodeIgniter'));
    }
}
```

## HTTP (Feature) Testing

Simulates a full HTTP request through the routing system.

```php
namespace Tests;

use CodeIgniter\Test\CIUnitTestCase;
use CodeIgniter\Test\FeatureTestTrait;

class AuthTest extends CIUnitTestCase
{
    use FeatureTestTrait;

    public function testLoginRedirect()
    {
        $result = $this->get('admin/dashboard');

        $result->assertRedirectTo('login');
    }
}
```
