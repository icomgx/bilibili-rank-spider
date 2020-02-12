# 项目的目标是让nodejs可以正常并无缝使用 python脚本
# 同时支持回到函数的传递
# 通过异步方式在本地服务器后端执行python脚本/ipynb格式的文件/以及python字符串
# 
## 1.机制
    充分利用node的异步加载的能力,通过child_pross中的spawn机制(异步的异步),基于promise封装执行并输出正常或错误的打印记录,实现实时检测python的处理结果
## 2.可以执行
1. python字符串,即符合标准的python脚本,调用 runpytext
2. 支持 .py文件 runpath
3. 支持 .ipynb (jupyter格式的文件) run_ipynb_code
```
注意:.ipynb根据官方说明,由于其存储的是一种json格式,也就是说暂时还无法直接执行程序,故在执行.ipynb程序的时候需要通过官方的jupyter nbconvert 方式对.ipynb进行格式的转换/目前是存于tmp临时文件中(支持window以及linux系统),再通过正常机制(runpath)处理python脚本
```

## 3.错误处理机制
    当python执行处理出错会抛出异常,可以通过回调函数捕捉异常

## 4.使用方法 安装项目包方法
```
    $ npm install --save jsexecpy 
```
## 使用方式

- 1. 字符串功能
    ``` nodejs
    > let jsexecpy = require("jsexecpy")
    > jsexecpy.runpytext("import os;import time;time.sleep(1);print('you are my love');time.sleep(5);a = 2;a+=1;print(a)")
    ```
- 2. 执行.py文件
    ```nodejs
    > let jsexecpy = require("jsexecpy")
    > jsexecpy.runpath("/home/.../test.py",callback)
    ```

- 3. 执行.ipynb文件
    ```nodejs
    > let jsexecpy = require("jsexecpy")
    > jsexecpy.run_ipynb_code("/home/.../test.ipynb",callback)

    ```

- 4. callback 写法
    callback返回的是{data,pythonpath} ,即打印日志数据,以及执行脚本的路径
    ```nodejs
     > let callback = function({data,pythonpath},otherargs = 11,...){
         dosomething(data,pythonpath,otherargs)
     }
     > jsexecpy.runpath("path.py",callback)
     > jsexecpy.run_ipynb_code("path.ipynb",callback)
    ```
- 5. python文件传参更新
    python some.py a b c -p=a --list=bb
    传参有两种方式
    a) string type

    ```nodejs
     > let params = "a b c -p=a --list=bb"
     > jsexecpy.runpath_with_params("some.py",params,callback)
    ```
    b) array type

    ```nodejs
     > let paramslist = ["a","b" ,"c", "-p=a", "--list=bb"]
     > jsexecpy.runpath_with_params("some.py",paramslist,callback)
    ```