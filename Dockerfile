FROM httpd:2.2.31
RUN mkdir -p /opt/mw/apache-test/logs
# ADD ./httpd-custom.conf /usr/local/apache2/conf/httpd.conf
COPY htdocs /usr/local/apache2/htdocs
EXPOSE 80