## JavaScript Fetch API usage

Both the client and the server should be on the same domain. Mind the CORS requirements.

Flask backend should send the Access-Control-Allow-Origin header.

```python
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
```

### Fetch API

```javascript
// Get request
fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('get_request').innerHTML = JSON.stringify(data);
    });


// POST request: send JSON
const data = {username: 'example'};
fetch('https://jsonplaceholder.typicode.com/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById('post_request').innerHTML = JSON.stringify(data);
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('post_request').innerHTML = error;
    });

// POST request with CORS enabled
fetch('http://localhost:5000/member', {
    method: 'POST', // PUT, DELETE, etc
    mode: 'cors', // no-cors, *cors, same-origin
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({'username': 'test'}),
})
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById('cors_post_request').innerHTML = JSON.stringify(data);
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('cors_post_request').innerHTML = error;
    });
```

Html for testing:

```html
<h3>Get request:</h3>
<div id="get_request"></div>

<h3>Post request:</h3>
<div id="post_request"></div>

<h3>Post request (CORS):</h3>
<div id="cors_post_request"></div>
```

**References:** [FetchAPI](References: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)