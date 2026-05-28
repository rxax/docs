## Nginx 

Serve static content (ex: react build)

`docker run --name nginx1 -v /build:/usr/share/nginx/html:ro -d nginx`

Windows:

`docker run --name nginx1 -p 8080:80 -v %cd%/build:/usr/share/nginx/html:ro -v /c/var/log/nginx1:/var/log -d nginx`