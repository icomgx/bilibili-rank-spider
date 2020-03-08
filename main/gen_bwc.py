# 中文分词库
import jieba
# 生成词云图的库
from wordcloud import WordCloud
import public_smalltool as mytool
import logging

jieba.setLogLevel(logging.INFO) # 去除“Building prefix dict from the default dictionary ...”的提示

# 分词
def word_separate(barrage_str):
    w_list = jieba.lcut(barrage_str)
    return w_list

# 生成词云图并保存
def genWordCloud(w_list, word_cloud_filename):
    w_str = ' '.join(w_list)
    w_settings = {
        'font_path': 'msyh.ttc',  # 词云使用字体
        'width': 800,  # 生成图片宽度
        'height': 580,  # 生成图片高度
        'background_color': 'white',  # 词云背景颜色
        'max_words': 80
    }
    # 实例化云词对象
    wc_obj = WordCloud(**w_settings).generate(w_str)
    # 保存到文件
    wc_obj.to_file(word_cloud_filename)


# 打开弹幕文件
def read_barrage_file(barrage_filename):
    with open(barrage_filename, mode='r', encoding='utf-8') as f:
        barrages = f.read()
        return barrages

# 词云生成主函数
def bwc_main(barrage_filename, word_cloud_filename):
    barrages = read_barrage_file(barrage_filename)
    word_list = word_separate(barrages)
    if mytool.checkFileExist(word_cloud_filename):
        return 1
    else:
        genWordCloud(word_list, word_cloud_filename)
        return 0