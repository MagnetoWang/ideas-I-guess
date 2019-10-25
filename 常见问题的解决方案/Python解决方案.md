## 说明

## 目录

[TOC]



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

### list对象的增删改查

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
```

### dict字典

```
dict = {}

# 如果有xxx，那么就是更新，如果没有xxx，那么就是新增一个键值
dict["xxx"] = xxxxxx
```



### set集合

```
empty_set = set()

empty_set.add(xxx)
empty_set.remove(xxx)

如果元素不存在,不报错
empty_set.discard(xxx)
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

### class 类

```
def __init__(self, texts, batch_size=16):
	xxxx
	
类似于Java的构造函数
self默认为this
texts, batch_size=16是传入参数
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



[TOC]

