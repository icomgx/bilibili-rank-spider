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
    uri = f'https://api.bilibili.com/x/player/pagelist?aid={av}&jsonp=jsonp'
    res = download_page(uri)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid

    # 根据cid请求弹幕


def get_barrage(cid):
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = download_page(url)
    res_xml = res.content.decode('utf-8')
    pattern = re.compile('<d.*?>(.*?)</d>')
    barrage_list = pattern.findall(res_xml)
    return barrage_list


# 把弹幕写入到文件中
def save_to_file(barrage_list, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        for barrage in barrage_list:
            f.write(barrage)
            f.write('\n')


# 开始主流程
def start(av_id, filename):
    save_to_file(get_barrage(get_cid(av_id)), filename)
