## 说明

## 目录

[TOC]



## Python解决方案

### 文档

- python必须跟官方的来写，因为2和3语法很令人恼火
- https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
- 所有函数的库文档：https://docs.python.org/2.7/library/stdtypes.html#file-objects

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

Python 图片操作

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



## 函数说明

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

[TOC]

