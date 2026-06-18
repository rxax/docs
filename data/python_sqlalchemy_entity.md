## SQL Alchemy model example (entity)

Imports:

```python
import time

from sqlalchemy import create_engine, String, Column, Integer, DateTime, func, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
```

Define entity class:

```python
class Record(Base):
    __tablename__ = 'records'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True)  # a record should have a name
    # add other fields
    # ...
    created_at = Column(DateTime(timezone=True), default=func.now())  # save creation datetime
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())  # save update datetime

    def __repr__(self):  # String representation of the record
        return "{cls}(id={id},name='{name}',created_at='{created_at}',updated_at='{updated_at}')". \
            format(
                cls=str(self.__class__.__name__),
                id=self.id,
                name=self.name,
                created_at=self.created_at,
                updated_at=self.updated_at
            )
```

Usage example:

```python
# Connect to DB and create tables
engine = create_engine('sqlite:///records.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine, checkfirst=True)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create object
record = Record(name='Test1')
session.add(record)
session.commit()
# get the auto increment value for id
session.refresh(record)

# Get previously inserted object
data = session.query(Record).filter_by(id=record.id).first()
print(data)

# Wait 5 seconds before the update to check the updated_at datetime value
time.sleep(5)

# Update object
record.name = 'Test2'
session.add(record)
session.commit()
data = session.query(Record).filter_by(id=record.id).first()
print(data)

# Delete object
session.delete(record)
session.commit()
```

Output:

> Creating object
>
> Record(id=1,name='Test1',created_at='2022-01-12 18:17:06',updated_at='2022-01-12 18:17:06')
> 
> Updating object
> 
> Record(id=1,name='Test2',created_at='2022-01-12 18:17:06',updated_at='2022-01-12 18:17:11')