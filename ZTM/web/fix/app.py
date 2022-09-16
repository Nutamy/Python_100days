from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return url_for('templates', filename='index.html')
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"