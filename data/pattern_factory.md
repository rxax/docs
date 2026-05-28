## Factory pattern

The factory pattern comes under the creational patterns list category. It provides one of the best ways to create an object. In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface.

```python
# Types of objects
class HTMLTag(object):
    html = ""

    def __str__(self):
        return self.html


class Image(HTMLTag):
    html = "<img></img>"


class Input(HTMLTag):
    html = "<input></input>"


# Object factory
class HTMLTagFactory:

    def create(self, type: str):
        # Create object of a given type
        target_class = type.capitalize()
        return globals()[target_class]()
```

Usage:

```python
factory = HTMLTagFactory()

image_tag = factory.create('image')
print(image_tag)

input_tag = factory.create('input')
print(input_tag)
```

Output:

> `<img></img>`
> 
> `<input></input>`