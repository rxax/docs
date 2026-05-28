## Iterator pattern

Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

```python
class IterableObject:

    def __init__(self, elements: list):
        self.elements = elements
        self.index = 0
        self.count = len(elements)

    def next(self):
        if self.has_more_elements():
            element = self.elements[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration()

    def has_more_elements(self):
        if self.count > 0:
            return self.index < self.count
        return False

```

Usage:

```python
objects = ['a', 'b', 'c', 'd', 'e']
iterator = IterableObject(objects)

while iterator.has_more_elements():
    item = iterator.next()
    print(item)

print('after traversing the iterator, do we have objects left to visit?', iterator.has_more_elements())
```

Output:

> a
> 
> b
> 
> c
> 
> d
> 
> e
> 
> after traversing the iterator, do we have objects left to visit? False

Note: The objects are traversed a single time. To traverse them again a new iterator is needed.


### Python Iterator

```python
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
```

Output:

> 1
> 
> 2
> 
> 4
>
> 8
> 
> Traceback (most recent call last):
> 
>   File "/home/bsoyuj/Desktop/Untitled-1.py", line 32, in <module>
> 
>     print(next(i))
> 
>   File "<string>", line 18, in __next__
> 
>    raise StopIteration
> 
> StopIteration

A python iterator can be used in for loops. E.g.:

```python
for item in numbers:
    print(item)
```