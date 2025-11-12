from flask import Flask, render_template
from os import scandir
import markdown
import random

app = Flask(__name__)

md_files = list(scandir("D:/PKM/0_inbox"))
random.shuffle(md_files)
feed_list = []

for i in md_files:
    with open(i.path, encoding="utf-8") as f:
        read_data = f.read()
        html_content = markdown.markdown(read_data, extensions=['fenced_code','codehilite', 'tables'])
        feed_list.append({
            "name": i.name, 
            "path": i.path, 
            "content": read_data,
            "html_content": html_content})

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/feed")
def feed():
    return render_template("feed.html", files=feed_list)