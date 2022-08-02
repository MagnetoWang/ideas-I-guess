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

### 镜像加速
```
参考文档；https://yeasy.gitbook.io/docker_practice/install/mirror

systemctl cat docker

vi /etc/docker/daemon.json
粘贴下面内容
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}

重启服务
sudo systemctl daemon-reload
sudo systemctl restart docker
```



### 容器操作

```
docker pull xxx // 拉取镜像
docker run xxx // 运行镜像
docker ps -a // 显示所有容器
docker container start id // 进入容器
docker stop id // 停止容器
docker container rm id // 删除容器

查看容器内部所有信息
docker inspect xxxx(Container)

docker // 可以启动一个可以用gdb调试的容器


快速入门
docker run -itd xxx // 镜像的名字
docker attach key // docker run 成功后会返回一个key，这个key可以进入容器内部

端口映射
docker exec -it 7f91b3579e15230b662894f749f44325f982e16d35bf647f6af0a2ac98cf95f9 /bin/bash


docker打包
docker commit 3be143f6ecd3884a442485faf235e599b2e42bcf76df80fc937b1497c2bc0ac3 xxx-your image name
sha256:0688a561dc6ad4c8215220e88fdc275ebd20f2c4428647ec8c965a877396ac32
docker push xxxx

docker镜像保存文件，并可以拷贝到其他机器上使用
docker save xxxx-镜像的名字而不是commit id > vnc-image.tar

docker load < ubuntu.tar


保存镜像
docker save redis:5.0.7 > redis.tar
加载镜像
docker load < redis.tar


docker

```

### 高级操作

```
容器里面里面执行复杂命令，
docker run -d --restart always -e --name=${xxxx} --net=host -v /data/xxx/log:/opt/xxx/log -w /opt/xxx --cap-add SYS_ADMIN -e xxx系统环境参数=25333 docker镜像名字 sh -c "mount -t nfs -o vers=3,nolock,proto=tcp,noresvport ${xxx}:${xxx} /root/xxx && mount -t nfs -o vers=3,nolock,proto=tcp,noresvport ${xxx}:${xxx} /root/xxx/xx && gunicorn -c conf/gunicorn_conf.py xxxx.application:flask_app"

如果要传递变量



查看内存，cpu占用
docker stats
```



### 容器和主机文件交换

- 显示所有容器：docker ps -a
- 获取id全名称：docker inspect -f '{{.Id}}' docker_name
- 文件复制：docker cp ID全称:容器文件路径 本地路径
  - docker cp /Users/magnetowang/Documents/4paradigm/images\ management/mnist7.png b5295ac7bc6b54deca8ab4c6dba818d520de80b3744fd8c1d44634b494f95bfa:/opt/caffe/examples/mnist/

```

```



### docker容器挂载

```
https://www.jianshu.com/p/9fd2f77001a3
docker run -itd -v /home/code-docker:/code xxxx
```

### dockerfile build 镜像

```
FROM python:3.7-alpine3.9
LABEL  MAINTAINER="soulteary <soulteary@gmail.com>"
 
ENV LIBRARY_PATH /lib:/usr/lib
 
RUN wget https://github.com/soulteary/gitbook2pdf/archive/master.zip -O /tmp/app.zip && \
    cd /tmp && unzip app.zip && mv /tmp/gitbook2pdf-master /app
 
RUN cat /etc/apk/repositories | sed -e "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/" | tee /etc/apk/repositories && \
    apk add build-base python3-dev gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev libxslt-dev && \
    cd /app && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt && \
    apk del build-base && rm -rf /var/cache/apk/*
 
VOLUME [ "/app/output" ]
VOLUME [ "/usr/share/fonts/" ]
 
WORKDIR /app
 
ENTRYPOINT [ "python", "/app/gitbook.py" ]


教程：https://soulteary.com/2019/05/07/generate-small-gitbook-pdf-using-the-docker-with-python.html
将上面的内容写到dockerfile里面
当前目录下执行
docker build -t mygitbook:1 .
这个时候就开始在打包了

docker run --rm -v `pwd`/fonts:/usr/share/fonts \
                -v `pwd`/output:/app/output \
                mygitbook:1 https://jaceklaskowski.gitbooks.io/mastering-spark-sql/content/
          
```
### docker存活监控脚本
```

is_alive_docker=`docker inspect --format '{{.State.Running}}' dockerxxxxxx`

echo docker alive status: $is_alive_docker

if [ $is_alive_docker = 'false' ]; then
    sleep 3
fi

```

### 常用容器服务

#### 启动 postgres 服务
```
版本9比较稳定，最新版可能有各种兼容问题

https://hub.docker.com/_/postgres?tab=description

docker pull postgres:9
docker run --net=host --name test_postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=magnetowang -e PGDATA=/var/lib/postgresql/data/pgdata -v /data/home/magnetowang/docker/postgres/pgdata:/var/lib/postgresql/data/c -p 5432:5432 -d postgres:9




```