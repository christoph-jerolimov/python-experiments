from flask import Flask
from flask.cli import main
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world() -> str:
    return "<h1>Hello, World!</h1>"


class User(Resource):
    def get(self) -> str:
        return "hello world"


api.add_resource(User, "/users")

if __name__ == "__main__":
    main()
