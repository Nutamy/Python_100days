from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)
year = dt.datetime.now().year
url_blog = "https://api.npoint.io/0a50e5219852c16cb6cb"
response_blog = requests.get(url_blog)
all_posts = response_blog.json()

@app.route("/")
def hello_world():
    return render_template("index.html", year=year)


@app.route("/guess/<cur_name>")
def guess(cur_name):
    name = str(cur_name)
    params = {"name": name}
    url_gender = "https://api.genderize.io/"
    url_age = "https://api.agify.io/"
    response_gender = requests.get(url_gender, params=params)
    response_age = requests.get(url_age, params=params)
    age = response_age.json()['age']
    gender = response_gender.json()['gender']
    return render_template("name.html", year=year, gender=gender, age=age, name=name)

@app.route("/blog")
def get_blog():
    return render_template("blog.html", year=year, posts=all_posts)

@app.route("/post/<int:idx>")
def get_post(idx):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == idx:
            requested_post = blog_post
            break
    return render_template("post.html", year=year, post=requested_post)

