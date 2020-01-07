## VSCode解决方案

### 使用入门

```
视频入门更快：https://www.bilibili.com/video/av32808486?from=search&seid=11649437142912112135 

命令行中启动vscode
在vscode设置里面，启动命令，输入shell，出现安装code
这样只需要命令行输入 code . 就可以启动vscode

创建项目独立的环境
python -m venv env
or
python3 -m venv env

保存安装包列表
pip freeze > requirements.txt

查询文件的结构
command + p
```



### 颜色配置

- 更改json配置，找到对应中文名：https://www.cnblogs.com/garvenc/p/vscode_customize_color_theme.html

### 插件安装

- https://zhuanlan.zhihu.com/p/40417719

### 代码自动分行

- 因为分屏太多，希望代码可以自动分行，减少左右移动次数
- 快捷键
- alt + z

### 自动添加头文件信息

- 插件：fileheader
- 输入命令fileheader即可

### c++自动补全

- 参考资料：<https://blog.csdn.net/cbc000/article/details/80670413>
- 添加插件

```
/.vscode/c_cpp_properties.json
在includePath
添加你的库头文件地址也可以增强补全功能
```



### 快捷键总结

- 参考资料：https://www.jianshu.com/p/feff1c7e9989

```
ctrl + shift + n
新建vscode窗口，由于vscode不能向sublime一样的拖拽标签生成新窗口
ctrl + x
剪切文本。但当未选中文本时，该命令会剪切光标所在整行，当然连续ctrl + x用于删除行也是不错的选择
ctrl + c
复制文本。但当未选中文本时，该命令会复制光标所在整行，（想想曾自以为聪明的按下ctrl + i选中当前整行在执行剪切或者复制的我。。。）
alt + ↑/↓
上下移动光标所在行，简单实用
shift + alt + ↑/↓
复制光标所在行（其实这里的上下箭头效果一样，原因自己理解）
ctrl + shift + k
删除光标所在行，类似ctrl + x（未选中内容）
ctrl + enter
光标所在行下方插入新行，直接跳到下一行，不会影响当前行内容
ctrl + shift + enter 向上跳，描述基本同上
ctrl + shift + \ 在匹配的闭合标签来回跳跃，So 如果代码片段太长，不要用仔细找闭合标签了，虽然我知道你有闭合标签高亮插件，依然是费眼，费精力
ctrl + [/] 向左/右缩进代码
ctrl + shift + [/] 折叠/展开光标所在代码块区域（如果该区域可以折叠），不用费尽心机的去找行首的小加号了
shift + alt + a 创建块状注释，超级实用，比行注释（ctrl + /）更加实用
alt + z
开关代码超出编辑器宽度折叠
ctrl + 123
打开123个并排编辑标签
alt + 123
在第一个切换到第123个编辑标签
ctrl + shift + o
跳到标签锚点，锚点可以是tags id class,伴随区域高亮，爽歪歪。
alt + ←/→
跳到上一次/下一次光标曾经停留过的地方
ctrl + shift + f
当前工程（也就是当前打开的文件夹）所有文件全局搜索相当于文件爬虫
alt + enter
选中所有搜索出来的高亮结果
shift + alt + i
在所有选中行后边插入光标
ctrl + backspace
按最小区块向前删除内容（好的其它编辑器都有的功能）
ctrl + delete
按最小区块向后删除内容（好的其它编辑器都有的功能）
ctrl + ←/→
按最小区块←/→跳跃光标，常常配合上边的插入光标使用
shift + alt +
鼠标左键拖动 鼠标可以垂直选择行，或者块状选择行，建议在结构相似的行之间操作
ctrl + shift + alt + ↑/↓/←/→
和上边一样的功能，鼠标改键盘操作了
```

### 显示空格

```
https://blog.csdn.net/bmzk123/article/details/86501706
renderControlCharacters
renderWhitespace
```

### 空格高亮

```
Rainbow 插件
```

### 注释管理

```
koroFileHeader

```

### remote-ssh消耗大量性能问题

```
原因是私钥和公钥
我在本地生成的私钥和公钥，传给服务器私钥，结果性能大量消耗

但是如果是服务器生成的私钥和公钥，传给本地公钥。这个问题就被解决了

https://code.visualstudio.com/docs/cpp/faq-cpp
后面仍然出现性能问题
所以原因不是key，仔细看c++自动补全的插件文档，分析是不是把当前目录下无论什么文件只要是c++就全部索引进去
于是将目录改成只有src中，而不是整个大项目。发现消耗明显下降
所以最终原因是索引的文件太多了，把第三方库全部加载进去
第三方库只需要在配置中添加incluede路径即可
插件还可以配置需要索引的目录，叫brower.path
```

