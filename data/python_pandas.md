## Pandas

Imports:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
DataFrame

```python
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#refer to the row index:
print(df.loc[0])

#Named indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

#refer to the named index:
print(df.loc["day2"])
```
Read SQL query result into a dataframe:

```python
with engine.connect() as con:
    query = """SELECT * FROM products"""
    products_df = pandas.read_sql_query(query, con=con)
    print(products_df['price'])
```

Read SQL table into dataframe:

```python
with engine.connect() as con:
    products_df = pandas.read_sql_table('products', con=con)
    print(products_df['price'])
```

Read CSV with headers:

```python
products_df = pandas.read_csv('products.csv', header=0, names=['name', 'quantity', 'price', 'promotion'])
print(products_df['price'])
```

Efficient reading of a query into a dataframe (works with PostgreSQL):

```python
def read_sql_tmpfile(query, db_engine):
    """ Read query result into pandas using a temp file (75% faster), works with postgresql"""
    with tempfile.TemporaryFile() as tmpfile:
        copy_sql = "COPY ({query}) TO STDOUT WITH CSV {head}".format(
           query=query, head="HEADER"
        )
        conn = db_engine.raw_connection()
        cur = conn.cursor()
        cur.copy_expert(copy_sql, tmpfile)
        tmpfile.seek(0)
        df = pandas.read_csv(tmpfile)
        return df
```

**References:** [Pandas](https://www.datacamp.com/community/blog/python-pandas-cheat-sheet?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=12492439676&utm_adgroupid=122563405321&utm_device=c&utm_keyword=pandas%20cheat%20sheet&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=504158801722&utm_targetid=aud-392016246653:kwd-385658525885&utm_loc_interest_ms=&utm_loc_physical_ms=1007850&gclid=CjwKCAiA_omPBhBBEiwAcg7smQUjwQHcFyQENvCLK4rc6t_05ugzD_HMCS5ci3GKikkBoKdjwgu-HRoCC9UQAvD_BwE)