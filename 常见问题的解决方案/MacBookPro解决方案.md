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

## 文件夹直通车

- 



## 终端

- 安装iterm
- 安装ohmyzsh：https://segmentfault.com/a/1190000014992947
  - sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
  - https://segmentfault.com/a/1190000014992947