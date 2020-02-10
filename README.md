# bilibili-rank-spider
bilibili排行榜数据可视化项目-初学者项目  
采用PyCharm IDE编写，初学py项目。  
定时获取b站排行榜信息写入数据库用于日后数据可视化，持续更新...  
库调用：
 - [requests](https://github.com/psf/requests "Github")
 - sqlite3
 - [schedule](https://github.com/dbader/schedule "Github")
 - time
 - BeautifulSoup4
 - [jieba](https://github.com/LiveMirror/jieba "Github")
 - wordcloud

#### 开发人员:  
 - ShengFAN_ [bilibili](https://space.bilibili.com/496636524 "前往他的bilibili")

 - 喵空的森林 [bilibili](https://space.bilibili.com/34476349 "前往他的bilibili")

 - 啊泰_ [bilibili](https://space.bilibili.com/23106193 "前往他的bilibili")

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
