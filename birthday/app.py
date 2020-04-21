#test app
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello Ronald"
    now = datetime.datetime.now()
    birthday = now.month == 8 and now.day == 18
    return render_template("index.html", birthday=birthday)
#creates a route or new pages with a slash
#you can use HTML5
# you can reference an html or css file as long as it is in the same path
@app.route("/Kyle")
def kyle():
        return "<h1>Kyle</h1>"
if __name__ == "__main__":
    app.run(debug=True)
