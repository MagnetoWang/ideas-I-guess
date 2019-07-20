## 说明

## 目录

[TOC]



## Java解决方案

### 异常

#### 异常介绍

- https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/

#### 只读异常

- ReadOnlyBufferException
- Unchecked exception thrown when a content-mutation method such as `put` or `compact` is invoked upon a read-only buffer.
- **1) Checked:** are the exceptions that are checked at compile time. If some code within a method throws a checked exception, then the method must either handle the exception or it must specify the exception using *throws* keyword.
- **2) Unchecked** are the exceptions that are not checked at compiled time. In C++, all exceptions are unchecked, so it is not forced by the compiler to either handle or specify the exception. It is up to the programmers to be civilized, and specify or catch the exceptions.
- In Java exceptions under *Error* and *RuntimeException* classes are unchecked exceptions, everything else under throwable is checked.
- Throwable
  - Error:unchecked
  - Exception
    - checked
    - RuntimeException:unchecked

#### 并发

- java.util.concurrent.TimeoutException
  - http://www.blogjava.net/xylz/archive/2011/07/12/354206.html	
  - 此异常是用来描述任务执行时间超过了期望等待时间，也许是一直没有获取到锁，也许是还没有执行完成。

### 代码规范

- 类名：每个单词首字母大写
  - ToPdf
- 方法名：动词+名词，动词小写，名词首字母大写
- 变量名：名词，首字母小写，多个单词的话，在后面单词每个首字母大写

### 编写规范

- 头脑要清醒
- 在引用jar包的时候，要保证jar包的内容不影响目前的项目
  - 创建文件的例子，因为jar里面也在创建文件，所有导致总是有某名的文件跟着一起创建，影响开发和差错
- 不要随意在finally里填写想当然的代码
  - 在文件打开的时候，然后又close文件，这个操作非常愚蠢，因为你不知道其他哪个地方需要继续调用这个文件
- 在多个项目编程，特别容易弄混编译哪个jar包
  - 在command 引用jar包总是编译了另一个包，浪费了大量 的无效时间
  - 配置太多，后面要定个编写流程规范，每一步都应该到位才行
- 函数参数
  - 参数的数据类型，就是表示你要输入的数据类型应该是什么，不要模糊了数据类型，也不要随意强制转型
- 数据类的定义
  - 不要重复定义两个功能相同的类，后面调用真的很麻烦麻烦
  - schema.ColumnDesc

### maven

- 发布jar包，跳过测试单元
  - mvn clean install -Dmaven.test.skip=true
- 执行jar包
  - 有main入口，需要在pom里面指定，有时候可能会影响项目的整体性
  - java -jar myjar.jar
  - 没有main入口
  - java -cp xxx.jar xxx.xxx.MainClass(src中有main的入口类)
- jar的可执行
  - 如果涉及到外部包的依赖，一定要添加插件
  - https://blog.csdn.net/change_on/article/details/79379400

#### maven命令总结

- 参考资料：<http://www.mojohaus.org/exec-maven-plugin/>

```
mvn clean install -Dmaven.test.skip=true

打包跳过测试
mvn package -Dmaven.test.skip=true

发布跳过测试
mvn deploy -Dmaven.test.skip=true
```



#### 发布含main入口的jar包

```
在pom里面添加插件并制定jar包入口
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <classpathPrefix>./lib/</classpathPrefix>
                            <!--<classpathPrefix>/RELATION/appuser/test_tools/lib/</classpathPrefix>-->
                            <!--<classpathPrefix>/home/work/tools/lib/</classpathPrefix>-->
                            <mainClass>com._4paradigm.predictor.demo.JprofilerTest</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            
在pom.xml目录下执行
mvn clean install -Dmaven.test.skip=true
```

#### 找maven的settings.xml位置

- 参考资料：https://stackoverflow.com/questions/9988814/how-do-i-find-out-which-settings-xml-file-maven-is-using
- mvn -X

#### maven执行指定具体的测试用例

```
java 测试框架
修改java-ut 中的代码，Dtest可以更改成具体的类


mvn clean test -Dtest=xxx包名.*Test,package_xxx.test_xxx

*Test 执行后缀为Test
```



### 命令行下执行Java项目整个过程

- 参考链接：https://blog.csdn.net/qbg19881206/article/details/19850857
- mvn compile
- mvn exec:java -Dexec.mainClass="rtidbperf.RtidbClusterTest"

```
执行代码传递参数
mvn exec:java -Dexec.mainClass="com.vineetmanohar.module.Main" -Dexec.args="arg0 arg1 arg2"

指定classpath运行依赖
mvn exec:java -Dexec.mainClass="com.vineetmanohar.module.Main" -Dexec.classpathScope=runtime

获取exec其他说明帮助
mvn exec:help -Ddetail=true -Dgoal=java

结合jprofiler使用
mvn exec:java -Dexec.mainClass="com._4paradigm.predictor.demo.JprofilerTest" -agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849


Java执行jar包
java -cp xxx.jar xxx.Main
```



### 命令行下创建完整java项目

- 参考链接：<https://www.cnblogs.com/yjmyzz/p/3495762.html>
- 四个步骤
- mvn archetype:generate
- 按回车，跳过Choose a number or apply filter这个
- 填写groupID等信息，就行了，可以填com.magnetowang
- 注意填写package的时候，写的是包名
- 选择*package*， jar或者war

```
<groupId>com.maven.JavaGraphics</groupId>
 <artifactId>ComputerGraphics</artifactId>
  <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

  <name>ComputerGraphics</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
  
解释
groupId 定义了项目属于哪个组，举个例子，如果你的公司是mycom，有一个项目为myapp，那么groupId就应该是com.mycom.myapp. 

artifacted 定义了当前maven项目在组中唯一的ID,比如，myapp-util,myapp-domain,myapp-web等。 

version 指定了myapp项目的当前版本，SNAPSHOT意为快照，说明该项目还处于开发中，是不稳定的版本。 

name 声明了一个对于用户更为友好的项目名称，不是必须的，推荐为每个pom声明name，以方便信息交流。 
```



### 自定义一个异常类并使用

- myException 继承 Exception
- 初始化的时候，要super()
- 定义serialVersionUID 全局唯一

how to throw an exception 或者 如何传递异常

- 原理：强烈建议看 java核心编程第一卷的异常章节，讲的非常详细！
- 代码实现：https://www.webucator.com/how-to/how-throw-an-exception-java.cfm
- 过程
  - throw new Exception()
  - catch exception

### 从只读的bytebuffer获取字符串

- 借助char[] ，然后转化成string
- https://stackoverflow.com/questions/23552114/extract-string-from-readonly-java-nio-bytebuffer
- 这个问题困扰8个小时了

### Copy-On-Write的并发写入原理

- 参考文章：https://coolshell.cn/articles/11175.html
- 针对一个对象
- 可以让多个线程共享读
- 但是
- 当要对这个对象进行修改或者写入新数据的时候
- 会对这个对象加锁，防止其他线程进行修改
- 然后，复制一个新的对象，在新的对象里进行修改
- 其他的线程，仍然读旧的对象
- 新的对象修改完成后，就会把旧对象的指针指向新对象
- 缺点
  - 因为有复制的过程
  - 一旦对象过大
  - 容易引起内存不足的问题，或者Java中的GC问题
  - 数据一致性，很明显，写的过程中，不保证读读线程实时更新数据。所以不能保证强一致性，只能保证最终一致性
- 优点
  - 只在写的时候执行延时懒惰策略
  - 读的时候不加锁

### Gradle

#### 参考链接

- 安装页面：<https://gradle.org/install/>

#### 安装编译运行

```
mac平台
brew install gradle

编译
chmod +x gradlew
./gradlew
```

## Java语法

### 函数参数传递的一些问题

```
对象传入
```

### var的使用

- <https://segmentfault.com/a/1190000017083955>

### Objects.equals的使用

- 资料：<https://www.jianshu.com/p/31ce2ce3eef1>
- 判断两个对象的引用是否相等

## Java类的使用

### Future

- 用于多线程场景使用，异步操作，非阻塞模型
- 基本介绍：https://blog.csdn.net/u014209205/article/details/80598209

#### 实战

- 定义future类，存放我们的操作变量
- 定义callable类，存放通信的消息子，也就是用来通知程序运行结果，以及监控程序的运行状态
- 定义Executors类，存放线程实例
- Executors 要登记 callable 
- callable里面有要操作的动作
- future类变量，获取 Executors submit 的信息。也就是说分配这个动作信息给future
- future之后将会做一系列动作，然后接收返回结果到future变量中
- 我们可以通过打印future变量，获取结果信息



### ByteBuffer

- 常用的缓冲区
- 信道的读写方法只接收ByteBuffer
- 图解：https://my.oschina.net/flashsword/blog/159613
- 文档
  - http://tutorials.jenkov.com/java-nio/buffers.html
  - https://docs.oracle.com/javase/7/docs/api/java/nio/ByteBuffer.html

#### 实战

- ByteBuffer buffer=ByteBuffer.allocate(256);
- 更常用的是从byte获取
-  ByteBuffer buffer=ByteBuffer.wrap(byteArray);
- byte类似于一个中间类型，是bytebuffer的桥梁
- buffer.clear(); 清楚数据，实际只是变更索引值，回到第一个位置，之后重写数据
- bytebuffer to byte ： buffer.get(new byte[6])   String value = new String(byte);
- Byte to bytebuffer :    ByteBuffer.wrap(byteArray);  buffer.put(byteArray)



### Builder

- 一般用于创建对象同时配置对象的内容
- 我在google的proto 里面正好用到这个builder
- 不深究，直接使用proto生成的Java代码即可

#### 实战

- .build()方法之后，一般直接生成好了对象。不能再进行set相关函数配置
- 如果要动态配置build，就需要Builder对象，然后set配置。set相关内容后，才能build最终对象出来

### ThreadLocal

- 参考资料：<http://www.cnblogs.com/lintong/p/4373876.html>

```
在static中创建好共享变量
```



### Lamda表达式

- <https://blog.csdn.net/renfufei/article/details/24600507>

### HashMap

- map.entry的使用：<https://www.cnblogs.com/guanjie20/p/3769772.html>

```
map可以直接返回key集合，也可以直接返回pair<k, v>集合用于遍历。map.entry就是返回键值对

 Iterator<Map.Entry<String, List<String>>> entrys = multiString.entrySet().iterator();
 返回一个迭代器，可以用于遍历
 
```

- 匿名内部类的使用方法：<https://www.cnblogs.com/xdouby/p/5890083.html>

```
Map<String, Object> map = new HashMap<String, Object>() {
    　　{
        　　put("name", "June");  
       　　 put("age", 12);  
    　　}
　　};
　　
　　这种方式可以初始化hashmap
　　
　　外层的一组“{}”表示的是一个匿名类，内层的一对“{}”表示的是实例初始化块，然后这边还有一点需要明白，实例初始化块的代码在编译器编译过后，是放在类的构造函数里面的，并且是在原构造函数代码的前面。
```



## Redis

### 资料

- 命令行端练习：<http://try.redis.io/>
- 快速入门：<https://redis.io/topics/quickstart>
- 代码入门：<https://www.runoob.com/redis/redis-java.html>
- 官方文档：<https://redis.io/>
- info命令配置中文说明：<http://redisdoc.com/client_and_server/info.html>
- redis-cli使用：<https://www.cnblogs.com/kongzhongqijing/p/6867960.html>
- redie faq：<https://redis.io/topics/faq>

### 特点

- 单线程内存操作
- 异步写入数据

### 服务端

```
启动服务器最大连接
redis-server --maxclients 100000

SET server:name "fido"
```



### 客户端

```
查看内存
info memory

查看数据量
dbsize

//删除当前数据库中的所有Key
flushdb

//删除所有数据库中的key
flushall

//下面的命令指定数据序号为0，即默认数据库
redis-cli -n 0 keys "*" | xargs redis-cli -n 0 del

如果要指定 Redis 数据库访问密码，使用下面的命令
redis-cli -a password keys "*" | xargs redis-cli -a password del
```

### 问题

#### redis无法连接远程服务器

```
参考资料
https://www.cnblogs.com/y-l-h/p/7930085.html

修改配置文件
1、修改redis服务器的配置文件  

注释以下绑定的主机地址  
# bind 127.0.0.1  
  
2、修改redis服务器的参数配置  
  
修改redis的守护进程为no ，不启用  
daemonize no

修改redis的保护模式为no，不启用  
protected-mode no
```



## JMeter

### 资料

- 中文文档：<http://www.testclass.net/jmeter/jmeter-doc-01/>
- 入门教程：https://www.jianshu.com/p/0e4daecc8122
- 入门教程：<http://www.cnblogs.com/zhangchaoyang/articles/2530731.html>
- 官网：<https://jmeter.apache.org/>
- 高阶教程： <https://www.jianshu.com/p/0e4daecc8122>
- java编程使用JMeter示例： <https://www.jianshu.com/p/a88e5cb1d6cb>
- Java请求：<https://www.cnblogs.com/yangxia-test/p/4019541.html>
- jmeter系列文章：<https://www.cnblogs.com/yangxia-test/category/431240.html>
- 多场景并发测试：<https://blog.csdn.net/laofashi2015/article/details/78552663>
- 在jmeter情况下，修改jvm参数：<http://jmeter.apache.org/usermanual/get-started.html>

### Demo

```
修改jvm参数
JVM_ARGS="-Xms1024m -Xmx1024m" jmeter -t test.jmx [etc.]

```



## 问题

### 命令端

#### no main manifest attribute

- 在执行jar包缺少main入口的原因

#### Error: Could not find or load main class clean

- 

#### Couldn't destroy threadgroup org.codehaus.mojo.exec.ExecJavaMojo$IsolatedThreadGroup[name=rtidbperf.RtidbClusterTest,maxpri=10]

- 参考链接：https://stackoverflow.com/questions/13471519/running-daemon-with-exec-maven-plugin-avoiding-illegalthreadstateexception

### NoClassDefFoundError和ClassNotFoundException区别

- <https://www.cnblogs.com/xyhz0310/p/6803950.html>
- 前者属于编译时期加载类出现的错误，后者属于运行时期加载类出现的错误

## 自动化脚本

### Java安装-非root情况

```
mkdir java
cd java
wget http://pkg.4paradigm.com/jdk/jdk-8u141-linux-x64.tar.gz
tar -zxvf jdk-8u141-linux-x64.tar.gz


echo 'export JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141'>>~/.bash_profile
echo 'export PATH=$PATH:/home/wangzixian/java/jdk1.8.0_141/bin'>>~/.bash_profile

echo 'export JRE_HOME=home/wangzixian/java/jdk1.8.0_141/jre'>>~/.bash_profile
echo 'export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib'>>~/.bash_profile
source ~/.bash_profile
java -version

vi ~/.bash_profile
```

### maven安装-非root情况

```
mkdir maven
cd maven

export MAVEN_HOME=/home/wangzixian/maven/apache-maven-3.5.4
export PATH=${MAVEN_HOME}/bin:${PATH}
```

## 技巧

### 如何编写可灵活的配置类

- 参考brpc客户端Optiona

```
this.loadBalanceType = LoadBalanceType.ROUND_ROBIN.getId();
```



## 常用代码片段

### 打印logger

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

private final static Logger logger = LoggerFactory.getLogger(TabletClientImpl.class);

maven包
<!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-api -->
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>1.7.25</version>
</dependency>
```



### 线程睡眠

- Thread.sleep(200);



# 新的章节

## Yaml语法

### 参考资料

- 类似与xml的文件：<https://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/index.html>
- 官网：<http://www.yaml.org/>
- Java版本：<http://jyaml.sourceforge.net/tutorial.html>

### 总结

```
语法
Structure通过空格来展示。Sequence里的项用"-"来代表，Map里的键值对用":"分隔.

比如
name: John Smith
age: 37
spouse:
    name: Jane Smith
    age: 25
children:
    -   name: Jimmy Smith
        age: 15
    -   name: Jenny Smith
        age 12
```



## Google Guava Collections

### 参考资料

- 使用介绍：<https://www.ibm.com/developerworks/cn/java/j-lo-googlecollection/index.html>



## Testng

### 参考资料

- 官网：<http://testng.org/doc/index.html>



[TOC]


