## 目录

[TOC]

### 命令清单

- http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html
- https://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%82%A8%E8%97%8F%EF%BC%88Stashing%EF%BC%89

### 远程仓库代码覆盖本地代码

- git reset --hard $HEAD
- git pull



### 拉取远程分支

- git pull
- git checkout  xxx





## 查看修改内容

- git log -p filename

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
- Cannot update paths and switch to branch at the same time
  - 命令行写错别字
- git push
  - Everything up-to-date
  - 已经commit了
  - 无法push上去
  - 解决：必须和远程分支的名字一样
- git commit 撤销
  - https://www.jianshu.com/p/9f11d398111f
  - git reset HEAD~

