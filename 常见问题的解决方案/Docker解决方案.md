## Docker解决方案

- 加快解决问题的效率，减少不必要的记忆和烦琐操作

[TOC]



## 容器和主机文件交换

- 显示所有容器：docker ps -a
- 获取id全名称：docker inspect -f '{{.Id}}' docker_name
- 文件复制：docker cp ID全称:容器文件路径 本地路径
  - docker cp /Users/magnetowang/Documents/4paradigm/images\ management/mnist7.png b5295ac7bc6b54deca8ab4c6dba818d520de80b3744fd8c1d44634b494f95bfa:/opt/caffe/examples/mnist/