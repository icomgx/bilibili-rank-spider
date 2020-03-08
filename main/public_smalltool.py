import os
import requests

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        return '文件夹路径已创建'
    else:
        return '文件夹路径已存在'

def checkFileExist(filename):
	return os.access(filename, os.F_OK) # 文件存在，返回True,否则返回False

# 获取网页
def download_website_page(weburl):
    # 添加请求头
    # User-Agent：浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36 '
    }
    # res = requests.get(url=weburl, headers=headers, timeout=2.5)
    res = requests.get(url=weburl)

    if res.status_code != 200:
        print(f'http访问出错,status_code{res.status_code}')
        return -1, 0
    else:
        return 0, res

# 将不存在的视频AV号保存至文件
def bugavid_file_write(bug_av_id, filename):
    av_bug = []
    with open('accounts.txt', 'r') as f:
        for line in f:
            av_bug.append(line.strip('\n'))
    if bug_av_id in av_bug:
        print(f'{bug_av_id} 已在列表中')
    else:
        with open(filename, mode='w+', encoding='utf-8') as f:
            f.write(bug_av_id)
            f.write('\n')
            f.close()
            print(f'{bug_av_id} 已加入列表')
