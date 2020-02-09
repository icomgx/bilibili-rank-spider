import requests
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup
from main import get_video_barrage as gv
from main import gen_bwc as gb

# 要请求的地址
url = 'https://www.bilibili.com/ranking'
# 获取请求内容
response = requests.get(url)
# 解析内容
soup = BeautifulSoup(response.text, 'html.parser')
# 列表解析到数组
items = soup.find_all('li', {'class': 'rank-item'})

av_items = []  # 存储需要处理的视频av号码


# 主工作流程
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
        uri = item.find('a', {'class': 'title'}).get('href')
        av_id = uri[len('https://www.bilibili.com/video/'):]
        # 添加到数据库
        add_rank_info_database(rank, title, score, visit, up, up_id, av_id, uri)
        # 添加对应弹幕信息到数据库
        av_items.append(av_id)
        # 打印信息
        print(f'{rank} {title} {av_id} {up} {up_id} \r\n Insert database ok ')
    print(f'执行完毕共{len(items)}条数据...定时继续启动...')
    for avid in av_items:
        barrage_list = gv.get_barrage(gv.get_cid(avid))  # 获取对应视频av的弹幕列表
        gen_time = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当日期为生成日期
        barrage_filename = f'main/word_cloud_img/txt/{avid}_{gen_time}.txt'  # 定义弹幕文件路径和名称
        word_cloud_image_filename = f'main/word_cloud_img/{avid}_{gen_time}.png'  # 定义词云图片的路径和名称
        gv.start(avid, barrage_filename)  # 启动生成弹幕文件
        gb.start(barrage_filename, word_cloud_image_filename)  # 启动读取弹幕文件生成词语
        add_video_barrage(avid, barrage_list)  # 弹幕添加到数据库


# TOP100排行榜信息添加到数据库
def add_rank_info_database(rank, title, score, visit, up, up_id, av_id, uri):
    print('11')
    con = sqlite3.connect('database/bilibili_rank.db3')
    cursor = con.cursor()
    sql = f'INSERT INTO rank_list(rank,title,score,visit,up,up_id,av_id,url,get_time)' \
          f'VALUES(\'{rank}\',\'{title}\',\'{score}\',\'{visit}\',\'{up}\',\'{up_id}\',\'{av_id}\',\'{uri}\',' \
          f'datetime(\'now\')) '
    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务
    con.commit()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    con.close()


# 弹幕信息添加到数据库
# av_id 弹幕所属av号码 barrage_list弹幕列表
def add_video_barrage(av_id, barrage_list):
    print('22')
    for barrage in barrage_list:
        con = sqlite3.connect('database/bilibili_rank.db3')
        cursor = con.cursor()
        sql = f'INSERT INTO barrage_list(barrage_av,barrage,get_time) ' \
              f'VALUES(\'{av_id}\',\'{barrage}\', datetime(\'now\'))'
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        con.commit()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        con.close()
        print(f'av:{av_id}添加弹幕: {barrage} \r\n ok!')


# 入口
if __name__ == '__main__':
    start = time.time()
    job()
    end = time.time()
    print("Execution Time: ", end - start)

# 每天到指定的时间执行拉取
# timer = input('请输入每天定时获取的时间如\"20:00\":')
# schedule.every().day.at(timer).do(job)
# print('定时服务启动...')
# while True:
#     schedule.run_pending()  # 运行所有可运行的任务
#     time.sleep(1)
