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

#### *

```
用于函数参数中可变长参数
https://blog.csdn.net/jxx4903049/article/details/82688117

    scala> def sum(args: Int*) = {
         | var result = 0
         | for (arg <- args) result += arg
         | result
         | }
    sum: (args: Int*)Int
     
    scala> val s = sum(1,2,3,4,5)
    s: Int = 15
    
  

```

### 资料

```
基本语法：https://docs.scala-lang.org/style/indentation.html#line-wrapping
charsheet展示语法：https://docs.scala-lang.org/cheatsheets/index.html
集合api：https://docs.scala-lang.org/overviews/collections-2.13/overview.html
迭代器：https://docs.scala-lang.org/overviews/collections-2.13/trait-iterable.html
列表接口：https://docs.scala-lang.org/overviews/collections-2.13/seqs.html
可修改列表接口：https://docs.scala-lang.org/overviews/collections-2.13/concrete-immutable-collection-classes.html
Array用法：https://docs.scala-lang.org/overviews/collections-2.13/arrays.html

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
dataframe接口：https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset
sql函数接口：https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$
```

### 概念

```
Physical movement of data between partitions is called shuffling

添加一列
```



### 语法

#### val 和 var区别

```
val和var。val就不能再赋值了。与之对应的，var可以在它生命周期中被多次赋值。

https://blog.csdn.net/s646575997/article/details/51264115
```



#### union

```
http://sqlandhadoop.com/spark-dataframe-union-union-all/
```

#### for循环,foreach

```
https://alvinalexander.com/scala/iterating-scala-lists-foreach-for-comprehension/
注意val和var的区别

scala> var sum = 0
sum: Int = 0

scala> val x = List(1,2,3)
x: List[Int] = List(1, 2, 3)

scala> x.foreach(sum += _)

scala> println(sum)
6


https://www.yiibai.com/scala/scala_for_loop.html
for( var x <- Range ){
   statement(s);
}


      for( a <- 1 to 10){
         println( "Value of a: " + a );
      }

打印1到10 包括10

      for( a <- 1 until 10){
         println( "Value of a: " + a );
      }
      
打印1到9，没有10

跳出for循环
https://www.runoob.com/scala/scala-break-statement.html
for (i <- 0 until 10 if flag) {
  res += i
  if (i == 4) flag = false
}
```

#### aggregate

```
dataframe可以实现不同类型转换
https://www.cnblogs.com/mecca/p/5617833.html
文档：https://www.jianshu.com/p/e0fd975055b3

 Scala 学习之 aggregate函数

fold和reduce都要求函数的返回值类型需要和我们所操作的RDD类型相同，但是我们有时确实需要一个不同类型的返回值。eg:

在计算平均值时，需要记录便利过程中的计数以及元素的数量，这就需要我们返回一个二元组。可以先对数据使用map操作，来把元素转移为改元素和1的二元组，也就是我们希望的返回类型。这样reduce就可以以二元组的形式进行归约。

aggregate函数把我们从返回值类型必须与输入RDD类型相同的限制中解脱出来。与fold相似，使用aggregate时，需要我们期待返回的类型的初始值，然后通过一个函数吧RDD中的元素合并起来放入累加器。考虑到每个节点是在本地进行累加的，最终 还需要提供第二个函数来将累加器两两合并。eg：
复制代码

1 val z = sc. parallelize ( List (1 ,2 ,3 ,4 ,5 ,6) , 2)
2 val result = z.aggregate((0,0))(//初始值
3   (acc,value)=>(acc._1+value,acc._2+1),//累加器 （元组累加元组结果，RDD单个元素值）=>（元组累加结果＋RDD单个元素，元组累加计数＋1）
4   (acc1,acc2)=>(acc1._1+acc2._1,acc1._2+acc2._2)//combine 合并函数 合并元组累加结果
5 )
6 val avg = result._1/result._2.toDouble 
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

#### case

```
样例类：https://www.cnblogs.com/MOBIN/p/5299951.html

自动生成apply方法，不需要new就可以创建对象
case本就旨在创建的是不可变数据，所以在使用模式匹配时显得极为容易
自动生成get方法，不能再set
里面对象是不可变的
类似Java的DAO，config的类型

写法如下
case class People(name:String,age:Int)
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

初始化
val partitionColNames = Seq(keyCol, bucketColName)

seq转map

java list 转seq 需要导入包
import scala.collection.JavaConverters._
val keys : Seq[String] = xxxList.asScala
        
或者
import scala.collection.JavaConversions._
val keys : Seq[String] = xxxList.toSeq


不能添加元素，要用arraybuffer
```

#### Array

```

```



#### ArrayBuffer

```
可变集合
添加元素
val listCols : List[String] = cols.toList
listCols:+rowNum
```

#### lazy

```
惰性赋值
https://www.cnblogs.com/cc11001100/p/10243616.html
```



#### 枚举

```
https://www.cnblogs.com/bonnienote/p/6087195.html

object WeekDay extends Enumeration {

   val Mon, Tue, Wed, Thu, Fri, Sat, Sun = Value    

     //在这里定义具体的枚举实例

  }
  
如果不指定ID值，则ID在前一个枚举值基础上＋1，从零开始，缺省name字段为字段名

这时可以用WeekDay.Mon , WeekDay.Tue 来引用枚举值了

这里枚举的类型为WeekDay.Value而不是WeekDay，后者代表对象

可以添加一个类型名称这样定义

object WeekDay extends Enumeration {

    type WeekDay = Value                              

    //这里仅仅是为了将Enumration.Value的类型暴露出来给外界使用而已

    val Mon, Tue, Wed, Thu, Fri, Sat, Sun = Value 

    //在这里定义具体的枚举实例

  }
  
```

#### 可变长参数

```
list通过下划线与星号可以变成n个参数
input.groupBy(cols: _*) // right 多个string对象

input.groupBy(cols) // wrong 一个list对象
```

#### 日期转毫秒

```
spark默认是转到秒级别而不是毫秒
val longCol = data.col(valueCol).cast(LongType)

先转成double * 1000
再转long
val longCol = (data.col(valueCol).cast(doubleType) * 1000).cast(LongType)

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

#### isInstanceOf 和 asInstanceOf 运用

```
https://blog.csdn.net/weixin_42181200/article/details/80324801
首先，需要使用isInstanceOf 判断对象是否为指定类的对象，如果是的话，则可以使用 asInstanceOf 将对象转换为指定类型；
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

#### dataframe

```
基本使用：https://docs.databricks.com/spark/latest/dataframes-datasets/introduction-to-dataframes-scala.html	
reduce简单用法：https://www.zybuluo.com/jewes/note/35032
接口文档：https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset


对某一列求和
var sum : Long = 0
    data.foreach(row => {
      println(row.getLong(row.length - 1))
      sum += row.getLong(row.length - 1)
      println("sum" + sum)
    })
 这样写是错误的，因为spark dataframe 是分布式的，只能计算每个分区的值，sum也拿不出来
 
 spark 有 driver和execute两个端，大部分计算放在execute，如果要拿到真正的值，需要用collect方式拉取到driver。传统的单机编程思维很不适合spark
```

#### 求和

```
终于知道spark该如何求和了！！！！！！！！！！！！！！！！！
var sum : Long = 0
    sum = data.rdd.aggregate((0L))(
      (value, row) => (value + row.getLong(row.length - 1)),
      (value1, value2) => (value1 + value2)
    )
```



### 报错

#### A master URL must be set in your configuration

```
https://blog.csdn.net/sinat_33761963/article/details/51723175
https://www.cnblogs.com/ChristianKula/p/9381180.html

加local

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

