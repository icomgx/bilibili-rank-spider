#coding: utf-8

from flask import *

app = Flask("bilibili_rank_spider_ui")

@app.route("/")
def root_uri():
    return redirect("/index")

@app.route("/index")
def index_page():
    return render_template(
        "index.html"
    )