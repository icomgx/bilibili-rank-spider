import requests
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup
from main import get_video_barrage as gv
from main import gen_bwc as gb
import os

# 要请求的地址
url = 'https://www.bilibili.com/ranking'
# 获取请求内容
response = requests.get(url)
# 解析内容
soup = BeautifulSoup(response.text, 'html.parser')
# 列表解析到数组
items = soup.find_all('li', {'class': 'rank-item'})

av_items_list = []  # 存储需要处理的视频av号码


# 获取当前python文件及上一级的路径，以构造稳定的sqlite文件存储路径
current_abstract_folder = os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
project_folder = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
sqlite_folder = project_folder+"\\database\\bilibili_rank.db3"


# 主工作流程
def main_func():
    # 打印标题
    print(soup.title.text)

    # 建立sqlite的连接，获取游标cursor
    db_connection = sqlite3.connect(sqlite_folder)
    cursor = db_connection.cursor()
    ranksort_start = time.time()

    item_index = 1
    # 遍历排行榜中的数据
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
        # add_rank_info_into_db(db_connection,cursor,rank, title, score, visit, up, up_id, av_id, uri)
        add_rank_info_into_db(db_connection,cursor,rank, title, score, visit, up, up_id, av_id, uri)

        print(f'the item_index index is {item_index}')
        item_index += 1

        # 添加对应弹幕信息到数据库
        av_items_list.append(av_id)
        # 打印信息
        # print(f'{rank} {title} {av_id} {up} {up_id} \r\n Insert database ok ')
    print(f'完成排行榜中共{len(items)}条数据的爬取...继续进行对应视频弹幕的爬取...')

    ranksort_end = time.time()
    print("rank sort Execution Time: ", ranksort_end - ranksort_start)

    barrage_start = time.time()

    barrage_item_index = 1;
    for avid in av_items_list:

        one_start=time.time()

        # 弹幕文件处理
        barrage_list = gv.get_barrage(gv.get_cid(avid))  # 获取对应视频av的弹幕列表
        gen_time = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当日期为生成日期
        # barrage_folder = project_folder+"\\barrage\\"
        barrage_file_full_name = project_folder+"\\barrage\\"+f'{avid}_{gen_time}.txt'
        # barrage_filename = f(barrage_folder+'{avid}_{gen_time}.txt'  # 定义弹幕文件路径和名称
        # barrage_filename = f'word_cloud_img/txt/{avid}_{gen_time}.txt'  # 定义弹幕文件路径和名称
        gv.vb_main(avid, barrage_file_full_name)  # 启动生成弹幕文件
        # add_video_barrage_into_db(db_connection,cursor,avid, barrage_list)

        print(f'the barrage index is {barrage_item_index}')
        barrage_item_index += 1

        # 弹幕文件词云生成
        word_cloud_image_full_name = project_folder+"\\word_cloud_img\\"+f'{avid}_{gen_time}.png'
        # word_cloud_image_filename = f'word_cloud_img/{avid}_{gen_time}.png'  # 定义词云图片的路径和名称
        gb.bwc_main(barrage_file_full_name, word_cloud_image_full_name)  # 启动读取弹幕文件生成词云

        one_end=time.time()
        print("Execution Time: ", one_end - one_start)

    print(f'完成共计{len(av_items_list)}个视频弹幕的爬取与词云的生成...')

    barrage_end = time.time()
    print("barrage Execution Time: ", barrage_end - barrage_start)


# 将TOP100排行榜信息添加到数据库
# def add_rank_info_into_db(db_connection,cursor,rank, title, score, visit, up, up_id, av_id, uri):
def add_rank_info_into_db(db_connection,cursor,rank, title, score, visit, up, up_id, av_id, uri):
    sql = f'INSERT INTO rank_list(rank,title,score,visit,up,up_id,av_id,url,get_time)' \
          f'VALUES(\'{rank}\',\'{title}\',\'{score}\',\'{visit}\',\'{up}\',\'{up_id}\',\'{av_id}\',\'{uri}\',' \
          f'datetime(\'now\')) '
    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务
    db_connection.commit()
    # # 关闭光标对象
    # cursor.close()
    # # 关闭数据库连接
    # con.close()


# 弹幕信息添加到数据库
# av_id 弹幕所属av号码 barrage_list弹幕列表
# def add_video_barrage_into_db(av_id, barrage_list):
def add_video_barrage_into_db(db_connection,cursor,av_id, barrage_list):

    for barrage in barrage_list:
        # con = sqlite3.connect(sqlite_folder)
        # cursor = con.cursor()
        sql = f'INSERT INTO barrage_list(barrage_av,barrage,get_time) ' \
              f'VALUES(\'{av_id}\',\'{barrage}\', datetime(\'now\'))'
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        db_connection.commit()
        # # 关闭光标对象
        # cursor.close()
        # # 关闭数据库连接
        # con.close()
        # # print(f'av:{av_id}添加弹幕: {barrage} \r\n ok!')


# 入口
if __name__ == '__main__':
    start = time.time()
    main_func()
    end = time.time()
    print("Execution Time: ", end - start)
    exit()

# 每天到指定的时间执行拉取
# timer = input('请输入每天定时获取的时间如\"20:00\":')
# schedule.every().day.at(timer).do(main_func)
# print('定时服务启动...')
# while True:
#     schedule.run_pending()  # 运行所有可运行的任务
#     time.sleep(1)
