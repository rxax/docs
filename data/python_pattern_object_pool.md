## Object pool pattern

The Object Pool design pattern uses a pool of initialized objects that are ready to be used rather than creating a new object all the time. 

```Python
class PoolObject:
    pass

class Pool:
    def __init__(self, size):
        self._objects = [PoolObject() for i in range(size)]

    def get_object(self):
        return self._objects.pop()

    def release_object(self, obj):
        self._objects.append(obj)

```

Usage:

```python
if __name__ == "__main__":
    pool = Pool(10)
    obj1 = pool.get_object()
    pool.release_object(obj1)
```


Example of Database Connection pool implementation:

```python
dbconfig = {  "database": "test", "user":"joe" }
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",pool_size = 3, **dbconfig)
```

Usage:

```python
cnx1 = cnxpool.get_connection()
cnx2 = cnxpool.get_connection()
```

**References:** 

- [Design Patterns](https://able.bio/ZoranPandovski/design-patterns-with-python--941uvwy)
- [Pooling with the DBUtils package](https://webwareforpython.github.io/DBUtils/)