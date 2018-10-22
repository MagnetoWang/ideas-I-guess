## 目录

[TOC]



### 远程仓库代码覆盖本地代码

- git reset --hard $HEAD
- git pull



### 拉取远程分支

- git pull
- git checkout  xxx



### 问题

- error: RPC failed; curl 18 transfer closed with outstanding read data remaining
  - 因为下载的包太大了。超过1个G
  - https://blog.csdn.net/lafengwnagzi/article/details/77839575
  - git config --global http.postBuffer 524288000
- ssh权限问题
  - https://www.jianshu.com/p/f22d02c7d943
  - ssh-keygen：生成密钥然后保存在指定目录
  - 找到后缀文件为pub，打开该文件将这个文件的内容复制到github官网的账号里面
  - 复制以后执行下面命令
  - ssh-add 密钥文件名字：无后缀名pub
  - 代表本机git也添加了该密钥
  - 都添加以后双方就有权限访问了
  - 

