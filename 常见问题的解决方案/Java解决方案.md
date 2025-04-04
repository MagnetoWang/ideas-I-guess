****

## 说明

## 目录

[TOC]



## Java解决方案

### 资料

- Java泛型高级用法：<http://angelikalanger.com/GenericsFAQ/JavaGenericsFAQ.html>
- java风格检测：http://hoverruan.github.io/blog/2013/06/21/using-maven-checkstyle-plugin/

### 安装Java

```
下载Java包

openjdk 11
wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz



在.bashrc里面配置路径
# Java配置
ROOT=`pwd`
export JAVA_HOME=$ROOT/j2sdk-bundle
export JRE_HOME=$ROOT/j2sdk-bundle/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$PATH:$JAVA_HOME/bin
```

## Maven

### 命令行下的maven

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
mvn clean package -Dmaven.test.skip=true
jar包最终应该在target的目录下

发布跳过测试
mvn clean deploy -Dmaven.test.skip=true

Java集成测试
mvn clean -U compile test

指定某个包的全部测试
mvn clean test  -Dtest=包名.*

显示依赖包的树
mvn dependency:tree

执行main函数
https://www.cnblogs.com/EasonJim/p/6830104.html
mvn exec:java -Dexec.mainClass=xxx

执行有参数的main函数
mvn exec:java -Dexec.mainClass="com.jsoft.test.MainClass" -Dexec.args="arg0 arg1 arg2"

指定测试某个类的单独方法
mvn clean test -Dtest=xxx.xxxTest#方法名

修改项目版本号
mvn versions:set -DnewVersion=1.7.3.9-rc2

打印debug日志
https://blog.csdn.net/iteye_6908/article/details/82522034
mvn clean test -Dtest=xxx.xxxTest#方法名  -X


将项目的依赖都统一放到一个目录下
mvn dependency:copy-dependencies -DoutputDirectory=/xxx/lib


mvn设置离线状态，不用每次从网络下载包，直接用本地即可，提高效率
<updatePolicy>always</updatePolicy>
<updatePolicy>never</updatePolicy>
<updatePolicy>daily</updatePolicy> 每天

```

#### 安装maven

```
wget mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/binaries/apache-maven-3.6.2-bin.zip
wget mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/source/apache-maven-3.6.2-src.tar.gz

unzip apache-maven-3.6.2-bin.zip

wget mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.zip


在bashrc 和 bash_profiler添加配置
# maven路径
export MAVEN_HOME=~/maven/apache-maven-3.6.2
export PATH=${MAVEN_HOME}/bin:${PATH}


配置仓库源，可以拉取jar包速度更快


自动式安装
mvn_version=3.8.8
wget https://mirror.bit.edu.cn/apache/maven/maven-3/$mvn_version/binaries/apache-maven-$mvn_version-bin.tar.gz
mvn_version=3.8.8
tar xvzf apache-maven-$mvn_version-bin.tar.gz
export MAVEN_HOME=`pwd`/apache-maven-$mvn_version
export PATH=${MAVEN_HOME}/bin:${PATH}


安装3.5.4
文档：https://maven.apache.org/docs/3.5.4/release-notes.html
包位置：https://archive.apache.org/dist/maven/maven-3/3.5.4/binaries/
```

#### mvn插件使用

```
maven-dependency-plugin 管理依赖的插件
http://maven.apache.org/plugins/maven-dependency-plugin/build-classpath-mojo.html




```



#### 发布含main入口的jar包，可执行jar包

```
在pom里面添加插件并制定jar包入口
               <build>
        <plugins>
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
                            <mainClass>xxxxx.xxx.UdfTools</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
            
            
上面插件有时候没有生效，可以改用下面这个：https://www.jianshu.com/p/0d85d0539b1a
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <executions>
        <execution>
            <goals>
                <goal>shade</goal>
            </goals>
            <configuration>
             <filters>
                 <filter>
                   <artifact>*:*</artifact>
                   <excludes>
                     <exclude>META-INF/*.SF</exclude>
                     <exclude>META-INF/*.DSA</exclude>
                     <exclude>META-INF/*.RSA</exclude>
                   </excludes>
                 </filter>
               </filters>
                <shadedArtifactAttached>true</shadedArtifactAttached>
                <transformers>
                    <transformer implementation=
                      "org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                        <mainClass>com.michealyang.jetty.embeded.EmbeddedJettyServer</mainClass>
                </transformer>
            </transformers>
        </configuration>
        </execution>
    </executions>
</plugin>

            
在pom.xml目录下执行
mvn clean install -Dmaven.test.skip=true
mvn clean package -Dmaven.test.skip=true


执行jar包
java -Dfile.encoding=UTF-8 -cp xxx.jar xxx.Main
```

#### 整合项目所有的依赖包，放到一个目录下

```
添加相关插件
mvn clean package

<plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-dependency-plugin</artifactId>
                <executions>
                    <execution>
                        <id>copy</id>
                        <phase>package</phase>
                        <goals>
                            <goal>copy-dependencies</goal>
                        </goals>
                        <!--<configuration>-->
                        <!--<outputDirectory>${project.build.directory}/lib-->
                        <!--</outputDirectory>-->
                        <!--</configuration>-->
                    </execution>
                </executions>
            </plugin>
            
          
 spark插件参考
  <!-- This plugin dumps the test classpath into a file -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <executions>
          <execution>
            <id>generate-test-classpath</id>
            <phase>test-compile</phase>
            <goals>
              <goal>build-classpath</goal>
            </goals>
            <configuration>
              <includeScope>test</includeScope>
              <outputProperty>test_classpath</outputProperty>
            </configuration>
          </execution>
          <execution>
            <id>copy-module-dependencies</id>
            <phase>${build.copyDependenciesPhase}</phase>
            <goals>
              <goal>copy-dependencies</goal>
            </goals>
            <configuration>
              <includeScope>runtime</includeScope>
              <outputDirectory>${jars.target.dir}</outputDirectory>
            </configuration>
          </execution>
        </executions>
      </plugin>
```

#### maven-dependency-plugin

```
maven-dependency-plugin


三种标签情况
删除某个包的依赖
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <version>3.2.0</version>
        <executions>
          <execution>
            <id>analyze</id>
            <goals>
              <goal>analyze-only</goal>
            </goals>
            <configuration>
              <failOnWarning>true</failOnWarning>
 
 
              <!-- ignore jsr305 for both "used but undeclared" and "declared but unused" -->
              <ignoredDependencies>
                <ignoredDependency>com.google.code.findbugs:jsr305</ignoredDependency>
              </ignoredDependencies>
 
              <!-- ignore annotations for "used but undeclared" warnings -->
              <ignoredUsedUndeclaredDependencies>
                <ignoredUsedUndeclaredDependency>com.google.code.findbugs:annotations</ignoredUsedUndeclaredDependency>
              </ignoredUsedUndeclaredDependencies>
 
              <!-- ignore annotations for "unused but declared" warnings -->
              <ignoredUnusedDeclaredDependencies>
                <ignoredUnusedDeclaredDependency>com.google.code.findbugs:annotations</ignoredUnusedDeclaredDependency>
              </ignoredUnusedDeclaredDependencies>
            </configuration>
          </execution>
        </executions>
      </plugin>
```

#### Maven-source-plugin

```
maven-source-plugin：打包的时候附带源码

         <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-source-plugin</artifactId>
                <executions>
                    <execution>
                        <id>attach-sources</id>
                        <phase>package</phase>
                        <goals>
                            <goal>jar-no-fork</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
 执行 mvn install，maven会自动将source install到repository 。
 执行 mvn deploy，maven会自动将source deploy到remote-repository 。
 执行 mvn source:jar，单独打包源码。
 注意：在多项目构建中，将source-plugin置于顶层或parent的pom中并不会发挥作用，必须置于具体项目的pom中。 
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

#### maven指定settings.xml
```
mvn -s YourOwnSettings.xml clean package


```

#### maven编译子模块
```
https://blog.csdn.net/xingbaozhen1210/article/details/89213789

-pl, --projects
        Build specified reactor projects instead of all projects
-am, --also-make
        If project list is specified, also build projects required by the list
-amd, --also-make-dependents
        If project list is specified, also build projects that depend on projects on the list


mvn install -pl xxx/xxx -DskipTests


```

#### maven依赖下的jar包冲突

```
资料：https://blog.csdn.net/andyzhaojianhui/article/details/51446413

推荐两个方法，
1，把要声明的jar包放到最前面
2，用exclued标签来剔除不应该依赖的jar包

<exclusions>
          <exclusion>
              <artifactId>log4j-over-slf4j</artifactId>
              <groupId>org.slf4j</groupId>
          </exclusion>
          </exclusions>
```

#### maven红线太多了

```
find ~/.m2  -name "*.lastUpdated" -exec grep -q "Could not transfer" {} \; -print -exec rm {} \;
```



#### 解决全局时区问题

```
mvn clean -U -Duser.timezone=Asia/Shanghai compile test
```

#### maven的jar包作用域

```
 <dependxxx
            <groupId>com.xxxx</groupId>
            <artifactId>xxx</artifactId>
            <version>${xxx.version}</version>
            <!--<scope>test</scope>-->
        </dependency>
        
scope 会让jar包只在test目录下有效，main中无法引用。这样方便测试

 
```

#### 编译protobuf前需要清理环境

```
mvn clean idea:idea -DskipTests
```



#### debug的方法

```
mvn跑test的时候，经常报错，但是无法在命令行端debug
可是日志信息是打不全的，这个时候需要用throw的方式，把异常信息栈打印出来
因为用println的方式，会无穷无尽，无法快速定位，必须找到问题的根源所在

try {
            builder = xxx
        } catch (Exception e) {
                e.printStackTrace();
                throw e;
        }

2020-11-15 11:43:46 INFO  xxxx
java.lang.NullPointerException
    xxxxxx
    xxxx

```

### maven进阶

#### idea报错

```
idea创建第一个maven项目报错：Cannot resolve plugin org.apache.maven.plugins:maven-clean-plugin:2.5

要对齐.m2的配置！！！
不要下载错了
```



#### 打包指定不要哪些包，哪些类，哪些资源

```
用maven-shade-plugin 插件可以选择性要哪些包，和不要哪些包
filters 可以过滤掉下载的依赖包里面，不要哪些资源。需要把全路径写清楚，不支持递归找文件

<plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>2.4.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer
                                        implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                                <transformer
                                        implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>${mainClass}</mainClass>
                                </transformer>
                            </transformers>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                                <filter>
                                	依赖jar包的全名
                                    <artifact>xxx:ccccc</artifact>
                                    <excludes>
                                        <exclude>nlp/dict/*</exclude>
                                        <exclude>nlp/dict/part_speech/*</exclude>
                                        <exclude>nlp/dict/sentiment/*</exclude>
                                        <exclude>nlp/dict/name_entity/*</exclude>
                                        <exclude>nlp/models/*</exclude>
                                        <exclude>nlp/performance/*</exclude>
                                        <exclude>natives/linux_64/*</exclude>
                                        <exclude>dict/*</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                            <relocations>
                                <relocation>
                                    <pattern>com.google.protobuf</pattern>
                                    <shadedPattern>shade.protobuf</shadedPattern>
                                </relocation>
                                <relocation>
                                    <pattern>com.google.common</pattern>
                                    <shadedPattern>shade.guava</shadedPattern>
                                </relocation>
                            </relocations>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
```



## Gradle
1. 深入了解gradle和maven的区别：https://cloud.tencent.com/developer/article/1787010
2. gradle跑测试用例：https://www.jetbrains.com/help/idea/work-with-tests-in-gradle.html

### 安装编译运行
```
加上代理如
systemProp.http.proxyHost=xx.74.xx.8
systemProp.http.proxyPort=xxx
systemProp.http.nonProxyHosts=localhost,127.0.0.1,localaddress
systemProp.https.proxyHost=xxx.74.xxx.xxx
systemProp.https.proxyPort=xxx

```


## JAVA版本的区别
1. java 17优势
   1. 语法变化：https://juejin.cn/post/7019952895999246366 
2. java 15优势
   1. 语法变化：https://www.cnblogs.com/javastack/p/13683220.html
3. java 11优势
   1. 语法变化：https://segmentfault.com/a/1190000016537503
```
package javafx.util does not exist
openJDK 没用这个包
改成oracle1.8 201解决

jdk11 以下不支持 repeat方法
separator += "-".repeat(width) + "-+-";

```
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
    - RuntimeException:
    
#### 打印异常栈
```
import org.apache.commons.lang3.exception.ExceptionUtils;

String r = ExceptionUtils.getStackTrace(e);

```

#### 打印异常栈的版本号
```


```

#### 并发

- java.util.concurrent.TimeoutException
  - http://www.blogjava.net/xylz/archive/2011/07/12/354206.html	
  - 此异常是用来描述任务执行时间超过了期望等待时间，也许是一直没有获取到锁，也许是还没有执行完成。

### 代码规范

- 类名：每个单词首字母大写
  - ToPdf
- 文件名：同类名
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


### 命令行下的Java

```
安装jdk
tar xzvf xxx

export JAVA_HOME=`pwd`/jdk1.8.0_141
export JRE_HOME=`pwd`/jdk1.8.0_141/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$PATH:`pwd`/jdk1.8.0_141/bin

wget xxx
tar xzvf xxxx
export JAVA_HOME=`pwd`/jdk
export JRE_HOME=`pwd`/jdk/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$PATH:`pwd`/jdk/bin
```



#### 命令行下执行Java项目整个过程

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
java -Dfile.encoding=UTF-8 -cp xxx.jar xxx.Main

解压jar包
unzip xxxx.jar

查看java加载包的日志
java -verbose:class

java依赖打印
mvn dependency:tree -Dverbose > tree.txt
```

#### Java加载类终极解决方案

```
直接执行
java -Dfile.encoding=UTF-8 -cp xxx.jar xxx.Main
经常会出现找不到包之类的问题

原因是需要配置classpath，把相关的所有类全部写到classpath中
export CLASSPATH=xxx


但是java -cp还是报错没有加载成功

```



#### 查看jdk路径

```
java -verbose
```



#### 命令行下创建完整java项目

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

#### 日志配置

```
log4j.rootLogger=INFO,console
log4j.additivity.org.apache=true

# console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.Threshold=INFO
log4j.appender.console.ImmediateFlush=true
log4j.appender.console.Target=System.out
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%p] %C{1} %L-%m%n

# spark log
log4j.logger.org.apache.spark=ERROR,console
log4j.logger.org.spark_project.jetty=ERROR,console





```

#### 日志 在idea上不生效
```
    private static final Logger LOG = LoggerFactory.getLogger(PlannerTest.class);

加pom依赖，然后再试试
 <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.30</version>
        </dependency>
        <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
            <version>1.7.30</version>
        </dependency>

```

#### 实现命令行工具

```
基本使用：https://www.cnblogs.com/widget90/p/10528620.html
文档：https://www.tutorialspoint.com/commons_cli/commons_cli_pdf_version.htm
```

#### 反编译

```
通过jdk自带的javap方法查看经过计算的class文件：
命令：javap -verbose XXX.class
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

### slf4j注解

```
先统一删除子依赖包
[INFO] |  |  +- org.slf4j:slf4j-log4j12:jar:1.7.10:compile
[INFO] |  +- org.slf4j:slf4j-api:jar:1.6.6:compile
[INFO] |  |  +- org.apache.logging.log4j:log4j-slf4j-impl:jar:2.12.1:test
[INFO] |  |  +- org.slf4j:slf4j-log4j12:jar:1.7.10:compile

[INFO] |  |  +- org.apache.logging.log4j:log4j-slf4j-impl:jar:2.12.1:test
[INFO] |  |  +- org.apache.logging.log4j:log4j-api:jar:2.12.1:compile
[INFO] |  |  \- org.apache.logging.log4j:log4j-core:jar:2.12.1:compile
[INFO] |  |  +- log4j:log4j:jar:1.2.17:compile
[INFO] |  |  +- org.slf4j:slf4j-log4j12:jar:1.7.10:compile

                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-log4j12</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-api</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.apache.logging.log4j</groupId>
                    <artifactId>log4j-slf4j-impl</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.apache.logging.log4j</groupId>
                    <artifactId>log4j-api</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>org.apache.logging.log4j</groupId>
                    <artifactId>log4j-core</artifactId>
                </exclusion>
                <exclusion>
                    <groupId>log4j</groupId>
                    <artifactId>log4j</artifactId>
                </exclusion>

https://blog.csdn.net/HeatDeath/article/details/79833880

<!--可以引入日志 @Slf4j注解-->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.22</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.25</version>
    <scope>compile</scope>
</dependency>
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.12</version>
</dependency>

@Slf4j
用log变量即可
但是idea需要额外的插件lombok才行

所以我觉得还是用传统方法好些

打印的日志可以修改格式
https://ln0491.github.io/2017/01/03/%E6%97%A5%E5%BF%97%E7%BB%84%E4%BB%B6slf4j%E4%BB%8B%E7%BB%8D%E5%8F%8A%E9%85%8D%E7%BD%AE%E8%AF%A6%E8%A7%A3/

log4j2.xml的配置
<?xml version="1.0" encoding="UTF-8"?>

<!-- Don't forget to set system property
-DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector
     to make all loggers asynchronous. -->

<Configuration status="INFO">
    <Appenders>

        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n" />
            <!--<PatternLayout pattern="%d %p [%t]\t%m%n" />-->
            <!--<PatternLayout pattern="%d [%-6p] %C{1}.%M – %m%n" />-->
        </Console>
    </Appenders>
    <Loggers>
        <Root level="info" includeLocation="false">
            <AppenderRef ref="Console" />
        </Root>
    </Loggers>
</Configuration>

log4j.properties
### 设置###
log4j.rootLogger = info,stdout,D,E

### 输出信息到控制抬 ###
log4j.appender.stdout = org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target = System.out
log4j.appender.stdout.layout = org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern = [%-5p] %d{yyyy-MM-dd HH:mm:ss,SSS} method:%l %m%n

### 输出DEBUG 级别以上的日志到=logs/error.log ###
log4j.appender.D = org.apache.log4j.DailyRollingFileAppender
log4j.appender.D.File = logs/log.log
log4j.appender.D.Append = true
log4j.appender.D.Threshold = DEBUG 
log4j.appender.D.layout = org.apache.log4j.PatternLayout
log4j.appender.D.layout.ConversionPattern = %-d{yyyy-MM-dd HH:mm:ss}  [ %t:%r ] - [ %p ]  %m%n

### 输出ERROR 级别以上的日志到=logs/error.log ###
log4j.appender.E = org.apache.log4j.DailyRollingFileAppender
log4j.appender.E.File =logs/error.log 
log4j.appender.E.Append = true
log4j.appender.E.Threshold = ERROR 
log4j.appender.E.layout = org.apache.log4j.PatternLayout
log4j.appender.E.layout.ConversionPattern = %-d{yyyy-MM-dd HH:mm:ss}  [ %t:%r ] - [ %p ]  %m%n



```



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


### 文件读写

```
简单例子：https://blog.csdn.net/jiangxinyu/article/details/7885518
一行一行的读
BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("ming.txt")));
String data = null;
while((data = br.readLine())!=null)
{
System.out.println(data);
}

文件写 写文件的路径是相对还是绝对要思考清楚
String dataPath = dataFile.getParent();
        File spiltFile = new File(dataPath, "behaviourTable--1.csv");
        if (!spiltFile.createNewFile()) {
            return;
        }
        int index = 2;
        FileOutputStream in = new FileOutputStream(spiltFile);
        in.write(schema.getBytes());
        in.write("\n".getBytes());
        for (int i = 0; i < csv.size(); i++) {
            if (i % size == 49) {
                in.close();
                spiltFile = new File(dataPath, "behaviourTable--" + index + ".csv");
                index++;
                in = new FileOutputStream(spiltFile);
                in.write(schema.getBytes());
                in.write("\n".getBytes());
            }
            in.write(csv.get(i).getBytes());
            in.write("\n".getBytes());
        }
        in.close();


```

### JNI-Java调用本地库

```
jni数据类型：https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/types.html
入门jni-推荐：https://developer.ibm.com/tutorials/j-jni/
c++调用Java：https://developer.ibm.com/tutorials/j-jni/#c-and-c-implementations-compared
调用c++方法：https://www.cnblogs.com/jaejaking/p/6840530.html
jni调用c++类：https://blog.csdn.net/xiaohan2909/article/details/50152997
工具包：https://github.com/scijava/native-lib-loader
jni传递map结构：
	https://blog.csdn.net/u014449046/article/details/79188013
	http://www.voidcn.com/article/p-dvjdodew-bqv.html

在src/main/java下
javah -classpath . com.xxx.xxx.xxx.类名

jni生成头文件：https://www.cnblogs.com/virgosnail/p/10711165.html
jni的所有接口方法-相当于函数字典：https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/functions.html
jni一维数组基本数据类型操作：https://blog.csdn.net/xiewenhao12/article/details/79098895

jni.h：https://github.com/LeeKamentsky/python-javabridge/issues/28
需要添加jdk的include
jni_md.h：https://coderanch.com/t/450630/java/jni-md-file-directory-Error
在jdk的include里面还有一个linux的include，在进去看就有这个文件

加载动态库path修改：https://examples.javacodegeeks.com/java-basics/java-library-path-what-is-it-and-how-to-use/

linux下 在LD_library_path 下添加路径即可

typedef union jvalue { 
    jboolean z; 
    jbyte    b; 
    jchar    c; 
    jshort   s; 
    jint     i; 
    jlong    j; 
    jfloat   f; 
    jdouble  d; 
    jobject  l; 
} jvalue; 

*
 * Class:     xxxx
 * Method:    nativeGetHandler
 * Signature: ([Ljava/lang/String;)J
 */
JNIEXPORT jlong JNICALL xxxx
  (JNIEnv *, jobject, jobjectArray);
  
java的签名只有jobjectArray，字符串数组，那么前面两个的作用是什么呢？
The parameter lists of all these functions have a pointer to a JNIEnv and a jobject, in addition to normal parameters in the Java declaration. The pointer to JNIEnv is in fact a pointer to a table of function pointers. As we’ll see in Step 4, these functions provide the various faculties to manipulate Java data in C and C++.
The jobject parameter refers to the current object. Thus, if the C or C++ code needs to refer back to the Java side, this jobject acts as a reference, or pointer, back to the calling Java object. The function name itself is made by the “Java_” prefix, followed by the fully qualified class name, followed by an underscore and the method name.

注意c++和c在调用指针的时候，语法上有区别，这里只介绍c++使用方法
1. #include "Sample1.h"
 2. #include <string.h>
 3.
 4.JNIEXPORT jint JNICALL Java_Sample1_intMethod
 5.  (JNIEnv *env, jobject obj, jint num) {
 6.   return num * num;
 7. }
 8.
 9. JNIEXPORT jboolean JNICALL Java_Sample1_booleanMethod
10.   (JNIEnv *env, jobject obj, jboolean boolean) {
11.   return !boolean;
12. }
13.
14. JNIEXPORT jstring JNICALL Java_Sample1_stringMethod
15.   (JNIEnv *env, jobject obj, jstring string) {
16.     const char *str = env->GetStringUTFChars(string, 0);
17.     char cap[128];
18.     strcpy(cap, str);
19.     env->ReleaseStringUTFChars(string, str);
20.     return env->NewStringUTF(strupr(cap));
21. }
22.
23. JNIEXPORT jint JNICALL Java_Sample1_intArrayMethod
24.   (JNIEnv *env, jobject obj, jintArray array) {
25.     int i, sum = 0;
26.     jsize len = env->GetArrayLength(array);
27.     jint *body = env->GetIntArrayElements(array, 0);
28.     for (i=0; i<len; i++)
29.     {    sum += body[i];
30.     }
31.     env->ReleaseIntArrayElements(array, body, 0);
32.     return sum;
33. }
34.
35. void main(){}

如果一定要用c语法方法，可改成下面的语法
jsize len = (*env)->GetArrayLength(env,array);


c++的数组转Java数组
https://www.jianshu.com/p/9ad1a7868e11
函数参考
jclass FindClass(JNIEnv *env, const char *name);

jobjectArray NewObjectArray(JNIEnv *env, jsize length,
jclass elementClass, jobject initialElement);

void SetObjectArrayElement(JNIEnv *env, jobjectArray array,
jsize index, jobject value);

jstring NewString(JNIEnv *env, const jchar *unicodeChars,
jsize len);

jstring NewStringUTF(JNIEnv *env, const char *bytes);

The name argument is a fully-qualified class name or an array type signature . For example, the fully-qualified class name for the java.lang.String class is:

                   "java/lang/String"

The array type signature of the array class java.lang.Object[] is:

                   "[Ljava/lang/Object;"



```

## Java进阶

### 文件高级读写

```
参考链接：https://blog.csdn.net/Dream_Weave/article/details/8498853
import org.apache.commons.io.FileUtils;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.File;
import java.io.IOException;
public class Demo {
    public static void main(String args[]) throws IOException {
        File file=new File("mejson");
        String content= FileUtils.readFileToString(file,"UTF-8");
        JSONObject jsonObject=new JSONObject(content);
        System.out.println("姓名是："+jsonObject.getString("name"));
        System.out.println("年龄："+jsonObject.getDouble("age"));
        System.out.println("学到的技能："+jsonObject.getJSONArray("major"));
        System.out.println("国家："+jsonObject.getJSONObject("Nativeplace").getString("country"));
 
    }
}

common-io库：https://blog.csdn.net/Dream_Weave/article/details/84988332

/* 写文件
 * 1.这里只列出3种方式全参数形式，api提供部分参数的方法重载
 * 2.最后一个布尔参数都是是否是追加模式
 * 3.如果目标文件不存在，FileUtils会自动创建
 * */
//static void:write(File file, CharSequence data, String encoding, boolean append) 
FileUtils.write(new File("D:/a/b/cxyapi.txt"), "程序换api","UTF-8",true);
 
//static void:writeLines(File file, Collection<?> lines, boolean append) 
List<String> lines=new ArrayList<String>();
lines.add("欢迎访问:");lines.add("www.cxyapi.com");
FileUtils.writeLines(new File("D:/a/b/cxyapi.txt"),lines,true);
 
//static void:writeStringToFile(File file, String data, String encoding, boolean append) 
FileUtils.writeStringToFile(new File("D:/a/b/cxyapi.txt"), "作者：cxy", "UTF-8",true);

//读文件
//static String:readFileToString(File file, String encoding) 
System.out.println(FileUtils.readFileToString(new File("D:/a/b/cxyapi.txt"), "UTF-8"));
 
//static List<String>:readLines(File file, String encoding) 
System.out.println(FileUtils.readLines(new File("D:/a/b/cxyapi.txt"), "UTF-8")); //返回一个list

//删除目录
//static void:deleteDirectory(File directory) 
FileUtils.deleteDirectory(new File("D:/not/cxyapi"));
 
//static boolean:deleteQuietly(File file) 
FileUtils.deleteQuietly(new File("D:/not/cxyapi")); //文件夹不是空任然可以被删除，永远不会抛出异常

//移动文件 或 文件夹
//static void：moveDirectory(File srcDir, File destDir) 
FileUtils.moveDirectory(new File("D:/cxyapi1"), new File("D:/cxyapi2")); //注意这里 第二个参数文件不存在会引发异常
//static void:moveDirectoryToDirectory(File src, File destDir, boolean createDestDir) 
FileUtils.moveDirectoryToDirectory(new File("D:/cxyapi2"), new File("D:/cxyapi3"), true);
/* 上面两个方法的不同是：
 * moveDirectory：D:/cxyapi2里的内容是D:/cxyapi1的内容。
 * moveDirectoryToDirectory：D:/cxyapi2文件夹移动到到D:/cxyapi3里
 * 
 * 下面的3个都比较简单没提供示例，只提供了api
 * 其中moveToDirectory和其他的区别是 它能自动识别操作文件还是文件夹
 */
//static void:moveFileToDirectory(srcFile, destDir, createDestDir)
//static void:moveFile(File srcFile, File destFile) 
//static void:moveToDirectory(File src, File destDir, boolean createDestDir)


//结果是cxyapi和cxyapi1在同一目录
FileUtils.copyDirectory(new File("D:/cxyapi"), new File("D:/cxyapi1")); 
//结果是将cxyapi拷贝到cxyapi2下
FileUtils.copyDirectoryToDirectory(new File("D:/cxyapi"), new File("D:/cxyapi2"));
 
//拷贝文件
FileUtils.copyFile(new File("d:/cxyapi.xml"), new File("d:/cxyapi.xml.bak"));
//拷贝文件到目录中
FileUtils.copyFileToDirectory(new File("d:/cxyapi.xml"), new File("d:/cxyapi"));
//拷贝url到文件
FileUtils.copyURLToFile(new URL("http://www.cxyapi.com/rss/cxyapi.xml"), new File("d:/cxyapi.xml"));

//判断是否包含文件或者文件夹
boolean b=FileUtils.directoryContains(new File("D:/cxyapi"), new File("D:/cxyapi/cxyapi.txt"));
System.out.println(b);
 
//获得临时目录 和 用户目录
System.out.println(FileUtils.getTempDirectoryPath());
System.out.println(FileUtils.getUserDirectoryPath());
 
//打开流，如果不存在创建文件及其目录结构
//第二个参数表示 文件流是否是追加方式
FileOutputStream fos=FileUtils.openOutputStream(new File("D:/cxyapi/cxyapi.txt"),true);
fos.write(new String("欢迎访问：www.cxyapi.com\r\n").getBytes());
fos.close();
 
//文件 或 文件夹大小
System.out.println(FileUtils.sizeOf(new File("D:/cxyapi")));
System.out.println(FileUtils.sizeOfDirectory(new File("D:/cxyapi")));
```

### Java8-行为参数化，匿名，lambda，流式编程

```
书籍：Java8实战

hashmap foreach遍历：https://blog.csdn.net/w605283073/article/details/80708943
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
     
    public class Test {
     
    	public static void main(String[] args) throws IOException {
     
    		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    		map.put(1, 10);
    		map.put(2, 20);
    		map.forEach((k, v) -> System.out.println("key: " + k + " value:" + v));
    		//scala中写法
    		map.forEach((k, v) => System.out.println("key: " + k + " value:" + v));
    	}
    }
    
    

lamda map用法
xxfunc(Arrays.asList(jars).stream().map(e -> path + "/" + e).collect(Collectors.toList()));


List<TTTT> x;
x.stream().map(TTTT::getMethod).collect(Collectors.toList());



```

### 动态加载jar和类

```
基本思路：https://blog.csdn.net/liuxiao723846/article/details/47441547


【实例3 把上述方法部署到web服务器上，就会抛出异常，需要使用线程上下文类加载器】

URLClassLoader loader = new URLClassLoader(urls);  
//如果用于WEB应用，则需要使用以下构造方法  
//URLClassLoader loader = new URLClassLoader(urls, Thread.currentThread().getContextClassLoader());  


获取一个jar包所有的class：https://www.baeldung.com/jar-file-get-class-names


public static Set<Class> getClassesFromJarFile(File jarFile) throws IOException, ClassNotFoundException {
    Set<String> classNames = getClassNamesFromJarFile(jarFile);
    Set<Class> classes = new HashSet<>(classNames.size());
    try (URLClassLoader cl = URLClassLoader.newInstance(
           new URL[] { new URL("jar:file:" + jarFile + "!/") })) {
        for (String name : classNames) {
            Class clazz = cl.loadClass(name); // Load the class by its name
            classes.add(clazz);
        }
    }
    return classes;
}



注意
注释掉scope或将provided改为compile，因为最后打包提交的时候要用到这个jar包。
provide会导致找不到环境变量的包
```

### 第三方包，多版本共存
```



```


## 并发编程

```
原子递增
https://blog.csdn.net/gong_yangyang/article/details/77281456
错误写法
cnt必须是原子类，但是get和自增两个操作也要保证是合并在一起做的，中间不能插入其他代码，不然无法保证多线程一致性
Object[] row = masterDataSet.get(cnt.get());
cnt ++ ;

正确写法
Object[] row = masterDataSet.get(cnt.getAndIncrement());

原子



```

### 多线程

```
线程总结：https://www.jianshu.com/p/b8197dd2934c

创建线程
class DemoThread extends Thread {

    @Override
    public void run() {
        super.run();
        // Perform time-consuming operation...
    }
}

DemoThread t = new DemoThread();
t.start();


runnable使用方法


线程池使用：https://www.jianshu.com/p/7ab4ae9443b9
public class ThreadPoolTest {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("thread id is: " + Thread.currentThread().getId());
                try {
                    Thread.sleep(1000L);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
        }
    }
}



```

### 线程池

```
线程池原理：https://www.cnblogs.com/dolphin0520/p/3932921.html
public ThreadPoolExecutor(int corePoolSize,int maximumPoolSize,long keepAliveTime,TimeUnit unit,
            BlockingQueue<Runnable> workQueue);
            
            
四种高级线程池：https://zhuanlan.zhihu.com/p/240892588
    Executors.newCachedThreadPool：创建可缓存无限制数量的线程池，如果线程中没有空闲线程池的话此时再来任务会新建线程，如果超过60秒此线程无用，那么就会将此线程销毁。简单来说就是忙不来的时候无限制创建临时线程，闲下来再回收

public static ExecutorService newCachedThreadPool() {
    return new ThreadPoolExecutor(0, Integer.MAX_VALUE, 60L, TimeUnit.SECONDS, new SynchronousQueue < runnable > ());
}

    Executors.newFixedThreadPool：创建固定大小的线程池，可控制线程最大的并发数，超出的线程会在队列中等待。简单来说就是忙不来的时候会将任务放到无限长度的队列里。

public static ExecutorService newFixedThreadPool(int nThreads) {
    return new ThreadPoolExecutor(nThreads, nThreads, 0L, TimeUnit.MILLISECONDS, new LinkedBlockingQueue < runnable > ());
}

    Executors.newSingleThreadExecutor：创建线程池中线程数量为1的线程池，用唯一线程来执行任务，保证任务是按照指定顺序执行

public static ExecutorService newSingleThreadExecutor() {
    return new FinalizableDelegatedExecutorService(new ThreadPoolExecutor(1, 1, 0L, TimeUnit.MILLISECONDS, new LinkedBlockingQueue < runnable > ()));
}

    Executors.newScheduledThreadPool：创建固定大小的线程池，支持定时及周期性的任务执行

public ScheduledThreadPoolExecutor(int corePoolSize) {
    super(corePoolSize, Integer.MAX_VALUE, 0, NANOSECONDS, new DelayedWorkQueue());
}

简单使用
ExecutorService service = Executors.newFixedThreadPool(5);
                service.execute(
                        new Runnable() {
                            @Override
                            // run 内部如果要使用外部变量，必须是final类型
                            public void run() {
                                System.out.println(Thread.currentThread().getId());
                            }
                        }
                );
                // 如果之后不再使用，一定要关掉线程池
                service.shutdown();
                
                
                
定时线程使用
http://www.yanzuoguang.com/article/130

public class ScheduledExecutorServiceTest {
    public static void main(String[] args) {
        ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
        executorService.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                System.out.println("run "+ System.currentTimeMillis());
            }
        }, 0, 100, TimeUnit.MILLISECONDS);
    }
}



```



### 线程等待

```
https://www.cnblogs.com/lixin-link/p/10998058.html
while循环
join方法
wait 和 notify方式 synchronized锁
CountDownLatch
Future 和 callable方法
BlockingQueue方法
CyclicBarrier


countdownLatch使用：https://www.cnblogs.com/Lee_xy_z/p/10470181.html
public static void main(String[] args) {
        ExecutorService service = Executors.newFixedThreadPool(3);
        final CountDownLatch latch = new CountDownLatch(3);
        for (int i = 0; i < 3; i++) {
            Runnable runnable = new Runnable() {
                @Override
                public void run() {
                    try {
                        System.out.println("子线程" + Thread.currentThread().getName() + "开始执行");
                        Thread.sleep((long) (Math.random() * 10000));
                        System.out.println("子线程"+Thread.currentThread().getName()+"执行完成");
                        每次使用一个线程就减一，计数的个数需要提前计算好，到底要用调几个线程
                        latch.countDown();//当前线程调用此方法，则计数减一
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            };
            service.execute(runnable);
        }

        try {
            System.out.println("主线程"+Thread.currentThread().getName()+"等待子线程执行完成...");
            // 这里会等待所有线程，如果线程是9个，而计数器是10，那么这里会永远被阻塞住。所以计数器和线程数一定要提前计算好
            latch.await();//阻塞当前线程，直到计数器的值为0
            System.out.println("主线程"+Thread.currentThread().getName()+"开始执行...");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

```



### 异步接口

```

```

###  测试

```
junit不能直接测试多线程，因为会直接中断线程任务
需要让junit不插手多线程的任务
https://blog.yumc.pw/posts/Use-The-ThreadPool-On-JUnit/

需要加一行 executorService.awaitTermination(10, TimeUnit.SECONDS);
至少让单元测试运行10秒，保证多线程里面的任务可以跑完


关闭线程池：https://juejin.cn/post/6844903631846637576
```



## Java语法

### 常识

```
类的成员不写访问修饰时默认为default。默认对于同一个包中的其他类相当于公开（public），对于不是同一个包中的其他类相当于私有（private）。受保护（protected）对子类相当于公开，对不是同一包中的没有父子关系的类相当于私有。

作用域
           当前类 同包 子类 其他
public      1111
protected   1110
default     1100
private     1000 

1表示作用域有效，0表示无效
```



### 函数参数传递的一些问题

```
对象传入
```

### var的使用

- <https://segmentfault.com/a/1190000017083955>

### Objects.equals的使用

- 资料：<https://www.jianshu.com/p/31ce2ce3eef1>
- 判断两个对象的引用是否相等

### 实现一个注解

- 资料：<https://blog.csdn.net/wangpengzhi19891223/article/details/78131137>
- 详细解释：<https://www.cnblogs.com/acm-bingzi/p/javaAnnotation.html>

```
   @Documented – 注解是否将包含在JavaDoc中
   @Retention – 什么时候使用该注解
   @Target – 注解用于什么地方
   @Inherited – 是否允许子类继承该注解
   
   1.）@Retention – 定义该注解的生命周期
  ●   RetentionPolicy.SOURCE : 在编译阶段丢弃。这些注解在编译结束之后就不再有任何意义，所以它们不会写入字节码。@Override, @SuppressWarnings都属于这类注解。
  ●   RetentionPolicy.CLASS : 在类加载的时候丢弃。在字节码文件的处理中有用。注解默认使用这种方式
  ●   RetentionPolicy.RUNTIME : 始终不会丢弃，运行期也保留该注解，因此可以使用反射机制读取该注解的信息。我们自定义的注解通常使用这种方式。

  2.）Target – 表示该注解用于什么地方。默认值为任何元素，表示该注解用于什么地方。可用的ElementType 参数包括
  ● ElementType.CONSTRUCTOR: 用于描述构造器
  ● ElementType.FIELD: 成员变量、对象、属性（包括enum实例）
  ● ElementType.LOCAL_VARIABLE: 用于描述局部变量
  ● ElementType.METHOD: 用于描述方法
  ● ElementType.PACKAGE: 用于描述包
  ● ElementType.PARAMETER: 用于描述参数
  ● ElementType.TYPE: 用于描述类、接口(包括注解类型) 或enum声明

 3.)@Documented – 一个简单的Annotations 标记注解，表示是否将注解信息添加在java 文档中。

 4.)@Inherited – 定义该注释和子类的关系
     @Inherited 元注解是一个标记注解，@Inherited 阐述了某个被标注的类型是被继承的。如果一个使用了@Inherited 修饰的annotation 类型被用于一个class，则这个annotation 将被用于该class 的子类

@Retention(RetentionPolicy.RUNTIME)
public @interface MyTarget {
}


```

### List< ? >

```
资料：https://www.cnblogs.com/aipan/p/7511999.html

可以看看泛型
```



### TypeVariable

```
类型变量，描述类型，表示泛指任意或相关一类类型，也可以说狭义上的泛型（泛指某一类类型），一般用大写字母作为变量，比如K、V、E等

https://blog.csdn.net/yaomingyang/article/details/81201817
https://blog.csdn.net/a327369238/article/details/52673338
```

### 迭代器

```
Iterable Iterator 两者区别

java.lang.Iterable
java.util.Iterator
```



### 泛型

```
只有泛型类、泛型接口、泛型方法，没有泛型变量
概念介绍：https://blog.csdn.net/s10461/article/details/53941091
http://www.runoob.com/java/java-generics.html

        class DataPair<K, V> {
            private K key;
            private V value;
            DataPair() {

            }
            DataPair(K k, V v) {
                key = k;
                value = v;
            }
            public K key() {
                return key;
            }
            public V value() {
                return value;
            }
        }
        
  优先队列中加入pair并制定比较器
  lamda写法
  Comparator<DataPair<Long, Integer>> comparator1 = (o1, o2) -> (int)(o2.key() - o1.key());
  
  原始写法
          Comparator<DataPair<Long, Integer>> comparator1 = new Comparator<DataPair<Long, Integer>>() {
            @Override
            public int compare(DataPair<Long, Integer> o1, DataPair<Long, Integer> o2) {
                return (int)(o2.key() - o1.key());
            }
        };
        
        
集成的限定通配符：https://zhuanlan.zhihu.com/p/36859885
<? extends T>、<? super T>、<?>。其中前两者被称为限定通配符，<?>被称为非限定通配符。

<? extends T> 上界通配符
上界通配符顾名思义，<? extends T>表示的是类型的上界（包含自身），因此通配的参数化类型可能是T或T的子类。正因为无法确定具体的类型是什么，add方法受限（可以添加null，因为null表示任何类型），但可以从列表中获取元素后赋值给父类型。如上图中的第一个例子，第三个add()操作会受限，原因在于List<Animal>和List<Cat>是List<? extends Animal>的子类型。

<? super T> 下界通配符
下界通配符<? super T>表示的是参数化类型是T的超类型（包含自身），层层至上，直至Object，编译器无从判断get()返回的对象的类型是什么，因此get()方法受限。但是可以进行add()方法，add()方法可以添加T类型和T类型的子类型，如第二个例子中首先添加了一个Cat类型对象，然后添加了两个Cat子类类型的对象，这种方法是可行的，但是如果添加一个Animal类型的对象，显然将继承的关系弄反了，是不可行的。

<?> 无界通配符
在理解了上界通配符和下界通配符之后，其实也自然而然的理解了无界通配符。无界通配符用<?>表示，?代表了任何的一种类型，能代表任何一种类型的只有null（Object本身也算是一种类型，但却不能代表任何一种类型，所以List<Object>和List<null>的含义是不同的，前者类型是Object，也就是继承树的最上层，而后者的类型完全是未知的）。
```

### 反射

```
如何将字符串描述的类型，转化真正的类型
比如 字符串 “123” 转化成 Integer 123
其中Integer在模板中是未知的
https://blog.csdn.net/salerzhang/article/details/49637605

class MyType<T> {
 // 自定义泛型类
}
 
 
public <X> MyType<X> getMyTypeInstance(Class<X> clazz) {
 return new MyType<X>();
}
 
public void test() {
 MyType<Integer> type = getMyTypeInstance(Integer.class);
}

反射创建对象
https://blog.csdn.net/lccone/article/details/7789666

反射和泛型模板创建对象
https://blog.csdn.net/tgbus18990140382/article/details/80622524

泛型可以避免类型转换
https://www.jianshu.com/p/7cc6921c3be4
比如
public class ObjectFactory {
    public static Object getInstance(String name){
        try {
            //创建指定类对应的Class对象
            Class cls = Class.forName(name);
            //返回使用该Class对象创建的实例
            return cls.newInstance();
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
            return null;
        }
    }
}
会有object的转换
Date date = (Date) ObjectFactory.getInstance("java.util.Date");
String string = (String) ObjectFactory.getInstance("java.util.Date");
但是
public class ObjectFactory {
    public static <T> T getInstance(Class<T> cls) {
        try {
            // 返回使用该Class对象创建的实例
            return cls.newInstance();
        } catch (InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
            return null;
        }
    }
}
返回的类型都由输入决定！！！！
String instance = ObjectFactory.getInstance(String.class);



反射实现：https://www.jianshu.com/p/356e1d7a9d11

==================================================================================================================

通过反射获取类的成员变量：https://www.jianshu.com/p/1361f1f43e99
getField和getDeclaredField都是Class类的方法
getField

获取一个类的 ==public成员变量，包括基类== 。
getDeclaredField

获取一个类的 ==所有成员变量，不包括基类== 。
Field.setAccessible

成员变量为private，必须进行此操作。

==================================================================================================================
通过反射获取类的方法
getDeclaredMethod

获取字段的访问权限
getModifiers()方法用于以整数形式返回用于字段对象的修饰符，作为声明的时间。应该使用Modifier类来解码修饰符。

==================================================================================================================
Modifier 类提供了static方法和常量，对类和成员访问修饰符进行解码
modifier 的数字表示权限，用二进制表示不同权限的情况
https://blog.csdn.net/zengxiantao1994/article/details/73927754



==================================================================================================================
示例反射 - 初始化私有类型的构造函数
初始化hivecatalog测试类

            Class<?> catalogClass = Class.forName("org.apache.flink.table.catalog.hive.HiveCatalog");
            HiveCatalog hiveCatalog = null;
            Constructor constructor =  catalogClass.getDeclaredConstructor(
                    String.class,
                    String.class,
                    HiveConf.class,
                    String.class,
                    boolean.class);
            constructor.setAccessible(true);
            hiveCatalog = (HiveCatalog) constructor
                    .newInstance(
                            name,
                            null,
                            createHiveConf(),
                            StringUtils.isNullOrWhitespaceOnly(hiveVersion)
                                    ? HiveShimLoader.getHiveVersion()
                                    : hiveVersion,
                            true);
            return hiveCatalog;



```



### Comparable

```
Comparator 和 Comparable 不同！！！
```



### Interface 接口

```
https://www.runoob.com/java/java-interfaces.html
接口无法被实例化
普通类必须实现接口的所有方法
抽象类不用实现所有方法

接口可以多继承接口
```



### 抽象类

```
https://www.runoob.com/java/java-abstraction.html
在面向对象的概念中，所有的对象都是通过类来描绘的，但是反过来，并不是所有的类都是用来描绘对象的，如果一个类中没有包含足够的信息来描绘一个具体的对象，这样的类就是抽象类。

抽象类除了不能实例化对象之外，类的其它功能依然存在，成员变量、成员方法和构造方法的访问方式和普通类一样。

由于抽象类不能实例化对象，所以抽象类必须被继承，才能被使用。也是因为这个原因，通常在设计阶段决定要不要设计抽象类。

父类包含了子类集合的常见的方法，但是由于父类本身是抽象的，所以不能使用这些方法。

在Java中抽象类表示的是一种继承关系，一个类只能继承一个抽象类，而一个类却可以实现多个接口。
```

### getContextClassLoader

```

```

### switch

```
java se7 以上支持匹配字符串

public class Test {
   public static void main(String args[]){
      //char grade = args[0].charAt(0);
      char grade = 'C';
 
      switch(grade)
      {
         case 'A' :
            System.out.println("优秀"); 
            break;
         case 'B' :
         case 'C' :
            System.out.println("良好");
            break;
         case 'D' :
            System.out.println("及格");
            break;
         case 'F' :
            System.out.println("你需要再努力努力");
            break;
         default :
            System.out.println("未知等级");
      }
      System.out.println("你的等级是 " + grade);
   }
}
public class Test {
   public static void main(String args[]){
      int i = 5;
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2:
            System.out.println("2");
         default:
            System.out.println("default");
      }
   }
}
```

### 序列化和反序列化

```
https://www.runoob.com/java/java-serialization.html
常规阶段的序列化是在对应的类实现序列化接口，调用对应的outputstream和inputstream即可实现

对于商业级别的序列化，Java内置无论是性能还是序列化后的文件大小都远远不达标
所以这里需要了解avro，protobuf和flatbuffer等等序列化框架，最后选出适合业务需求的序列化

序列化还要考虑schema是否需要代码生成

序列化到字节流：https://blog.csdn.net/zhengzhaoyang122/article/details/81673947

序列化到文件如下
定义对象
public class Employee implements java.io.Serializable
{
   public String name;
   public String address;
   public transient int SSN;
   public int number;
   public void mailCheck()
   {
      System.out.println("Mailing a check to " + name
                           + " " + address);
   }
}

序列化
import java.io.*;
 
public class SerializeDemo
{
   public static void main(String [] args)
   {
      Employee e = new Employee();
      e.name = "Reyan Ali";
      e.address = "Phokka Kuan, Ambehta Peer";
      e.SSN = 11122333;
      e.number = 101;
      try
      {
         FileOutputStream fileOut =
         new FileOutputStream("/tmp/employee.ser");
         ObjectOutputStream out = new ObjectOutputStream(fileOut);
         out.writeObject(e);
         out.close();
         fileOut.close();
         System.out.printf("Serialized data is saved in /tmp/employee.ser");
      }catch(IOException i)
      {
          i.printStackTrace();
      }
   }
}

反序列化
import java.io.*;
 
public class DeserializeDemo
{
   public static void main(String [] args)
   {
      Employee e = null;
      try
      {
         FileInputStream fileIn = new FileInputStream("/tmp/employee.ser");
         ObjectInputStream in = new ObjectInputStream(fileIn);
         e = (Employee) in.readObject();
         in.close();
         fileIn.close();
      }catch(IOException i)
      {
         i.printStackTrace();
         return;
      }catch(ClassNotFoundException c)
      {
         System.out.println("Employee class not found");
         c.printStackTrace();
         return;
      }
      System.out.println("Deserialized Employee...");
      System.out.println("Name: " + e.name);
      System.out.println("Address: " + e.address);
      System.out.println("SSN: " + e.SSN);
      System.out.println("Number: " + e.number);
    }
}
```

### 编解码

```
Java中字符串编码默认是跟着系统走，utf-8是常见编码

```



### transient

```
https://www.cnblogs.com/lanxuezaipiao/p/3369962.html

 当一个类实现序列化接口后，可以用transient选择不序列化的字段
```



### 继承的用法

```
用法一
父类特有的数据结构和public数据方法
子类可以直接调用方法
比如
父类有String类型，setString,getString
子类可以调用setString,getString，实现父类的String的修改。子类无法直接访问String，但是可以通过方法访问

用法二

```

### 异常

```
语法：https://www.runoob.com/java/java-exceptions.html
图解：https://blog.csdn.net/hguisu/article/details/6155636

有两种方式操作异常
一个是捕捉异常，另一个扔出异常
扔出异常
public void deposit(double amount) throws RemoteException
  {
    // Method implementation
    throw new RemoteException();
  }
  
捕捉异常
public static void main(String args[]){
    int a[] = new int[2];
    try{
       System.out.println("Access element three :" + a[3]);
    }catch(ArrayIndexOutOfBoundsException e){
       System.out.println("Exception thrown  :" + e);
    }
    finally{
       a[0] = 6;
       System.out.println("First element value: " +a[0]);
       System.out.println("The finally statement is executed");
    }
  }
  
 
RuntimeException 和 Exception 完全不一样！！！！
RuntimeException 不需要throw 直接终止程序！


有些异常无法捕获
https://zhuanlan.zhihu.com/p/67234342
https://www.jianshu.com/p/ccfd0b14f377
像这类 java.lang.NoClassDefFoundError: org/apache/commons/collections4/IterableUtils，由于NoClassDefFoundError是Throwable的Error子类，所以Exception是捕捉不到的

三 解决办法
catch(Throwable t)
{ }
```

### 打印堆栈
```
for (StackTraceElement e : Thread.currentThread().getStackTrace()) {
    logger.info(String.format("my track %s", e.toString()));
}


```
### 正则表达式

```
https://www.runoob.com/java/java-regular-expressions.html
```

### 静态类

```
静态类只能用于内部类使用
https://www.jianshu.com/p/80b404da976b

如果一个类要被声明为static的，只有一种情况，就是静态内部类。如果在外部类声明为static，程序会编译都不会过。在一番调查后个人总结出了3点关于内部类和静态内部类（俗称：内嵌类）

1.静态内部类跟静态方法一样，只能访问静态的成员变量和方法，不能访问非静态的方法和属性，但是普通内部类可以访问任意外部类的成员变量和方法

2.静态内部类可以声明普通成员变量和方法，而普通内部类不能声明static成员变量和方法。

1.如果类的构造器或静态工厂中有多个参数，设计这样类时，最好使用Builder模式，特别是当大多数参数都是可选的时候。

                               2.如果现在不能确定参数的个数，最好一开始就使用构建器即Builder模式。
```




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

```
bytebuffer 和 string互转

编码形式的互转
String str = "string";
str.getBytes(StandardCharsets.UTF_8);

16进制形式的互转

```



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

### synchronized

```
https://www.geeksforgeeks.org/synchronized-in-java/
https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html
https://www.runoob.com/java/java-multithreading.html

// Only one thread can execute at a time. 
// sync_object is a reference to an object
// whose lock associates with the monitor. 
// The code is said to be synchronized on
// the monitor object
synchronized(sync_object)
{
   // Access shared variables and other
   // shared resources
}


class RunnableDemo implements Runnable {
   private Thread t;
   private String threadName;
   
   RunnableDemo( String name) {
      threadName = name;
      System.out.println("Creating " +  threadName );
   }
   
   public void run() {
      System.out.println("Running " +  threadName );
      try {
         for(int i = 4; i > 0; i--) {
            System.out.println("Thread: " + threadName + ", " + i);
            // 让线程睡眠一会
            Thread.sleep(50);
         }
      }catch (InterruptedException e) {
         System.out.println("Thread " +  threadName + " interrupted.");
      }
      System.out.println("Thread " +  threadName + " exiting.");
   }
   
   public void start () {
      System.out.println("Starting " +  threadName );
      if (t == null) {
         t = new Thread (this, threadName);
         t.start ();
      }
   }
}
 
public class TestThread {
 
   public static void main(String args[]) {
      RunnableDemo R1 = new RunnableDemo( "Thread-1");
      R1.start();
      
      RunnableDemo R2 = new RunnableDemo( "Thread-2");
      R2.start();
   }   
}

```



### Lamda表达式

- <https://blog.csdn.net/renfufei/article/details/24600507>

```
    // 1. 不需要参数,返回值为 5
    () -> 5
     
    // 2. 接收一个参数(数字类型),返回其2倍的值
    x -> 2 * x
     
    // 3. 接受2个参数(数字),并返回他们的差值
    (x, y) -> x – y
     
    // 4. 接收2个int型整数,返回他们的和
    (int x, int y) -> x + y
     
    // 5. 接受一个 string 对象,并在控制台打印,不返回任何值(看起来像是返回void)
    (String s) -> System.out.print(s)
    
复杂写法
players.forEach((player) -> System.out.print(player + "; "));


JAVA高级写法参考
rootNode.descendants.stream().map(n -> n.table)
        .collect(Collectors.toCollection(LinkedHashSet::new));
        
supersqlPrivileges.stream().map(s -> true).collect(Collectors.toList());

allFields.stream().anyMatch(i -> i >= lower && i < upper)

List<Pair<String, V>> result = range.entrySet().stream()
        .flatMap(e -> e.getValue().stream().map(v -> Pair.of(e.getKey(), v)))
        .collect(Collectors.toList())
 
List<Pair<String, String>> txts
List<String> sqls = txts.stream().map(x -> x.getLeft() + "\n" + x.getRight()).collect(Collectors.toList());

```

### Set

```
hashSet

        result.clear();
        result.addAll(set1);
        result.retainAll(set2);
        System.out.println("交集：" + result);
 
        result.clear();
        result.addAll(set1);
        result.removeAll(set2);
        System.out.println("差集：" + result);
 
        result.clear();
        result.addAll(set1);
        result.addAll(set2);
        System.out.println("并集：" + result);
交集：[1, 3]
差集：[5]
并集：[1, 2, 3, 5]

set1: [1,3,5]
set2: [1,2,3]

Set<String> s1 = new HashSet<>();

// Add a few elements
s1.add("HTML");
```



### HashMap

- map.entry的使用：<https://www.cnblogs.com/guanjie20/p/3769772.html>

```
map可以直接返回key集合，也可以直接返回pair<k, v>集合用于遍历。map.entry就是返回键值对

 Iterator<Map.Entry<String, List<String>>> entrys = multiString.entrySet().iterator();
 返回一个迭代器，可以用于遍历，使用方法如下
         while (entrys.hasNext()) {
            Map.Entry<String, List<String>> en = entrys.next();
        }
        
 hashmap结构的key，存储double
https://stackoverflow.com/questions/1074781/double-in-hashmap
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

### List

```java
list包含数组形式和链表形式，因为Java把方法封装成一样的

增加
add

修改数据
set(index, data)

查询
get

删除
remove

indexOf(Object obj)方法的实现机制是从序列(List)的第0个元素开始依次循环，并且调用每个元素的equals()方法和参数对象进行比较，如果某一个元素的equals()方法返回值为true，那么就把当前元素的索引位置作为结果返回。假如序列中有多个重复的元素，只返回这个重复的元素第一次出现时所在的索引位置的值。

lastIndexOf(Object obj)方法，与indexOf()方法相反，它返回的是某个元素最后一次出现的索引位置的值，也就是它会从序列的队尾向队头进行遍历。

以上两个方法的参数对象如果在序列中都没有出现的话，那么这两个方法都会返回-1。


高级用法
List<String> names = new ArrayList<String>() {{
                            add("key"),
                            
                        }
                    };

List<Map<String, String>> xx = new ArrayList() {{
    add(new HashMap() {{
        put("port", "88");
    }});
    add(new HashMap() {{
        put("port", "88");
    }});
}};

                    
list 和 数组转换 https://www.jianshu.com/p/7eee157f74fc
strList.toArray(strArray1);
Arrays.asList()


数组类型强制转换
//要转换的list集合
 List<String> testList = new ArrayList<String>(){{add("aa");add("bb");add("cc");}};

 //使用toArray(T[] a)方法
 String[] array2 = testList.toArray(new String[testList.size()]);


ArrayList<String> arrayList = new ArrayList<String>(Arrays.asList(arrays));



```

### Queue

```
https://www.jianshu.com/p/c577796e537a

Queue<String> queue = new LinkedList<>();

添加元素
add offer 

获取并删除元素
poll


推荐isEmpty来循环判断队列比较合适


```

### Class

```

```

### String

```
split分隔要注意转义符
https://www.cnblogs.com/mingforyou/archive/2013/09/03/3299569.html
1、如果用“.”作为分隔的话,必须是如下写法,String.split("\\."),这样才能正确的分隔开,不能用String.split(".");

2、如果用“|”作为分隔的话,必须是如下写法,String.split("\\|"),这样才能正确的分隔开,不能用String.split("|");

“.”和“|”都是转义字符,必须得加"\\";

3、如果在一个字符串中有多个分隔符,可以用“|”作为连字符,比如,“acount=? and uu =? or n=?”,把三个都分隔出来,可以用String.split("and|or");

使用String.split方法分隔字符串时,分隔符如果用到一些特殊字符,可能会得不到我们预期的结果。 

分隔符注意事项
StringUtils.split()和string.split()的区别
https://www.cnblogs.com/yulinlewis/p/10680697.html
```

### Enum

```
简单用法：https://www.jianshu.com/p/46dbd930f6a2
文档：https://www.runoob.com/java/method-enum1.html
枚举，数字，字符串可互相转化：https://www.cnblogs.com/myJavaCareerLife-yewei/p/8109661.html
详尽用法：https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html

enum QuestionType {
    SINGLECHOICE(2), 
    MULTIPLECHOICE(3), 
    MATRIXSINGLECHOICE(4)
}
enum Direction {
  East, South, West, North
}

public class Main {
  public static void main(String args[]) {
    Direction dir = Direction.South;
    switch (dir) {
    case South:
      System.out.println("south");
      break;
    case East:
      System.out.println("East");
      break;
    case West:
      System.out.println("West");
      break;
    case North:
      System.out.println("North.");
      break;
    }
  }
}

枚举里面定义方法
public enum Color {  
    RED("红色", 1), GREEN("绿色", 2), BLANK("白色", 3), YELLO("黄色", 4);  
    }
https://blog.csdn.net/qq_27093465/article/details/52180865

```

## Java 测试
### 模版
```
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;

public class CalculatorTest {

    @DataProvider(name = "testData")
    public Object[][] createData() {
        return new Object[][] {
            { 1, 2, 3 },
            { -1, 1, 0 },
            { 0, 0, 0 },
            { 100, 200, 300 }
        };
    }

    @Test(dataProvider = "testData")
    public void testAdd(int a, int b, int expected) {
        Calculator calculator = new Calculator();
        int result = calculator.add(a, b);
        assertEquals(result, expected, "Expected " + expected + " but got " + result);
    }
}

```

## JDK8

### getOrDefault

```

```

### System.copyArray

```

```


## IDEA
### IDEA设置不自动生成import *
1. https://www.cnblogs.com/mrgavin/p/13039124.html
```

File  --  Settings  --  Editor  --  Code Style  --  Java  -- Imports，将图示区域中的数值修改大一点并应用。



```

### java import顺序
```
File  --  Settings  --  Editor  --  Code Style  --  Java  -- Imports 设置顺序

在 code - reformat code 可以所有文件自动调整

statis other module
java
javax
org
com
other module

     <module name="ImportOrder">
            <property name="groups" value="java,javax,org,com"/>
            <property name="ordered" value="true"/>
            <property name="separated" value="true"/>
            <property name="option" value="top"/>
            <property name="sortStaticImportsAlphabetically" value="true"/>
        </module>
```

### idea 自动换行
1. https://blog.csdn.net/weixin_44874132/article/details/125682334


### idea debug运行特别慢
1. 关闭所有断点：https://www.cnblogs.com/Vincent-yuan/p/16485913.html


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

```
很明显NoClassDefFoundError的错误是因为在运行时类加载器在classpath下找不到需要加载的类，所以我们需要把对应的类加载到classpath中，或者检查为什么类在classpath中是不可用的，这个发生可能的原因如下：

    对应的Class在java的classpath中不可用
    你可能用jar命令运行你的程序，但类并没有在jar文件的manifest文件中的classpath属性中定义
    可能程序的启动脚本覆盖了原来的classpath环境变量
    因为NoClassDefFoundError是java.lang.LinkageError的一个子类，所以可能由于程序依赖的原生的类库不可用而导致
    检查日志文件中是否有java.lang.ExceptionInInitializerError这样的错误，NoClassDefFoundError有可能是由于静态初始化失败导致的（这是我遇到的问题的解决办法）
    如果你工作在J2EE的环境，有多个不同的类加载器，也可能导致NoClassDefFoundError。
    NoClassDefFoundError也可能由于类的静态初始化模块错误导致，当你的类执行一些静态初始化模块操作，如果初始化模块抛出异常，哪些依赖这个类的其他类会抛出NoClassDefFoundError的错误。如果你查看程序日志，会发现一些java.lang.ExceptionInInitializerError的错误日志，ExceptionInInitializerError的错误会导致java.lang.NoClassDefFoundError: Could not initialize class

```

### Error: Could not find or load main class

```
clean 或者重新下载代码编译
```

### Cannot find class in classpath

```
clean clean clean
rm -rf xx
rm -rf xx
rm -rf xx

只能重新编译！！！
```



### Detected both log4j-over-slf4j.jar AND bound slf4j-log4j12.jar on the class path

```
同时引用相同的包over-slf4j，要删除其中一个

exclude标签
<exclusions>
          <exclusion>
              <artifactId>log4j-over-slf4j</artifactId>
              <groupId>org.slf4j</groupId>
          </exclusion>
          </exclusions>
```

### an enum switch case label must be the unqualified name of an enumeration constant

```
https://stackoverflow.com/questions/10161408/java-using-switch-statement-with-enum-under-subclass

//Main Class
public class SomeClass {

    //Sub-Class
    public static class AnotherClass {
        public enum MyEnum {
            VALUE_A, VALUE_B
        }    
        public MyEnum myEnum;
    }

    public void someMethod() { 
        MyEnum enumExample //...

        switch (enumExample) {
            case AnotherClass.MyEnum.VALUE_A: { <-- error on this line
                //..
                break;
            }
        }
    }
}

在switch语法报错
只需要放入值，不需要前面名字限定
switch (enumExample) {
    case VALUE_A: {
        //..
        break;
    }
}
```

### Failed to execute goal net.alchim31.maven:scala-maven-plugin:4.0.2:compile (scala-compile-first) on project xxx: Execution scala-compile-first of goal net.alchim31.maven:scala-maven-plugin:4.0.2:compile failed.
```
https://www.jianshu.com/p/5b81d87a678c

scala版本没有对齐

```

### idea报Cannot find class in classpath

```
重启重启，重下代码，全部重来
```

### mvn 更新版本命令 报错maven expression: no value

```
mvn versions:set -DnewVersion=${1}

目前未解决
```

### spark做codegen的编译源码文件大于64k在1.6版本会报错

```
用2.3版本不报错
```

### java.util.MissingFormatArgumentException: Format specifier '%s'

```
打印日志的时候，变量和打印的变量个数没有对齐
```

### build.plugins.plugin.version' for org.apache.maven.plugins:maven-compiler-plugin is missing. @ line 72, column 12 

```
https://blog.csdn.net/jackgaogaogao/article/details/51533663

 <plugins>  
    <plugin>  
        <artifactId>maven-compiler-plugin</artifactId>  
        <configuration>  
            <source>1.6</source>  
            <target>1.6</target>  
            <encoding>UTF-8</encoding>  
        </configuration>  
    </plugin>  
</plugins>

添加version

 <plugins>  
    <plugin>  
        <artifactId>maven-compiler-plugin</artifactId>  
        <verison> xxx</versioon>
        <configuration>  
            <source>1.6</source>  
            <target>1.6</target>  
            <encoding>UTF-8</encoding>  
        </configuration>  
    </plugin>  
</plugins>

```

### TestNG by default disables loading DTD from unsecured Urls. If you need to explicitly load the DTD from a http url, please do so by using the JVM argument [-Dtestng.dtd.http=true]

```
org.testng.TestNGException: 
TestNG by default disables loading DTD from unsecured Urls. If you need to explicitly load the DTD from a http url, please do so by using the JVM argument [-Dtestng.dtd.http=true]
	at org.testng.xml.TestNGContentHandler.resolveEntity(TestNGContentHandler.java:115)
	at org.apache.xerces.util.EntityResolverWrapper.resolveEntity(Unknown Source)
	at org.apache.xerces.impl.XMLEntityManager.resolveEntity(Unknown Source)
	at org.apache.xerces.impl.XMLDocumentScannerImpl$DTDDispatcher.dispatch(Unknown Source)
	at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)
	at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
	at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
	

降低版本号
或者添加参数
```

### [ERROR] Forbidden method invocation: java.lang.System#exit(int) [Please do not try to kill the world]

```
https://github.com/checkstyle/checkstyle/issues/1217

    <plugin>
      <groupId>de.thetaphi</groupId>
      <artifactId>forbiddenapis</artifactId>
      <version>1.8</version>
      <configuration>
        <targetVersion>${java.version}</targetVersion>
        <!-- disallow undocumented classes like sun.misc.Unsafe: -->
        <internalRuntimeForbidden>true</internalRuntimeForbidden>
        <!--
          if the used Java version is too new,
          don't fail, just do nothing:
        -->
        <failOnUnsupportedJava>false</failOnUnsupportedJava>
        <bundledSignatures>
          <!--
            This will automatically choose the right
            signatures based on 'maven.compiler.target':
          -->
          <bundledSignature>jdk-unsafe</bundledSignature>
          <bundledSignature>jdk-deprecated</bundledSignature>
        </bundledSignatures>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>check</goal>
            <goal>testCheck</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
    
   注释上面这个插件
   
   
 <!--        <plugin>-->
<!--          <groupId>de.thetaphi</groupId>-->
<!--          <artifactId>forbiddenapis</artifactId>-->
<!--          <version>${forbiddenapis.version}</version>-->
<!--        </plugin>-->
```

### 'static' modifier out of order with the JLS suggestions

```
'static' modifier out of order with the JLS suggestions


public or private should come before static, which should come before final.
```

### AvoidStarImportCheck

```
不能用 * 的原因，就是会编译出错
https://stackoverflow.com/questions/147454/why-is-using-a-wild-card-with-a-java-import-statement-bad
```

### Utility classes should not have a public or default constructor.

```
class StringUtils { // Compliant

  private StringUtils() {
    throw new IllegalStateException("Utility class");
  }

  public static String concatenate(String s1, String s2) {
    return s1 + s2;
  }

}


工具类不能有构造函数，必须加一个throw
```

### Exception in thread "main" java.lang.SecurityException: Invalid signature file digest for Manifest main attributes

```
打包要过滤多个重复配置文件
https://www.cnblogs.com/hark0623/p/6253043.html

Exception in thread "main" java.lang.SecurityException: Invalid signature file digest for Manifest main attributes
	at sun.security.util.SignatureFileVerifier.processImpl(SignatureFileVerifier.java:330)
	at sun.security.util.SignatureFileVerifier.process(SignatureFileVerifier.java:263)
	at java.util.jar.JarVerifier.processEntry(JarVerifier.java:318)
	at java.util.jar.JarVerifier.update(JarVerifier.java:230)
	at java.util.jar.JarFile.initializeVerifier(JarFile.java:383)
	at java.util.jar.JarFile.ensureInitialization(JarFile.java:618)
	at java.util.jar.JavaUtilJarAccessImpl.ensureInitialization(JavaUtilJarAcc



有些Jar包会在metainf里包含一个.SF：包含原Jar包内的class文件和资源文件的Hash， 用来校验文件的完整度等验证。

但是在打fat-jar的时候，我们是把很多jar包合成了一个，这样fatjar下就会存在各个jar包中的签名文件，但是他们显然无法跟最终的fatjar作校验。

解决方案，添加插件
<plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>1.7.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
```

### mvn的所有异常

```

================================================================================================

[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-jar-plugin:3.1.2:jar (default-jar) on project spark-tags_2.12: You have to use a classifier to attach supplemental artifacts to the project instead of replacing them. -> [Help 1]
[ERROR]








 PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target -> [Help 1]

https://www.cnblogs.com/wpbxin/p/11746229.html

一般请求某个仓库如果出现异常，就无法继续查找下一个仓库
所以有时候我们仓库里面有相关的包，但是因为查找顺序会出现很多不容易避开的问题


================================================================================================

was cached in the local repository, resolution will not be reattempted until the update interval of tianqiong-releases has elapsed or updates are forced
https://blog.51cto.com/qiangsh/1743074

Maven默认会使用本地缓存的库来编译工程，对于上次下载失败的库，maven会在​​~/.m2/repository/<group>/<artifact>/<version>/​​​目录下创建xxx.lastUpdated文件，一旦这个文件存在，那么在直到下一次nexus更新之前都不会更新这个依赖库。

​删除v~/.m2/repository/<group>/<artifact>/<version>/目录下的*.lastUpdated文件，然后再次运行mvn compile编译工程。
修改~/.m2/settings.xml 或/opt/maven/conf/settings.xml文件，将其中的仓库添加 <updatePolicy>always</updatePolicy>来强制每次都更新依赖库。
<repositories>
        <repository>
                <id>central</id>
                <url>http://central</url>
                <releases>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                </releases>
                <snapshots>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                </snapshots>
        </repository>
</repositories>





================================================================================================


[ERROR] Failed to execute goal org.apache.maven.plugins:maven-jar-plugin:2.6:jar (default-jar) on project hybris-common: Execution default-jar of goal org.apache.maven.plugins:maven-jar-plugin:2.6:jar failed: An API incompatibility was encountered while executing org.apache.maven.plugins:maven-jar-plugin:2.6:jar: java.lang.ExceptionInInitializerError: null
[ERROR] -----------------------------------------------------
[ERROR] realm =    plugin>org.apache.maven.plugins:maven-jar-plugin:2.6
[ERROR] strategy = org.codehaus.plexus.classworlds.strategy.SelfFirstStrategy
[ERROR] urls[0] = file:/root/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/2.6/maven-jar-plugin-2.6.jar
[ERROR] urls[1] = file:/root/.m2/repository/org/slf4j/slf4j-jdk14/1.5.6/slf4j-jdk14-1.5.6.jar
[ERROR] urls[2] = file:/root/.m2/repository/org/slf4j/jcl-over-slf4j/1.5.6/jcl-over-slf4j-1.5.6.jar
[ERROR] urls[3] = file:/root/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1/maven-reporting-api-2.2.1.jar
[ERROR] urls[4] = file:/root/.m2/repository/org/apache/maven/doxia/doxia-sink-api/1.1/doxia-sink-api-1.1.jar
[ERROR] urls[5] = file:/root/.m2/repository/org/apache/maven/doxia/doxia-logging-api/1.1/doxia-logging-api-1.1.jar
[ERROR] urls[6] = file:/root/.m2/repository/junit/junit/3.8.1/junit-3.8.1.jar
[ERROR] urls[7] = file:/root/.m2/repository/commons-cli/commons-cli/1.2/commons-cli-1.2.jar
[ERROR] urls[8] = file:/root/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.jar
[ERROR] urls[9] = file:/root/.m2/repository/backport-util-concurrent/backport-util-concurrent/3.1/backport-util-concurrent-3.1.jar
[ERROR] urls[10] = file:/root/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.jar
[ERROR] urls[11] = file:/root/.m2/repository/org/sonatype/plexus/plexus-cipher/1.4/plexus-cipher-1.4.jar
[ERROR] urls[12] = file:/root/.m2/repository/org/codehaus/plexus/plexus-interpolation/1.11/plexus-interpolation-1.11.jar
[ERROR] urls[13] = file:/root/.m2/repository/org/apache/maven/maven-archiver/2.6/maven-archiver-2.6.jar
[ERROR] urls[14] = file:/root/.m2/repository/org/apache/maven/shared/maven-shared-utils/0.7/maven-shared-utils-0.7.jar
[ERROR] urls[15] = file:/root/.m2/repository/com/google/code/findbugs/jsr305/2.0.1/jsr305-2.0.1.jar
[ERROR] urls[16] = file:/root/.m2/repository/org/codehaus/plexus/plexus-utils/3.0.20/plexus-utils-3.0.20.jar
[ERROR] urls[17] = file:/root/.m2/repository/org/codehaus/plexus/plexus-archiver/2.9/plexus-archiver-2.9.jar
[ERROR] urls[18] = file:/root/.m2/repository/org/codehaus/plexus/plexus-io/2.4/plexus-io-2.4.jar
[ERROR] urls[19] = file:/root/.m2/repository/commons-io/commons-io/2.2/commons-io-2.2.jar
[ERROR] urls[20] = file:/root/.m2/repository/org/apache/commons/commons-compress/1.9/commons-compress-1.9.jar
[ERROR] Number of foreign imports: 1
[ERROR] import: Entry[import  from realm ClassRealm[maven.api, parent: null]]
[ERROR] 
[ERROR] -----------------------------------------------------
[ERROR] : Index 1 out of bounds for length 1
[ERROR] -> [Help 1]


java版本太高了，用java11打包会失败
mvn-jar-plugins版本是2.6
改成java1.8

https://stackoverflow.com/questions/46353477/jdk9-and-maven-jar-plugin




================================================================================================

[WARNING] Could not transfer metadata net.minidev:json-smart/maven-metadata.xml from/to maven-default-http-blocker (http://0.0.0.0/): transfer failed for http://0.0.0.0/net/minidev/json-smart/maven-metadata.xml, proxy: ProxyInfo{host='web-proxy.tencent.com', userName='null', port=8080, type='http', nonProxyHosts='null'}
[WARNING] Could not transfer metadata net.minidev:json-smart/maven-metadata.xml from/to alimaven (http://maven.aliyun.com/nexus/content/groups/public/): transfer failed for http://maven.aliyun.com/nexus/content/groups/public/net/minidev/json-smart/maven-metadata.xml, proxy: ProxyInfo{host='web-proxy.tencent.com', userName='null', port=8080, type='http', nonProxyHosts='null'}
D



[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  10:21 min
[INFO] Finished at: 2022-04-20T19:46:52+08:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal on project hybris-service-biz: Could not resolve dependencies for project com.tencent.cloud:hybris-service-biz:jar:2.0.0-wedata-SNAPSHOT: Failed to collect dependencies at org.apache.hive:hive-metastore:jar:2.3.5 -> org.apache.hive:hive-serde:jar:2.3.5 -> org.apache.hive:hive-common:jar:2.3.5 -> com.github.joshelser:dropwizard-metrics-hadoop-metrics2-reporter:jar:0.1.2 -> org.apache.hadoop:hadoop-common:jar:2.8.5 -> org.apache.hadoop:hadoop-auth:jar:2.8.5 -> com.nimbusds:nimbus-jose-jwt:jar:4.41.1 -> net.minidev:json-smart:jar:2.3-SNAPSHOT: Failed to read artifact descriptor for net.minidev:json-smart:jar:2.3-SNAPSHOT: Could not transfer artifact net.minidev:json-smart:pom:2.3-SNAPSHOT from/to maven-default-http-blocker (http://0.0.0.0/): Blocked mirror for repositories: [tbds (http://tbdsrepo.oa.com/repository/tbds/, default, releases+snapshots)] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/DependencyResolutionException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <args> -rf :hybris-service-biz


maven-default-http-blocker (http://0.0.0.0/)
mvn3.8.1以上的默认只支持https，不支持http

================================================================================================

[ERROR] Failed to execute goal on project hybris-inferschema-online: Could not resolve dependencies for project com.tencent.cloud:hybris-inferschema-online:jar:2.0.0-wedata-SNAPSHOT: Failed to collect dependencies at com.tencent.cloud:lakefs-cosn-client:jar:1.0: Failed to read artifact descriptor for com.tencent.cloud:lakefs-cosn-client:jar:1.0: Could not transfer artifact com.tencent.cloud:lakefs-cosn-client:pom:1.0 from/to alimaven (http://maven.aliyun.com/nexus/content/groups/public/): Transfer failed for http://maven.aliyun.com/nexus/content/groups/public/com/tencent/cloud/lakefs-cosn-client/1.0/lakefs-cosn-client-1.0.pom ProxyInfo{host='web-proxy.tencent.com', userName='null', port=8080, type='http', nonProxyHosts='null'}: Connect to web-proxy.tencent.com:8080 [web-proxy.tencent.com/10.28.36.104] failed: Connection timed out (Connection timed out) -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/DependencyResolutionException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <args> -rf :hybris-inferschema-online




================================================================================================

https://www.cnblogs.com/ried12138/p/14840635.html

 Fatal error compiling: java.lang.IllegalAccessError: class lombok.javac.apt.LombokProcessor (in unnamed module @0x2aa7399c) cannot access class com.sun.tools.javac.processing.JavacProcessingEnvironment (in module jdk.compiler) because module jdk.compiler does not export com.sun.tools.javac.processing to unnamed module @0x2aa7399c


================================================================================================

[ERROR] Failed to execute goal on project hybris-inferschema-online: Could not resolve dependencies for project com.tencent.cloud:hybris-inferschema-online:jar:1.5.0: Failed to collect dependencies at com.tencent.cloud:lakefs-cosn-client:jar:1.0: Failed to read artifact descriptor for com.tencent.cloud:lakefs-cosn-client:jar:1.0: Could not transfer artifact com.tencent.cloud:lakefs-cosn-client:pom:1.0 from/to alimaven (http://maven.aliyun.com/nexus/content/groups/public/): Transfer failed for http://maven.aliyun.com/nexus/content/groups/public/com/tencent/cloud/lakefs-cosn-client/1.0/lakefs-cosn-client-1.0.pom ProxyInfo{host='web-proxy.tencent.com', userName='null', port=8080, type='http', nonProxyHosts='null'}: web-proxy.tencent.com: nodename nor servname provided, or not known -> [Help 1]


注释 <proxies> 标签的内容
关闭代理
================================================================================================


[ERROR] Failed to execute goal on project dep-hive311: Could not resolve dependencies for project com.tencent.cloud:dep-hive311:jar:1.0.0: Failed to collect dependencies at org.apache.hive:hive-jdbc:jar:3.1.1 -> org.apache.hive:hive-service:jar:3.1.1 -> org.apache.hive:hive-llap-server:jar:3.1.1 -> org.apache.hbase:hbase-server:jar:2.0.0-alpha4 -> org.glassfish.web:javax.servlet.jsp:jar:2.3.2 -> org.glassfish:javax.el:jar:3.0.1-b06-SNAPSHOT: Failed to read artifact descriptor for org.glassfish:javax.el:jar:3.0.1-b06-SNAPSHOT: Could not transfer artifact org.glassfish:javax.el:pom:3.0.1-b06-SNAPSHOT from/to jvnet-nexus-snapshots (https://maven.java.net/content/repositories/snapshots): Transfer failed for https://maven.java.net/content/repositories/snapshots/org/glassfish/javax.el/3.0.1-b06-SNAPSHOT/javax.el-3.0.1-b06-SNAPSHOT.pom: Remote host closed connection during handshake: SSL peer shut down incorrectly -> [Help 1]


https://cloud.tencent.com/developer/article/1948981


https://icode.best/i/81187038460452


配置repo1仓库

<mirror>
            <id>repo1</id>
            <name>repo1 maven</name>
            <url>https://repo1.maven.org/maven2/</url>
            <mirrorOf>central</mirrorOf>
        </mirror> 

glassfish jar包
https://repo1.maven.org/maven2/org/glassfish/javax.el/3.0.1-b06/
================================================================================================
镜像仓库大全
https://blog.csdn.net/Hello_World_QWP/article/details/82459915


================================================================================================

[ERROR] Failed to execute goal org.apache.maven.plugins:maven-shade-plugin:3.4.1:shade (default) on project executor-spark-dataminig: Unable to parse configuration of mojo org.apache.maven.plugins:maven-shade-plugin:3.4.1:shade for parameter resource: Cannot find 'resource' in class org.apache.maven.plugins.shade.resource.ManifestResourceTransformer -> [Help 1]
org.apache.maven.lifecycle.LifecycleExecutionException: Failed to execute goal org.apache.maven.plugins:maven-shade-plugin:3.4.1:shade (default) on project executor-spark-dataminig: Unable to parse configuration of mojo org.apache.maven.plugins:maven-shade-plugin:3.4.1:shade for parameter resource: Cannot find 'resource' in class org.apache.maven.plugins.shade.resource.ManifestResourceTransformer
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:215)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:156)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:148)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:117)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:81)
    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:56)
    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:128)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:305)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:192)
    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:105)
    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:957)
    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:289)
    at org.apache.maven.cli.MavenCli.main (MavenCli.java:193)
    at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke (Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced (Launcher.java:282)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch (Launcher.java:225)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode (Launcher.java:406)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main (Launcher.java:347)
Caused by: org.apache.maven.plugin.PluginConfigurationException: Unable to parse configuration of mojo org.apache.maven.plugins:maven-shade-plugin:3.4.1:shade for parameter resource: Cannot find 'resource' in class org.apache.maven.plugins.shade.resource.ManifestResourceTransformer
    at org.apache.maven.plugin.internal.DefaultMavenPluginManager.populatePluginFields (DefaultMavenPluginManager.java:665)
    at org.apache.maven.plugin.internal.DefaultMavenPluginManager.getConfiguredMojo (DefaultMavenPluginManager.java:597)
    at org.apache.maven.plugin.DefaultBuildPluginManager.executeMojo (DefaultBuildPluginManager.java:124)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:210)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:156)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:148)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:117)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:81)
    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:56)
    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:128)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:305)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:192)
    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:105)
    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:957)
    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:289)
    at org.apache.maven.cli.MavenCli.main (MavenCli.java:193)
    at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke (Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced (Launcher.java:282)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch (Launcher.java:225)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode (Launcher.java:406)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main (Launcher.java:347)
Caused by: org.codehaus.plexus.component.configurator.ComponentConfigurationException: Cannot find 'resource' in class org.apache.maven.plugins.shade.resource.ManifestResourceTransformer
    at org.eclipse.sisu.plexus.CompositeBeanHelper.setProperty (CompositeBeanHelper.java:252)
    at org.codehaus.plexus.component.configurator.converters.composite.ObjectWithFieldsConverter.processConfiguration (ObjectWithFieldsConverter.java:101)
    at org.codehaus.plexus.component.configurator.converters.composite.ObjectWithFieldsConverter.fromConfiguration (ObjectWithFieldsConverter.java:57)
    at org.codehaus.plexus.component.configurator.converters.composite.AbstractCollectionConverter.fromChildren (AbstractCollectionConverter.java:54)
    at org.codehaus.plexus.component.configurator.converters.composite.ArrayConverter.fromConfiguration (ArrayConverter.java:52)
    at org.eclipse.sisu.plexus.CompositeBeanHelper.convertProperty (CompositeBeanHelper.java:273)
    at org.eclipse.sisu.plexus.CompositeBeanHelper.setProperty (CompositeBeanHelper.java:210)
    at org.codehaus.plexus.component.configurator.converters.composite.ObjectWithFieldsConverter.processConfiguration (ObjectWithFieldsConverter.java:101)
    at org.codehaus.plexus.component.configurator.BasicComponentConfigurator.configureComponent (BasicComponentConfigurator.java:34)
    at org.apache.maven.plugin.internal.DefaultMavenPluginManager.populatePluginFields (DefaultMavenPluginManager.java:635)
    at org.apache.maven.plugin.internal.DefaultMavenPluginManager.getConfiguredMojo (DefaultMavenPluginManager.java:597)
    at org.apache.maven.plugin.DefaultBuildPluginManager.executeMojo (DefaultBuildPluginManager.java:124)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:210)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:156)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:148)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:117)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:81)
    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:56)
    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:128)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:305)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:192)
    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:105)
    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:957)
    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:289)
    at org.apache.maven.cli.MavenCli.main (MavenCli.java:193)
    at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke (Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced (Launcher.java:282)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch (Launcher.java:225)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode (Launcher.java:406)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main (Launcher.java:347)

shade插件打包异常
注释相关行 transformer的标签
                      <transformer-->
<!--                                        implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">-->
<!--                                    <mainClass>-->
<!--                                        com.meituan.service.mobile.offline.selector.indexgenerator.framework.IndexGeneratorService-->
<!--                                    </mainClass>-->
<!--                                </transformer>-->

================================================================================================




================================================================================================





================================================================================================






================================================================================================
```



### CheckStyle

```
Method length is 371 lines (max allowed is 370). [MethodLength]
方法类里面不能超过371行

ImportOrder
遵循顺序
（1）同组的包放在一起

（2）同组的包按照一定的顺序，一般是按照字典顺序

（3）不同组之间的包流一个空行
```


### Kotlin: Language version 1.2 is no longer supported; please, use version 1.3 or greater.
```

Kotlin: Language version 1.2 is no longer supported; please, use version 1.3 or greater.
Errors occurred while compiling module 'tests of calcite-core'





```


### [ERROR] Failed to execute goal org.apache.maven.plugins:maven-enforcer-plugin:3.1.0:enforce (enforce-maven) on project flink-parent: Some Enforcer rules have failed. Look above for specific messages explaining why the rule failed. -> [Help 1]
```

暂无解决方案


```


### package sun.util does not exist
```

java 11很多底层被orcle屏蔽了，因为版权问题

```

### [ERROR] Failed to execute goal org.apache.rat:apache-rat-plugin:0.12:check (default) on project flink-parent: Too many files with unapproved license: 132 See RAT report in: /home/clouddev/kwai-flink/target/rat.txt -> [Help 1]
```
skip 这个插件

```



### java: Cannot run program "/usr/java/jdk1.8.0_181/bin/java" (in directory "/home/clouddev/.cache/JetBrains/RemoteDev-IU/_home_clouddev_kaiworks-stream/compile-server"): error=0, Failed to exec spawn helper: pid: 880983, signal: 11

```
idea 远程开发会出现的问题

解决
https://blog.csdn.net/qq_44768464/article/details/135868229
https://youtrack.jetbrains.com/issue/IDEA-304440/Cannot-run-program-java-failed-to-exec-spawn-helper-exit-value-1


Alternatively, you may try to configure JDK to use older launching mechanism by adding flag to File | Settings | Build, Execution, Deployment | Compiler | * build process VM options text field

-Djdk.lang.Process.launchMechanism=vfork



```


### scala: No JDK in module flink-sql-parser
```

用命令行没问题，idea就有问题
只能重新编译

```





### java: warning source release 11 requires target release 11
```
全部改成1.8 重编译 重编译

```



### Too many files with unapproved license: 131 See RAT report in: /home/clouddev/kwai-flink/target/rat.txt

```
加参数跳过
mvn clean install -DskipTests -Dcheckstyle.skip=true  -Pskip-webui-build -Drat.skip=true

```



### scalac: Scala compiler JARs not found (module 'flink-runtime_2.11'): /home/clouddev/.m2/repository/org/scala-lang/modules/scala-parser-combinators_2.11/1.0.4/scala-parser-combinators_2.11-1.0.4.jar

```
scala版本问题，命令行重新编译，scala代码不要再动了。idea不适合从源头编译


```



### javac 8 was used to compile java sources
```
Errors occurred while compiling module 'xxxx'
javac 8 was used to compile java sources


 确保您的 Java 文件编码与 JDK 支持的编码一致。通常，UTF-8 编码是推荐使用的。
 mvn clean install 重新编译吧
```



### Invalid signature file digest for Manifest main attributes
```
shade打包，包含第三方配置文件
需要删除无用文件

shade加上配置
 <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>



java.lang.SecurityException: Invalid signature file digest for Manifest main attributes

	at sun.security.util.SignatureFileVerifier.processImpl(SignatureFileVerifier.java:330)
	at sun.security.util.SignatureFileVerifier.process(SignatureFileVerifier.java:263)
	at java.util.jar.JarVerifier.processEntry(JarVerifier.java:318)
	at java.util.jar.JarVerifier.update(JarVerifier.java:230)
	at java.util.jar.JarFile.initializeVerifier(JarFile.java:383)
	at java.util.jar.JarFile.getInputStream(JarFile.java:450)
	at sun.misc.URLClassPath$JarLoader$2.getInputStream(URLClassPath.java:977)
	at sun.misc.Resource.cachedInputStream(Resource.java:77)
	at sun.misc.Resource.getByteBuffer(Resource.java:160)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:454)
	at java.net.URLClassLoader.access$100(URLClassLoader.java:73)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:368)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:362)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:361)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	at java.lang.Class.getDeclaredMethods0(Native Method)
	at java.lang.Class.privateGetDeclaredMethods(Class.java:2701)
	at java.lang.Class.privateGetMethodRecursive(Class.java:3048)
	at java.lang.Class.getMethod0(Class.java:3018)
	at java.lang.Class.getMethod(Class.java:1784)
	at org.junit.internal.builders.SuiteMethodBuilder.hasSuiteMethod(SuiteMethodBuilder.java:18)
	at org.junit.internal.builders.SuiteMethodBuilder.runnerForClass(SuiteMethodBuilder.java:10)
	at org.junit.runners.model.RunnerBuilder.safeRunnerForClass(RunnerBuilder.java:59)
	at org.junit.internal.builders.AllDefaultPossibilitiesBuilder.runnerForClass(AllDefaultPossibilitiesBuilder.java:26)
	at org.junit.runners.model.RunnerBuilder.safeRunnerForClass(RunnerBuilder.java:59)
	at org.junit.internal.requests.ClassRequest.getRunner(ClassRequest.java:33)
	at org.junit.internal.requests.FilterRequest.getRunner(FilterRequest.java:36)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:50)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater$1.execute(IdeaTestRunner.java:38)
	at com.intellij.rt.execution.junit.TestsRepeater.repeat(TestsRepeater.java:11)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:35)
	at com.intellij.rt.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:232)
	at com.intellij.rt.junit.JUnitStarter.main(JUnitStarter.java:55)



```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```



### 
```


```





## 自动化脚本

### Java安装-非root情况

```
mkdir java
cd java
wget http://pkg.4paradigm.com/jdk/jdk-8u141-linux-x64.tar.gz
tar -zxvf jdk-8u141-linux-x64.tar.gz


wget https://github.com/Tencent/TencentKona-8/releases/download/8.0.19-GA/TencentKona8.0.19.b1_jdk_linux-x86_64_8u422.tar.gz



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

### 字节流创建字符串，无hashcode

```
    // construct string with no hashcode
    protected Object newInstanceFromString(Class c, String s) {
        try {
            Constructor ctor = stringCtorCache.get(c);
            if (ctor == null) {
                ctor = c.getDeclaredConstructor(String.class);
                ctor.setAccessible(true);
                stringCtorCache.put(c, ctor);
            }
            return ctor.newInstance(s);
        } catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException | InstantiationException e) {
            throw new AvroRuntimeException(e);
        }
    }
```



## 常用代码片段

### 打印logger-到底怎么配置logger

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

配置log（已经验证n次了）！！！！
需要在main或者test的resource处放 log4j.properties文件
不然无法初始化日志系统

```



### 线程睡眠

```
Thread.sleep(200);
```



### 资源加载

```
private static Properties properties = new Properties();
String path = System.getProperty("user.dir") + xxxx
properties.load(new BufferedInputStream(new FileInputStream(new File(path))));

path 是当前项目的目录路径
properties 加载路径的文件资源
文件格式统一：变量名=xxxxx

获取资源
properties.getProperty("变量名");

```

### 获取当前类和名字

```
https://www.huaweicloud.com/articles/af74a73f5ad4c8847a9bf5fb090ff22f.html

Thread.currentThread().getStackTrace()[1].getClassName();
Thread.currentThread().getStackTrace()[1].getMethodName();

或者

this.getClass().getName();

```




### 读文件转字符串

```
  public static String readFileToString(String path) throws IOException {
    String context = FileUtils.readFileToString(new File(path));
    return context;
  }
```



### gson

```
使用指南：https://www.jianshu.com/p/e740196225a4

Hashmap valueMap
Gson gson = new Gson();
String value = gson.toJson(valueMap);


Gson gson = new Gson();
int i = gson.fromJson("100", int.class);              //100
double d = gson.fromJson("\"99.99\"", double.class);  //99.99
boolean b = gson.fromJson("true", boolean.class);     // true
String str = gson.fromJson("String", String.class);   // String


Gson gson = new Gson();
String jsonNumber = gson.toJson(100);       // 100
String jsonBoolean = gson.toJson(false);    // false
String jsonString = gson.toJson("String"); //"String"


Gson gson = new Gson();
User user = new User("怪盗kidou",24);
String jsonObject = gson.toJson(user); // {"name":"怪盗kidou","age":24}


Gson gson = new Gson();
String jsonString = "{\"name\":\"怪盗kidou\",\"age\":24}";
User user = gson.fromJson(jsonString, User.class);

2.8.3以上的版本可以直接用静态方法解析json字符串
JsonElement je = JsonParser.parseString(readFileToString(new File(path)));


if (withPretty) {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            JsonParser jp = new JsonParser();
            return gson.toJson(jp.parse(jo.toString()));
        } else {
            return jo.toString();
        }

```

### byte[] 和 string 互转 需要借助base64
```
byte[] userActionProtos = ua.toByteArray();
Base64.getDecoder().decode(Base64.getEncoder().encodeToString(userActionProtos))



```


### 从类名找到具体jar包名 （autosroll from source)
1. https://www.baeldung.com/java-full-path-of-jar-from-class

```


import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Paths;
public class Demo {
    public static void main(String[] args) throws URISyntaxException {
        String jarPath = byGetProtectionDomain(XXXXXXXXXXXXXXXXXXXXX.class);
        System.out.println(jarPath);
    }

    static String byGetProtectionDomain(Class clazz) throws URISyntaxException {
        URL url = clazz.getProtectionDomain().getCodeSource().getLocation();
        return Paths.get(url.toURI()).toString();
    }
}

```

### 消除编译的无效警告（该对象没有被使用的警告）
```

  /**
   * Does nothing with its argument. Call this method when you have a value
   * you are not interested in, but you don't want the compiler to warn that
   * you are not using it.
   */
  public static void discard(Object o) {
    if (false) {
      discard(o);
    }
  }

```

## 常用命令

```
查看java加载包的日志
java -verbose:class
```



# 新的章节

## Yaml语法

### 参考资料

- 类似与xml的文件：<https://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/index.html>
- 官网：<http://www.yaml.org/>
- Java版本：<http://jyaml.sourceforge.net/tutorial.html>
- 字符串缩进要求：https://www.cnblogs.com/didispace/p/12524194.html

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

## **javapoet**

### 资料

- 源码：<https://github.com/square/javapoet>
- 中文介绍：**<https://blog.csdn.net/crazy1235/article/details/51876192>**
- 入门使用：<https://juejin.im/entry/58fefebf8d6d810058a610de>
- example：<https://www.programcreek.com/java-api-examples/?api=com.squareup.javapoet.CodeBlock>

```
package com.example.helloworld;

public final class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, JavaPoet!");
  }
  
  
用javapoet生成上面的代码
MethodSpec main = MethodSpec.methodBuilder("main")
    .addModifiers(Modifier.PUBLIC, Modifier.STATIC)
    .returns(void.class)
    .addParameter(String[].class, "args")
    .addStatement("$T.out.println($S)", System.class, "Hello, JavaPoet!")
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
    .addMethod(main)
    .build();

JavaFile javaFile = JavaFile.builder("com.example.helloworld", helloWorld)
    .build();

javaFile.writeTo(System.out);

可以直接用字符串转Java类
MethodSpec main = MethodSpec.methodBuilder("main")
    .addCode(""
        + "int total = 0;\n"
        + "for (int i = 0; i < 10; i++) {\n"
        + "  total += i;\n"
        + "}\n")
    .build();
    
或者用内置方法实现换行和分号
MethodSpec main = MethodSpec.methodBuilder("main")
    .addStatement("int total = 0")
    .beginControlFlow("for (int i = 0; i < 10; i++)")
    .addStatement("total += i")
    .endControlFlow()
    .build();
    


```

### 个人总结

```
javapoet用最原始的字符串方式，来生成代码
用户使用的时候，只需要想办法构造代码字符串即可

为了方便构造代码字符串，javapoet提供相关类，比如方法类，接口类等等方便快速构造结构化的代码
也提供包管理，自动找到包的引用
同时提高结构流，循环流，分支流之类的

```



### Example

以 `HelloWorld` 类为例:

```java
package com.example.helloworld;

public final class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, JavaPoet!");
  }
}
```

上面的代码就是使用javapoet用下面的代码进行生成的：

```java
MethodSpec main = MethodSpec.methodBuilder("main")
    .addModifiers(Modifier.PUBLIC, Modifier.STATIC)
    .returns(void.class)
    .addParameter(String[].class, "args")
    .addStatement("$T.out.println($S)", System.class, "Hello, JavaPoet!")
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
    .addMethod(main)
    .build();

JavaFile javaFile = JavaFile.builder("com.example.helloworld", helloWorld)
    .build();

javaFile.writeTo(System.out);
```

通过`MethodSpec`类来创建一个”main”方法，并配置了修饰符、返回值类型、参数以及代码语句。然后把这个main方法添加到 `HelloWorld` 类中，最后添加到 `HelloWorld.java`文件中。
这个例子中，我们将文件通过`Sytem.out` 进行输出，但是同样也可以使用(`JavaFile.toString()`) 得到string字符串，或者通过 (`JavaPoet.writeTo()`) 方法写入到文件系统中。

[Javadoc](https://square.github.io/javapoet/1.x/javapoet/) 中包括了完整的JavaPoet API, 我们接着往下看。

### Code & Control Flow

大多数JavaPoet的API使用的是简单的不可变的Java对象。通过建造者模式，链式方法，可变参数是的API比较友好。JavaPoet提供了(`TypeSpec`)用于创建类或者接口，(`FieldSpec`)用来创建字段，(`MethodSpec`)用来创建方法和构造函数，(`ParameterSpec`)用来创建参数，(`AnnotationSpec`)用于创建注解。

但是如果没有语句类，没有语法结点数，可以通过字符串来构建代码块：

```java
MethodSpec main = MethodSpec.methodBuilder("main")
    .addCode(""
        + "int total = 0;\n"
        + "for (int i = 0; i < 10; i++) {\n"
        + "  total += i;\n"
        + "}\n")
    .build();1234567
```

生成的代码如下:

```java
void main() {
  int total = 0;
  for (int i = 0; i < 10; i++) {
    total += i;
  }
}123456
```

人为的输入分号、换行和缩进是比较乏味的。所以JavaPoet提供了相关API使它变的容易。
`addStatement()` 负责分号和换行，`beginControlFlow()` + `endControlFlow()` 需要一起使用，提供换行符和缩进。

```java
MethodSpec main = MethodSpec.methodBuilder("main")
    .addStatement("int total = 0")
    .beginControlFlow("for (int i = 0; i < 10; i++)")
    .addStatement("total += i")
    .endControlFlow()
    .build();123456
```

这个例子稍微有点差劲。生成的代码如下：

```java
private MethodSpec computeRange(String name, int from, int to, String op) {
  return MethodSpec.methodBuilder(name)
      .returns(int.class)
      .addStatement("int result = 0")
      .beginControlFlow("for (int i = " + from + "; i < " + to + "; i++)")
      .addStatement("result = result " + op + " i")
      .endControlFlow()
      .addStatement("return result")
      .build();
}
```

调用`computeRange("multiply10to20", 10, 20, "*")`就生成如下代码:

```java
int multiply10to20() {
  int result = 0;
  for (int i = 10; i < 20; i++) {
    result = result * i;
  }
  return result;
}1234567
```

方法生成方法！JavaPoet生成的是源代码而不是字节码，所以可以通过阅读源码确保正确。

### $L for Literals

字符串连接的方法`beginControlFlow()` 和 `addStatement`是分散开的，操作较多。
针对这个问题, JavaPoet 提供了一个语法但是有违[`String.format()`](http://developer.android.com/reference/java/util/Formatter.html)语法. 通过 **$L** 来接受一个 **literal** 值。 这有点像 `Formatter`’s `%s`:

```java
private MethodSpec computeRange(String name, int from, int to, String op) {
  return MethodSpec.methodBuilder(name)
      .returns(int.class)
      .addStatement("int result = 0")
      .beginControlFlow("for (int i = $L; i < $L; i++)", from, to)
      .addStatement("result = result $L i", op)
      .endControlFlow()
      .addStatement("return result")
      .build();
}12345678910
```

Literals 直接写在输出代码中，没有转义。 它的类型可以是字符串、primitives和一些接下来要说的JavaPoet类型。

### $S for Strings

当输出的代码包含字符串的时候, 可以使用 **$S** 表示一个 **string**。 下面的代码包含三个方法，每个方法返回自己的名字:

```java
public static void main(String[] args) throws Exception {
  TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
      .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
      .addMethod(whatsMyName("slimShady"))
      .addMethod(whatsMyName("eminem"))
      .addMethod(whatsMyName("marshallMathers"))
      .build();

  JavaFile javaFile = JavaFile.builder("com.example.helloworld", helloWorld)
      .build();

  javaFile.writeTo(System.out);
}

private static MethodSpec whatsMyName(String name) {
  return MethodSpec.methodBuilder(name)
      .returns(String.class)
      .addStatement("return $S", name)
      .build();
}1234567891011121314151617181920
```

输出结果如下:

```java
public final class HelloWorld {
  String slimShady() {
    return "slimShady";
  }

  String eminem() {
    return "eminem";
  }

  String marshallMathers() {
    return "marshallMathers";
  }
}12345678910111213
```

### $T for Types

使用Java内置的类型会使代码比较容易理解。JavaPoet极大的支持这些类型，通过 **$T** 进行映射，会自动`import`声明。

```java
MethodSpec today = MethodSpec.methodBuilder("today")
    .returns(Date.class)
    .addStatement("return new $T()", Date.class)
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC, Modifier.FINAL)
    .addMethod(today)
    .build();

JavaFile javaFile = JavaFile.builder("com.example.helloworld", helloWorld)
    .build();

javaFile.writeTo(System.out);1234567891011121314
```

自动完成import声明，生成代码如下:

```java
package com.example.helloworld;

import java.util.Date;

public final class HelloWorld {
  Date today() {
    return new Date();
  }
}123456789
```

再举一个相似的例子，但是应用了一个不存在的类：

```java
ClassName hoverboard = ClassName.get("com.mattel", "Hoverboard");

MethodSpec today = MethodSpec.methodBuilder("tomorrow")
    .returns(hoverboard)
    .addStatement("return new $T()", hoverboard)
    .build();123456
```

类不存在，但是代码是完整的:

```java
package com.example.helloworld;

import com.mattel.Hoverboard;

public final class HelloWorld {
  Hoverboard tomorrow() {
    return new Hoverboard();
  }
}123456789
```

`ClassName` 这个类非常重要, 当你使用JavaPoet的时候会频繁的使用它。
它可以识别任何声明类。具体看下面的例子:

```java
ClassName hoverboard = ClassName.get("com.mattel", "Hoverboard");
ClassName list = ClassName.get("java.util", "List");
ClassName arrayList = ClassName.get("java.util", "ArrayList");
TypeName listOfHoverboards = ParameterizedTypeName.get(list, hoverboard);

MethodSpec beyond = MethodSpec.methodBuilder("beyond")
    .returns(listOfHoverboards)
    .addStatement("$T result = new $T<>()", listOfHoverboards, arrayList)
    .addStatement("result.add(new $T())", hoverboard)
    .addStatement("result.add(new $T())", hoverboard)
    .addStatement("result.add(new $T())", hoverboard)
    .addStatement("return result")
    .build();12345678910111213
```

JavaPoet将每一种类型进行分解，并尽可能的导入其声明.

```java
package com.example.helloworld;

import com.mattel.Hoverboard;
import java.util.ArrayList;
import java.util.List;

public final class HelloWorld {
  List<Hoverboard> beyond() {
    List<Hoverboard> result = new ArrayList<>();
    result.add(new Hoverboard());
    result.add(new Hoverboard());
    result.add(new Hoverboard());
    return result;
  }
}123456789101112131415
```

#### Import static

JavaPoet支持`import static`。它显示的收集类型成员的名称。例子如下:

```java
...
ClassName namedBoards = ClassName.get("com.mattel", "Hoverboard", "Boards");

MethodSpec beyond = MethodSpec.methodBuilder("beyond")
    .returns(listOfHoverboards)
    .addStatement("$T result = new $T<>()", listOfHoverboards, arrayList)
    .addStatement("result.add($T.createNimbus(2000))", hoverboard)
    .addStatement("result.add($T.createNimbus(\"2001\"))", hoverboard)
    .addStatement("result.add($T.createNimbus($T.THUNDERBOLT))", hoverboard, namedBoards)
    .addStatement("$T.sort(result)", Collections.class)
    .addStatement("return result.isEmpty() $T.emptyList() : result", Collections.class)
    .build();

TypeSpec hello = TypeSpec.classBuilder("HelloWorld")
    .addMethod(beyond)
    .build();

JavaFile.builder("com.example.helloworld", hello)
    .addStaticImport(hoverboard, "createNimbus")
    .addStaticImport(namedBoards, "*")
    .addStaticImport(Collections.class, "*")
    .build();12345678910111213141516171819202122
```

JavaPoet将会首先添加 `import static` 代码块进行配置，当然也需要导入其他所需的类型引用。

```java
package com.example.helloworld;

import static com.mattel.Hoverboard.Boards.*;
import static com.mattel.Hoverboard.createNimbus;
import static java.util.Collections.*;

import com.mattel.Hoverboard;
import java.util.ArrayList;
import java.util.List;

class HelloWorld {
  List<Hoverboard> beyond() {
    List<Hoverboard> result = new ArrayList<>();
    result.add(createNimbus(2000));
    result.add(createNimbus("2001"));
    result.add(createNimbus(THUNDERBOLT));
    sort(result);
    return result.isEmpty() ? emptyList() : result;
  }
}1234567891011121314151617181920
```

### $N for Names

使用 **$N** 可以引用另外一个通过名字生成的声明。

```java
public String byteToHex(int b) {
  char[] result = new char[2];
  result[0] = hexDigit((b >>> 4) & 0xf);
  result[1] = hexDigit(b & 0xf);
  return new String(result);
}

public char hexDigit(int i) {
  return (char) (i < 10 ? i + '0' : i - 10 + 'a');
}12345678910
```

生成的代码如下，在`byteToHex()`方法中通过`$N`来引用 `hexDigit()`方法作为一个参数：

```java
MethodSpec hexDigit = MethodSpec.methodBuilder("hexDigit")
    .addParameter(int.class, "i")
    .returns(char.class)
    .addStatement("return (char) (i < 10 ? i + '0' : i - 10 + 'a')")
    .build();

MethodSpec byteToHex = MethodSpec.methodBuilder("byteToHex")
    .addParameter(int.class, "b")
    .returns(String.class)
    .addStatement("char[] result = new char[2]")
    .addStatement("result[0] = $N((b >>> 4) & 0xf)", hexDigit)
    .addStatement("result[1] = $N(b & 0xf)", hexDigit)
    .addStatement("return new String(result)")
    .build();1234567891011121314
```

### Methods

上面的例子中的方法都有方法体。 使用 `Modifiers.ABSTRACT` 创建的方法是没有方法体的。通常用来创建一个抽象类或接口。

```java
MethodSpec flux = MethodSpec.methodBuilder("flux")
    .addModifiers(Modifier.ABSTRACT, Modifier.PROTECTED)
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC, Modifier.ABSTRACT)
    .addMethod(flux)
    .build();12345678
```

生成如下代码：

```java
public abstract class HelloWorld {
  protected abstract void flux();
}123
```

当执行修饰符的时。JavaPoet用的是
[`javax.lang.model.element.Modifier`](http://docs.oracle.com/javase/8/docs/api/javax/lang/model/element/Modifier.html)类，这个类在android平台上不可用. 这只限制与生成代码阶段；输出的代码可运行在任何平台上: JVMs, Android,
and GWT。

方法可能会有参数，异常，可变参数，注释，注解，类型变量和一个返回类型。这些都可以通过 `MethodSpec.Builder` 来进行配置。

### Constructors

`MethodSpec` 也可以用来创建构造函数:

```java
MethodSpec flux = MethodSpec.constructorBuilder()
    .addModifiers(Modifier.PUBLIC)
    .addParameter(String.class, "greeting")
    .addStatement("this.$N = $N", "greeting", "greeting")
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC)
    .addField(String.class, "greeting", Modifier.PRIVATE, Modifier.FINAL)
    .addMethod(flux)
    .build();1234567891011
```

生成如下代码:

```java
public class HelloWorld {
  private final String greeting;

  public HelloWorld(String greeting) {
    this.greeting = greeting;
  }
}1234567
```

多数情况下，构造方法同普通方法一样。当生成代码时，构造函数会先于其他方法生成。

### Parameters

通过 `ParameterSpec.builder()` 可以创建参数，或者直接调用 `MethodSpec`类的 `addParameter()` 方法添加参数：

```java
ParameterSpec android = ParameterSpec.builder(String.class, "android")
    .addModifiers(Modifier.FINAL)
    .build();

MethodSpec welcomeOverlords = MethodSpec.methodBuilder("welcomeOverlords")
    .addParameter(android)
    .addParameter(String.class, "robot", Modifier.FINAL)
    .build();12345678
```

虽然上面的代码生成`android` 和 `robot`这两个参数是不同的方式，但是输出是一样的：

```java
void welcomeOverlords(final String android, final String robot) {
}12
```

当参数有注解(比如 `@Nullable`)的时候，通过扩展的 `Builder` 方式创建参数是比较方便的。

### Fields

字段通参数一样通过 `build` 方式创建:

```java
FieldSpec android = FieldSpec.builder(String.class, "android")
    .addModifiers(Modifier.PRIVATE, Modifier.FINAL)
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC)
    .addField(android)
    .addField(String.class, "robot", Modifier.PRIVATE, Modifier.FINAL)
    .build();123456789
```

生成如下代码:

```java
public class HelloWorld {
  private final String android;

  private final String robot;
}12345
```

通关 `Builder` 方式很容易生成带注释、注解或者初始化的字段。
Field的初始化代码如下：

```java
FieldSpec android = FieldSpec.builder(String.class, "android")
    .addModifiers(Modifier.PRIVATE, Modifier.FINAL)
    .initializer("$S + $L", "Lollipop v.", 5.0d)
    .build();1234
```

生成代码：

```java
private final String android = "Lollipop v." + 5.0;1
```

### Interfaces

JavaPoet同样可以生成接口。注意接口的方法必须是 `PUBLICABSTRACT` 类型，接口的变量必须是 `PUBLIC STATIC FINAL` 类型。
创建接口的时候必须要添加上这些修饰符。

```java
TypeSpec helloWorld = TypeSpec.interfaceBuilder("HelloWorld")
    .addModifiers(Modifier.PUBLIC)
    .addField(FieldSpec.builder(String.class, "ONLY_THING_THAT_IS_CONSTANT")
        .addModifiers(Modifier.PUBLIC, Modifier.STATIC, Modifier.FINAL)
        .initializer("$S", "change")
        .build())
    .addMethod(MethodSpec.methodBuilder("beep")
        .addModifiers(Modifier.PUBLIC, Modifier.ABSTRACT)
        .build())
    .build();12345678910
```

但是这些修饰符在生成的java文件中是找不到的。这些都是缺省值。

```java
public interface HelloWorld {
  String ONLY_THING_THAT_IS_CONSTANT = "change";

  void beep();
}12345
```

### Enums

通过 `enumBuilder` 可以创建枚举类型, 调用 `addEnumConstant()` 可添加枚举变量：

```java
TypeSpec helloWorld = TypeSpec.enumBuilder("Roshambo")
    .addModifiers(Modifier.PUBLIC)
    .addEnumConstant("ROCK")
    .addEnumConstant("SCISSORS")
    .addEnumConstant("PAPER")
    .build();123456
```

生成如下代码:

```java
public enum Roshambo {
  ROCK,

  SCISSORS,

  PAPER
}1234567
```

Fancy enums 也是支持的。

```java
TypeSpec helloWorld = TypeSpec.enumBuilder("Roshambo")
    .addModifiers(Modifier.PUBLIC)
    .addEnumConstant("ROCK", TypeSpec.anonymousClassBuilder("$S", "fist")
        .addMethod(MethodSpec.methodBuilder("toString")
            .addAnnotation(Override.class)
            .addModifiers(Modifier.PUBLIC)
            .addStatement("return $S", "avalanche!")
            .build())
        .build())
    .addEnumConstant("SCISSORS", TypeSpec.anonymousClassBuilder("$S", "peace")
        .build())
    .addEnumConstant("PAPER", TypeSpec.anonymousClassBuilder("$S", "flat")
        .build())
    .addField(String.class, "handsign", Modifier.PRIVATE, Modifier.FINAL)
    .addMethod(MethodSpec.constructorBuilder()
        .addParameter(String.class, "handsign")
        .addStatement("this.$N = $N", "handsign", "handsign")
        .build())
    .build();12345678910111213141516171819
```

生成代码:

```java
public enum Roshambo {
  ROCK("fist") {
    @Override
    public void toString() {
      return "avalanche!";
    }
  },

  SCISSORS("peace"),

  PAPER("flat");

  private final String handsign;

  Roshambo(String handsign) {
    this.handsign = handsign;
  }
}123456789101112131415161718
```

### Anonymous Inner Classes

在上面的枚举代码汇总，使用了 `Types.anonymousInnerClass()`。匿名内部类也可以在代码块中使用。 通过 `$L` 引用匿名内部类：

```java
TypeSpec comparator = TypeSpec.anonymousClassBuilder("")
    .addSuperinterface(ParameterizedTypeName.get(Comparator.class, String.class))
    .addMethod(MethodSpec.methodBuilder("compare")
        .addAnnotation(Override.class)
        .addModifiers(Modifier.PUBLIC)
        .addParameter(String.class, "a")
        .addParameter(String.class, "b")
        .returns(int.class)
        .addStatement("return $N.length() - $N.length()", "a", "b")
        .build())
    .build();

TypeSpec helloWorld = TypeSpec.classBuilder("HelloWorld")
    .addMethod(MethodSpec.methodBuilder("sortByLength")
        .addParameter(ParameterizedTypeName.get(List.class, String.class), "strings")
        .addStatement("$T.sort($N, $L)", Collections.class, "strings", comparator)
        .build())
    .build();123456789101112131415161718
```

生成的代码包含一个类和一个方法：

```java
void sortByLength(List<String> strings) {
  Collections.sort(strings, new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
      return a.length() - b.length();
    }
  });
}12345678
```

定义匿名内部类的一个特别棘手的问题是参数的构造。在上面的代码中我们传递了不带参数的空字符串。`TypeSpec.anonymousClassBuilder("")`。

### Annotations

对方法添加注解非常简单：

```java
MethodSpec toString = MethodSpec.methodBuilder("toString")
    .addAnnotation(Override.class)
    .returns(String.class)
    .addModifiers(Modifier.PUBLIC)
    .addStatement("return $S", "Hoverboard")
    .build();123456
```

生成如下代码：

```java
  @Override
  public String toString() {
    return "Hoverboard";
  }1234
```

通过 `AnnotationSpec.builder()` 可以对注解设置属性：

```java
MethodSpec logRecord = MethodSpec.methodBuilder("recordEvent")
    .addModifiers(Modifier.PUBLIC, Modifier.ABSTRACT)
    .addAnnotation(AnnotationSpec.builder(Headers.class)
        .addMember("accept", "$S", "application/json; charset=utf-8")
        .addMember("userAgent", "$S", "Square Cash")
        .build())
    .addParameter(LogRecord.class, "logRecord")
    .returns(LogReceipt.class)
    .build();123456789
```

生成如下代码：

```java
@Headers(
    accept = "application/json; charset=utf-8",
    userAgent = "Square Cash"
)
LogReceipt recordEvent(LogRecord logRecord);12345
```

注解同样可以注解其它的注解。通过 `$L` 进行引用：

```java
MethodSpec logRecord = MethodSpec.methodBuilder("recordEvent")
    .addModifiers(Modifier.PUBLIC, Modifier.ABSTRACT)
    .addAnnotation(AnnotationSpec.builder(HeaderList.class)
        .addMember("value", "$L", AnnotationSpec.builder(Header.class)
            .addMember("name", "$S", "Accept")
            .addMember("value", "$S", "application/json; charset=utf-8")
            .build())
        .addMember("value", "$L", AnnotationSpec.builder(Header.class)
            .addMember("name", "$S", "User-Agent")
            .addMember("value", "$S", "Square Cash")
            .build())
        .build())
    .addParameter(LogRecord.class, "logRecord")
    .returns(LogReceipt.class)
    .build();123456789101112131415
```

生成如下代码：

```java
@HeaderList({
    @Header(name = "Accept", value = "application/json; charset=utf-8"),
    @Header(name = "User-Agent", value = "Square Cash")
})
LogReceipt recordEvent(LogRecord logRecord);12345
```

`addMember()` 可以调用多次。

### Javadoc

变量方法和类都可以添加注释:

```java
MethodSpec dismiss = MethodSpec.methodBuilder("dismiss")
    .addJavadoc("Hides {@code message} from the caller's history. Other\n"
        + "participants in the conversation will continue to see the\n"
        + "message in their own history unless they also delete it.\n")
    .addJavadoc("\n")
    .addJavadoc("<p>Use {@link #delete($T)} to delete the entire\n"
        + "conversation for all participants.\n", Conversation.class)
    .addModifiers(Modifier.PUBLIC, Modifier.ABSTRACT)
    .addParameter(Message.class, "message")
    .build();12345678910
```

生成如下：

```java
  /**
   * Hides {@code message} from the caller's history. Other
   * participants in the conversation will continue to see the
   * message in their own history unless they also delete it.
   *
   * <p>Use {@link #delete(Conversation)} to delete the entire
   * conversation for all participants.
   */
  void dismiss(Message message);123456789
```

使用 `$T` 可以自动导入类型的引用

## IDEA使用
1. 所有版本：https://www.jetbrains.com/zh-cn/idea/download/other.html

### 自动生成注释模板

- <https://blog.csdn.net/xiaoliulang0324/article/details/79030752>

```
/**
 * @Author YourName
 * @Description TODO
 * @Date ${DATE} ${TIME}
 **/
```

### 关闭插件val var
```
advanced java folding 关闭即可
```



### idea无法启动

```
idea报错
Picked up JAVA_TOOL_OPTIONS: 
OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
IDE has not been initialized yet



ROOT=~
SOFTWARE=$ROOT/software
jdk_version=jdk-9.0.4+12
export JAVA_HOME=$SOFTWARE/$jdk_version
export JRE_HOME=$SOFTWARE/$jdk_version/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$SOFTWARE/$jdk_version/bin:$PATH
export IDEA_JDK=$JAVA_HOME
sh idea.sh 

要把之前的idea的进程杀死
ps -xf | grep wangzixian/software/idea | awk '{print $1}' | while read line; do kill -9 $line; done


  100  ps -xf | grep idea.sh
  101  ps -xf | grep idea
  102  ps -xf | grep wangzixian/software/idea
  103  ps -xf | grep wangzixian/software/idea | awk '{print $2}'
  104  ps -xf | grep wangzixian/software/idea | awk '{print $1}'
  105  ps -xf | grep wangzixian/software/idea | awk '{print $1}' | while read line; do kill -9 $line; done
  106  sh idea.sh 

```

### 异常 

```
java: JDK isn't specified for module 
https://blog.csdn.net/weixin_44259720/article/details/105294743

在IDEA中关掉该项目，将文件目录下的 .idea文件删除，然后重新打开项目即可。
```



## Jprofiler

### 资料

- jprofiler部署：https://www.cnblogs.com/bumengru/p/7879854.html

```
http://resources.ej-technologies.com/jprofiler/help/doc/index.html?spm=5176.100239.blogcont276.32.pMeguT



/home/wangzixian/task/jprofiler11.0/bin/linux-x64/libjprofilerti.so

/home/wangzixian/task/bin/linux-x64/libjprofilerti.so


https://sre.ink/jprofiler-on-linux/

jprofiler -agentpath:linux-x64/libjprofilerti.so=port=8849,nowait

-agentpath:/home/wangzixian/task/jprofiler11.0\bin\windows-x64\jprofilerti.dll=port=8849 

-agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849

export LD_LIBRARY_PATH=/home/wangzixian/task/jprofiler/bin/linux-x64

export INSTALL4J_JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141/jre

mvn exec:java -Dexec.mainClass="com._4paradigm.predictor.demo.JprofilerTest" -agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849

java -cp stress-0.0.1-SNAPSHOT.jar com._4paradigm.predictor.demo.JprofilerTest

java -agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849

java -jar /home/wangzixian/task/performance-redis-1/qastress/target/stress-0.0.1-SNAPSHOT.jar


java -cp /home/wangzixian/task/performance-redis-1/qastress/target/stress-0.0.1-SNAPSHOT.jar com._4paradigm.predictor.demo.JprofilerTest -agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849


java -agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849 -jar target/stress-0.0.1-SNAPSHOT.jar

添加jvm环境变量
https://segmentfault.com/a/1190000008545160

export JAVA_TOOL_OPTIONS="-agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849"


mvn exec:java -Dexec.mainClass="com.OnlinePredictorClient"
```



### 部署

```
本地和服务器
本地安装可视化的jprofiler
服务器直接安装免费的jprofiler

本地不需要任何配置
服务器需要配置环境变量

对接的时候
注意配置好端口，服务器端口必须空闲没有其他程序占用
服务器端一定要配置好export JAVA_TOOL_OPTIONS="-agentpath:/home/wangzixian/task/jprofiler/bin/linux-x64/libjprofilerti.so=port=5004" 动态程序和端口

使用
先启动服务器端的程序，它会等待客户端连接

启动本地的客户端，打开会话输入服务器地址，用户名等等
最主要是端口必须保持一致
```



### 问题

#### another application is listening on port

```
配置有问题，需要核对单词是否有问题
```

#### Could not bind socket

```

```



## Flink

### 资料

- 开发者资料：<https://ververica.cn/developers-resources/>
- api概念：<https://ci.apache.org/projects/flink/flink-docs-master/zh/dev/api_concepts.html>
- 编程模型：<https://ci.apache.org/projects/flink/flink-docs-master/concepts/programming-model.html>
- lamda表达式在flink中的表现：<https://ci.apache.org/projects/flink/flink-docs-master/zh/dev/java_lambdas.html>
- flink管理内容：<https://my.oschina.net/u/2359207/blog/3086501>
- Apache Flink 类型和序列化机制简介：<https://cloud.tencent.com/developer/article/1240444>
- flink三张状态存储：<https://www.cnblogs.com/029zz010buct/p/9403283.html>
- 状态管理：<https://blog.csdn.net/xorxos/article/details/80877266>
- 官方文档状态管理详细说明：<https://ci.apache.org/projects/flink/flink-docs-release-1.9/dev/stream/state/state.html>
- flink状态翻译：<https://www.jianshu.com/p/e9a330399b30>

### 状态设计

```
状态类型
operator or keyed state
StateDescriptor 状态描述符，状态的名字

可存储状态的形式
ValueState<T> getState(ValueStateDescriptor<T>)
ReducingState<T> getReducingState(ReducingStateDescriptor<T>)
ListState<T> getListState(ListStateDescriptor<T>)
AggregatingState<IN, OUT> getAggregatingState(AggregatingStateDescriptor<IN, ACC, OUT>)
FoldingState<T, ACC> getFoldingState(FoldingStateDescriptor<T, ACC>)
MapState<UK, UV> getMapState(MapStateDescriptor<UK, UV>)

可以进化的状态
Data schema of the state type has evolved, i.e. adding or removing a field from a POJO that is used as state.
Generally speaking, after a change to the data schema, the serialization format of the serializer will need to be upgraded.
Configuration of the serializer has changed.


```

## Avro

### 资料

- java语言使用入门：<https://avro.apache.org/docs/current/gettingstartedjava.html>
- 数据结构介绍：<https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html#avro-complexdatatypes>
- 文档说明：https://avro.apache.org/docs/current/spec.html#preamble

### 创建Schema

```
Schema schema = Schema.createMap(Schema.create(Schema.Type.BOOLEAN)); 
```

### schema的赋值

```

```

### 创建map

```
https://www.programcreek.com/java-api-examples/?class=org.apache.avro.Schema&method=createMap

```



### 创建array

### 创建bytes

### 添加数据

```
avro建议是一次性put数据，递归方式put数据，会将序列化难度加大
比如
多层嵌套Map结构，可以只存储最外围的map，内部的map不再做解析
同样list结构也是，准备好list的数据，作为一个对象直接放到avro中
```

### 数据实体序列化

```

```

### 重要demo

```
demo都在项目的ut中
序列化的演示，TestSeekableByteArrayInput

```

### 对null序列化

```
java中的校验，只有union可以支持默认的null，其他类型不支持

/**
   * Validates that a particular value for a given field is valid according to the
   * following algorithm: 1. If the value is not null, or the field type is null,
   * or the field type is a union which accepts nulls, returns. 2. Else, if the
   * field has a default value, returns. 3. Otherwise throws AvroRuntimeException.
   * 
   * @param field the field to validate.
   * @param value the value to validate.
   * @throws NullPointerException if value is null and the given field does not
   *                              accept null values.
   */
  protected void validate(Field field, Object value) {
    if (isValidValue(field, value)) {
    } else if (field.defaultVal() != null) {
    } else {
      throw new AvroRuntimeException("Field " + field + " does not accept null values");
    }
  }

如果想要支持null的话，可以在avro的外层逻辑解决
比如设置两个schema，一个存储只有null的结果的schema，另一个存储没有null的schema。有null的schema，用自定义的默认值即可。两个schema的命名，可以是有区别的
```

### 序列化

```
avro序列化本质是OutputStream
通过这个封装一层schema解析

写字节流核心代码
由ByteBuffer对象开始写
this.writeFixed(bytes.array(), bytes.arrayOffset() + pos, len);

avro字节码的bytebuffer不能直接转换字符串，需要转16进制，确保字节数组不丢失数据

在构造map结构的，avro反序列是返回hashmap结果，而不是有序map，这是个问题
public class GenericDatumReader<D> implements DatumReader<D> 
 org.apache.avro.generic
    protected Object newMap(Object old, int size) {
        if (old instanceof Map) {
            ((Map)old).clear();
            return old;
        } else {
            return new HashMap(size);
        }
    }

```

### bytebuffer转字符串

```
avro序列化的bytebuffer 是特殊的字节流，前两位是自己的标志位。所以不能简单的用utf-8转字符串
需要一些特殊处理，网络上的方案都不好用，因为字节数组转字符串出现信息丢失情况
但是java不能像c++那样直接地址拷贝，所以可以先转成16进制字符串
Hex.encodeHexString(bytes.array());
<dependency>
            <groupId>commons-codec</groupId>
            <artifactId>commons-codec</artifactId>
            <version>1.9</version>
        </dependency>
```

### avro反序列后map字段

```
这里面有大问题！！！
下面是我debug的信息
deMap 是avro反序列后的结果
本质是string, bytebuffer的结构
但是无法通过row_0查询到结果！！！！！！！！！！！！！！！！！！！！！！！！！
原因是它的key，hash值竟然是0！！！！！！！！！！
avro is so bad

又一次细看，发现，应该传个utf8内部的结构体
String newKey = "row_" + i;
            Utf8 uKey = new Utf8(newKey);
            if (map.get(uKey) == null) {
                throw new RuntimeException("wrong row for window status");
            }
avro is so bad again

logger = {Log4jLogger@3571} 
this = {WindowStatus@3556} 
utf8 = {Utf8@3570} "row_0"
 bytes = {byte[5]@3623} 
 length = 5
 string = "row_0"
  value = {char[5]@3626} 
  hash = 108705547
deMap = {HashMap@3567}  size = 1
 0 = {HashMap$Node@3617} "row_0" -> "java.nio.HeapByteBuffer[pos=0 lim=28 cap=28]"
  key = {Utf8@3618} "row_0"
   bytes = {byte[5]@3624} 
   length = 5
   string = "row_0"
    value = {char[5]@3625} 
     0 = 'r' 114
     1 = 'o' 111
     2 = 'w' 119
     3 = '_' 95
     4 = '0' 48
    hash = 0
  value = {HeapByteBuffer@3619} "java.nio.HeapByteBuffer[pos=0 lim=28 cap=28]"
key = "row_0"
 value = {char[5]@3626} 
 hash = 108705547
logger = {Log4jLogger@3571} 

```

### 注意

- map结构的key默认是string，所以只需要定义value的type



## Parquet文件

### 读取parquet文件

```
https://www.codota.com/code/java/classes/org.apache.hadoop.fs.Path


pandas 0.21 introduces new functions for Parquet:

pd.read_parquet('example_pa.parquet', engine='pyarrow')
or
pd.read_parquet('example_fp.parquet', engine='fastparquet')
```

## CSV文件

逗号切割问题

```
,,广西,百色,,,,,,,,,
针对表格本身有很多空值行为的逗号，是不好切割的
Java里要改成
stringLine.split(",", -1)
-1的意思是切割的内容中间允许空值
```



## Flatbuffer

### 资料

- 官方文档：<https://google.github.io/flatbuffers/index.html#flatbuffers_overview>

### 特点确定使用场景

- **Access to serialized data without parsing/unpacking** - What sets FlatBuffers apart is that it represents hierarchical data in a flat binary buffer in such a way that it can still be accessed directly without parsing/unpacking, while also still supporting data structure evolution (forwards/backwards compatibility).

- **Memory efficiency and speed** - The only memory needed to access your data is that of the buffer. It requires 0 additional allocations (in C++, other languages may vary). FlatBuffers is also very suitable for use with mmap (or streaming), requiring only part of the buffer to be in memory. Access is close to the speed of raw struct access with only one extra indirection (a kind of vtable) to allow for format evolution and optional fields. It is aimed at projects where spending time and space (many memory allocations) to be able to access or construct serialized data is undesirable, such as in games or any other performance sensitive applications. See the [benchmarks](https://google.github.io/flatbuffers/flatbuffers_benchmarks.html) for details.

- **Flexible** - Optional fields means not only do you get great forwards and backwards compatibility (increasingly important for long-lived games: don't have to update all data with each new version!). It also means you have a lot of choice in what data you write and what data you don't, and how you design data structures.

- **Tiny code footprint** - Small amounts of generated code, and just a single small header as the minimum dependency, which is very easy to integrate. Again, see the benchmark section for details.（有代码生成过程）

- **Strongly typed** - Errors happen at compile time rather than manually having to write repetitive and error prone run-time checks. Useful code can be generated for you.

- **Convenient to use** - Generated C++ code allows for terse access & construction code. Then there's optional functionality for parsing schemas and JSON-like text representations at runtime efficiently if needed (faster and more memory efficient than other JSON parsers).

  Java and Go code supports object-reuse. C# has efficient struct based accessors.

- **Cross platform code with no dependencies** - C++ code will work with any recent gcc/clang and VS2010. Comes with build files for the tests & samples (Android .mk files, and cmake for all other platforms).

## 项目集

### jar包资源工具库

```
可以参考开源项目native-lib-loader
基本读写：https://www.mkyong.com/java/java-read-a-file-from-resources-folder/

```

### java网络资源下载器

```

```



## DL4J

### 资料

- 代码导航：https://deeplearning4j.org/docs/latest/deeplearning4j-examples-tour
- 开始深度学习：https://deeplearning4j.org/docs/latest/deeplearning4j-beginners
- 配置dl4j到项目：https://deeplearning4j.org/docs/latest/deeplearning4j-quickstart
- 中文文档：https://deeplearning4j.org/cn/gettingstarted
- 支持keras的能力范围：https://deeplearning4j.org/docs/latest/keras-import-supported-features
- keras模型导入：https://deeplearning4j.org/docs/latest/keras-import-model-import
- 每个版本的新功能和注意点：https://deeplearning4j.org/release-notes#onezerozerobeta5

### 安装

```
deeplearning4j-core, which contains the neural network implementations
nd4j-native-platform, the CPU version of the ND4J library that powers DL4J
datavec-api - Datavec is our library vectorizing and loading data

依赖包如下


```

### 不支持神经网络层

```
GRU
CRF
```



### 问题

#### dyld: lazy symbol binding failed: Symbol not found: ___emutls_get_address

```
原项目本身特别的大
问题非常难定位
后面是抽出需要用的dl4j包，新建一个自己的项目，发现可以正常运行
所以就避开这个不知道怎么冒出来的棘手问题
```

#### Exception in thread "main" java.lang.ClassCastException: java.util.LinkedHashMap cannot be cast to java.util.List

```
https://github.com/eclipse/deeplearning4j/issues/6527

keras版本问题
I reproduce the exception compiling with Keras 2.2.3 and importing with 1.0.0-beta2.
It seems that the keras field for "config" (retrieve here modelConfig.get(config.getModelFieldConfig())) has changed from list of object in version 2.0.X to object representing map.

Keras 2.0.9 :
{ "backend": "tensorflow", "keras_version": "2.0.9", "class_name": "Sequential", "config": [ { "class_name": "Dense", "config": { "kernel_initializer": { "class_name": "VarianceScaling", "config": { "distribution": "uniform", "scale": 1.0, "seed": null, "mode": "fan_avg" }

Keras 2.2.3 :
{ "backend": "tensorflow", "keras_version": "2.2.3", "class_name": "Sequential", "config": { "name": "sequential_1", "layers": [ { "class_name": "Dense", "config": { "name": "dense_1", "trainable": true, "batch_input_shape": [ null, 100 ],

2.0.9和2.2.3内部结构修改了
```



## docker
```
数据可视化利器
https://www.metabase.com/start/docker.html
```

### docker安装

```
  $ docker run -d -p 3000:3000 --name metabase metabase/metabase
```

## Flux & Mono

### 资料

```
异步发射器：https://www.jianshu.com/p/611f3667c4d2
```

## arthas

### 资料

```
官网：https://alibaba.github.io/arthas/
中文使用：https://github.com/alibaba/arthas/blob/master/README_CN.md
国内文档访问更快：https://www.bookstack.cn/read/arthas306/11.md
```

### 笔记

```
Arthas 是Alibaba开源的Java诊断工具，深受开发者喜爱。

当你遇到以下类似问题而束手无策时，Arthas可以帮助你解决：

    这个类从哪个 jar 包加载的？为什么会报各种类相关的 Exception？

    我改的代码为什么没有执行到？难道是我没 commit？分支搞错了？

    遇到问题无法在线上 debug，难道只能通过加日志再重新发布吗？

    线上遇到某个用户的数据处理有问题，但线上同样无法 debug，线下无法重现！

    是否有一个全局视角来查看系统的运行状况？

    有什么办法可以监控到JVM的实时运行状态？

    怎么快速定位应用的热点，生成火焰图？

Arthas支持JDK 6+，支持Linux/Mac/Winodws，采用命令行交互模式，同时提供丰富的 Tab 自动补全功能，进一步方便进行问题的定位和诊断。
```

## jgrapht

```
使用说明：https://www.programcreek.com/java-api-examples/index.php?api=org.jgrapht.EdgeFactory

官网：https://jgrapht.org/
官网使用手册：https://jgrapht.org/guide/UserOverview
demo例子：https://github.com/jgrapht/jgrapht/wiki/Users:-Running-JGraphT-demos
```

## Lucene

### 资料

```
反向索引实现：https://blog.csdn.net/itsoftchenfei/article/details/83052206
FST字典实现：https://www.cnblogs.com/bonelee/p/6226185.html
```

## Gitlab
### 基本使用
```


```




## calsite

### 资料

```
注册一个函数：https://zhuanlan.zhihu.com/p/65472726
calsite基本概念：https://matt33.com/2019/03/07/apache-calcite-process-flow/
javacc研究与心得：https://www.cnblogs.com/Gavin_Liu/archive/2009/03/07/1405029.html

```




[TOC]

