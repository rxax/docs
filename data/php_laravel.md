## Laravel framework

Laravel is a popular PHP framework that follows the MVC (Model-View-Controller) pattern. It provides tools for:

- Routing
- Database access (Eloquent ORM)
- Authentication
- Validation
- Migrations
- APIs
- Testing

Create project

`composer create-project laravel/laravel my-app`

Run the dev server

`cd my-app php artisan serve`

Visit

`http://127.0.0.1:8000`

###Routes

Routes are in `routes/web.php`

```php
Route::get('/', function () { 
    return 'Hello Laravel'; 
}); 

Route::get('/about', function () { 
    return 'About Page'; 
});
```

###Controllers

`php artisan make:controller UserController`

```php
namespace App\Http\Controllers;

class UserController extends Controller
{
    public function index()
    {
        return 'List of users';
    }
}
```

then in Routes change:

```php
use App\Http\Controllers\UserController; 

Route::get('/users', [UserController::class, 'index']);
```

###Views (Blade templates)

Create `resources/views/users.blade.php`

Change the controller

```php
public function index() { 
    return view('users'); 
}
```

###Migrations

`php artisan make:migration create_users_table`

Example:

```php
Schema::create('users', function ($table) { 
    $table->id(); 
    $table->string('name');
    $table->string('email')->unique(); 
    $table->timestamps(); 
    });
```

Run migration

`php artisan migrate`

###Models (Eloquent ORM)

`php artisan make:model User`

```php
namespace App\Models; 
use Illuminate\Database\Eloquent\Model; 

class User extends Model { 
    protected $fillable = [ 
        'name', 
        'email' 
    ]; 
}
```

**CRUD operations**

Fetching data

Get all users: 

```php
$users = User::all();
```

Get one user: 

```php
$user = User::find(1);
```

Create user:

```php
User::create([ 
    'name' => 'John', 
    'email' => 'john@example.com' 
]);
```

Update user:

```php
$user = User::find(1); 
$user->name = 'Jane'; 
$user->save();
```

Delete user:

```php
$user->delete();
```

###Passing data to Views

In the controller:

```php
$users = User::all(); 
return view('users', compact('users'));
```

In the view:
```php
@foreach($users as $user) 
<p>{ { $user->name } }</p> 
@endforeach
```

###Request validation

```php
$request->validate([ 
    'name' => 'required|min:3', 
    'email' => 'required|email' 
]);
```

###Artisan commands

Generate controller:

`php artisan make:controller UserController`

Generate model:

`php artisan make:model User`

Generate migration:

`php artisan make:migration create_users_table`

Run migrations:

`php artisan migrate`

List routes:

`php artisan route:list`