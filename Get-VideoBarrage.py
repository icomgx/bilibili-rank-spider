import json
import re
import requests


# 获取页面
def download_page(url):
    # 添加请求头
    # User-Agent：浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36 '
    }
    res = requests.get(url=url, headers=headers)
    return res


# 根据视频的av号获取cid
def get_cid(av):
    av = av.strip('av')
    url = f'https://api.bilibili.com/x/player/pagelist?aid={av}&jsonp=jsonp'
    res = download_page(url)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid


# 根据cid请求弹幕
def get_dan_mu(cid):
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = download_page(url)
    res_xml = res.content.decode('utf-8')
    pattern = re.compile('<d.*?>(.*?)</d>')
    dan_mu_list = pattern.findall(res_xml)
    return dan_mu_list


