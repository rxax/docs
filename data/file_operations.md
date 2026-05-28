## File operations

Read CSV file with a header:

```python
entries = []
file = open("data.csv", "r")
next(file)
for line in file:
    data = line.rstrip().split(',')
    entries.append(data)
    print(data)
file.close()
```

Append to CSV file:

```python
product = ['Tomatoes', '11', '8']
with open("data.csv", "a") as file:
    file.write('\n')
    file.write(','.join(product))
```

Write CSV file with a header:

```python
with open("data_out.csv", "w") as file:
    file.write("Product,Price,Quantity")
    for values in entries:
        file.write('\n')
        file.write(','.join(values))
```

Read JSON file:

```python
import json
with open("data.json", "r") as file:
    entries_list = json.load(file)
    print(entries_list)
```

Write JSON file:

```python
with open("data.json", "w") as file:
    json.dump(entries, file)
```

Append to JSON file:

```python
new_entry = ['Potatoes', '11', '3']
with open("data.json", "r") as file:
    entries_list = json.load(file)
    entries_list.append(new_entry)
    with open("data_out.json", "w") as out_file:
        json.dump(entries_list, out_file)
```

Write bytes to file:

```python
with open("data.bin", "wb") as f:
    f.write(bytearray("Hello Python!".encode("utf-8")))
```

Read bytes from file:

```python
import mmap
with open("data.bin", "rb") as file:
    m = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    ba = bytearray(m)
    print(ba)
```
