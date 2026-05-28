## JavaScript Rest client using XMLHttpRequest

Both the client and the server should be on the same domain.

GET request:

```javascript
    function get_request(url, headers, onsuccess, onfailure) {
        // Send GET Request
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE) {
                if ([200].includes(this.status)) {
                    if (typeof onsuccess !== 'undefined') {
                        onsuccess(this);
                    }
                } else {
                    if (typeof onfailure !== 'undefined') {
                        onfailure(this);
                    }
                }
            }
        }
        request.open('GET', url);
        // add request headers
        for (const [key, value] of Object.entries(headers)) {
            request.setRequestHeader(key, value);
        }
        request.send();
    }
```
Usage:

```javascript
    get_request(
        "https://jsonplaceholder.typicode.com/users",
        {'Content-Type': 'application/json'},
        onsuccess = (response) => {
            // list all the users from the API
            const list = JSON.parse(response.responseText);
            document.getElementById('get_test').innerHTML = '';
            list.forEach(item => document.getElementById('get_test').innerHTML += '<p>' + item['name'] + '</p>')
        },
        onfailure = (error) => {
            document.getElementById('get_test').innerHTML = 'Cannot retrieve data.';
        }
    )
```

POST request:

```javascript
    function post_request(url, headers, data, onsuccess, onfailure) {
        // Send Post Request
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE) {
                if ([200, 201].includes(this.status)) {
                    if (typeof onsuccess !== 'undefined') {
                        onsuccess(this);
                    }
                } else {
                    if (typeof onfailure !== 'undefined') {
                        onfailure(this);
                    }
                }
            }
        };

        request.open('POST', url);
        // add request headers
        for (const [key, value] of Object.entries(headers)) {
            request.setRequestHeader(key, value);
        }
        request.send(data);
    }
```

Usage:

```javascript
    post_request(
        'https://my-json-server.typicode.com/typicode/demo/posts',
        {'Content-Type': 'application/json'},
        JSON.stringify({'id': 5, 'title': 'A title'}),
        onsuccess = (response) => {
            document.getElementById('post_test').innerHTML = response.responseText;
        },
        onfailure = (error) => {
            document.getElementById('post_test').innerHTML = error.responseText;
        }
    )
```

DELETE request:

```javascript
    function delete_request(url, headers, onsuccess, onfailure) {
        // Send Post Request
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE) {
                if ([200].includes(this.status)) {
                    if (typeof onsuccess !== 'undefined') {
                        onsuccess(this);
                    }
                } else {
                    if (typeof onfailure !== 'undefined') {
                        onfailure(this);
                    }
                }
            }
        };

        request.open('DELETE', url);
        // add request headers
        for (const [key, value] of Object.entries(headers)) {
            request.setRequestHeader(key, value);
        }
        request.send();
    }
```

Usage:

```javascript
    // Test DELETE request
    delete_request(
        'https://my-json-server.typicode.com/typicode/demo/posts/1',
        {'Content-Type': 'application/json'},
        onsuccess = (response) => {
            document.getElementById('delete_test').innerHTML = response.responseText;
        },
        onfailure = (error) => {
            document.getElementById('delete_test').innerHTML = error.responseText;
        }
    )

```

PUT request:

```javascript
    function put_request(url, headers, data, onsuccess, onfailure) {
        // Send Post Request
        var request = new XMLHttpRequest();

        request.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE) {
                if ([200, 201].includes(this.status)) {
                    if (typeof onsuccess !== 'undefined') {
                        onsuccess(this);
                    }
                } else {
                    if (typeof onfailure !== 'undefined') {
                        onfailure(this);
                    }
                }
            }
        };

        request.open('PUT', url);
        // add request headers
        for (const [key, value] of Object.entries(headers)) {
            request.setRequestHeader(key, value);
        }
        request.send(data);
    }
```

Usage:

```javascript
    put_request(
        'https://my-json-server.typicode.com/typicode/demo/posts/2',
        {'Content-Type': 'application/json'},
        JSON.stringify({'id': 5, 'title': 'A title'}),
        onsuccess = (response) => {
            document.getElementById('put_test').innerHTML = response.responseText;
        },
        onfailure = (error) => {
            document.getElementById('put_test').innerHTML = error.responseText;
        }
    )
```

HTML for testing:

```html
<h3>GET:</h3>
<div id="get_test">fetching...</div>

<h3>POST:</h3>
<div id="post_test"></div>

<h3>DELETE:</h3>
<div id="delete_test"></div>

<h3>UPDATE:</h3>
<div id="put_test"></div>
```

**References:**: [a note on cors](https://hacks.mozilla.org/2009/07/cross-site-xmlhttprequest-with-cors/)