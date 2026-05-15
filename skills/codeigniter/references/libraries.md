# Library Reference

CodeIgniter 4 includes a variety of libraries to help with common tasks.

## Loading Libraries

Most libraries are available as **Services** or can be instantiated directly.

### Using Services (Recommended)
```php
$validation = \Config\Services::validation();
$email      = \Config\Services::email();
$curl       = \Config\Services::curlrequest();
```

### Direct Instantiation
```php
$session = new \CodeIgniter\Session\Session($config);
```

## Common Libraries

### Validation
Used to validate data, typically from a form or API request.
```php
$validation = \Config\Services::validation();
if (!$validation->run($data, 'signup')) {
    return $validation->getErrors();
}
```

### CURLRequest
A powerful HTTP client (based on Guzzle principles).
```php
$client = \Config\Services::curlrequest();
$response = $client->get('https://api.example.com/data');
echo $response->getBody();
```

### Session Library
Handles user sessions.
```php
$session = \Config\Services::session();
$session->set('user_id', 123);
$userId = $session->get('user_id');
```

### Email Class
Sends emails.
```php
$email = \Config\Services::email();
$email->setTo('user@example.com');
$email->setSubject('Welcome');
$email->setMessage('Hello world');
$email->send();
```

### Times and Dates (Time)
A wrapper around PHP's `DateTime` with extra features.
```php
use CodeIgniter\I18n\Time;

$myTime = new Time('now');
echo $myTime->toDateTimeString();
echo $myTime->humanize(); // "1 minute ago"
```

### Pagination
Automatically handles creating pagination links and managing offsets.
```php
$userModel = new UserModel();
$data = [
    'users' => $userModel->paginate(10),
    'pager' => $userModel->pager,
];
return view('users/index', $data);
```

### Pagination in Views
```php
<?= $pager->links() ?>
```
