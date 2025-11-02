from flask import Flask, render_template
from os import scandir

app = Flask(__name__)

md_files = scandir("D:/PKM/0_inbox")
feed_list = []

for i in md_files:
    feed_list.append(i)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/feed")
def feed():
    return render_template("feed.html", files=feed_list)