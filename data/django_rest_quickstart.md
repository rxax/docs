## Django Rest Quickstart

### Setup

Create a database in postgres:

`createdb -h localhost -U postgres -W django_database`

Create a simple python project (with virtual environment)

[ from IDE or command line ]

Install dependencies for Django, DjangoRest and Postgres:

```html
pip install Django

pip install djangorestframework

pip install psycopg2
```

Create the django project:

```html
django-admin startproject app
```

Create a new django app inside the project:

```html
cd app
python manage.py startapp base1
```

Update `app/settings.py` from the django project to include Postgres and DjangoREST:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_01',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": [ "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
}
```

Add DjangoREST, and the newly created app to `app/settings.py`:

```python
INSTALLED_APPS = [
    'rest_framework',
    'base1',
    ...
]
```

Prepare the datababse tables for first use:

```html
python manage.py migrate
```

Add the root user:

```html
python manage.py createsuperuser
```

Test the server:

```html
python manage.py runserver
```

### Using the new app

Create the models in `base1/models.py`:

```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
```

Create the model serializer classes in `base1/serializers.py`:

```python
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description"]
```

Add the model to the admin panel in `base1/admin.py`:

```python
@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
```

Create the view classes in `base1/views.py`

```python
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_view_name(self):
        return "Article List"


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_view_name(self):
        return "Article Detail"
```



Update the `base1/urls.py` to use the view classes:

```python
urlpatterns = [
    path("articles/", ArticleList.as_view(),
         name="rest_article_list"),
    path(
        "articles/<int:pk>/", ArticleDetail.as_view(),
        name="rest_article_detail"
    )
]
```

Link the urls with the django project `app/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("base1.urls")),
]
```

Apply the database changes for the new models:

```html
python manage.py makemigrations

python manage.py migrate
```

Test the server:

```html
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/api/articles/`


### Pagination Explained

```python
class ProductListView(generics.ListAPIView):
    """List products for the selected organization.

    The catalog page calls this with three filters:
      - `org`: only show products belonging to this organization
      - `min_rating`: only show products rated at or above this value
      - `published_only`: only count published reviews in the rating/count
    """

    serializer_class = ProductSerializer
    pagination_class = ResultsSetPagination # This is the pagination class
    paginate_by = 10


    def get_queryset(self):

        queryset = Product.objects.all()
        # if we have pages
        if self.request.query_params.get("page"):

            min_rating = self.request.query_params.get("min_rating")
            if min_rating:
                return queryset.filter(reviews__rating__gte=min_rating)
            else:
                # return without filtering
                return queryset


        # return no data when no page is selected (frontend error scenario)
        return Product.objects.none()
```

The pagination class

```python
class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
```

Also the changes for `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
```