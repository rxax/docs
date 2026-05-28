## React Router (v6)

Example of navigation with nested paths:

```js
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import ManagedForm from "./components/ManagedForm"
import CustomLinks from "./components/CustomLinks"
import Home from './components/Home'
import {
    BrowserRouter,
    Route,
    Routes,
    Link
} from "react-router-dom"

function App() {
    return (
        <div className="container">

            <BrowserRouter>
                <div className="row">
                    <nav className="navbar navbar-expand-lg navbar-light bg-light">
                        <ul className="navbar-nav">
                            <li className="nav-item"><Link className="nav-link" to="/">Home</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/form">Example form</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/links">Links</Link></li>
                        </ul>
                    </nav>
                </div>


                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route exact path="/form" element={<ManagedForm/>}/>
                    <Route path="/links" element={<CustomLinks/>}>
                        <Route path=":linkid" element={<CustomLinks/>}/>
                    </Route>
                </Routes>
            </BrowserRouter>
        </div>
    )
}

export default App
```

and the CustomLinks component for reference:

```js
import {Link, useParams, useLocation} from "react-router-dom";

const CustomLinks = () => {
    // use path parameters
    let params = useParams()
    // use path location
    let location = useLocation()

    return <>
        <Link to="/links/10">Go to links/10</Link>

        {params.linkid && <p>The path param is {params.linkid}</p>}

        <p>Current location {location.pathname}</p>

        </>
}

export default CustomLinks
```

**Rerefences:** [React-Router](https://reactrouter.com/docs/en/v6/getting-started/overview)