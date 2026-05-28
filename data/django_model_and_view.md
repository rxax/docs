## Django Models and Views

### Models

Imports:

```python
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
```

Model with UUID instead of ID as primary key, with absolute_url

```python
class Book(models.Model):
    # Use UUID as primary key instead of numbers
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    # Used to get the url to the object in the templates
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
```

Django model with foreign key (many-to-one) and user_model

```python
class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
```

### Views

Imports:

```python
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Book
```

ListView class, used to list objects

```python
class BookListView(ListView):
    model = Book
    # Accessible in the template files
    context_object_name = 'books_list'
    template_name = 'books/book_list.html'
```

ListDetail class, used to show one object

```python
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
```

ListView with overwritten queryset

```python
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    # What to sow in the list view
    def get_queryset(self):
        # Get the query value from request
        query = self.request.GET.get('q')

        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
```

Example of view function, for reference

```python
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```


### Complete test for Book and Review models

```python
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Book, Review


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')

        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())

        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')  # new
        self.assertTemplateUsed(response, 'books/book_detail.html')

```