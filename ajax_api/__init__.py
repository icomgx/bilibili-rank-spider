# coding: utf-8

from flask import *
from main import get_bilibili_rank
import json

app = Flask("bilibili_rank_spider_ui")


def getfile_str(filename):
    f = open(filename, encoding="utf-8")
    c = f.read()
    f.close()
    return c


@app.route("/")
def root_uri():
    return redirect("/index")


@app.route("/index")
def index_page():
    return render_template(
        "index.html",
        translate_text=getfile_str("./"),
        **json.loads(getfile_str("./language"))
    )


def main():
    app.run("0.0.0.0", )