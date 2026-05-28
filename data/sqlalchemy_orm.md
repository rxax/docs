## SQL Alchemy ORM CRUD operations

```python
from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
```

Define entity class:

```python
Base = declarative_base()

# Define entity class
class Book(Base):
    __tablename__ = 'books'
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
```

Connect to the database:

```python
# Connect to DB and create tables
engine = create_engine('sqlite:///bookstore.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine, checkfirst=True)
```

Create sesssion:

```python
# Create session
Session = sessionmaker(bind=engine)
session = Session()
```

### CRUD operations

Create object:

```python
book1 = Book(id=1, title="First Book")
session.add(book1)
try:
    session.commit()
    print("entry updated")
except:
    session.rollback()
    print("update failed")
```

Read object:

```python
book1 = session.query(Book).filter_by(id=1).first()
print(book1.title)
```

Read all objects:

```python
books = session.query(Book).all()
for book in books:
    print(book.title)
```

Update object:

```python
book1 = session.query(Book).filter_by(id=1).first()
book1.title = "New Title"
try:
    session.commit()
    print("entry updated")
except:
    session.rollback()
    print("update failed")
```

Update object from dict:

```python
book1 = session.query(Book).filter_by(id=1).first()
book_dict = {'title': 'A new title'}
for key, value in book_dict.items():
    setattr(book1, key, value)
try:
    session.commit()
    print("entry updated")
except:
    session.rollback()
    print("update failed")
```

Delete object:

```python
book1 = session.query(Book).filter_by(id=1).first()
session.delete(book1)
try:
    session.commit()
    print("entry deleted")
except:
    session.rollback()
    print("update failed")
```