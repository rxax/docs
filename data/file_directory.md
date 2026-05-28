## Folder management

Get all the folders and files from a given folder:

```python
import os


def get_dir_entries(folder_path: str, scan_subdirs: bool = True, include_dir_results: bool = True):
    """
    Get folder entries from path.
    :param folder_path: The path to the folder
    :param scan_subdirs: Get items from sub-folders too
    :param include_dir_results: Add sub-folder names to the results
    :return: list of path strings
    """
    # get list of folder entries
    if os.path.isfile(folder_path) or not os.path.isdir(folder_path):
        raise ValueError('Invalid path: ' + str(folder_path) + ' (this is not a folder)')
    items = []

    if scan_subdirs:
        # Get files from folder and all sub-folders
        for path, sub_dirs, files in os.walk(folder_path):
            for name in files:
                path = os.path.join(path, name)
                items.append(path)
            if include_dir_results and sub_dirs:
                for dir_name in sub_dirs:
                    items.append(os.path.join(os.path.dirname(path), dir_name))
    else:
        # Get files from the folder_path folder only
        files = os.listdir(folder_path)
        for file in files:
            path = os.path.join(folder_path, file)
            if os.path.isfile(path):
                items.append(path)
            elif include_dir_results:
                items.append(path)
    return items
```

Usage:

```python
all = get_dir_entries("templates")

print('result:')
print('\n'.join(all))
```

Output:

> result:
> 
> templates\test.html
> 
> templates\admin
> 
> templates\admin\list.html
> 
> templates\admin\subadmin
> 
> templates\admin\subadmin\subpage.txt