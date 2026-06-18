## React QuickStart Guide

### Creating Components

Functional Components

```js
function MyComponent() {
  return <h1>Hello React</h1>;
}

export default MyComponent;
```

Arrow function

```js
const MyComponent = () => {
  return <h1>Hello React</h1>;
};

export default MyComponent;
```

###JSX 

JSX lets you write HTML-like syntax in JavaScript.

```js
const element = <h1>Hello world</h1>;
```

Embedded JS expressions

```js
const name = "Alex";
return <h1>Hello {name}</h1>;
```

Conditional Rendering

```js
return isLoggedIn ? <Dashboard /> : <Login />;
```

### Core Features

###Hooks

useState

```js
import { useState } from "react";

const [count, setCount] = useState(0);

setCount(count + 1);
```

useEffect

```js
import { useEffect } from "react";

useEffect(() => {
  console.log("Mounted or updated");

  return () => console.log("Cleanup");
}, [dependency]);
```

`[]` → run once on mount

`[value]` → run when value changes

useRef

```js
import { useRef } from "react";

const inputRef = useRef(null);

inputRef.current.focus();
```

useMemo (for performance)

```js
const result = useMemo(() => expensiveCalc(a), [a]);
```

useCallback

```js
const handleClick = useCallback(() => {
  console.log("Clicked");
}, []);
```

Props

```js
function Welcome(props) {
  return <h1>Hello {props.name}</h1>;
}
```

Destructing props

```js
function Welcome({ name }) {
  return <h1>Hello {name}</h1>;
}
```

Usage:

```html
<Welcome name="Sam" />
```

**States vs Props:**

Props → read-only (passed from parent)

State → internal, can change

**Lists and Keys**

```js
const items = ["A", "B", "C"];

return (
  <ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>
);
```

**Event Handling**

```js
function handleClick() {
  alert("Clicked!");
}

<button onClick={handleClick}>Click me</button>
```

With parameters:

```js
<button onClick={() => handleClick(id)} />
```

Forms 

```js
const [value, setValue] = useState("");

return (
  <input
    value={value}
    onChange={(e) => setValue(e.target.value)}
  />
);
```

Component LifeCycle

| Class lifecycle	    | Hook equivalent
|-----------------------|----------------------------
| componentDidMount	    | useEffect(() => {}, [])
| componentDidUpdate	| useEffect(() => {}, [deps])
| componentWillUnmount	| return cleanup in useEffect


###Fetching Data

```js
useEffect(() => {
  fetch("https://api.example.com/data")
    .then(res => res.json())
    .then(data => setData(data));
}, []);
```

### Common Patterns

**Lifting state up**

Move shared state to nearest common parent.

**Controlled component**

Input value is controlled by React state.

**Conditional rendering**

```js
{loading && <Spinner />}
```