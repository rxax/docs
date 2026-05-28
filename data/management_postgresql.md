## Database Management Commands

### PostgreSQL

Create binary backup

`pg_dump -h localhost -U postgres -W -F t blog > blog.tar`

Create SQL backup

`pg_dump -h localhost -U postgres -W -F p blog > blog.sql`

Restore database from binary backup

`pg_restore -h localhost -U postgres -W -d blog2 -v -F t blog.tar`

Restore database from SQL backup

`psql -h localhost -U postgres -d blog2 -W --set ON_ERROR_STOP=on -f blog.sql`

Delete and create a database:

`dropdb -h localhost -U postgres -f -W blog2`

`createdb -h localhost -U postgres -W blog2`