# 中文分词库
import jieba
# 生成词云图的库
from wordcloud import WordCloud

# 分词
def word_separate(barrage_str):
    p_list = jieba.lcut(barrage_str)
    return p_list

# 生成词云图
def genWordCloud(p_list, word_cloud_filename):
    w_str = ' '.join(p_list)
    w_settings = {
        'font_path': 'msyh.ttc',  # 词云使用字体
        'width': 800,  # 生成图片宽度
        'height': 580,  # 生成图片高度
        'background_color': 'white',  # 词云背景颜色
        'max_words': 80
    }
    # 实例化云词对象
    wc = WordCloud(**w_settings).generate(w_str)
    # 保存到文件
    wc.to_file(word_cloud_filename)


# 打开弹幕文件
def read_barrage_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        barrages = f.read()
        return barrages


# 开始主流程
def bwc_main(barrage_filename, word_cloud_filename):
    genWordCloud(word_separate(read_barrage_file(barrage_filename)), word_cloud_filename)
