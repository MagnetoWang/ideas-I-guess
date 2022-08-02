## 目录

[TOC]

### 命令清单

- http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html
- https://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%82%A8%E8%97%8F%EF%BC%88Stashing%EF%BC%89

### 修改用户名

```
git config --global user.name xxx
git config --global user.email xxx
```

### Git rebase 合并commit

```
git rebase --edit-todo

合并某个分支，但是没有commit
git rebase xxx 

出现冲突，先修改，然后
git add xxxx
再执行
git rebase --continue
重复上面两个操作

修复冲突后继续更改
git rebase --continue


放弃更改
git rebase --abort  

使用说明：https://zhuanlan.zhihu.com/p/34197548

```



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

### 撤销当前commit，但是修改内容不回退
```
必须用soft
git reset --soft HEAD^


```

### 回滚指定位置

```
git reset --hard commitID
```

### 拉取远程分支

- git pull
- git checkout  xxx

### 删除远程分支

```
git push origin --delete <branchName>
```



### 本地分支推到远程分支

```
git pull
git checkout -b xxx
一般来说这是在本地新建一个分支，远程并没有这个分支

希望把xxx推到远程某个分支名上
 git push --set-upstream origin xxx
```

### 新建分支

```

git checkout 主分支
git checkout -b branchname // 从主分支拉新分支
git push origin branchname // 推送到远程分支
```



### 删除远程分支

```
git push origin --delete xxxx

https://www.cnblogs.com/utank/p/7880441.html
删除其他分支
git branch -d xxx

删除当前的分支-一般不用
git branch -D xxx

```



### 从某一个commit开始创建本地分支

```
// 通过checkout 跟上commitId 即可创建制定commit之前的本地分支
git checkout commitId -b 本地新branchName


// 依然通过push 跟上你希望的远程新分支名字即可
git push origin HEAD:远程新branchName

```



### 分支与分支之间的合并merge

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
### 合并某个commit功能
```

 git cherry-pick 1d502fb0bca93c23d89c8d95b3714be4ace67fb8

```
### 开发分支落后主分支太多commit，无法直接merge到主分支

```
只能一个个解决
```



### 更新依赖submodule

```
git submodule update --init --recursive
```

### 修改子模块的commit

```
 git submodule update --init --recursive
 
 cd xxxx-子模块名字目录
 git checkout 8b2a7b9c3f9e9a39aeb3d5222bcd85b8962ac56
 git pull
 cd ..
 git add xxxx
 git commit -m "xxx"
 git push
```

### 修改commit的message信息
```
https://docs.github.com/cn/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message

重写最近的提交消息
 git commit --amend

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



### git blame xxx 查看文件历史修改记录

```
https://www.jianshu.com/p/9b691ba43357

git blame 文件名
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

### git tag

```
版本号打tag
git add -u && git commit -m "1.7.6.7-RELEASE" && git push
git tag -a v1.7.6.7 -m "1.7.6.7-RELEASE"
git push origin v1.7.6.7

git tag -a v1.7.7.8-rc3 -m "1.7.7.8-rc3"
git push origin v1.7.7.8-rc3
```



### 生成ssh key

```
https://www.jianshu.com/p/31cbbbc5f9fa/

ssh-keygen -t rsa -C "your_email@example.com"
```



### 统计git成员代码情况

```
https://rzrobert.github.io/2017/02/04/git%E7%BB%9F%E8%AE%A1%E9%A1%B9%E7%9B%AE%E4%B8%AD%E5%90%84%E6%88%90%E5%91%98%E4%BB%A3%E7%A0%81%E9%87%8F/

查看git上个人代码量

git log --author="username" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -

统计每个人的增删行数

git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done

查看仓库提交者排名前 5

git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r | head -n 5

贡献者统计：

git log --pretty='%aN' | sort -u | wc -l

提交数统计：

git log --oneline | wc -l

```

### git 查询一个文件的历史所有更改内容

```


git log --pretty=oneline pom.xml> log.txt
awk '{print $1}'

git show 3cd413eabb29e23dce952dc775c9e41fa99460c8

```

### 项目迁移保留历史commit

```
https://www.huaweicloud.com/articles/e5d045b6fb38a4f9b481345b3f4f5409.html

1). 从原地址克隆一份裸版本库，比如原本托管于 GitHub。

git clone --bare git@git.oschina.net:tantexian/wishPatterns.git

--bare 创建的克隆版本库都不包含工作区，直接就是版本库的内容，这样的版本库称为裸版本库。

2). 然后到新的 Git 服务器上创建一个新项目，比如 wishPatterns。

3). 以镜像推送的方式上传代码到 GitCafe 服务器上。

cd wishPatterns.git
git push --mirror https://github.com/tantexian/wishPatterns.git

-- mirror 克隆出来的裸版本对上游版本库进行了注册，这样可以在裸版本库中使用git fetch命令和上游版本库进行持续同步。

4). 删除本地代码

cd ..
rm -rf wishPatterns.git

5). 到新服务器 GitCafe 上找到 Clone 地址，直接 Clone 到本地就可以了。

git clone https://github.com/tantexian/wishPatterns.git
```

### git关闭权限
```
https://learnku.com/laravel/t/5340/linux-solution-to-modify-the-file-permissions-caused-by-the-git-record-file-changes

git 默认会跟踪文件的权限修改，当我们使用 chmod 指令的时候，git 也会把被修改权限的文件添加到被修改的状态。

cat .git/config
git config core.filemode false
```

## CICD

### 安装cicd在服务器上

```
https://docs.gitlab.com/runner/install/

讲解：https://developer.aliyun.com/article/719968

背景，已经有gitlab的服务，但是公用的机器资源不够，需要在自己的服务器搭建一个runner

docker run -d --name gitlab-runner --restart always -v /srv/gitlab-runner/config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner:latest
--name gitlab-runner 这个名字可以随意，最好定制化的名字
注册gitlab
docker exec -it gitlab-runner bash
gitlab-runner register

填信息和token，可以在gitlab网页的cicd设置中看到，类似于和gitlab取得联系和信任
------------------------------------------------------------------------
输入Gitlab实例的地址

Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com )
http://xxx

输入token

Please enter the gitlab-ci token for this runner
xxx

输入Runner的描述

Please enter the gitlab-ci description for this runner
[hostname] my-runner 这个随意

输入与Runner关联的标签

Please enter the gitlab-ci tags for this runner (comma separated):
my-tag,another-tag 这个随意

输入Ruuner的执行者

Please enter the executor: ssh, docker+machine, docker-ssh+machine, kubernetes, docker, parallels, virtualbox, docker-ssh, shell:
docker

如果上面执行者为docker，需要你在.gitlab-ci.yml中指定docker版本

Please enter the Docker image (eg. ruby:2.1):
alpine:latest 这个也可以随意
------------------------------------------------------------------------
修改toml文件
vim /srv/gitlab-runner/config/config.toml
每次修改需要重启docker
docker restart gitlab-runner


配置示例
[[runners]]
  name = "wangzixian"
  url = "xxxx"
  token = "xxx"
  executor = "docker"
  output_limit = 409600
  [runners.custom_build_dir]
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "xxxxx"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
    pull_policy = "if-not-present"

```

### 针对master分支发布版本

```
deploy:
  stage: deploy
  script:
    - mvn deploy -U -Dmaven.test.skip=true
  only:
    - master
```

### 修改cicd产出日志的限制

```
需要修改docker的toml配置

```



### Github cicd 部署

```
https://docs.github.com/cn/actions/hosting-your-own-runners/adding-self-hosted-runners

配置说明：https://cloud.tencent.com/developer/article/1614404


所用到的action插件

    actions/checkout@v2 ：拉代码
    actions/cache@v1：缓存
    actions/upload-artifact@v1：打包上传构件
    actions/download-artifact@v1：下载构件
    easingthemes/ssh-deploy@v2.0.7：ssh-deploy部署插件
    contention/rsync-deployments@v1.0.0：rsync同步插件
    appleboy/ssh-action@master：ssh命令行插件

上传自定义的docker镜像
创建token：https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
token在action使用
https://docs.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#github-context
https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#env

在服务器上login token
export CR_PAT=YOUR_TOKEN
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

This example pushes the latest version of IMAGE-NAME.
$ docker push ghcr.io/OWNER/IMAGE_NAME:latest

This example pushes the 2.5 version of the image.
$ docker push ghcr.io/OWNER/IMAGE-NAME:2.5


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

### fatal: Cannot update paths and switch to branch 'feat/insert-sdk' at the same time.

```

```



### hint: Pulling without specifying how to reconcile divergent branches is

```
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint:
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
Already up to date.


git pull 会因为本地分支和远程分支有冲突自动生成一个commit
所以才会出现上面异常
可以先git fetch
然后git merge
```



















## end