## 目录

[TOC]

### 命令清单

- http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html
- https://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%82%A8%E8%97%8F%EF%BC%88Stashing%EF%BC%89

### 远程仓库代码覆盖本地代码

- git reset --hard $HEAD
- git pull

### 克隆最新一次提交的代码，不要历史提交

- git clone --depth 1 xxx

### 拉取远程分支

- git pull
- git checkout  xxx

### 解决冲突问题

- 出现confilct
- 在当前分支执行 git merge origin/远程的主分支
- merge之后将会出现，冲突的代码，然后手动删除就行了

### 无法rm文件

- fatal: pathspec 'test-common/integrationtest/testcase/test_setlimit.py' did not match any files
- 一文件不存在
- 二，就是文件不在git管理的范围，也就是要先git add 这个文件，然后才能remove

### 查看修改内容

- git log -p filename

### 无法提交因为有没有合并到文件

- https://stackoverflow.com/questions/12961752/git-merge-error-commit-is-not-possible-because-you-have-unmerged-files
- git merge 一下分支

### 解决github下载速度太慢的问题

- 一是翻墙用外网
- 二是我经常用的方法
  - fork你要下载的仓库
  - 然后导入码云仓库中
  - 码云在国内的服务器，让你下载有飞一般的感觉

## 问题

### error: RPC failed; curl 18 transfer closed with outstanding read data remaining

- 因为下载的包太大了。超过1个G
- https://blog.csdn.net/lafengwnagzi/article/details/77839575
- git config --global http.postBuffer 524288000

### ssh权限问题

- https://www.jianshu.com/p/f22d02c7d943
- ssh-keygen：生成密钥然后保存在指定目录
- 找到后缀文件为pub，打开该文件将这个文件的内容复制到github官网的账号里面
- 复制以后执行下面命令
- ssh-add 密钥文件名字：无后缀名pub
- 代表本机git也添加了该密钥
- 都添加以后双方就有权限访问了
### Cannot update paths and switch to branch at the same time
  - 命令行写错别字
### git push
  - Everything up-to-date
  - 已经commit了
  - 无法push上去
  - 解决：必须和远程分支的名字一样
###  git commit 撤销

  - https://www.jianshu.com/p/9f11d398111f
  - git reset HEAD~

### warning: push.default is unset

- 参考资料：https://www.jianshu.com/p/e26175b2e916
- git config --global push.default matching

### pre-receive hook declined

- [remote rejected] develop -> develop (pre-receive hook declined)
- 解决方案
  - 添加你要push的分支名
  - git push origin branch_name

### GitHub Desktop was unable to store the account token in the keychain. Please check you have unlocked access to the 'login' keychain.

- <https://github.com/desktop/desktop/issues/4614>
- 打开钥匙串应用
- 先锁住钥匙串再解锁
- 然后重新登录就解决了

### key_load_public: invalid format

- 重新创建秘钥和公钥
- 正常来讲，应该出现xxx和xxx.pub两个文件

### ssh_add 出现 Could not open a connection to your authentication agent

- 参考资料：<https://blog.csdn.net/roserose0002/article/details/40078577>

```
先执行
eval `ssh-agent`
ssh-add ~/.ssh/rsa
```

