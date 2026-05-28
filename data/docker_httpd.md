## HTTPD

Web server for serving HTML, JS, and CSS files from a folder.

Dockerfile
```html
FROM httpd:2.2.31
RUN mkdir -p /opt/mw/apache-test/logs
COPY htdocs /usr/local/apache2/htdocs
EXPOSE 80
```

Create and run the container:

`docker build -t http-server-img .`

`docker stop http-server`

`docker rm http-server`

`docker run --name  http-server -d --publish 80:80 http-server-img`