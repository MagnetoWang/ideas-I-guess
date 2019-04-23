## 图片

## Mac使用中的问题

[TOC]



## 说明

- 因为公司发了一台mac，所以中间使用遇到不少问题，因此记录下来



## 常见问题

- 右键的点击：两只手指轻点触摸板】
- 创建文件：不能直接直接，只能通过相关应用程序创建专门的文件
- cpu和内存占用率：活动监视器



## mac文件路径

-  mac似乎没有特别清晰的路径，让新手一开始很难弄清楚文件的存放，和根目录的情况
-  Pwd：打印当前目录
-  文件详解：https://www.jianshu.com/p/f5b2c506dd67



## mac命令行

- 安装brew：
  - brew是专门安装系统软件的方便工具
  - https://brew.sh/：/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  - brew help：查看相关命令
  - brew install wget
- 安装XCode

  - xcode-select --install 
- 启动shadowsocks服务

  - /usr/local/opt/shadowsocks-libev/bin/ss-local -c /usr/local/etc/shadowsocks-libev.json -u
- 安装python3

  - brew install python3
  - pip安装：curl <https://bootstrap.pypa.io/get-pip.py> | python3
  - pip list
  - pip -version
- 文件跳转

  - " / "  ：根目录
  - " ~ " ：用户主目录的缩写。例如当前用户为hello，那么" ~ "展开来就是：/Users/hello
  - " . "  ：当前目录
  - ".."   ：父目录
  - clear 清空当前输入
  - history 查看输入历史记录
  - 切换英文目录：cd Library/AAA\ English\ Path/
  - ls -a：显示所有文件包括隐藏文件
  - rm -rf 文件/文件夹名字：直接删除不做任何提示。慎用服务器中
- Finder软件操作
  - defaults write com.apple.finder _FXShowPosixPathInTitle -bool TRUE;killall Finder：显示当前路径在显示栏目上面
  - defaults delete com.apple.finder _FXShowPosixPathInTitle;killall Finder：只显示文件名，不显示路径
  - Option+Cmd+P：可以快速切换路径，底部显示路径栏
- 文本操作
  - open -t settings.xml ：默认编辑本打开
  - open -e settings.xml ：文本编辑本打开
  - open -a vscode settings.xml ：指定应用打开
  - https://blog.csdn.net/example440982/article/details/80220270
  - code settings.xml：用vscode打开文本

## mac常用功能

### 查找文件

- find 文件路径 参数
- find Documents/ -iname  工程设计

### 查看mac内部有多少字体

- 直接复制执行下面的命令
- fc-list :lang=zh file family style

## 安装软件

### 安装md5sum

- brew install md5sha1sum
- 参考资料：https://raamdev.com/2008/howto-install-md5sum-sha1sum-on-mac-os-x/

### 安装tree

- brew install tree
- 参考资料：http://macappstore.org/tree/

## 文件夹直通车

- 

## pandoc使用过程

### 资料

- https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/
- 中文字体：https://blog.csdn.net/penghouwen/article/details/50491177
- pdf模版设置：https://www.jianshu.com/p/7f9a9ff053bb

### 字体找不到

- 是因为名字错误，要找mac内置中文字体
- fc-list :lang=zh
- https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/#%E4%BD%BF%E7%94%A8-pandoc-%E4%BB%8E-markdown-%E7%94%9F%E6%88%90-pdf-%E6%96%87%E4%BB%B6

### fontspec error: "font-not-found"

- 找英文字体

###  LaTeX Error: Option clash for package fontspec.

- https://blog.csdn.net/Dylan_Frank/article/details/71713285
- 滚蛋pandac。浪费我时间的垃圾软件

### 无法找到pdflatex

- 可以考虑重新开个终端运行

### Fatal format file error; I'm stymied

- 未解决
- 重新安装
- 也没有解决
- 换方法
- 用python md2pdf

### 滚蛋pandac。浪费我时间的垃圾软件

## 常见问题

### mac Operation not permitted 权限问题

- 开启权限：http://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/
- 重启电脑，进入恢复模式
- 然后关闭
- 再重启
- https://stackoverflow.com/questions/32659348/operation-not-permitted-when-on-root-el-capitan-rootless-disabled
- csrutil disable
- reboot
- 即可

### 取消brew安装软件时候自动更新的问题

- 打开 ~/.bashrc
- 添加
- export HOMEBREW_NO_AUTO_UPDATE=true 

### 两个python版本切换

- https://blog.csdn.net/qq_38789531/article/details/82431933

- 修改两个文件

- vi ~/.bash_profile

- PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"
  export PATH

  PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
  export PATH	

- vi ~/.bashrc

  - alias python2='/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7'
    alias python3='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6'
    alias python=python2

- source ~/.bash_profile

- source ~/.bashrc

- python -V

### ValueError: unknown locale: UTF-8 in Python

- ```
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  ```

### 安装gnu-getopt的问题

- 参考资料：http://macappstore.org/gnu-getopt/
- ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
- brew install gnu-getopt
- echo 'export PATH="/usr/local/opt/gnu-getopt/bin:$PATH"' >> ~/.bashrc
- source ~/.bashrc
- path路径一定要写进bashrc才能生效！！！

### 打开ppt的时候总是会弹出以前的自动保存的ppt内容

- 参考资料：<https://answers.microsoft.com/zh-hans/msoffice/forum/msoffice_powerpoint-mso_mac-mso_mac2016/%E6%AF%8F%E6%AC%A1%E5%90%AF%E5%8A%A8ppt%E6%97%B6/24aa4a9a-013a-49de-8ffe-455fbe5f38b2>
- 进入目录 ~/Library/Containers/com.microsoft.Powerpoint/Data/Library/Preferences/AutoRecover
- 删除里面的文件，就可以了

## 终端

- 安装iterm
- 安装ohmyzsh：https://segmentfault.com/a/1190000014992947
  - sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
  - https://segmentfault.com/a/1190000014992947

[TOC]

