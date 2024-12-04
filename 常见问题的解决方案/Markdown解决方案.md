## Markdown解决方案

- 为了更高效利用markdown的特性，提高文章阅读速度和定位想要的内容位置
- 增加书写效率，提高观赏度，规范化写作

[TOC]

## 资料

- Typora 使用手册：https://baka943.coding.me/2018/02/08/2018-02-08-TyporaSimpleDoc/#%E5%9F%BA%E6%9C%AC%E7%9A%84%E4%B8%8D%E5%B8%A6%E5%BF%AB%E6%8D%B7%E9%94%AE%20Markdown%20%E4%B9%A6%E5%86%99%E6%BC%94%E7%A4%BA
- markdown 官方语法：https://guo365.github.io/study/Markdown.html

## 导出pdf
1. obsidian 和 notion 可以将markdown导出pdf

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

## 图床解决方案
1. 路径配置：https://blog.csdn.net/LT_admin/article/details/135136872
2. 重命名：https://juejin.cn/post/7244809769794289721

## 画图工具

- 思维导图：https://blog.csdn.net/wangyaninglm/article/details/52887045
- 流程图：https://blog.csdn.net/aizhaoyu/article/details/44350821

### flow语法

### type

- start 
  end 
  operation 
  subroutine 
  condition 
  inputoutput

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```





st=>start: Get
check1=>operation: check Key
check2=>operation: check TS
check3=>operation: check Value
cond1=>condition: Have it or not?
cond2=>condition: Have it or not?
cond3=>condition: Have it or not?
none=>operation: return none
value=>operation: return value
e=>end: End
st->chek1->cond1
cond1(yes)->check2->cond2
cond2(yes)->check3->cond3
cond3(yes)->value->e
cond1(no)->none->e
cond2(no)->none->e
cond3(no)->none->e



## 数学公式
1. 公式语法：https://www.cnblogs.com/bytesfly/p/markdown-formula.html
2. 需要 $公式语法$ 框起来
3. [转]Markdown数学符号 - 李睿的文章 - 知乎 https://zhuanlan.zhihu.com/p/2293107002
4. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
5. https://www.mathjax.org/
6. latex语法：https://qyxf.github.io/2020/01/03/latex-formula-beginner
   1. 粗体（bold font shape），可以用 \mathbf 命令
   2. 镂空粗体（blackboard bold）字符，应使用 \mathbb 命令
   3. 花体（calligraphical） \mathcal 与文本体（script） \mathscr
   4. 一对命令 \Bigl 与 \Bigr 吸附在左右括号之前，调整了其大小

$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

$\rightarrow$

$\leftarrow$

$\sqrt{3x-1}+(1+x)^2$


$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

$f(x) = \Bigl( \frac{a^x}{b} \Bigr)$

$f(x) = \left( \frac{a^x}{b} \right)$


矩阵
- 自带圆括号 ()的 pmatrix 环境；
- 自带方括号 []的 bmatrix 环境；
- 自带花括号 {}的 Bmatrix 环境；
- 自带绝对值界的 vmatrix 环境与自带范数界的 Vmatrix 
$\begin{matrix}
a & b & c\\
d & e & f
\end{matrix}$


```math
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
```

$0.98^{365} \approx 0.0006$