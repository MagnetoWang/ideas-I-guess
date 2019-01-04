##  《Effective C++》读书笔记

## 第三版

### 看书顺序

- 先看每个技巧都小节
- 然后思考为什么
- 带着为什么从小节内容中寻找答案

### 个人总结

- 写的每一行代码应该明确它的目的和约束
- 

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
- 个人总结
  - 构造函数之前要初始化
  - 赋值和初始化是不一样的概念和操作
  - 初始化效率更高，赋值前需要调用default构造函数所以效率更低
  - 跨编译单元的问题，主要是指在多个源文件中，有多个类，A类调用B类的接口时，因为B类并没有初始化，导致调用B类失败。这个时候为了更好保证调用B类是无感知的。应该在A类构造函数中，就初始化B类。防止后期提供接口出现问题

### 构造/析构/赋值

- 这三个操作，掌握着类的生杀大权
- 必须加以约束，否则后期的bug都非常难找

#### 5C++默认编写并调用这些函数：Constructors,Destructors,and Assignment Operators

- 总结
  - 四个影响性能函数
  - default函数
  - copy构造函数
  - copy assignment函数
  - 析构函数

#### 6若不想使用编译器自动生成的函数，就明确拒绝：Explicitly disallow the use of compiler-generated functions you do not want

- 总结
  - 自己声明某个自动生成函数即可，然后实现内部功能

#### 7为多态基类声明virtual析构函数：Declare destructors virtual in polymorphic base classes

- 原因
  - 多个子类共同继承一个父类时，如果没有添加virual到析构函数。当父类进行析构的时候，那么子类的成分将不会被析构销毁。造成资源泄漏
- 解决
  - 添加virual即可实现自动识别子类对象，并进行析构
  - 但是也不能随便添加virual，除非存在virual函数才能添加viual析构函数
- 总结
  - polymorphic base classes 应该声明一个virtual析构函数。尤其是拥有virtual函数，就应该拥有一个virtual析构函数
  - classes的设计目的如果不是为了多态性的基类使用，就不该声明virtual析构函数和virtual函数
- 个人总结
  - 认清类的两种类型
  - 一种是为了后面子类基础扩展的，就要考虑到多态性。
  - 一种是为了单纯使用的类，不是为扩展。就不能添加virtual析构函数

#### 8别让异常逃离析构函数：Prevent exceptions from leaving destructors

- 原因
- 解决
- 总结
  - 析构函数绝对不要吐出异常。如果一个被析构函数调用的函数可能抛出异常，析构函数应该捕捉任何异常，然后吞下它们，防止传播或结束程序
  - 如果客户需要对某个操作函数运行期间抛出异常做出反应，那么class应该提供一个普通函数执行改操作
- 个人总结

#### 9绝不在构造和析构过程中调用virtual函数：Never call virtual functions during construction or destruction

- 原因
- 解决
- 总结
  - 在构造和析构过程中不要调用virtual函数，因为这类调用从不下降至derived class
- 个人总结

#### 10operator= 返回 reference to * this：Have assignment operators return a reference to * this

- 原因
  - 一个协议，为了符合右结合规律
- 个人总结
  - 不是很重要

#### 11operator= 处理“自我赋值”：Handle assignent to self in operator=

- 原因
  - 会出现 object c;
  - c = c
  - 情况
  - 潜在意识到自我赋值
  - 根本问题在于：两个不同名字但是实际是同一对象，然后出现赋值操作的问题。这个时候要好好处理赋值函数的代码。不然会出现对象丢失或者指针指向错误的问题
- 解决
  - 方案一
    - 删除原来对象
    - 赋值新对象
    - 返回对象
    - 缺点
      - 原来的对象和新对象本是同一个对象，删除后，对象丢失
  - 方案二
    - 用指针指原来的对象
    - 赋值新对象
    - 删除原来对象
    - 缺点
      - 赋值对象可能出现异常
      - 缺少identity test来判断两个对象是否是同一对象
  - 方案三
    - 备份新的对象
    - 备份的新对象和原来对象互相交换数据
    - 返回this
- 总结
  - 确保当对象自我赋值时 operator= 有良好行为。其中技术包括比较“来源对象”和“目标对象”的地址，精心周到的语句顺序，以及copy-and-swap
  - 确定任何函数如果操作一个以上的对象，而其中多个对象是同个印象时，行为仍然正确
- 个人总结
  - copy-and-swap的方法，主要的意思是，在遇到可能同一个对象自己赋值情况下，每次对传进来的对象，都直接备份的新的对象，然后在交换数据，就可以解决自我赋值的问题
  - 具体结合书中的代码来看每个方案的优点和缺点
  - 万无一失的办法就是，创建一个新对象然后赋值。这就间接解决了同一对象自我赋值的问题

#### 12复制对象勿忘其每一个成分：Copy all parts of an object

- 原因
  - 规范的对象会有copy构造函数和copy assignment操作符。编译器自动生成
  - 如果要自己实现的话，
- 解决
  - 成员变量都要复制一遍，或者不要自己去实现
  - 最好写一个init函数，构造函数和赋值函数可以直接调用
- 总结
  - copying函数应该确保复制“对象内的所有成员变量”和“所有base class”的成分
  - 不要尝试以某个copying函数实现另一个copying函数。应该将共同机能放进第三个函数中，并由两个copying函数共同调用
- 个人总结

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
  - 传对象值，会发生构造一次对象，析构一次对象消耗。同时不改变实际参数的值
- 解决
  - bool funcition (const student & s);
  - const根据情况是否需要
- 总结
  - 尽量用引用替换值传递，前者高效，并且避免切割问题
  - 这个规则不适用STL的迭代器和函数对象
- 个人总结
  - STL一般传递值

#### 21必须返回对象时，别妄想返回reference：Don't try to return a reference when you must return an object

- 原因
  - Rational result(xx,xx,xx) 这是在栈上面开辟空间，函数结束后会被销毁
  - 得到的只是没有用的引用
  - Rational * result = new Rational(xxx) 这是在heap上开辟空间
  - 返回引用后，根本没办法delete 释放资源。导致资源泄漏
  - 上面不管什么方式，都构造了新的对象，造成新的消耗
- 解决
  - 不声明即可
- 总结
  - 绝不要返回指针或reference指向一个local stack对象，或返回reference指向一个heap-allocated 对象，或返回pointer或reference指向
- 个人总结
  - local 对象无论怎么生成，最终都会破坏使用这个对象统一性。
  - 统一性是指，可以自主的创建的对象，同时也可以自主销毁这个对象。
  - 一旦这个主动权交给了编译器或者无名的力量，那么就是破坏你在你代码面前的权威性

#### 22将成员变量声明为private：Declare data members private

- 原因
  - 为了统一规范化，成员调用统一函数
  - 更细节的权限管理
  - 封装性，以后可以修改函数内部，不影响外部情况
- 解决
- 总结
  - 声明成员变量为private
  - protect并不比public更具有封装性
- 个人总结
  - 声明就是了

#### 23选择non-member,non-friend替换member函数：Prefer non-member non-friend functions to member functions

- 原因
- 解决
- 总结
- 个人总结

#### 24

#### 25



### 实现

#### 实现一个类可能出现的问题

- 提前定义变量造成效率拖延
- 过度使用 casts 强制转型，导致代码难以维护
- 返回对象内部的数据，可能会破坏封装并留给客户风险
- 不处理异常导致资源泄漏和数据败坏
- 过度使用inlining可能导致代码膨胀
- 过度耦合coupling 则可能导致让人不满意等待编译时间

#### 26尽可能延后变量定义式的出现时间：postpone variable definitions as long as possible

- 原因
  - 定义对象，至少需要两个代价，构造和析构
- 解决
  - 在需要使用对象的时候再开始定义
  - 高效例子
    - 传入参数 password
    - std::string encry(password);
    - encrypt_function(encry);
    - return encry;
    - 这是真正定义变量，应该延后到可以给它设置初值实参为止
    - 这样避免构造不必要对象，和无意义的default构造行为
    - 因为定义变量，不赋值，就会启动default的构造函数
- 总结
  - 延后定义变量和赋值
- 个人总结
  - 注意，这里不是绝对，在一个循环里面，应该考虑在循环外定义好变量
  - 这里抓住三个核心，构造，析构和赋值
  - 如果在循环内出现大量构造，析构操作，那么就应该在外面定义变量
  - 总之，要比较这个三个操作的成本就可以确定在哪个位置定义变量

#### 27尽量少做转型动作：minimize casting

- 原因

  - 不同语言对接时，可能出现转型的需求

- 解决

  - 

- 总结

  - C语法

    - (T) expression
    - T(expression)
  - C++ 语法
    - const_cast\<T\> (expression) 
      - 将对象的常量性转除
    - dynamic_cast\<T\> (expression) 
      - 安全向下转型，决定某对象是否归属继承体系中某个类型
      - 该转型成本非常大
    - reinterpret_cast\<T\> (expression) 
      - 执行低级转型，转型结果取决于编译器，不可移植
      - 使用情况非常少
    - static_cast\<T\> (expression) 
      - 强迫隐式转换
      - 比如
      - non-const 到 const 相反操作使用 const_cast
      - int 到 double
      - pointer-to- base 到 pointer-to-derived
  - 尽量避免转型，尤其是避免dynamic_casts
  - 如果转型是必要的，请封装好。用户可以随时调用函数而不需要考虑转型问题
  - 使用C++转型，不要用旧式

- 个人总结

#### 28避免返回handles指向对象内部成分：Avoid returning "handles" to object internals

- 原因
  - 返回引用和指针的时候，可能会指向内部的private级别的变量。也就是破坏了封装性
- 解决
  - const Point& upper_func( ) const {return data->object; }
- 总结
  - 尽量避免返回handles（包括引用，指针，迭代器）指向对象的内部。保证封装性。
- 个人总结
  - 这个是看情况而定，有一定开发经验才能决定
  - 因为有些时候需要返回一个引用，方便调用

#### 29为 异常安全 而努力是值得的：Strive for exception-safe code

- 原因
  - 一段没有异常安全的代码会发生以下问题
  - 泄露的资源
  - 数据败坏，数据无用
- 解决
  - 资源泄漏，通过构造和析构函数解决
  - 异常安全函数三个保证
    - 基本保证
    - 强烈保证
    - 不抛出异常
- 总结
  - 异常安全函数，即使发生异常也不会泄露资源或允许任何数据结构败坏。这样的函数区分为三种可能的保证
    - 基本型
    - 强烈型
    - 不抛异常型
  - 强烈保证往往能够以 copy-and-swap 实现出来，但 强烈保证 并非对所有函数都可实现或具备现实意义
  - 函数提供的 异常安全保证 通常最高只等于其所调用之各个函数的 异常安全保证 中的最弱者
- 个人总结

#### 30透彻了解inlining的里里外外：Understand the ins and outs of inlining

- 原因
- 解决
- 总结
- 个人总结

#### 31将文件间的编译依存关系降至最低：Minimize compilation dependencies between files

- 原因
- 解决
- 总结
- 个人总结

### 继承与面向对象设计

### 模版与泛型编程

### 定制new和delete



[TOC]

