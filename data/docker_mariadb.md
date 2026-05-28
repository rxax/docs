## MariaDB

Pull image and create the container:

`docker pull mariadb:10.4`

`docker run --name mariadb1 -e MYSQL_ROOT_PASSWORD=password -p 3307:3306 -d mariadb:10.4`

`docker ps`

Change restart policy to 'always':

`docker update --restart always mariadb1`

Connect to container:

`docker exec -it mariadb1 bash`

Set external volume (persist data):

`docker run --name mariadb1 -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -p 3307:3306 -d mariadb:10.4`
