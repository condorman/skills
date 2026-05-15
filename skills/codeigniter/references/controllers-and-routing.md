# Controllers and Routing

Controllers are the heart of your application, determining how HTTP requests are handled. Routing maps URLs to specific controller methods.

## Controllers

### Definition
A controller is a class that extends `BaseController`. It receives the request and returns a response.

```php
namespace App\Controllers;

class User extends BaseController
{
    public function profile($id)
    {
        // Load model
        $model = model(UserModel::class);
        $user = $model->find($id);

        return view('user/profile', ['user' => $user]);
    }
}
```

### Included Properties
- `$this->request`: The `IncomingRequest` object.
- `$this->response`: The `Response` object.
- `$this->logger`: The `Logger` instance.

### Data Validation in Controllers
```php
if (! $this->validate([
    'username' => 'required|max_length[30]',
    'email'    => 'required|valid_email',
])) {
    return view('signup', ['validation' => $this->validator]);
}
```

## URI Routing

Routes are defined in `app/Config/Routes.php`.

### Basic Routing
```php
$routes->get('users/(:num)', 'User::profile/$1');
```

### Route Placeholders
- `(:any)`: Any characters.
- `(:num)`: Numeric characters only.
- `(:alphanum)`: Alphanumeric characters only.
- `(:segment)`: Any character except a forward slash.

### HTTP Verb Routes
```php
$routes->get('products', 'Product::index');
$routes->post('products', 'Product::create');
$routes->put('products/(:num)', 'Product::update/$1');
$routes->delete('products/(:num)', 'Product::delete/$1');
```

### RESTful Resource Routes
Generates all standard CRUD routes for a resource.
```php
$routes->resource('photos');
```
This maps to methods: `index()`, `show()`, `new()`, `create()`, `edit()`, `update()`, `delete()`.

### Route Groups
```php
$routes->group('admin', function($routes) {
    $routes->get('users', 'Admin\Users::index');
    $routes->get('settings', 'Admin\Settings::index');
});
```

### Controller Filters
Filters run before or after a controller method.
```php
$routes->get('dashboard', 'Dashboard::index', ['filter' => 'auth']);
```
