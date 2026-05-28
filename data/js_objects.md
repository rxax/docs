## JavaScript Objects

A) Unordered collection of properties

```js
let person = new Object();
		
// props
person.name = "Nicholas";
person.age = 29;
person.job = "Software Engineer";

// methods
person.sayName = function() {
    document.getElementById('p1').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
}

person.sayName();
```

B) Object literal

```js
let person2 = {
    name: "Nicholas",
    age: 29,
    job: "Software Engineer",
    sayName() {
        document.getElementById('p2').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    }
}

person2.sayName();
```

C) Enhanced object syntax

```js
let name = "Nicholas", age = 29, job= "Software Engineer";

let person3 = {
    name,
    age,
    job,
    // Concise Method Syntax
    sayName(name) { 
        document.getElementById('p3').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    }
}

person3.sayName();
```

D) Factory pattern

```js
function createPerson(name, age, job) {
    let o = new Object();
    o.name = name;
    o.age = age;
    o.job = job;

    o.sayName = function() {
        document.getElementById('p4').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    };

    return o;
}

let person4 = createPerson("Nicholas", 29, "Software Engineer");
person4.sayName();
```

E) Constructor function pattern

```js
function Person(name, age, job){
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = function() {
        document.getElementById('p5').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    }
}

let person5 = new Person("Nicholas", 29, "Software Engineer");
person5.sayName();
```

F) Prototype pattern (can share methods)

```js
function Person6(name, age, job){
    this.name = name;
    this.age = age;
    this.job = job;
}

Person6.prototype = {
    name: "Nicholas",
    age: 29,
    job: "Software Engineer",
    sayName() {
        document.getElementById('p6').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    }
}

let person6 = new Person6('Andrew',40,'Senior Developer');
person6.sayName();
```

G) Classes

```js
class Person7 {
			
    constructor(name, age, job) {
        this.name = name;
        this.age = age;
        this.job = job;
    }

    sayName() {
        document.getElementById('p7').innerHTML = this.name + ', ' + this.age + ', ' +  this.job
    }
}

let person7 = new Person7("Nicholas", 29, "Software Engineer");
person7.sayName();
```