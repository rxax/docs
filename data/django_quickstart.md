### Django Quickstart Guide

**Install Django**

`pip install Django`

**Create the Project**

`django-admin startproject mysite`

**Create your app**

`python manage.py startapp app_name`

**Database setup**

- Change models in `models.py`

- Create migrations `python manage.py makemigrations app_name`

- Apply changes to DB / initial setup `python manage.py migrate`

**Admin Setup**

`python manage.py createsuperuser`

**Run Django Server**

`python manage.py runserver`
