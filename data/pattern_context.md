## Context pattern

A Context is a collection of data, often stored in a Map or in a custom class which acts as a struct with accessors and modifiers. It is used for maintaining state and for sharing information within a system.

[See Object Manager Pattern](pattern_manager.html)

### Python Context Interface

Generic Context Manager example:

```python
class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

# Using the context
with ContextManager() as manager:
    print('with statement block')
```


File Manager example:

```python
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)
```

Database Manager example:

```python
from pymongo import MongoClient

class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

# connecting with a localhost
with MongoDBConnectionManager('localhost', '27017') as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({'_id': 1})
    print(data.get('name'))
```