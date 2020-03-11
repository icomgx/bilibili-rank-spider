import os
import time
import subprocess
import public_smalltool as mytool

# 本脚本用于自动运行排行榜爬虫并将日志保存至文件

print('Bilibili排行榜爬虫脚本已启动...\n记录日志中...')
time_in_filename_str = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前日期用作数据库名/弹幕子文件夹路径/词云子文件路径

def run_cmd2file(cmd,ordilog,errorlog):
    fdout = open(ordilog, 'a')
    fderr = open(errorlog, 'a')
    p = subprocess.Popen(cmd, stdout=fdout, stderr=fderr, shell=True, encoding='utf-8')
    if p.poll():
        return 1
    p.wait()
    return 0

file_folder = os.getcwd()  #表示当前所处的文件夹
project_folder = os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
daily_log_general_folder = f'{project_folder}\\log\\{time_in_filename_str}\\'                   # 每日日志存储路径，打算用于保存命令行中输出的文字
print(f'日志{mytool.mkdir(daily_log_general_folder)}')
command = f'python {file_folder}\\get_bilibili_rank.py' #可以直接在命令行中执行的命令

errorlog = f'{daily_log_general_folder}异常日志.log'
ordilog = f'{daily_log_general_folder}正常日志.log'

status = run_cmd2file(command, ordilog, errorlog)
if status == 0:
    print(f'爬虫已正常结束，如有需要请查看正常日志')
else:
    print(f'爬虫异常退出，请查看异常日志')
input('Press any key to exit:')