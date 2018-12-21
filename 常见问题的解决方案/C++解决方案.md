## 说明

- c+不同于Java，有非常多的细节需要专门注意，所以需要特意写个方案解决平时遇到的问题

## 目录

[TOC]

## 资源

- https://github.com/fffaraz/awesome-cpp
- cpp大神博客：http://huqunxing.site/



## C++解决方案

### 规范

- 成员变量：全部小写+下划线分开+尾巴后面加下划线
  - table_meta_
- 普通变量：全部小写+下划线分开
  - table_meta_
- 函数名称：单词首字母大写-双驼峰
  - DropTable
- 文件名字：全部小写，下划线分开单词
  - name_server_impl
- 类名：首字母大写，下划线分开单词
  - NameServerImpl
- 域名：namespace 全部小写，不超过三个单词
  - namespace，protobuf

### 与Java不同之处，更多是一种习惯的不同

- 定义std::map 不用new。可以直接使用
  - 适应所有STL中容器



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
- 迭代
  - const auto& iter: table_info_

### unordered_map使用

- 哈希map，查找速度更快，常数级别
- 显然，hash算法不能兼容有序的特点
- 类似Java中的HashMap
- 参考文档：
  - http://www.cplusplus.com/reference/utility/pair/
  - https://en.cppreference.com/w/cpp/container/unordered_map

### vector使用

- 参考文档：http://www.cplusplus.com/reference/vector/vector/
- 

### 函数中的参数

- 默认参数和缺省参数：https://blog.csdn.net/CHF_VIP/article/details/8586921
- 初始化的参数，可以可以赋值也可以不赋值

### Explicit 使用

- 

### 线程

#### 线程池

- 简单实现：https://www.cnblogs.com/lzpong/p/6397997.html
- 介绍：https://zhuanlan.zhihu.com/p/26025722

#### 锁机制

- 锁相关函数：http://www.cnblogs.com/haippy/p/3346477.html
- Lock_guard如何释放锁：https://my.oschina.net/yangcol/blog/123433



### 并发

#### 教程

- 共享数据：https://baptiste-wicht.com/posts/2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data.html
- 

### inline

### const成员函数

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

## GLog

- 日志的声明：http://www.voidcn.com/article/p-cfnlsnnv-os.html

## Gflags

- 基本调用：http://dreamrunner.org/blog/2014/03/09/gflags-jian-ming-shi-yong/
- 主要两点
  - 在某个文件定义好所有的全局变量，统一管理
  - 在其他要使用该文件的代码中，加一条生命即可
  - 比如
  - DEFINE_string(endpoint, "", "config the ip and port that rtidb serves for");
  - DECLARE_string(endpoint);
  - 掌握这两点即可！



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

### Inheritance

- 本质：Classes related by inheritance form a hierarchy. 
- 实际：there is a base class at the root of the hierarchy,from which the other classes inherit, directly or indirectly.
- 这些继承的类也被称作：derived class

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

## 模版

### template


[TOC]

