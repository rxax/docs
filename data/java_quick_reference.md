### Java Quick Reference


Main class / method

```java
public class Main {
    public static void main(String[] args) {
        System.out.printIn("Hello, World!");
    }
}
```

Variables and Data Types

```java
int age = 25;
double price = 19.99;
char grade = 'A';
boolean isJavaFun = true;
String name = "Alice";
```

Operations

```java
+  // addition
-  // subtraction
* ~ // multiplication
/ // division
%  // modulus
== // equal
!= // not equal
```

Keyboard input with Scanner

```java
import java.util.Scanner;
// ...
String input = "";
try (Scanner scanner = new Scanner(System.in)) {
    while (!input.equals("q")) {
       System.out.print("Input: ");
       input = scanner.nextLine();
       System.out.println("Input was: " + input);
    }
}
```

Conditional operations: IF statement

```java
if (x > 0) {
    System.out.println("Positive");
} else if (x < 0) {
        System.out.println("Negative");
       } else {
            System.out.println("Zero");
       }
```
Switch statement

```java
switch(day) {
    case 1:
    System.out.printin("Mon");
    break;
    default:
    System.out.println("Unknown");
```

Loops: FOR loop

```java
int[] n = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
// Iterate through the array using a for loop
for (int i = 0; i < n.length; i++) {
     System.out.println("Index " + i + ": " + n[i]);
}
```

Loops: Enhanced FOR loop

```java
int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
 // Iterate through the array using an enhanced for loop
for (int a : arr) {
       System.out.println(a);
}
```

Loops: WHILE loop

```java
int i = 0;
while (i < 5) {
  System.out.println(i);
  i++;
}
```

Arrays

```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
int[] myNum = {10, 20, 30, 40};

// Array Length
System.out.println(cars.length);

// Accessing elements by id
System.out.println(cars[0]);

// Change element
cars[0] = "Opel";

// Loop through Array
for (int i = 0; i < cars.length; i++) {
  System.out.println(cars[i]);
}

// Enhanced for Loop
for (String car : cars) {
  System.out.println(car);
}
```

String basic methods

```java
String string = "Hello";
System.out.println(string.equalsIgnoreCase("HeLLo")); // Result: true
System.out.println(string.toLowerCase()); // Result: hello
System.out.println(string.toUpperCase()); // Result: HELLO
System.out.println(string.startsWith("h")); // Result: false
System.out.println(string.endsWith("lo")); // Result: true
System.out.println(Arrays.toString(string.toCharArray())); // Result: [H, e, l, l, o]
System.out.println(string.charAt(0)); // Result: H
System.out.println(string.indexOf('l')); // Result: 2
System.out.println(string.lastIndexOf('l')); // Result: 3
System.out.println(string.contains("l")); // Result: true
System.out.println(string.matches("(.*)l(.*)")); // Result: true
```


**Java Collection Framework**

- Provides ready-to-use data structures (e.g., ArrayList, HashSet, HashMap).
- Offers interfaces (Collection, List, Set, Map, Queue) to define standard behaviors.
- Supports dynamic resizing, unlike arrays with a fixed size.
- Includes algorithms (sorting, searching, iteration) via the Collections utility class.
- Improves code reusability and performance by reducing boilerplate code.
```java
		// Creating a List of Strings using ArrayList (dynamic array)
		List<String> list = new ArrayList<>();

		// Adding elements to the ArrayList
		list.add("Java");
		list.add("Python");
		list.add("C++");

		// Printing the elements of the ArrayList
		System.out.println("Programming Languages:");

		// Enhanced for-loop to iterate through the list
		for (String lang : list) {
			System.out.println(lang);
		}
		
		// Removing item from ArrayList
		list.remove("Java"); 
```


Core interfaces and implementations

- Collection Interface
- List Interface: ArrayList, LinkedList, Vector, Stack
- Set Interface: HashSet, TreeSet, EnumSet, SortedSet
- Queue/ Deque Interface: PriorityQueue, ArrayDeque, BlockingQueue, ConcurrentLinkedQueue
- Map Interface: HashMap, LinkedHashMap, TreeMap, HashTable


Exception Handling

```java
try {
	int x = 10 / 0;
} catch (Exception e) {
	System.out.println(e.getMessage());
} finally {
	System.out.println("Done");
}
```
