## Scala解决方案

### 安装

- 官方命令行安装：<https://docs.scala-lang.org/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html>

```
mac
brew install sbt@1

linux
wget https://downloads.lightbend.com/scala/2.13.3/scala-2.13.3.tgz
配置path路径，这样scala环境就有了
其他版本号
wget https://downloads.lightbend.com/scala/2.13.3/scala-2.13.3.tgz
wget https://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz
wget https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz

安装spark
wget https://archive.apache.org/dist/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz

tar -zxvf spark-2.3.0-bin-hadoop2.7.tgz

cd spark-2.3.0-bin-hadoop2.7/conf

mv spark-env.sh.template spark-env.sh
vi spark-env.sh：添加SPARK_HOME
vi ~/.bashrc：添加SPARK_HOME      
source ~/.bashrc
执行spark-shell 报错，解决后run fe报错

SPARK_HOME=/home/wangzixian/my-env/spark
vi ~/.bash_profile
#spark 环境
export PATH=$PATH:~/my-env/spark
source ~/.bash_profile

不同版本的spark
wget https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz


要想在idea编写spark程序，最好手动引入jar包和配置scala环境
还要对应上相关的版本号

```

### 命令行

```
java执行scala的包
https://blog.csdn.net/leano/article/details/5867108


可以把idea的执行命令复制下来好好研究
java "-javaagent:/Applications/IntelliJ IDEA.app/Contents/lib/idea_rt.jar=63883:/Applications/IntelliJ IDEA.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath /Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/jre/lib/charsets.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/jre/lib/deploy.jar:/Users/magnetowang/.m2/repository/org/ow2/asm/asm-util/5.2/asm-util-5.2.jar com._4paradigm.ferrari.prophet.SparkUtils
```



### 特殊符号

#### =>

```
https://nanxiao.me/scala-function-instance-sugar/
Scala中的=>符号可以看做是创建函数实例的语法糖。例如：A => T，A,B => T表示一个函数的输入参数类型是“A”，“A,B”，返回值类型是T。
另外，() => T表示函数输入参数为空，而A => Unit则表示函数没有返回值。
```

#### * 和 _*

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
    
  
形参 sum(args: Int*)
如果输入是array类型
那么 sum(arr: _*) 意思是将arr每个元素传入进去

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
dataframe接口：https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html
sql函数接口：https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$
column类型：https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html
统计行数：https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html
groupby例子：https://sparkbyexamples.com/spark/using-groupby-on-dataframe/

2.3文档：https://spark.apache.org/docs/2.3.0/api/scala/index.html#org.apache.spark.sql.Dataset
1.6文档：https://spark.apache.org/docs/1.6.0/api/scala/index.html#org.apache.spark.sql.Dataset

国内文档，访问速度快：http://spark.apachecn.org/#/
文档github项目：https://github.com/apachecn/spark-doc-zh


```

### 概念

```
Physical movement of data between partitions is called shuffling

添加一列
```



### 语法

#### val 和 var区别 - 变量

```

val和var。val就不能再赋值了。与之对应的，var可以在它生命周期中被多次赋值。

https://blog.csdn.net/s646575997/article/details/51264115

var minNum:Int = _ 初始化为0
var minNum:String = _ 初始化null

在java中，作为类的属性时，变量不需要立刻初始化，但是在scala中必须要立刻初始化。
    val的变量定义的时候必须赋值
    var的变量可以使用默认初始化,既用下划线对变量赋值,但是使用的时候要注意以下几点:
    
强制类型
value是any的type
value.asInstanceOf[Int]
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

Seq遍历 
https://www.cnblogs.com/cunchen/p/9464092.html
val names = Seq("Kitty", "Tom", "Luke", "Kit")
for (name <- names) {
  println(name)
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



v1 match  {
      case 1=> "1"
      case 2=> "1"
      case 3=> "2"
      case _=> "default"
    }
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



val tags =  keys :+ "xxx"
Seq类的操作
WHAT IT IS 	WHAT IT DOES
索引和长度 	 
xs(i) 	(或者写作xs apply i)。xs的第i个元素
xs isDefinedAt i 	测试xs.indices中是否包含i。
xs.length 	序列的长度（同size）。
xs.lengthCompare ys 	如果xs的长度小于ys的长度，则返回-1。如果xs的长度大于ys的长度，则返回+1，如果它们长度相等，则返回0。即使其中一个序列是无限的，也可以使用此方法。
xs.indices 	xs的索引范围，从0到xs.length - 1。
索引搜索 	 
xs indexOf x 	返回序列xs中等于x的第一个元素的索引（存在多种变体）。
xs lastIndexOf x 	返回序列xs中等于x的最后一个元素的索引（存在多种变体）。
xs indexOfSlice ys 	查找子序列ys，返回xs中匹配的第一个索引。
xs lastIndexOfSlice ys 	查找子序列ys，返回xs中匹配的倒数一个索引。
xs indexWhere p 	xs序列中满足p的第一个元素。（有多种形式）
xs segmentLength (p, i) 	xs中，从xs(i)开始并满足条件p的元素的最长连续片段的长度。
xs prefixLength p 	xs序列中满足p条件的先头元素的最大个数。
加法： 	 
x +: xs 	由序列xs的前方添加x所得的新序列。
xs :+ x 	由序列xs的后方追加x所得的新序列。
xs padTo (len, x) 	在xs后方追加x，直到长度达到len后得到的序列。
更新 	 
xs patch (i, ys, r) 	将xs中第i个元素开始的r个元素，替换为ys所得的序列。
xs updated (i, x) 	将xs中第i个元素替换为x后所得的xs的副本。
xs(i) = x 	（或写作 xs.update(i, x)，仅适用于可变序列）将xs序列中第i个元素修改为x。
排序 	 
xs.sorted 	通过使用xs中元素类型的标准顺序，将xs元素进行排序后得到的新序列。
xs sortWith lt 	将lt作为比较操作，并以此将xs中的元素进行排序后得到的新序列。
xs sortBy f 	将序列xs的元素进行排序后得到的新序列。参与比较的两个元素各自经f函数映射后得到一个结果，通过比较它们的结果来进行排序。
反转 	 
xs.reverse 	与xs序列元素顺序相反的一个新序列。
xs.reverseIterator 	产生序列xs中元素的反序迭代器。
xs reverseMap f 	以xs的相反顺序，通过f映射xs序列中的元素得到的新序列。
比较 	 
xs startsWith ys 	测试序列xs是否以序列ys开头（存在多种形式）。
xs endsWith ys 	测试序列xs是否以序列ys结束（存在多种形式）。
xs contains x 	测试xs序列中是否存在一个与x相等的元素。
xs containsSlice ys 	测试xs序列中是否存在一个与ys相同的连续子序列。
(xs corresponds ys)(p) 	测试序列xs与序列ys中对应的元素是否满足二元的判断式p。
多集操作 	 
xs intersect ys 	序列xs和ys的交集，并保留序列xs中的顺序。
xs diff ys 	序列xs和ys的差集，并保留序列xs中的顺序。
xs union ys 	并集；同xs ++ ys。
xs.distinct 	不含重复元素的xs的子序列。

```

#### Array

```
array 转seq
val keys: Array[String] = Array(1, 2, 3)
val cols: Seq[String] = keys

def main(args: Array[String]) {
      var myList = Array(1.9, 2.9, 3.4, 3.5)
      
      // Print all the array elements
      for ( x <- myList ) {
         println( x )
      }

      // Summing all elements
      var total = 0.0;
      
      for ( i <- 0 to (myList.length - 1)) {
         total += myList(i);
      }
      println("Total is " + total);

      // Finding the largest element
      var max = myList(0);
      
      for ( i <- 1 to (myList.length - 1) ) {
         if (myList(i) > max) max = myList(i);
      }
      
      println("Max is " + max);
   }
```

#### List

```
不可变列表
// 字符串列表
val site: List[String] = List("Runoob", "Google", "Baidu")

// 整型列表
val nums: List[Int] = List(1, 2, 3, 4)

// 空列表
val empty: List[Nothing] = List()



::: 两个列表可以拼接
:: 列表拼接元素 有操作元
val nums1: List[Int] = List(3, 4)
val nums2: List[Int] = List(1, 2)
nums1 ::: nums2
1 :: nums1 必须1在左边， 意思是nums1调用::方法，参数是1

java list转 seq
https://www.cnblogs.com/pekkle/p/9367577.html
1. List 转 Seq：
List<String> tmpList = new ArrayList<>();
tmpList.add("abc");
Seq<String> tmpSeq = JavaConverters.asScalaIteratorConverter(tmpList.iterator()).asScala().toSeq();

2. Seq 转 List：
List<String> tmpList = scala.collection.JavaConversions.seqAsJavaList(tmpSeq);



```

#### 元祖
```
val pair = (99, "oo", "dsfsd")
println(pair._1)
println(pair._2)
println(pair._3)

```

#### Set
```
val nums = Set(1,2,3)
nums + 5
nums - 3
nums ++ List(5,6)
```



#### Map

```
https://www.runoob.com/scala/scala-maps.html
var A:Map[Char,Int] = Map()

A += ('I' -> 1)
A += ('J' -> 5)
A += ('K' -> 10)
A += ('L' -> 100)


你可以使用 ++ 运算符或 Map.++() 方法来连接两个 Map，Map 合并时会移除重复的 key。
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

override lazy val result: DataFrame = compute
compute是计算方法，被调用一次以后，result不为null，就不会再调用compute了


https://www.cnblogs.com/cc11001100/p/10243616.html
lazy是scala中用来实现惰性赋值的关键字，被lazy修饰的变量初始化的时机是在第一次使用此变量的时候才会赋值，并且仅在第一次调用时计算值，即值只会被计算一次，赋值一次，再之后不会被更改了，这个特性有点熟悉哎？没错，所以lazy修饰的变量必须同时是val修饰的不可变变量。
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


date类型转换问题，转换会有时区问题
https://yq.aliyun.com/articles/618130
首先很直观的是直接把DateType cast 成 LongType, 如下:

df.select(df.col("birth").cast(LongType))

但是这样出来都是 null, 这是为什么? 答案就在 org.apache.spark.sql.catalyst.expressions.Cast 中, 先看 canCast 方法, 可以看到 DateType 其实是可以转成 NumericType 的, 然后再看下面castToLong的方法, 可以看到case DateType => buildCast[Int](_, d => null)居然直接是个 null, 看提交记录其实这边有过反复, 然后为了和 hive 统一, 所以返回最后还是返回 null 了.


```

#### 函数

```
默认参数写法
def addInt( a:Int=5, b:Int=7 ) : Int = {
      var sum:Int = 0
      sum = a + b

      return sum
   }
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

#### column和字符串互转
```
字符串 2 column
cols: Seq[String]
srcDF: DataFrame
val columns = cols.map(srcDF(_))


column 2 string

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
A
1
B
2
C
3


val arr=sc.parallelize(Array(("A",1),("B",2),("C",3)))
arr.map(x=>(x._1+x._2)).foreach(println)
A1
B2
C3
```

#### dataframe

```
基本使用：https://docs.databricks.com/spark/latest/dataframes-datasets/introduction-to-dataframes-scala.html	
reduce简单用法：https://www.zybuluo.com/jewes/note/35032
接口文档：https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset

已知列名，获取的列的索引位置
val tag_index = res.columns.indexOf("xxx")

对某一列求和
var sum : Long = 0
    data.foreach(row => {
      println(row.getLong(row.length - 1))
      sum += row.getLong(row.length - 1)
      println("sum" + sum)
    })
 这样写是错误的，因为spark dataframe 是分布式的，只能计算每个分区的值，sum也拿不出来
 
 spark 有 driver和execute两个端，大部分计算放在execute，如果要拿到真正的值，需要用collect方式拉取到driver。传统的单机编程思维很不适合spark
 
 
写入csv文件
df.coalesce(1).write.option("header", "true").csv("skewData.csv")


distinct
https://xieyuanpeng.com/2019/06/22/spark-distinct-vs-groupBy/
针对整行数据校验，去重。单独列没法用这个函数

reduce、reduceByKey


根据某一列，去重
dropDuplicates
def dropDuplicates(col1: String, cols: String*): Dataset[T]
Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
For a static batch Dataset, it just drops duplicate rows. For a streaming Dataset, it will keep all data across triggers as intermediate state to drop duplicates rows. You can use withWatermark to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.


column的操作
  /**
   * True if the current column is between the lower bound and upper bound, inclusive.
   *
   * @group java_expr_ops
   * @since 1.4.0
   */
  def between(lowerBound: Any, upperBound: Any): Column = {
    (this >= lowerBound) && (this <= upperBound)
  }
  
  
xxx && xxx 这是表示between的意思，不是逻辑与的关系


mapPartitions操作，针对每个分片的计算
// data是dataframe类型，keys是输入字符串list，需要映射成column，然后根据key做分片
val df = data.repartition(keys.map(data(_)): _*)
// 分片以后可以调用mapPartitions，针对每个分片编写计算逻辑，输入是df每一行，也就是row，输出是Iterator[row]，返回一个迭代器，迭代器的元素《类型》就是输入的row
    df.mapPartitions(row => {
    // 返回的迭代器可以是来自flatmap，或者map
      val iter = row.flatMap(row => {
//        row.getLong(0)
        Option(null)

      })
      iter
    })(Encoders(df.schema)) // 这里是最难以理解，新手不明白的地方，encoder表示输出的row，需要编解码，用于网络传输，编解码的字段类型和名字，需要人为给，一般都是原始数据集的schema
    
这是源码中的函数声明
 def mapPartitions[U : Encoder](func: Iterator[T] => Iterator[U]): Dataset[U] = {
 
 
 最后发现encoder这个怎么也编译不过去
 改成rdd就行了
 df.rdd.mapPartitions(row => {
//      row.foreach()
      val iter = row.flatMap(row => {

        logger.info(row.toString())
//        row.getLong(0)
        Option(null)
//        row

      })
      iter
    })

在原有数据基础上增加行数
val res:Dataframe
res.rdd.flatMap(row => {
      val arr = row.toSeq.toArray
      var arrays = Seq(row)
      arrays = arrays :+ Row.fromSeq(arr)
      arrays
    })
    
    
打印分片后的结果
window.repartition(20, keys.map(window(_)): _*).foreach(
      row => {
        println("rows_wzx" + row.toString())
      }
    )


```

#### 求和

```
终于知道spark该如何求和了！！！！！！！！！！！！！！！！！
var sum : Long = 0
    sum = data.rdd.aggregate((0L))(
      (value, row) => (value + row.getLong(row.length - 1)),
      (value1, value2) => (value1 + value2)
    )
    
(0L) 初始值

(value, row) => (value + row.getLong(row.length - 1)) row是rdd里面的对象，针对每个对象需要做的处理 value就是你希望返回的值，这里是求和，希望返回一个整数值结果

(value1, value2) => (value1 + value2) 两个value都是你返回的对象，但是这里的value是对应着每个分区计算的结果，如果是算全局的sum，那么每个分区结果计算完以后，还要求和分区的结果，才是真正的所有数据求和


```

#### partition by和 group by的区别

```
例子说明：https://www.cnblogs.com/hello-yz/p/9962356.html
1. group by是分组函数，partition by是分析函数（然后像sum()等是聚合函数）；

2. 在执行顺序上，

以下是常用sql关键字的优先级

from > where > group by > having > order by

而partition by应用在以上关键字之后，实际上就是在执行完select之后，在所得结果集之上进行partition。

3. partition by相比较于group by，能够在保留全部数据的基础上，只对其中某些字段做分组排序（类似excel中的操作），而group by则只保留参与分组的字段和聚合函数的结果（类似excel中的pivot）。
sql1
select a.cc,a.num, min(a.num) over (partition by a.cc order by a.num asc) as amount
from table_temp a
group by a.cc,a.num;

sql2
select a.cc,a.num, min(a.num) over (partition by a.cc order by a.num desc) as amount
from table_temp a
group by a.cc,a.num;

一个是asc 一个是desc
两个sql的唯一区别在于a.num的排序上，但从结果红框中的数据对比可以看到amount值并不相同，且第二个结果集amount并不都是最小值1。
在这里就是要注意将聚合函数用在partition后的结果集上时，聚合函数是逐条累积计算值的！
逐条累积的意思是：sql1的结果会一样，因为是升序，第一条就是最小值
sql2结果都不一样，因为是降序，每次都会找到最小值
对于数据 1，2，3，4
升序找min
1 1
2 1
3 1
4 1

降序找min，逐条计算找到min
4 4
3 3
2 2
1 1


```



#### 隐式转换和隐式参数

```
https://www.cnblogs.com/MOBIN/p/5351900.html
```

#### 样例类和模式匹配

```

```



#### 尾递归优化

```
scala会针对递归函数做优化
所以不用太担心递归和循环之间性能差问题

```

#### java和scala的写法对比 互转

```
新建list
List<String> nodes = new ArrayList<>();
val nodes: util.List[String] = new util.ArrayList[String]


import scala.collection.JavaConverters._
nodes.asScala



```

#### 自定义函数注册-这样可以使用sql字符串执行

```
https://www.cnblogs.com/itboys/p/9347403.html



调用sqlContext.udf.register()

此时注册的方法 只能在sql()中可见，对DataFrame API不可见

用法：sqlContext.udf.register("makeDt", makeDT(_:String,_:String,_:String))

示例：
复制代码

def makeDT(date: String, time: String, tz: String) = s"$date $time $tz"
sqlContext.udf.register("makeDt", makeDT(_:String,_:String,_:String))
 
// Now we can use our function directly in SparkSQL.
sqlContext.sql("SELECT amount, makeDt(date, time, tz) from df").take(2)
// but not outside
df.select($"customer_id", makeDt($"date", $"time", $"tz"), $"amount").take(2) // fails

复制代码

2）调用spark.sql.function.udf()方法

此时注册的方法，对外部可见

用法：valmakeDt = udf(makeDT(_:String,_:String,_:String))

示例：

import org.apache.spark.sql.functions.udf
val makeDt = udf(makeDT(_:String,_:String,_:String))
// now this works
df.select($"customer_id", makeDt($"date", $"time", $"tz"), $"amount").take(2)

 

```



#### spark-submit

```
https://www.jianshu.com/p/1d41174441b6

spark2-submit \      # 第1行
--class com.google.datalake.TestMain \      #第2行
--master yarn \      # 第3行
--deploy-mode client \      # 第4行
--driver-memory 3g \      # 第5行
--executor-memory 2g \      # 第6行
--total-executor-cores 12 \      # 第7行
--jars /home/jars/test-dep-1.0.0.jar,/home/jars/test-dep2-1.0.0.jar,/home/jars/test-dep3-1.0.0.jar \      # 第8行
/home/release/jars/test-sql.jar \      # 第9行
para1 \      # 第10行
para2 \      # 第11行
"test sql" \      # 第12行
parax      # 第13行

第1行：指定该脚本是一个spark submit脚本（spark老版本是spark-submit，新版本spark2.x是spark2-submit）；
第2行：指定main类的路径；
第3行：指定master（使用第三方yarn作为spark集群的master）；
第4行：指定deploy-mode（应用模式，driver进程运行在spark集群之外的机器，从集群角度来看该机器就像是一个client）；
第5行：分配给driver的内存为3g，也可用m（兆）作为单位；
第6行：分配给单个executor进程的内存为2g，也可用m（兆）作为单位；
第7行：分配的所有executor核数（executor进程数最大值）；
第8行：运行该spark application所需要额外添加的依赖jar，各依赖之间用逗号分隔；
第9行：被提交给spark集群执行的application jar；
第10～13行：传递给main方法的参数，按照添加顺序依次传入，如果某个参数含有空格则需要使用双引号将该参数扩起来；

保留历史执行情况
--conf spark.eventLog.dir=hdfs://m7-qaperf-hdp01/tmp/feoutput/history 
--conf spark.eventLog.enabled=true
```

### 代码代码

#### 初始化

```
val spark = SparkSession.builder.appName("Simple Application").master("local").getOrCreate()
val data = spark.read.parquet(path)
data.coalesce(1).write.option("header", "true").csv(output)

```

#### 定义dataframe

```
import spark.implicits._
val simpleData = Seq(("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  )
val df = simpleData.toDF("employee_name","department","state","salary","age","bonus")
df.show()

读取parquet文件

```

#### 运行scala程序

```
    object RunAppDemo {  
        def main(args: Array[String]): Unit = {
        	println("Hello, Scala")  
        }  
    }  
    
需要用object方式才能编写main函数，class不行！！！
    
```



#### 定义变量和函数

```
val big = new java.math.BigInteger("12345")
val numbers = Array("zero", "one", "two")

def functions(data: DataFrame, keys: Seq[String]): Unit = {

 }


```

#### 统计函数

```
import org.apache.spark.sql.functions._
df.groupBy("department").count()
df.groupBy("department").min()
df.groupBy("department").max()
df.groupBy("department").avg()
```

#### 打印日志

```
import org.slf4j.LoggerFactory
val logger = LoggerFactory.getLogger(this.getClass)
```





### 性能调优

```
所有参数说明：https://www.cnblogs.com/pekkle/p/10525757.html
美团调优：https://tech.meituan.com/2016/04/29/spark-tuning-basic.html
task，job，stage关系：https://www.cnblogs.com/upupfeng/p/12385979.html


分页分段高效查询：https://www.cnblogs.com/whiterock/p/7423715.html
rows_number使用：https://www.cnblogs.com/weixing/p/5460697.html


```



### spark迭代

```
内置百分位计算udf：https://github.com/apache/spark/blob/master/sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/expressions/aggregate/ApproximatePercentile.scala
```



### 无语

```
 override lazy val
 不能lazy var
 不能override var
 这些限制怎么那么多
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

#### scalac bad symbolic reference

```
scalac bad symbolic reference
包引用错误，后面是通过对比pom文件，才发现spark版本号没有对应上
```

#### scala.collection.mutable.Buffer$.empty()Lscala/collection/GenTraversable

```
Exception in thread "main" java.lang.NoSuchMethodError: scala.collection.mutable.Buffer$.empty()Lscala/collection/GenTraversable;
	at org.apache.spark.sql.SparkSessionExtensions.<init>(SparkSessionExtensions.scala:72)
	at org.apache.spark.sql.SparkSession$Builder.<init>(SparkSession.scala:780)
	at org.apache.spark.sql.SparkSession$.builder(SparkSession.scala:981)
	at com._4paradigm.ferrari.prophet.SparkUtils$.getNoRepeatData(SparkUtils.scala:37)
	at com._4paradigm.ferrari.prophet.SparkUtils$.main(SparkUtils.scala:17)
	at com._4paradigm.ferrari.prophet.SparkUtils.main(SparkUtils.scala)
	
scala的版本和打包的jar包没有一致
统一版本号就可以了
```

#### java.lang.NoClassDefFoundError: scala/collection/Seq

```
Exception in thread "main" java.lang.NoClassDefFoundError: scala/collection/Seq
	at com....SparkUtils.main(SparkUtils.scala)
Caused by: java.lang.ClassNotFoundException: scala.collection.Seq
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 1 more
	
java 执行jar包的时候报错，用-cp的命令添加指定的jar包
可以使用通配符
java -cp xxx/*:xxx.jar xxxx
```



#### java.lang.NoClassDefFoundError: org/apache/spark/sql/SparkSession$

```
Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/spark/sql/SparkSession$
	at com._4paradigm.ferrari.prophet.SparkUtils$.getNoRepeatData(SparkUtils.scala:37)
	at com._4paradigm.ferrari.prophet.SparkUtils$.main(SparkUtils.scala:17)
	at com._4paradigm.ferrari.prophet.SparkUtils.main(SparkUtils.scala)
Caused by: java.lang.ClassNotFoundException: org.apache.spark.sql.SparkSession$
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 3 more
	
	
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/spark/sql/Dataset
	at java.lang.Class.getDeclaredMethods0(Native Method)
	at java.lang.Class.privateGetDeclaredMethods(Class.java:2701)
	at java.lang.Class.privateGetMethodRecursive(Class.java:3048)
	at java.lang.Class.getMethod0(Class.java:3018)
	at java.lang.Class.getMethod(Class.java:1784)
	at sun.launcher.LauncherHelper.validateMainClass(LauncherHelper.java:544)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:526)
Caused by: java.lang.ClassNotFoundException: org.apache.spark.sql.Dataset
	at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 7 more


idea 上没有找到jar包，检查pom
scala和spark依赖都添加了！
有可能是编译顺序有问题
scala要先编译
写了简单demo，scala编译成功
那就是spark的依赖没有找到，但是检查实际依赖包，发现有spark的包
pom明明依赖了但是却没有加载，神奇的是，命令行可以执行程序
网上搜索发现
原因是：IDEA默认下是不加载pom下的provided依赖的，而Eclipse是支持的。
所以需要在idea的config中勾选加载provide：https://www.cnblogs.com/parent-absent-son/p/10064856.html




	
```

#### import spark.implicits._ 报红  encoder 也包含，隐士转换排查方向就是怎样让机器知道你这个转换

```
https://blog.csdn.net/qq_39597203/article/details/83006695

def main(args: Array[String]): Unit = {
        //Create SparkConf() And Set AppName
      SparkSession.builder()
                .appName("Spark Sql basic example")
                .config("spark.some.config.option", "some-value")
                .getOrCreate()
 
        //import implicit DF,DS
        import spark.implicits._ //这里的spark出现了红色，无法导入
    }
    
    
def main(args: Array[String]): Unit = {
        //Create SparkConf() And Set AppName
     val spark=  SparkSession.builder()
                .appName("Spark Sql basic example")
                .config("spark.some.config.option", "some-value")
                .getOrCreate()
 
        //import implicit DF,DS
        import spark.implicits._
    }

必须先用sparksession，然后才能从session里面用implicits


```

#### spark type mismatch dataframe

```
大概率是spark和scala版本号没有对齐
尤其是在idea中，一定要手动引入scala和spark的环境变量和jar包
https://blog.csdn.net/shenziheng1/article/details/98541432
还有就是项目重新启动，把.idea删除，这个配置总是有缓存，导致手动的设置不生效
```

#### Failed to load class "org.slf4j.impl.StaticLoggerBinder"

```
https://www.cnblogs.com/justlove/p/7637681.html

需要添加包
<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-nop</artifactId>
			<version>1.7.2</version>
		</dependency>
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

