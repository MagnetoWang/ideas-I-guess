## 《Effective C++》读书笔记

### 看书顺序

- 先看每个技巧都小节
- 然后思考为什么
- 带着为什么从小节内容中寻找答案

[TOC]



### 习惯c++

#### 1c++是个语言联邦：View C++ as a federation of languages

- 原因：c++支持多种编程范式
  - 明确每个范性的定义和内涵
  - 支持过程编程
  - 面向对象
  - 函数形式
  - 范型形式
  - 元编程形式
- 解决
- 方案一
  - C
    - 优点：区块，语句，预处理器，内置数据类型，数组，指针
    - 缺点：没有模版，没有异常，没有重载
  - C++
    - 优点：类，构造函数，析构函数，封装（encapsulation），继承（inheritance），多态（polymorphism），virtual函数
    - 缺点：难理解
  - Template C++
    - 范型编程
  - STL
    - template程序库

#### 2尽量以const,enum,inline替换 #define：Perfer consts,enums,and inlines to #define

- 原因： #define是单纯的文字替换。在多人开发中，你定义的一个宏变量，可能在某个文件中，会出现相同的名字，比如字符串之类的。而编译的时候不会报错。查问题很麻烦
- 解决
  - const
    - const 代替你使用的名字，因为有了类型的约束，并且会进入符号表
  - const
    - 定义一个常量，只在类中的作用域生效
    - 那么这个常量必须是类的成员
    - 为保证这个常量在这个类中是唯一的，用static来修饰
    - 比如
    - static const int NumTurns = 5 这是声明式，一般放在头文件
    - 如果要放在实现文件
    - const int XXXClass::NumTurns; 这是定义式
  - enum
    - 用枚举类型定义常量
    - enum { NumTurns = 5  };
    - enum 可以 约束别人对你的常量引用。因为pointer 和 reference 无法指向枚举类型的整数
  - inline
    - define 可以定义宏函数，但是使用起来容易出问题
    - 用模版 + inline 可以约束你的宏函数
- 总结
  - 对于单纯的常量，最好用const和enum替换define
  - 对于形似函数的宏，改用inline函数替换define

#### 3尽可能使用const：Use const whenever possible

- 原因：具有语义约束

#### 4确定对象被使用前已先被初始化：Make sure that objects are initialized before they're used

- 原因：
- 解决
- 总结：
  - 内置型对象进行手工初始化，因为c++不保证初始化
  - 构造函数最好使用成员初值列（member initialization list），而不要在构造函数本体内使用赋值操作。初值列列出的成员变量，其排列次序应该和它们在class中声明次序相同
  - 为免除“跨编译单元的初始化顺序”，用local static 对象替换non-local static对象

### 资源管理

#### 13对象管理资源：Use objects to manage resources

- 原因：在调用函数创建对象的时候我们总是会忘记delete对象，导致对象泄漏内存
- 解决
  - 方案一
    - std::auto_ptr\<Object\> name ( createObject() )
    - 将创造的对象让auto_ptr封装对象，对象的内部的析构函数会自动删除对象
  - 方案二
    - 方案一，只适合静态的管理，不适合动态管理
      - 比如，std::auto_ptr\<Object\> name1 (name)
      - name = name1
      - 这个时候，非常诡异复制的操作，让auto_ptr没办法自动管理对象。auto会指向null
    - RCSP:reference-counting smart pointer
      - 引用计数型智慧指针，可以追踪多少对象引用资源
      - 无人引用的时候，自动回收
      - 缺点：无法打破互相引用的环
    - std::shared_ptr \<Object\> name ( createObject() )
- 总结
  - 获得资源后立刻放进管理对象
  - 管理对象会在走出作用域之后，其析构函数被自动调用
  - RAII：资源取得时机便是初始化时机
  - Resourse Acquistion Is Initialization

#### 14在资源管理类中小心coping行为：Think carefully about copying behavior in resource-managing classes

- 原因：不是所有资源都是 heap-based。RAII可以解决部分复制资源。面对其他类型的资源比如，锁。我们需要完全自己加锁，释放锁。所以资源的复制，是非常难管理的。
- 解决
  - 方案一
    - 禁止复制
    - 部分资源的复制并不合理，很难拥有同步化基础器物（synchronization primitives）
  - 方案二
    - 底层资源使用引用计数法
    - 难度高，很麻烦
  - 方案三
    - 复制底部资源
    - 直接制造副本给另外一个对象
    - 深度拷贝
  - 方案四
    - 转移底部资源的拥有权
    - 直接给对方引用的对象，之前的转为null
- 总结
  - 复制RAII对象必须一并复制它所管理的资源。深度拷贝

#### 15在资源管理类中提供对原始资源的访问：provide access to raw resources in resource-managing classes

- 原因：完美的世界，只需要RAII就可以解决资源泄露问题。然而在部分情况下，我们需要直接获取原始资源。比如我们的提供外部的api。需要的事原始资源而不是封装的指针
- 解决
  - 显式转换
    - get函数
  - 隐式转换
    - 直接返回的就是原始资源。容易误用，在复制对象的时候，一旦原始资源被释放了，复制后的对象就无效了
  - 接口不应该被误用，更多的选择显示转换
- 总结
  - API往往要求访问原始资源，所以每个RAII class应该提供一个“取得其所管理之资源”的办法
  - 对原始资源可以是显式或者隐式转换。显式安全，隐式对客户比较方便

#### 16成对使用new和delete时要采取相同形式：use the same form in corresponding uses of new and delete

- 原因：删除对象的时候，尤其是数组对象，我们可能只是删除了数组的一个对象，数组的其他位置的对象没有被删除
- 解决
  - new array[] 时 ，也要delete []
  - new object 时， 要 delete object
- 总结
  - 和方案一个意思。主要区分数组对象和对象



#### 17以独立语句将newed对象置入智能指针：store need objects in smart pointers in standalone statements

- 一句话
  - new一个对象应该用一条语句
  - 如果一条语句实现多个操作，那么一旦异常抛出，有可能导致难以察觉的资源泄漏

### 设计与声明

#### 18让接口容易被正确使用，不易被误用：make interface easy to use correctly and hard to use incorrectly

- 原因：各式各样的接口种类繁多，funciton，class，template等等各种接口。接口要让客户容易被正确的使用
- 解决
- 总结
  - 好的接口很容易被正确使用，不容易被误用
  - 促进正确使用，的办法包括接口的一致性，以及与内置类型的行为兼容
  - 阻止误用，的办法包括建立新类型，限制类型上的操作，束缚对象值，以及消除客户的资源管理责任
  - Trl 指针 支持定制行删除器，可防范DLL

#### 19设计class犹如设计type：treat class design as type design

- 原因：因为class相当于扩充你的类型系统，本质和系统的中原有type一样。需要考虑重载，操作符，控制内存和归还，定义对象初始化的所有事情
- 解决
  - 用构造函数和析构函数以及内存分配函数和释放函数进行对象的创建和销毁
  - 对象初始化和对象赋值区分开
  - 新type的对象如果被 pass by value，意味着什么？
  - 什么是新type的合法值？
    - 考虑约束条件，错误检查工作
  - 新type是否需要配合某个继承关系吗？
    - 注意virtual 和 non-virtual的影响
  - 新type需要什么样的转换？
  - 什么样的操作符和函数对此新type而言是合理的？
  - 什么样的标准函数应该驳回
  - 谁会使用新type的成员
  - 什么是新type的未声明接口
  - 你的新type有多么一般化
  - 你真的需要一个新type吗
- 总结
  - 同解决方案内容一样

#### 20选择pass-by-reference-to-const 替换 pass-by-value：prefer pass-by-reference-to-const to pass-by-value

- 原因

25



### 实现

#### 26尽可能延后变量定义式的出现时间：postpone variable definitions as long as possible

#### 27尽量少做转型动作：minimize casting

- 

#### 28避免返回handles指向对象内部成分

#### 29为 异常安全 而努力是值得的



[TOC]

