## JQuery Ajax Example

Import JQuery:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
```

The code is usually placed inside `$(document).ready(()=>{...})`:

```javascript
// GET Request
$.ajax({
    url: "https://jsonplaceholder.typicode.com/users",
    type: "GET",
    dataType: "json",
    success: function (data) {
        document.getElementById('get_request').innerHTML = JSON.stringify(data);
    },
    error: function (err) {
        document.getElementById('get_request').innerHTML = 'cannot fetch data';
    }
});

// POST Request
data = {username: 'test', password: 'pass'}
$.ajax({
    type: "POST",
    url: "https://jsonplaceholder.typicode.com/users",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (data) {
        document.getElementById('post_request').innerHTML = JSON.stringify(data);
    },
    error: function (err) {
        document.getElementById('post_request').innerHTML = 'cannot post data';
    }
});

// POST Request with cors
data = {username: 'test', password: 'pass'}
$.ajax({
    type: "POST",
    url: "https://jsonplaceholder.typicode.com/users",
    crossDomain: true,
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (data) {
        document.getElementById('cors_post_request').innerHTML = JSON.stringify(data);
    },
    error: function (err) {
        document.getElementById('cors_post_request').innerHTML = 'cannot post data';
    }
});


// PUT Request
data = {username: 'test', password: 'pass'}
$.ajax({
    type: "PUT",
    url: "https://jsonplaceholder.typicode.com/users/1",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (data) {
        document.getElementById('put_request').innerHTML = JSON.stringify(data);
    },
    error: function (err) {
        document.getElementById('put_request').innerHTML = 'cannot post data';
    }
});

// DELETE Request
$.ajax({
    type: "DELETE",
    url: "https://jsonplaceholder.typicode.com/users/1",
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (data) {
        document.getElementById('delete_request').innerHTML = JSON.stringify(data);
    },
    error: function (err) {
        document.getElementById('delete_request').innerHTML = 'cannot post data';
    }
});
```

HTML for the output:

```html
<h3>Get request:</h3>
<div id="get_request"></div>

<h3>Post request:</h3>
<div id="post_request"></div>

<h3>Post request (CORS):</h3>
<div id="cors_post_request"></div>

<h3>Put request:</h3>
<div id="put_request"></div>

<h3>Delete request:</h3>
<div id="delete_request"></div>
```