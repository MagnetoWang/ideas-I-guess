## Go解决方案

### 资料

```
go中文网：https://books.studygolang.com/The-Golang-Standard-Library-by-Example/chapter01/01.2.html
官网：https://golang.google.cn/
国内镜像源：https://goproxy.cn/
```

### 语法

#### rune

```
按照utf8的一个字节为单位，无论英文还是汉字。
```

#### defer
```
https://www.cnblogs.com/ysherlock/p/8150726.html
延迟函数 延迟直到函数return的时候，会被调用。尤其是文件close的时候常用
```

#### chan

```
http://c.biancheng.net/view/97.html
管道，起到不同goroutine的通信作用
```

#### struct

```

```

#### interface

```

```



### 相关库

#### io

```
func ReadFile(filename string) ([]byte, error)

```

#### unicode

#### strings

```
FieldsFunc 用这样的 Unicode 代码点 c 进行分隔：满足 f(c) 返回 true。该函数返回[]string。如果字符串 s 中所有的代码点 (unicode code points) 都满足 f(c) 或者 s 是空，则 FieldsFunc 返回空 slice。

也就是说，我们可以通过实现一个回调函数来指定分隔字符串 s 的字符。比如上面的例子，我们通过 FieldsFunc 来实现：

fmt.Println(strings.FieldsFunc("  foo bar  baz   ", unicode.IsSpace))

```

#### sync

```
sync.Once
https://zhuanlan.zhihu.com/p/44360489
sync.Once 是 Golang package 中使方法只执行一次的对象实现，作用与 init 函数类似。但也有所不同。

    init 函数是在文件包首次被加载的时候执行，且只执行一次sync.Onc 是在代码运行中需要的时候执行，且只执行一次

当一个函数不希望程序在一开始的时候就被执行的时候，我们可以使用 sync.Once 。

```

