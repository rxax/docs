## Flask request handling

```python
import json
import os

from flask import Flask, Response, request, render_template, jsonify, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
```

Handle path arguments:

```python
@app.route('/api/<int:id>/<string:name>')
def answer_path(id: int, name: str):
    return Response(response='id=' + str(id) + ', name=' + str(name), status=200)

# http://127.0.0.1:5000/api/5/testname
```

Handle query parameters:

```python
@app.route('/api')
def answer_query():
    name = request.args.get("name")
    id = request.args.get("id")
    return Response(response='id=' + str(id) + ', name=' + str(name), status=200)

# http://127.0.0.1:5000/api?name=testname&id=5
```


### Handle forms

**Step 1)** Send Html form:

```python
@app.route('/api/form', methods=['GET'])
def show_form():
    return render_template("form.html")

# http://127.0.0.1:5000/api/form
```

Html form template (form.html file):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form test</title>
    <style type="text/css">
        div * {
            padding: 5px;

        }
        div label {
            display: inline-block;
            width: 100px;
        }
    </style>
</head>
<body>
<form method="post" action="/api/form" enctype="application/x-www-form-urlencoded">
    <div><label>Name</label><input type="text" name="name"></div>
    <div><label>Id</label><input type="number" name="id"></div>
    <div>
        <button>Send</button>
    </div>
</form>
<div>{{form_answer}}</div>
</body>
</html>
```

**Step 2)** Respond to html form POST request:

```python
@app.route('/api/form', methods=['POST'])
def answer_form():
    id = request.form.get('id')
    name = request.form.get('name')
    return render_template("form.html", form_answer='id=' + str(id) + ', name=' + str(name))

# http://127.0.0.1:5000/api/form
```

### JSON

Handle JSON GET requests:

```python
# Handle json GET
@app.route('/api/data', methods=['GET'])
def answer_get_json():
    # load data to dict
    data = {'id': 5, 'name': 'test name'}
    # return json str
    return jsonify(data)

# http://127.0.0.1:5000/api/data
```

Handle JSON POST requests:

```python
# Handle json POST
@app.route('/api/data', methods=['POST'])
def answer_post_json():
    # load data to dict
    data = json.loads(request.data)
    # return json str
    return jsonify(data)

# http://127.0.0.1:5000/api/data
```

### Uploads

Handle file upload:

```python
app.config['UPLOAD_FOLDER'] = 'upload_dir'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@app.route('/api/upload', methods=['POST'])
def answer_upload():
    if 'file' in request.files:
        file = request.files['file']
        if file and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return Response(response='file uploaded')
    return abort(400, 'Invalid file upload')

#http://127.0.0.1:5000/api/upload
```

