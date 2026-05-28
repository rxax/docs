# Flask Blueprints

Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications.

**References:** [Flask Blueprints](https://flask.palletsprojects.com/en/2.0.x/blueprints/)

```python
from flask import Flask, Blueprint, render_template
```

Create Blueprint:

```python
# Create Blueprint
admin_page = Blueprint(
    'admin_page',
    __name__,
    template_folder='templates/admin'
)

# Use Blueprint
@admin_page.route("/list")
def list_admins():
    admins = ['user1', 'user2', 'user3']
    return render_template("list.html", users=admins)
```

Register Blueprint in app:

```python
app = Flask(__name__)

# register Blueprint to app
app.register_blueprint(admin_page, url_prefix='/admins')

app.run(debug=True)
```

File: templates/admin/list.html:

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
{% for e in users %}
    {{e}}
{% endfor %}
</body>
</html>
```

Testing url:

> http://127.0.0.1:5000/admins/list

Output:

> result: user1 user2 user3