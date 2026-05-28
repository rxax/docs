## Flask quickstart template

Copy-paste this code to get started.

```python
from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.url_map.strict_slashes = False
# cors allow all domains (for testing)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Connect to DB and create session
engine = create_engine('sqlite:///base.db', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/', methods=['GET'])
def start():
    # TODO: your code here
    return jsonify({'status': 'ok'}), 200


@app.route('/echo/<string:data>')
def echo(data):
    # TODO: your code here
    return jsonify({'echo': data}), 200


if __name__ == "__main__":
    app.run(debug=True)
```