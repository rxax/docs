## Django ORM Relationships

### One-to-One

Ex.: One department has One manager, One manager has One department

```python
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Department('{self.name}')"


class Manager(models.Model):
    department = models.OneToOneField(Department,
                                      on_delete=models.CASCADE,
                                      primary_key=True,
                                      )  # has primary key
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Manager('{self.name}')"
```

### One-to-Many

Note: the foreign-key is in the child entity.

Examples:

- One order can have many products.
- One area can be the habitat of many readers.
- One reader can have many subscriptions.
- One newspaper can have many subscriptions.

```python
class Order(models.Model):
    client_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Order('{self.client_name}')"


class Product(models.Model):
    name = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')  # no primary key

    def __str__(self):
        return f"Product('{self.name}')"
```

### Many-to-One

Note: the foreign-key is in the parent entity.

Examples:

- Many readers live in one area.
- Many subscriptions can be of one and the same reader.
- Many subscriptions are for one and the same newspaper.

```python
class Subscription(models.Model):
    name = models.CharField(max_length=50)
    newsletter = models.ForeignKey('Newsletter', null=True, related_name='subscriptions', on_delete=models.CASCADE)

    def __str__(self):
        return f"Subscription('{self.name}')"


class Newsletter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Newsletter('{self.name}',{self.subscriptions.all()})"
```

### Many-to-Many

Note: requires an association table.

Examples:

- many customers are registered to many services

```python
class Customer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Customer('{self.name})"


class Service(models.Model):
    name = models.CharField(max_length=50)
    customers = models.ManyToManyField(Customer, related_name='services')

    def __str__(self):
        return f"Services('{self.name})"
```

## Testing

Django unit test for all the relationships above:

```python
from django.test import TestCase

# Create your tests here.
from .models import Department, Manager, Product, Order, Newsletter, Subscription, Customer, Service


class OneToOneModelTests(TestCase):
    def test_one_to_one(self):
        department = Department(name='test_department')
        department.save()  # must save parent first
        manager = Manager(name='Jhon Doe', department=department)
        manager.save()

        print('one-to-one relationship:')
        print('the department for', manager, 'is', manager.department)
        print('the manager for', department, 'is', department.manager)

    def test_one_to_many(self):
        order = Order(client_name="John doe")
        order.save()

        p1 = Product(name='apples', order=order)
        p1.save()
        p2 = Product(name='oranges', order=order)
        p2.save()
        p3 = Product(name='pears', order=order)
        p3.save()

        print('one-to-many relationship')
        print('order with 3 products', order, order.products.all())

    def test_many_to_one(self):
        newsletter = Newsletter(name='The Daily Harold')
        newsletter.save()
        subscription1 = Subscription(name='Anthony Martin')
        subscription2 = Subscription(name='Alex Parker')
        subscription1.newsletter = newsletter
        subscription2.newsletter = newsletter
        subscription1.save()
        subscription2.save()

        print('many-to-one relationship')
        print('newsletter subscriptions for', newsletter)

    def test_many_to_many(self):
        customer1 = Customer(name="Andrew Bold")
        customer1.save()
        customer2 = Customer(name="John Deere")
        customer2.save()
        service1 = Service(name="JustEat")
        service1.save()
        service2 = Service(name="Argos")
        service2.save()

        service1.customers.add(customer1)
        service1.customers.add(customer2)
        service2.customers.add(customer1)
        service2.customers.add(customer2)

        print('many-to-many relationship')
        print('customer1 services', customer1, ':')
        for service in customer1.services.all():
            print('-', service)

        print('customer2 services', customer2, ':')
        for service in customer1.services.all():
            print('-', service)

        print('service1 customers', service1, ':')
        for customer in service1.customers.all():
            print('-', customer)

        print('service2 customers', service2, ':')
        for customer in service2.customers.all():
            print('-', customer)
```

Output:

> many-to-many relationship
> 
> customer1 services Customer('Andrew Bold) :
> 
> - Services('JustEat)
> 
> - Services('Argos)
> 
> customer2 services Customer('John Deere) :
> 
> - Services('JustEat)
> 
> - Services('Argos)
> 
> service1 customers Services('JustEat) :
> 
> - Customer('Andrew Bold)
> 
> - Customer('John Deere)
> 
> service2 customers Services('Argos) :
> 
> - Customer('Andrew Bold)
> 
> - Customer('John Deere)

Output:

> many-to-one relationship
> 
> newsletter subscriptions for Newsletter('The Daily Harold',`<QuerySet [<Subscription: Subscription('Anthony Martin')>, <Subscription: Subscription('Alex Parker')>]>`)

Output:
 
> one-to-many relationship
> 
> order with 3 products Order('John doe') `<QuerySet [<Product: Product('apples')>, <Product: Product('oranges')>, <Product: Product('pears')>]>`

Output:

> one-to-one relationship:
> 
> the department for Manager('Jhon Doe') is Department('test_department')
> 
> the manager for Department('test_department') is Manager('Jhon Doe')

