## 说明

## 目录

[TOC]



## Python解决方案



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





## 函数说明

### OS模块

- 举例说明
  - https://www.jianshu.com/p/5fb5dc9d4906

- os.getenv('PATH')
  - 获取当前环境变量



### argparse

- 命令行解析包
  - 入门使用：https://www.jianshu.com/p/fef2d215b91d
  - 官方文档：https://docs.python.org/3/library/argparse.html





[TOC]

