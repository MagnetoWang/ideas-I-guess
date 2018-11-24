## 说明

- c+不同于Java，有非常多的细节需要专门注意，所以需要特意写个方案解决平时遇到的问题

## 目录

[TOC]

## 资源

- https://github.com/fffaraz/awesome-cpp



## C++解决方案

### 规范

- 成员变量：全部小写+下划线分开+尾巴后面加下划线
- 普通变量：全部小写+下划线分开
- 函数名称：单词首字母大写-双驼峰
- 文件名字：全部小写
- 类名：首字母大写，只有一个大写单词



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





### Map使用

- map需要make_pair多重insert
- Map.find（key)。返回的是迭代器
- 在迭代器的基础上，iter->second。就可以返回value
- 一般返回迭代器都会判断一下
- key中的类对象，必须实现比较函数，不然编译错误
- 不要用指针当key！！！

### 参数

- 默认参数和缺省参数：https://blog.csdn.net/CHF_VIP/article/details/8586921
- 初始化的参数，可以可以赋值也可以不赋值

### 线程

#### 线程池

- 简单实现：https://www.cnblogs.com/lzpong/p/6397997.html
- 介绍：https://zhuanlan.zhihu.com/p/26025722

#### 锁机制

- 锁相关函数：http://www.cnblogs.com/haippy/p/3346477.html
- Lock_guard如何释放锁：https://my.oschina.net/yangcol/blog/123433



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


[TOC]

