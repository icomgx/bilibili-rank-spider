# bilibili-rank-spider
bilibili排行榜数据可视化项目-初学者项目  
采用PyCharm IDE编写，初学py项目。  
定时获取b站排行榜信息写入数据库用于日后数据可视化，持续更新...  
## 库调用：
 - [requests](https://github.com/psf/requests "Github")
 - sqlite3
 - [schedule](https://github.com/dbader/schedule "Github")
 - time
 - os
 - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/ "BeautifulSoup4")
 - [jieba](https://github.com/LiveMirror/jieba "Github")
 - [wordcloud](https://github.com/amueller/word_cloud "wordcloud")
 - [Flask](https://github.com/pallets/flask "Flask")
 - [Flask-Babel](https://github.com/python-babel/flask-babel "Flask-Babel")
 - json



## WebUI引用：
 - [mdui](https://www.mdui.org/docs "docs")
 - [jQuery](https://www.jquery.com/ "docs")
 - [socket.io](https://socket.io/ "docs")

#### 开发人员:  
 - 喵空的森林 [bilibili](https://space.bilibili.com/34476349 "前往他的bilibili")

 - 啊泰_ [bilibili](https://space.bilibili.com/23106193 "前往他的bilibili")

 - ShengFAN_ [bilibili](https://space.bilibili.com/496636524 "前往他的bilibili")

### 2020-03-11：
 - 解决了未创建日志文件前检查路径是否存在的问题
 - 另，解释一下弹幕不存在的视频跳过策略依据抓取时是否开放弹幕而定，并非是否存在历史弹幕，如3.11日74名《【独家视频】习近平考察火神山医院》，存在156条弹幕，但Up并未开放弹幕权限，故无法获取这些弹幕【废话两句】

### 2020-03-09：
 - 增加了通过cmd运行爬虫程序并保存日志至文件的脚本(该脚本本身亦可通过cmd运行)【~~禁止套娃套娃~~】

### 2020-03-08：
 - 完善了不存在弹幕的视频抓取策略
 - 加上了MySQL接口，待deBug

### 2020-02-11 #2：
 - 删除了cid冗余代码，加快程序运行速度
 - 完善了将不存在视频av号保存至av_id_404_list.txt功能，文件写模式为w+，并加上了注释

### 2020-02-11 #1：
 - 补充异常处理，主要包括文件夹路径不存在\网络异常\视频不存在\无权限对图片文件重写
 - 新增路径\文件存在性检查公共函数，当路径不存在时自动创建，反之则不处理
 - 新增数据库及数据表重配置功能，并按日期格式化数据库名
 - 将公共功能函数进行抽取，放在public_smalltool文件中
 - 重新配置了数据库\弹幕\词云\日志文件存储路径，并按日期新建子文件夹以存储弹幕\词云\日志文件。
 - 继续优化变量名\函数名\排版格式，通过使用对象，对部分函数的参数列表进行了归并


### 2020-02-10 #2:
 - WebUI的site.js完善


### 2020-02-10 #1:
 - 把上面三个链接替换为超链接形式


### 2020-02-09 #2:
 - 添加WebUI模块
 - 添加startup_tools.py，一键开启程序


### 2020-02-09 #1:  
 - 数据库换用Sqlite  
 - 获取弹幕和词云模块完成  

 - 变量名/函数名层面进行了部分优化，增强了代码可读性
 - 将数据库连接及关闭移出循环加快运行速度
 - 优化了sqlite3数据库连接所使用的路径语句，之前的版本在我这里无法运行
 - 调整了弹幕及词云保存路径，并对应调整了代码
 - 新增了少量用于调试的日志打印语句


### 2020-02-08:  
 - 数据库初步构建完成   
 - 基础代码完成可以定时运行  
