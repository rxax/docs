## Flask Before and After request methods

Can be used as request filters or interceptors.

### Example of API/APP KEY filtering

```python
from flask import Flask, Response, request, abort
from werkzeug.routing import BaseConverter
```

Before and after request functions:

```python
@app.before_request
def before_request_func():
    """
    Intercept illegal APP KEYs
    :return:
    """
    print(request.path)
    paths = request.path.split('/')
    app_key = paths[2]
    print("received app key", app_key)
    if app_key != 'VALIDAPIKEY':
        abort(403)


@app.after_request
def after_request_func(response):
    return response
```
Usage:

```python
@app.route('/api/<string:appid>/test')
def test(appid):
    return Response(response="All Good", status=200)
```

Accepted path: 
> http://127.0.0.1:5000/api/VALIDAPIKEY/test