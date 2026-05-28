## Start http server

docker run --name docs_nginx1 -p 80
80:80 -v %cd%/htdocs:/usr/share/nginx/html:ro -v /c/var/log/docs_nginx1:/var/log -d nginx

Run convert to generate docs html

Add md source files to data dir