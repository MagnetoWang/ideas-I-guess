## VSCode解决方案

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

