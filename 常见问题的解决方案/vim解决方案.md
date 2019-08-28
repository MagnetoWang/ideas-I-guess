## vim解决方案

- 快速进入vim的编辑环境，让vim的编辑无感于vscode
- 全身心投入代码的编辑，而不是一系列繁琐的配置中
- 因为历史原因学习vim，而不是因为好用才学习vim

[TOC]

## 资料

- https://blog.csdn.net/chuanj1985/article/details/6873830
- 基本配置：<http://c.biancheng.net/view/3024.html>
- 高级配置：<https://www.jianshu.com/p/a0b452f8f720>
- 目录树：<https://blog.csdn.net/lyhdream/article/details/22490531>
- 状态栏：<https://blog.csdn.net/XIAOZHOUWNX/article/details/8274988>
- 语法高亮：<https://www.cnblogs.com/Lucky-qin2013/p/6171090.html>
- 打造IDE：<http://yuez.me/jiang-ni-de-vim-da-zao-cheng-qing-qiao-qiang-da-de-ide/>

## 全局配置

- 直接修改vim的文件
- vim ~/.vimrc

## 设置行号

- :set number



## 复制文件内容

- 常规是vim打开
- 但是里面包含行号，很麻烦
- 网络上用 ggVG+y的命令来复制，但是始终没办法复制到windows系统上，只能在命令行端
- gg 是到行首
- G 是到行尾
- V 是可视化操作
- +y是复制到系统粘贴板
- 比较好的方法是用cat 打开文件，然后复制



## 删除一行

- dd

## 查找单词

```
斜杆即可
:/ words
```

## 撤回

```
:u
```

## 跳到指定行

```
:n
n可以是任意数字
```

## 目录树

```
设置f5启动

通过hjkl来移动光标
o打开关闭文件或目录，如果想打开文件，必须光标移动到文件名
t在标签页中打开
s和i可以水平或纵向分割窗口打开文件
p到上层目录
P到根目录
K到同目录第一个节点
P到同目录最后一个节点
```



## 状态栏语法

- <https://blog.csdn.net/icbm/article/details/73028623>

```
" 显示状态行当前设置
set statusline

" 设置状态行显示常用信息
" %F 完整文件路径名
" %m 当前缓冲被修改标记
" %m 当前缓冲只读标记
" %h 帮助缓冲标记
" %w 预览缓冲标记
" %Y 文件类型
" %b ASCII值
" %B 十六进制值
" %l 行数
" %v 列数
" %p 当前行数占总行数的的百分比
" %L 总行数
" %{...} 评估表达式的值，并用值代替
" %{"[fenc=".(&fenc==""?&enc:&fenc).((exists("+bomb") && &bomb)?"+":"")."]"} 显示文件编码
" %{&ff} 显示文件类型
set statusline=%F%m%r%h%w%=\ [ft=%Y]\ %{\"[fenc=\".(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\"+\":\"\").\"]\"}\ [ff=%{&ff}]\ [asc=%03.3b]\ [hex=%02.2B]\ [pos=%04l,%04v][%p%%]\ [len=%L]

" 设置 laststatus = 0 ，不显式状态行
" 设置 laststatus = 1 ，仅当窗口多于一个时，显示状态行
" 设置 laststatus = 2 ，总是显式状态行
set laststatus=2
 ———————————————— 
版权声明：本文为CSDN博主「icbm」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/icbm/article/details/73028623
```





| 设置参数                                                     | 功能描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936 set termencoding=utf-8 set encoding=utf-8 | 设置编码格式，encoding 选项用于缓存的文本、寄存器、Vim 脚本文件等；fileencoding 选项是 Vim 写入文件时采用的编码类型；termencoding 选项表示输出到终端时采用的编码类型。 |
| set nu set number                                            | nu 是 number 的缩写，所以上面两个配置命令是完全等效的，二选一即可。取消行号可使用 set nonu。 |
| set cursorline                                               | 突出显示当前行。                                             |
| set mouse=a set selection=exclusive set selectmode=mouse,key | Vim 编辑器里默认是不启用鼠标的，通过此设置即可启动鼠标。     |
| set autoindent                                               | 设置自动缩进，即每行的缩进同上一节相同。                     |
| set tabstop=4                                                | 设置 Tab 键宽度为 4 个空格。                                 |

## 基本配置说明

```
"标尺功能，显示当前光标所在行列号
set ruler

"粘贴时保持格式
set paste
 
"高亮显示匹配的括号
set showmatch
 
"在搜索的时候忽略大小写
set ignorecase

"高亮被搜索的句子
set hlsearch
 
"在搜索时，输入的词句的逐字符高亮（类似firefox的搜索）
set incsearch

"继承前一行的缩进方式，特别适用于多行注释
set autoindent


"历史命令保存行数
set history=100
 
"当文件被外部改变时自动读取
set autoread
 
"取消自动备份及产生swp文件
set nobackup
set nowb
set noswapfile
 
"允许使用鼠标点击定位
set mouse=a

"与windows共享剪贴板
set clipboard+=unnamed

"打开语法高亮
syntax on
 
"使用配色方案
colorscheme desert
 
"打开文件类型检测功能
filetype on
 
"不同文件类型采用不同缩进
filetype indent on
 
"允许使用插件
filetype plugin on
filetype plugin indent on
```



## 安装配置

```
https://www.jianshu.com/p/a0b452f8f720

装插件的管理器，直接输入下面命令即可
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

在这个colors目录下，可以下载任意vim配色主题，在vimrc上修改名字即可
mkdir ~/.vim/colors

安装gruvbox主题
mkdir -p ~/.vim/colors 
git clone --depth 1 https://github.com/morhetz/gruvbox.git ~/.vim/bundle/gruvbox
cp ~/.vim/bundle/gruvbox/colors/gruvbox.vim ~/.vim/colors/gruvbox.vim
然后在.vimrc上添加即可
colorscheme gruvbox
set background=dark




装目录树
git clone https://github.com/scrooloose/nerdtree.git ~/.vim/bundle/nerdtree
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe

状态栏
set laststatus=2 “长久显示：1
set statusline=%t\ %y\ format:\ %{&ff};\ [%c,%l]
```



## 高级配置

```
更好的插件管理
git clone https://github.com/ludovicchabant/vim-gutentags.git ~/.vim/bundle/vim-gutentags
```

