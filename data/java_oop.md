***Object-Oriented Programming***

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects that contain data (fields) and behavior (methods). 

- Improves code reusability
- Enhances maintainability and scalability
- Makes programs easier to understand and manage
- Closely models real-world entities 

Key concepts: classes, objects, abstraction, encapsulation, inheritance, and polymorphism.

- ***Classes*** are the starting point of all objects, and we may consider them as the template for creating objects.

- ***Objects*** are created from classes and are called instances of the class.

- ***Abstraction*** is hiding complexities of implementation and exposing simpler interfaces.

- ***Encapsulation*** is hiding the state or internal representation of an object from the consumer of an API.

- ***Inheritance*** is the mechanism that allows one class to acquire all the properties from another class by inheriting the class.

- ***Polymorphism*** is the ability of an OOP language to process data differently depending on their types of inputs.

Example class:

```java
public class Person {

	private String name = "";

	// Constructor 1
	public Person() {
		setName("");
	}
		
	// Constructor 2
	public Person(String n) {
		this();
		setName(n);
	}
		
	// Getter and Setter methods
	public String getName() {
		return name;
	}
		
	public void setName(String n) {
		this.name = n;
	}
		
	// Method
	public Boolean isUpercase() {
		if(name != null && !name.isEmpty()) {
			return Character.isUpperCase(name.charAt(0));
		}else {
			return false;
		}
	}
}
```

*super()* is used in a subclass constructor to call the constructor of its parent class, ensuring the parent part of the object is initialized first. Calls the parent class constructor.


*this()* is used in a class constructor to call another constructor of the same class, allowing constructor chaining and reducing code duplication.