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

### 资料

```
基本语法：https://docs.scala-lang.org/style/indentation.html#line-wrapping
charsheet展示语法：https://docs.scala-lang.org/cheatsheets/index.html
集合api：https://docs.scala-lang.org/overviews/collections-2.13/overview.html
迭代器：https://docs.scala-lang.org/overviews/collections-2.13/trait-iterable.html
列表接口：https://docs.scala-lang.org/overviews/collections-2.13/seqs.html
可修改列表接口：https://docs.scala-lang.org/overviews/collections-2.13/concrete-immutable-collection-classes.html

迭代器高级用法：https://docs.scala-lang.org/overviews/collections-2.13/iterators.html
```

### 符号

```
If the function used :: instead of #::, then every call to the function would result in another call, thus causing an infinite recursion. Since it uses #::, though, the right-hand side is not evaluated until it is requested. Here are the first few elements of the Fibonacci sequence starting with two ones:
```

### 分区

```
自定义分区：https://zhuanlan.zhihu.com/p/43723758

hash分区：有可能出现不同key在一起，因为hash计算后结果会对分区求余，可能分配在一块

自定义分区代码：https://blog.csdn.net/xiao_jun_0820/article/details/45913745

DoubleRDDFunctions

添加一列
scala> postsDf.filter('postTypeId === 1).withColumn("ratio", 'viewCount / 'score). where('ratio < 35).show()

自增id列，高效做法：https://www.jianshu.com/p/3e998a12ec3c
```



# 新的章节

## Spark

### 资料

```
spark最新动态新闻：https://databricks.com/blog
```

### 概念

```
Physical movement of data between partitions is called shuffling

添加一列
```



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

seq转map


不能添加元素，要用arraybuffer
```

#### ArrayBuffer

```
可变集合
添加元素
val listCols : List[String] = cols.toList
listCols:+rowNum
```



### 进阶语法

#### class 与 object区别

```
https://www.jianshu.com/p/e0fc0ab7a9d2
class Counter {
    private var value = 0 
    def increment(step: Int): Unit = { value += step}
    def current(): Int = { value }
}
object MyCounter{
    def main(args:Array[String]){
        val myCounter = new Counter
        myCounter.increment(5)
        println(myCounter.current)
    }
}

scala 中没有 static 关键字对于一个class来说，所有的方法和成员变量在实例被 new 出来之前都是无法访问的因此class文件中的main方法也就没什么用了，scala object 中所有成员变量和方法默认都是 static 的所以 可以直接访问main方法。


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

#### 下划线使用大全

```
https://my.oschina.net/joymufeng/blog/863823

下划线这个符号几乎贯穿了任何一本Scala编程书籍，并且在不同的场景下具有不同的含义，绕晕了不少初学者。正因如此，下划线这个特殊符号无形中增加Scala的入门难度。本文希望帮助初学者踏平这个小山坡。
1. 用于替换Java的等价语法

由于大部分的Java关键字在Scala中拥有了新的含义，所以一些基本的语法在Scala中稍有变化。
1.1 导入通配符

*在Scala中是合法的方法名，所以导入包时要使用_代替。

//Java
import java.util.*;

//Scala
import java.util._

1.2 类成员默认值

Java中类成员可以不赋初始值，编译器会自动帮你设置一个合适的初始值：

class Foo{
     //String类型的默认值为null
     String s;
}

而在Scala中必须要显式指定，如果你比较懒，可以用_让编译器自动帮你设置初始值：

class Foo{
    //String类型的默认值为null
    var s: String = _
}

    该语法只适用于类成员，而不适用于局部变量。

1.3 可变参数

Java声明可变参数如下：

public static void printArgs(String ... args){
    for(Object elem: args){
        System.out.println(elem + " ");
    }
}

调用方法如下：

 //传入两个参数
printArgs("a", "b");
//也可以传入一个数组
printArgs(new String[]{"a", "b"});

在Java中可以直接将数组传给printArgs方法，但是在Scala中，你必须要明确的告诉编译器，你是想将集合作为一个独立的参数传进去，还是想将集合的元素传进去。如果是后者则要借助下划线：

printArgs(List("a", "b"): _*)

1.4 类型通配符

Java的泛型系统有一个通配符类型，例如List<?>，任意的List<T>类型都是List<?>的子类型，如果我们想编写一个可以打印所有List类型元素的方法，可以如下声明：

public static void printList(List<?> list){
    for(Object elem: list){
        System.out.println(elem + " ");
    }
}

对应的Scala版本为：

def printList(list: List[_]): Unit ={
   list.foreach(elem => println(elem + " "))
}

2 模式匹配
2.1 默认匹配

str match{
    case "1" => println("match 1")
    case _   => println("match default")
}

2.2 匹配集合元素

//匹配以0开头，长度为三的列表
expr match {
  case List(0, _, _) => println("found it")
  case _ =>
}

//匹配以0开头，长度任意的列表
expr match {
  case List(0, _*) => println("found it")
  case _ =>
}

//匹配元组元素
expr match {
  case (0, _) => println("found it")
  case _ =>
}

//将首元素赋值给head变量
val List(head, _*) = List("a")

3. Scala特有语法
3.1 访问Tuple元素

val t = (1, 2, 3)
println(t._1, t._2, t._3)

3.2 简写函数字面量（function literal）

如果函数的参数在函数体内只出现一次，则可以使用下划线代替：

val f1 = (_: Int) + (_: Int)
//等价于
val f2 = (x: Int, y: Int) => x + y

list.foreach(println(_))
//等价于
list.foreach(e => println(e))

list.filter(_ > 0)
//等价于
list.filter(x => x > 0)

3.3 定义一元操作符

在Scala中，操作符其实就是方法，例如1 + 1等价于1.+(1)，利用下划线我们可以定义自己的左置操作符，例如Scala中的负数就是用左置操作符实现的：

-2
//等价于
2.unary_-

3.4 定义赋值操作符

我们通过下划线实现赋值操作符，从而可以精确地控制赋值过程：

   class Foo {
      def name = { "foo" }
      def name_=(str: String) {
        println("set name " + str)
   }

    val m = new Foo()
    m.name = "Foo" //等价于: m.name_=("Foo")

3.5 定义部分应用函数（partially applied function）

我们可以为某个函数只提供部分参数进行调用，返回的结果是一个新的函数，即部分应用函数。因为只提供了部分参数，所以部分应用函数也因此而得名。

def sum(a: Int, b: Int, c: Int) = a + b + c
val b = sum(1, _: Int, 3)
b: Int => Int = <function1>
b(2) //6

3.6 将方法转换成函数

Scala中方法和函数是两个不同的概念，方法无法作为参数进行传递，也无法赋值给变量，但是函数是可以的。在Scala中，利用下划线可以将方法转换成函数：

//将println方法转换成函数，并赋值给p
val p = println _  
//p: (Any) => Unit

4. 小结

下划线在大部分的应用场景中是以语法糖的形式出现的，可以减少击键次数，并且代码显得更加简洁。但是对于不熟悉下划线的同学阅读起来稍显困难，希望通过本文能够帮你解决这个的困惑。本文成文仓促，如有遗漏，欢迎留言! 转载请注明作者: joymufeng
```

#### spark分区

```
https://blog.csdn.net/sunspeedzy/article/details/69733837?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
rdd1.mapPartitionsWithIndex{
          (partIdx,iter) => {
              var part_map = scala.collection.mutable.Map[String,Int]()
              while(iter.hasNext){
                  var part_name = "part_" + partIdx;
                  if(part_map.contains(part_name)) {
                     var ele_cnt = part_map(part_name)
                     part_map(part_name) = ele_cnt + 1
                  } else {
                     part_map(part_name) = 1
                  }
                  iter.next()
              }
              part_map.iterator
         }
}.collect
```

#### map和flatmap区别

```
https://blog.csdn.net/u010824591/article/details/50732996
map：对集合中每个元素进行操作。
flatMap：对集合中每个元素进行操作然后再扁平化。

val arr=sc.parallelize(Array(("A",1),("B",2),("C",3)))
arr.flatmap(x=>(x._1+x._2)).foreach(println)

val arr=sc.parallelize(Array(("A",1),("B",2),("C",3)))
arr.map(x=>(x._1+x._2)).foreach(println)
```



### 报错

#### A master URL must be set in your configuration

```
https://blog.csdn.net/sinat_33761963/article/details/51723175
https://www.cnblogs.com/ChristianKula/p/9381180.html

val spark = SparkSession.builder.appName("Simple Application").master("local").getOrCreate()
val data = spark.read.parquet("xxxxx")
println(data.show())
```

#### Spark 2.0 DataFrame map操作中Unable to find encoder for type stored in a Dataset.问题的分析与解决

```
https://www.cnblogs.com/0xcafedaddy/p/7489534.html
要进行map操作，要先定义一个Encoder。。
这就增加了系统升级繁重的工作量了。为了更简单一些，幸运的dataset也提供了转化RDD的操作。因此只需要将之前dataframe.map
在中间修改为：data
```

#### java.lang.RuntimeException: Error while encoding: java.lang.RuntimeException: java.lang.Long is not a valid external type for schema of timestamp

```
https://www.cnblogs.com/xiashiwendao/p/7599386.html
map类型和schema类型不一致导致问题，Schema中定义为Long，但是map的时候映射为String，这里只要把r(1)变为r(1).toLong即可。
sortIdDataframe.rdd.map(row => {
      println(row.getString(3))
        row
    })
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

