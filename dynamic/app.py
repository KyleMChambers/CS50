from flask import Flask
#LOL make sure you put a capital F.

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello world'

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
