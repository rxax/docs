## Singleton pattern

This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.

It provides a global point of access to the instance created.

```python
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
```

Usage:

```python
s = Singleton()
print('Object signature =', id(s))

s = Singleton.getInstance()
print('Object signature =', id(s))

# Cannot create a singleton object a second time, use getInstance() instead
s = Singleton()
```