## React Controlled Components

Event handling in React:
```javascript
import {useState} from 'react'

const EventHandlingComponent = (props) => {

    // state variable
    const [variable, setVariable] = useState('Test value')

    const handleChange = (event) => {
        // input handler, saves the value of the input into the components state
        setVariable(event.target.value)
    }
    
    return <>
        <input type="text" value={variable} onChange={handleChange}/>
        <span>The input contains: {variable}</span>
    </>
}

export default EventHandlingComponent
```

The values of the input fields are stored in the formValue object (in the state).

```js
import {useState} from 'react'

const ManagedForm = (props) => {

    const [formValue, setFormValue] = useState({username: '', address: '', income: 0, active: false})

    const handleChange = (e) => {
        // store input values in state
        setFormValue({...formValue, [e.target.name]: e.target.type === "checkbox" ? e.target.checked : e.target.value})
    }

    const handleSubmit = (e) => {
        // handle form submission
        e.preventDefault()

    }

    return <form onSubmit={handleSubmit}>
        {JSON.stringify(formValue)}

        <div className="form-group row p-2">
            <label className="col-2">Username</label>
            <input className="form-control col"
                   type="text"
                   name="username"
                   value={formValue['username']}
                   onChange={handleChange}
            />
        </div>

        <div className="form-group row p-2">
            <label className="col-2">Address</label>
            <input className="form-control col"
                   type="text"
                   name="address"
                   value={formValue['address']}
                   onChange={handleChange}
            />
        </div>

        <div className="form-group row p-2">
            <label className="col-2">Income</label>
            <input className="form-control col"
                   type="number"
                   name="income"
                   value={formValue['income']}
                   onChange={handleChange}
            />
        </div>

        <div className="form-group row p-2">
            <label className="col-2 form-check-label" htmlFor="f1">Active</label>
            <input className="form-check-input"
                   id="f1"
                   type="checkbox"
                   name="active"
                   checked={formValue['active']}
                   onChange={handleChange}
            />
        </div>

        <div className="row justify-content-center">
            <div className="col-1">
                <button className="btn btn-primary">Send</button>
            </div>
        </div>

    </form>
}

export default ManagedForm
```