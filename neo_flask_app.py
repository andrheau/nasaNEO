from flask import Flask
from flask import render_template
import neo_fun



app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

if __name__ == "__main__":
    app.run(debug = True)