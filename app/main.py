from flask import Flask
from flask import render_template
import json
from Testpage import main

app = Flask(__name__)

@app.route("/")
def home():
    user = {'username': 'Moon Person'}
    return render_template('template.html', title='Doom', user=user)

@app.route("/asteroid")
def asteroid():
    user = {'username': 'Moon Person'}
    return render_template('asteroid.html', title='Doom', user=user)

@app.route("/experiment")
def experiment():
    user = {'username': 'Moon Person'}
    return render_template('experimentalasteroid.html', title='Doom', user=user)

@app.route('/testpage')
def testrun():
    return Testpage.main()


if __name__ == "__main__":
    app.run(debug=True)