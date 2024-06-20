from flask import Flask
from flask.cli import main

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    main()
