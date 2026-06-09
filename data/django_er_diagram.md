### Django ER Diagram

Entity-Relationship Diagrams (ERDs) generated directly from the models

***Generate PNG / SVG ERD Using django-extensions***

[Source link](https://dev.to/ajitkumar/zero-effort-er-diagrams-in-django-auto-generate-directly-from-your-models-1ji3)

```
pip install django-extensions
pip install graphviz
pip install pygraphviz==2.0rc
```
Note: You may need to install this too https://graphviz.org/download/ and `Visual Studio Build Tools`

**Set up fontconfig environment variables**

Windows 11
`$env:FONTCONFIG_PATH = "C:\<project-path>\fontconfig\"`


**Enable the extensions**

```
# settings.py
INSTALLED_APPS = [
    ...
    "django_extensions",
]
```

Generate diagram for all apps

```
python manage.py graph_models -a -o project_erd.png
```

Generate diagram for one app

```
python manage.py graph_models app_name -o app_name_erd.png
```