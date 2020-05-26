## Scala解决方案

### 安装

- 官方命令行安装：<https://docs.scala-lang.org/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html>

```
mac
brew install sbt@1

linux

```

### 特殊符号

#### =>

```
https://nanxiao.me/scala-function-instance-sugar/
Scala中的=>符号可以看做是创建函数实例的语法糖。例如：A => T，A,B => T表示一个函数的输入参数类型是“A”，“A,B”，返回值类型是T。
另外，() => T表示函数输入参数为空，而A => Unit则表示函数没有返回值。
```

# 新的章节

## Spark

### 资料

### 语法

#### union

```
http://sqlandhadoop.com/spark-dataframe-union-union-all/
```

#### for

```

```



#### until

```
https://blog.csdn.net/ycy258325/article/details/50561677


for (i <- 1 to n)
  r = r * i

说明：1 to n 这个调用返回数字1到数字n的Range(区间)。

to,until都表示范围，二者有何区别？

to为包含上限的闭区间，如：1 to 3,Range为1,2,3;

until不包含上限，如：1 to 3, Range为1,2

在需要使用从0到n-1的区间时，可以使用until方法。

```

#### match

```
https://blog.csdn.net/Next__One/article/details/77666782
```

#### AtomicReference

```
https://www.cnblogs.com/houji/p/6287291.html

```

#### zipWithIndex

```
https://blog.csdn.net/shenxiaoming77/article/details/56288500

问题：
你要遍历一个有序集合，同时你又想访问一个循环计数器，但最重要的是你真的不需要手动创建这个计数器。
解决方案：

    使用zipWithIndex或者zip方法来自动地创建一个计数器，假设你有一个有序集合days，那么你可以使用zipWithIndex和counter来打印带有计数器的集合元素：


使用方法
scala> val days = Array("Sunday", "Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday")
days: Array[String] = Array(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
 
scala> days.zipWithIndex.foreach{case(day,count) => println(s"$count is $day")}
0 is Sunday
1 is Monday
2 is Tuesday
3 is Wednesday
4 is Thursday
5 is Friday
6 is Saturday



scala> val fruits = Array("apple", "banana", "orange")
fruits: Array[String] = Array(apple, banana, orange)
 
scala> for (i <- 0 until fruits.size) println(s"element $i is ${fruits(i)}")
element 0 is apple
element 1 is banana
element 2 is orange

```

#### Seq
```
https://blog.csdn.net/u013176681/article/details/86624076
Scala的Seq将是Java的List，Scala的List将是Java的LinkedList。
```


### 进阶语法

#### class 与 object区别

```

```

#### 遍历

```

```
#### trait
```
语法：https://www.runoob.com/scala/scala-traits.html
Scala Trait(特征) 相当于 Java 的接口，实际上它比接口还功能强大。

与接口不同的是，它还可以定义属性和方法的实现。

一般情况下Scala的类只能够继承单一父类，但是如果是 Trait(特征) 的话就可以继承多个，从结果来看就是实现了多重继承。

Trait(特征) 定义的方式与类类似，但它使用的关键字是 trait，如下所示：

trait Equal {
  def isEqual(x: Any): Boolean
  def isNotEqual(x: Any): Boolean = !isEqual(x)
}
```


## 单元测试

### 资料

- maven配置：https://blog.csdn.net/zpf336/article/details/85036646

### 运行scala测试

```
https://blog.csdn.net/zpf336/article/details/85036646

屏蔽Java的测试
<!-- disable surefire -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>2.8.1</version>
                    <configuration>
                        <skipTests>true</skipTests>
                    </configuration>
                </plugin>
                
                
添加scala插件


<plugin>
                    <groupId>org.scalatest</groupId>
                    <artifactId>scalatest-maven-plugin</artifactId>
                    <version>1.0</version>
                    <configuration>
                        <reportsDirectory>${project.build.directory}/surefire-reports</reportsDirectory>
                        <junitxml>.</junitxml>
                        <filereports>WDF TestResult.txt</filereports>
                    </configuration>
                    <executions>
                        <execution>
                            <id>test</id>
                            <phase>test</phase>
                            <goals>
                                <goal>test</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>


```

### 运行单个scala测试

```
https://stackoverflow.com/questions/24852484/how-to-run-a-single-test-in-scalatest-from-maven

mvn test -Dsuites='org.example.
HelloSuite @a pending test, org.example.HelloWordSpec' 

mvn test -Dsuites='org.example.HelloSuite hello'


```

