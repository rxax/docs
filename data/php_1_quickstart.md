## PHP Quickstart Guide

###Basic Syntax

Variable declarations

```php
$name = "John";
$age = 25;
```

Super-globals

`$_GET, $_POST, $_REQUEST, $_SERVER, $_SESSION, $_COOKIE, $_FILES`

Constants

```php
define("SITE_NAME", "My Website");
```

Conditional operations

```php
if ($age >= 18) {
        echo "Adult";
    } else {
        echo "Minor";
    }
```

Loops

```php
# standard for loop
for ($i = 1; $i <= 5; $i++) {
    echo $i;
}

# enhanced for
foreach ($colors as $color) {
    echo $color;
}
```

Arrays

One-dimensional Arrays

```php
$fruits = ["Apple", "Banana"];
```

Multi-dimensional Arrays

```php
  $name[0][0] = 'Claudia Mustermann';
  $name[0][1] = 'info@mustermann.de';

  $name[1][0] = 'Dieter Hinz';
  $name[1][1] = 'dieter.hinz@wasweissich.de';

  $name[2][0] = 'Peter Kunz';
  $name[2][1] = 'peter@kunz.de';
```

Associative arrays

```php
  $adresse['name']   = 'Claudia Mustermann';
  $adresse['straße'] = 'Musterstraße 0';
  $adresse['plz']    = '00000';
  $adresse['ort']    = 'Musterstadt';
  $adresse['mail']   = 'info@mustermann.de';
  
  $user = ["name"=>"John","age"=>25];
```

Functions

```php
function greet($name) {
    return "Hello, $name";
}
```

Form Handling

```php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    echo $_POST["username"];
}
```

File Operations

```php
file_put_contents("data.txt", "Hello");

$content = file_get_contents("data.txt");
```

## OOP with PHP

Class definition and instance creation

```php
class User {
 // Public property
    public string $name;

    // Private property
    private int $age;

    // Static property (shared by all instances)
    private static int $userCount = 0;

    // Constructor
    public function __construct(string $name, int $age)
    {
        $this->name = $name;
        $this->age = $age;

        self::$userCount++;
    }

    // Public method
    public function getProfile(): string
    {
        return $this->formatProfile();
    }

    // Public method
    public function setAge(int $age): void
    {
        if ($age > 0) {
            $this->age = $age;
        }
    }

    // Public method
    public function getAge(): int
    {
        return $this->age;
    }

    // Private method
    private function formatProfile(): string
    {
        return "Name: {$this->name}, Age: {$this->age}";
    }

    // Static method
    public static function getUserCount(): int
    {
        return self::$userCount;
    }
}
```

Usage:

```php
// Create objects
$user1 = new User("John", 25);
$user2 = new User("Jane", 30);

// Access public property
echo $user1->name . PHP_EOL;

// Call public method
echo $user1->getProfile() . PHP_EOL;

// Call static method
echo "Total users: " . User::getUserCount() . PHP_EOL;
```

Database access

```php
$pdo = new PDO("mysql:host=localhost;dbname=test","root","password");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
 
$pdo->prepare('SELECT name, colour, calories FROM fruit WHERE calories < :calories AND colour = :colour');
$pdo->bindParam(':calories', $calories);
$pdo->bindParam(':colour', $colour);
$pdo->execute();

$users = $pdo->fetchAll(PDO::FETCH_ASSOC);

foreach ($users as $user) {
        echo $user['name'] . "<br>";
    }
```

Exception handling

```php
try {
    throw new Exception("Error");
} catch (Exception $e) {
    echo $e->getMessage();
}
```

Namespaces

```php
namespace App\Controllers;
class HomeController {}
```

PHP Development server

`php -S localhost:8000`

###Build tools

`composer init`

Composer is a dependency manager for PHP. Dependencies are written into `composer.json`:

```json
{
    "require": {
        "monolog/monolog": "2.0.*"
    }
}
```
Then run `composer install`