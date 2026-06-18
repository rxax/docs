# markdown_to_html.py
#
# Convert a Markdown file to HTML.
#
# Usage:
#   python markdown_to_html.py input.md output.html
#
# Install dependency first:
#   pip install markdown
import os
import re
import shutil
import sys
import markdown
from pathlib import Path
from bs4 import BeautifulSoup

def replace_extension(path: str, new_ext: str) -> str:
    """
    Replace the file extension of a path.

    Args:
        path: Original file path.
        new_ext: New extension (with or without leading dot).

    Returns:
        Path with replaced extension.
    """
    if not new_ext.startswith("."):
        new_ext = "." + new_ext

    return str(Path(path).with_suffix(new_ext))



def write_to_file(filename, text):
    """
        Python function to write file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def markdown_to_html(markdown_text: str) -> str:
    """
    Convert Markdown text to HTML.

    Args:
        markdown_text: Markdown-formatted string

    Returns:
        HTML string
    """
    return markdown.markdown(markdown_text, extensions=['tables','markdown.extensions.fenced_code'])

def read_file(file_path):
    """
    Reads and returns the contents of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File contents.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"


def read_all_files(folder_path, pattern="*"):
    """
    Read all files in a folder and return a dictionary:
    {
        "filename": "file contents"
    }

    Args:
        folder_path (str): Path to the folder
        pattern (str): File pattern (default "*" = all files)

    Returns:
        dict
    """
    folder = Path(folder_path)
    contents = {}

    for file_path in folder.glob(pattern):
        if file_path.is_file():
            try:
                contents[file_path.name] = file_path.read_text(encoding="utf-8")
            except Exception as e:
                contents[file_path.name] = f"ERROR: {e}"

    return contents


def copy_folder(src, dst):
    """
    Copy a folder and all its contents to another location.

    Args:
        src (str or Path): Source folder path
        dst (str or Path): Destination folder path
    """
    src = Path(src)
    dst = Path(dst)

    # Copy entire directory tree
    shutil.copytree(src, dst, dirs_exist_ok=True)

def clear_folder(folder_path):
    """
    Delete all files and subfolders inside a folder,
    but keep the folder itself.
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # remove file or symlink
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # remove directory
        except Exception as e:
            print(f"Failed to delete {item_path}: {e}")

def make_sidebar_html(data: list) -> str:
    """
        Generate ul li pairs from file names
        Example
        python_sys_datetime.md becomes <ul><label>Python</label><ul><li>sys datetime</li></ul></ul>
        Multiple files from the same category are grouped together
    """

    def __unpack_results(top_category:str, entries: list[list])->str:
        """
        Crearte a neat anchor list from the nested data
        like: [['model', 'and', 'view'], ['orm'], ['relationships']]
        """
        result = ''
        link_start = '<li class="col-12"><a class="page" href="'
        link_end = '</li></a>'

        for items in entries:

            # put default label name
            if len(items) == 0 and items is not []:
                label = top_category
                href = top_category
            else:
                label = ' '.join(items)
                href = top_category+'_'+('_'.join(items))
            href = href + '.html'

            if label == ' ':
                label = top_category
            result = (result + link_start + href + '">'+
                      label+
                      link_end)

        return result

    data.sort()
    results = {}
    html = '<ul class="nav nav-list">'

    for entry in data:
        blocks = entry.replace('.md','').split('_')
        # create empty list
        if blocks[0] not in results:
            results[blocks[0]] = []
        results[blocks[0]].append(blocks[1:])



    #print(results)
    for entry in results:
        html = (html + '<ul class="col-12">'+
                '<label class="tree-toggler nav-header category">'+
                entry+
                '</label>'+
                '<ul class="nav nav-list tree">'+
                '<li class="col-12">'+
                __unpack_results(entry, results[entry])+
                '</li>'+
                '</ul>'+
                '</ul>')

    html = html + '</ul>'

    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()

def replace_text_in_file(file_path: str, old_text: str, new_text: str):
    """
    Replace a given text in a file
    """
    path = Path(file_path)

    # Read file content
    content = path.read_text(encoding="utf-8")

    # Replace text
    updated_content = content.replace(old_text, new_text)

    # Write updated content back
    path.write_text(updated_content, encoding="utf-8")



def remove_tags_and_content(html: str, tags_to_remove: list[str], strip_remaining_tags:bool = False) -> str:
    """
    Remove specified HTML tags and everything inside them.

    Args:
        html: Input HTML string
        tags_to_remove: List of tag names to remove completely

    Returns:
        Cleaned HTML string
    """
    soup = BeautifulSoup(html, "html.parser")

    for tag_name in tags_to_remove:
        for tag in soup.find_all(tag_name):
            tag.decompose()  # removes tag + all nested content

    if strip_remaining_tags:
        return str(soup.get_text())
    else:
        return str(soup)

if __name__ == "__main__":
    #clear old data
    if os.path.exists("htdocs"):
        clear_folder("htdocs")
    else:
        os.makedirs("htdocs")

    # read html template files
    html_file = read_file("resources/template.html")

    # read markdown files
    markdown_files = read_all_files("data","*.md")
    # remove index from sidebar
    no_index_markdown_files = {k: v for k, v in markdown_files.items() if k != 'index.md'}
    sidebar_html = make_sidebar_html(list(no_index_markdown_files.keys()))
    #print(sidebar_html)

    search_data = []

    # convert each file to html
    for markdown_file_name, markdown_file_content in markdown_files.items():
        html_sniplet = markdown_to_html(markdown_file_content)

        # build html file using the template and replace placeholder with html
        final_html_file_content = html_file.replace('{body}', html_sniplet)
        final_html_file_content = final_html_file_content.replace('{sidebar}', sidebar_html)
        final_html_file_name = replace_extension(markdown_file_name, '.html')

        write_to_file('htdocs/'+final_html_file_name, final_html_file_content)

        # write search array for vue search
        search_data.append({
            'file':final_html_file_name,
            'data': remove_tags_and_content(html_sniplet,['pre','code'],True)
        })



    # copy template files
    copy_folder("resources/css", "htdocs/css")
    copy_folder("resources/js", "htdocs/js")

    # write search data into vuesearch.js
    replace_text_in_file("htdocs/js/vuesearch.js",old_text='const search_data = []',
                         new_text="const search_data = "+str(search_data)+';')


    # write index file (no longer needed, we have an index.md)
    #index_content =  html_file.replace('{sidebar}',sidebar_html)
    #index_content = index_content.replace('{body}','')
    #write_to_file('htdocs/index.html', index_content)

