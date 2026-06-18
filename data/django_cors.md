## Django Enable CORS Feature

Install dependencies

`python -m pip install django-cors-headers`

then in the `settings.py` file

In the installed apps part:

```python
INSTALLED_APPS = [
    'corsheaders',
    ]
```
At the very top of the Middleware part:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
```
And at the end:

```python
CORS_URLS_REGEX = r'^/api/.*$' #path with cors

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173', #for vite-react
    'http://localhost:5173', #for vite-react
]

CORS_ALLOW_CREDENTIALS = True
```

Note:

Chrome cache's request responses, therefore if CORS is enabled but doesn't seem to work clear the site cache and then try again.