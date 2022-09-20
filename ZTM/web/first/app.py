from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def get_home():
    return render_template('index.html')

@app.route("/browse")
def get_browse():
    return render_template('browse.html')

@app.route("/details")
def get_details():
    return render_template('details.html')

@app.route("/profile")
def get_profile():
    return render_template('profile.html')

@app.route("/streams")
def get_streams():
    return render_template('streams.html')
