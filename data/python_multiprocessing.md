### Multi-threading and multiprocessing

Get first command line argument

```python
import sys
# skip filename
argv = sys.argv[1:]
if len(argv) != 0:
    arg1 = argv[0]
else:
    arg1 = 'default value'
```


#### Subprocess

Execute python script as subprocess

```python
import subprocess

process = subprocess.Popen(
    ['./.venv/scripts/python.exe','./uk_indeed_links.py', str(keyword)], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
out, err = process.communicate()

print((process.returncode, out, err))
```
