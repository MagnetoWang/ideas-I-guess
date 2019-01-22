## Markdown解决方案

- 为了更高效利用markdown的特性，提高文章阅读速度和定位想要的内容位置
- 增加书写效率，提高观赏度，规范化写作

[TOC]

## 资料

- Typora 使用手册：https://baka943.coding.me/2018/02/08/2018-02-08-TyporaSimpleDoc/#%E5%9F%BA%E6%9C%AC%E7%9A%84%E4%B8%8D%E5%B8%A6%E5%BF%AB%E6%8D%B7%E9%94%AE%20Markdown%20%E4%B9%A6%E5%86%99%E6%BC%94%E7%A4%BA
- markdown 官方语法：https://guo365.github.io/study/Markdown.html

## 添加目录树

- [TOC]独占一行才行

## 文档内跳转，添加锚点

- 详细介绍锚点使用：https://my.oschina.net/antsky/blog/1475173
- 先定义锚点
- [随便什么名字](#资料)
- 然后定义标题，h1到h6之间的等级。typore这个功能似乎无效，只能在github上面体现这个功能
- 括号里面的名字要和标题对应就行了，尽量不要参杂多余的符号



## 安装 GitBook

- 比 typora好一万倍的 md to pdf 的软件
- 官方教程：https://toolchain.gitbook.com/ebook.html
- 安装npm教程：https://www.jianshu.com/p/9f24f8e27fc6
- 安装gitbook convert：https://blog.csdn.net/sinat_25295611/article/details/78973827
- brew install npm
- sudo npm install -g gitbook-cli
- npm install ebook-convert -g
- 下载转换器：https://calibre-ebook.com/download_osx
- 把
- sudo ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/bin