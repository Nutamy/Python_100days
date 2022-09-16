from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('templates/index.html')

@app.route("/browse")
def browse():
    return render_template('templates/browse.html')

@app.route("/details")
def details():
    return render_template('templates/details.html')

@app.route("/profile")
def profile():
    return render_template('templates/profile.html')

@app.route("/streams")
def streams():
    return render_template('./templates/streams.html')
