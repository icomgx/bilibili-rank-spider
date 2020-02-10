# coding: utf-8

import requests as req
import json

CHANNEL_MASTER = "master"
CHANNEL_DEV = "dev"


def check_update(
        channel=CHANNEL_MASTER
):
    response = req.get(
        "https://raw.githubusercontent.com/icomgx/bilibili-rank-spider/" + channel + "/ota/version"
    )
    f = open("./version", "r", encoding="utf-8")
    response.encoding = "utf-8"
    version_local = json.load(f)
    version_latest = response.json()
    if version_latest['ver'] > version_local['ver']:
        response = req.get(
            "https://raw.githubusercontent.com/icomgx/bilibili-rank-spider/" + channel + "/ota/changelog"
        )
        if response.status_code != 200:
            return {
                "need_update": True,
                "changelog": "暂时获取不到ChangeLog，如果要获取更新内容请提一个issue"
            }
        else:
            return {
                "need_update": True,
                "changelog": response.content.decode("utf-8")
            }
    else:
        return {
            "need_update": False,
            "changelog": None
        }
