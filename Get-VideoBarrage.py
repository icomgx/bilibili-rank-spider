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
    """
    根据视频的av号获取cid
    :param av: B站视频的AV号  如：https://www.bilibili.com/video/av83743079
    :return: 视频的cid号
    """
    av = av.strip('av')
    url = f'https://api.bilibili.com/x/player/pagelist?aid={av}&jsonp=jsonp'
    res = download_page(url)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid


# 根据cid请求弹幕
def get_dan_mu(cid):
    """
    根据cid请求弹幕
    :param cid: 视频的cid号
    :return: 弹幕列表
    """
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = download_page(url)
    res_xml = res.content.decode('utf-8')
    pattern = re.compile('<d.*?>(.*?)</d>')
    dan_mu_list = pattern.findall(res_xml)
    return dan_mu_list


# 把弹幕写入到文件中
def save_to_file(dan_mu_list, filename):
    """
    把弹幕写入到文件中
    :param dan_mu_list: 弹幕列表
    :param filename: 保存的文件名
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        for one_dan_mu in dan_mu_list:
            f.write(one_dan_mu)
            f.write('\n')

