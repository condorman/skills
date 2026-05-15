# Modeling Data

CodeIgniter 4 provides powerful tools for database interaction through its **Model** and **Entity** classes.

## CodeIgniter Model

The `CodeIgniter\Model` class provides a consistent way to interact with database tables.

### Basic Model Setup
```php
namespace App\Models;

use CodeIgniter\Model;

class UserModel extends Model
{
    protected $table            = 'users';
    protected $primaryKey       = 'id';
    protected $useAutoIncrement = true;
    protected $returnType       = 'array'; // or 'object' or \App\Entities\User::class
    protected $useSoftDeletes   = false;
    protected $allowedFields    = ['name', 'email', 'password'];

    // Dates
    protected $useTimestamps = true;
    protected $dateFormat    = 'datetime';
    protected $createdField  = 'created_at';
    protected $updatedField  = 'updated_at';
    protected $deletedField  = 'deleted_at';

    // Validation
    protected $validationRules      = [
        'email' => 'required|valid_email|is_unique[users.email]',
    ];
    protected $validationMessages   = [];
    protected $skipValidation       = false;
}
```

### Finding Data
- `$model->find($id)`: Find a single record by primary key.
- `$model->findAll()`: Find all records.
- `$model->where('name', 'John')->first()`: Find the first record matching a condition.

### Saving Data
- `$model->insert($data)`: Insert a new record.
- `$model->update($id, $data)`: Update an existing record.
- `$model->save($data)`: Smartly decides between insert and update based on the presence of the primary key.

### Soft Deletes
If `$useSoftDeletes` is true, calling `$model->delete($id)` will set the `deleted_at` field instead of removing the row. Use `$model->withDeleted()` to include them in results.

## Entities

Entities allow you to represent a single row as a class, providing a place to put business logic for that specific record.

### Entity Definition
```php
namespace App\Entities;

use CodeIgniter\Entity\Entity;

class User extends Entity
{
    protected $datamap = [];
    protected $dates   = ['created_at', 'updated_at', 'deleted_at'];
    protected $casts   = [];

    public function setPassword(string $pass)
    {
        $this->attributes['password'] = password_hash($pass, PASSWORD_BCRYPT);
        return $this;
    }
}
```

### Using Entities in Models
Set `protected $returnType = \App\Entities\User::class;` in your model. When you retrieve data, it will be returned as an instance of your Entity class.

```php
$userModel = new \App\Models\UserModel();
$user = $userModel->find(1);

echo $user->name; // Accessing property
$user->name = 'New Name';
$userModel->save($user); // Saving the entity back
```
