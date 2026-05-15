# Helpers

Helpers are collections of useful procedural functions that are not part of a class.

## Loading Helpers

Helpers are loaded using the `helper()` function.

### Loading in a Controller
```php
public function index()
{
    helper(['url', 'form']);
    return view('my_view');
}
```

### Loading Globally
You can also load helpers in `app/Config/Autoload.php` if you need them everywhere.

## Common Helpers

### URL Helper
Provides functions to help you work with URLs.
- `base_url($path)`: Returns your site base URL as specified in your config file.
- `current_url()`: Returns the full URL of the current page.
- `site_url($path)`: Returns your site URL with the `index.php` (if used).
- `anchor($uri, $title, $attributes)`: Creates a standard HTML anchor link.

### Form Helper
Provides functions to assist with creating forms.
- `form_open($action)`: Creates an opening form tag.
- `form_input($data)`: Creates a standard text input field.
- `form_hidden($name, $value)`: Creates a hidden input field.
- `form_close()`: Creates a closing form tag.

### Array Helper
Functions to work with arrays.
- `dot_array_search($index, $array)`: Search an array using dot-notation (e.g., 'foo.bar.baz').

### Date Helper
- `now()`: Returns the current time as a UNIX timestamp.

### Filesystem Helper
- `get_filenames($path)`: Returns an array containing the names of all files in a directory.

### Text Helper
- `random_string($type, $length)`: Generates a random string based on the type and length.
- `ellipsize($str, $max_length)`: Truncates a string and adds an ellipsis.
