# Command Line Usage (CLI)

CodeIgniter 4 provides a powerful CLI interface through the `spark` script.

## Using Spark

`spark` is located in the root of your project.

### Common Commands
- `php spark serve`: Starts the built-in development server.
- `php spark list`: Lists all available commands.
- `php spark make:controller Name`: Generates a new controller.
- `php spark make:model Name`: Generates a new model.
- `php spark migrate`: Runs pending database migrations.
- `php spark db:seed Name`: Runs a specific database seeder.

## Creating Custom Commands

You can create your own CLI commands by extending `CodeIgniter\CLI\BaseCommand`.

### Command File
Create a file in `app/Commands/MyCommand.php`.

```php
<?php

namespace App\Commands;

use CodeIgniter\CLI\BaseCommand;
use CodeIgniter\CLI\CLI;

class MyCommand extends BaseCommand
{
    protected $group       = 'Custom';
    protected $name        = 'custom:hello';
    protected $description = 'Displays a greeting message.';

    public function run(array $params)
    {
        CLI::write('Hello World!', 'green');
    }
}
```

### Running the Custom Command
```bash
php spark custom:hello
```

## CLI Library

The `CLI` class provides useful methods for interacting with the console.
- `CLI::write($text, $foreground, $background)`: Writes text to the console.
- `CLI::error($text)`: Writes an error message (red).
- `CLI::prompt($field, $default, $rules)`: Prompts the user for input.
- `CLI::table($rows, $headers)`: Displays a table in the console.
