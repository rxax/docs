## Logrotate

Enable log rotation to keep disk usage low.

```Dockerfile
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y logrotate

COPY logrotate.conf ./logrotate.conf

RUN logrotate -f ./logrotate.conf
```

Logrotate config file (logrotate.conf):

```html
compress

/var/log/nginx/access.log {
    size 10M
    rotate 5
    missingok
}
```

Add all log files and folders as configuration entries in the config file.