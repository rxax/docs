## Java Features (java 17+)

### Records

Records are immutable by default (final). For mutability use traditional class. 

```java
// User.java (1 line)
public record User(long id, String username) { }

// Usage: 
var user = new User(42, "theIndieDev");
long userId = user.id(); // Accessors are named after the field
```

### Pattern Matching for instanceof

```java
public void process(Object o) {
    // 's' is automatically cast to String and is in scope
    if (o instanceof String s) { 
        System.out.println("Length: " + s.length());
    }
    // 's' is out of scope here
}
```

### Switch Expressions

No more breaks required.

```java
String dayType = switch (day) {
    case MONDAY, FRIDAY -> "Busy";
    case SATURDAY, SUNDAY -> "Weekend";
    default -> "Normal";
}
```

### Sealed Classes

Explicitly declare which classes or records can implement or extend a sealed type, enforcing a controlled hierarchy.

```java
// Enforcing that only Circle, Square, and Rectangle can be shapes
public sealed interface Shape 
    permits Circle, Square, Rectangle { }

public record Circle(double radius) implements Shape { }
public final class Square implements Shape { /* ... */ } 
// Any class that is not explicitly 'permitted' cannot implement Shape
```

### Text blocks

```java
String JSON_PAYLOAD = """
    {
      "name": "AccountCreatedEvent",
      "timestamp": "%s"
    }
    """.formatted(now()); // Works great with .formatted()!
   ```

### Local Variable Type Inference (var)

```java
// The type is obvious from the right-hand side (RHS)
var userMap = new HashMap<String, List<User>>(); 

// Still explicit enough for readability
try (var reader = new BufferedReader(new FileReader("data.txt"))) {
    // ...
}

```

### Better Optional

```java
// Cleaner way to throw an exception
String result = optionalValue.orElseThrow(NoSuchElementException::new); 

// Cleaner side-effect handling
optionalValue.ifPresentOrElse(
    this::doSomething, 
    this::doSomethingElse
);
```

### Stream finalizer

Replaces Collectors.toList()

```java
List<String> names = employees.stream()
    .map(Employee::getName)
    .toList(); // A single method call
```