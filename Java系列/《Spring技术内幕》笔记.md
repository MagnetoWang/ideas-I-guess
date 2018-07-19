![spring内幕笔记](https://github.com/MagnetoWang/ideas-I-guess/blob/master/markdown-for-document-organization-management/manage-pictures/java-spring-notes.png)

## Spring的设计理念
spring 的目标和愿景

## Spring Framework的核心: IoC容器的实现
### IoC特点
- 降低了框架的侵入性
- 使用POJO来完成开发
- 各个模块的依赖关系通过IoC配置文件进行描述
- 让应用开发面向接口编程
- 不与第三方的解决方案竞争，而是更好的集成
- 减少Spring API的依赖
- 优点
  - 把应用从复杂的对象依赖关系管理中解放出来
  - 减少对象依赖的关系和系统运行的状态关联性
  - 新建对象，赋值对象交给容器统一完成
  - 对象的关系，不会被程序运行的状态随意破坏

### 依赖反转
- 也叫依赖注入
- 依赖对象的获得被反转
- 反转的体现
  - 在一个非常优秀的应用中，每个对象之间需要互相合作
  - 互相合作的前提是：对象要能获取它想要的对象，或者说要能调用它想合作的对象
  - 那么如果在这个获取对象的过程，需要自身实现，对于整个代码的编写难度会增加
  - 这个时候我们需要把反转这个依赖，交给IoC来做这个事情

### IoC实现

- 在对象生成或初始化时直接将数据注入到对象中，也可以将对象引用注入到对象数据域中的方式来注入对方法调用的依赖。
- 注入可以递归的
- 提供了一个基本的JavaBean容器，通过IoC模式管理依赖关系，并通过依赖注入和AOP切面增强了为JavaBean这样的POJO对象赋予事务管理，生命周期等基本功能
- 注入方式
  - setter注入
  - 构造器注入
  - 为了防止注入异常，容器同时提供特定依赖的检查

### IoC容器系列的设计与实现：BeanFactory和ApplicationContext

- BeanFactory：作为最基本的容器实现最基本的功能
  - BeanDefinition：来管理基于Spring的应用中的各种对象以及它们之间的相互依赖关系
  - 抽象了Bean的定义
- ApplicationContext：作为容器的高级形态而存在。应用上下文
  - 支持不同信息源。扩展了messageSource，为开发多语言版本的应用提供服务
  - 访问资源，可以从不同地方得到Bean的定义资源。从而灵活定义Bean定义信息
  - 支持应用事件。继承了ApplicationEventPublisher
  - 风格方面，面向框架编程，支持使用ApplicationContext作为IoC容器的基本形式
  - 设计难点
    - 实例化的时候，要refresh上下文
    - 加载定位所需要的资源

### FactoryBean 和 BeanFactory 的区别

- 

### IoC容器的初始化过程

- 入口是refresh
  - 包括BeanDefintion的Resource定位，载入和注册三个基本过程
  - 三个过程是用不同模块来完成，足见这个三个过程之复杂和重要
  - Resource定位
    - BeanDefinition的资源定位
    - 由ResourceLoader通过统一的Resource接口来完成
    - 容器寻找数据的过程
  - BeanDefinition的载入
    - 把用户已经定义好的Bean表示成IoC容器内部的数据结构
    - 这个容器内部的数据结构就是BeanDefinition
    - BeanDefinition实际就是POJO对象在IoC容器中的抽象
  - 向IoC容器注册这些BeanDefinition的过程
    - 调用BeanDefinitionRegistry接口的实现来完成
    - 解析得到的数据结构向IoC注册
    - 最终注入到HashMap中，通过hashMap来管理
- 依赖注入和载入是分开的
  - 在第一次getBean的时候，才会依赖注入







## 深入探讨

- DefaultListableBeanFactory
- BeanDefinition
- FileSystemXmlApplicationContext
- AbstractApplicationContext
- refreshBeanFactory
- DefaultDocumentLoader
- 































