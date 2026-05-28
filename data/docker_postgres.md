## PostgreSQL

Start container:

`docker run --name postgres1 -p 1000:5432 -e POSTGRES_PASSWORD=password -d postgres:14`

Connect to the containers postgres instance:

`psql postgresql://postgres:password@localhost:1000/postgres`