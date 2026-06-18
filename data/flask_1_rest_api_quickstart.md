## Flask REST API Quickstart

Use this as a blueprint to get started:

```Python
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
```

Create the app:

```Python
app = Flask(__name__)
# cors allow all domains (for testing)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
```

Add the request handling methods (CRUD operations):

```Python
@app.route('/member', methods=['POST'])
def create():
    # Create new resource
    record = {}
    if request.method == 'POST':
        print("post request received, data =", request.data)
        record = json.loads(request.data)
        # TODO: execute create
        return jsonify(record), 201


@app.route('/member/<id>', methods=['GET'])
def read(id):
    # Get resource
    record = {'id': id}
    if request.method == 'GET':
        print("get request received")
        # TODO: get data
        return record, 200


@app.route('/member/<id>', methods=['PUT'])
def update(id):
    # Update existing resource
    record = {'id': id}
    if request.method == 'PUT':
        print("update request received, data =", request.data)
        record = json.loads(request.data)
        # TODO: execute update
        return jsonify(record), 200


@app.route('/member/<id>', methods=['DELETE'])
def delete(id):
    # Delete resource
    record = {'id': id}
    if request.method == 'DELETE':
        print("delete request received")
        # TODO: execute remove
        return jsonify(record), 200
```

Start the Flask app:

```Python
app.run(debug=True)
```

**References:** [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)