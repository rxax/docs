## JavaScript Arrays

Create an array

```js
const cars = ["Saab", "Volvo", "BMW"];

// or

const cars = new Array("Saab", "Volvo", "BMW");
```


Find one object

```js
let car = cars.find(car => car.color === "red");
```

Find multiple objects, can also be used to remove items from the array

```js
let redCars = cars.filter(car => car.color === "red");
```

Sorting

```js
let sortedCars = cars.sort((c1, c2) => (c1.capacity < c2.capacity) ? 1 : (c1.capacity > c2.capacity) ? -1 : 0);
```

Check if some entries satisfy the condition

```js
cars.some(car => car.color === "red" && car.type === "cabrio");
```

Check if all entries satisfy the condition

```js
cars.every(car => car.capacity >= 4);
```