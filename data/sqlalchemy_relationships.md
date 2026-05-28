## SQLAlchemy Relationships

```python
import os

from sqlalchemy import create_engine, String, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()
```


### One-to-One

Ex.: One department has One manager, One manager has One department

```python
class Department(Base):
    __tablename__ = 'departments'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    manager = relationship("Manager", back_populates="department", uselist=False)

    def __repr__(self):
        return f"Department({self.id},'{self.name}')"


class Manager(Base):
    __tablename__ = 'managers'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="manager")

    def __repr__(self):
        return f"Manager({self.id},'{self.name}')"
```

### One-to-Many

Note: the foreign-key is in the child entity.

Examples:

- One order can have many products.
- One area can be the habitat of many readers.
- One reader can have many subscriptions.
- One newspaper can have many subscriptions.

```python
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String)
    products = relationship("Product", back_populates="orders", lazy='joined')

    def __repr__(self):
        return f"Order({self.id},'{self.client_name}',{self.products})"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    order_id = Column(Integer, ForeignKey('orders.id'))
    orders = relationship("Order", back_populates="products")

    def __repr__(self):
        return f"Product({self.id},'{self.name}')"
```

### Many-to-One

Note: the foreign-key is in the parent entity.

Examples:

- Many readers live in one area.
- Many subscriptions can be of one and the same reader.
- Many subscriptions are for one and the same newspaper.


```python
class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    newsletter_id = Column(Integer, ForeignKey('newsletters.id'))
    newsletter = relationship("Newsletter", back_populates="subscriptions")

    def __repr__(self):
        return f"Subscription({self.id},'{self.name}')"


class Newsletter(Base):
    __tablename__ = 'newsletters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    subscriptions = relationship("Subscription", back_populates="newsletter", lazy='joined')

    def __repr__(self):
        return f"Newsletter({self.id},'{self.name}',{self.subscriptions})"
```

### Many-to-Many

Note: requires an association table.

Examples:

- many customers are registered to many services

```python
association_table = Table('customer_service', Base.metadata,
                          Column('customer_id', ForeignKey('customers.id'), primary_key=True),
                          Column('service_id', ForeignKey('services.id'), primary_key=True)
                          )


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    services = relationship(
        "Service",
        secondary=association_table,
        back_populates="customers",
        lazy='joined')

    def __repr__(self):
        return f"Customer({self.id},'{self.name}')"


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    customers = relationship(
        "Customer",
        secondary=association_table,
        back_populates="services",
        lazy='joined')

    def __repr__(self):
        return f"Services({self.id},'{self.name}')"
```

Example usage:

````python
# Connect to DB and create tables
engine = create_engine('sqlite:///' + db_file, connect_args={'check_same_thread': False})
Base.metadata.create_all(engine, checkfirst=True)

# Create session
Session = sessionmaker(bind=engine)
session = Session()
````

### Testing one-to-one

```python
department = Department(name='Sales')
manager = Manager(name='Brown Thomas')
manager.department = department
session.add(manager)  # department is saved automatically too
session.commit()
session.refresh(manager)

print('one-to-one relationship:')
print('the department for', manager, 'is', manager.department)
print('the manager for', department, 'is', department.manager)
```

Output:

> one-to-one relationship:
>
> the department for Manager(1,'Brown Thomas') is Department(1,'Sales')
>
> the manager for Department(1,'Sales') is Manager(1,'Brown Thomas')

### Testing one-to-many

```python
product1 = Product(name='apples')
product2 = Product(name='oranges')
product3 = Product(name='lemons')
order = Order(client_name='Jhon Doe')
order.products.append(product1)
order.products.append(product2)
order.products.append(product3)
session.add(order)
session.commit()
session.refresh(order)
print('one-to-many relationship')
print('order with 3 products', order)
```

Output:

> one-to-many relationship 
> 
> order with 3 products Order(1,'Jhon Doe',[Product(1,'apples'), Product(2,'oranges'), Product(3,'lemons')])


### Testing many-to-one

```python
newsletter = Newsletter(name='The Dayly Harold')
subscription1 = Subscription(name='Anthony Martin')
subscription2 = Subscription(name='Alex Parker')
subscription1.newsletter = newsletter
subscription2.newsletter = newsletter
session.add(newsletter)
session.commit()
session.refresh(newsletter)
print('many-to-one relationship')
print('newsletter subscriptions for', newsletter)
```

Output:

> many-to-one relationship 
> 
> newsletter subscriptions for Newsletter(1,'The Dayly Harold',[Subscription(1,'Anthony Martin'), Subscription(2,'Alex Parker')])


### Testing many-to-many

```python
customer1 = Customer(name="Andrew Bold")
customer2 = Customer(name="John Deere")
service1 = Service(name="JustEat")
service2 = Service(name="Argos")
service1.customers.append(customer1)
service1.customers.append(customer2)
service2.customers.append(customer1)
service2.customers.append(customer2)
session.add(service1)
session.add(service2)
session.commit()
session.refresh(service1)
session.refresh(service2)

print('many-to-many relationship')
print('customer1 services', customer1, ':')
for service in customer1.services:
    print('-', service)

print('customer2 services', customer2, ':')
for service in customer1.services:
    print('-', service)

print('service1 customers', service1, ':')
for customer in service1.customers:
    print('-', customer)

print('service2 customers', service2, ':')
for customer in service2.customers:
    print('-', customer)
```

Output:

> many-to-many relationship
> 
> customer1 services Customer(1,'Andrew Bold') :
> 
> - Services(1,'JustEat')
> 
> - Services(2,'Argos')
> 
> customer2 services Customer(2,'John Deere') :
> 
> - Services(1,'JustEat')
> 
> - Services(2,'Argos')
> 
> service1 customers Services(1,'JustEat') :
> 
> - Customer(2,'John Deere')
> 
> - Customer(1,'Andrew Bold')
> 
> service2 customers Services(2,'Argos') :
> 
> - Customer(2,'John Deere')
> 
> - Customer(1,'Andrew Bold')
