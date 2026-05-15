# Installation

CodeIgniter 4 has two supported installation methods: manual download, or using **Composer**.

## Composer Installation (Recommended)
Composer is the recommended method because it handles dependencies and updates easily.

### Basic Installation
```bash
composer create-project codeigniter4/appstarter project-root
```

### Manual Installation
1. Download the latest version from the [CodeIgniter4 repository](https://github.com/codeigniter4/CodeIgniter4/releases).
2. Extract the contents to your server's web root.

## Server Requirements
- **PHP version 8.1 or newer** is required, with the following extensions:
  - `intl`
  - `mbstring`
  - `json` (usually enabled by default)
- Database support (MySQL, PostgreSQL, SQLite3, etc.)
- `curl` extension (if using CURLRequest)

## Running Your App
You can run your app using the built-in development server:

```bash
php spark serve
```
The app will be available at `http://localhost:8080`.

## Initial Configuration
1. **Environment File**: Rename `env` to `.env`.
2. **Base URL**: Set `app.baseURL` in `.env`.
3. **Database**: Configure your database settings in `.env`.

```ini
# .env example
app.baseURL = 'http://localhost:8080/'
database.default.hostname = localhost
database.default.database = ci4_db
database.default.username = root
database.default.password = root
database.default.DBDriver = MySQLi
```

## Folder Structure
- `app/`: Your application logic (Controllers, Models, Views).
- `public/`: The web root (index.php, assets).
- `writable/`: Temporary files, logs, cache.
- `tests/`: Your test suites.
- `vendor/`: Composer dependencies.
