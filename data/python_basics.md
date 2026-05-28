## Python basics

Recap:

```python
import json

# Create variables
a = 10
b = "A text message"
c = False

# String concatenation
d = b + str(a) + str(c)
print(d)

# String to int
e = int("10")
print(e)

# Conditional statements
if a >= 10 and not c:
    print('this is true')
else:
    print('this is false')

# Lists
data = [1, 2, 3, "Something"]
length = len(data)
print('data length ', length)

# Get element at index
print(data[2])

# For loop
print('data items:')
for item in data:
    print(item)

# Iterate by index
for i in range(len(data)):
    print(data[i])

# Slice a list
print(data[1:3])

# Add to list
data.append(10)

# Index of item in list
print('the index of 10 is', data.index(10))

# Dictionaries
obj = {'firstname': 'Jhon', 'lastname': 'Doe'}
for key, value in obj.items():
    print('key=', key, ', value=', value)

# To JSON
s = json.dumps(obj)
print(s)

# From JSON
obj = json.loads(s)
print(obj)

# Exceptions
try:
    d = a.upper()
except:
    print('a is not a text')


# Functions
def sum_of_two_numbers(a, b):
    return a + b


print('the sum of', 10, 'and', 15, 'is', sum_of_two_numbers(10, 15))

# Functions: Lambda syntax (single line function)
sum_of_two = lambda a, b: a + b
print('the sum of', 7, 'and', 4, 'is', sum_of_two(7, 4))
```

Output:

> A text message10False
> 
> 10
> 
> this is true
> 
> data length  4
> 
> 3
> 
> data items:
> 
> 1
> 
> 2
> 
> 3
> 
> Something
> 
> 1
> 
> 2
> 
> 3
> 
> Something
> 
> [2, 3]
> 
> the index of 10 is 4
> 
> key= firstname , value= Jhon
> 
> key= lastname , value= Doe
> 
> {"firstname": "Jhon", "lastname": "Doe"}
> 
> {'firstname': 'Jhon', 'lastname': 'Doe'}
> 
> a is not a text
> 
> the sum of 10 and 15 is 25
> 
> the sum of 7 and 4 is 11