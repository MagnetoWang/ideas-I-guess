

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

查找字符
txt.find(xxx)
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

集合 交集、并集、差集运算
交集 	& 	取两集合公共的元素 	>>> set1 & set2
{3}
并集 	| 	取两集合全部的元素 	>>> set1 | set2
{1,2,3,4,5}
差集 	- 	取一个集合中另一集合没有的元素 	>>> set1 - set2
{1,2}
>>> set2 - set1
{4,5}
对称差集 	^ 	取集合 A 和 B 中不属于 A&B 的元素 	>>> set1 ^ set2
{1,2,4,5}


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

### for循环

```

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

```



### json格式化输出

```
json.dumps(dict_xxx, sort_keys=False, indent=4, separators=(',', ':'))


json.load 读取文件
json.loads 读取json字符串
```

### yaml格式化读写

```
https://www.cnblogs.com/yoyoketang/p/9255109.html


```

### 文件操作

```
https://www.cnblogs.com/sysuoyj/archive/2012/03/14/2395789.html
按行读
f = open("foo.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    print line,                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()

for line in open("foo.txt"):
    print line
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

安装pytorch

```

### 环境布置

```
virtualenv
https://virtualenv.pypa.io/en/stable/

source /opt/rh/rh-python36/enable
python -m pip install --user virtualenv


===========================================================================
pyenv 可以隔离不同python环境
https://github.com/pyenv/pyenv-virtualenv
https://github.com/pyenv/pyenv#basic-github-checkout
https://www.jianshu.com/p/861f9a474f70

安装
国外
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
国内
git clone https://gitee.com/mirrors/pyenv.git ~/.pyenv
export PYTHON_BUILD_MIRROR_URL="https://npm.taobao.org/mirrors/python/"

国内加速
export v=3.7.1; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v 

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

bashrc

安装某个python版本
pyenv install 3.7.1


pyenv virtualenv 2.7.1 env271

在当前目录下创建一个 python 版本为2.7.1的环境，环境名字为 env271。 这个环境的真实目录位于~/.pyenv/versions/

pyenv activate env271

（创建时并不激活）激活当前环境。此时已经进入虚拟环境，在当前环境下所有pip等操作都不会影响系统环境和系统路径。

pyenv deactivate

离开已激活的环境，切换回系统环境。但并没有被删除，下次依旧可以启动。

pyenv uninstall env271

删除一个环境，当然也可以到真实目录下删除文件夹
===========================================================================

安装virtualenvs
国内码云
git clone https://gitee.com/cattus/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile




===========================================================================
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

### 导入自己项目的包

```

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
https://www.runoob.com/python/python-object.html

def __init__(self, texts, batch_size=16):
	xxxx
	
类似于Java的构造函数
self默认为this
texts, batch_size=16是传入参数



    __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    __doc__ :类的文档字符串
    __name__: 类名
    __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）


类的继承
```



### 重载函数

```
python不支持c++的重载特性！！！

因为python可以一个函数，覆盖所有形参，从而达到重载的效果
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

### __ file __

```
https://blog.csdn.net/bestallen/article/details/52079847

__file__表示显示文件当前的位置

但是：

如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！

如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！
```

### __ name __

```
返回当前文件的名字
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

### rst生成文档

```
pip install -r requirements.txt

txt内容
sphinx==2.4.4
-e git+https://github.com/pytorch/pytorch_sphinx_theme.git#egg=pytorch_sphinx_theme
sphinxcontrib.katex
matplotlib
javasphinx

```

### init .py 作用详解
```
https://www.cnblogs.com/Lands-ljk/p/5880483.html

__init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。

# package
# __init__.py
import re
import urllib
import sys
import os

# a.py
import package 
print(package.re, package.urllib, package.sys, package.os)

__init__.py中还有一个重要的变量，__all__, 它用来将模块全部导入。

# __init__.py
__all__ = ['os', 'sys', 're', 'urllib']

# a.py
from package import *

当导入模块时，解释器按照sys.path列表中的目录顺序来查找导入文件
import sys
>>> print(sys.path)
```

### 文件之间的依赖

```
https://www.zhihu.com/question/38857862

from 文件夹/模块名 import 函数名

import 模块名
```

### yield

```
说明：https://developer.ibm.com/zh/technologies/python/articles/os-cn-python-yield/

 yield 的函数在 Python 中被称之为 generator（生成器）
 
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
        

这一段是生成斐波列数字的代码
print改成yield以后
for n in fab(5):
	print n
	
那么for循环中每次会调用fab函数计算
而不是只调用一次，然后拿全部的斐波列数字的结果
生成器就是每次生成下次结果，之前的结果不关系，从而节省了空间！
```



### range 和 xrange区别

```
xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。
xrange可以比range更节省空间
```

### logging设置

```
https://www.cnblogs.com/pycode/p/logging.html

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  \
                    datefmt='%a, %d %b %Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.info("hello world")


format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:

    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息

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

### ImportError: cannot import name 'PILLOW_VERSION' from 'PIL'

```
https://blog.csdn.net/ternence_hsu/article/details/103821264

要安装7.0.0以下版本才行
    pip uninstall Pillow
    pip install Pillow==6.2.2
pip3 install 'pillow<7.0.0'

conda 安装最合适
conda install 'pillow<7.0.0'

这个方法也可能无效
https://blog.csdn.net/Lee_lg/article/details/103901632

直接修改源码，出错的文件，重新导入
使用from PIL import Image, ImageOps, ImageEnhance, __version__ 替换文件中from PIL import Image, ImageOps, ImageEnhance,PILLOW_VERSION这句。

说白了就是用__version__ 替换原来的PILLOW_VERSION。点击保存即可。
```

### pyenv-virtualenv: `3.7.1' is not installed in pyenv.

```
https://stackoverflow.com/questions/51698662/pyenv-virtualenv-3-6-4-is-not-installed-in-pyenv

pyenv install 3.7.1
```

### Perhaps pyenv-virtualenv has not been loaded into your shell properly.

```
https://www.cnblogs.com/walker-/p/10976027.html
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### No module named 'Queue'

```
https://blog.csdn.net/DarrenXf/article/details/82962412
写法不同
py3
import queue

py2
import Queue
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

## 单元测试

```
unittest
https://www.cnblogs.com/feng0815/p/8045850.html


pytest
https://www.jianshu.com/p/932a4d9f78f8


```

## kafka

- python 调用：https://github.com/confluentinc/confluent-kafka-python

```
kafka客户端：https://github.com/dpkp/kafka-python 
pykafka：https://github.com/Parsely/pykafka
kafka demo：https://github.com/muscledreamer/Kafka_Demo

kafka开发手册：http://kafka.apache.org/25/documentation/streams/developer-guide/
kafka官网多语言说明：https://cwiki.apache.org/confluence/display/KAFKA/Clients
多语言功能区别：https://docs.confluent.io/current/clients/index.html
流式写入：http://kafka.apache.org/25/documentation/streams/core-concepts
python高性能写入和消费，封装底层c++：https://docs.confluent.io/current/clients/python.html#python-client

kafka客户端配置：https://docs.confluent.io/current/clients/confluent-kafka-python/#pythonclient-configuration
c语言客户端配置：https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
kafka schema配置：https://docs.confluent.io/current/schema-registry/index.html

kafka代码演示：https://docs.confluent.io/current/clients/python.html

python3标准库编解码：https://docs.python.org/3/library/codecs.html#standard-encodings
```

### 安装

```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/kafka/2.5.0/kafka_2.12-2.5.0.tgz
```



### 快速入门

```
http://kafka.apache.org/quickstart

tar -xzf kafka_2.12-2.5.0.tgz
cd kafka_2.12-2.5.0

没有zk服务，可启动单节点zk。有则忽略
bin/zookeeper-server-start.sh config/zookeeper.properties

启动kafka服务
bin/kafka-server-start.sh config/server.properties

创建topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

检查topic
bin/kafka-topics.sh --list --bootstrap-server localhost:9092


```

## swig

### 资料

```
简单示例：https://segmentfault.com/a/1190000013219667
快速入门：https://www.ibm.com/developerworks/cn/aix/library/au-swig/
```



[TOC]

