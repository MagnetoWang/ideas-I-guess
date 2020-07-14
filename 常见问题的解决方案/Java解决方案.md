## 说明

## 目录

[TOC]



## Java解决方案

### 资料

- Java泛型高级用法：<http://angelikalanger.com/GenericsFAQ/JavaGenericsFAQ.html>

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

### 

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


打印debug日志
https://blog.csdn.net/iteye_6908/article/details/82522034
mvn clean test -Dtest=xxx.xxxTest#方法名  -X
```

#### 安装maven

```
wget mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/binaries/apache-maven-3.6.2-bin.zip
wget mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.2/source/apache-maven-3.6.2-src.tar.gz

unzip apache-maven-3.6.2-bin.zip




在bashrc 和 bash_profiler添加配置
# maven路径
export MAVEN_HOME=~/maven/apache-maven-3.6.2
export PATH=${MAVEN_HOME}/bin:${PATH}


配置仓库源，可以拉取jar包速度更快


自动式安装
wget https://mirror.bit.edu.cn/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
tar xvzf apache-maven-3.6.3-bin.tar.gz
export MAVEN_HOME=`pwd`/apache-maven-3.6.3
export PATH=${MAVEN_HOME}/bin:${PATH}
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

### maven进阶

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
https://blog.csdn.net/HeatDeath/article/details/79833880

<!--可以引入日志 @Slf4j注解-->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
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
# Root logger option
log4j.rootLogger=INFO, stdout

# Direct log messages to stdout
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target=System.out
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m

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

```
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
```

### Queue

```
https://www.jianshu.com/p/c577796e537a

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

```

## JDK8

### getOrDefault

```

```

### System.copyArray

```

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
jar包
 <dependency>
            <groupId>org.apache.jmeter</groupId>
            <artifactId>ApacheJMeter_java</artifactId>
            <version>5.1</version>
        </dependency>

        <dependency>
            <groupId>org.apache.jmeter</groupId>
            <artifactId>ApacheJMeter_http</artifactId>
            <version>2.8</version>
        </dependency>

创建类
@Log4j
public class JmeterTest implements JavaSamplerClient {

    @Override
    public void setupTest(JavaSamplerContext javaSamplerContext) {
        
    }

    @Override
    public SampleResult runTest(JavaSamplerContext javaSamplerContext) {
        return null;
    }

    @Override
    public void teardownTest(JavaSamplerContext javaSamplerContext) {

    }

    @Override
    public Arguments getDefaultParameters() {
        return null;
    }
}

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

```



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

## Spark

### 安装

```
wget http://ftp.kddilabs.jp/infosystems/apache/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
tar -zxvf spark-2.4.5-bin-hadoop2.7.tgz
cp 


```

### 概念

```
spark分区数,task数目,core数,worker节点个数,excutor数量梳理：https://www.cnblogs.com/hadoop-dev/p/6669232.html
spark配置说明：http://spark.apache.org/docs/latest/configuration.html

job，stage，task：https://www.cnblogs.com/upupfeng/p/12385979.html
数量调优：https://www.jianshu.com/p/b3d87df219e9
shuffle调优：https://zhuanlan.zhihu.com/p/21483985

stage
	exchange
	wholestageCodegen
	sortAggregate
	exchange
	sortMergeJoin
	deserializeToObject
	mapPartitios
	mapPartitiosWithIndex
	map
	existingRDD
	exchange
	zipWithIndex

wholestageCodegen
火山模型和直接代码生成的性能区别

CoarseGrainedExecutorBackend
ShuffleBlockFetcherIterator


```



### shuffle排序原理

```
canUseSerializedShuffle：可以序列化排序的数据，达到性能提升作用
```

### 性能优化

```
https://www.jianshu.com/p/dc69ed5c1d66
开启G1GC 通过 -XX:+UseG1GC选项

https://www.cnblogs.com/sxdcgaq8080/p/7196580.html
JVM调优参考
-Xmx300m                   　　　　　　最大堆大小
-Xms300m                　　　　　　　　初始堆大小
-Xmn100m                　  　　　　　　年轻代大小
-XX:SurvivorRatio=8        　　　　　　Eden区与Survivor区的大小比值，设置为8,则两个Survivor区与一个Eden区的比值为2:8,一个Survivor区占整个年轻代的1/10

-XX:+UseG1GC                　　　　　　使用 G1 (Garbage First) 垃圾收集器    
-XX:MaxTenuringThreshold=14        　　提升年老代的最大临界值(tenuring threshold). 默认值为 15[每次GC，增加1岁，到15岁如果还要存活，放入Old区]
-XX:ParallelGCThreads=8            　　设置垃圾收集器在并行阶段使用的线程数[一般设置为本机CPU线程数相等，即本机同时可以处理的个数，设置过大也没有用]
-XX:ConcGCThreads=8            　　　　并发垃圾收集器使用的线程数量


-XX:+DisableExplicitGC　　　　　　　　　　禁止在启动期间显式调用System.gc()


-XX:+HeapDumpOnOutOfMemoryError        OOM时导出堆到文件
-XX:HeapDumpPath=d:/a.dump        　　  导出OOM的路径
-XX:+PrintGCDetails           　　　　   打印GC详细信息
-XX:+PrintGCTimeStamps            　　　 打印CG发生的时间戳
-XX:+PrintHeapAtGC            　　　　　  每一次GC前和GC后，都打印堆信息
-XX:+TraceClassLoading            　　　  监控类的加载
-XX:+PrintClassHistogram        　　　　　 按下Ctrl+Break后，打印类的信息

===================================================================================
join调优
1.减少data shuffle的规模。多map掉无用column再进行reduce like的操作。2.检查数据是否是skewed data。也就是说join出的key value pair大小极度不均。3. Spark参数调优。4.升级集群。至于是否升级，建议采用ganglia监控集群，如果Total used memory的peak接近所有可用memory，那么要么加大spill到disk的量，要么就升级集群内存。
===================================================================================
consolidate机制
下图说明了优化后的HashShuffleManager的原理。这里说的优化，是指我们可以设置一个参数，spark.shuffle.consolidateFiles。该参数默认值为false，将其设置为true即可开启优化机制。通常来说，如果我们使用HashShuffleManager，那么都建议开启这个选项。

开启consolidate机制之后，在shuffle write过程中，task就不是为下游stage的每个task创建一个磁盘文件了。此时会出现shuffleFileGroup的概念，每个shuffleFileGroup会对应一批磁盘文件，磁盘文件的数量与下游stage的task数量是相同的。一个Executor上有多少个CPU core，就可以并行执行多少个task。而第一批并行执行的每个task都会创建一个shuffleFileGroup，并将数据写入对应的磁盘文件内。

当Executor的CPU core执行完一批task，接着执行下一批task时，下一批task就会复用之前已有的shuffleFileGroup，包括其中的磁盘文件。也就是说，此时task会将数据写入已有的磁盘文件中，而不会写入新的磁盘文件中。因此，consolidate机制允许不同的task复用同一批磁盘文件，这样就可以有效将多个task的磁盘文件进行一定程度上的合并，从而大幅度减少磁盘文件的数量，进而提升shuffle write的性能。
===================================================================================
控制每个stage的task数目






===================================================================================
shuffle调优
https://www.cnblogs.com/qingyunzong/p/8954552.html

SortShuffleManager运行原理
SortShuffleManager的运行机制主要分成两种，一种是普通运行机制，另一种是bypass运行机制。当shuffle read task的数量小于等于spark.shuffle.sort.bypassMergeThreshold参数的值时（默认为200），就会启用bypass机制。


===================================================================================
基础调优
https://zhuanlan.zhihu.com/p/21484009

原则一：避免创建重复的RDD
原则二：尽可能复用同一个RDD
原则三：对多次使用的RDD进行持久化
原则四：尽量避免使用shuffle类算子
原则五：使用map-side预聚合的shuffle操作
原则六：使用高性能的算子
原则七：广播大变量
原则八：使用Kryo优化序列化性能
原则九：优化数据结构


===================================================================================
NODE_LOCAL
https://www.cnblogs.com/shishanyuan/p/4721326.html
通过页面监控可以看到该作业分为8个任务，其中一个任务的数据来源于两个数据分片，其他的任务各对应一个数据分片，即显示7个任务获取数据的类型为（NODE_LOCAL），1个任务获取数据的类型为任何位置（ANY）。

数据本地化运行
https://www.cnblogs.com/jxhd1/p/6702224.html
 TaskScheduler在发送task的时候，会根据数据所在的节点发送task,这时候的数据本地化的级别是最高的，如果这个task在这个Executor中等待了三秒，重试发射了5次还是依然无法执行，那么TaskScheduler就会认为这个Executor的计算资源满了，TaskScheduler会降低一级数据本地化的级别，重新发送task到其他的Executor中执行，如果还是依然无法执行，那么继续降低数据本地化的级别...
 
    现在想让每一个task都能拿到最好的数据本地化级别，那么调优点就是等待时间加长。注意！如果过度调大等待时间，虽然为每一个task都拿到了最好的数据本地化级别，但是我们job执行的时间也会随之延长

    spark.locality.wait 3s//相当于是全局的，下面默认以3s为准，手动设置了，以手动的为准
    spark.locality.wait.process
    spark.locality.wait.node
    spark.locality.wait.rack
    newSparkConf.set("spark.locality.wait","100")


===================================================================================
jvm 参数调优
https://www.jianshu.com/p/43f4283df1b7
bin/spark-submit \
--class com.xyz.bigdata.calendar.PeriodCalculator \
--master yarn \
--deploy-mode cluster \
--queue default_queue \
--num-executors 50 \
--executor-cores 2 \
--executor-memory 4G \
--driver-memory 2G \
--conf "spark.default.parallelism=250" \
--conf "spark.shuffle.memoryFraction=0.3" \
--conf "spark.storage.memoryFraction=0.5" \
--conf "spark.driver.extraJavaOptions=-XX:+UseG1GC" \
--conf "spark.executor.extraJavaOptions=-XX:+UseG1GC" \
--verbose \
${PROJECT_DIR}/bigdata-xyz-0.1.jar



===================================================================================
jvm 参考各个代的内存分配
https://www.cnblogs.com/itboys/p/7227893.html



===================================================================================
jvm 垃圾回收器
https://www.cnblogs.com/butterfly100/p/9175673.html
该选用哪一种垃圾回收器？

1. 客户端程序: 一般使用 -XX:+UseSerialGC (Serial + Serial Old). 特别注意, 当一台机器上起多个 JVM, 每个 JVM 也可以采用这种 GC 组合

2. 吞吐率优先的服务端程序（计算密集型）: -XX:+UseParallelGC 或者 -XX:+UseParallelOldGC

3. 响应时间优先的服务端程序: -XX:+UseConcMarkSweepGC

4. 响应时间优先同时也要兼顾吞吐率的服务端程序：-XX:+UseG1GC


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

### Tungsten Engine

```
简要介绍：https://spoddutur.github.io/spark-notes/second_generation_tungsten_engine.html
火山模型和手写代码的性能差距：https://www.cnblogs.com/snova/p/9195692.html
whole codegen：https://www.jianshu.com/p/689bf23f31ed

查询优化技术要点：https://zhuanlan.zhihu.com/p/41562506
Volcano Model是一种经典的基于行的流式迭代模型
```

### 类型转换

```
时间戳 转
```



### 异常

#### Missing an output location for shuffle 4

```
https://blog.csdn.net/weixin_44455388/article/details/101198654

减少shuffle数据
主要从代码层面着手，可以将不必要的数据在shuffle前进行过滤，比如原始数据有20个字段，只要选取需要的字段进行处理即可，将会减少一定的shuffle数据。

修改分区
通过spark.sql.shuffle.partitions控制分区数，默认为200，根据shuffle的量以及计算的复杂度适当提高这个值，例如500。

增加失败的重试次数和重试的时间间隔
通过spark.shuffle.io.maxRetries控制重试次数，默认是3，可适当增加，例如10。
通过spark.shuffle.io.retryWait控制重试的时间间隔，默认是5s，可适当增加，例如10s。

提高executor的内存
在spark-submit提交任务时，适当提高executor的memory值，例如15G或者20G。

考虑是否存在数据倾斜的问题

```

#### Too Large Frame

```
https://yq.aliyun.com/articles/71172
数据倾斜太严重了，集中到一个task
这样导致网络传输开销太大

在成功的任务里，stage26与24的executor完全是同一个，这样数据是完全本地化的，甚至是同一个进程，因而经过优化不再需要通过网络传输
而在失败的任务里，stage26在执行时发现这个node上有3个executor，为了性能的提升，将数据分配给3个executor执行计算。可见其中也成功了一半，32686这个端口的executor是24中执行的那个，因而虽然它要处理3.3g的数据，但是因为不需要网络传输，也仍然可以成功。可是对于另外两个，即使是同一个节点，但是由于是不同进程，仍然需要通过netty的server拉取数据，而这一次的拉取最大不能超过int最大值，因而失败了一个，导致整个stage失败，也就导致了整个job的失败。
总结
由此可见在数据极度倾斜的情况下，增大executor的数量未见得是好事，还是要根据具体情况而来。减小了数量解决了问题，但是这其实并不是最好的解决方案，因为这种情况下，可见数据基本等同于本地执行，完全浪费了集群的并发性，更好的解决方案还需要再继续深入理解。
```

#### Exception in thread "main" java.lang.NoClassDefFoundError: com/sun/jersey/api/client/config/ClientConfig

```
20/07/08 17:29:21 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
log4j:WARN No appenders could be found for logger (org.apache.hadoop.hdfs.BlockReaderLocal).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
Exception in thread "main" java.lang.NoClassDefFoundError: com/sun/jersey/api/client/config/ClientConfig
	at org.apache.hadoop.yarn.client.api.TimelineClient.createTimelineClient(TimelineClient.java:55)
	at org.apache.hadoop.yarn.client.api.impl.YarnClientImpl.createTimelineClient(YarnClientImpl.java:181)
	at org.apache.hadoop.yarn.client.api.impl.YarnClientImpl.serviceInit(YarnClientImpl.java:168)
	at org.apache.hadoop.service.AbstractService.init(AbstractService.java:163)
	at org.apache.spark.deploy.yarn.Client.submitApplication(Client.scala:161)
	at org.apache.spark.deploy.yarn.Client.run(Client.scala:1135)
	at org.apache.spark.deploy.yarn.YarnClusterApplication.start(Client.scala:1527)
	at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:845)
	at org.apache.spark.deploy.SparkSubmit.doRunMain$1(SparkSubmit.scala:161)
	at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:184)
	at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
	at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:920)
	at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:929)
	at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
Caused by: java.lang.ClassNotFoundException: com.sun.jersey.api.client.config.ClientConfig
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 14 more
	
这是某个jar包有问题，需要手动更换下

https://blog.csdn.net/zhanglong_4444/article/details/106097216
spark-2.0后jersey升级到了ver2.x版本，但实际使用时还需要1.x。导致报错。

主要这三个包
jersey-client-1.19.jar
jersey-core-1.19.1.jar
jersey-guice-1.19.jar
放到${SPAKR_HOME}/jars 目录之下
```



## 



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



[TOC]


