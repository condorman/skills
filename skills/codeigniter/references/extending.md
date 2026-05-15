# Extending CodeIgniter

CodeIgniter 4 is designed to be easily extensible.

## Extending the Controller

The best way to add shared functionality across all your controllers is to modify the `BaseController.php`.

### BaseController
Located in `app/Controllers/BaseController.php`.

```php
abstract class BaseController extends Controller
{
    protected $helpers = ['url', 'form', 'my_custom_helper'];

    public function initController(RequestInterface $request, ResponseInterface $response, LoggerInterface $logger)
    {
        // Do Not Edit This Line
        parent::initController($request, $response, $logger);

        // Preload services or set global variables
        $this->session = \Config\Services::session();
    }
}
```

## Events

The Events system allows you to tap into the framework execution at specific points.

### Defining Events
Defined in `app/Config/Events.php`.

```php
Events::on('pre_system', function () {
    // Logic to run very early in the execution
});

Events::on('post_controller_constructor', ['App\Libraries\MyLibrary', 'myMethod']);
```

## Replacing Core Classes

You can replace core system classes by mapping them in `app/Config/Autoload.php`.

```php
public $classmap = [
    'CodeIgniter\HTTP\Request' => APPPATH . 'Libraries/HTTP/MyRequest.php',
];
```

## Creating Composer Packages

You can create reusable modules and distribute them via Composer. CodeIgniter 4 automatically detects and loads packages if they follow the standard structure.
