

## 说明

- c++不同于Java，有非常多的细节需要专门注意，所以需要特意写个方案解决平时遇到的问题

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


## 思考
1. 为什么C/C++等少数编程语言要区分左右值？ - 腾讯技术工程的回答 - 知乎 https://www.zhihu.com/question/428340896/answer/2913419725

## C++解决方案

### 版本迭代
1. C++11/14/17/20/23新特性，哪些是必须掌握的，哪些基本用得不多？ - xiaokang的回答 - 知乎 https://www.zhihu.com/question/474664436/answer/3624228368
#### 11
```
auto 允许编译器推断变量类型，减少代码冗余

nullptr

std::vector<int> v1 = {1, 2, 3};
std::vector<int> v2 = std::move(v1); // 移动语义，避免拷贝

C++11 为我们提供了标准的线程支持（std::thread）和同步机制（std::mutex、std::condition_variable）

```

#### 14
```
auto lambda = [](auto x) { return x + x; };


推荐掌握。C++14 为我们提供了 std::make_unique，与 std::make_shared 类似，它是创建 unique_ptr 的最佳方式，避免手动管理 new 关键字。

```


#### 17
```
std::optional

std::pair<int, std::string> p = {1, "hello"};
auto [id, name] = p;  // 结构化绑定


std::variant 是一个类型安全的联合体，用来存储多个可能类型的值。配合 std::visit 使用，可以替代传统的 union，适用于需要存储不同类型数据的场景。

```



#### 20
```
Modules
Coroutines
concepts
ranges


```


#### 23
```
std::expected 、std::ranges::to
std::stacktrace

```



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
- 良好的编程习惯
  - 头文件只声明函数和类，源文件负责定义实现具体的类和函数，这样防止重复定义函数的问题，以及同一个变量，因为多个文件调用一个头文件的变量出现分别定义这个变量

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

## c++ 基础
### 指针

- 强弱应用：https://www.jianshu.com/p/4b047fc3b0be
- 多个***，代表什么意思：https://blog.csdn.net/soonfly/article/details/51131141
- 图解多级指针：https://www.cnblogs.com/chenyangyao/p/5222696.html
- 结构体指针：http://c.biancheng.net/cpp/html/94.html
- 类对象指针：https://www.cnblogs.com/flylong0204/p/4731318.html
- make_shared & shared_ptr：https://www.jianshu.com/p/4b047fc3b0be
- 只有指针或者引用可以达到多态。对象不行

```
===========================================================================
对象指针初始化
	Test* t1 = new Test();

    Student* s1; 
    s1 = new Student(); 

===========================================================================
make_shared shared_ptr
// make_shared 和 shared_ptr 设计初衷是引入引用计数这个概念来减少程序
// 员的工作量. 他的设计想法跟 Objective-c 的引用计数有点类似。请看以下代码: 

int main(int argc, const char * argv[])
{
    printf("----- start ----- \n");       
    std::shared_ptr<StructA> pA = std::make_shared<StructA>();
    std::shared_ptr<StructB> pB (new StructB());
    printf("----- end ----- \n");
    return 0;
}    

环形引用
环形应用: 就是对象 A 持有对象 B 的强引用, 对象 B 持有对象 A 的强应用,最终导致 A 和 B 都无法释放。
环形链表
// 解决方法, 其中一方使用弱引用
===========================================================================
weak_ptr

    weak_ptr 主要是用来判断 shared_ptr 所指向的数据内存是否存在, 因为make_shared 只作一次内存分配, shared_ptr 可以把这种内存分配分为两个步骤, weak_ptr 可以通过 lock 来判断 shared_ptr 所指向的数据内存是否被释放


===========================================================================

===========================================================================


===========================================================================

===========================================================================


===========================================================================

===========================================================================


===========================================================================
```

### 智能指针

- 参考资料：https://www.cnblogs.com/wxquare/p/4759020.html
- 文档：https://en.cppreference.com/w/cpp/memory/unique_ptr

```
// 共享指针        
        std::shared_ptr<int> ptra = std::make_shared<int>(a);
        std::shared_ptr<int> ptra2(ptra); //copy
        
        std::shared_ptr<class> table_info = 
                    std::make_shared<class>();
        
// unique_ptr
https://www.cnblogs.com/diysoul/p/5930388.html
        std::unique_ptr<int> uptr(new int(10));  //绑定动态对象
        //std::unique_ptr<int> uptr2 = uptr;  //不能賦值
        //std::unique_ptr<int> uptr2(uptr);  //不能拷貝
        std::unique_ptr<int> uptr2 = std::move(uptr); //轉換所有權
        uptr2.release(); //释放所有权
        
        // 指针间接赋值
        std::unique_ptr<tensorflow::Session>  session_;
        std::unique_ptr<tensorflow::Session> session(tensorflow::NewSession(tensorflow::SessionOptions()));
    session_ = std::move(session);
        
构造tensorflow的session
    tensorflow::SessionOptions options;
    std::unique_ptr<tensorflow::Session> session(tensorflow::NewSession(options));
    
智能指针不能直接复制！！！
必须用move
ptest2 = std::move(ptest)
    
unique_ptr 是一个独享所有权的智能指针，它提供了严格意义上的所有权，包括：

1、拥有它指向的对象

2、无法进行复制构造，无法进行复制赋值操作。即无法使两个unique_ptr指向同一个对象。但是可以进行移动构造和移动赋值操作

3、保存指向某个对象的指针，当它本身被删除释放的时候，会使用给定的删除器释放它指向的对象

unique_ptr 可以实现如下功能：

1、为动态申请的内存提供异常安全

2、讲动态申请的内存所有权传递给某函数

3、从某个函数返回动态申请内存的所有权

4、在容器中保存指针

5、auto_ptr 应该具有的功能



shared_ptr unique_ptr 区别非常大
shared_ptr可以正常赋值等     std::shared_ptr<ModelManager> model = std::make_shared<ModelManager>(config);

unique_ptr 要求非常多，很难用  std::unique_ptr<ModelManager> model(new ModelManager(config));

 智能指针与指针的转换
 https://www.cnblogs.com/fushi/p/7768906.html
std::shared_ptr<tensorflow::GraphDef> graph_def = std::make_shared<tensorflow::GraphDef>();
tensorflow::GraphDef* gg = graph_def.get();
get的以后原来的智能指针失效了！
```

#### 注意

```
c++没有空对象的说法，只有空指针
返回一个对象，就只能返回一个对象，不能返回指针
所以最好的方式，万物指针操作！可以内存不那么容易泄露，对象存活时间有保障

指针出了作用域也是会失效的！
如果想在函数内部的指针在外面也有效，需要用一个外面的函数专门创建这个对象，可以保证指针有效的
```



### 内存问题

```
c++的内存问题就好像无色无味的毒c++的内存问题就好像无色无味的毒的气
它在你的身边，但是你无法感受到，直到你的身体出现状况

构造函数的陷阱
std::string text = "2018年北京天安门";
StringUtil string_util(text);

StringUtil(std::string data) 
        : data_(data.c_str()) {}
data_是char*, 这个时候打印data_，会没有任何结果
而修改成 StringUtil(std::string& data) 
则可以打印出结果！

构造函数第二个陷阱
std::string text = "2018年北京天安门";
StringUtil string_util(text);
text = "xxxxxxxxxxxxxxxx";

StringUtil(std::string& data) 
        : data_(data.c_str()) {}
这个时候打印StringUtil里面的data，会打印xxxxxxxxxx
从这里可以发现，这个构造函数传递的是string的char*  地址，而并没有传递值
外部可以随意修改这部分内容！


为了保证StringUtil，可以正常打印，我们需要传递值！
正确做法
应该在类里面自己new一个新的string！


内存泄露
是指你在程序new一个内存空间，但是一直没有释放，一直也不使用。这就造成内存空间浪费
也可以说是内存泄露
```

### 异常

```
https://www.runoob.com/cplusplus/cpp-exceptions-handling.html

捕捉异常

try
{
   // 保护代码
}catch( ExceptionName e1 )
{
   // catch 块
}catch( ExceptionName e2 )
{
   // catch 块
}catch( ExceptionName eN )
{
   // catch 块
}

抛出异常

double division(int a, int b)
{
   if( b == 0 )
   {
      throw "Division by zero condition!";
   }
   return (a/b);
}

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

enum OpReqType {
  /*! \brief no operation, do not write anything */
  kNullOp,
  /*! \brief write gradient to provided space */
  kWriteTo,
  /*!
  * \brief perform an inplace write,
  * Target shares memory with one of input arguments.
  * This option only happen when
  */
  kWriteInplace,
  /*! \brief add to the provided space */
  kAddTo
};
```

### 宏使用

```
常见问题：https://www.cnblogs.com/fnlingnzb-learner/p/6903966.html
高级用法：https://www.cnblogs.com/sinferwu/articles/6902530.html


通过可变参数灵活设置日志输出：https://blog.csdn.net/bat67/article/details/77542165
gcc编译器特有的宏：__VA_ARGS__ ，用于可变参数



```



### 可变参数 ... 省略号

```
... 可以用来表示函数的参数个数是可变的


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

```
资料：https://blog.csdn.net/wenqian1991/article/details/29178649

// assignment function
    Slice(const Slice&) = default;
    Slice& operator=(const Slice&) = default;
    
如果没有上面两行，就会默认删除这些函数，这些对象无法再vector和map中操作
```



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

#### 打印数据类型

```
https://www.cnblogs.com/klobohyz/archive/2012/04/25/2470010.html

#include <typeinfo>
using namespace std;

int main()
{

   int iobj; 
 
   cout << typeid( iobj ).name() << endl;  //  打印: int 
   cout << typeid( 8.16 ).name() << endl; // 打印: double
   
   return 0;
}

#include <type_info> 

using namespace std;
 
int main()
{
   employee *pe = new manager; 
   employee& re = *pe; 
 
   if ( typeid( pe ) == typeid( employee* ) )  // true 
     // do something 
   return 0;
}
```

#### 内部类

```
类里面定义新的类

#include<iostream> 

using namespace std; 

/* start of Enclosing class declaration */
class Enclosing {	 
private: 
	int x; 
	
/* start of Nested class declaration */
class Nested { 
	int y; 
	void NestedFun(Enclosing *e) { 
		cout<<e->x; // works fine: nested class can access 
					// private members of Enclosing class 
	}	 
}; // declaration Nested class ends here 
}; // declaration Enclosing class ends here 

int main() 
{	 

} 

```

#### 注意

```
对象是否需要复制，赋值。如果不需要改成指针形式传递
```



### Map使用

- 参考文档：http://www.cplusplus.com/reference/map/map/

- 在多重map中，需要用make_pair进行封装，然后在插入数据

  - 比如key也是map,value也是map
  - 那么key 也要make_pair， value也要make_pair

- Map.find（key)。返回的是迭代器
  - 在迭代器的基础上，iter->second。就可以返回value

  - iter->first 就是返回key

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
- 需要->first 或者 ->second来获取key和value
  
- 迭代

  - const auto& iter: map

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

```
遍历map
    for (auto& e : map) {
        std::cout << e.first << e.second << std::endl;
    }
    
    



```

#### 高级用法

```
初始化列表
https://blog.csdn.net/wangshubo1989/article/details/50001185
std::map<int, string> int_to_string = {
{1, "what"},
{2, "a"},
{3, "fuck"},
{4, "day"},
....
};
```



### unordered_map使用

- 哈希map，查找速度更快，常数级别
- 显然，hash算法不能兼容有序的特点
- 类似Java中的HashMap
- 参考文档：
  - http://www.cplusplus.com/reference/unordered_map/
  - https://en.cppreference.com/w/cpp/container/unordered_map
- 基本操作
- 和map基本一致



```
// unordered_map::cbegin/cend example
#include <iostream>
#include <unordered_map>

int main ()
{
  std::unordered_map<std::string,std::string> mymap;
  mymap = {{"Australia","Canberra"},{"U.S.","Washington"},{"France","Paris"}};

  std::cout << "mymap contains:";
  for ( auto it = mymap.cbegin(); it != mymap.cend(); ++it )
    std::cout << " " << it->first << ":" << it->second;  // cannot modify *it
  std::cout << std::endl;

  std::cout << "mymap's buckets contain:\n";
  for ( unsigned i = 0; i < mymap.bucket_count(); ++i) {
    std::cout << "bucket #" << i << " contains:";
    for ( auto local_it = mymap.cbegin(i); local_it!= mymap.cend(i); ++local_it )
      std::cout << " " << local_it->first << ":" << local_it->second;
    std::cout << std::endl;
    }
  return 0;
}
```



### list使用

```
双向链表，常数级别的插入数据
但是！！！
不支持随机访问！！！！！！！！
一定注意这个性质，不同场景不同需求


begin() 	返回指向容器中第一个元素的双向迭代器。
end() 	返回指向容器中最后一个元素所在位置的下一个位置的双向迭代器。
rbegin() 	返回指向最后一个元素的反向双向迭代器。
rend() 	返回指向第一个元素所在位置前一个位置的反向双向迭代器。
cbegin() 	和 begin() 功能相同，只不过在其基础上，增加了 const 属性，不能用于修改元素。
cend() 	和 end() 功能相同，只不过在其基础上，增加了 const 属性，不能用于修改元素。
crbegin()  	和 rbegin() 功能相同，只不过在其基础上，增加了 const 属性，不能用于修改元素。
crend() 	和 rend() 功能相同，只不过在其基础上，增加了 const 属性，不能用于修改元素。
empty() 	判断容器中是否有元素，若无元素，则返回 true；反之，返回 false。
size() 	返回当前容器实际包含的元素个数。
max_size() 	返回容器所能包含元素个数的最大值。这通常是一个很大的值，一般是 232-1，所以我们很少会用到这个函数。
front() 	返回第一个元素的引用。
back() 	返回最后一个元素的引用。
assign() 	用新元素替换容器中原有内容。
emplace_front() 	在容器头部生成一个元素。该函数和 push_front() 的功能相同，但效率更高。
push_front() 	在容器头部插入一个元素。
pop_front() 	删除容器头部的一个元素。
emplace_back() 	在容器尾部直接生成一个元素。该函数和 push_back() 的功能相同，但效率更高。
push_back() 	在容器尾部插入一个元素。
pop_back() 	删除容器尾部的一个元素。
emplace() 	在容器中的指定位置插入元素。该函数和 insert() 功能相同，但效率更高。
insert()  	在容器中的指定位置插入元素。
erase() 	删除容器中一个或某区域内的元素。
swap() 	交换两个容器中的元素，必须保证这两个容器中存储的元素类型是相同的。
resize() 	调整容器的大小。
clear() 	删除容器存储的所有元素。
splice() 	将一个 list 容器中的元素插入到另一个容器的指定位置。
remove(val) 	删除容器中所有等于 val 的元素。
remove_if() 	删除容器中满足条件的元素。
unique() 	删除容器中相邻的重复元素，只保留一个。
merge() 	合并两个事先已排好序的 list 容器，并且合并之后的 list 容器依然是有序的。
sort() 	通过更改容器中元素的位置，将它们进行排序。
reverse() 	反转容器中元素的顺序。
```

### stack

```
https://www.cplusplus.com/reference/stack/stack/
#include <stack>          // std::stack

empty
    Test whether container is empty (public member function )

size
    Return size (public member function )

top
    Access next element (public member function )

push
    Insert element (public member function )

emplace
    Construct and insert element (public member function )

pop
    Remove top element (public member function )

swap
    Swap contents (public member function )
    
   
```



### vector使用

- 参考文档：http://www.cplusplus.com/reference/vector/vector/
- 常用函数

```
reserve(number) 提前开辟vector空间，可以减少后面自动增长的开销
clear() 清除所有的元素
push_back(element) 往最后一个位置插入元素
erase(index) 删除第index个位置的元素
pop_back() 删除最后一个元素
push_back(element) 添加元素到最后

取对象
xxx[i] 即可

容器初始化
std::vector<double> values;
values.reserve(20);

20个元素初始化为99
std::vector<long> numbers(20, 99L);
```

```
两个vector合并

https://blog.csdn.net/cau_eric/article/details/26011627

vector<string>vec1,vec2,vec3;
		//... vec1,vec2赋值
		vec3.insert(vec3.end(),vec1.begin(),vec1.end());
		vec3.insert(vec3.end(),vec2.begin(),vec2.end());

```

```
vector指针的使用

std::vector<llvm::Value*>* args

new 和 取地址符 在函数传递的区别



insert用法
    #include <iostream> 
    #include <vector> 
    #include <array> 
    using namespace std;
    int main()
    {
        std::vector<int> demo{1,2};
        //第一种格式用法
        demo.insert(demo.begin() + 1, 3);//{1,3,2}
        //第二种格式用法
        demo.insert(demo.end(), 2, 5);//{1,3,2,5,5}
        //第三种格式用法
        std::array<int,3>test{ 7,8,9 };
        demo.insert(demo.end(), test.begin(), test.end());//{1,3,2,5,5,7,8,9}
        //第四种格式用法
        demo.insert(demo.end(), { 10,11 });//{1,3,2,5,5,7,8,9,10,11}
        for (int i = 0; i < demo.size(); i++) {
            cout << demo[i] << " ";
        }
        return 0;
    }
```

#### 高级用法

```
初始化
std::vector<std::pair<std::string, Tensor>> input = {
        {"Input", tensor},
    };
std::vector v = { 1, 2, 3, 4 };
```



### string使用

- 参考文档
  - http://www.cplusplus.com/reference/string/string/
  - https://en.cppreference.com/w/cpp/string/basic_string
  - 字符串更多功能可以看boost
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

从0开始，选3个字符。注意不是0 到 3！！！！
xx.substr(0,3);

字符串长度
int n = s.size();

往第一个位置插入字符1
result.insert((result.begin(), '1');

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
  - 从0开始，选3个字符
  - 注意不是0 到 3！！！！！
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

#### 高级用法

```
字符串切割
https://www.cnblogs.com/dfcao/p/cpp-FAQ-split.html

// s是源字符串，v是切割后的结果，c是切割符号
void SplitString(const std::string& s, std::vector<std::string>& v, const std::string& c)
{
  std::string::size_type pos1, pos2;
  pos2 = s.find(c);
  pos1 = 0;
  while(std::string::npos != pos2)
  {
    v.push_back(s.substr(pos1, pos2-pos1));
 
    pos1 = pos2 + c.size();
    pos2 = s.find(c, pos1);
  }
  if(pos1 != s.length())
    v.push_back(s.substr(pos1));
}


字符串遍历
一个一个字母遍历，只需要用数组形式即可
https://blog.csdn.net/stpeace/article/details/50406627
s[i]

汉字字符串遍历
上面仅限于英文遍历，不适用汉字！！！


轻量级utf8编解码
https://stackoverflow.com/questions/6140223/c-boost-encode-decode-utf-8?lq=1


字符串是否包含另一个字符串
find_last_of 
find
find_first_of
if判断 dict_path.find("stopWord") != std::string::npos

find_last_of这个函数有bug，一直没有返回过npos，不要用！

字符串和数字的转换
https://www.jianshu.com/p/60e05c02ea9e
stod()//字符串转double
stof()//字符串转float
stoi()//字符串转int
stol()//字符串转long
stold()//字符串转double
stoll()//字符串转long long
stoul()//字符串转unsigned long
stoull()//字符串转unsinged long long
//注意！没有unsigned double和unsigned float！！！
//没有 (unsigned+浮点数) 这种类型！！！
//下面用stoi举例，其它类似

//次函数的参数可以传任何数字类型
//int, unsigned int, long, unsigned long, long long, unsigned long long
//float, double
string to_string(待转换数字)

原始字符串 R
https://www.cnblogs.com/lidabo/p/7151951.html

// 一个普通的字符串，'\n'被当作是转义字符，表示一个换行符。
std::string normal_str = "First line.\nSecond line.\nEnd of message.\n";

// 一个raw string，'\'不会被转义处理。因此，"\n"表示两个字符：字符反斜杠 和 字母n。
std::string raw_str = R"(First line.\nSecond line.\nEnd of message.\n)";

```

### queue

```
http://c.biancheng.net/view/479.html

priority_queue<int,vector,greater> q;最小堆
 priority_queue<int,vector,less> q;最大堆（默认为最大堆）

对 priority_queue 进行操作有一些限制：

    push(const T& obj)：将obj的副本放到容器的适当位置，这通常会包含一个排序操作。
    push(T&& obj)：将obj放到容器的适当位置，这通常会包含一个排序操作。
    emplace(T constructor a rgs...)：通过调用传入参数的构造函数，在序列的适当位置构造一个T对象。为了维持优先顺序，通常需要一个排序操作。
    top()：返回优先级队列中第一个元素的引用。
    pop()：移除第一个元素。
    size()：返回队列中元素的个数。
    empty()：如果队列为空的话，返回true。
    swap(priority_queue<T>& other)：和参数的元素进行交换，所包含对象的类型必须相同。



优先队列使用，找中位数
#include <queue>
class MedianFinder {
    priority_queue<int> lo;                              // max heap
    priority_queue<int, vector<int>, greater<int>> hi;   // min heap

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        lo.push(num);                                    // Add to max heap

        hi.push(lo.top());                               // balancing step
        lo.pop();

        if (lo.size() < hi.size()) {                     // maintain size property
            lo.push(hi.top());
            hi.pop();
        }
    }

    // Returns the median of current data stream
    double findMedian()
    {
        return lo.size() > hi.size() ? (double) lo.top() : (lo.top() + hi.top()) * 0.5;
    }
};

```



### wstring

- 文档：http://www.cplusplus.com/reference/string/wstring/
- 简单用法：https://codeday.me/bug/20180108/115942.html

```
定义wstring
std::wstring st = L"SomeText"; // Notice the "L"

打印wstring
std::wcout << st; 

wstring word为单位的字符串
http://www.cplusplus.com/reference/string/wstring/

wstring和string转化
https://blog.csdn.net/hongxingabc/article/details/82846396

int,double等类型转换wstring
http://www.cplusplus.com/reference/string/to_wstring/
std::
wstring to_wstring (int val);
wstring to_wstring (long val);
wstring to_wstring (long long val);
wstring to_wstring (unsigned val);
wstring to_wstring (unsigned long val);
wstring to_wstring (unsigned long long val);
wstring to_wstring (float val);
wstring to_wstring (double val);
wstring to_wstring (long double val);

string 和 wstring 对比
https://stackoverflow.com/questions/402283/stdwstring-vs-stdstring

实用耳鼻咽喉头颈外科学（第2版） 
```



### char* 使用

- 拷贝函数
  - memcpy(void *dest, const void *src, size_t n) 
  - 从源src所指的内存地址的起始位置开始拷贝n个字节到目标dest所指的内存地址的起始位置中
  - source和destin都不一定是数组，任意的可读写的空间均可
- char* test = new char[size];
- 字符串拼接
  - https://baike.baidu.com/item/strcat
  - char *strcat(char *dest, const char *src);

```

```



### set使用

- 参考文档
  - http://www.cplusplus.com/reference/set/set/
- 头文件 #include < set >

```
insert

find

erase

简单使用 求最长连续子序列，用set维护结果
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        int res = 0;
        for (int e : nums) {
            s.insert(e);
        }
        for (const int& num : s) {
            if (s.count(num) == 1) {
                int begin = num;
                int cnt = 1;
                while (s.count(begin + 1) != 0) {
                    begin++;
                    cnt++;
                }
                res = max(cnt, res);
            }
        }
        return res;
    }
};



```



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

### noexcept

```
使用说明：https://www.cnblogs.com/sword03/p/10020344.html

constexpr initializer_list() noexcept
      : _M_array(0), _M_len(0) { }

该关键字告诉编译器，函数中不会发生异常,这有利于编译器对程序做更多的优化。
如果在运行时，noexecpt函数向外抛出了异常（如果函数内部捕捉了异常并完成处理，这种情况不算抛出异常），程序会直接终止，调用std::terminate()函数，该函数内部会调用std::abort()终止程序。

```

### __builtin_expect

```
使用说明：https://www.jianshu.com/p/2684613a300f

这个指令是gcc引入的，作用是允许程序员将最有可能执行的分支告诉编译器。这个指令的写法为：__builtin_expect(EXP, N)。
意思是：EXP==N的概率很大。

内核里面的宏
#define likely(x) __builtin_expect(!!(x), 1) //x很可能为真       
#define unlikely(x) __builtin_expect(!!(x), 0) //x很可能为假

调用代码
int x, y;
 if(unlikely(x > 0))
    y = 1; 
else 
    y = -1;

```



### using使用

```
https://blog.csdn.net/shift_wwx/article/details/78742459

命名空间
using namespace android;

引用基类
using T5Base::test1

可以起到别名的作用
很方便的就知道是创建了一个函数和指针
using FP = void (*) (int, const std::string&);
using arrow_schema_ptr = std::shared_ptr<arrow::Schema>;
```



### 函数中的参数

- 默认参数和缺省参数：https://blog.csdn.net/CHF_VIP/article/details/8586921
- 初始化的参数，可以可以赋值也可以不赋值
- 参数一般都是默认传值。传值的意思就是，传递参数会复制一个新对象到函数内部。尤其传递一个对象时，会显得十分耗时。而且是函数内部的修改该值的时候，是不会影响实际参数的值。
- 传引用的就是传地址的值！而不是对象内部数据的值！
- 传对象的值到函数里面，会发生构造一次对象，析构一次对象消耗。而且这是没有考虑到对象中可能还含有其他对象的情况，那么消耗将会更加多。
- 规范：输入参数在前，输出结果在后




### 编程常用函数

```

prev()和next()函数用法详解
#include <iostream>     // std::cout
#include <iterator>     // std::next
#include <list>         // std::list

http://c.biancheng.net/view/7384.html
prev 原意为“上一个”，但 prev() 的功能远比它的本意大得多，该函数可用来获取一个距离指定迭代器 n 个元素的迭代器。

和 prev 相反，next 原意为“下一个”，但其功能和 prev() 函数类似，即用来获取一个距离指定迭代器 n 个元素的迭代器。


#include <ctype.h>
C 库函数 void isalnum(int c) 检查所传的字符是否是字母和数字。

fill_n()
  std::vector<int> myvector (8,10);        // myvector: 10 10 10 10 10 10 10 10
  std::fill_n (myvector.begin(),4,20);     // myvector: 20 20 20 20 10 10 10 10
  std::fill_n (myvector.begin()+3,3,33);   // myvector: 20 20 20 33 33 33 10 10
OutputIterator fill_n (OutputIterator first, Size n, const T& val);
Assigns val to the first n elements of the sequence pointed by first.


strtod
#include <stdio.h>
#include <stdlib.h>
double strtod(const char *str, char **endptr)
Parameters

    str − This is the value to be converted to a string.

    endptr − This is the reference to an already allocated object of type char*, whose value is set by the function to the next character in str after the numerical value.

int main () { 
   char str[30] = "20.30300 This is test";
   char *ptr;
   double ret;

   ret = strtod(str, &ptr);
   printf("The number(double) is %lf\n", ret);
   printf("String part is |%s|", ptr);

   return(0);
}


isspace
https://www.runoob.com/cprogramming/c-function-isspace.html
' '     (0x20)    space (SPC) 空格符
'\t'    (0x09)    horizontal tab (TAB) 水平制表符    
'\n'    (0x0a)    newline (LF) 换行符
'\v'    (0x0b)    vertical tab (VT) 垂直制表符
'\f'    (0x0c)    feed (FF) 换页符
'\r'    (0x0d)    carriage return (CR) 回车符
int isspace(int c);
参数

    c -- 这是要检查的字符。

返回值

如果 c 是一个空白字符，则该函数返回非零值（true），否则返回 0（false）。


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

#### close函数

```
http://c.biancheng.net/cpp/html/229.html

#include <unistd.h>
int close(int fd);
函数说明：当使用完文件后若已不再需要则可使用 close()关闭该文件, 二close()会让数据写回磁盘, 并释放该文件所占用的资源. 参数fd 为先前由open()或creat()所返回的文件描述词.

返回值：若文件顺利关闭则返回0, 发生错误时返回-1.
```

#### ifstream

```
https://www.cnblogs.com/azraelly/archive/2012/04/14/2446914.html

#include <fiostream.h>
```



#### getline函数

```
http://www.cplusplus.com/reference/istream/istream/getline/
http://c.biancheng.net/cpp/biancheng/view/2232.html

一行一行的读取文件

// istream::getline example
#include <iostream>     // std::cin, std::cout

int main () {
  char name[256], title[256];

  std::cout << "Please, enter your name: ";
  std::cin.getline (name,256);

  std::cout << "Please, enter your favourite movie: ";
  std::cin.getline (title,256);

  std::cout << name << "'s favourite movie is " << title;

  return 0;
}


    #include <iostream>
    using namespace std;
    int main( )
    {
       char ch[20];
       cout<<"enter a sentence:"<<endl;
       cin>>ch;
       cout<<"The string read with cin is:"<<ch<<endl;
       cin.getline(ch,20,'/');  //读个字符或遇'/'结束
       cout<<"The second part is:"<<ch<<endl;
       cin.getline(ch,20);  //读个字符或遇'/n'结束
       cout<<"The third part is:"<<ch<<endl;
       return 0;
    }
```



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

#### 流式状态
  ```
https://blog.csdn.net/yangbomoto/article/details/80782633

badbit, failbit, eofbit
1. badbit表示发生系统级的错误，如不可恢复的读写错误。通常情况下一旦badbit被置位，流就无法再使用了。

2. failbit 表示发生可恢复的错误，如期望读取一个数值，却读出一个字符等错误。这种问题通常是可以修改的，流还可以继续使用。

3. 当到达文件的结束位置时，eofbit 和 failbit 都会被置位。

4. goodbit 被置位表示流未发生错误。如果badbit failbit 和eofbit 任何一个被置位，则检查流状态的条件会失败。

对应的bad(), fail(), eof(), good()能检查对应位是否被置位，返回1表示被置位。但是，badbit被置位时，fail()也会返回1。所以使用good()和fail()是确定流能否使用的正确方法。。实际上，流当做条件使用的代码就等价于！fail()。而且eof() 和bad() 操作只能表示特定的错误。
————————————————
版权声明：本文为CSDN博主「嘿碳头」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yangbomoto/article/details/80782633

  ```

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

```
文件流形式读数据
http://www.cplusplus.com/reference/fstream/ifstream/
/ print the content of a text file.
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream

int main () {
  std::ifstream ifs;

  ifs.open ("test.txt", std::ifstream::in);

  char c = ifs.get();

  while (ifs.good()) {
    std::cout << c;
    c = ifs.get();
  }

  ifs.close();

  return 0;
}
```



#### fstream

- Stream class to both read and write from/to files.


#### istream
```
读取Shape结构体流式处理

inline std::istream &operator>>(std::istream &is, Shape &shape) {
  // get (
  while (true) {
    char ch = is.get();
    if (ch == '(') break;
    if (!isspace(ch)) {
      is.setstate(std::ios::failbit);
      return is;
    }
  }
  index_t idx;
  std::vector<index_t> tmp;
  while (is >> idx) {
    tmp.push_back(idx);
    char ch;
    do {
      ch = is.get();
    } while (isspace(ch));
    if (ch == ',') {
      while (true) {
        ch = is.peek();
        if (isspace(ch)) {
          is.get(); continue;
        }
        if (ch == ')') {
          is.get(); break;
        }
        break;
      }
      if (ch == ')') break;
    } else if (ch == ')') {
      break;
    } else {
      is.setstate(std::ios::failbit);
      return is;
    }
  }
  shape.CopyFrom(tmp.begin(), tmp.end());
  return is;
}
```

#### ostream
```
打印Shape结构体为字符串

inline std::ostream &operator<<(std::ostream &os, const Shape &shape) {
  os << '(';
  for (index_t i = 0; i < shape.ndim(); ++i) {
    if (i != 0) os << ',';
    os << static_cast<int>(shape[i]);  // Supports negative Shape 'special codes' for inferring
  }
  // python style tuple
  if (shape.ndim() == 1) os << ',';
  os << ')';
  return os;
}

```

#### stringstream
```
    std::string value_str;
    std::stringstream ss;
    ss << value; 读数据
    ss >> value_str; 写数据 赋值

　　%% 印出百分比符号，不转换。
　　%c 整数转成对应的 ASCII 字元。
　　%d 整数转成十进位。
　　%f 倍精确度数字转成浮点数。
　　%o 整数转成八进位。
　　%s 整数转成字符串。
　　%x 整数转成小写十六进位。
　　%X 整数转成大写十六进位。
　　%n sscanf(str, "%d%n", &dig, &n)，%n表示一共转换了多少位的字符

```

#### std::ostringstream

```
字符串输出流
http://www.cplusplus.com/reference/sstream/ostringstream/

Objects of this class use a string buffer that contains a sequence of characters. This sequence of characters can be accessed directly as a string object, using member str.

std::ostringstream oss;
    oss << "print schema\n";
    for (int i = 0; i < schema.size(); i++) {
        oss << schema.get(i).name() << ":";
        if (i + 1 != schema.size()) {
            oss << ", ";
        }
    }
    std::cout << oss.str();
```

#### std::fpos_t

```
https://en.cppreference.com/w/cpp/io/c/fpos_t

std::fpos_t pos;
fgetpos(&*_file, &pos) == 0
fseek(&*_file, -len, SEEK_END) == 0
fsetpos(&*_file, &pos) == 0
```

#### std::fpos

```
https://en.cppreference.com/w/cpp/io/fpos

```



#### 文件流终止

```
https://www.bbsmax.com/A/RnJWpVay5q/
fin.eof() 可以判断结尾结束
```



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

### 网络请求

```
boost/asio.hpp

boost/asio/streambuf.hpp
```



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

### 模板

类型判断is_same

```
std::is_same和std::decay
https://blog.csdn.net/czyt1988/article/details/52812797

std::cout << std::is_same<int, int32_t>::value << '\n';   // true
std::cout << std::is_same<int, int64_t>::value << '\n';   // false
```



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
## c++ 性能
### 性能优化

- insert 对象的时候，其实是复制了一个对象，要想优化，最后insert一个指针或者引用
- 上面这一行是错误的！！！！！！
- 不能insert指针或者引用！！！！！！
- 不能insert指针或者引用！！！！！！
- 不能insert指针或者引用！！！！！！
- 这会在STL中因为赋值操作，导致指针失效！！！

### 实现Java的synchronized机制

```
代码：https://www.codeproject.com/Articles/12362/A-quot-synchronized-quot-statement-for-C-like-in-J
```




### 并发

#### 教程

- 共享数据：https://baptiste-wicht.com/posts/2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data.html


## c++ 关键词
### ifndef 用法

```
防止头文件重复编译

#ifndef LLVM_IR_IRBUILDER_H
#define LLVM_IR_IRBUILDER_H

#endif // LLVM_IR_IRBUILDER_H


注意即使你用了，仍然可能会报重复定义
multiple definition of `LogError(char const*)'

因为#ifndef只能保证重复包含时，只包含一次。但在不同的C文件是分别进行编译的，所以另一个C语言里的#define对另一个C文件不起作用。也就是说正确的作法应该这样：

1）在头文件里只声明不定义
2）把定义定义在C文件里

注意
如果非要在头文件定义函数，建议添加static
```

### inline 用法

- 可以在任意函数前面加inline
- 它的作用只是在调用该函数的时候，直接张开函数里面的内容，而不是真正的用栈调用
- 减少函数切换的开销
```
比如 pytorch 函数接口大量使用inline

inline Tensor feature_alpha_dropout(
    Tensor input,
    double p,
    bool training,
    bool inplace) {
  if (p < 0. || p > 1.) {
    TORCH_CHECK(
        false, "dropout probability has to be between 0 and 1, but got ", p);
  }
  return inplace ? torch::feature_alpha_dropout_(input, p, training)
                 : torch::feature_alpha_dropout(input, p, training);
}

```
### define 用法
```
===================================================================================
#if defined(__cpp_lib_logical_traits) && !(defined(_MSC_VER) && _MSC_VER < 1920)


===================================================================================
__HIP_PLATFORM_HCC__
CUDA_HOST_DEVICE



===================================================================================
pytorch定义 多个dropout函数类型

#define ALIAS_SPECIALIZATION(ALIAS_NAME, IS_FEATURE, IS_ALPHA)                      \
template <bool inplace, typename... Args>                                           \
Ctype<inplace> ALIAS_NAME(Args&&... args) {                                         \
  return _dropout_impl<IS_FEATURE, IS_ALPHA, inplace>(std::forward<Args>(args)...); \
}

ALIAS_SPECIALIZATION(_dropout,               false, false)
ALIAS_SPECIALIZATION(_feature_dropout,       true,  false)
ALIAS_SPECIALIZATION(_alpha_dropout,         false, true )
ALIAS_SPECIALIZATION(_feature_alpha_dropout, true,  true )


===================================================================================


```
### 函数定义和声明
```
定义只能有一次，而声明可以用多次

定义就是完整把一个变量或者函数具体形式，写出来
比如
static int64_t Discrete(int value) {
    std::cout << "int Discrete (" << value << ")" << std::endl;
    std::string value_name = std::to_string(value);
    return hash64(value_name);
}

而声明只需要写出变量名字或者函数
比如
static int64_t Discrete(int value) ;
```



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

```
https://baike.baidu.com/item/dynamic_cast

dynamic_cast运算符可以在执行期决定真正的类型。如果 downcast 是安全的（也就说，如果基类指针或者引用确实指向一个派生类对象）这个运算符会传回适当转型过的指针。如果 downcast 不安全，这个运算符会传回空指针（也就是说，基类指针或者引用没有指向一个派生类对象）
```



### delete 和 default函数

- c++11 的新特性
- 主要用来修饰构造函数，赋值函数，析构函数
- delete表示禁止编译器自动生成这些函数
- default表示默认使用编译器的函数
- 用法
  - Arena() = delete;
  - void operator=() = default;

## STD标准库函数

```c++
列表复制
std::vector<int> features;
std::vector<int> new_features;
std::copy(features.begin(), features.end(),new_features.HostVector().begin());
std::shuffle(new_features.HostVector().begin(),new_features.HostVector().end(), rng_);
std::sort(new_features.HostVector().begin(),new_features.HostVector().end());


std::transform
std::back_inserter

```



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

### std::move

- 官方文档：<https://en.cppreference.com/w/cpp/utility/move>
- move本质上把对象值掏空给另外一个值引用：<https://blog.csdn.net/p942005405/article/details/84644069>

```
作用：将左值引用转换为右值引用，中间没有值拷贝，所以非常高效

仔细观察下面代码的str

	string str = "Hello";
    std::vector<std::string> v;
    
    v.push_back(str);
    std::cout << "After copy, str is \"" << str << "\"\n";
    
    v.push_back(std::move(str));
    std::cout << "After move, str is \"" << str << "\"\n";
    
    std::cout << "The contents of the vector are \"" << v[0]
                                         << "\", \"" << v[1] << "\"\n";


结果：move掏空str里面的值
After copy, str is "Hello"
After move, str is ""
The contents of the vector are "Hello", "Hello"


```

### std::copy_n

```

```

### std::mt19937

```
/*!
 * \brief Define mt19937 as default type Random Engine.
 */
using RandomEngine = std::mt19937;
RandomEngine rng_; 
rng_.seed(seed);
```

### std::clock()

```
#include <ctime>

返回当前时间
```
### std::partial_sum

```
计算序列部分和
std::partial_sum
http://c.biancheng.net/view/686.html

std::vector<int> data {2, 3, 5, 7, 11, 13, 17, 19};
std::cout << "Partial sums: ";
std::partial_sum(std::begin(data), std::end(data),std::ostream_iterator<int>{std::cout, " "});
std::cout << std::endl; // Partial sums: 2 5 10 17 28 41 58 77

```
### std::stable_sort
```
http://c.biancheng.net/view/563.html
std::stable_sort(std::begin(names), std::end(names),[](const Name& name1, const Name& name2) { return name1.get_second() < name2.get_second(); });


https://www.cnblogs.com/xenny/p/9404758.html
其实你会发现不仅仅sort有stable_sort，partition也有stable_partition，我们都知道sort是一个不稳定的排序，但stable_sort就是如字面意思一样，是一个稳定的sort排序，那么你可能有疑问，排序后，相同的元素会在一起，稳定不稳定不都是一样的么，如果你存在这个疑问的话，那就肯定还是做题力度不够=7=，你只想到了对元素表面的排序，如果是对元素的某种性质排序呢
string s[4] = {"spring","lip","eye","winter"};

bool cmp(string a, string b){
    return a.size() < b.size();
}

sort(s,s+4,cmp);


只对元素的size比较，而不是元素字母

```

### std::iota
```
http://c.biancheng.net/view/681.html
定义在 numeric 头文件中的 iota() 函数模板会用连续的 T 类型值填充序列。前两个参数是定义序列的正向迭代器，第三个参数是初始的 T 值。第三个指定的值会被保存到序列的第一个元素中。保存在第一个元素后的值是通过对前面的值运用自增运算符得到的。当然，这意味着 T 类型必须支持 operator++()。下面展示了如何生成一个有连续的浮点值元素的 vector 容器：
std::vector<double> data(9);
double initial {-4};
std::iota (std::begin (data) , std::end (data) , initial);
std::copy(std::begin(data), std::end(data),std::ostream_iterator<double>{std::cout<< std::fixed << std::setprecision(1), " "});
std::cout << std::endl;  // -4.0 -3.0 -2.0 -1.0 0.0 1.0 2.0 3.0 4.0

更直接用法
    std::vector<int64> perm(9);
    std::iota(perm.begin(), perm.end(), -4.0);

```

### std::bind

```
https://www.jianshu.com/p/f191e88dcc80

可将std::bind函数看作一个通用的函数适配器，它接受一个可调用对象，生成一个新的可调用对象来“适应”原对象的参数列表。

std::bind将可调用对象与其参数一起进行绑定，绑定后的结果可以使用std::function保存。std::bind主要有以下两个作用：

    将可调用对象和其参数绑定成一个防函数；
    只绑定部分参数，减少可调用对象传入的参数。

double my_divide (double x, double y) {return x/y;}
auto fn_half = std::bind (my_divide,_1,2);  
std::cout << fn_half(10) << '\n';                        // 5



```

### std::exception

```
异常类

```



### std::getenv
```
文档：https://en.cppreference.com/w/cpp/utility/program/getenv
头文件：#include <cstdlib>


#include <iostream>
#include <cstdlib>
 
int main()
{
    if(const char* env_p = std::getenv("PATH"))
        std::cout << "Your PATH is: " << env_p << '\n';
}
```

### std::function

```
基本使用：https://www.jianshu.com/p/f191e88dcc80
std::function<void(boost::asio::streambuf&)> prep_request_func

std::function 是一个可调用对象包装器，是一个类模板，可以容纳除了类成员函数指针之外的所有可调用对象，它可以用统一的方式处理函数、函数对象、函数指针，并允许保存和延迟它们的执行。
定义格式：std::function<函数类型>。
std::function可以取代函数指针的作用，因为它可以延迟函数的执行，特别适合作为回调函数使用。它比普通函数指针更加的灵活和便利。


```

### std::ref

```
文档：http://www.cplusplus.com/reference/functional/ref/

```

### std::type_index

```
基本使用：https://blog.csdn.net/audi2/article/details/104014908

typeid运算符，返回类型信息const std::type_info&。这种类型是不能赋值的。例如：

    const std::typeinfo& a = typeid(int);  //初始化可以
    a = typeid(double);  //再赋值就是错误

为了解决这个问题，C++引入了std::type_index类。这个类可以理解为封装了一个指向typeinfo的指针。理论上，std::type_index是值语义的。例如：

    std::type_index a = typeid(int);  //实际是调用构造函数 std::type_index(typeid(int));
    std::type_index b = a;
    assert(a==b); //a,b都指向同一个type_info
    b=typeid(double);   //重新赋值
    assert(a!=b);  //a,b不再相同，a不受影响，仍指向int的type_info
    std::cout <<a.name();   //实际调用的是底层type_info::name()函数

这样就可以把type_index对象当做普通值（像int，std::string）一样放到容器里，或者放到类中当做普通数据成员。
```




### union

```

```

### decltype

```
https://www.cnblogs.com/QG-whz/p/4952980.html
 int i = 4;
 decltype(i) a; //推导结果为int。a的类型为int。
    
    vector<int >vec;
    typedef decltype(vec.begin()) vectype;
    for (vectype i = vec.begin; i != vec.end(); i++)
    {
    //...
    }
   
   

如果e是一个没有带括号的标记符表达式或者类成员访问表达式，那么的decltype（e）就是e所命名的实体的类型。此外，如果e是一个被重载的函数，则会导致编译错误。
否则 ，假设e的类型是T，如果e是一个将亡值，那么decltype（e）为T&&
否则，假设e的类型是T，如果e是一个左值，那么decltype（e）为T&。
否则，假设e的类型是T，则decltype（e）为T。

```

### std::enable_if_t

```
文档：https://en.cppreference.com/w/cpp/types/enable_if

https://www.jianshu.com/p/a961c35910d2

SFINAE是英文Substitution failure is not an error的缩写，意思是匹配失败不是错误
```

### 少见复杂的std函数

```
===================================================================================
std::is_constructible 
Trait class that identifies whether T is a constructible type with the set of argument types specified by Arg.
For this class, a constructible type is a type that can be constructed using a particular set of arguments.
is_constructible inherits from integral_constant as being either true_type or false_type, depending on whether T is constructible with the list of arguments Args.

===================================================================================
std::is_same


===================================================================================
std::swap



===================================================================================
std::is_array



===================================================================================
std::is_base_of




===================================================================================
std::enable_if




===================================================================================
std::forward


===================================================================================
std::conjunction
https://en.cppreference.com/w/cpp/types/conjunction

#include <iostream>
#include <type_traits>
 
// func is enabled if all Ts... have the same type as T
template<typename T, typename... Ts>
std::enable_if_t<std::conjunction_v<std::is_same<T, Ts>...>>
func(T, Ts...) {
    std::cout << "all types in pack are T\n";
}
 
// otherwise
template<typename T, typename... Ts>
std::enable_if_t<!std::conjunction_v<std::is_same<T, Ts>...>>
func(T, Ts...) {
    std::cout << "not all types in pack are T\n";
}
 
int main() {
    func(1, 2, 3);
    func(1, 2, "hello!");
}

===================================================================================
std::disjunction


===================================================================================
std::bool_constant



===================================================================================
std::negation




===================================================================================
std::true_type


===================================================================================
std::integral_constant


===================================================================================
template<class T> using void_t = std::void_t<T>;


===================================================================================
template <class F, class Tuple>
CUDA_HOST_DEVICE inline constexpr decltype(auto) apply(F&& f, Tuple&& t) {
  return std::apply(std::forward<F>(f), std::forward<Tuple>(t));
}

===================================================================================
std::remove_reference_t




===================================================================================
std::make_index_sequence


===================================================================================
std::tuple_size


===================================================================================
std::function<void(Stack&)> callable_;


===================================================================================
std::is_lvalue_reference



===================================================================================
std::mt19937
高质量随机数种子
https://www.jianshu.com/p/9516c837739e
http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/CODES/MTARCOK/mt19937ar-cok.c
https://github.com/syed-ahmed/benchmark-rngs



===================================================================================
std::uniform_real_distribution
这个方法有bug
http://open-std.org/JTC1/SC22/WG21/docs/lwg-active.html#2524



===================================================================================
std::exception



===================================================================================
std::nth_element



===================================================================================
std::this_thread::yield


===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================



===================================================================================




===================================================================================




===================================================================================





```




### 注释

```
比较好的写法可以参考
#include <array> // array
#include <cassert> // assert
#include <cstddef> // size_t
#include <cstdio> //FILE *
#include <cstring> // strlen
#include <istream> // istream
#include <iterator> // begin, end, iterator_traits, random_access_iterator_tag, distance, next
#include <memory> // shared_ptr, make_shared, addressof
#include <numeric> // accumulate
#include <string> // string, char_traits
#include <type_traits> // enable_if, is_base_of, is_pointer, is_integral, remove_pointer
#include <utility> // pair, declval


```





## Glibc

```
// [Note SSE-AVX transitions]
// There is a bug in Glibc2.23
// https://bugs.launchpad.net/ubuntu/+source/glibc/+bug/1663280. Calling zeroall
// when using AVX/AVX2 code resolves this.

```

## C++的指针

```
(ConstantInt*)arg_0->getValue().getRawData()
这样不是强转，gcc5.4.0会认为是*arg_0 获取指针对象
```

### 对象指针

```
new 出来的指针，系统不会回收
```



## C++的函数

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

#### 传递的例子

```
vector指针传递
function(std::vector<Tensor>* out_tensors)
std::vector<Tensor> resized_tensors;
function(&resized_tensors)

引用传递
void func1(vector<int> &q){
 
...
 
}
int main(){
vector<int> q;
q.push_back(2);
q.push_back(3);
q.push_back(1);
func1(q);
}
```



#### 注意问题

- 如果传入指针进入函数里面，要避免指针被函数内部修改！！！最好在指针右边加 const。可以编译中查出问题
- 如果修改指针的内容，那么也要注意修改是否正确

### 函数指针

#### 场景

- 来模板中调用统一函数接口，函数名相同，但是函数的参数全部都一样。比如服务端的各种类型的请求函数

#### 资料

- 使用方法：<https://www.cprogramming.com/tutorial/function-pointers.html

#### 高级用法

```
获取函数地址，然后调用：https://blog.csdn.net/Kwansy/article/details/79328003
void func(void);//有一个函数
int address = (int)func;//用整数保存其地址
((void(*)())address)();//通过地址调用func


定义一个有参数变量的函数
((void(*)(int,int,int,int,int))main_func)(  raw_data.at(0),
                                                    raw_data.at(1),
                                                    raw_data.at(2),
                                                    raw_data.at(3),
                                                    raw_data.at(4));
```

### 函数的局部变量问题

```
函数内创建的局部变量，再函数结束后，局部变量会失效
除非是return的变量，return的变量不会失效

如何保存局部变量
一
	用vector保存变量，vector会把值复制一遍，这样局部变量的值就在外部了。
	注意：vector不适合保存对象的指针，对象指针保存以后，局部变量的值仍然可以被释放，只有指针的地址是不能访问局部变量
	
二
	外部创建的变量，放到局部函数中，局部变量可以赋值给外部变量
	
总结：大体思路，就是让局部变量的作用域范围更大
```








## C++工具集

```
结巴分词：https://github.com/yanyiwu/cppjieba
limonp：https://github.com/yanyiwu/limonp
	字符串工具，线程，文件锁，md5等等
	字符串包含不同格式编解码，字符串切割
rapidJson：https://rapidjson.org/
c++json性能比较：https://github.com/miloyip/nativejson-benchmark
glib全新的底层分配内存：https://developer.gnome.org/glib/stable/glib-Memory-Allocation.html
valgrind内存泄露工具：http://valgrind.org/downloads/current.html#current
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
#include<boost/algorithm/string.hpp>

分割与合并字符串
	std::string s("test stringa-test stringb-test stringc");
    std::vector<std::string> sv;
    boost::split(sv,s,boost::is_any_of("-"),boost::token_compress_on);
    //Now,sv={"test stringa","test stringb","test stringc"};
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

#### boost::any

```

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
