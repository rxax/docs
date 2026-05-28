##  Flask - Manage API Keys in Memory

```python
import uuid
from collections import namedtuple
from functools import wraps
from flask import Flask, Response, request, abort
```

The API key contains a UUID-based key, and an IP address associated with the key.

Define the API Key and the API Key Manager:

```python
APIKey = namedtuple('APIKey', ['key', 'ip'])


class ApiKeyManager:
    keys = []

    @classmethod
    def generate_key(cls, ip: str):
        return APIKey(key=str(uuid.uuid4()).replace('-', ''), ip=ip)

    @classmethod
    def register_key(cls, api_key: APIKey):
        cls.keys.append(api_key)
        print(api_key, 'added to registry')

    @classmethod
    def unregister_key(cls, api_key: APIKey):
        cls.keys = [key_obj for key_obj in cls.keys if key_obj.key != api_key.key]
        print(api_key, 'removed from registry')

    @classmethod
    def get_api_key(cls, key: str):
        # filter api_keys by key
        match = [api_key for api_key in cls.keys if api_key.key == key]
        if len(match) == 1:
            return match[0]
        else:
            return None

    @classmethod
    def validate_api_key(cls, key, ip):
        if key is None or ip is None:
            return False
        api_key = cls.get_api_key(key)
        if api_key is None:
            return False
        elif api_key.key == key and api_key.ip == "0.0.0.0":
            return True
        elif api_key.key == key and api_key.ip == ip:
            return True
        return False
```

Create route decorator function:

```python
def require_app_key(f):
    """
    @param f: flask function
    @return: decorator, return the wrapped function or abort json object.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # get key from headers
        key = request.headers.get('api-key')
        if ApiKeyManager.validate_api_key(key, request.remote_addr):
            return f(*args, **kwargs)
        else:
            print("Unauthorized address trying to use API: " + request.remote_addr)
            abort(401)

    return decorated
```

Add the decorator to the protected routes:

```python
@app.route('/test')
@require_app_key
def test():
    return Response(response="All Good", status=200)
```

Test the API Key Manager:

```python
# Create API key
api_key = ApiKeyManager.generate_key("0.0.0.0")
print('generated test api key', api_key)

#  Add key to Manager
ApiKeyManager.register_key(api_key)
api_key = ApiKeyManager.get_api_key(api_key.key)
print('api key retrieved', api_key)

# Remove key from Manager
ApiKeyManager.unregister_key(api_key)
```