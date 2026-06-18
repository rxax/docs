## Model-View-Controller pattern


### The Model

```python
class Person:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
```

### The View

```python
def person_view(p: Person):
    print('Person = {')
    print('first_name:', p.first_name)
    print('last_name:', p.last_name)
    print('}')
```

### The Controller

```python
def create_person(fist_name: str, last_name: str):
    person = Person(fist_name, last_name)
    return person_view(person)
```

Usage:

```python
if __name__ == "__main__":
    # running controller function
    create_person('Andrew', 'Parker')
```

Output:

> Person = {
> 
> first_name: Andrew
> 
> last_name: Parker
> 
> }