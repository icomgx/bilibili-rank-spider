import requests
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup

# 要请求的地址
url = 'https://www.bilibili.com/ranking'
# 获取请求内容
response = requests.get(url)
# 解析内容
soup = BeautifulSoup(response.text, 'html.parser')
# 列表解析到数组
items = soup.find_all('li', {'class': 'rank-item'})


def job():
    # 打印标题
    print(soup.title.text)
    # 遍历取出数据
    for item in items:
        title = item.find('a', {'class': 'title'}).text
        score = item.find('div', {'class': 'pts'}).find('div').text
        rank = item.find('div', {'class': 'num'}).text
        visit = item.find('span', {'class': 'data-box'}).text
        up = item.find_all('a')[2].text
        up_id = item.find_all('a')[2].get('href')[len('//space.bilibili.com/'):]
        url = item.find('a', {'class': 'title'}).get('href')
        av_id = url[len('https://www.bilibili.com/video/'):]
        # 添加到数据库
        add_database(rank, title, score, visit, up, up_id, av_id, url)
        # 打印信息
        print(f'{rank} {title} {av_id} {up} {up_id} \r\n Insert database ok ')
    print(f'执行完毕共{len(items)}条数据...定时继续启动...')


def add_database(rank, title, score, visit, up, up_id, av_id, url):
    con = sqlite3.connect('database/bilibili_rank.db3')
    cursor = con.cursor()
    sql = f'INSERT INTO rank_list(rank,title,score,visit,up,up_id,av_id,url,get_time)' \
          f'VALUES(\'{rank}\',\'{title}\',\'{score}\',\'{visit}\',\'{up}\',\'{up_id}\',\'{av_id}\',\'{url}\',' \
          f'datetime(\'now\')) '
    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务
    con.commit()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    con.close()


# 入口
if __name__ == '__main__':
    # 每天到指定的时间执行拉取
    timer = input('请输入每天定时获取的时间如\"20:00\":')
    schedule.every().day.at(timer).do(job)
    print('定时服务启动...')
    while True:
        schedule.run_pending()  # 运行所有可运行的任务
        time.sleep(1)
