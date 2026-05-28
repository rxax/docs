## SQLAlchemy Metadata usage

```python
from sqlalchemy import create_engine, Table, String, MetaData, DateTime, Column, Integer, func
from sqlalchemy.orm import sessionmaker
```

Define the table:
```python
metadata = MetaData()
books = Table('book', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('title', String),
              Column('created_at', DateTime(timezone=True), default=func.now()),
              Column('updated_at', DateTime(timezone=True), default=func.now(), onupdate=func.now())
              )
```

Connect to DB and create tables:
```python
engine = create_engine('sqlite:///bookstore.db', connect_args={'check_same_thread': False})
metadata.create_all(engine, checkfirst=True)
```