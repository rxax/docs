## SQL Alchemy Programmatic SQL
```python
from sqlalchemy import create_engine, Table, String, MetaData, Column, Integer, text
from sqlalchemy.orm import sessionmaker
```

Define the table:
```python
metadata = MetaData()
books = Table('book', metadata,
  Column('id', Integer, primary_key=True),
  Column('title', String),
)
```

Connect to DB and create tables:
```python
engine = create_engine('sqlite:///bookstore.db', connect_args={'check_same_thread': False})
metadata.create_all(engine, checkfirst=True)
```

Create session or use a connection:
```python
Session = sessionmaker(bind=engine)
session  = Session()
```

CRUD operations:
```python
# Create object
insert_stmt = books.insert().values(id=1,  title="Book Title")
result = session.execute(insert_stmt)
print("inserted rows", result.rowcount)

# Read object
select_stmt = books.select().where(text('id=1')).limit(1)
result = session.execute(select_stmt)
data = result.fetchone()
if data:
  print(data)
  
# Read all objects
select_stmt = books.select()
result = session.execute(select_stmt)
for data in result:
  if data:
    print(data)

# Update object
update_stmt = books.update(whereclause=text('id=1')).values(id=1,  title="New Book Title")
result = session.execute(update_stmt)
print("updated rows", result.rowcount)

# Delete object
delete_stmt = books.delete(whereclause=text('id=1'))
result = session.execute(update_stmt)
print("deleted rows", result.rowcount)
```