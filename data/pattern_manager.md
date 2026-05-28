### Manager/Repository pattern

This design pattern can be applied whenever a system needs to support many entities of same or similar type. The Manager object is designed to keep track of all the entities. In many cases, the Manager will also route messages to individual entities.

```python
## The managed object
class Product:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)

# The object manager class
class Manager:
    def __init__(self):
        self.products = []

    def add(self, p):
        if isinstance(p, Product):
            self.products.append(p)
        else:
            raise Exception("object is not a Product")

    def get(self, _id):
        _result = [p for p in self.products if p.id == _id]
        if len(_result) == 1:
            return _result[0]
        else:
            return None

    def remove(self, _id):
        self.products = [p for p in self.products if p.id != _id]

    def update(self, _id, p):
        if not isinstance(p, Product):
            raise Exception("object is not a Product")
        if self.get(_id):
            p.id = _id
            self.products = [p if x.id == _id else x for x in self.products]
            return True
        else:
            return False

    def count(self):
        return len(self.products)

    def clear(self):
        self.products = []
```

Usage:

```python
if __name__ == '__main__':

    # add 3 products
    p1 = Product(1)
    p2 = Product(5)
    p3 = Product(10)

    m = Manager()
    m.add(p1)
    m.add(p2)
    m.add(p3)

    print("product count", m.count())

    # get existing element
    p1 = m.get(1)
    print('get element with id 1 =', p1)

    # remove element
    m.remove(1)
    p1b = m.get(1)
    print('get element with id 1 after removal =', p1b)

    # update element
    result = m.update(10, p1)
    p2b = m.get(10)
    print('update result =', result, ', updated element =', p2b)

    # update non-existing element
    p1 = Product(12)
    print('new product =', p1)
    result = m.update(2, p1)
    px = m.get(2)
    print('update result =', result, ', retrieved product =', px)

```

Output:

> product count 3
> 
> get element with id 1 = Product(1)
> 
> get element with id 1 after removal = None
> 
> update result = True , updated element = Product(10)
> 
> new product = Product(12)
> 
> update result = False , retrieved product = None

**References:** [Manager Pattern](https://www.eventhelix.com/design-patterns/manager/)