## 《Effective C++》读书笔记

[TOC]



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

18

19

20

25





[TOC]

