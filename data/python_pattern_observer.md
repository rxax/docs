# Observer pattern

In this pattern, objects are represented as observers that wait for an event to trigger. An observer attaches to the subject once the specified event occurs. As the event occurs, the subject tells the observers that it has occurred.

```python
# the observer class
class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, subject) -> None:
        # handle updates from observer
        print(self.name, "- notification received from Subject")


# the Subject class
class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        # attach observer object
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # remove observer
        self._observers.remove(observer)

    def notify(self) -> None:
        # notify all observers
        for observer in self._observers:
            observer.update(self)
```

Usage:

```python
sub = Subject()

observer1 = Observer('obs1')
sub.attach(observer1)

observer2 = Observer('obs2')
sub.attach(observer2)

# notify observers about an event
sub.notify()
```
Output:

> obs1 - notification received from Subject
>
> obs2 - notification received from Subject