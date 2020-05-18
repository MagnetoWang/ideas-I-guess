## Docker解决方案

- 加快解决问题的效率，减少不必要的记忆和烦琐操作

[TOC]

### 基本操作

- docker与本机互相传输文件：https://segmentfault.com/a/1190000011609175
  - docker cp ID全称:容器文件路径 本地路径
  - docker ps -a：获取所有容器的名字和短ID
  - docker inspect -f '{{.Id}}' docker_name：获取id全名称
  - 6adbf95b93b03fbc628db0d95c82a0fddab078f81ccdc5d3943170cfb0dc808d
- docker命令教程：https://yeasy.gitbooks.io/docker_practice/image/rm.html
- 容器如何进入
  - 启动：docker container start id
  - 进入容器命令行：docker attach id
- 删除容器：docker container rm **id**
- 显示所有容器：docker ps -a



### 容器操作

```
docker pull xxx // 拉取镜像
docker run xxx // 运行镜像
docker ps -a // 显示所有容器
docker container start id // 进入容器
docker stop id // 停止容器
docker container rm id // 删除容器

docker // 可以启动一个可以用gdb调试的容器


快速入门
docker run -itd xxx // 镜像的名字
docker attach key // docker run 成功后会返回一个key，这个key可以进入容器内部

端口映射
docker exec -it 7f91b3579e15230b662894f749f44325f982e16d35bf647f6af0a2ac98cf95f9 /bin/bash

```



### 容器和主机文件交换

- 显示所有容器：docker ps -a
- 获取id全名称：docker inspect -f '{{.Id}}' docker_name
- 文件复制：docker cp ID全称:容器文件路径 本地路径
  - docker cp /Users/magnetowang/Documents/4paradigm/images\ management/mnist7.png b5295ac7bc6b54deca8ab4c6dba818d520de80b3744fd8c1d44634b494f95bfa:/opt/caffe/examples/mnist/

### docker容器挂载

```
https://www.jianshu.com/p/9fd2f77001a3
docker run -itd -v /home/code-docker:/code xxxx
```

