## 说明

- c+不同于Java，有非常多的细节需要专门注意，所以需要特意写个方案解决平时遇到的问题

## 目录

[TOC]

## 资源

- https://github.com/fffaraz/awesome-cpp
- cpp大神博客：http://huqunxing.site/
- 非常棒的笔记：http://www.fredosaurus.com/notes-cpp/index.html

## 个人感受

- c++的环境依赖，版本配置简直是个神坑，填不完的感觉
- 看文档的时候，学习英语四六级快速阅读的技巧。找关键词
- 学习c++应该采取非线性思维，类似于给你一堆零碎的图片，而你要做的是贴图

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

### 代码准则-实战获得经验

- 要用的时候再定义变量，不要提前定义好所有的变量
- 借鉴别人的代码的时候不要直接copy，可以先写下所有的函数名字，然后自己一个个的实现，最后做个比较，看看有没有可以优化的地方
- 如果是禁止复制的对象，那么对象在传递的时候必须用指针！！！或者使用引用
- 如果是禁止复制的对象，定义的时候必须用指针！然后通过初始化赋值指针！
- 写模板，包含比较器的时候，必须使用struct，因为使用class，里面的函数默认是私有函数，还需要额外加public变量！！！
- 对于模块的设计，一定要越精简越好，不需要的功能不要加，可以通过其他函数组合成新的功能，也不要加。后续重新封装就好了。这样可以减少bug，同时提高稳定性和可移植性
- 文件编译顺序，先声明类，再定义类，最后才能使用类！！

### 快速写代码

#### 定义类

- 确定类名
- 所有变量放private
- 用列表初始化写构造函数 
- 必要的时候需要加：const 修饰函数 和 返回值
- 遵循用的时候才定义类的原则
  - private定义的变量一般放在public后面
  - 偶尔public需要变量，就可以定义到private后面
- 类里面如果还要定义对象，请设置成指针对象，防止两次对象申明

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

// 实际参考

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
- 只有指针或者引用可以达到多态。对象不行

```
对象指针初始化
	Test* t1 = new Test();

    Student* s1; 
    s1 = new Student(); 
```

### 智能指针

- 参考资料：<https://www.cnblogs.com/wxquare/p/4759020.html>

```
// 共享指针        
        std::shared_ptr<int> ptra = std::make_shared<int>(a);
        std::shared_ptr<int> ptra2(ptra); //copy
        
// unique_ptr
        std::unique_ptr<int> uptr(new int(10));  //绑定动态对象
        //std::unique_ptr<int> uptr2 = uptr;  //不能賦值
        //std::unique_ptr<int> uptr2(uptr);  //不能拷貝
        std::unique_ptr<int> uptr2 = std::move(uptr); //轉換所有權
        uptr2.release(); //释放所有权
```



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

### 枚举的使用 enumerations

- It also lets you define new types but in a fairly restricted fashion

- enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet};

- It makes spectrum the name of a new type; spectrum is termed an enumeration, 

  much as a struct variable is called a structure. 

- It establishes red, orange, yellow, and so on, as symbolic constants for the integer
  values 0–7.These constants are called enumerators.

```
// example
enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet};
spectrum band; // band a variable of type spectrum
band = blue; // valid, blue is an enumerator
band = 2000; // invalid, 2000 not an enumerator
band = orange; // valid
++band; // not valid, ++ discussed in Chapter 5
band = orange + red; // // not valid, but a little tricky

命名规定
enum UrlTableErrors { 
	OK = 0,
    ERROR_OUT_OF_MEMORY,
	ERROR_MALFORMED_INPUT,
   };
```



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

#### 默认的构造函数

#### 默认的赋值函数

- 如果是自己实现的默认构造函数

- 比如levelDB的slice类

- 当slice是指针的时候

- slice*  s

- *s = Slice(参数);

- 而不应该是 *s = new Slice(xx,xx);

  ```
      Slice(const Slice&) = default;
      Slice& operator=(const Slice&) = default;
  	Slice* result;
  	*result = Slice(scratch, message_size);
  ```

#### 类里面声明其他类

- 参考资料：<https://blog.csdn.net/jinjgkfadfaf/article/details/52713256>
- 如果类里面声明其他类，那么会出现声明两次对象的现象
- 为了解决这个问题统一改成类里面声明其他类的指针

```
class B {
private:
	A *a;
public:
	B() {
		a = new A();
		cout << "B is constructed!" << endl;
	}
	~B() {
		delete a;
	}

```



### Map使用

- 参考文档：http://www.cplusplus.com/reference/map/map/

- 在多重map中，需要用make_pair进行封装，然后在插入数据

  - 比如key也是map,value也是map
  - 那么key 也要make_pair， value也要make_pair

- Map.find（key)。返回的是迭代器
  - 在迭代器的基础上，iter->second。就可以返回value

  - 一般返回迭代器都会判断一下，是否为end情况

  - ```
      std::map<char,int> mymap;
      std::map<char,int>::iterator it;
      it = mymap.find('b');
      if (it != mymap.end())
        mymap.erase (it);
      ```

- key中的类对象，必须实现比较函数，不然编译错误

  - 不要用指针当key！！！

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

- map中是有序的

  - 插入顺序：1000 500 700
  - 迭代后的顺序是：500 700 1000
  - 字符串顺序按字典序：aaa，abc，abcd，abcde，bbb，ccc

- 修改map的value对象

  - class& name = map.at(key)
  - at返回是个引用
  - 如果对象后面不加引用，那么map就会复制出一个value对象，然后传出来。这样当你修改value对象里面的内容的时候，就和map中的value没有关系了
  - 所以是否加引用，要看具体情况。如果要修改map中value对象的内容，那么就要加
  - std::map<std::string, std::map<uint64_t, uint32_t>>::iterator it = offset_pos_map_.find(current_file);
  - std::map<uint64_t, uint32_t>& offset_pos = offset_pos_map_.at(current_file)

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

```
reserve(number) 提前开辟vector空间，可以减少后面自动增长的开销
clear() 清除所有的元素
push_back(element) 往最后一个位置插入元素
erase(index) 删除第index个位置的元素
```



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
- 字符串赋值
  - <http://www.cplusplus.com/reference/string/string/assign/>
  - str.assign(source_str)

```

string& assign (const string& str, size_t subpos, size_t sublen);
  std::string str;
  std::string base="The quick brown fox jumps over a lazy dog.";
  str.assign(base);
  std::cout << str << '\n';
  // result
  The quick brown fox jumps over a lazy dog.

```

- 找字符串字符的最后一个位置
  - <http://www.cplusplus.com/reference/string/string/find_first_of/>
  - std::string::find_last_of
  - std::string::npos

```
#include <iostream>       // std::cout
#include <string>         // std::string
#include <cstddef>         // std::size_t

void SplitFilename (const std::string& str)
{
  std::cout << "Splitting: " << str << '\n';
  std::size_t found = str.find_last_of("/\\");
  std::cout << " path: " << str.substr(0,found) << '\n';
  std::cout << " file: " << str.substr(found+1) << '\n';
}

int main ()
{
  std::string str1 ("/usr/bin/man");
  std::string str2 ("c:\\windows\\winhelp.exe");

  SplitFilename (str1);
  SplitFilename (str2);

  return 0;
}
```

- 选择子字符串
  - xx.substr(0,3);
  - 左闭右开
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
- 字符串拼接
  - https://baike.baidu.com/item/strcat
  - char *strcat(char *dest, const char *src);

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

- 基本用法
  - typedef unsigned int uint32_t;
  - 只是定义一个新的好记的名字！或者叫别名Aliases
- 高级用法：
  - <http://www.cnblogs.com/shenlian/archive/2011/05/21/2053149.html>
  - <http://www.cnblogs.com/csyisong/archive/2009/01/09/1372363.html>

```
定义函数指针，从zookeeper看到的
typedef void (*watcher_fn)(zhandle_t *zh, int type, int state, const char *path,void *watcherCtx);

watcher_fn 可以直接用定义函数，因为它是个函数，后面的括号是它的签名zhandle,int,int等等， void是它返回值类型

和int,double直接用
watcher_fn fn;
fn(x,x,xx,xxx);
```



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

### exception使用

- std::exception
- 资料：<https://blog.csdn.net/fengbingchun/article/details/78303734>

### 函数中的参数

- 默认参数和缺省参数：https://blog.csdn.net/CHF_VIP/article/details/8586921
- 初始化的参数，可以可以赋值也可以不赋值
- 参数一般都是默认传值。传值的意思就是，传递参数会复制一个新对象到函数内部。尤其传递一个对象时，会显得十分耗时。而且是函数内部的修改该值的时候，是不会影响实际参数的值。
- 传引用的就是传地址的值！而不是对象内部数据的值！
- 传对象的值到函数里面，会发生构造一次对象，析构一次对象消耗。而且这是没有考虑到对象中可能还含有其他对象的情况，那么消耗将会更加多。
- 规范：输入参数在前，输出结果在后

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

- 所有的引用必须加const限定

```
std::string xx("hello");
function(xx);

// 定义函数
function(const std::string& xx) {
    xxxxx
}
```

#### 传递的区别

- 引用不需要再定义指针变量，只是给之前的变量换了一个别名

#### 注意问题

- 如果传入指针进入函数里面，要避免指针被函数内部修改！！！最好在指针右边加 const。可以编译中查出问题
- 如果修改指针的内容，那么也要注意修改是否正确

### 函数指针

#### 场景

- 来模板中调用统一函数接口，函数名相同，但是函数的参数全部都一样。比如服务端的各种类型的请求函数

#### 资料

- 使用方法：<https://www.cprogramming.com/tutorial/function-pointers.html

#### 使用

```

```



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

#### 文件描述符

- 参考资料：https://blog.csdn.net/lf_2016/article/details/54605651

- ```
  open:以指定方式打开一个文件，调用成功后返回一个文件描述符。 
  creat:打开一个文件，如果文件不存在则创建它，成功后返回一个文件描述符。 
  close:关闭文件，进程对文件加锁全部被释放。 
  read:从文件描述符对应的文件中读取文件，成功后返回读出的字节数。 
  write:向文件描述符对应的文件中写入数据，成功后返回写入的字节数。 
  ftruncate:把文件描述符对应的文件缩短到指定的长度。 
  lseek：把文件指针设置到指定的位置，相当于库函数中的fseek。 
  fsync:将已经写入到文件的数据写入到磁盘或其他下层设备中，成功返回0。 
  fstat:返回文件描述符所对应文件的相关信息，把结果保存在struct stat中，成功返回0。 
  fchown:修改文件描述符对应的文件的文件所有者和文件所有者组的信息。 
  fchmod:修改文件描述符对应的文件的权限。 
  flock：对文件施加建议性锁，成功返回0。 
  fcntl:技能施加建议性锁也能施加强制性锁，能建立记录锁、读取锁，写入锁，成功返回0 
  dup:复制文件描述符，返回没有使用的文件描述符中的最小编号。 
  dup2:由用户指定返回的文件描述符的值，用来重新打开或重定向一个文件描述符。 
  select:同时从多个文件描述符读取数据或向多个文件描述符写入数据
  ```


#### fopen函数

- 参考资料
  - https://blog.csdn.net/cyforce/article/details/6159989
  - 读写随机还是顺序：https://blog.csdn.net/jianzhanger/article/details/3637322
- 返回值：文件顺利打开后，指向该流的文件指针就会被返回。如果文件打开失败则返回NULL，并把错误代码存在errno 中。
- 参数 a+ 是否需要 要看场景

```
　　r 打开只读文件，该文件必须存在。

　　r+ 打开可读写的文件，该文件必须存在。

　　rb+ 读写打开一个二进制文件，只允许读写数据。

　　rt+ 读写打开一个文本文件，允许读和写。

　　w 打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件。

　　w+ 打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。

　　a 以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。（EOF符保留）

　　a+ 以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 （原来的EOF符不保留）

　　wb 只写打开或新建一个二进制文件；只允许写数据。

　　wb+ 读写打开或建立一个二进制文件，允许读和写。

　　wt+ 读写打开或着建立一个文本文件；允许读写。

　　at+ 读写打开一个文本文件，允许读或在文本末追加数据。

　　ab+ 读写打开一个二进制文件，允许读或在文件末追加数据。
```

#### remove函数

- 文档资料：http://www.cplusplus.com/reference/cstdio/remove/
- 删除文件
- 等于0表示成功
- 注意
  - 文件下必须没有文件才能删除成功

#### fwrite函数

- 文档：http://www.cplusplus.com/reference/cstdio/fwrite/
- size_t fwrite ( const void * ptr, size_t size, size_t count, FILE * stream );
- Write block of data to stream
- ptr 数组内容
- stream 输出的文件
- size 每个元素的大小
- count 写入多少个元素

#### pread函数

- 文档：https://linux.die.net/man/2/pread

- ```
      int n = 100;
      char* scratch = (char*)malloc(sizeof(char) * n);
      uint64_t offset = 10;
      Status status;
      ssize_t read_size = ::pread(fd, scratch, n, static_cast<off_t>(offset));
  ```


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
- 

#### ftruncate()函数

- http://www.cppblog.com/jerryma/archive/2010/06/14/117888.html
- 改变文件大小
- int ftruncate(int fd, off_t  length)
- 返回值  ：返回和stream文件流对应的文件描述符。如果失败，返回-1

#### lseek函数

- https://baike.baidu.com/item/lseek
- off_t lseek(int handle, off_t offset, int fromwhere);
- [当前文件](https://baike.baidu.com/item/%E5%BD%93%E5%89%8D%E6%96%87%E4%BB%B6)[偏移量](https://baike.baidu.com/item/%E5%81%8F%E7%A7%BB%E9%87%8F)（current file offset）cfo

#### lstat函数

- https://baike.baidu.com/item/lstat/2885045
- 返回文件的状态
- include \<sys/stat.h\>

#### 按位读写

- 参考资料：https://blog.csdn.net/shixiaoguo90/article/details/24832031

- ```
  
  ```

### 流处理

#### ofstream

- 文档资料：http://www.cplusplus.com/doc/tutorial/files/

- 文件写入流对象，Stream class to write on files

- ```
  #include <iostream>
  #include <fstream>
  using namespace std;
  
  int main () {
    ofstream file;
    file.open ("codebind.txt");
    file << "Please writr this text to a file.\n this text is written using C++\n";
    file.close();
    return 0;
  }
  ```

#### ifstream

- Stream class to read from files

#### fstream

- Stream class to both read and write from/to files.

### 字符串函数

- 函数集合：http://www.kuqin.com/clib/string/memccpy.html

#### memcmp函数使用

- memcmp(data_, x.data_, x.size_) == 0 data 与 x 比较 前 x个字符串

#### memcpy函数使用

- string.h 不要用cstring 参数有区别
- memcpy(void *dest, const void *src, size_t n) 
- 从源src所指的内存地址的起始位置开始拷贝n个字节到目标dest所指的内存地址的起始位置中
- source和destin都不一定是数组，任意的可读写的空间均可
- 最好在指针字符串末尾添加 \0 ，防止字节流尾部出现无关字符

#### snprintf函数

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

#### 概念

- 函数对象：<https://baike.baidu.com/item/%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1>
- 函数绑定：boost::bind

#### 线程队列

- brpc有实现的线程队列

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

### inline使用

- 可以在任意函数前面加inline
- 它的作用只是在调用该函数的时候，直接张开函数里面的内容，而不是真正的用栈调用
- 减少函数切换的开销

### static_cast 和 reinterpret_cast

- static_cast文档：https://en.cppreference.com/w/cpp/language/static_cast
- reinterpret_cast文档：https://en.cppreference.com/w/cpp/language/reinterpret_cast
- 什么时候用： https://stackoverflow.com/questions/573294/when-to-use-reinterpret-cast
- 用法注意事项：http://c.biancheng.net/view/410.html
- static_cast一般用于同类型转换，如浮点数转整数，但是不能指针，或者字符串转整数
- reinterpret_cast高风险的类型转换，可以什么类型都互相转换，出现问题不负责，程序员自己承担。它是根据比特流的复制，然后重新解读到新类型

```
#include <vector>
#include <iostream>
 
struct B {
    int m = 0;
    void hello() const {
        std::cout << "Hello world, this is B!\n";
    }
};
struct D : B {
    void hello() const {
        std::cout << "Hello world, this is D!\n";
    }
};
 
enum class E { ONE = 1, TWO, THREE };
enum EU { ONE = 1, TWO, THREE };
 
int main()
{
    // 1: initializing conversion
    int n = static_cast<int>(3.14); 
    std::cout << "n = " << n << '\n';
    std::vector<int> v = static_cast<std::vector<int>>(10);
    std::cout << "v.size() = " << v.size() << '\n';
 
    // 2: static downcast
    D d;
    B& br = d; // upcast via implicit conversion
    br.hello();
    D& another_d = static_cast<D&>(br); // downcast
    another_d.hello();
 
    // 3: lvalue to xvalue
    std::vector<int> v2 = static_cast<std::vector<int>&&>(v);
    std::cout << "after move, v.size() = " << v.size() << '\n';
 
    // 4: discarded-value expression
    static_cast<void>(v2.size());
 
    // 5. inverse of implicit conversion
    void* nv = &n;
    int* ni = static_cast<int*>(nv);
    std::cout << "*ni = " << *ni << '\n';
 
    // 6. array-to-pointer followed by upcast
    D a[10];
    B* dp = static_cast<B*>(a);
 
    // 7. scoped enum to int or float
    E e = E::ONE;
    int one = static_cast<int>(e);
    std::cout << one << '\n';
 
    // 8. int to enum, enum to another enum
    E e2 = static_cast<E>(one);
    EU eu = static_cast<EU>(e2);
 
    // 9. pointer to member upcast
    int D::*pm = &D::m;
    std::cout << br.*static_cast<int B::*>(pm) << '\n';
 
    // 10. void* to any type
    void* voidp = &e;
    std::vector<int>* p = static_cast<std::vector<int>*>(voidp);
}
```

### const_cast

- const类型转非const
- 也就是去const属性
- 通过指针的特点来去除const

```
const int constant = 21;
int* modifier = const_cast<int*>(&constant);
```

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

### std::sort

- <https://zh.cppreference.com/w/cpp/algorithm/sort>

```
#include <algorithm>
   std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3}; 
   
   // 传入迭代器，位置随意，一般都是头和尾巴。在传入比较器，或者使用默认排序规则也行
    std::sort(s.begin(), s.end(), std::greater<int>());

    // 用 lambda 表达式排序
    std::sort(s.begin(), s.end(), [](int a, int b) {
    return b < a;   
    });

    // 用自定义函数对象排序
    struct {
        bool operator()(int a, int b) const
        {   
            return a < b;
        }   
    } customLess;
    std::sort(s.begin(), s.end(), customLess);
```

### std::stoull

- 文档：<http://www.cplusplus.com/reference/string/stoull/>
- 解释字符串到数字

```
// stoull example
#include <iostream>   // std::cout
#include <string>     // std::string, std::stoull

int main ()
{
  std::string str = "8246821 0xffff 020 -1";

  std::string::size_type sz = 0;   // alias of size_t

  while (!str.empty()) {
    unsigned long long ull = std::stoull (str,&sz,0);
    std::cout << str.substr(0,sz) << " interpreted as " << ull << '\n';
    str = str.substr(sz);
  }

  return 0;
}

8246821 interpreted as 8246821
 0xffff interpreted as 65535
 020 interpreted as 16
 -1 interpreted as 18446744073709551615
```

### std::accumulate

```
#include <numeric> 
求和函数

std::vector<uint64_t> level;
uint64_t sum = accumulate(level.begin() , level.end() , 0);

求均值
double average = (double)sum/(double)level.size();
```



## C++常用代码段

### 打印时间

- http://www.cnblogs.com/mfryf/archive/2012/02/13/2349360.html

```
#include <iostream>
#include <ctime>
using namespace std;
int main()
{
    time_t now_time;
    now_time = time(NULL);
    cout<<now_time;
    return 0;
}
```

### 打印毫秒级别的时间

- 资料
  - <https://stackoverflow.com/questions/19555121/how-to-get-current-timestamp-in-milliseconds-since-1970-just-the-way-java-gets>
- 文档
  - <https://en.cppreference.com/w/cpp/chrono>
  - <https://blog.csdn.net/u013390476/article/details/50209603>
  - <https://www.jianshu.com/p/80de04b41c31>
- 时间戳转换工具：<https://tool.lu/timestamp/>

```
static inline uint64_t GetMillisecondTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count();
    return ts;
}

static inline uint64_t GetMicrosecondsTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::microseconds>(now.time_since_epoch()).count();
    return ts;
}

static inline uint64_t GetSecondTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count();
    return ts;
}
```



### 数字转字节

- 这个超级常用，数字写入文件的时候一定要压缩到规定4字节或者8字节。这样就能按字节大小读出文件

- 如果直接写数字到文件里面，那么就是1个数字符号1个字节。根本没有办法规定大小读取数字！！！

- 这个弄了我一个下午，后面发现levelDB里面

- ```c++
  inline void EncodeFixed32(char* buf, uint32_t value) {
      if (kLittleEndian) {
          memcpy(buf, &value, sizeof(value));
      } else {
          buf[0] = value & 0xff;
          buf[1] = (value >> 8) & 0xff;
          buf[2] = (value >> 16) & 0xff;
          buf[3] = (value >> 24) & 0xff;
      }
  }
  
  inline void EncodeFixed64(char* buf, uint64_t value) {
      if (kLittleEndian) {
          memcpy(buf, &value, sizeof(value));
      } else {
          buf[0] = value & 0xff;
          buf[1] = (value >> 8) & 0xff;
          buf[2] = (value >> 16) & 0xff;
          buf[3] = (value >> 24) & 0xff;
          buf[4] = (value >> 32) & 0xff;
          buf[5] = (value >> 40) & 0xff;
          buf[6] = (value >> 48) & 0xff;
          buf[7] = (value >> 56) & 0xff;
      }
  }
  
  inline uint32_t DecodeFixed32(const char* ptr) {
      if (kLittleEndian) {
          // Load the raw bytes
          uint32_t result;
          memcpy(&result, ptr, sizeof(result));  // gcc optimizes this to a plain load
          return result;
      } else {
          return ((static_cast<uint32_t>(static_cast<unsigned char>(ptr[0])))
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[1])) << 8)
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[2])) << 16)
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[3])) << 24));
      }
  }
  
  inline uint64_t DecodeFixed64(const char* ptr) {
      if (kLittleEndian) {
          // Load the raw bytes
          uint64_t result;
          memcpy(&result, ptr, sizeof(result));  // gcc optimizes this to a plain load
          return result;
      } else {
          uint64_t lo = DecodeFixed32(ptr);
          uint64_t hi = DecodeFixed32(ptr + 4);
          return (hi << 32) | lo;
      }
  }
  ```

### 大小端检查

```c++
typedef signed char           int8_t;
typedef signed short          int16_t;
typedef signed int            int32_t;
typedef signed long long      int64_t;
typedef unsigned char         uint8_t;
typedef unsigned short        uint16_t;
typedef unsigned int          uint32_t;
typedef unsigned long long    uint64_t;
namespace ibdb {
namespace port {

inline const bool IsLittleEndian() {
    int a = 1;
    if (*(char*)&a == 1) {
      return true;
    } else {
      return false;
    }
}

static const bool kLittleEndian = IsLittleEndian();
```



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
### errno.h
  - http://www.runoob.com/cprogramming/c-standard-library-errno-h.html
  - 定义了整数变量 **errno**，它是通过系统调用设置的，在错误事件中的某些库函数表明了什么发生了错误。该宏扩展为类型为 int 的可更改的左值，因此它可以被一个程序读取和修改。
  - 在程序启动时，**errno** 设置为零，C 标准库中的特定函数修改它的值为一些非零值以表示某些类型的错误。您也可以在适当的时候修改它的值或重置为零。

### assert.h

- ASSERT_NE
- ASSERT_EQ
- ASSERT_TRUE
- ASSERT_FALSE

### unist.h

#### usleep函数-进程延时

- 参考资料：<https://baike.baidu.com/item/usleep%E5%87%BD%E6%95%B0>

### limits.h

- 文档：<http://www.cplusplus.com/reference/climits/>

```

name	expresses	value*
CHAR_BIT	Number of bits in a char object (byte)	8 or greater*
SCHAR_MIN	Minimum value for an object of type signed char	-127 (-27+1) or less*
SCHAR_MAX	Maximum value for an object of type signed char	127 (27-1) or greater*
UCHAR_MAX	Maximum value for an object of type unsigned char	255 (28-1) or greater*
CHAR_MIN	Minimum value for an object of type char	either SCHAR_MIN or 0
CHAR_MAX	Maximum value for an object of type char	either SCHAR_MAX or UCHAR_MAX
MB_LEN_MAX	Maximum number of bytes in a multibyte character, for any locale	1 or greater*
SHRT_MIN	Minimum value for an object of type short int	-32767 (-215+1) or less*
SHRT_MAX	Maximum value for an object of type short int	32767 (215-1) or greater*
USHRT_MAX	Maximum value for an object of type unsigned short int	65535 (216-1) or greater*
INT_MIN	Minimum value for an object of type int	-32767 (-215+1) or less*
INT_MAX	Maximum value for an object of type int	32767 (215-1) or greater*
UINT_MAX	Maximum value for an object of type unsigned int	65535 (216-1) or greater*
LONG_MIN	Minimum value for an object of type long int	-2147483647 (-231+1) or less*
LONG_MAX	Maximum value for an object of type long int	2147483647 (231-1) or greater*
ULONG_MAX	Maximum value for an object of type unsigned long int	4294967295 (232-1) or greater*
LLONG_MIN	Minimum value for an object of type long long int	-9223372036854775807 (-263+1) or less*
LLONG_MAX	Maximum value for an object of type long long int	9223372036854775807 (263-1) or greater*
ULLONG_MAX	Maximum value for an object of type unsigned long long int	18446744073709551615 (264-1) or greater*
```



### boost库

#### 字符串转数字

- 文档：<http://www.habadog.com/2011/05/07/boost-lexical_cast-intro/>

```
#include "iostream"
#include "boost/lexical_cast.hpp" // 需要包含的头文件
 
using boost::lexical_cast;
using boost::bad_lexical_cast;
using namespace std;
 
int main()
{
    char* p="32768";
    int i=0;
    try
    {
        i=lexical_cast<int>(p); // 将字符串转化为整数
    }
    catch(bad_lexical_cast&)    // 转换失败会抛出一个异常
    {
        i=0;
    }
    cout << i << endl;
    return i;
}
```

#### 字符串操作

- 参考资料
  - 入门介绍：<https://www.cnblogs.com/racaljk/p/7822301.html>
  - 官方教程：<https://theboostcpplibraries.com/boost.stringalgorithms>
- 用法

```

```



#### boost::function

- 参考资料
  - 简单例子：<http://www.cnblogs.com/sld666666/archive/2010/12/16/1907591.html>
  - 结合模板的高级例子
    - https://stackoverflow.com/questions/3040893/passing-template-into-boost-function
    - https://stackoverflow.com/questions/33096012/using-boostfunction-with-templates
- 一个函数的包装器(function wrapper)，用来定义函数对象。代替函数指针
- 简单用法

```
#include "boost/function.hpp"
// 推荐下面的写法，其他写法不是所有编译器支持
boost::function<float(int x, int y)>function_name

// function_name 可以当做int,double一样随意定义，赋值的时候，把函数地址赋值即可
int real_sum(int x, int y) 
{ 
	return x + y;
};
function_name sum;
// sum is a function name, real_sum is a real function which realize the sum of two integer
sum = &real_sum;
sum(1,2);


```

- 高级用法

```
模板加boost::function

```

#### boost::bind

- 参考资料
  - 简单使用：<https://theboostcpplibraries.com/boost.bind>
  - 进阶教程：<https://www.boost.org/doc/libs/1_65_1/libs/bind/doc/html/bind.html#bind.purpose.using_bind_with_functions_and_fu>
  - 中文介绍：<https://www.cnblogs.com/blueoverflow/p/4740093.html>
  - 中文使用：<https://blog.csdn.net/adcxf/article/details/3970116>
- 作为类中的回调函数
  - <https://blog.csdn.net/stelalala/article/details/36882159>
- 绑定函数的代码

```
最简单用法
 void fun(int x, int y) {
  cout << x << ", " << y << endl;
 }
 第一种写法
 boost::bind(&fun, 3, 4)( );  //无参数. 输出 3, 4
 第二种写法
 boost::bind(&fun, _1, _2)(3, 4);    // 3将代替_1占位符, 4将代替_2占位符.输出 3, 4
 第三种写法
 boost::bind(&fun, _2, _1)(3, 4);   // 3将代替_1占位符, 4将代替_2占位符.输出 4, 3
 第四种写法
 boost::bind(&fun, _1, _1)(3);  // 输出 3, 3

#include <boost/bind.hpp>
#include <vector>
#include <algorithm>
#include <iostream>

void print(std::ostream *os, int i)
{
  *os << i << '\n';
}

int main()
{
  std::vector<int> v{1, 3, 2};
  std::for_each(v.begin(), v.end(), boost::bind(print, &std::cout, _1));
}


```



### mutex.h

#### mutex

- 加互斥元是为了多线程访问一个函数或者变量时，可以保证只有一个线程可以访问，而其他线程只能等待

```
先定义互斥元
std::mutex mu_;

用的时候加普通锁，在当前的大括号范围内的所有变量都会被加锁保护
std::lock_guard<std::mutex> lock(mu_);
加独占锁
std::unique_lock<std::mutex> lock(mu_);
```



#### condition_variable

- 参考资料
  - <https://en.wikipedia.org/wiki/Monitor_%28synchronization%29>
  - <https://www.cnblogs.com/haippy/p/3252041.html>
- 条件变量
  - Threads attempting an operation may need to wait until some condition P holds true
  - 有时候线程需要等待某个条件允许后才能继续运行
  - 这个时候就需要条件变量来控制线程的调度情况

```
定义条件变量
std::condition_variable cv_;

因为需要等待某个条件允许，所以有个等待函数
cv_.wait_for(lock, std::chrono::milliseconds(timestamp));

条件允许后，需要通知其他等待的线程可以执行了
cv_.notify_one();// 随机唤醒一个线程
或者
cv.notify_all(); // 唤醒所有线程.
```

- 场景
  - 一般用于回调函数
  - 函数需要等待回调函数执行的结果来确定是否继续运行
  - 根据结果然后唤醒线程
  - 当然也不能无限等待，需要在wait函数里面添加等待时间

### thread

#### std::this_thread::sleep_for

- std::this_thread::sleep_for(std::chrono::microseconds(limit_time - time_used));

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

## 教你C++怎么找bug

### cout打印法

- 可能出的问题上，打印日志信息，然后后面程序运行查看信息

### 创建类出现段错误

- 一个类里面可能有多个类
- 那么这个时候要向指定哪里创建类出现问题
- 就可以单独拿出来创建查看

```
RandomAccessFileHandle::RandomAccessFileHandle(std::string& filename)
    :   filename_(filename),
        offset_(0),
        current_offset_(0),
        fd_(0),
        limiter_(nullptr),
        random_access_file_(nullptr),
        filestream_(nullptr) {
            filestream_ = fopen(filename.c_str(), "r+");
            assert(filestream_ != nullptr);
            fd_ = fileno(filestream_);
            assert(fd_ != -1);
            limiter_ = new Limiter(FLAGS_limiter_max_required);
            assert(limiter_ != nullptr);
            random_access_file_ = ibdb::log::NewRandomAccessFile(filename_, fd_, limiter_);
            assert(random_access_file_ != nullptr);
        }
        
这里有
limiter_
random_access_file_
两个类，可以单独创建定位问题
后面查出问题在
limiter_ = new Limiter(FLAGS_limiter_max_required);
limiter_不支持赋值语句!!!!
必须用列表初始化来构造Limiter对象
```

- 当然也可能是最愚蠢的问题
- 创建对象没有添加new

### 使用lldb或者gdb来查找segment fault

- 这是最有效的方法查找段错误，也就是内存错误。
- 因为可以一步一步单步调试，所以很方便
- 如何使用查询本方案目录栏

## GLog

- 日志的声明：http://www.voidcn.com/article/p-cfnlsnnv-os.html
- 基本操作：https://www.cppfans.org/1566.html
- 链接gtest 和 glog 两个库。直接运行下面代码

```
#include "gtest/gtest.h"
#include "glog/logging.h"

class GlogTest {};

TEST(GlogTest, InfoLog) {
    LOG(INFO) << "this is glog logging test " << std::endl;
}

int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    google::SetLogDestination(google::INFO,"/Users/magnetowang/Documents/GitHub/IcebergDB/ibdb/log/");  
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```



## Gflags

- 文档：https://gflags.github.io/gflags/#define

- 基本调用：http://dreamrunner.org/blog/2014/03/09/gflags-jian-ming-shi-yong/

- 主要两点
  - 在某个文件定义好所有的全局变量，统一管理
  - 在其他要使用该文件的代码中，加一条声明即可
  - 头文件
  - 比如
  - DEFINE_string(endpoint, "", "config the ip and port that rtidb serves for");
    - 变量名，变量值，变量说明
  - DECLARE_string(endpoint);
  - 掌握这两点即可！

- Gflags类型

- ```
  DEFINE_bool: boolean
  DEFINE_int32: 32-bit integer
  DEFINE_int64: 64-bit integer
  DEFINE_uint64: unsigned 64-bit integer
  DEFINE_double: double
  DEFINE_string: C++ string 
  
  头文件
  #include "gflags/gflags.h"
  
  使用Gflags
     if (FLAGS_consider_made_up_languages)
       FLAGS_languages += ",klingon";   // implied by --consider_made_up_languages
     if (FLAGS_languages.find("finnish") != string::npos)
       HandleFinnish();
       
  声明Gflags
  	DECLARE_bool(big_menu);
  ```

## GTest

- 基本使用：https://www.ibm.com/developerworks/aix/library/au-googletestingframework.html
- 文档：https://github.com/google/googletest/blob/master/googletest/docs/primer.md
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

- 生成xml文档：https://stackoverflow.com/questions/8268584/generate-google-c-unit-test-xml-report

- TEST说明

- ```
  use the TEST_P macro to define as many test patterns using this fixture as you want. The _P suffix is for "parameterized" or "pattern", whichever you prefer to think.
  
  you can use INSTANTIATE_TEST_SUITE_P to instantiate the test suite with any set of parameters you want. googletest defines a number of functions for generating test parameters. They return what we call (surprise!) parameter generators. Here is a summary of them, which are all in the testing namespace
  ```


## protobuf

- 文档

  - https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message
  - https://developers.google.cn/protocol-buffers/docs/reference/cpp-generated
  - 高级操作：<https://www.ibm.com/developerworks/cn/linux/l-cn-gpb/index.html>

- 编译安装：https://github.com/protocolbuffers/protobuf/tree/master/src

- ```
  $ git clone https://github.com/protocolbuffers/protobuf.git
  $ cd protobuf
  $ ./autogen.sh
  $ ./configure
  $ make -j5 或者 make
  $ make install
  ```

- 主要操作：

- 定义好相关message信息

- ```
  message Foo {
    optional string text = 1;
    repeated int32 numbers = 2;
  }
  ```

- 然后proto 格式转换成cpp，java等等。后面直接调用

- ```
  protoc --proto_path=src --cpp_out=build/gen src/foo.proto src/bar/baz.proto
  
  proto_path 根目录
  cpp_out 是生成之后的文件目录
  src/foo.proto src/bar/baz.proto 是目标文件的位置，必须在proto_path之内
  
  转Java
  protoc -I=/Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config --java_out=/Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config/proto /Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config/tablet.proto 
  protoc -I=/Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config --java_out=/Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config/proto /Users/magnetowang/Documents/GitHub/Backup-For-Mac/workplace/config/name_server.proto
  ```

- 关键函数

  - Name()：获取内容值

  - setName()：设置内容值

  - MegerFrom

  - Merge the fields from the given message into this message.

    Singular fields will be overwritten, if specified in from, except for embedded messages which will be merged. Repeated fields will be concatenated. The given message must be of the same type as this message (i.e. the exact same class).

  - CopyFrom

  - Make this message into a copy of the given message.

    The given message must have the same descriptor, but need not necessarily be the same class. By default this is just implemented as "Clear(); MergeFrom(from);".

- message类型API

  - 文档：https://developers.google.cn/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message

- 序列化和反序列化

  - 在日志和通信压缩里面可以使用
  - https://developers.google.cn/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.SerializeToFileDescriptor.details

- cmakelist中可以直接生成proto文件

- ```
  include(FindProtobuf)
  protobuf_generate_cpp(PROTO_SRC PROTO_HEADER echo.proto)
  ```

- 导入其他proto文件

  - 参考资料：<https://www.jianshu.com/p/506d6db06676

  - 非常重要的功能

  - 因为不可能所有proto都只在一个文件声明，而不能互相导入

  - 这样扩展性很差

  - ```
    import "myproject/other_protos.proto";
    ```

- 定义rpc服务

  - 参考资料

    - <https://blog.csdn.net/liujiayu2/article/details/77837450>
    - <https://blog.csdn.net/nk_test/article/details/72682780>
    - <https://developers.google.cn/protocol-buffers/docs/proto#services>

  - service结构

  - ```
    service SearchService {
      rpc Search (SearchRequest) returns (SearchResponse);
    }
    ```

  - service使用

  - 需要自己实现channel 和 controller两个类

  - ```
    class EchoServiceImpl : public EchoService {
        public:
        EchoServiceImpl() {}
        virtual void Foo(::google::protobuf::RpcController* controller,
                           const ::FooRequest* request,
                           ::FooResponse* response,
                           ::google::protobuf::Closure* done) {
            std::string str = request->text();
    
            std::string tmp = str;
            for (int i = 1; i < request->times(); i++)
                str += (" " + tmp);
            response->set_text(str);
            response->set_result(true);
            if (done)
                done->Run();
        }   
    };
    int main(int argc, char *argv[]) {
        EchoServiceImpl *impl = new EchoServiceImpl();
        RpcServer rpc_server;
        rpc_server.RegisterService(impl);
        rpc_server.Start();
        return 0;
    }
    
    // google official example
    using google::protobuf;
    
    protobuf::RpcChannel* channel;
    protobuf::RpcController* controller;
    SearchService* service;
    SearchRequest request;
    SearchResponse response;
    
    void DoSearch() {
      // You provide classes MyRpcChannel and MyRpcController, which implement
      // the abstract interfaces protobuf::RpcChannel and protobuf::RpcController.
      channel = new MyRpcChannel("somehost.example.com:1234");
      controller = new MyRpcController;
    
      // The protocol compiler generates the SearchService class based on the
      // definition given above.
      service = new SearchService::Stub(channel);
    
      // Set up the request.
      request.set_query("protocol buffers");
    
      // Execute the RPC.
      service->Search(controller, request, response, protobuf::NewCallback(&Done));
    }
    
    void Done() {
      delete service;
      delete channel;
      delete controller;
    }
    ```

- 注意

  - protobuf 3 有很多问题，推荐使用2.5左右版本。主要是为了兼容使用Brpc
  - 找到protobuf ，然后删除
    - which protoc
  - 2.5版本在github全部clone下来
  - git checkout v2.5.0
  - 注意官网编译脚本有问题
  - autogen.sh 要注释掉部分没用的语句
  - 直接生成configutation即可
  - 后面就是make 一系列操作

- proto模板

```

syntax="proto2";
package ibdb.storage;

option cc_generic_services = true;
// option java_generic_services = true;
// option java_package = "com.ibdb.storage";
// option java_outer_classname = "Storage";

message LogEntry {
    required uint64 offset = 1;
    required uint32 message_size = 2;
    required string message = 3;
}

message Field {
    required string name = 1;
    required string type = 2;
    required bool is_key = 3;
}
```



## BRPC

### 文档

- memory_management
- consistent_hashing.md
- load_balancing.md
- lalb.md
- json2pb.md
- iobuf.md
- io.md
- http_service.md
- http_client.md
- circuit_breaker.md
- client.md
- case_ubrpc.md
- bvar.md
- execution_queue.md
- error_code.md
- builtin_service.md
- bthread.md
- bthread_or_not.md
- bthread_id.md
- baidu_std.md
- avalanche.md
- auto_concurrency_limiter.md
- server.md
- threading_overview.md
- streaming_rpc.md

### 概念

- brpc::Channel
  - 连接服务器的类，主要参数是服务器地址
- brpc::ChannelOptions
  - 设置rpc的管道相关参数
  - protocol
  - connection_type
  - timeout_ms
  - max_retry
- brpc::Controller
  - brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
- brpc::Stub
- brpc::ClosureGuard done_guard(done);
  - This object helps you to call done->Run() in RAII style

### 函数

- usleep

### 用法

#### 客户端

```
#include <gflags/gflags.h>
#include <butil/logging.h>
#include <butil/time.h>
#include <brpc/channel.h>
#include "echo.pb.h"


int main(int argc, char* argv[]) {
    // Parse gflags. We recommend you to use gflags as well.
    GFLAGS_NS::ParseCommandLineFlags(&argc, &argv, true);
    
    // A Channel represents a communication line to a Server. Notice that 
    // Channel is thread-safe and can be shared by all threads in your program.
    brpc::Channel channel;
    
    // Initialize the channel, NULL means using default options.
    brpc::ChannelOptions options;
    options.protocol = FLAGS_protocol;
    options.connection_type = FLAGS_connection_type;
    options.timeout_ms = FLAGS_timeout_ms/*milliseconds*/;
    options.max_retry = FLAGS_max_retry;
    if (channel.Init(FLAGS_server.c_str(), FLAGS_load_balancer.c_str(), &options) != 0) {
        LOG(ERROR) << "Fail to initialize channel";
        return -1;
    }

    // Normally, you should not call a Channel directly, but instead construct
    // a stub Service wrapping it. stub can be shared by all threads as well.
    example::EchoService_Stub stub(&channel);

    // Send a request and wait for the response every 1 second.
    int log_id = 0;
    while (!brpc::IsAskedToQuit()) {
        // We will receive response synchronously, safe to put variables
        // on stack.
        example::EchoRequest request;
        example::EchoResponse response;
        brpc::Controller cntl;

        request.set_message("hello world");

        cntl.set_log_id(log_id ++);  // set by user
        // Set attachment which is wired to network directly instead of 
        // being serialized into protobuf messages.
        cntl.request_attachment().append(FLAGS_attachment);

        // Because `done'(last parameter) is NULL, this function waits until
        // the response comes back or error occurs(including timedout).
        stub.Echo(&cntl, &request, &response, NULL);
        if (!cntl.Failed()) {
            LOG(INFO) << "Received response from " << cntl.remote_side()
                << " to " << cntl.local_side()
                << ": " << response.message() << " (attached="
                << cntl.response_attachment() << ")"
                << " latency=" << cntl.latency_us() << "us";
        } else {
            LOG(WARNING) << cntl.ErrorText();
        }
        usleep(FLAGS_interval_ms * 1000L);
    }

    LOG(INFO) << "EchoClient is going to quit";
    return 0;
}

```

#### 服务端

```
// A server to receive EchoRequest and send back EchoResponse.

#include <gflags/gflags.h>
#include <butil/logging.h>
#include <brpc/server.h>
#include "echo.pb.h"

// Your implementation of example::EchoService
// Notice that implementing brpc::Describable grants the ability to put
// additional information in /status.
namespace example {
class EchoServiceImpl : public EchoService {
public:
    EchoServiceImpl() {};
    virtual ~EchoServiceImpl() {};
    virtual void Echo(google::protobuf::RpcController* cntl_base,
                      const EchoRequest* request,
                      EchoResponse* response,
                      google::protobuf::Closure* done) {
        // This object helps you to call done->Run() in RAII style. If you need
        // to process the request asynchronously, pass done_guard.release().
        brpc::ClosureGuard done_guard(done);

        brpc::Controller* cntl =
            static_cast<brpc::Controller*>(cntl_base);

        // The purpose of following logs is to help you to understand
        // how clients interact with servers more intuitively. You should 
        // remove these logs in performance-sensitive servers.
        LOG(INFO) << "Received request[log_id=" << cntl->log_id() 
                  << "] from " << cntl->remote_side() 
                  << " to " << cntl->local_side()
                  << ": " << request->message()
                  << " (attached=" << cntl->request_attachment() << ")";

        // Fill response.
        response->set_message(request->message());

        // You can compress the response by setting Controller, but be aware
        // that compression may be costly, evaluate before turning on.
        // cntl->set_response_compress_type(brpc::COMPRESS_TYPE_GZIP);

        if (FLAGS_echo_attachment) {
            // Set attachment which is wired to network directly instead of
            // being serialized into protobuf messages.
            cntl->response_attachment().append(cntl->request_attachment());
        }
    }
};
}  // namespace example

int main(int argc, char* argv[]) {
    // Parse gflags. We recommend you to use gflags as well.
    GFLAGS_NS::ParseCommandLineFlags(&argc, &argv, true);

    // Generally you only need one Server.
    brpc::Server server;

    // Instance of your service.
    example::EchoServiceImpl echo_service_impl;

    // Add the service into server. Notice the second parameter, because the
    // service is put on stack, we don't want server to delete it, otherwise
    // use brpc::SERVER_OWNS_SERVICE.
    if (server.AddService(&echo_service_impl, 
                          brpc::SERVER_DOESNT_OWN_SERVICE) != 0) {
        LOG(ERROR) << "Fail to add service";
        return -1;
    }

    // Start the server.
    brpc::ServerOptions options;
    options.idle_timeout_sec = FLAGS_idle_timeout_s;
    if (server.Start(FLAGS_port, &options) != 0) {
        LOG(ERROR) << "Fail to start EchoServer";
        return -1;
    }

    // Wait until Ctrl-C is pressed, then Stop() and Join() the server.
    server.RunUntilAskedToQuit();
    return 0;
}

```

### 测试rpc功能

- 参考资料
  - 中文说明：<http://www.cnblogs.com/welkinwalker/archive/2011/11/29/2267225.html>
  - 使用说明：<https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md

#### 手动测试

- 编写客户端
- 编写服务端
- 然后查看消息传送的内容
- 非常传统，低效率

#### gmock

- 使用gtest里面的gmock

```

```

### brpc进阶

- 模块协议设计：https://www.cnblogs.com/xudong-bupt/p/9496887.html
- 

## ZooKeeper

### 入门

- 参考资料
  - 官方文档：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperProgrammers.html#sc_zkDataModel_znodes>
  - zk配置文件说明：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperStarted.html
  - 命令行文档（超级棒）：<http://www.corejavaguru.com/bigdata/zookeeper/cli>
  - zk内部实现原理文档：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperInternals.html>
  - zk实现生产者和消费者队列和进程的屏障类：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperTutorial.html>
  - c++example：<https://github.com/tgockel/zookeeper-cpp>
  - zooCAPI使用：<http://www.cnblogs.com/haippy/archive/2013/02/21/2920426.html>
  - ACL控制权：<http://ifeve.com/zookeeper-access-control-using-acls/>
  - 书籍推荐
    - 从paxos到zookeeper分布式一致性原理与实践
    - ZooKeeper官方指南
- 问题
  - 集群模式和单机模式
    - 集群就是要配好多台机器的ip和端口。那么每台机器都要有zk程序才行
    - 单机只需要配置本机ip和端口即可
- 使用

```bash
zk的编程学习分三步，建议配合参考资料更详细的说明一起来入门zk
第一步，配置zk服务
第二步，启动zk服务
第三步，开始编程


前提:在zk目录下
第一步，配置zk服务
# 进入conf目录下
cd conf
cp zoo_sample.cfg zoo.cfg

# zoo.cfg服务器配置说明
# the first port is for synchronizing data and communication
# the second port is for leader election
server.1=127.0.0.1:2888:3888
server.2=127.0.0.1:2788:3788
server.3=127.0.0.1:2688:3688

# 单机版
# ip不变，端口一定要不一样
# 集群版
# ip一定要不一样，端口无所谓

# zoo.cfg 里面有DataDir目录，在这个目录下创建myid，myid里面写上id数字就行了

第二步，启动zk服务
# 进入bin目录下，启动服务脚本
cd bin
sh zkServer.sh start
# 验证服务
telnet 127.0.0.1 2181

第三步，开始编程
# 有三种方式，一种是编程语言，另一种是命令行对zk操作
# 先介绍命令行方式
sh zkCli.sh
# 输出所有命令行语法
help
create /zk_test my_data
get /zk_test
# get的结果说明
my_data :This line of text is the data that we stored in the znode.
cZxid = 0x8 :The zxid (ZooKeeper Transaction Id) of the change that caused this znode to be created.
ctime = Mon Nov 30 18:41:06 IST 2015 :The time when this znode was created.
mZxid = 0x8 :The zxid of the change that last modified this znode.
mtime = Mon Nov 30 18:41:06 IST 2015 :The time when this znode was last modified.
pZxid = 0x8 :The zxid of the change that last modified children of this znode.
cversion = 0 :The number of changes to the children of this znode.
dataVersion = 0 :The number of changes to the data of this znode.
aclVersion = 0 :The number of changes to the ACL of this znode.
ephemeralOwner = 0x0: The session id of the owner of this znode if the znode is an ephemeral node. If it is not an ephemeral node, it will be zero.
dataLength = 7 :The length of the data field of this znode.
numChildren = 0 :The number of children of this znode.
# 设置watch
# Watches show a notification when the specified znode’s data get changed
get /zk_test 1

# 编程语言方式
Java非常简单引入jar包，然后直接调接口就行了
直接看C语言编程怎么引入，这里专门放下面一栏
```

### C++ API使用

- 强烈建议先在命令行下体验zk的功能，然后再来编程封装适合自己业务的功能
- 参考资料
  - zk 状态说明：<http://www.cnblogs.com/haippy/archive/2013/02/21/2920241.html>
  - 接口设计参考：<http://www.throwable.club/2018/12/16/zookeeper-curator-usage/#Curator%E7%9A%84%E5%9F%BA%E6%9C%ACApi>
- 注意
  - zk命令行中不提供递归创建节点，同时也不提供创建无数据的节点

```
#include "zookeeper.h"
zhandle_t *zh;

```

- zookeeper状态码

```c++
/** zookeeper return constants **/

enum ZOO_ERRORS {
  ZOK = 0, /*!< Everything is OK */

  /** System and server-side errors.
   * This is never thrown by the server, it shouldn't be used other than
   * to indicate a range. Specifically error codes greater than this
   * value, but lesser than {@link #ZAPIERROR}, are system errors. */
  ZSYSTEMERROR = -1,
  ZRUNTIMEINCONSISTENCY = -2, /*!< A runtime inconsistency was found */
  ZDATAINCONSISTENCY = -3, /*!< A data inconsistency was found */
  ZCONNECTIONLOSS = -4, /*!< Connection to the server has been lost */
  ZMARSHALLINGERROR = -5, /*!< Error while marshalling or unmarshalling data */
  ZUNIMPLEMENTED = -6, /*!< Operation is unimplemented */
  ZOPERATIONTIMEOUT = -7, /*!< Operation timeout */
  ZBADARGUMENTS = -8, /*!< Invalid arguments */
  ZINVALIDSTATE = -9, /*!< Invliad zhandle state */

  /** API errors.
   * This is never thrown by the server, it shouldn't be used other than
   * to indicate a range. Specifically error codes greater than this
   * value are API errors (while values less than this indicate a 
   * {@link #ZSYSTEMERROR}).
   */
  ZAPIERROR = -100,
  ZNONODE = -101, /*!< Node does not exist */
  ZNOAUTH = -102, /*!< Not authenticated */
  ZBADVERSION = -103, /*!< Version conflict */
  ZNOCHILDRENFOREPHEMERALS = -108, /*!< Ephemeral nodes may not have children */
  ZNODEEXISTS = -110, /*!< The node already exists */
  ZNOTEMPTY = -111, /*!< The node has children */
  ZSESSIONEXPIRED = -112, /*!< The session has been expired by the server */
  ZINVALIDCALLBACK = -113, /*!< Invalid callback specified */
  ZINVALIDACL = -114, /*!< Invalid ACL specified */
  ZAUTHFAILED = -115, /*!< Client authentication failed */
  ZCLOSING = -116, /*!< ZooKeeper is closing */
  ZNOTHING = -117, /*!< (not error) no server responses to process */
  ZSESSIONMOVED = -118 /*!<session moved to another server, so operation is ignored */ 
};

/**
*  @name Debug levels
*/
typedef enum {ZOO_LOG_LEVEL_ERROR=1,ZOO_LOG_LEVEL_WARN=2,ZOO_LOG_LEVEL_INFO=3,ZOO_LOG_LEVEL_DEBUG=4} ZooLogLevel;

/**
 * @name ACL Consts
 */
extern ZOOAPI const int ZOO_PERM_READ;
extern ZOOAPI const int ZOO_PERM_WRITE;
extern ZOOAPI const int ZOO_PERM_CREATE;
extern ZOOAPI const int ZOO_PERM_DELETE;
extern ZOOAPI const int ZOO_PERM_ADMIN;
extern ZOOAPI const int ZOO_PERM_ALL;

/** This Id represents anyone. */
extern ZOOAPI struct Id ZOO_ANYONE_ID_UNSAFE;
/** This Id is only usable to set ACLs. It will get substituted with the
 * Id's the client authenticated with.
 */
extern ZOOAPI struct Id ZOO_AUTH_IDS;

/** This is a completely open ACL*/
extern ZOOAPI struct ACL_vector ZOO_OPEN_ACL_UNSAFE;
/** This ACL gives the world the ability to read. */
extern ZOOAPI struct ACL_vector ZOO_READ_ACL_UNSAFE;
/** This ACL gives the creators authentication id's all permissions. */
extern ZOOAPI struct ACL_vector ZOO_CREATOR_ALL_ACL;

/**
 * @name Interest Consts
 * These constants are used to express interest in an event and to
 * indicate to zookeeper which events have occurred. They can
 * be ORed together to express multiple interests. These flags are
 * used in the interest and event parameters of 
 * \ref zookeeper_interest and \ref zookeeper_process.
 */
// @{
extern ZOOAPI const int ZOOKEEPER_WRITE;
extern ZOOAPI const int ZOOKEEPER_READ;
// @}

/**
 * @name Create Flags
 * 
 * These flags are used by zoo_create to affect node create. They may
 * be ORed together to combine effects.
 */
// @{
extern ZOOAPI const int ZOO_EPHEMERAL;
extern ZOOAPI const int ZOO_SEQUENCE;
// @}

/**
 * @name State Consts
 * These constants represent the states of a zookeeper connection. They are
 * possible parameters of the watcher callback.
 */
// @{
extern ZOOAPI const int ZOO_EXPIRED_SESSION_STATE;
extern ZOOAPI const int ZOO_AUTH_FAILED_STATE;
extern ZOOAPI const int ZOO_CONNECTING_STATE;
extern ZOOAPI const int ZOO_ASSOCIATING_STATE;
extern ZOOAPI const int ZOO_CONNECTED_STATE;
// @}

/**
 * @name Watch Types
 * These constants indicate the event that caused the watch event. They are
 * possible values of the first parameter of the watcher callback.
 */
// @{
/**
 * \brief a node has been created.
 * 
 * This is only generated by watches on non-existent nodes. These watches
 * are set using \ref zoo_exists.
 */
extern ZOOAPI const int ZOO_CREATED_EVENT;
/**
 * \brief a node has been deleted.
 * 
 * This is only generated by watches on nodes. These watches
 * are set using \ref zoo_exists and \ref zoo_get.
 */
extern ZOOAPI const int ZOO_DELETED_EVENT;
/**
 * \brief a node has changed.
 * 
 * This is only generated by watches on nodes. These watches
 * are set using \ref zoo_exists and \ref zoo_get.
 */
extern ZOOAPI const int ZOO_CHANGED_EVENT;
/**
 * \brief a change as occurred in the list of children.
 * 
 * This is only generated by watches on the child list of a node. These watches
 * are set using \ref zoo_get_children or \ref zoo_get_children2.
 */
extern ZOOAPI const int ZOO_CHILD_EVENT;
/**
 * \brief a session has been lost.
 * 
 * This is generated when a client loses contact or reconnects with a server.
 */
extern ZOOAPI const int ZOO_SESSION_EVENT;

/**
 * \brief a watch has been removed.
 * 
 * This is generated when the server for some reason, probably a resource
 * constraint, will no longer watch a node for a client.
 */
extern ZOOAPI const int ZOO_NOTWATCHING_EVENT;
```



## OOP

- 定义：object-oriented programming are data abstraction, inheritance,
  and dynamic binding. 

### copy constructors

- 参考：http://www.fredosaurus.com/notes-cpp/oop-condestructors/copyconstructors.html

```c++
Person q("Mickey"); // constructor is used to build q.
Person r(p);        // copy constructor is used to build r.
Person p = q;       // copy constructor is used to initialize in declaration.
p = q;              // Assignment operator, no constructor or copy constructor.
```

### Inheritance

- 本质：Classes related by inheritance form a hierarchy. 
- 实际：there is a base class at the root of the hierarchy,from which the other classes inherit, directly or indirectly.
- 这些继承的类也被称作：derived class

#### 代码

- 支持多继承
- 默认是private继承权限

```
class SingingWaiter : public Waiter, public Singer {...};
```

#### 多继承

- 容易出现歧义
- 建议少用

#### 基类和派生类的转换问题

三种

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

### configure参数详解

- 参考资料：https://blog.csdn.net/zjt289198457/article/details/6918656

- ```
  --prefix=PREFIX 
  把所有文件装在目录   PREFIX下面而不是   /usr/local/pgsql   里．实际的文件会安装到不同的子目录里；甚至没有一个文件会直接   安装到   PREFIX   目录里．
  这个是最常用的！！！
  ```

### 添加GDB调试功能

- 先按照好gdb

- 然后在cmake里面写这些配置

- ```
  set(CMAKE_BUILD_TYPE "Debug")
  set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
  set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
  ```

### 震惊30天的cmake用法

- 这是一个悲伤的故事

```

```



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

## GDB的使用

- 参考资料
  - <https://www.cs.cmu.edu/~gilpin/tutorial/>
  - <https://blog.csdn.net/liigo/article/details/582231>

```
添加可以gdb调试的文件
gdb xxx

然后运行
run 或者 start


```

### Unable to find Mach task port for process-id 801: (os/kern) failure (0x5)

- 参考资料：<https://stackoverflow.com/questions/11504377/gdb-fails-with-unable-to-find-mach-task-port-for-process-id-error>
- 最快的方法
- sudo gdb xxxx
- 长久的方法
  - <http://codelife.me/blog/2014/07/14/install-gdb-on-osx-mavericks/>
- 安装gdb证书

### During startup program terminated with signal SIG113 ?

- 编译被终止了在mac系统中

### During startup program terminated with signal SIGTRAP

- 

## lldb的使用

- 参考资料
  - <https://www.jianshu.com/p/087cd19d49ba>
- 下一步直接进入源码层 s
- 下一步但是不进入源码层 n
- 给某个文件设置断点
  - breakpoint set -f Foo.m -l 10
  - <https://www.jianshu.com/p/dcc8e647a501>
- 跳到下一个断点
  - c
- 打印变量内容
  - print 变量名 打印基本数据类型的内容
  - po 变量名 打印对象内容
  - <http://see.sl088.com/wiki/LLDB_%E6%89%93%E5%8D%B0%E5%8F%98%E9%87%8F>

```
Debugger commands:
  apropos           -- List debugger commands related to a word or subject.
  breakpoint        -- Commands for operating on breakpoints (see 'help b' for shorthand.)
  bugreport         -- Commands for creating domain-specific bug reports.
  command           -- Commands for managing custom LLDB commands.
  disassemble       -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  expression        -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  frame             -- Commands for selecting and examing the current thread's stack frames.
  gdb-remote        -- Connect to a process via remote GDB server.  If no host is specifed, localhost is assumed.
  gui               -- Switch into the curses based GUI mode.
  help              -- Show a list of all debugger commands, or give details about a specific command.
  kdp-remote        -- Connect to a process via remote KDP server.  If no UDP port is specified, port 41139 is assumed.
  language          -- Commands specific to a source language.
  log               -- Commands controlling LLDB internal logging.
  memory            -- Commands for operating on memory in the current target process.
  platform          -- Commands to manage and create platforms.
  plugin            -- Commands for managing LLDB plugins.
  process           -- Commands for interacting with processes on the current platform.
  quit              -- Quit the LLDB debugger.
  register          -- Commands to access registers for the current thread and stack frame.
  script            -- Invoke the script interpreter with provided code and display any results.  Start the interactive interpreter if no code is supplied.
  settings          -- Commands for managing LLDB settings.
  source            -- Commands for examining source code described by debug information for the current target process.
  statistics        -- Print statistics about a debugging session
  target            -- Commands for operating on debugger targets.
  thread            -- Commands for operating on one or more threads in the current process.
  type              -- Commands for operating on the type system.
  version           -- Show the LLDB debugger version.
  watchpoint        -- Commands for operating on watchpoints.
Current command abbreviations (type 'help command alias' for more info):
  add-dsym  -- Add a debug symbol file to one of the target's current modules by specifying a path to a debug symbols file, or using the options to specify a module to download symbols
               for.
  attach    -- Attach to process by ID or name.
  b         -- Set a breakpoint using one of several shorthand formats.
  bt        -- Show the current thread's call stack.  Any numeric argument displays at most that many frames.  The argument 'all' displays all threads.
  c         -- Continue execution of all threads in the current process.
  call      -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  continue  -- Continue execution of all threads in the current process.
  detach    -- Detach from the current target process.
  di        -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  dis       -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  display   -- Evaluate an expression at every stop (see 'help target stop-hook'.)
  down      -- Select a newer stack frame.  Defaults to moving one frame, a numeric argument can specify an arbitrary number.
  env       -- Shorthand for viewing and setting environment variables.
  exit      -- Quit the LLDB debugger.
  f         -- Select the current stack frame by index from within the current thread (see 'thread backtrace'.)
  file      -- Create a target using the argument as the main executable.
  finish    -- Finish executing the current stack frame and stop after returning.  Defaults to current thread unless specified.
  image     -- Commands for accessing information for one or more target modules.
  j         -- Set the program counter to a new address.
  jump      -- Set the program counter to a new address.
  kill      -- Terminate the current target process.
  l         -- List relevant source code using one of several shorthand formats.
  list      -- List relevant source code using one of several shorthand formats.
  n         -- Source level single step, stepping over calls.  Defaults to current thread unless specified.
  next      -- Source level single step, stepping over calls.  Defaults to current thread unless specified.
  nexti     -- Instruction level single step, stepping over calls.  Defaults to current thread unless specified.
  ni        -- Instruction level single step, stepping over calls.  Defaults to current thread unless specified.
  p         -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  parray    -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  po        -- Evaluate an expression on the current thread.  Displays any returned value with formatting controlled by the type's author.
  poarray   -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  print     -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  q         -- Quit the LLDB debugger.
  r         -- Launch the executable in the debugger.
  rbreak    -- Sets a breakpoint or set of breakpoints in the executable.
  repl      -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  run       -- Launch the executable in the debugger.
  s         -- Source level single step, stepping into calls.  Defaults to current thread unless specified.
  si        -- Instruction level single step, stepping into calls.  Defaults to current thread unless specified.
  sif       -- Step through the current block, stopping if you step directly into a function whose name matches the TargetFunctionName.
  step      -- Source level single step, stepping into calls.  Defaults to current thread unless specified.
  stepi     -- Instruction level single step, stepping into calls.  Defaults to current thread unless specified.
  t         -- Change the currently selected thread.
  tbreak    -- Set a one-shot breakpoint using one of several shorthand formats.
  undisplay -- Stop displaying expression at every stop (specified by stop-hook index.)
  up        -- Select an older stack frame.  Defaults to moving one frame, a numeric argument can specify an arbitrary number.
  x         -- Read from the memory of the current target process.
```



## Flex && Bison

### 资料

- bison官网：<https://www.gnu.org/software/bison/>
- flex下载：<http://gnuwin32.sourceforge.net/packages/flex.htm>

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

