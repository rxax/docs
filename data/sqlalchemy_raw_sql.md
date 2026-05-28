## SQLAlchemy Execute RAW SQL Statements

```python
from sqlalchemy import create_engine, Table, String, MetaData, Column, Integer
```

Connect to the database:

```python
engine = create_engine('sqlite:///bookstore.db', connect_args={'check_same_thread': False})
```

Execute raw SQL statements:

```python
with engine.connect() as con:

    # Insert one row (Create)
    id = 10
    title = "The Book Title"
    rs = con.execute(f"INSERT INTO book(id,title) VALUES({id},'{title}')")
    print("rows created:", rs.rowcount)

    # Get all rows (Read)
    rs = con.execute("SELECT * FROM book")
    for row in rs:
        print(row)

    # Get one row (Read)
    rs = con.execute(f"SELECT * FROM book WHERE id={id} LIMIT 1")
    row = rs.fetchone()
    if row:
        print(row)

    # update a row  (Update)
    new_title = "New Book Title"
    rs = con.execute(f"UPDATE book set title='{new_title}' WHERE id={id}")
    print("results:", rs.rowcount)
    if rs.rowcount:
        print("Row updated")

    # delete a row (Delete)
    rs = con.execute(f"DELETE FROM book WHERE id={id}")
    print("results:", rs.rowcount)
    if rs.rowcount:
        print("Row deleted")
```
See also [sqlalchemy_metadata.html](sqlalchemy_metadata.html)