## JavaScript Quick Reference

```js
// Create variables
let a = 10
let b = "A text message"
let c = false
var ex1 = 10 // this is visible globally
const ex2 = 'Fixed' // this value cannot be changed later 

// String concatenation
let d = b + a + c
console.log(d)

// String to int
let e = parseInt("12")
console.log(e)

// Conditional statements
if (a >= 10 && !c) {
    console.log('this is true')
} else {
    console.log('this is false')
}

// Lists
let data = [1, 2, 3, "Something"]
let length = data.length
console.log('data length = ', length)

// Get element at index
console.log(data[2])

// For Loop
console.log('data items:')
for (let item of data) {
    console.log(item)
}

// Iterate by index
for (let i = 0; i < data.length; i++) {
    console.log(data[i])
}

// Slice a list
console.log(data.slice(1, 3))

// Add to list
data.push(10)

// Index of item in list
console.log('the index of 10 is', data.indexOf(10))

// Objects
const obj = {firstname: "Jhon", lastname: "Doe"}
for (let item of Object.keys(obj)) {
    console.log('key=', item, ', value=', obj[item])
}

// To JSON
let s = JSON.stringify(obj)
console.log(s)

// From JSON
let obj2 = JSON.parse(s)
console.log(obj2)

// Exceptions
try {
    let d = a.toUpperCase()
} catch (err) {
    console.log('a is not a text')
}

// Functions
function sumOfTwoNumbers(a, b) {
    return a + b
}

console.log('the sum of', 10, 'and', 15, 'is', sumOfTwoNumbers(10, 15))

// Functions: Arrow syntax (same as above)
const sumOfTwo = (a, b) => {
    return a + b
}

console.log('the sum of', 7, 'and', 4, 'is', sumOfTwo(7, 4))
```
