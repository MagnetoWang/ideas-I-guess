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

### 下载某个项目的某个分支或者某个版本

```
git clone -b netty-4.0.33.Final --single-branch git@github.com:netty/netty.git

git clone -b gcc-5_4_0-release --single-branch https://github.com/gcc-mirror/gcc.git

git clone -b  apache-arrow-0.14.0 --single-branch https://github.com/apache/arrow.git
```

### 撤销当前所有修改内容

```
git checkout .
```

### 回滚指定位置

```
git reset --hard commitID
```

### 拉取远程分支

- git pull
- git checkout  xxx

### 本地分支推到远程分支

```
git pull
git checkout -b xxx
一般来说这是在本地新建一个分支，远程并没有这个分支

希望把xxx推到远程某个分支名上
 git push --set-upstream origin xxx
```



### 分支与分支之间的合并

```
在idea直接merge，非常方便，还会显示冲突直接选择

在命令行下
比如现在你有分支a
你要合并分支b

最好先更新分支b的内容，然后直接合并！
git checkout b
git pull

git checkout a
git merge b
```

### 更新依赖submodule

```
git submodule update --init --recursive
```

### 撤销push远端的代码

```
git reset --hard <版本号>
git push origin <分支名> --force

https://blog.csdn.net/xs20691718/article/details/51901161
```



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

### 下载大数据集文件

```
背景
在深度学习训练的时候，会有代码和数据集两类文件
代码可以托管在git服务器，并且随时同步
而数据集因为本身体积较大，不方便随时同步，因此可以给数据集打个标签，记录数据存放某个服务器的地址即可，需要的时候才下载，不需要的时候只传输地址
这就需要lfs插件来上传数据集和下载数据集，因为lfs会负责整理大数据集一系列变动，不需要人工过多干预

https://git-lfs.github.com/
lfs = large files storage

mac安装
brew install git-lfs

linux安装
wget https://github.com/git-lfs/git-lfs/archive/v2.9.0.tar.gz
tar -zxvf v2.9.0
cd git-lfs-2.9.0/
发现是go语言，放弃
系统是redhat
sudo yum install git-lfs即可
git lfs install


git lfs pull 就会把所有的数据集文件下载下来
数据集文件之前push的时候会打好hash和地址

大数据集文件标记文件的内容
version https://git-lfs.github.com/spec/v1
oid sha256:xxxxxxxxxxxxxxxxxxxxxxxxxx
size 5484424
```



### git diff 和 status高亮

```
git config --global color.ui true
```

### 撤销某个文件的修改

```
git checkout 文件名
```

### git stash用法

```
https://blog.csdn.net/wh_19910525/article/details/7784901
$git stash
$do some work
$git stash pop


git stash          # save uncommitted changes
# pull, edit, etc.
git stash list     # list stashed changes in this git
git show stash@{0} # see the last stash 
git stash pop      # apply last stash and remove it from the list

git stash --help   # for more info
```

### 生成ssh key

```
https://www.jianshu.com/p/31cbbbc5f9fa/

ssh-keygen -t rsa -C "your_email@example.com"
```



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
```
ssh-keygen -o -f ~/.ssh/id_rsa
然后复制公钥即可
```



### ssh权限不够问题

- 最好把秘钥名字改成id_rsa

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
- 如果还是无效，就是说明这个分支的权限被保护了，你不能push，只能找管理员帮忙
- 如果着急使用，可以临时拉个新分支，pull下来，merge本地代码，然后push新分支，等之后让管理员帮你远程merge即可

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

### Please move or remove them before you merge.

```
https://blog.csdn.net/chinacmt/article/details/52221733
git clean  -d  -fx ""
d  -----删除未被添加到git的路径中的文件
f  -----强制运行
x  -----删除忽略文件已经对git来说不识别的文件
```

### Clone succeeded, but checkout failed

```
项目中还包含数据集文件，数据集文件非常大！！！
所以不能下载下下来
```

