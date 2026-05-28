## React functional components 

A basic template:

```javascript
import {useState, useEffect} from 'react'

const FunctionalComponent = (props) => {
    
    // state variable
    const [variable, setVariable] = useState('initial value')
    
    useEffect(()=>{
        // api fetch or callbacks here
    },[])
    
    return <>
        {variable}
    </>
    
}

export default FunctionalComponent
```

Conditional rendering based on state value:

```javascript
import {useState} from 'react'

const ConditionalRendering = (props) => {

    // state variable
    const [flag, setFlag] = useState(false)

    // when the button is pressed the flag is set to !flag
    const handleClick = () => {
        setFlag(!flag)
    }
    return <>
        {flag &&
        <div>The flag is set to true</div>
        }
        {!flag &&
        <div>The flag is set to false</div>
        }

        <button onClick={handleClick}>Change flag</button>
    </>

}

export default ConditionalRendering
```

A more complex example that contains state, effects, conditional rendering, and mapping data to jsx.

```javascript
import React, { useState, useEffect } from 'react'

const Users = props => {

    // State managed objects
    const [users, setUsers] = useState([])
    const [pressed, setPressed] = useState(false)

    // Side effect management (componentDidMount)
    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/users').then(r => r.json()).then(data => { setUsers(data); console.log(data); })
    }, [/* variables that can trigger the effect */])

    // Button handler
    const buttonHandler = () => {
        setPressed(!pressed)
    }

    // conditional rendering based on state
    return <>
        <button onClick={buttonHandler}>Action</button>
        {pressed &&
            <span>Button pressed</span>
        }
        <div>
            {users.map(user => {
                return <div key={user.username+user.id}>{user.name}</div>
            })}
        </div>
    </>
}

export default Users;
```