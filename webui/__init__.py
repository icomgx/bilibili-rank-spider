#coding: utf-8

from flask import *

app = Flask("bilibili_rank_spider_ui")

@app.route("/")
def index():
    return redirect(
        "/"
    )