#test app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

#creates a route or new pages with a slash
@app.route("/myfriendkmc")
def don():
        return "myfriendkmc"
if __name__ == "__main__":
    app.run(debug=True)
