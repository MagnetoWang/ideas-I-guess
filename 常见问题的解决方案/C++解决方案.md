

## 说明

- c+不同于Java，有非常多的细节需要专门注意，所以需要特意写个方案解决平时遇到的问题

## 目录

[TOC]

## 资源

- https://github.com/fffaraz/awesome-cpp
- cpp大神博客：http://huqunxing.site/
- 非常棒的笔记：http://www.fredosaurus.com/notes-cpp/index.html



## C++解决方案

### 规范

- 成员变量：全部小写+下划线分开+尾巴后面加下划线
  - table_meta_
- 普通变量：全部小写+下划线分开
  - table_meta
- 函数名称：单词首字母大写-双驼峰
  - DropTable
- 文件名字：全部小写，下划线分开单词
  - name_server_impl
- 类名：首字母大写
  - NameServerImpl
- 域名：namespace 全部小写，不超过三个单词
  - namespace，protobuf

### 代码优化-实战获得经验

- 要用的时候再定义变量，不要提前定义好所有的变量
- 借鉴别人的代码的时候不要直接copy，可以先写下所有的函数名字，然后自己一个个的实现，最后做个比较，看看有没有可以优化的地方

### 快速写代码

#### 定义类

- 确定类名
- 所有变量放private
- 用列表初始化写构造函数 
- 必要的情况：const 修饰函数 和 返回值
- 遵循用的时候才定义类的原则
  - private定义的变量一般放在public后面
  - 偶尔public需要变量，就可以定义到private后面

#### 模板的编写

- 基本介绍：http://www.cnblogs.com/gaojun/archive/2010/09/10/1823354.html
- 模板详细介绍：https://www.cnblogs.com/wxquare/p/4743180.html
- 模板形参介绍：http://www.cnblogs.com/gw811/archive/2012/10/25/2738929.html

```
Template <class或者也可以用typename T>
返回类型 函数名（形参表）
{//函数定义体 }

在正常的函数前面加一行 template即可
<> 里面是模板形式参数，这里面可以有多个class，这函数体里面可以选择调用形参里面的T
```



### 与Java不同之处，更多是一种习惯的不同

- 定义std::map 不用new。可以直接使用
  - 适应所有STL中容器
- 函数返回参数，不能是指针和引用，必须是实体对象！！
  - Java似乎用某种方式实现返回对象的指针或者引用



### 指针

- 强弱应用：https://www.jianshu.com/p/4b047fc3b0be

- 多个***，代表什么意思：https://blog.csdn.net/soonfly/article/details/51131141

- 图解多级指针：https://www.cnblogs.com/chenyangyao/p/5222696.html

- 结构体指针：http://c.biancheng.net/cpp/html/94.html

- 类对象指针：https://www.cnblogs.com/flylong0204/p/4731318.html

- make_shared & shared_ptr：https://www.jianshu.com/p/4b047fc3b0be



### 语法问题

- FileReceiver(const FileReceiver&) = delete;
- std::basic_string<char> 和 std::string区别
  - https://stackoverflow.com/questions/1662107/whats-the-difference-between-stdstring-and-stdbasic-string-and-why-are-bot

- 类型转换问题

```
error: no matching function for call to 'std::vector<std::basic_string<char> >::insert(std::string&)'
                 endpoints.insert(endpoint);
       
       
将insert改成push_back就ok了
```

- map无法insert

```
std::map<std::pair<uint32_t,uint32_t>, std::vector<std::string>> pos_endpoints;

这种复杂类型，无法insert。我查了7个小时终于找到了

多套一重make_pair
pos_endpoints.insert(std::make_pair(std::make_pair(idx, kv.second->table_partition(idx).pid()), endpoints));
```

### Iterator使用

- 解决一些常规函数的重复编写
- iterators give us indirect access to an object.
- In the case of an iterator, that object is an element in a container or a character in a string. We can use an iterator to fetch an element and iterators have operations to move from one element to another. As with pointers, an iterator may be valid or invalid. A valid iterator either denotes an element or denotes a position one past the last element in a container. All other iterator values are invalid.
- note
  - If the container is empty, the iterators returned by begin and end are equal —they are both off-the-end iterators.
- 文档：http://www.cplusplus.com/reference/iterator/
- 用法
  - s.begin() != s.end() 确保迭代器不为空
  - s++ 表示移动迭代器到下一位
  - != 来判断相关条件，是因为要表示使用的是迭代器而不是下标
  - vector\<int\> ::iterator   类对象::迭代器
  - vector\<int\> ::const_iterator. 只能读不能写
  - 解除迭代器和对象的引用
    - ( * iit).empty()
    - It -> empty()
- 算术操作
  - 类似加减可以当作下标直接操作
- 难点
  -  friend iterator; // Make it a friend 
  -  friend class iterator
  -  https://stackoverflow.com/questions/6195954/what-is-the-difference-of-friend-iterator-and-friend-class-iterator-which-encoun/6196028



### Class的正确使用

-  classes are data abstraction and encapsulation. 
   -  Data abstraction is a programming (and design) technique that relies on the separation of interface and implementation. The interface of a class consists of the operations that users of the class can execute. The implementation includes the class’ data members, the bodies of the functions that constitute the interface, and any functions needed to define the class that are not intended for general use.
   -  Encapsulation enforces the separation of a class’ interface and implementation. A class that is encapsulated hides its implementation—users of the class can use the interface but have no access to the implementation.
-  The only difference between using class and using struct to define a class is the default access level.

#### 用法

- 局部类和嵌套类
  - https://www.jianshu.com/p/2e4de807526e
  - 局部类是在函数中，临时定义的类，作用域有限
  - 嵌套类是在类中又定义的类，相当于复合结构的类。为了扩展类的数据类型丰富度。一般类内部自己使用不对外
  - https://zh.cppreference.com/w/cpp/language/nested_types
  - 局部类不常用
  - 嵌套类常用，两个独立的类，更多的是作用域的考量
  - 为了更好的使用，外部类在使用嵌套类的时候，最好声明，然后再使用



### Map使用

- 在多重map中，需要用make_pair进行封装，然后在插入数据
  - 比如key也是map,value也是map
  - 那么key 也要make_pair， value也要make_pair
- Map.find（key)。返回的是迭代器
- 在迭代器的基础上，iter->second。就可以返回value
- 一般返回迭代器都会判断一下，是否为end情况
- key中的类对象，必须实现比较函数，不然编译错误
- 不要用指针当key！！！
- 参考文档：http://www.cplusplus.com/reference/map/map/
- 插入数据
  - map.insert(std::make_pair(key, value));
- 更新数据
  - map[key] = value
- 删除数据
  - erase
  - map.erase(key)
- 查找数据
  - find
  - map.find(key)
  - 返回的是迭代器
- 迭代
  - const auto& iter: table_info_

### unordered_map使用

- 哈希map，查找速度更快，常数级别
- 显然，hash算法不能兼容有序的特点
- 类似Java中的HashMap
- 参考文档：
  - http://www.cplusplus.com/reference/unordered_map/
  - https://en.cppreference.com/w/cpp/container/unordered_map
- 基本操作
- 和map基本一致

### vector使用

- 参考文档：http://www.cplusplus.com/reference/vector/vector/
- 常用函数
- reserve

### string使用

- 参考文档
  - http://www.cplusplus.com/reference/string/string/
  - https://en.cppreference.com/w/cpp/string/basic_string
- 转换字符串
  - std::to_string
  - https://en.cppreference.com/w/cpp/string/basic_string/to_string
- 字符串转c字符串
  - 成员函数：xxxstring.c_str
- 字符串拼接

  - 可以直接用加号连接
- 字符串比较

  - a.compare(b)

  - = 0 

  - < 0 就是 a < b

  - \>  0 就是 a > b

| value | relation between *compared string* and *comparing string*    |
| ----- | ------------------------------------------------------------ |
| `0`   | They compare equal                                           |
| `<0`  | Either the value of the first character that does not match is lower in the *compared string*, or all compared characters match but the *compared string* is shorter. |
| `>0`  | Either the value of the first character that does not match is greater in the *compared string*, or all compared characters match but the *compared string* is longer. |

### char* 使用

- 拷贝函数
  - memcpy(void *dest, const void *src, size_t n) 
  - 从源src所指的内存地址的起始位置开始拷贝n个字节到目标dest所指的内存地址的起始位置中
  - source和destin都不一定是数组，任意的可读写的空间均可
- char* test = new char[size];



### set使用

- 参考文档
  - http://www.cplusplus.com/reference/set/set/
- 头文件 #include < set >

### typename使用

- 参考资料：https://www.cnblogs.com/wuchanming/p/3765345.html
- 第一种用法
  - 放在模板里面，修饰模板的形式参数
- 第二种用法
  - 消除* 的歧义
  - 有时候需要返回模板类的迭代器，实质返回指针
  - 但是编译器可能无法识别这是个指针
  - 这个时候需要在前面加typename
- 如下例子

```
   template <typename T> class Y
   {
       typename T::iterator *iter;
       typedef typename T::iterator iterator; //定义了Y::iterator类型名称
       ...
   };
```



### typedef用法

- typedef unsigned int uint32_t;
- 只是定义一个新的好记的名字！

### const用法

- 所有用法集合：http://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777416.html

- 常变量：  **const 类型说明符 变量名**

    常引用：  **const 类型说明符 &引用名**

    常对象：  **类名 const 对象名**

    常成员函数：  **类名::fun(形参) const**

    常数组：  **类型说明符 const 数组名[大小]**    

    常指针：  **const 类型说明符\* 指针名 ，类型说明符* const 指针名**

- const的口诀

    - 左内右本：https://www.cnblogs.com/liushui-sky/p/9668413.html
    - const 出现在* 左边，说明是该指针的内容不允许修改
    - const 出现在* 右边，说明是该指针本身不允许修改

- 常量指针

  - const int *pi = &i;
  - *pi = 100; 错
  - 不能通过常量指针修改指针里面的内容
  - const int *p=&a //常量指针
  - *p=9;//操作错误
  - p=&b;//操作成功
  - 和指针常量的区别：https://blog.csdn.net/weibo_dm/article/details/80445205

- 指针常量

  -  int* const m2 = new int(20);
  - int * const p=&a //指针常量
  - *p=9;//操作成功
  - p=&b;//操作错误

- 函数后面加个const

  - 该函数不能修改数据成员

- 函数前面加const

  - 返回的对象不能被外部修改

- 类对象前面加const

  - 不能引用非const的成员函数
  - 参考链接：http://www.cnblogs.com/xing901022/p/3413019.html

- const对象只能调用const函数

    - 解释：https://www.cnblogs.com/cplinux/articles/5553716.html

### 函数中的参数

- 默认参数和缺省参数：https://blog.csdn.net/CHF_VIP/article/details/8586921
- 初始化的参数，可以可以赋值也可以不赋值
- 参数一般都是默认传值。传值的意思就是，传递参数会复制一个新对象到函数内部。尤其传递一个对象时，会显得十分耗时。而且是函数内部的修改该值的时候，是不会影响实际参数的值。
- 最好的方式是使用传引用，然后选择性的是否修改里面的值。
- 传引用的就是传地址的值！而不是对象内部数据的值！
- 传对象的值到函数里面，会发生构造一次对象，析构一次对象消耗。而且这是没有考虑到对象中可能还含有其他对象的情况，那么消耗将会更加多。

### 函数中的参数传递

#### 指针传递

```
Handle* wh;
// 使用函数
function(&wh)


// 定义函数
function(Handle** wh) {
    xxxxx
}
```

#### 引用传递

```

```

#### 传递的区别

### File使用

- 参考资料
  - http://www.cplusplus.com/reference/cstdio/FILE/
  - https://blog.csdn.net/jiahehao/article/details/1862867
- 打开和关闭文件

```
/* FEOF example */
#include <stdio.h>

int main()
{
   FILE * pFile;
   char buffer [100];

   pFile = fopen ("myfile.txt" , "r");
   if (pFile == NULL) perror ("Error opening file");
   else
   {
     while ( ! feof (pFile) )
     {
       if ( fgets (buffer , 100 , pFile) == NULL ) break;
       fputs (buffer , stdout);
     }
     fclose (pFile);
   }
   return 0;
}
Edit & Run

```




#### fwrite函数

- 文档：http://www.cplusplus.com/reference/cstdio/fwrite/
- size_t fwrite ( const void * ptr, size_t size, size_t count, FILE * stream );
- Write block of data to stream
- ptr 数组内容
- stream 输出的文件
- size 每个元素的大小
- count 写入多少个元素

#### fflush函数

- 文档：http://www.cplusplus.com/reference/cstdio/fflush/
- int fflush ( FILE * stream );
- If the given *stream* was open for writing (or if it was open for updating and the last i/o operation was an output operation) any unwritten data in its output buffer is written to the file.
- return: A zero value indicates success.

#### sync、fsync与fdatasync区别

- https://blog.csdn.net/cywosp/article/details/8767327
- sync函数只是将所有修改过的块缓冲区排入写队列，然后就返回，它并不等待实际写磁盘操作结束。通常称为update的系统守护进程会周期性地（一般每隔30秒）调用sync函数。这就保证了定期冲洗内核的块缓冲区
- fsync函数只对由文件描述符filedes指定的单一文件起作用，并且等待写磁盘操作结束，然后返回。fsync可用于数据库这样的应用程序，这种应用程序需要确保将修改过的块立即写到磁盘上。
- fdatasync函数类似于fsync，但它只影响文件的数据部分。而除数据外，fsync还会同步更新文件的属性。
- fdatasync文档：https://linux.die.net/man/2/fdatasync

#### fileno()函数

- http://www.cppblog.com/jerryma/archive/2010/06/14/117888.html
- 把文件流指针转换成文件描述符
- int fileno(FILE *stream)

#### ftruncate()函数

- http://www.cppblog.com/jerryma/archive/2010/06/14/117888.html
- 改变文件大小
- int ftruncate(int fd, off_t  length)

#### lseek函数

- https://baike.baidu.com/item/lseek
- off_t lseek(int handle, off_t offset, int fromwhere);
- [当前文件](https://baike.baidu.com/item/%E5%BD%93%E5%89%8D%E6%96%87%E4%BB%B6)[偏移量](https://baike.baidu.com/item/%E5%81%8F%E7%A7%BB%E9%87%8F)（current file offset）cfo
- 


### memcmp函数使用

- memcmp(data_, x.data_, x.size_) == 0 data 与 x 比较 前 x个字符串

### memcpy函数使用

- memcpy(void *dest, const void *src, size_t n) 
- 从源src所指的内存地址的起始位置开始拷贝n个字节到目标dest所指的内存地址的起始位置中
- source和destin都不一定是数组，任意的可读写的空间均可

### snprintf函数

- http://www.cnblogs.com/armlinux/archive/2010/05/25/2397004.html
- int snprintf(char *restrict buf, size_t n, const char * restrict  format, ...);
- 最多从源串中拷贝n－1个字符到目标串中，然后再在后面加一个0。所以如果目标串的大小为n 的话，将不会溢出
- 函数返回值:若成功则返回欲写入的字符串长度，若出错则返回负值。

### sizeof使用

- char buffer[] = { 'x' , 'y' , 'z' };
  - sizeof(buffer) = 3
- int buffer[] = { 1,2,3};
  - sizeof(buffer) = 3 * 4 = 12
- 针对数组计算公式
  - sizeof = type * count
  - 元素单个大小 * 元素的数量
- const char* buffer = "abcdef";  或者 "abdc"
  - sizeof(buffer) = 8 
  - 只是buffer指针的大小

### Explicit 使用

- 关键字只能用于修饰只有一个参数的类构造函数, 它的作用是表明该构造函数是显示的, 而非隐式的, 跟它相对应的另一个关键字是implicit, 意思是隐藏的,类构造函数默认情况下即声明为implicit(隐式)
- google规范，只有一个参数的构造函数必须使用explicit修饰：https://www.cnblogs.com/ymy124/p/3632634.html
- ​    CxString string1(24);     // 这样是OK的  
- ​    CxString string2 = 10;    // 这样是不行的, 因为explicit关键字取消了隐式转换  
- ​    CxString string3;         // 这样是不行的, 因为没有默认构造函数  
- ​    CxString string4("aaaa"); // 这样是OK的  
- ​    CxString string5 = "bbb"; // 这样也是OK的, 调用的是CxString(const char *p)  
- ​    CxString string6 = 'c';   // 这样是不行的, 其实调用的是CxString(int size), 且size等于'c'的ascii码, 但explicit关键字取消了隐式转换  
- ​    string1 = 2;              // 这样也是不行的, 因为取消了隐式转换  
- ​    string2 = 3;              // 这样也是不行的, 因为取消了隐式转换  
- ​    string3 = string1;        // 这样也是不行的, 因为取消了隐式转换, 除非类实现操作符"="的重载  



### 线程

#### 线程池

- 简单实现：https://www.cnblogs.com/lzpong/p/6397997.html
- 介绍：https://zhuanlan.zhihu.com/p/26025722

#### 锁机制

- 锁相关函数：http://www.cnblogs.com/haippy/p/3346477.html
- Lock_guard如何释放锁：https://my.oschina.net/yangcol/blog/123433

#### 哪些地方需要考虑线程安全

- 静态变量
- 类的成员变量

### 性能优化

- insert 对象的时候，其实是复制了一个对象，要想优化，最后insert一个指针或者引用
- 不能insert指针或者引用！！！！！！
- 不能insert指针或者引用！！！！！！
- 不能insert指针或者引用！！！！！！
- 这会在STL中因为赋值操作，导致指针失效！！！




### 并发

#### 教程

- 共享数据：https://baptiste-wicht.com/posts/2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data.html
- 

### inline

- 可以在任意函数前面加inline
- 它的作用只是在调用该函数的时候，直接张开函数里面的内容，而不是真正的用栈调用
- 减少函数切换的开销

### const成员函数



### static_cast 和 reinterpret_cast

- static_cast文档：https://en.cppreference.com/w/cpp/language/static_cast
- reinterpret_cast文档：https://en.cppreference.com/w/cpp/language/reinterpret_cast
- 什么时候用： https://stackoverflow.com/questions/573294/when-to-use-reinterpret-cast
- 用法注意事项：http://c.biancheng.net/view/410.html
- static_cast一般用于同类型转换，如浮点数转整数，但是不能指针，或者字符串转整数
- reinterpret_cast高风险的类型转换，可以什么类型都互相转换，出现问题不负责，程序员自己承担。它是根据比特流的复制，然后重新解读到新类型

### const_cast

- const类型转非const
- 也就是去const属性

### dynamic_cast

- 不推荐使用

### delete 和 default函数

- c++11 的新特性
- 主要用来修饰构造函数，赋值函数，析构函数
- delete表示禁止编译器自动生成这些函数
- default表示默认使用编译器的函数
- 用法
  - Arena() = delete;
  - void operator=() = default;

### std::random 随机库使用

- 基本使用：http://www.cnblogs.com/egmkang/archive/2012/09/06/2673253.html

## C++常用库

- boost - C++的准标准库
- gflags - Google的命令行flag解析库
- glog - Google的日志库
- gtest - Google的单元测试库
- gmock - Google的C++ mock库
- double-conversion - V8引擎中使用的浮点数和字符串转换库
- jemalloc - 内存优化组件
- lz4 - 压缩算法库
- lzma - 压缩算法库
- snappy - 压缩算法库
- zlib1g - 压缩算法库
- libevent - 高性能异步网络库
- libssl - SSL加密库
- libdwarf - DWARF调试信息处理库 (experimental)
- libunwind - 程序中调用链的检测库 (experimental)
- unistd.h
  - 提供对 [POSIX](http://baike.baidu.com/view/209573.htm) 操作系统 [API](http://baike.baidu.com/view/16068.htm) 的访问功能的[头文件](http://baike.baidu.com/view/668911.htm)的名称
  - 文档：http://pubs.opengroup.org/onlinepubs/7908799/xsh/unistd.h.html
  - http://www.cnblogs.com/haore147/p/3646243.html
- errno.h
  - http://www.runoob.com/cprogramming/c-standard-library-errno-h.html
  - 定义了整数变量 **errno**，它是通过系统调用设置的，在错误事件中的某些库函数表明了什么发生了错误。该宏扩展为类型为 int 的可更改的左值，因此它可以被一个程序读取和修改。
  - 在程序启动时，**errno** 设置为零，C 标准库中的特定函数修改它的值为一些非零值以表示某些类型的错误。您也可以在适当的时候修改它的值或重置为零。

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



## GLog

- 日志的声明：http://www.voidcn.com/article/p-cfnlsnnv-os.html
- 基本操作：https://blog.csdn.net/a379039233/article/details/46009369

## Gflags

- 基本调用：http://dreamrunner.org/blog/2014/03/09/gflags-jian-ming-shi-yong/
- 主要两点
  - 在某个文件定义好所有的全局变量，统一管理
  - 在其他要使用该文件的代码中，加一条生命即可
  - 比如
  - DEFINE_string(endpoint, "", "config the ip and port that rtidb serves for");
  - DECLARE_string(endpoint);
  - 掌握这两点即可！

## GTest

- 基本使用：https://www.ibm.com/developerworks/aix/library/au-googletestingframework.html
- 基本操作
  - 引用头文件 "gtest/gtest.h"
  - 必须先创建一个Test类，然后继承GTest

```
#include "gtest/gtest.h"


TEST (SquareRootTest, PositiveNos) { 
    EXPECT_EQ (18.0, square-root (324.0));
    EXPECT_EQ (25.4, square-root (645.16));
    EXPECT_EQ (50.3321, square-root (2533.310224));
}
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

SquareRootTest 就是新建的Test类
PositiveNos 测试用例的函数名字
EXPECT_EQ 类似于assert 和 if 专门用于测试结果是否符合预期
square-root 这就是我们测试的函数

```

- 高级操作：http://www.cnblogs.com/coderzh/archive/2009/04/06/1426755.html

## protobuf

- 文档：https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message

- 主要操作：

- 定义好相关message信息

- ```
  message Foo {
    optional string text = 1;
    repeated int32 numbers = 2;
  }
  ```

- 然后proto 格式转换成cpp，java等等。后面直接调用

- 关键函数

  - Name()：获取内容值

  - setName()：设置内容值

  - MegerFrom

  - Merge the fields from the given message into this message.

    Singular fields will be overwritten, if specified in from, except for embedded messages which will be merged. Repeated fields will be concatenated. The given message must be of the same type as this message (i.e. the exact same class).

  - CopyFrom

  - Make this message into a copy of the given message.

    The given message must have the same descriptor, but need not necessarily be the same class. By default this is just implemented as "Clear(); MergeFrom(from);".



## OOP

- 定义：object-oriented programming are data abstraction, inheritance,
  and dynamic binding. 

### copy constructors

- 参考：http://www.fredosaurus.com/notes-cpp/oop-condestructors/copyconstructors.html

```
Person q("Mickey"); // constructor is used to build q.
Person r(p);        // copy constructor is used to build r.
Person p = q;       // copy constructor is used to initialize in declaration.
p = q;              // Assignment operator, no constructor or copy constructor.
```

### Inheritance

- 本质：Classes related by inheritance form a hierarchy. 
- 实际：there is a base class at the root of the hierarchy,from which the other classes inherit, directly or indirectly.
- 这些继承的类也被称作：derived class

#### 基类和派生类的转换问题

- http://c.biancheng.net/cpp/biancheng/view/239.html
- 派生类可以直接转换到基类，但是转换的过程，派生类独有的数据类型和成员函数基类将无法访问
- 也就是说只能子类访问基类的公开元素，基类不能访问派生类的特有元素

#### protected访问权限

- https://blog.csdn.net/luoruiyi2008/article/details/7179788
- Like private members, protected members are inaccessible to users of the class.
- Like public members, the protected members are accessible to classes derived from this class.
- In addition, protected has another important property:
  A derived object may access the protected members of its base class only through a derived object. The derived class has no special access to the protected members of base type objects.
- 前两点好理解
- 第三点如何理解呢？
- 如下面的例子，在父类person中StrName 是 private
- 这个时候程序编译会出错
- 因为子类不能直接修改或者调用父类的private变量
- 但是把private改成 protected就可以了，子类可以调用修改

```
#include <string>
#include <iostream>
using std::string;
using std::cout;
using std::endl;
//define interface
class Person
{
public:
	Person()//成员列表初始化参数
	{};
	virtual ~Person(){};
	virtual void Eat()=0;//人需要吃东西
	virtual void Sleep()=0;//人需要睡觉
	virtual void SetName(const string strName)=0;//人都有名字
	virtual string GetName()=0;//获取名字
	virtual void Work()=0;//人可能要有工作
private:
	string StrName;
};
//实现接口
//实现接口是通过派生类实现的，每个派生类依据自身特点，可以获取同一接口的不同实现
//也就是所谓的多态
class Student:public Person
{
public:
	Student():m_strName("lalalal")
	{};
	~Student()
	{};
	void Eat();
	void Sleep();
	void SetName(const string strName);
	string GetName();
	void Work();
private:
	string m_strName;
};

void Student::Sleep()
{
	cout<<"student sleep."<<endl;
}
void Student::Eat()
{
	cout<<"student eat."<<endl;
}
void Student::SetName(const string strName)
{
	StrName=strName;
}
void Student::Work()
{
	cout<<"student work."<<endl;
}
string Student::GetName()
{
	return StrName;
}

int main() {
    Person* person = new Student();
    person->Eat();
    person->SetName("mingbai");
    cout<<person->GetName()<<endl;
}
```



### Dynamic Binding

- 

###  Virtual Functions

- 参考资料：
  - http://blog.jobbole.com/107432/
  - https://blog.csdn.net/shuzfan/article/details/77165474
- 我的理解：虚函数更多是帮助我们管理子类调用父类的函数。它是通过动态绑定实现。因为在声明的时候，确认了子类，在后期通过基类统一调用虚函数可以动态调用哪个子类的覆盖函数。在多个子类共同继承同一个父类的时候，方便性非常明显
- 结论
  - **虚函数的调用取决于指向或者引用的对象的类型，而不是指针或者引用自身的类型。**
  - **虚函数使得我们可以创建一个统一的基类指针列表，并且调用不同子类的函数而无需知道子类对象究竟是什么**
  - **静态函数不可以声明为虚函数，同时也不能被const 和 volatile关键字修饰。**
- 虚函数实现方式
  - 虚函数表：vtable
  - 虚指针：vptr
  - 参考资料：https://blog.csdn.net/haoel/article/details/1948051/

### 多态

- 参考资料：http://blog.jobbole.com/107432/
- 派生类重写基类的虚函数实现多态，要求函数名、参数列表、返回值完全相同。(协变除外)
- 基类中定义了虚函数，在派生类中该函数始终保持虚函数的特性
- 只有类的成员函数才能定义为虚函数，静态成员函数不能定义为虚函数
- 如果在类外定义虚函数，只能在声明函数时加virtual关键字，定义时不用加
- 构造函数不能定义为虚函数，虽然可以将operator=定义为虚函数，但最好不要这么做，使用时容 易混淆
- 不要在构造函数和析构函数中调用虚函数，在构造函数和析构函数中，对象是不完整的，可能会 出现未定义的行为
- 最好将基类的析构函数声明为虚函数。(析构函数比较特殊，因为派生类的析构函数跟基类的析构 函数名称不一样，但是构成覆盖，这里编译器做了特殊处理)
- 虚表是所有类对象实例共用的
- 多态，虚函数，动态绑定这三者是融合在一起的

### virtual关键字使用

- 资料：http://www.cnblogs.com/xd502djj/archive/2010/09/22/1832912.html
- 定义一个基类和派生类
- 基类的在部分函数前面加virtual
- 派生类继承基类后，可以实现virtual函数里面的内容。也就是覆盖的意思
- final 和 override的作用
- 在定义函数后面添加final表示后面继承的类不可以覆盖该函数
- 在定义函数后面添加override是对应的基类，该函数已经覆盖的了基类函数

```
struct B {
    virtual void f1(int) const;
    virtual void f2();
    void f3();
}
struct D : B {
    void f1(int) const override; 正确
    void f2(int) override;	错误,m没有f2这样的参数的函数
    void f3() override; 	错误,f3不是虚函数
    void f4() override;		错误，B没有f4
}
```

- 如何声明纯虚函数
  - 后面 =0 
  - virtual 函数类型 函数名 (参数表列) =0;
  - 纯虚函数没有函数体
  - 只有函数的名字而不具备函数的功能，不能被调用

## CMake教程

### 参考资料

- 非常经典的5个入门例子：https://blog.csdn.net/dbzhang800/article/details/6314073
- 基本语法：https://www.jianshu.com/p/8909efe13308

### 基本操作

```cmake
cmake_minimum_required(VERSION 3.6)   # CMake version check
project(simple_example)               # Create project "simple_example"
set(CMAKE_CXX_STANDARD 11)            # Enable c++11 standard

set(SOURCE_FILES main.cpp)            # Add main.cpp file of project root directory as source file
add_executable(simple_example ${SOURCE_FILES})       # Add executable target with source files listed in SOURCE_FILES variable
```

### 语法讲解

#### add_executable

- 文档说明：https://cmake.org/cmake/help/v3.0/command/add_executable.html
- 中文讲解：https://elloop.github.io/tools/2016-04-10/learning-cmake-2-commands

#### link_directories

- 参考资料：https://www.cnblogs.com/binbinjx/p/5626916.html
- 专门用于链接lib目录下的动态库

## Linux下的C++

### 基本编译运行

- g++ helloworld.cpp -o helloworld
- ./helloworld

### 复杂文件编译运行

- 需要编写makefile

### 编译中的动态库和静态库

- 参考资料：
  - https://www.jianshu.com/p/63ea84c9666e
  - https://segmentfault.com/q/1010000005269977
- 静态库是指编译连接时，把库文件的代码全部加入到可执行文件中，所以生成的文件较大，但运行时，就不再需要库文件了。即，程序与静态库编译链接后，即使删除静态库文件，程序也可正常执行。
- 动态库正好相反，在编译链接时，没有把库文件的代码加入到可执行文件中，所以生成的文件较小，但运行时，仍需要加载库文件。即，程序只在执行启动时才加载动态库，如果删除动态库文件，程序将会因为无法读取动态库而产生异常。
- 静态库.a
- 动态库.so
- --enable-static 生成静态库a文件
- --enable-shared 生成共享库so文件

## Mac下的C++

### endian.h 配置路径

- vscode自动补全路径

```
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**",
                "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/machine"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```



## 脚本

### 编译运行单个c++文件

- sh xx.sh filename_without_suffix

```
cpp_file=$1
g++ $cpp_file.cpp -o $cpp_file
./$cpp_file
rm -rf $cpp_file
```




[TOC]

