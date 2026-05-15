# Modeling Data

CodeIgniter 4 provides a robust **Model** and **Entity** system for database interaction, offering features like automatic validation, soft deletes, and event hooks.

## 1. Model Configuration

The `CodeIgniter\Model` class is configured via protected properties.

### Property Reference
| Property | Type | Description |
| :--- | :--- | :--- |
| `$table` | `string` | The database table to operate on. |
| `$primaryKey` | `string` | The table's primary key (default: `id`). |
| `$useAutoIncrement`| `bool` | Whether the table uses auto-increment for the PK. |
| `$returnType` | `string` | Result format: `'array'`, `'object'`, or Entity FQCN. |
| `$useSoftDeletes` | `bool` | If true, `delete()` sets `deleted_at` instead of removing. |
| `$allowedFields` | `array` | List of fields allowed for mass-assignment (security). |
| `$useTimestamps` | `bool` | Automatically manage `$createdField` and `$updatedField`. |
| `$dateFormat` | `string` | Format of timestamps: `'datetime'`, `'date'`, or `'int'`. |
| `$createdField` | `string` | Column name for "created at" timestamp. |
| `$updatedField` | `string` | Column name for "updated at" timestamp. |
| `$deletedField` | `string` | Column name for "deleted at" timestamp. |
| `$validationRules` | `array` | Rules for automatic data validation. |
| `$validationMessages`| `array` | Custom error messages for validation. |
| `$skipValidation` | `bool` | Bypass validation for all operations. |
| `$allowCallbacks` | `bool` | Enable/disable event hooks. |

---

## 2. Core Retrieval Methods

### Standard Finders
- **`find($id = null)`**: Returns a single row by PK. If `$id` is an array, returns all matching rows.
- **`findAll(int $limit = 0, int $offset = 0)`**: Returns all rows (with optional limit/offset).
- **`first()`**: Returns the first result in the current query.
- **`findColumn(string $columnName)`**: Returns an array of values for that column.

### Soft Delete Utilities
- **`withDeleted()`**: Includes soft-deleted records in the next finder call.
- **`onlyDeleted()`**: Returns *only* soft-deleted records.

---

## 3. Core Persistence Methods

### Saving Data
- **`insert($data, bool $returnID = true)`**: Inserts a new row. Returns the new ID or boolean.
- **`update($id, $data)`**: Updates an existing row by PK. Returns boolean.
- **`save($data)`**: Wrapper for `insert`/`update`. If PK exists in `$data`, it updates.
- **`delete($id = null, bool $purge = false)`**: Deletes rows by PK. If `$purge` is true, bypasses soft-deletes.
- **`purgeDeleted()`**: Permanently removes all soft-deleted records.

### Error Handling
- **`errors()`**: Returns validation errors from the last operation.

---

## 4. Query Builder Integration

The model shares a Query Builder instance. You can chain methods before calling model finders.

```php
$users = $model->where('status', 'active')
               ->like('email', '@gmail.com')
               ->orderBy('created_at', 'DESC')
               ->findAll(10);
```

> [!NOTE]
> Chaining standard Query Builder methods like `get()` or `getResult()` will bypass model features like `$returnType` and callbacks. Use Model methods (`find*`, `first`, etc.) to maintain these features.

---

## 5. Model Validation

Validation is automatically triggered during `insert()`, `update()`, and `save()`.

### Placeholder Usage
Use `{id}` in rules to ignore the current record during updates (common for `is_unique`):
```php
protected $validationRules = [
    'email' => 'required|valid_email|is_unique[users.email,id,{id}]',
];
```

---

## 6. Model Events (Callbacks)

Hooks allow you to run logic at specific points in the lifecycle. Define method names in these properties:
`$beforeInsert`, `$afterInsert`, `$beforeUpdate`, `$afterUpdate`, `$afterFind`, `$beforeDelete`, `$afterDelete`.

### Callback Signature
Callback methods receive a single `$data` array and **must** return it.
```php
protected $beforeInsert = ['hashPassword'];

protected function hashPassword(array $data)
{
    if (! isset($data['data']['password'])) return $data;

    $data['data']['password'] = password_hash($data['data']['password'], PASSWORD_BCRYPT);
    return $data;
}
```

---

## 7. Entities

Entities provide an object-oriented way to interact with a single row, encapsulating business logic.

### Entity Setup
```php
namespace App\Entities;
use CodeIgniter\Entity\Entity;

class User extends Entity
{
    // Map database column name to object property name
    protected $datamap = ['full_name' => 'name']; 

    // Fields to be automatically cast to PHP types
    protected $casts = [
        'is_admin' => 'boolean',
        'options'  => 'json',
    ];

    // Mutator: runs when setting $user->password
    public function setPassword(string $pass)
    {
        $this->attributes['password'] = password_hash($pass, PASSWORD_BCRYPT);
        return $this;
    }
}
```

### Entity Utility Methods
- **`hasChanged(string $key)`**: Check if a property was modified.
- **`getDirty()`**: Get an array of all modified properties.
- **`toRawArray()`**: Get attributes as they are stored in the database.
- **`toArray()`**: Get attributes as mapped/casted.
