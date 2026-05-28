## Flask with uwsgi in Docker

Dockerfile

```html
FROM tiangolo/uwsgi-nginx-flask:python3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY www ./app
WORKDIR ./app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

```

uwsgi.ini file:

```html
[uwsgi]
module = main
callable = app
```

Folder structure:

> www/static
> 
> www/templates
> 
> www/main.py
> 
> www/uwsgi.ini
> 
> Dockerfile

How to start:

`docker build -t flask-app .`

`docker run -d -p 5010:80 --name=flask-app flask-app`