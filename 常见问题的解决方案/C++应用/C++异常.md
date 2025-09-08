
## 常见问题

### executable is not specified

- clion 编译运行的时候出现
- 参考链接：https://stackoverflow.com/questions/30086210/when-compiling-in-clion-i-get-the-error-executable-is-not-specified
- 解决方案
  - 一个cpp项目需要用cmakelist.txt
  - 所以应该添加cmakelist.txt,并执行，才能运行整个项目

###  no matching member function for call to 'insert'

- 迭代map中的元素无法用insert
- 可以把这个问题普遍化，如果遇到无法调用的函数的情况有什么原因呢
  - 1，确实没有这个函数
  - 2，函数里面的参数使用错误，导致无法找到配对形式参数的函数
- 解决方案
  - map查文档，有insert函数
  - 但是没有对应的参数，可以insert，key和value
  - 只有经过make_pari()封装后作为的insert的函数
  - 后修改，问题解决！

### ld returned 1 exit status 

- https://stackoverflow.com/questions/27272525/what-does-collect2-error-ld-returned-1-exit-status-mean
- ld 这个工具 返回了一个错误

### a space is required between consecutive right angle brackets (use '> >')
```
语法问题
请注意，这个问题只会在某些编译器和特定的编译选项下出现，因为 C++ 标准规定连续的右尖括号 >> 可能会被解释为右移运算符。为了避免这种歧义，我们需要在模板参数之间添加一个空格。
    std::unordered_map<int, std::pair<int, std::list<int>::iterator>> cache;
    改成
        std::unordered_map<int, std::pair<int, std::list<int>::iterator> > cache;

run.cpp:8:68: error: a space is required between consecutive right angle brackets (use '> >')
    std::unordered_map<int, std::pair<int, std::list<int>::iterator>> cache;

  
                                   

```

###
```
这个编译错误是因为在 C++11 标准之前，不支持使用花括号 {} 进行直接初始化。为了解决这个问题，你可以使用传统的构造函数语法来初始化 cache[key] 的值。修改后的代码如下：

run.cpp:46:26: error: expected expression
            cache[key] = {value, lruList.begin()};
                         ^
1 error generated.


```
