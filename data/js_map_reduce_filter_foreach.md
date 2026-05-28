## JavaScript 

### Map 

The `map()` method is used for creating a new array from an existing one, applying a function to each one of the elements of the first array.

```JS
var new_array = arr.map(function callback(element, index, array) {
    // Return value for new_array
}[, thisArg])
```

Example:

```JS
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(item => item * 2);
console.log(doubled); // [2, 4, 6, 8]
```

### Filter

The `filter()` method takes each element in an array and it applies a conditional statement against it. If this conditional returns true, the element gets pushed to the output array. If the condition returns false, the element does not get pushed to the output array.

```JS
var new_array = arr.filter(function callback(element, index, array) {
    // Return true or false
}[, thisArg])
```
Example:

```JS
const students = [
  { name: 'Quincy', grade: 96 },
  { name: 'Jason', grade: 84 },
  { name: 'Alexis', grade: 100 },
  { name: 'Sam', grade: 65 },
  { name: 'Katie', grade: 90 }
];

const studentGrades = students.filter(student => student.grade >= 90);
return studentGrades; // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
```

### Reduce

The `reduce()` method reduces an array of values down to just one value. To get the output value, it runs a reducer function on each element of the array.

```JS
arr.reduce(callback[, initialValue])
```

The callback function can take 5 arguments: `accumulator, currentValue, index, array, initialValue`

Example:

```JS
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce(function (result, item) {
  return result + item;
}, 0);
console.log(sum); // 10
```

### forEach

Applies a function to each element of the array. It can be used as a for loop.

```JS
array.forEach(function(currentValue, index, arr), thisValue)
```

Example:

```JS
let sum = 0;
const numbers = [65, 44, 12, 4];
numbers.forEach(myFunction);

document.getElementById("demo").innerHTML = sum; // 125

function myFunction(item) {
  sum += item;
}
```

**References:**

- [freecodecamp](https://www.freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples/)