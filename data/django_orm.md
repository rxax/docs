## Django ORM CRUD operations

Define the model:

```python
class Book(models.Model):
    title = models.CharField(max_length=50)
```

### CRUD operations

Create object:

```python
book = Book(title='This is a book')
book.save()
# get the book id
id = book.id
print(id)
```

Read object:

```python
# with filter
book = Book.objects.filter(title__startswith='This')
print(book[0].title)

# with get id
book = Book.objects.get(id=id)
print(book.title)

# with get by field value
book = Book.objects.get(title='This is a book')
print(book.title)
```

Read all objects:

```python
books = Book.objects.all()
for book in books:
    print(book.title)
```

Update object:

```python
book = Book.objects.filter(title__endswith='a book').first()
book.title = 'A new title'
book.save()
print(book.title)
```

Delete object:

```python
book = Book.objects.filter(title__endswith='new title').first()
book.delete()
```