

## 说明

## 目录







## Python解决方案

### 常识

#### pip命令

```
pip install --upgrade pip
```

#### conda命令

```
conda config --show channels

conda不能下载第三方库，只能安装pip的官方库
```

#### pycharm

```
三种安装额外包，conda，pip和手动
pycharm可以给每个项目开新的库环境，根据这一特点，用户非常方便管理不同项目所依赖的包

远程开发服务器代码
需求：代码和数据集都在服务器中，本地端只保留代码。运行在服务端
方便调试，所有计算资源都托管在服务器上


```

#### 安装python

```
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tar.xz
tar -xvf Python-3.7.5.tar.xz
cd Python-3.7.5
mkdir build
./configure --prefix=/home/wangzixian/python/Python-3.7.5/build
make -j12 && make install

export PATH=xxxx/python/Python-3.7.5/build/bin:$PATH
确定python解释器是否安装成功
which python3


注意
If you want a release build with all stable optimizations active (PGO, etc),
please run ./configure --enable-optimizations
```

#### 安装conda

```
linux下
wget 
sh Anaconda3-5.3.0-Linux-x86_64.sh
在内部需要指定安装路径
最后配置好路径即可
source ~/python/anaconda3/etc/profile.d/conda.sh
```



### 文档

- python必须跟官方的来写，因为2和3语法很令人恼火
- https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
- 所有函数的库文档：https://docs.python.org/2.7/library/stdtypes.html#file-objects

### 代码规范

- 函数名称
  - 小写字母和下划线分隔
  - sync_dir
  - get_env
- 变量名
  - 小写字母和下划线分隔
  - pass_envs
  - working_dir
  - node
- 类名
  - 大写首字母其余小写
  - LocalLauncher

### 单元测试

- unittest模块
  - https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140137128705556022982cfd844b38d050add8565dcb9000
  - 架构介绍：https://cloud.tencent.com/developer/article/1085258
  - 如何自动化测试：https://www.jianshu.com/p/bc6c93b8d601
  - 断言汇总：https://blog.csdn.net/qq1124794084/article/details/51668672
- ddt数据传输：https://www.cnblogs.com/hellowcf/p/6962935.html
- ddt文档：https://ddt.readthedocs.io/en/latest/api.html



### subprocess

- 调用子进程的函数：http://www.cnblogs.com/vamei/archive/2012/09/23/2698014.html
- 进程文本基本通信：http://www.cnblogs.com/vamei/archive/2012/09/23/2698014.html
- 多轮通信：
  - 2.7版本是阻塞方式，不管怎么使用都会读到EOF然后终止通信
  - 所以需要其他小技巧来实现交互
  - https://stackoverflow.com/questions/50434204/running-interactive-program-from-within-python：可行
  - https://stackoverflow.com/questions/3065060/communicate-multiple-times-with-a-process-without-breaking-the-pipe
  - https://www.cnblogs.com/suwings/p/6216279.html
- 文档：https://docs.python.org/2.7/library/subprocess.html#module-subprocess

### 并行自动化测试

- -m 和 .py 冲突
  - https://docs.python.org/2/using/cmdline.html#cmdoption-m
  - AttributeError: 'module' object has no attribute 'py'
  - https://stackoverflow.com/questions/39527284/module-object-has-no-attribute-py-when-running-from-cmd
- 多进程插件
  - nosetests --plugins：查看插件
  - https://blog.csdn.net/jianhong1990/article/details/8268876

### 文件路径问题

- read_path = "/tmp/server_in"
  - 格式错误。没办法打开
  - IOError: [Errno 2] No such file or directory: 'test.txt'
  - read_path = "tmp/server_in" 正确做法是去掉第一个反斜杆
- 

### Python 图片操作

- PIL文档：https://pillow.readthedocs.io/en/4.2.x/reference/Image.html
- 颜色转化公式：https://blog.csdn.net/icamera0/article/details/50843196
- image = Image.fromarray(one_pic_arr)
- 这一步数组转化成图片，容易出问题，有bug。后面再仔细查找

### python常用对象转字符串

- str(对象)
- json.dumps(dict)

### 字符串转数字

```
int(str)
```

### 字符串

```
字符串拼接

```



### list对象的基本操作

- py2
- 直接复制，直接运行。
- 执行命令：python xx.py

```python
list = []
# 增加
for i in range(10):
    list.append(i)
print list
# 插入
list.insert(4, 44)
# 修改
list[4] = 44
print list
# 删除
list.pop(4)
print list

遍历list
for s in list_xxxx:
  实现xxxxxxxx
  
遍历list的大小
for index in range(len(list)):
  xxxxxx
  

将列表每个元素拼接起来
code = []
"\n".join(code)

len(list) 返回list的size
```

### dict字典

```
dict = {}

# 如果有xxx，那么就是更新，如果没有xxx，那么就是新增一个键值
dict["xxx"] = xxxxxx

循环遍历字典
 for key, value in dict.items():
        print("pos_name_.insert(\"", key, "\", \" ", value, "\");")
```



### set集合

```
empty_set = set()

empty_set.add(xxx)
empty_set.remove(xxx)

如果元素不存在,不报错
empty_set.discard(xxx)

初始化
t = set(['h', 'e', 'l', 'l', 'o'])
或者
t = {"sum", "max"}
```

### print

```
https://www.w3schools.com/python/ref_func_print.asp
print(object(s), separator=separator, end=end, file=file, flush=flush) 

打印多个变量的时候，python会默认打印空格隔开，如果不想有空格隔开，可以加seq指定分隔符
print('pos_name_.insert(std::make_pair(\"', key, "\", \"", value, "\"));", sep="")
```

### json格式化输出

```
json.dumps(dict_xxx, sort_keys=False, indent=4, separators=(',', ':'))
```



## 命令行下的python

### 执行

```
cd src
export PYTHONPATH=`pwd`:$PYTHONPATH
python3 -m unittest test/*_test.py

pythonpath是维护一个python项目的重要路径！

建议统一用anaconda管理，设置环境
source /xxxx/anaconda3/bin/activate
conda activate base
```

### 调试

```
python3 -m pdb xxx

断点的方法和gdb基本一致，可以查看c++解决方案
```

### 依赖库导入

```
https://www.anaconda.com/distribution/#download-section

wget https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.sh

sh xx
bach文件会自动写入路径配置，非常方便
source ~/.bashrc


自动每个终端识别python环境
conda config --set auto_activate_base True

安装网站
https://anaconda.org/conda-forge/pyspark

安装pandas
conda install -c anaconda pandas

安装pyspark
conda install -c conda-forge pyspark


安装自动补全插件
conda install -c conda-forge jupyter_contrib_nbextensions


```

### 环境布置

```
virtualenv
https://virtualenv.pypa.io/en/stable/

source /opt/rh/rh-python36/enable
python -m pip install --user virtualenv
```

### juypter安装

```
https://jupyter.org/
conda install -c conda-forge jupyterlab
或者
pip install jupyterlab

运行juypter
https://jupyter.readthedocs.io/en/latest/running.html#running
jupyter notebook


修改ip和端口
jupyter notebook --ip=172.27.128.37  --port=8889

查看命令
jupyter notebook --help

自动补全
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user --skip-running-check
3、重启jupyter，在弹出的主页面里，能看到增加了一个Nbextensions标签页，在这个页面里，勾选Hinterland即启用了代码自动补全。

注：如果页面无Hinterland项，或者不全，命令行执行：


查看搭建的jupyter搭建服务的token
jupyter notebook list 
```

### conda配置

```
查看配置
conda info

切换源
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/

conda config --set show_channel_urls yes

```



## pycharm下的python

### 设置自己的项目

```
导入自己项目的时候，pycharm无法识别自己的模块，需要手动添加识别路径
https://blog.csdn.net/weixin_40807247/article/details/82781032

右键make_directory as-->sources path将当前工作的文件夹加入source_path就可以了。
```

## 多线程

```
https://zhuanlan.zhihu.com/p/43352965
```



## 语法

### OS模块

- 举例说明
  - https://www.jianshu.com/p/5fb5dc9d4906

- os.getenv('PATH')
  - 获取当前环境变量

### 系统输入输出-sys.stdin stdout

- sys.stdout.write('hello'+'\n')  等价于 print
- sys.stdin 等价于 raw_input
- 参考
  - https://www.cnblogs.com/turtle-fly/p/3280519.html

### argparse

- 命令行解析包
  - 入门使用：https://www.jianshu.com/p/fef2d215b91d
  - 官方文档：https://docs.python.org/3/library/argparse.html



### input()和raw_input()

- raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float )

### 文件读写

- Python2.7 
  - 参数不能rw，否则无法写入，弄了我3个小时了。靠
  - 一定要照着文档的example来写，网上其他的代码到处都是坑，很不严谨！！！！
  - https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects

- 读写顺序，异常顺序要保持一致

- ```python
  try:
      os.mkfifo(write_path)
      os.mkfifo(java2py_path)
  except OSError:
      print 'making fifo is failed'
      os.remove(write_path)
      os.remove(java2py_path)
  ```

- 管道的打开顺序很重要

  - Examples：https://www.programcreek.com/python/example/3522/os.mkfifo

```
python3

https://www.jianshu.com/p/85f1d3c0dce0
# -*- coding: utf-8 -*-
with open('path\filename', 'w') as file_obj:
    file_obj.write('I love Python.')
    
    
读json


读文件

```



### class 类

```
def __init__(self, texts, batch_size=16):
	xxxx
	
类似于Java的构造函数
self默认为this
texts, batch_size=16是传入参数
```

### __ getitem __ 等类型函数

```
当实例对象通过[] 运算符取值时，会调用它的方法__getitem__
https://zhuanlan.zhihu.com/p/27661382


https://blog.csdn.net/xhw88398569/article/details/48690577
__len__ 当使用len(A)该对象时调用该方法，当没有该方法是会报错，且返回数据不为整数也会报错
__reversed__():当使用reversed函数翻转对象时调用
__contains__():当使用in，not in 对象的时候 调用(not in 是在in完成后再取反,实际上还是in操作)

```

### 打印当前路径

```
print(__file__)
```

### 读取json文件

```
f = open("../../onebox/config.json", encoding='utf-8')
code = """multi_last_value(sample,product.sku_id,10)"""
config_obj = json.load(f)
        
读取json字符串        
config_obj = json.loads(json_str)        
        
        
```

### isinstance

```
https://www.runoob.com/python/python-func-isinstance.html
isinstance(object, classinfo)
object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。


>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True

```

### None

```
判断是否为None的情况
if x != None 不建议
if x is not = None 推荐
```

### ascii码和字符转换

```
https://blog.csdn.net/yzy_1996/article/details/89556049
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

### timeit 计时器

```

https://www.cnblogs.com/PrettyTom/p/6657984.html

#导入timeit.timeit
from timeit import timeit  

#看执行1000000次x=1的时间：
timeit('x=1')

#看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
timeit('x=1', number=1)

#看一个列表生成器的执行时间,执行1次：
timeit('[i for i in range(10000)]', number=1)

#看一个列表生成器的执行时间,执行10000次：
timeit('[i for i in range(100) if i%2==0]', number=10000)


测试一个函数的执行时间
from timeit import timeit

def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000)
print(t)
```



## 正则表达式

### 获取括号里面的内容

```
https://www.jb51.net/article/141283.htm

# -*- coding:utf-8 -*-
#! python2
import re
string = 'abe(ac)ad)'
p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))

输出：

    ['ac']
    ['ac)ad']

解释一下：

1.正则匹配串前加了r就是为了使得里面的特殊符号不用写反斜杠了。

2.[ ]具有去特殊符号的作用,也就是说[(]里的(只是平凡的括号

3.正则匹配串里的()是为了提取整个正则串中符合括号里的正则的内容

4. .是为了表示除了换行符的任一字符。*克林闭包，出现0次或无限次。

5. 加了？是最小匹配，不加是贪婪匹配。

6. re.S是为了让.表示除了换行符的任一字符。

PS：这里再为大家提供2款非常方便的正则表达式工具供大家参考使用：

JavaScript正则表达式在线测试工具：
http://tools.jb51.net/regex/javascript

正则表达式在线生成工具：
http://tools.jb51.net/regex/create_reg
```



## Python的奇怪语法

### 逗号

- 参考资料：<http://www.runoob.com/python3/python3-tuple.html>
- ​        losses = self.loss_detection, self.loss_landmarks, self.loss_visibility, self.loss_pose, self.loss_gender, self.loss
- losses是元组类型，默认可以不加括号

### 下划线

- 参考资料：<http://www.runoob.com/w3cnote/python-5-underline.html>
-  self.session.run返回三个值，其中一个值返回给_
- _：表示临时变量或者没有意义的变量

```
        _, merged_summary, loss_values = self.session.run([self.train_op, self.merged_summary, losses], feed_dict={
            self.inputs: inputs,
            self.detection_gt: outputs.detection,
            self.landmarks_gt: outputs.landmarks,
            self.visibility_gt: outputs.visibility,
            self.pose_gt: outputs.pose,
            self.gender_gt: outputs.gender,
        })
```

### 切片

- 参加资料：<https://blog.csdn.net/xpresslink/article/details/77727507>

```

```

### 列表生成法

```

test = [[0 for i in range(m)] for j in range(n)]

```

### 生成二维数组

- 参考资料：<https://www.cnblogs.com/PyLearn/archive/2017/11/06/7795552.html>

```
列表生成法
test = [[0 for i in range(m)] for j in range(n)]

模块numpy创建
import numpy as np
test = np.zeros((m, n), dtype=np.int)

生成随机二维数组
test = np.random.random((3,5))

切割数组验证
print(test)
test[:,1:]
```

### 两个斜杆

```
https://blog.csdn.net/HappyRocking/article/details/79806499
双斜杠（//）表示地板除，即先做除法（/），然后向下取整（floor）。至少有一方是float型时，结果为float型；两个数都是int型时，结果为int型。
```



## Python的陷阱

### 新建一个变量

- 参考资料：<https://www.cnblogs.com/ifantastic/p/3811145.html>

```

```

### module 'tensorflow' has no attribute 'placeholder'

```
https://stackoverflow.com/questions/37383812/tensorflow-module-object-has-no-attribute-placeholder



It happened to me too. I had tensorflow and it was working pretty well, but when I install tensorflow-gpu along side the previous tensorflow this error arose then I did these 3 steps and it started working with no problem:

    I removed tensorflow-gpu, tensorflow, tensorflow-base packages from Anaconda. Using. conda remove tensorflow-gpu tensorflow tensorflow-base
    re-installed tensorflow. Using conda install tensorflow


使用conda方式重新安装tensorflow
conda install tensorflow
```

### cannot unpack non-iterable NoneType object

```
没有return的时候，是默认返回none
```

### only list-like objects are allowed to be passed to isin()

```
输入参数不对，不好用这个方法，不用了
```

### 作用域

```
python和c++，java作用域用法完全不一样！！

https://blog.csdn.net/wentyoon/article/details/53301594

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域

LEGB原则搜索变量，即优先级L>E>G>B。

#dir 为python内建函数
dir = 1 # Global
def outer():
    dir = 2  # Enclosing
    def inner():
        dir = 3 # Local
        return dir
    return inner

print outer()() # 输出3


有local变量，就会跟着local，不管你的作用域在哪里
无法隔离开来

```



# 新项目

## 爬虫

### 库

```

```

### 问题

#### ssl 验证不通过 urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1051)>

```
https://www.cnblogs.com/my8100/p/7279133.html
因为有校验过程，需要跳过
全局设置加一行代码
ssl._create_default_https_context = ssl._create_unverified_context

```

#### urllib.error.HTTPError: HTTP Error 403: Forbidden

```
在请求的对象里面，添加更多头文件信息，模拟浏览器的请求

```

## 数据分析

### pyspark

```
读数据：https://towardsdatascience.com/a-brief-introduction-to-pyspark-ff4284701873
入门实战：https://www.jianshu.com/p/5a42fe0eed4d
```



[TOC]

