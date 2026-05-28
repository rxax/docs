## Flask View classes

Initial setup

```Python
rom flask import Flask, render_template
from flask.views import View

app = Flask(__name__)

""" In-memory user list """
users = [{'name': 'Alan'}, {'name': 'Parker'}, {'name': 'Peter'}]
```

View function example

```Python
@app.route("/users/")
def user_list():
    """ View function """
    return render_template("users.html", users=users)
```

View class example

```Python
class ListView(View):
    """ View class """
    init_every_request = False

    def __init__(self, model, template):
        """ This is not mandatory ... the args must be passed in the as_view call bellow """
        self.model = model
        self.template = template

    def dispatch_request(self):
        #items = self.model.query.all() # if model from db
        items = self.model
        return render_template(self.template, users=items)


app.add_url_rule(
    "/user-list",
    view_func=ListView.as_view("my-view", users, 'users.html'),
    methods=["GET", "POST"],
)
```

Start flask app

```Python
""" Start app """
if __name__ == "__main__":
    app.run(debug=True)
```


**Resources:**

- [Flask view classes](https://flask.palletsprojects.com/en/2.2.x/views/)

- [Docs](https://tedboy.github.io/flask/interface_api.class_based_views.html)