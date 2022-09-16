from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/browse")
def browse():
    return render_template('browse.html')

@app.route("/details")
def details():
    return render_template('details.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/streams")
def streams():
    return render_template('streams.html')
