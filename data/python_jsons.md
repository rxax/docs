## JSON package

```python
import json
```

Convert JSON string to Object:
```python
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
```

Convert Object to JSON string:

```python
person_dict = {'name': 'Bob', 'age': 12, 'email': 'bob123@gmail.com' }
person_json = json.dumps(person_dict)
```

Read JSON from file:

```python
with open("data.json", "r") as file
    persondict = json.load(file)
```
Write Object to JSON file:

```python
with open("data.json", "w") as file:
    json.dump(person_dict, file)
```

### JSONS package

Convert objects into dicts or (json) strings and back.

Example:

```python
import jsons

# Object
class Person:
    name: str
    birthday: datetime

p = Person('Guido van Rossum', birthday)

# convert Object to JSON string (serialize)
out = jsons.dump(p)

# convert JSON string to Object (deserialize)
p2 = jsons.load(out, Person)
```

**References**: [jsons package](https://pypi.org/project/jsons/)