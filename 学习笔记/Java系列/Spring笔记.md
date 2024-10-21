## Spring





### 如何用XML配置Java

#### 阅读记录

- 标签constructor-arg 
  - 用于构造函数配置
  - 可以给构造函数一个默认值
  - 针对list,set系列，也可以用value复制更多默认值
- 标签property 
  - 设置Java方法的属性
  - 用法和constructor-arg 一样
- 标签\<util:list\>
  -  用来配置list集合，这样在bean配置中可以直接通过ID调用。让bean变得更加精炼
  - 类似的参看书Manning.Spring.in.Action.4th.Edition，P59
- @Import，将两个类的配置放在一起。新建一个类，直接导入配置即可
- @ImportResource 加载配置好的xml格式的bean
- 标签<import >可以导入在xml配置中导入其他xml配置
- 标签bean ，可以在xml中配置javaConfig





### 如何转移配置到另外一个开发环境

#### 阅读记录

- @Profile 注解，声明在哪个开发环境。只有在指定环境，被注解的类才能生效。否则会被无视
- 