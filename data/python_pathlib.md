## Get file name, extension, and parent director / folder name

```python
import pathlib
```

Get file name and extension:
```python
win_path = "c:\\users\\folder\\file1.txt"
result = pathlib.Path(win_path).name
print(result)

linux_path = "/users/folder/file2.txt"
result = pathlib.Path(linux_path).name
print(result)
```
Output:

> file1.txt

> file2.txt


Get file name without extension:
```Python
win_path = "c:\\users\\folder\\file1.txt"
result = pathlib.Path(win_path).stem
print(result)

linux_path = "/users/folder/file2.txt"
result = pathlib.Path(linux_path).stem
print(result)
```

Output:

> file1

> file2

Get file extension:

```Python
win_path = "c:\\users\\folder\\file1.txt"
result = pathlib.Path(win_path).suffix
print(result)

linux_path = "/users/folder/file2.txt"
result = pathlib.Path(linux_path).suffix
print(result)

```
Output:

> .txt

> .txt


Get parent folder / directory:

```Python
win_path = "c:\\users\\folder\\file.txt"
result = str(pathlib.Path(win_path).parent)
print(result)

linux_path = "/users/folder/file.txt"
result = str(pathlib.Path(linux_path).parent)
print(result)
```

Output:

> c:\users\folder
> 
> \users\folder

### Helper function for path splitting

Function that extracts the file name, extension, and dir name from a given path string.

```Python

import pathlib
from collections import defaultdict, namedtuple

def split_path(path, as_object=False):
    result = defaultdict(lambda: "")
    p = pathlib.Path(path)
    result['basename'] = result['filename'] = result['file_name'] = p.name
    result['name'] = p.stem
    result['extension'] = result['ext'] = p.suffix
    result['dir'] = result['parent'] = str(p.resolve().parent)
    result['path'] = p

    if as_object:
        # convert dict to namedtuple
        return namedtuple("path_info", result.keys())(*result.values())
    else:
        return result

```

Example usage:
```Python
file_path = "c:\\users\\folder\\file.txt"
# Get ressults as dict
x = split_path(file_path)
print('file name', x['filename'])
```

```python
#Get results as an object
x = split_path(path, as_object=True)
print('file name', x.filename)
```