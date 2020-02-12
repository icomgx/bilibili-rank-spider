import sqlite3
import schedule
import time
import os
from bs4 import BeautifulSoup
from main import get_video_barrage as gv
from main import gen_bwc as gb
from main import public_smalltool as mytool


################################
# 定义全局变量

# 将排行榜中每个条目定义为website_ele对象
class website_ele:
    def __init__(self, rank, title, score, visit_time_count, up_name, up_id, av_id, v_url):
        self.title = title
        self.score = score
        self.rank = rank
        self.visit_time_count = visit_time_count
        self.up_name = up_name
        self.up_id = up_id
        self.v_url = v_url
        self.av_id = av_id


bilibili_ranking_all_url = 'https://www.bilibili.com/ranking'  # 排行榜url

time_in_filename_str = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前日期用作数据库名/弹幕子文件夹路径/词云子文件路径

ranking_all_avid_list = []  # 存储需要处理的视频av号码

project_folder = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径

db_general_folder = f'{project_folder}\\database\\'  # 数据库存储路径
barrage_general_folder = f'{project_folder}\\barrage\\{time_in_filename_str}\\'  # 弹幕文件存储路径
wordcloud_pic_general_folder = f'{project_folder}\\wordCloudImg\\{time_in_filename_str}\\'  # 词云存储路径
daily_log_general_folder = f'{project_folder}\\log\\{time_in_filename_str}\\'  # 每日日志存储路径，打算用于保存命令行中输出的文字
general_log_general_folder = f'{project_folder}\\log\\'  # 总日志存储路径，不存在的视频av号列表文件即保存在这个路径下


################################

################################
# 系统操作函数

# 路径检查，若不存在该文件夹则创建
def ProjectFileDirCheck():
    print(f'数据库{mytool.mkdir(db_general_folder)}')
    print(f'弹幕文件{mytool.mkdir(barrage_general_folder)}')
    print(f'词云图片{mytool.mkdir(wordcloud_pic_general_folder)}')
    print(f'爬虫总日志{mytool.mkdir(general_log_general_folder)}')
    print(f'爬虫每日日志{mytool.mkdir(daily_log_general_folder)}')


################################

################################
# 数据库操作

# 初始化sqlite数据库
def sqlitedb_init():
    database_name = 'bilibili_rank_' + time_in_filename_str + '.db3'

    sqlitedbpath = db_general_folder + database_name

    conn = sqlite3.connect(sqlitedbpath)
    cursor = conn.cursor()
    print(f'sqlite数据库已配置')

    # 初始化RANK_LIST数据表
    drop_sql = "DROP TABLE IF EXISTS RANK_LIST;"
    cursor.execute(drop_sql)
    conn.commit()
    create_table_sql = """
            CREATE TABLE "rank_list" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "rank" TEXT,
    "title" TEXT,
    "score" TEXT,
    "visit_time_count" TEXT,
    "up_name" TEXT,
    "up_id" TEXT,
    "av_id" TEXT,
    "v_url" TEXT,
    "get_time" TEXT
    );"""
    cursor.execute(create_table_sql)
    conn.commit()
    print("RANK_LIST数据表初始化完成")

    # 初始化barrage_list数据表
    drop_sql = "DROP TABLE IF EXISTS barrage_list;"
    cursor.execute(drop_sql)
    conn.commit()
    create_table_sql = """
        CREATE TABLE "barrage_list" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "barrage_av" TEXT,
    "barrage_text" TEXT,
    "get_time" TEXT
    );
    """
    cursor.execute(create_table_sql)
    conn.commit()
    print("Barrage_List数据表初始化完成")

    cursor.close()
    conn.close()

    return sqlitedbpath


# 将TOP100排行榜信息添加到数据库
def add_rank_info_into_db(conn, cursor, data_element):
    current_time = time.time()
    sql = f'INSERT INTO rank_list(rank,title,score,visit_time_count,up_name,up_id,av_id,v_url,get_time) ' \
          f'VALUES(\'{data_element.rank}\',\'{data_element.title}\',\'{data_element.score}\'' \
          f',\'{data_element.visit_time_count}\',\'{data_element.up_name}\',\'{data_element.up_id}\'' \
          f',\'{data_element.av_id}\',\'{data_element.v_url}\'' \
          f',datetime(\'now\',\'localtime\')) '  # 输出本机时间使用datetime('now','localtime')

    # 执行SQL语句
    cursor.execute(sql)
    # 提交事务
    conn.commit()


# 弹幕信息添加到数据库
# av_id 弹幕所属av号码 barrage_list弹幕列表
def add_video_barrage_into_db(conn, cursor, av_id, barrage_list):
    for barrage in barrage_list:
        sql = f'INSERT INTO barrage_list(barrage_av,barrage,get_time) ' \
              f'VALUES(\'{av_id}\',\'{barrage}\', datetime(\'now\',\'localtime\'))'
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        conn.commit()
        # # print(f'av:{av_id}添加弹幕: {barrage} \r\n ok!')


################################

################################
# 网页操作及下载

# 下载网页，解析为item列表
def website_item_download(bilibili_ranking_all_url):
    # # 请求头
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                     'Chrome/79.0.3945.88 Safari/537.36 '
    # }
    # # 获取请求内容
    # response = requests.get(url=bilibili_ranking_all_url, headers=headers)
    status, response = mytool.download_website_page(bilibili_ranking_all_url)
    if status == 0:
        # 解析内容
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'开始爬取{soup.title.text}')
        # 列表解析到数组
        website_item = soup.find_all('li', {'class': 'rank-item'})
        return 0, website_item
    else:
        return -1, 0


# item列表解析，构造并返回每个item信息对象
def ranking_item_analysis(item):
    title = item.find('a', {'class': 'title'}).text
    score = item.find('div', {'class': 'pts'}).find('div').text
    rank = item.find('div', {'class': 'num'}).text
    visit_time_count = item.find('span', {'class': 'data-box'}).text
    up_name = item.find_all('a')[2].text
    up_id = item.find_all('a')[2].get('href')[len('//space.bilibili.com/'):]
    uri = item.find('a', {'class': 'title'}).get('href')
    av_id = uri[len('https://www.bilibili.com/video/'):]
    ranking_element = website_ele(rank, title, score, visit_time_count, up_name, up_id, av_id, uri)

    return ranking_element


def main(rank_url):
    status, website_item = website_item_download(rank_url)
    if status == -1:  # 网络状态异常
        print("网络访问异常，请检查网络状态\n即将退出程序")
        return -1
    else:  # 网络正常
        # 配置工程需要保存文件所在的文件夹
        ProjectFileDirCheck()
        sqlite_folder = sqlitedb_init()

        # 建立sqlite的连接，获取游标cursor
        bilibili_ranking_all_db_conn = sqlite3.connect(sqlite_folder)
        bilibili_ranking_all_db_cursor = bilibili_ranking_all_db_conn.cursor()

        # 爬取排行榜信息
        crawl_start = time.time()

        item_index = 1
        # 遍历排行榜中的数据
        for item in website_item:
            ranking_element = ranking_item_analysis(item)

            # 将排行榜信息添加到数据库
            add_rank_info_into_db(bilibili_ranking_all_db_conn, bilibili_ranking_all_db_cursor, ranking_element)

            print(f'排行榜第{item_index}名信息已归档！')
            item_index += 1

            # 更新ranking_all_avid_list列表
            ranking_all_avid_list.append(ranking_element.av_id)

            # 打印排行榜中每条视频相关信息
            # print(f'{ranking_element.rank} {ranking_element.title} {ranking_element.av_id} {ranking_element.up_name} {ranking_element.up_id} \r\n Insert database ok ')

        print(f'已完成排行榜中共{len(website_item)}条数据的爬取...\n继续进行对应视频弹幕的爬取...')

        # 如需将弹幕文件保存到数据库，则需将下面两条语句移至本函数尾部
        bilibili_ranking_all_db_cursor.close()
        bilibili_ranking_all_db_conn.close()

        crawl_end = time.time()
        print(f'排行榜爬取共耗时: {crawl_end - crawl_start} s')

        # 爬取视频弹幕
        barrage_start = time.time()

        barrage_item_index = 1;
        for avid in ranking_all_avid_list:

            # 根据完整的av号获取弹幕文件，视频状态正常时可解析到cid，否则将av号写入txt
            status, av_cid = gv.get_cid(avid, daily_log_general_folder)
            if status < 0:  # 视频异常处理，
                print(f'编号为{avid}的视频不存在')
            else:
                barrage_file_full_name = barrage_general_folder + f'barrage_{avid}_{time_in_filename_str}.txt'
                status = gv.vb_main(av_cid, barrage_file_full_name, general_log_general_folder)  # 保存弹幕文件

                # 由于弹幕文件较大，存在数据库IO不足的问题，故暂时不使用数据库存储
                # add_video_barrage_into_db(bilibili_ranking_all_db_conn,cursor,avid, barrage_list)

                print(f'排行榜第{barrage_item_index}名的视频弹幕已下载')

                # 弹幕文件词云生成
                word_cloud_image_full_name = wordcloud_pic_general_folder + f'wordcloud_{avid}_{time_in_filename_str}.png'
                # 读取弹幕文件生成词云
                gb.bwc_main(barrage_file_full_name, word_cloud_image_full_name)
                print(f'排行榜第{barrage_item_index}名的视频弹幕词云已生成')

                barrage_item_index += 1

        print(f'{len(ranking_all_avid_list)}个视频弹幕的爬取与词云的生成工作已完成...')

        barrage_end = time.time()
        print(f'弹幕下载及词云生成共耗时: {barrage_end - barrage_start} s')
        return 0


# 主函数
if __name__ == '__main__':
    print(f'当前时间为{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
    start = time.time()
    status = main(bilibili_ranking_all_url)
    if status == 0:  # 网络状态正常
        end = time.time()
        print(f'排行榜爬虫总耗时: {end - start}')
    print('即将退出爬虫')
    exit()

# 每天到指定的时间执行拉取
# timer = input('请输入每天定时获取的时间如\"20:00\":')
# schedule.every().day.at(timer).do(main)
# print('定时服务启动...')
# while True:
#     schedule.run_pending()  # 运行所有可运行的任务
#     time.sleep(1)