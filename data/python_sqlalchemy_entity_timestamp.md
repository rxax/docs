### SQL Alchemy entity with timestamp dates

Timestamps are int values that enable faster sorting by dates. Note that the example has no timezones.

Imports:

```Python
from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime, time
from datetime import datetime as dt
from sqlalchemy.types import TypeDecorator, Integer
```

Requires a type decorator (new column type). This is used to convert from timestamp to datetime and from datetime to timestamp:

```python
class IntegerDateTime(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, engine):
        """Assumes a datetime.datetime"""
        if isinstance(value, datetime.datetime):
            return int(time.mktime(value.timetuple()))
        elif isinstance(value, float):
            return int(value)
        else:
            raise ValueError("Invalid type for IntegerDateTime value", type(value).__name__)

    def process_result_value(self, value, engine):
        return dt.fromtimestamp(int(value))

    def copy(self):
        return IntegerDateTime()
```

Entity class using the new column type:

```python
Base = declarative_base()

# Define entity class, using created_at and updated_at timestamps (faster db ordering)
class Record(Base):
    __tablename__ = 'records'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True)  # a record should have a name
    # add other fields
    # ...
    created_at = Column(IntegerDateTime, default=time.mktime(dt.now().timetuple()))  # save entity creation time
    updated_at = Column(IntegerDateTime, default=time.mktime(dt.now().timetuple()),
                        onupdate=lambda: time.mktime(dt.now().timetuple()))  # save update datetime

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

Usage:

```python
# Connect to DB and create tables
engine = create_engine('sqlite:///records2.db', connect_args={'check_same_thread': False})
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

> Record(id=1,name='Test1',created_at='2022-01-13 10:56:38',updated_at='2022-01-13 10:56:38')
> 
> Record(id=1,name='Test2',created_at='2022-01-13 10:56:38',updated_at='2022-01-13 10:56:43')
