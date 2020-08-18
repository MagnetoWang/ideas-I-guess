

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

### vector使用

- 参考文档：http://www.cplusplus.com/reference/vector/vector/
- 常用函数

```
reserve(number) 提前开辟vector空间，可以减少后面自动增长的开销
clear() 清除所有的元素
push_back(element) 往最后一个位置插入元素
erase(index) 删除第index个位置的元素

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

### ifndef用法

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

### C++的定义和声明

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
    ss << value;
    ss >> value_str;

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

### 性能优化

- insert 对象的时候，其实是复制了一个对象，要想优化，最后insert一个指针或者引用
- 上面这一行是错误的！！！！！！
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

```
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


### 编译环境define
```
===================================================================================
#if defined(__cpp_lib_logical_traits) && !(defined(_MSC_VER) && _MSC_VER < 1920)


===================================================================================
__HIP_PLATFORM_HCC__
CUDA_HOST_DEVICE



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
#include <chrono> // for timestamp

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

### 打印人类可读的存储大小

```
tensorflow/stream_executor代码中看到的
static string ToString(int64 num_bytes) {
    if (num_bytes == std::numeric_limits<int64>::min()) {
      // Special case for number with not representable nagation.
      return "-8E";
    }

    const char* neg_str = GetNegStr(&num_bytes);

    // Special case for bytes.
    if (num_bytes < 1024LL) {
      // No fractions for bytes.
      return port::Printf("%s%lldB", neg_str, num_bytes);
    }

    static const char units[] = "KMGTPE";  // int64 only goes up to E.
    const char* unit = units;
    while (num_bytes >= (1024LL) * (1024LL)) {
      num_bytes /= (1024LL);
      ++unit;
      assert(unit < units + sizeof(units));
    }

    return port::Printf(((*unit == 'K') ? "%s%.1f%c" : "%s%.2f%c"), neg_str,
                        num_bytes / 1024.0, *unit);
  }
  
  template <typename T>
  static const char* GetNegStr(T* value) {
    if (*value < 0) {
      *value = -(*value);
      return "-";
    } else {
      return "";
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

### 字符串切割

```
inline void Split(const string& src, vector<string>& res, const string& pattern, size_t maxsplit = string::npos) {
  res.clear();
  size_t Start = 0;
  size_t end = 0;
  string sub;
  while(Start < src.size()) {
    end = src.find_first_of(pattern, Start);
    if(string::npos == end || res.size() >= maxsplit) {
      sub = src.substr(Start);
      res.push_back(sub);
      return;
    }
    sub = src.substr(Start, end - Start);
    res.push_back(sub);
    Start = end + 1;
  }
  return;
}
```

### 字母大小写

```
inline string& Upper(string& str) {
  transform(str.begin(), str.end(), str.begin(), (int (*)(int))toupper);
  return str;
}

inline string& Lower(string& str) {
  transform(str.begin(), str.end(), str.begin(), (int (*)(int))tolower);
  return str;
}
```

### 字符串拼接

```
template<class T>
void Join(T begin, T end, string& res, const string& connector) {
  if(begin == end) {
    return;
  }
  stringstream ss;
  ss<<*begin;
  begin++;
  while(begin != end) {
    ss << connector << *begin;
    begin ++;
  }
  res = ss.str();
}
```

### 数据类型的最大最小值

```
http://www.cplusplus.com/reference/climits/


```

### 打印服务器配置

```
#if defined(__linux)
    time_t now = time(nullptr);
    fprintf(stderr, "Date:       %s", ctime(&now));  // ctime() adds newline

    FILE* cpuinfo = fopen("/proc/cpuinfo", "r");
    if (cpuinfo != nullptr) {
      char line[1000];
      int num_cpus = 0;
      std::string cpu_type;
      std::string cache_size;
      while (fgets(line, sizeof(line), cpuinfo) != nullptr) {
        const char* sep = strchr(line, ':');
        if (sep == nullptr) {
          continue;
        }
        Slice key = TrimSpace(Slice(line, sep - 1 - line));
        Slice val = TrimSpace(Slice(sep + 1));
        if (key == "model name") {
          ++num_cpus;
          cpu_type = val.ToString();
        } else if (key == "cache size") {
          cache_size = val.ToString();
        }
      }
      fclose(cpuinfo);
      fprintf(stderr, "CPU:        %d * %s\n", num_cpus, cpu_type.c_str());
      fprintf(stderr, "CPUCache:   %s\n", cache_size.c_str());
    }
#endif

这里要切割根据空格字符串
#if defined(__linux)
static Slice TrimSpace(Slice s) {
  size_t start = 0;
  while (start < s.size() && isspace(s[start])) {
    start++;
  }
  size_t limit = s.size();
  while (limit > start && isspace(s[limit-1])) {
    limit--;
  }
  return Slice(s.data() + start, limit - start);
}
#endif
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

### 快速定位segment fault

```
两个print的方法
std::cout<< "ok 169" << std::endl;
std::cout<< "ok 122" << std::endl;
一头一尾，不断往中间靠拢，来定位哪一行的bug
```



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

### 安装

```
git clone https://github.com/gflags/gflags.git

cd gflags
mkdir build && cd build
cmake .. && make
cp -r include/. xxxx
cp -r lib/. xxxx
```

### 使用

```
随意定义一个文件
#include <gflags/gflags.h>

   DEFINE_bool(big_menu, true, "Include 'advanced' options in the menu listing");
   DEFINE_string(languages, "english,french,german",
                 "comma-separated list of languages to offer in the 'lang' menu");
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



## Apache arrow

### 资料

- 介绍：<https://www.cnblogs.com/smartloli/p/6367719.html

### 常用功能

```
结构体转arrow的table类型
https://arrow.apache.org/docs/cpp/examples/tuple_range_conversion.html

table转结构体
https://arrow.apache.org/docs/cpp/examples/row_columnar_conversion.html

获取arrow的int,long,double类型方法
auto values = std::static_pointer_cast<arrow::Int32Array>(column_data.at(i)->chunk(0));
int32_t value = values->Value(j);

auto values = std::static_pointer_cast<arrow::Int64Array>(column_data.at(i)->chunk(0));
double value = values->Value(j);


```



## Hadoop

### 资料

- 官网：<https://hadoop.apache.org/>

### 安装

```
wget http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
tar -zxvf hadoop-3.1.2.tar.gz

mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.2.jar grep input output 'dfs[a-z.]+'
cat output/*


```

### hadoop命令

```
FS Shell
调用文件系统(FS)Shell命令应使用 bin/hadoop fs <args>的形式。 所有的的FS shell命令使用URI路径作为参数。URI格式是scheme://authority/path。对HDFS文件系统，scheme是hdfs，对本地文件系统，scheme是file。其中scheme和authority参数都是可选的，如果未加指定，就会使用配置中指定的默认scheme。一个HDFS文件或目录比如/parent/child可以表示成hdfs://namenode:namenodeport/parent/child，或者更简单的/parent/child（假设你配置文件中的默认值是namenode:namenodeport）。大多数FS Shell命令的行为和对应的Unix Shell命令类似，不同之处会在下面介绍各命令使用详情时指出。出错信息会输出到stderr，其他信息输出到stdout。

cat
使用方法：hadoop fs -cat URI [URI …]

将路径指定文件的内容输出到stdout。

示例：

hadoop fs -cat hdfs://host1:port1/file1 hdfs://host2:port2/file2
hadoop fs -cat file:///file3 /user/hadoop/file4
返回值：
成功返回0，失败返回-1。

chgrp
使用方法：hadoop fs -chgrp [-R] GROUP URI [URI …] Change group association of files. With -R, make the change recursively through the directory structure. The user must be the owner of files, or else a super-user. Additional information is in the Permissions User Guide. -->

改变文件所属的组。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。更多的信息请参见HDFS权限用户指南。

chmod
使用方法：hadoop fs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI …]

改变文件的权限。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。更多的信息请参见HDFS权限用户指南。

chown
使用方法：hadoop fs -chown [-R] [OWNER][:[GROUP]] URI [URI ]

改变文件的拥有者。使用-R将使改变在目录结构下递归进行。命令的使用者必须是超级用户。更多的信息请参见HDFS权限用户指南。

copyFromLocal
使用方法：hadoop fs -copyFromLocal <localsrc> URI

除了限定源路径是一个本地文件外，和put命令相似。

copyToLocal
使用方法：hadoop fs -copyToLocal [-ignorecrc] [-crc] URI <localdst>

除了限定目标路径是一个本地文件外，和get命令类似。

cp
使用方法：hadoop fs -cp URI [URI …] <dest>

将文件从源路径复制到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。 
示例：

hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2
hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir
返回值：

成功返回0，失败返回-1。

du
使用方法：hadoop fs -du URI [URI …]

显示目录中所有文件的大小，或者当只指定一个文件时，显示此文件的大小。
示例：
hadoop fs -du /user/hadoop/dir1 /user/hadoop/file1 hdfs://host:port/user/hadoop/dir1 
返回值：
成功返回0，失败返回-1。 
dus
使用方法：hadoop fs -dus <args>

显示文件的大小。

expunge
使用方法：hadoop fs -expunge

清空回收站。请参考HDFS设计文档以获取更多关于回收站特性的信息。

get
使用方法：hadoop fs -get [-ignorecrc] [-crc] <src> <localdst> 
复制文件到本地文件系统。可用-ignorecrc选项复制CRC校验失败的文件。使用-crc选项复制文件以及CRC信息。

示例：

hadoop fs -get /user/hadoop/file localfile
hadoop fs -get hdfs://host:port/user/hadoop/file localfile
返回值：

成功返回0，失败返回-1。

getmerge
使用方法：hadoop fs -getmerge <src> <localdst> [addnl]

接受一个源目录和一个目标文件作为输入，并且将源目录中所有的文件连接成本地目标文件。addnl是可选的，用于指定在每个文件结尾添加一个换行符。

ls
使用方法：hadoop fs -ls <args>

如果是文件，则按照如下格式返回文件信息：
文件名 <副本数> 文件大小 修改日期 修改时间 权限 用户ID 组ID 
如果是目录，则返回它直接子文件的一个列表，就像在Unix中一样。目录返回列表的信息如下：
目录名 <dir> 修改日期 修改时间 权限 用户ID 组ID 
示例：
hadoop fs -ls /user/hadoop/file1 /user/hadoop/file2 hdfs://host:port/user/hadoop/dir1 /nonexistentfile 
返回值：
成功返回0，失败返回-1。 
lsr
使用方法：hadoop fs -lsr <args> 
ls命令的递归版本。类似于Unix中的ls -R。

mkdir
使用方法：hadoop fs -mkdir <paths> 
接受路径指定的uri作为参数，创建这些目录。其行为类似于Unix的mkdir -p，它会创建路径中的各级父目录。

示例：

hadoop fs -mkdir /user/hadoop/dir1 /user/hadoop/dir2
hadoop fs -mkdir hdfs://host1:port1/user/hadoop/dir hdfs://host2:port2/user/hadoop/dir
返回值：

成功返回0，失败返回-1。

movefromLocal
使用方法：dfs -moveFromLocal <src> <dst>

输出一个”not implemented“信息。

mv
使用方法：hadoop fs -mv URI [URI …] <dest>

将文件从源路径移动到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。不允许在不同的文件系统间移动文件。 
示例：

hadoop fs -mv /user/hadoop/file1 /user/hadoop/file2
hadoop fs -mv hdfs://host:port/file1 hdfs://host:port/file2 hdfs://host:port/file3 hdfs://host:port/dir1
返回值：

成功返回0，失败返回-1。

put
使用方法：hadoop fs -put <localsrc> ... <dst>

从本地文件系统中复制单个或多个源路径到目标文件系统。也支持从标准输入中读取输入写入目标文件系统。
hadoop fs -put localfile /user/hadoop/hadoopfile
hadoop fs -put localfile1 localfile2 /user/hadoop/hadoopdir
hadoop fs -put localfile hdfs://host:port/hadoop/hadoopfile
hadoop fs -put - hdfs://host:port/hadoop/hadoopfile 
从标准输入中读取输入。
返回值：

成功返回0，失败返回-1。

rm
使用方法：hadoop fs -rm URI [URI …]

删除指定的文件。只删除非空目录和文件。请参考rmr命令了解递归删除。
示例：

hadoop fs -rm hdfs://host:port/file /user/hadoop/emptydir
返回值：

成功返回0，失败返回-1。

rmr
使用方法：hadoop fs -rmr URI [URI …]

delete的递归版本。
示例：

hadoop fs -rmr /user/hadoop/dir
hadoop fs -rmr hdfs://host:port/user/hadoop/dir
返回值：

成功返回0，失败返回-1。

setrep
使用方法：hadoop fs -setrep [-R] <path>

改变一个文件的副本系数。-R选项用于递归改变目录下所有文件的副本系数。

示例：

hadoop fs -setrep -w 3 -R /user/hadoop/dir1
返回值：

成功返回0，失败返回-1。

stat
使用方法：hadoop fs -stat URI [URI …]

返回指定路径的统计信息。

示例：

hadoop fs -stat path
返回值：
成功返回0，失败返回-1。

tail
使用方法：hadoop fs -tail [-f] URI

将文件尾部1K字节的内容输出到stdout。支持-f选项，行为和Unix中一致。

示例：

hadoop fs -tail pathname
返回值：
成功返回0，失败返回-1。

test
使用方法：hadoop fs -test -[ezd] URI

选项：
-e 检查文件是否存在。如果存在则返回0。
-z 检查文件是否是0字节。如果是则返回0。 
-d 如果路径是个目录，则返回1，否则返回0。
示例：

hadoop fs -test -e filename
text
使用方法：hadoop fs -text <src> 
将源文件输出为文本格式。允许的格式是zip和TextRecordInputStream。

touchz
使用方法：hadoop fs -touchz URI [URI …] 
创建一个0字节的空文件。

示例：

hadoop -touchz pathname
返回值：
成功返回0，失败返回-1。
```



### Yarn

- hadoop的组件
- 概念介绍：<https://zhuanlan.zhihu.com/p/41151457>
- 常用命令：<https://yarn.bootcss.com/docs/usage/>

### 常用功能

```
命令行
https://blog.csdn.net/sunshingheavy/article/details/53227581
```

## RocksDB

### 资料

- 中文网：<https://rocksdb.org.cn/doc/Implement-Queue-Service-Using-RocksDB.html>

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

### 多个文件互相调用函数

```
使用extern 声明外部文件的函数

使用头文件方式，引入外部函数
```

### 多个文件互相调用同一个头文件的变量问题

```
a.h
std::vector<Value*> row

b.cpp
c.cpp
d.cpp
```

### 生成core文件，然后调试

```
快速上手：https://blog.csdn.net/u011806486/article/details/81409992
调试详细文章：https://blog.csdn.net/hello2mao/article/details/79258471

查看core文件大小，默认为0
ulimit -a

core file size 为无限
ulimit -c unlimited

不产生core文件,注意，改回0以后，就无法再改成unlimited
ulimit -c 0

调试
gdb 可执行程序 core


进阶 进入gdb界面以后
直接打印问题代码堆栈
bt

动态编译的程序是不能直接gdb，需要在cmakelist中添加定义
add_definitions(-D_DEBUG)
```

### 安装GCC 5.4.0版本

```
https://www.jianshu.com/p/0caef3ce8e06

wget https://mirrors.ustc.edu.cn/gnu/gcc/gcc-5.4.0/gcc-5.4.0.tar.gz
tar -zxvf gcc-5.4.0.tar.gz
cd gcc-5.4.0
./contrib/download_prerequisites
mkdir build
./configure --prefix=/home/wangzixian/software/gcc-5.4.0/build --enable-languages=c,c++ --disable-multilib --enable-host-shared
make -j12 && make install

./configure --prefix=/home/wangzixian/ferrari/feql-jit/compatible-with-linux-1/pico/gcc/build --enable-threads=posix --disable-multilib --enable-languages=c,c++
```

### 安装bazel

```
wget https://github.com/bazelbuild/bazel/releases/download/0.29.0/bazel-0.29.0-installer-darwin-x86_64.sh
sh bazel-0.29.0-installer-darwin-x86_64.sh --prefix=/xxx/xxx/third_party

添加bin的环境路径
```



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

然后运行 也可以重新执行
run 或者 start


设置断点
b <行号>
b <函数名称>
b *<函数名称>
b *<代码地址>

跳下一个断点
c continue

删除断点
d [断点的编号]

函数判断
s: 执行一行源程序代码，如果此行代码中有函数调用，则进入该函数；
n: 执行一行源程序代码，此行代码中的函数调用也一并执行。 

打印变量
p <变量名称>
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

### 调试文件的过程

```
lldb xxxx.file
r // 执行程序，之后会开始跑程序，有些程序需要输入数据，才会开始启动
breakpoint set -f node_test.cpp -l 17

s 进入源码层
n 下一行代码，不进入源码层
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





# 新项目

## RocksDB

### 资料

- 全面介绍：<http://alexstocks.github.io/html/rocksdb.html>



## Json-C++

### 资料

- nlohman库：https://github.com/nlohmann/json

### 文件读取json对象

```
https://blog.csdn.net/kuyu05/article/details/88561319
using json = nlohmann::json;

std::ifstream read("broker.json");
	json in = json::parse(read);
	cout << in.dump(4) << endl;
```

### json对象函数传入

```
using Json = nlohmann::json;

Json::iterator
Json
```

## Xgboost

### llvm RTTI

```
https://baike.baidu.com/item/RTTI
RTTI（Run-Time Type Identification)，通过运行时类型信息程序能够使用基类的指针或引用来检查这些指针或引用所指的对象的实际派生类型。
```
## Mxnet

```
base.h
只有枚举类

shape.h
声明ndarray数组维度和大小


operator symbol


ndarray.h

c_api_ndarray.cc
实现很多调用函数，比如
MXImperativeInvoke,MXImperativeInvokeImpl


```

## dmlc

```
有非常多工具库函数
CSVParser


```

## DCPMM

```
说明：https://blog.csdn.net/limanjihe/article/details/106158713
编程工具库：https://pmem.io/pmdk/
```

[TOC]

