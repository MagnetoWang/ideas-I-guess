## Spark
### 理解时间
```
2023年3月4号启动

```

### 背景
```


统计命令

wc -l `find . -name '*.scala'`

安装tree命令
tree -ACL 1


```

### spark工作流程
1. 学习阶段
   1. 了解功能
   2. 了解配置
   3. 了解应用
2. 工作阶段
   1. 代码开发
   2. SQL调整
   3. 配置调整
   4. 问题排查
   5. 日志查看
   6. 技术选型
   7. 收集典型任务日志
   8. 异常信息总结
   9. 收集经典优化case
3. 源码阶段
   1. 算子实现
   2. 拼表实现
   3. 版本迭代
   4. 性能优化
   5. 执行流程
   6. 函数调用
   7. 模块梳理
4. 理解
   1. 代码生成更多是解决通用型算子的虚函数调用开销 广泛的内存访问和无法利用流水线、预取、分支预测、SIMD、循环展开等能力。
   2. 

### 参考资料
1. 原理
   1. spark内部实现：https://github.com/JerryLead
   2. SparkInternals
   3. steaming解析：https://github.com/lw-lin/CoolplaySpark
   4. mllib解析：https://github.com/endymecy/spark-ml-source-analysis
2. 应用
   1. sparkML应用示例：https://github.com/sunbow1/SparkMLlibDeepLearn/blob/master/src/CNN/CNN.scala
   2. https://github.com/susanli2016/PySpark-and-MLlib/blob/master/K-Means.ipynb
   3. https://github.com/linzhouzhi/SparkML/blob/master/%E5%9B%9E%E5%BD%92/%E4%BF%9D%E5%BA%8F%E5%9B%9E%E5%BD%92.ipynb
   4. https://github.com/xubo245/SparkLearning
   5. streaming + ml：https://github.com/freeman-lab/spark-ml-streaming/blob/master/python/mlstreaming/kmeans.py
   6. 推荐场景：https://github.com/huangyueranbbc/Spark_ALS
3. 面试
   1. 谷歌苹果Spark面试题，搞懂这些绝对稳稳的 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/679253575
   2. spark常见事故：https://zhuanlan.zhihu.com/p/659056832
   3. 
4. Spark性能调优实战 极客时间课程



### 模块详解 - 横向拆解
1. 数据结构
   1. ExternalAppendOnlyUnsafeRowArray
2. sql - core
   1. 列读取
      1. 源码解析Spark中的Parquet高性能向量化读 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/673930340
      2. 一文全面图解Parquet文件格式 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/680143641
3. catalyst
   1. InternalRow
      1. UnsafeRow UnsafeMapData UnsafeArrayData
         1. org.apache.spark.unsafe
         2. com.esotericsoftware.kryo
      2. GenericInternalRow
   2. JoinedRow
   3. ColumnarRow
   4. ColumnarBatchRow
   5. ColumnVector
      1. OnHeapColumnVector
      2. OnHeapColumnVector
4. 算子
   1. 注册：FunctionRegistryBase
5. 表达式 src/main/scala/org/apache/spark/sql/catalyst/expressions
   1. dsl 加减乘除均封装
   2. expressions
      1. Expression.scala 
      2. AggregateFunction
   3. codegen
      1. 
   4. Cast
      1. canCast canNullSafeCastToDecimal forceNullable
   5. 
   6. project
      1. InterpretedMutableProjection
6. 聚合能力
   1. aggregate
7. 代码生成
   1. WholeStageCodeGeneration WSCG
   2. 
8. SparkStrategy
   1. 路由各个算子和计划能力
9.  列向量
10. 优化规则
    1.  Spark3中的谓词下推VS投影下推 - Tim在路上的文章 - 知乎https://zhuanlan.zhihu.com/p/656673370
    2.  

### 横向拆解 core能力
1. 


### 横向拆解 Row设计 + Schema设计 + dataframe + table
1. sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/InternalRow.scala
2. sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/encoders/RowEncoder.scala
3. sql/catalyst/src/main/scala/org/apache/spark/sql/execution/RowIterator.scala
4. sql/catalyst/src/main/scala/org/apache/spark/sql/Row.scala
5. schema
   1. 

### 横向拆解 列向量设计
1. sql/core/src/main/scala/org/apache/spark/sql/execution/columnar

### 横向拆解 Join设计
1. sql/core/src/main/scala/org/apache/spark/sql/execution/joins
   
#### 大表Join小表
1. Join Key远大于Payload
2. 过滤条件的Selectivity较高

#### 大表Join大表
```
“大表Join大表”的第一种调优思路是“分而治之”，我们要重点掌握它的调优思路以及两个关键环节的优化处理。

“分而治之”的核心思想是通过均匀拆分内表的方式 ，把一个复杂而又庞大的Shuffle Join转化为多个Broadcast Joins，它的目的是，消除原有Shuffle Join中两张大表所引入的海量数据分发，大幅削减磁盘与网络开销的同时，从整体上提升作业端到端的执行性能。

在“分而治之”的调优过程中，内表的拆分最为关键，因为它肩负着Shuffle Join能否成功转化为Broadcast Joins的重要作用。而拆分的关键在于拆分列的选取。为了兼顾执行性能与开发效率，拆分列的基数要足够大，这样才能让子表小到足以放进广播变量，但同时，拆分列的基数也不宜过大，否则实现“分而治之”的开发成本就会陡然上升。通常来说，日期列往往是个不错的选择。

为了避免在调优的过程中引入额外的计算开销，我们要特别注意外表的重复扫描问题。针对外表的重复扫描，我们至少有两种应对方法。第一种是将外表全量缓存到内存，不过这种方法对于内存空间的要求较高，不具备普适性。第二种是利用Spark 3.0版本推出的DPP特性，在数仓设计之初，就以Join Key作为分区键，对外表做分区存储。

当我们做好了内表拆分，同时也避免了外表的重复扫描，我们就可以把原始的Shuffle Join转化为多个Broadcast Joins，在消除海量数据在全网分发的同时，避免引入额外的性能开销。那么毫无疑问，查询经过“分而治之”的调优过后，作业端到端的执行性能一定会得到大幅提升。

```

#### 数据倾斜
```
以Task为粒度解决数据倾斜

学过AQE之后，要应对数据倾斜，想必你很快就会想到AQE的特性：自动倾斜处理。给定如下配置项参数，Spark SQL在运行时可以将策略OptimizeSkewedJoin插入到物理计划中，自动完成Join过程中对于数据倾斜的处理。

spark.sql.adaptive.skewJoin.skewedPartitionFactor，判定倾斜的膨胀系数。
spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes，判定倾斜的最低阈值。
spark.sql.adaptive.advisoryPartitionSizeInBytes，以字节为单位定义拆分粒度。



以Executor为粒度解决数据倾斜
“分而治之”和“两阶段Shuffle”
这里的分而治之与上一讲的分而治之在思想上是一致的，都是以任务分解的方式来解决复杂问题。区别在于我们今天要讲的，是以Join Key是否倾斜为依据来拆解子任务。具体来说，对于外表中所有的Join Keys，我们先按照是否存在倾斜把它们分为两组。一组是存在倾斜问题的Join Keys，另一组是分布均匀的Join Keys。因为给定两组不同的Join Keys，相应地我们把内表的数据也分为两份。


今天这一讲，你需要掌握以Shuffle Join的方式去应对“大表Join大表”的计算场景。数据分布不同，应对方法也不尽相同。

当参与Join的两张表数据分布比较均匀，而且内表的数据分片能够完全放入内存，Shuffle Hash Join的计算效率往往高于Shuffle Sort Merge Join，后者是Spark SQL默认的关联机制。你可以使用关键字“shuffle_hash”的Join Hints，强制Spark SQL在运行时选择Shuffle Hash Join实现机制。对于内表数据分片不能放入内存的情况，你可以结合“三足鼎立”的调优技巧，调整并行度、并发度与执行内存这三类参数，来满足这一前提条件。

当参与Join的两张表存在数据倾斜时，如果倾斜的情况在集群内的Executors之间较为均衡，那么最佳的处理方法就是，利用AQE提供的自动倾斜处理机制。你只需要设置好以下三个参数，剩下的事情交给AQE就好了。

spark.sql.adaptive.skewJoin.skewedPartitionFactor，判定倾斜的膨胀系数。
spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes，判定倾斜的最低阈值。
spark.sql.adaptive.advisoryPartitionSizeInBytes，以字节为单位，定义拆分粒度。
但是，如果倾斜问题仅集中在少数的几个Executors中，而且这些负载过高的Executors已然成为性能瓶颈，我们就需要采用“分而治之”外加“两阶段Shuffle”的调优技巧去应对。“分而治之”指的是根据Join Keys的倾斜与否，将内外表的数据分为两部分分别处理。其中，均匀的部分可以使用Shuffle Hash Join来完成计算，倾斜的部分需要用“两阶段Shuffle”进行处理。

两阶段Shuffle的关键在于加盐和去盐化。加盐的目的是打散数据分布、平衡Executors之间的计算负载，从而消除Executors单点瓶颈。去盐化的目的是还原原始的关联逻辑。尽管两阶段Shuffle的开发成本较高，但只要获得的性能收益足够显著，我们的投入就是值得的。
```


### 横向拆解 过滤器设计
1. sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/StructFilters.scala

### 横向拆解 读写IO设计
1. sql/core/src/main/scala/org/apache/spark/sql/DataFrameWriterV2.scala

### 横向拆解 SQL集成CSV能力
1. sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/csv/CSVInferSchema.scala

### 横向拆解 shuffle
1. [SPARK][CORE] 面试问题 之 Spark Shuffle概述 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524157404
2. [SPARK][CORE] 面试问题之UnsafeShuffleWriter流程解析（上） - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524160470
3. [SPARK][CORE] 面试问题之UnsafeShuffleWriter流程解析（下） - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524161757
4. [SPARK][CORE] 面试问题之 SortShuffleWriter的实现详情 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524159361
5. [SPARK][CORE] 面试问题之 BypassMergeSortShuffleWriter的细节 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524158783
6. 字节：https://www.infoq.cn/article/mar2oiscijee2czyqogn
7. oppo：https://www.infoq.cn/article/pxmvcpffvtmjqsuiat0f
8. Uber 的 RSS [5]：2020 年开源，底层存储基于本地磁盘，Shuffle Server 提供读写数据功能，对性能有一定的影响，另外，开源时间比较早，但维护较少
9. 腾讯的 FireStorm [6]：2021 年 11 月开源，底层存储使用 HDFS，对稳定性以及性能优化设计考虑较少
10. 阿里云 EMR-RSS [7]：2022 年 1 月开源，底层存储基于本地磁盘，对本地 IO 做了深入的优化，不过这种基于本地存储的 Shuffle Service，有着天然的限制
11. LinkedIn MagNet [2]：MagNet 严格来说不算真正意义的 RSS，只能算是 Push Based  的 Shuffle。MagNet 在 Spark 原生 Shuffle 数据落盘的同时把数据 Push 到远端 NodeManager 的 ESS 上，同一份数据，会落盘两次，这样其实会增加集群的 IO 压力。不过，MagNet 已经合入到 Spark3.2 版本，鉴于此，MagNet 的 Shuffle 才做了这样的设计
12. https://github.com/bytedance/CloudShuffleService
13. [SPARK][CORE] 面试问题之 3.2新的特性Push-based Shuffle源码解析 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/528860023
14. BypassMergeSortShuffleWriter和HashShuffle有什么区别？ - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/646831008
15. Remote Shuffle Service 和 Push-based Shuffle 他们的优劣分别是什么？ - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/645382382
16. [SPARK][CORE] 面试问题之谈一谈Push-based shuffle - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/527326885
17. [SPARK][CORE] 面试问题之什么是external shuffle service？ - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/526685828
18. [SPARK][CORE] 面试问题之 Shuffle reader 的细枝末节 （上） - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/524162595
19. [SPARK][CORE] 面试问题之 Shuffle reader 的细枝末节 （下） - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/525122882
```

push-based shuffle是在shuffle write结束后追加了push与合并操作，那么是否只有在发生FetchFailed的情况下（导致stage重试）push-based shuffle的性能更好？

为什么push-based shuffle性能会更加稳定，它的优势是？

push-based shuffle 能否进行精简下？例如取消掉driver端的行为。





```

### 横向拆解 KVStore
1. common/kvstore/src/main/java/org/apache/spark/util/kvstore/RocksDB.java
2. common/kvstore/src/main/java/org/apache/spark/util/kvstore/LevelDB.java
3. 

### 横向拆解 SparkUI前端
1. sql/core/src/main/scala/org/apache/spark/sql/execution/ui

### 横向拆解 内存管理
1. Spark系统与架构系列：内存机制 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/642722131

### 横向拆解 代码生成
1. SparkSql全代码生成规则梳理-CollapseCodegenStages - 小萝卜算子的文章 - 知乎https://zhuanlan.zhihu.com/p/567231268
2.  [SPARK][SQL] Tungsten Codegen 全阶段代码生成，让代码更加"定制化" - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/563332917
3.  spark目前针对cpu和内存的优化有那些? 有哪些调优手段？ - 天天来了的回答 - 知乎 https://www.zhihu.com/question/42924755/answer/2648123201
4. [SPARK][SQL] Tungsten Codegen优势与表达式生成 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/558510076
5. 
```
全阶段代码生成是如何实现的？
1. insertWholeStageCodegen
2. CodegenSupport的还需判断其所有表达式是否都支持Codegen， 当前plan和其孩子plan的schema的字段个数是否超过了conf.wholeStageMaxNumFields（默认100）
3. 需要注意的是whole-stage-codegen是基于row的，如果plan支持columnar， 则不能同时支持全阶段代码生成。

1、全阶段代码生成是将一个Stage的代码进行“捏合”

2、它在执行物理计划前会执行CollapseCodegenStages 规则，它的作用正是尝试为每一个 Stages 生成“手写代码”。

3、每一个WholeStageCodegenExec执行时，首先获取输入inputRDDs，直接从叶子节点获取数据的输入。

4、从父节点到子节点，递归调用 doProduce，生成代码框架，直到遇到 Shuffle Boundary 为止。

5、从子节点到父节点，递归调用 doConsume，向框架填充每一个操作符的运算逻辑。


算子模式函数调用
open() - 初始化一个状态
next() - 产生一个输出
close() - 清理状态
虚函数的调用；
代码本地化能力差，需要保存复杂处理信息等。
内存数据的随机存取。


case说明
select count(userid) from citizens where city = 'beijing'

算子
scan -> filter -> project -> agg

代码
 var count = 0;
 for (citizen <- citizens) {
   if (citizen.city == beijing) count += 1;
 }

```


### 横向拆解 Tungsten
1. Unsafe Row：二进制数据结构
   1. 字节数组的存储方式在消除存储开销的同时，仅用一个数组对象就能轻松完成一条数据的封装，显著降低GC压力
   2. JVM至少需要6个对象才能存储一条用户数据。其中，GenericMutableRow用于封装一条数据，Array用于存储实际的数据值。Array中的每个元素都是一个对象，如承载整型的BoxedInteger、承载字符串的String等等。
2. 内存页管理
   1. 优化GC，提升内存利用率
3. WSCG
   1. WSCG指的是基于同一Stage内操作符之间的调用关系，生成一份“手写代码”，真正把所有计算融合为一个统一的函数。
   2. 火山迭代模型：原因在于，迭代器嵌套的计算模式会涉及两种操作，一个是内存数据的随机存取，另一个是虚函数调用（next）。这两种操作都会降低CPU的缓存命中率，影响CPU的工作效率。
   3. 
```
Schema为（userID，name，age，gender）
jvm 内存对象
首先，存储开销大。我们拿类型是String的name来举例，如果一个用户的名字叫做“Mike”，它本应该只占用4个字节，但在JVM的对象存储中，“Mike”会消耗总共48个字节，其中包括12个字节的对象头信息、8字节的哈希编码、8字节的字段值存储和另外20个字节的其他开销。从4个字节到48个字节，存储开销可见一斑。

其次，在JVM堆内内存中，对象数越多垃圾回收效率越低。因此，一条数据记录用一个对象来封装是最好的。但是，我们从下图中可以看到，JVM需要至少6个对象才能存储一条数据记录。如果你的样本数是1千亿的话，这意味着JVM需要管理6千亿的对象，GC的压力就会陡然上升。

基于内存页的内存管理
为了统一管理Off Heap和On Heap内存空间，Tungsten定义了统一的128位内存地址，简称Tungsten地址。Tungsten地址分为两部分：前64位预留给Java Object，后64位是偏移地址Offset。但是，同样是128位的Tungsten地址，Off Heap和On Heap两块内存空间在寻址方式上截然不同。

对于On Heap空间的Tungsten地址来说，前64位存储的是JVM堆内对象的引用或者说指针，后64位Offset存储的是数据在该对象内的偏移地址。而Off Heap空间则完全不同，在堆外的空间中，由于Spark是通过Java Unsafe API直接管理操作系统内存，不存在内存对象的概念，因此前64位存储的是null值，后64位则用于在堆外空间中直接寻址操作系统的内存空间。

显然，在Tungsten模式下，管理On Heap会比Off Heap更加复杂。这是因为，在On Heap内存空间寻址堆内数据必须经过两步：第一步，通过前64位的Object引用来定位JVM对象；第二步，结合Offset提供的偏移地址在堆内内存空间中找到所需的数据。

JVM对象地址与偏移地址的关系，就好比是数组的起始地址与数组元素偏移地址之间的关系。给定起始地址和偏移地址之后，系统就可以迅速地寻址到数据元素。因此，在上面的两个步骤中，如何通过Object引用来定位JVM对象就是关键了。接下来，我们就重点解释这个环节。


Tungsten使用一种叫做页表（Page Table）的数据结构，来记录从Object引用到JVM对象地址的映射。页表中记录的是一个又一个内存页（Memory Page），内存页实际上就是一个JVM对象而已。只要给定64位的Object引用，Tungsten就能通过页表轻松拿到JVM对象地址，从而完成寻址。

收益
那么，Tungsten使用这种方式来管理内存有什么收益呢？我们不妨以常用的HashMap数据结构为例，来对比Java标准库（java.util.HashMap）和Tungsten模式下的HashMap。
java hashmap问题首先是存储开销和GC负担比较大。结合上面的示意图我们不难发现，存储数据的对象值只占整个HashMap一半的存储空间，另外一半的存储空间用来存储引用和指针，这50%的存储开销还是蛮大的。而且我们发现，图中每一个Key、Value和链表元素都是JVM对象。假设，我们用HashMap来存储一百万条数据条目，那么JVM对象的数量至少是三百万。由于JVM的GC效率与对象数量成反比，因此java.util.HashMap的实现方式对于GC并不友好。

其次，在数据访问的过程中，标准库实现的HashMap容易降低CPU缓存命中率，进而降低CPU利用率。链表这种数据结构的特点是，对写入友好，但访问低效。用链表存储数据的方式确实很灵活，这让JVM可以充分利用零散的内存区域，提升内存利用率。但是，在对链表进行全量扫描的时候，这种零散的存储方式会引入大量的随机内存访问（Random Memory Access）。相比顺序访问，随机内存访问会大幅降低CPU cache命中率。

Tungsten 如何实现自己的hashmap
首先，Tungsten放弃了链表的实现方式，使用数组加内存页的方式来实现HashMap。数组中存储的元素是Hash code和Tungsten内存地址，也就是Object引用外加Offset的128位地址。Tungsten HashMap使用128位地址来寻址数据元素，相比java.util.HashMap大量的链表指针，在存储开销上更低。

其次，Tungsten HashMap的存储单元是内存页，内存页本质上是Java Object，一个内存页可以存储多个数据条目。因此，相比标准库中的HashMap，使用内存页大幅缩减了存储所需的对象数量。比如说，我们需要存储一百万条数据记录，标准库的HashMap至少需要三百万的JVM对象才能存下，而Tungsten HashMap可能只需要几个或是十几个内存页就能存下。对比下来，它们所需的JVM对象数量可以说是天壤之别，显然，Tungsten的实现方式对于GC更加友好。

再者，内存页本质上是JVM对象，其内部使用连续空间来存储数据，内存页加偏移量可以精准地定位到每一个数据元素。因此，在需要扫描HashMap全量数据的时候，得益于内存页中连续存储的方式，内存的访问方式从原来的随机访问变成了顺序读取（Sequential Access）。顺序内存访问会大幅提升CPU cache利用率，减少CPU中断，显著提升CPU利用率



```

#### WSCG
```
火山迭代模型（Volcano Iteration Model，以下简称VI模型）。

从内存中读取父操作符的输出结果作为输入数据
调用hasNext、next方法，以操作符逻辑处理数据，如过滤、投影、聚合等等
将处理后的结果以统一的标准形式输出到内存，供下游算子消费


```

### 横向拆解 容错机制
1. Batch mode容错
2. 在Batch mode下，Structured Streaming利用Checkpoint机制来实现容错。在实际处理数据流中的Micro-batch之前，Checkpoint机制会把该Micro-batch的元信息全部存储到开发者指定的文件系统路径，比如HDFS或是Amazon S3。这样一来，当出现作业或是任务失败时，引擎只需要读取这些事先记录好的元信息，就可以恢复数据流的“断点续传”。
3. 在Checkpoint存储目录下，有几个子目录，分别是offsets、sources、commits和state，它们所存储的内容，就是各个Micro-batch的元信息日志。对于不同子目录所记录的实际内容，我把它们整理到了下面的图解中，供你随时参考。
4. Continuous mode容错
5. 在Continuous mode下，Structured Streaming利用Epoch Marker机制，来实现容错。
```
在Batch mode下，Structured Streaming会将数据流切割为一个个的Micro-batch。对于每一个Micro-batch，引擎都会创建一个与之对应的作业，并将作业交付给Spark SQL与Spark Core付诸优化与执行。

Batch mode的特点是吞吐量大，但是端到端的延迟也比较高，延迟往往维持在秒的量级。Batch mode的高延迟，一方面来自作业调度本身，一方面来自它的容错机制，也就是Checkpoint机制需要预写WAL（Write Ahead Log）日志。

要想获得更低的处理延迟，你可以采用Structured Streaming的Continuous mode计算模型。在Continuous mode下，引擎会创建一个Long running job，来负责消费并服务来自Source的所有消息。

在这种情况下，Continuous mode天然地避开了频繁生成、调度作业而引入的计算开销。与此同时，利用Epoch Marker，通过先处理数据、后记录日志的方式，Continuous mode进一步消除了容错带来的延迟影响。

尺有所短、寸有所长，Batch mode在吞吐量上更胜一筹，而Continuous mode在延迟性方面则能达到毫秒级。

不过，需要特别指出的是，到目前为止，在Continuous mode下，Structured Streaming仅支持非聚合（Aggregation）类操作，比如map、filter、flatMap，等等。而聚合类的操作，比如“流动的Word Count”中的分组计数，Continuous mode暂时是不支持的，这一点难免会限制Continuous mode的应用范围，需要你特别注意。

```



### 初级模块
```

.
├── CHANGE.md
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-binary
├── NOTICE
├── NOTICE-binary
├── R
├── README.md
├── appveyor.yml
├── assembly
├── bin
├── binder
├── build
├── build_distribution.sh
├── build_distribution_with_hive.sh
├── build_distribution_with_odfs.sh
├── build_distribution_with_odfs_hadoop3.sh
├── build_distribution_with_odfs_k8s.sh
├── build_distribution_with_toolkit.sh
├── common
├── conf
├── core
├── data
├── dev
├── docs
├── examples
├── external
├── graphx
├── hadoop-cloud
├── launcher
├── licenses
├── licenses-binary
├── mllib
├── mllib-local
├── pom.xml
├── project
├── python
├── repl
├── resource-managers
├── sbin
├── scalastyle-config.xml
├── settings.xml
├── spark.und
├── sql
├── streaming
├── target
├── tdw-spark-toolkit
├── test.sh
└── tools

```

### core模块 - 122043 total
```
     25 ./java/org/apache/spark/api/java/function/package.scala
     63 ./scala/org/apache/spark/Aggregator.scala
    289 ./scala/org/apache/spark/api/java/JavaDoubleRDD.scala
     43 ./scala/org/apache/spark/api/java/JavaHadoopRDD.scala
     43 ./scala/org/apache/spark/api/java/JavaNewHadoopRDD.scala
   1082 ./scala/org/apache/spark/api/java/JavaPairRDD.scala
    264 ./scala/org/apache/spark/api/java/JavaRDD.scala
    745 ./scala/org/apache/spark/api/java/JavaRDDLike.scala
    767 ./scala/org/apache/spark/api/java/JavaSparkContext.scala
     72 ./scala/org/apache/spark/api/java/JavaSparkStatusTracker.scala
    101 ./scala/org/apache/spark/api/java/JavaUtils.scala
     23 ./scala/org/apache/spark/api/java/package.scala
     69 ./scala/org/apache/spark/api/python/Py4JServer.scala
     74 ./scala/org/apache/spark/api/python/PythonGatewayServer.scala
    184 ./scala/org/apache/spark/api/python/PythonHadoopUtil.scala
     55 ./scala/org/apache/spark/api/python/PythonPartitioner.scala
    966 ./scala/org/apache/spark/api/python/PythonRDD.scala
    683 ./scala/org/apache/spark/api/python/PythonRunner.scala
     99 ./scala/org/apache/spark/api/python/PythonUtils.scala
    388 ./scala/org/apache/spark/api/python/PythonWorkerFactory.scala
    217 ./scala/org/apache/spark/api/python/SerDeUtil.scala
    189 ./scala/org/apache/spark/api/python/WriteInputFormatTestDataGenerator.scala
    350 ./scala/org/apache/spark/api/r/BaseRRunner.scala
     75 ./scala/org/apache/spark/api/r/JVMObjectTracker.scala
     38 ./scala/org/apache/spark/api/r/RAuthHelper.scala
    195 ./scala/org/apache/spark/api/r/RBackend.scala
     54 ./scala/org/apache/spark/api/r/RBackendAuthHandler.scala
    281 ./scala/org/apache/spark/api/r/RBackendHandler.scala
    185 ./scala/org/apache/spark/api/r/RRDD.scala
    179 ./scala/org/apache/spark/api/r/RRunner.scala
    113 ./scala/org/apache/spark/api/r/RUtils.scala
    500 ./scala/org/apache/spark/api/r/SerDe.scala
    253 ./scala/org/apache/spark/BarrierCoordinator.scala
    285 ./scala/org/apache/spark/BarrierTaskContext.scala
     31 ./scala/org/apache/spark/BarrierTaskInfo.scala
    149 ./scala/org/apache/spark/broadcast/Broadcast.scala
     46 ./scala/org/apache/spark/broadcast/BroadcastFactory.scala
     83 ./scala/org/apache/spark/broadcast/BroadcastManager.scala
     25 ./scala/org/apache/spark/broadcast/package.scala
    351 ./scala/org/apache/spark/broadcast/TorrentBroadcast.scala
     48 ./scala/org/apache/spark/broadcast/TorrentBroadcastFactory.scala
     42 ./scala/org/apache/spark/ContextAwareIterator.scala
    317 ./scala/org/apache/spark/ContextCleaner.scala
    149 ./scala/org/apache/spark/Dependency.scala
     41 ./scala/org/apache/spark/deploy/ApplicationDescription.scala
    324 ./scala/org/apache/spark/deploy/client/StandaloneAppClient.scala
     47 ./scala/org/apache/spark/deploy/client/StandaloneAppClientListener.scala
    295 ./scala/org/apache/spark/deploy/Client.scala
    138 ./scala/org/apache/spark/deploy/ClientArguments.scala
     29 ./scala/org/apache/spark/deploy/Command.scala
    198 ./scala/org/apache/spark/deploy/DependencyUtils.scala
    293 ./scala/org/apache/spark/deploy/DeployMessage.scala
     31 ./scala/org/apache/spark/deploy/DriverDescription.scala
     34 ./scala/org/apache/spark/deploy/ExecutorDescription.scala
     31 ./scala/org/apache/spark/deploy/ExecutorState.scala
    178 ./scala/org/apache/spark/deploy/ExternalShuffleService.scala
     37 ./scala/org/apache/spark/deploy/ExternalShuffleServiceSource.scala
    451 ./scala/org/apache/spark/deploy/FaultToleranceTest.scala
     77 ./scala/org/apache/spark/deploy/history/AdhocFsHistoryProvider.scala
    421 ./scala/org/apache/spark/deploy/history/ApplicationCache.scala
    160 ./scala/org/apache/spark/deploy/history/ApplicationHistoryProvider.scala
    177 ./scala/org/apache/spark/deploy/history/BasicEventFilterBuilder.scala
    109 ./scala/org/apache/spark/deploy/history/EventFilter.scala
    225 ./scala/org/apache/spark/deploy/history/EventLogFileCompactor.scala
    283 ./scala/org/apache/spark/deploy/history/EventLogFileReaders.scala
    432 ./scala/org/apache/spark/deploy/history/EventLogFileWriters.scala
   1644 ./scala/org/apache/spark/deploy/history/FsHistoryProvider.scala
     79 ./scala/org/apache/spark/deploy/history/HistoryAppStatusStore.scala
    101 ./scala/org/apache/spark/deploy/history/HistoryPage.scala
    356 ./scala/org/apache/spark/deploy/history/HistoryServer.scala
     90 ./scala/org/apache/spark/deploy/history/HistoryServerArguments.scala
    341 ./scala/org/apache/spark/deploy/history/HistoryServerDiskManager.scala
     86 ./scala/org/apache/spark/deploy/history/HistoryServerMemoryManager.scala
    187 ./scala/org/apache/spark/deploy/history/HybridStore.scala
    263 ./scala/org/apache/spark/deploy/JsonProtocol.scala
     85 ./scala/org/apache/spark/deploy/LocalSparkCluster.scala
    140 ./scala/org/apache/spark/deploy/master/ApplicationInfo.scala
     41 ./scala/org/apache/spark/deploy/master/ApplicationSource.scala
     25 ./scala/org/apache/spark/deploy/master/ApplicationState.scala
     58 ./scala/org/apache/spark/deploy/master/DriverInfo.scala
     33 ./scala/org/apache/spark/deploy/master/DriverState.scala
     56 ./scala/org/apache/spark/deploy/master/ExecutorDesc.scala
     89 ./scala/org/apache/spark/deploy/master/FileSystemPersistenceEngine.scala
     43 ./scala/org/apache/spark/deploy/master/LeaderElectionAgent.scala
   1231 ./scala/org/apache/spark/deploy/master/Master.scala
    112 ./scala/org/apache/spark/deploy/master/MasterArguments.scala
     42 ./scala/org/apache/spark/deploy/master/MasterMessages.scala
     47 ./scala/org/apache/spark/deploy/master/MasterSource.scala
    102 ./scala/org/apache/spark/deploy/master/PersistenceEngine.scala
     78 ./scala/org/apache/spark/deploy/master/RecoveryModeFactory.scala
     24 ./scala/org/apache/spark/deploy/master/RecoveryState.scala
    158 ./scala/org/apache/spark/deploy/master/ui/ApplicationPage.scala
    362 ./scala/org/apache/spark/deploy/master/ui/MasterPage.scala
    116 ./scala/org/apache/spark/deploy/master/ui/MasterWebUI.scala
    178 ./scala/org/apache/spark/deploy/master/WorkerInfo.scala
     24 ./scala/org/apache/spark/deploy/master/WorkerState.scala
     90 ./scala/org/apache/spark/deploy/master/ZooKeeperLeaderElectionAgent.scala
     80 ./scala/org/apache/spark/deploy/master/ZooKeeperPersistenceEngine.scala
    180 ./scala/org/apache/spark/deploy/PythonRunner.scala
    463 ./scala/org/apache/spark/deploy/rest/RestSubmissionClient.scala
    334 ./scala/org/apache/spark/deploy/rest/RestSubmissionServer.scala
    216 ./scala/org/apache/spark/deploy/rest/StandaloneRestServer.scala
     36 ./scala/org/apache/spark/deploy/rest/SubmitRestProtocolException.scala
    146 ./scala/org/apache/spark/deploy/rest/SubmitRestProtocolMessage.scala
     81 ./scala/org/apache/spark/deploy/rest/SubmitRestProtocolRequest.scala
     85 ./scala/org/apache/spark/deploy/rest/SubmitRestProtocolResponse.scala
    260 ./scala/org/apache/spark/deploy/RPackageUtils.scala
    120 ./scala/org/apache/spark/deploy/RRunner.scala
    362 ./scala/org/apache/spark/deploy/security/HadoopDelegationTokenManager.scala
    238 ./scala/org/apache/spark/deploy/security/HadoopFSDelegationTokenProvider.scala
    129 ./scala/org/apache/spark/deploy/security/HBaseDelegationTokenProvider.scala
     55 ./scala/org/apache/spark/deploy/SparkApplication.scala
     68 ./scala/org/apache/spark/deploy/SparkCuratorUtil.scala
    563 ./scala/org/apache/spark/deploy/SparkHadoopUtil.scala
   1547 ./scala/org/apache/spark/deploy/SparkSubmit.scala
    647 ./scala/org/apache/spark/deploy/SparkSubmitArguments.scala
    165 ./scala/org/apache/spark/deploy/StandaloneResourceUtils.scala
    120 ./scala/org/apache/spark/deploy/worker/CommandUtils.scala
    278 ./scala/org/apache/spark/deploy/worker/DriverRunner.scala
    105 ./scala/org/apache/spark/deploy/worker/DriverWrapper.scala
    213 ./scala/org/apache/spark/deploy/worker/ExecutorRunner.scala
    166 ./scala/org/apache/spark/deploy/worker/ui/LogPage.scala
    223 ./scala/org/apache/spark/deploy/worker/ui/WorkerPage.scala
     59 ./scala/org/apache/spark/deploy/worker/ui/WorkerWebUI.scala
    929 ./scala/org/apache/spark/deploy/worker/Worker.scala
    183 ./scala/org/apache/spark/deploy/worker/WorkerArguments.scala
     51 ./scala/org/apache/spark/deploy/worker/WorkerSource.scala
     76 ./scala/org/apache/spark/deploy/worker/WorkerWatcher.scala
    546 ./scala/org/apache/spark/executor/CoarseGrainedExecutorBackend.scala
     33 ./scala/org/apache/spark/executor/CommitDeniedException.scala
   1046 ./scala/org/apache/spark/executor/Executor.scala
     30 ./scala/org/apache/spark/executor/ExecutorBackend.scala
     72 ./scala/org/apache/spark/executor/ExecutorExitCode.scala
     93 ./scala/org/apache/spark/executor/ExecutorLogUrlHandler.scala
    109 ./scala/org/apache/spark/executor/ExecutorMetrics.scala
    189 ./scala/org/apache/spark/executor/ExecutorMetricsPoller.scala
     64 ./scala/org/apache/spark/executor/ExecutorMetricsSource.scala
    132 ./scala/org/apache/spark/executor/ExecutorSource.scala
     59 ./scala/org/apache/spark/executor/InputMetrics.scala
     57 ./scala/org/apache/spark/executor/OutputMetrics.scala
     24 ./scala/org/apache/spark/executor/package.scala
    233 ./scala/org/apache/spark/executor/ProcfsMetricsGetter.scala
    157 ./scala/org/apache/spark/executor/ShuffleReadMetrics.scala
     60 ./scala/org/apache/spark/executor/ShuffleWriteMetrics.scala
    329 ./scala/org/apache/spark/executor/TaskMetrics.scala
    149 ./scala/org/apache/spark/ExecutorAllocationClient.scala
   1008 ./scala/org/apache/spark/ExecutorAllocationManager.scala
    304 ./scala/org/apache/spark/FutureAction.scala
     56 ./scala/org/apache/spark/Heartbeater.scala
    253 ./scala/org/apache/spark/HeartbeatReceiver.scala
     88 ./scala/org/apache/spark/input/FixedLengthBinaryInputFormat.scala
    126 ./scala/org/apache/spark/input/FixedLengthBinaryRecordReader.scala
    217 ./scala/org/apache/spark/input/PortableDataStream.scala
     71 ./scala/org/apache/spark/input/WholeTextFileInputFormat.scala
    124 ./scala/org/apache/spark/input/WholeTextFileRecordReader.scala
    279 ./scala/org/apache/spark/internal/config/ConfigBuilder.scala
    288 ./scala/org/apache/spark/internal/config/ConfigEntry.scala
     64 ./scala/org/apache/spark/internal/config/ConfigProvider.scala
    121 ./scala/org/apache/spark/internal/config/ConfigReader.scala
     79 ./scala/org/apache/spark/internal/config/Deploy.scala
    214 ./scala/org/apache/spark/internal/config/History.scala
     66 ./scala/org/apache/spark/internal/config/Kryo.scala
    107 ./scala/org/apache/spark/internal/config/Network.scala
   2111 ./scala/org/apache/spark/internal/config/package.scala
     69 ./scala/org/apache/spark/internal/config/Python.scala
     45 ./scala/org/apache/spark/internal/config/R.scala
     77 ./scala/org/apache/spark/internal/config/Status.scala
     75 ./scala/org/apache/spark/internal/config/Streaming.scala
     86 ./scala/org/apache/spark/internal/config/Tests.scala
    206 ./scala/org/apache/spark/internal/config/UI.scala
     85 ./scala/org/apache/spark/internal/config/Worker.scala
    183 ./scala/org/apache/spark/internal/io/FileCommitProtocol.scala
     38 ./scala/org/apache/spark/internal/io/HadoopMapRedCommitProtocol.scala
    411 ./scala/org/apache/spark/internal/io/HadoopMapReduceCommitProtocol.scala
     82 ./scala/org/apache/spark/internal/io/HadoopWriteConfigUtil.scala
    459 ./scala/org/apache/spark/internal/io/SparkHadoopWriter.scala
    117 ./scala/org/apache/spark/internal/io/SparkHadoopWriterUtils.scala
    252 ./scala/org/apache/spark/internal/Logging.scala
    217 ./scala/org/apache/spark/internal/plugin/PluginContainer.scala
     88 ./scala/org/apache/spark/internal/plugin/PluginContextImpl.scala
     64 ./scala/org/apache/spark/internal/plugin/PluginEndpoint.scala
     79 ./scala/org/apache/spark/InternalAccumulator.scala
     41 ./scala/org/apache/spark/InterruptibleIterator.scala
    288 ./scala/org/apache/spark/io/CompressionCodec.scala
     23 ./scala/org/apache/spark/io/package.scala
    129 ./scala/org/apache/spark/launcher/LauncherBackend.scala
     25 ./scala/org/apache/spark/launcher/SparkSubmitArgumentsParser.scala
     47 ./scala/org/apache/spark/launcher/WorkerCommandBuilder.scala
     27 ./scala/org/apache/spark/MapOutputStatistics.scala
   1027 ./scala/org/apache/spark/MapOutputTracker.scala
     95 ./scala/org/apache/spark/mapred/SparkHadoopMapRedUtil.scala
    181 ./scala/org/apache/spark/memory/ExecutionMemoryPool.scala
    270 ./scala/org/apache/spark/memory/MemoryManager.scala
     71 ./scala/org/apache/spark/memory/MemoryPool.scala
     73 ./scala/org/apache/spark/memory/package.scala
    138 ./scala/org/apache/spark/memory/StorageMemoryPool.scala
    236 ./scala/org/apache/spark/memory/UnifiedMemoryManager.scala
    215 ./scala/org/apache/spark/metrics/ExecutorMetricType.scala
    151 ./scala/org/apache/spark/metrics/MetricsConfig.scala
    275 ./scala/org/apache/spark/metrics/MetricsSystem.scala
     65 ./scala/org/apache/spark/metrics/sink/ConsoleSink.scala
     74 ./scala/org/apache/spark/metrics/sink/CsvSink.scala
    103 ./scala/org/apache/spark/metrics/sink/GraphiteSink.scala
     42 ./scala/org/apache/spark/metrics/sink/JmxSink.scala
     67 ./scala/org/apache/spark/metrics/sink/MetricsServlet.scala
     23 ./scala/org/apache/spark/metrics/sink/package.scala
    128 ./scala/org/apache/spark/metrics/sink/PrometheusServlet.scala
     24 ./scala/org/apache/spark/metrics/sink/Sink.scala
     68 ./scala/org/apache/spark/metrics/sink/Slf4jSink.scala
    163 ./scala/org/apache/spark/metrics/sink/StatsdReporter.scala
     76 ./scala/org/apache/spark/metrics/sink/StatsdSink.scala
     89 ./scala/org/apache/spark/metrics/source/AccumulatorSource.scala
     48 ./scala/org/apache/spark/metrics/source/JVMCPUSource.scala
     33 ./scala/org/apache/spark/metrics/source/JvmSource.scala
     23 ./scala/org/apache/spark/metrics/source/package.scala
     25 ./scala/org/apache/spark/metrics/source/Source.scala
    110 ./scala/org/apache/spark/metrics/source/StaticSources.scala
     74 ./scala/org/apache/spark/network/BlockDataManager.scala
    124 ./scala/org/apache/spark/network/BlockTransferService.scala
    162 ./scala/org/apache/spark/network/netty/NettyBlockRpcServer.scala
    213 ./scala/org/apache/spark/network/netty/NettyBlockTransferService.scala
     68 ./scala/org/apache/spark/network/netty/SparkTransportConf.scala
    101 ./scala/org/apache/spark/package.scala
     88 ./scala/org/apache/spark/partial/ApproximateActionListener.scala
     27 ./scala/org/apache/spark/partial/ApproximateEvaluator.scala
     42 ./scala/org/apache/spark/partial/BoundedDouble.scala
     64 ./scala/org/apache/spark/partial/CountEvaluator.scala
     52 ./scala/org/apache/spark/partial/GroupedCountEvaluator.scala
     64 ./scala/org/apache/spark/partial/MeanEvaluator.scala
     26 ./scala/org/apache/spark/partial/package.scala
    137 ./scala/org/apache/spark/partial/PartialResult.scala
     90 ./scala/org/apache/spark/partial/SumEvaluator.scala
     33 ./scala/org/apache/spark/Partition.scala
    352 ./scala/org/apache/spark/Partitioner.scala
    143 ./scala/org/apache/spark/rdd/AsyncRDDActions.scala
     66 ./scala/org/apache/spark/rdd/BinaryFileRDD.scala
     91 ./scala/org/apache/spark/rdd/BlockRDD.scala
     93 ./scala/org/apache/spark/rdd/CartesianRDD.scala
     47 ./scala/org/apache/spark/rdd/CheckpointRDD.scala
     52 ./scala/org/apache/spark/rdd/coalesce-public.scala
    398 ./scala/org/apache/spark/rdd/CoalescedRDD.scala
    194 ./scala/org/apache/spark/rdd/CoGroupedRDD.scala
    253 ./scala/org/apache/spark/rdd/DoubleRDDFunctions.scala
     34 ./scala/org/apache/spark/rdd/EmptyRDD.scala
    533 ./scala/org/apache/spark/rdd/HadoopRDD.scala
     93 ./scala/org/apache/spark/rdd/InputFileBlockHolder.scala
    227 ./scala/org/apache/spark/rdd/JdbcRDD.scala
     67 ./scala/org/apache/spark/rdd/LocalCheckpointRDD.scala
     78 ./scala/org/apache/spark/rdd/LocalRDDCheckpointData.scala
     69 ./scala/org/apache/spark/rdd/MapPartitionsRDD.scala
    403 ./scala/org/apache/spark/rdd/NewHadoopRDD.scala
    101 ./scala/org/apache/spark/rdd/OrderedRDDFunctions.scala
     23 ./scala/org/apache/spark/rdd/package.scala
   1196 ./scala/org/apache/spark/rdd/PairRDDFunctions.scala
    156 ./scala/org/apache/spark/rdd/ParallelCollectionRDD.scala
    113 ./scala/org/apache/spark/rdd/PartitionerAwareUnionRDD.scala
     82 ./scala/org/apache/spark/rdd/PartitionPruningRDD.scala
     78 ./scala/org/apache/spark/rdd/PartitionwiseSampledRDD.scala
    246 ./scala/org/apache/spark/rdd/PipedRDD.scala
   2136 ./scala/org/apache/spark/rdd/RDD.scala
     80 ./scala/org/apache/spark/rdd/RDDBarrier.scala
    112 ./scala/org/apache/spark/rdd/RDDCheckpointData.scala
    158 ./scala/org/apache/spark/rdd/RDDOperationScope.scala
    337 ./scala/org/apache/spark/rdd/ReliableCheckpointRDD.scala
     87 ./scala/org/apache/spark/rdd/ReliableRDDCheckpointData.scala
     81 ./scala/org/apache/spark/rdd/SequenceFileRDDFunctions.scala
    117 ./scala/org/apache/spark/rdd/ShuffledRDD.scala
    136 ./scala/org/apache/spark/rdd/SubtractedRDD.scala
    116 ./scala/org/apache/spark/rdd/UnionRDD.scala
    102 ./scala/org/apache/spark/rdd/util/PeriodicRDDCheckpointer.scala
     69 ./scala/org/apache/spark/rdd/WholeTextFileRDD.scala
    153 ./scala/org/apache/spark/rdd/ZippedPartitionsRDD.scala
     70 ./scala/org/apache/spark/rdd/ZippedWithIndexRDD.scala
     77 ./scala/org/apache/spark/resource/ExecutorResourceRequest.scala
    150 ./scala/org/apache/spark/resource/ExecutorResourceRequests.scala
    113 ./scala/org/apache/spark/resource/ResourceAllocator.scala
     66 ./scala/org/apache/spark/resource/ResourceDiscoveryScriptPlugin.scala
    101 ./scala/org/apache/spark/resource/ResourceInformation.scala
    491 ./scala/org/apache/spark/resource/ResourceProfile.scala
     99 ./scala/org/apache/spark/resource/ResourceProfileBuilder.scala
    128 ./scala/org/apache/spark/resource/ResourceProfileManager.scala
    490 ./scala/org/apache/spark/resource/ResourceUtils.scala
     58 ./scala/org/apache/spark/resource/TaskResourceRequest.scala
     88 ./scala/org/apache/spark/resource/TaskResourceRequests.scala
    218 ./scala/org/apache/spark/rpc/netty/Dispatcher.scala
    236 ./scala/org/apache/spark/rpc/netty/Inbox.scala
    194 ./scala/org/apache/spark/rpc/netty/MessageLoop.scala
     67 ./scala/org/apache/spark/rpc/netty/NettyRpcCallContext.scala
    759 ./scala/org/apache/spark/rpc/netty/NettyRpcEnv.scala
     91 ./scala/org/apache/spark/rpc/netty/NettyStreamManager.scala
    283 ./scala/org/apache/spark/rpc/netty/Outbox.scala
     40 ./scala/org/apache/spark/rpc/netty/RpcEndpointVerifier.scala
     50 ./scala/org/apache/spark/rpc/RpcAddress.scala
     41 ./scala/org/apache/spark/rpc/RpcCallContext.scala
    164 ./scala/org/apache/spark/rpc/RpcEndpoint.scala
     74 ./scala/org/apache/spark/rpc/RpcEndpointAddress.scala
     22 ./scala/org/apache/spark/rpc/RpcEndpointNotFoundException.scala
    120 ./scala/org/apache/spark/rpc/RpcEndpointRef.scala
    206 ./scala/org/apache/spark/rpc/RpcEnv.scala
     20 ./scala/org/apache/spark/rpc/RpcEnvStoppedException.scala
    134 ./scala/org/apache/spark/rpc/RpcTimeout.scala
     49 ./scala/org/apache/spark/scheduler/AccumulableInfo.scala
     69 ./scala/org/apache/spark/scheduler/ActiveJob.scala
    218 ./scala/org/apache/spark/scheduler/AsyncEventQueue.scala
     65 ./scala/org/apache/spark/scheduler/BarrierJobAllocationFailed.scala
    147 ./scala/org/apache/spark/scheduler/cluster/CoarseGrainedClusterMessage.scala
    917 ./scala/org/apache/spark/scheduler/cluster/CoarseGrainedSchedulerBackend.scala
     47 ./scala/org/apache/spark/scheduler/cluster/ExecutorData.scala
     77 ./scala/org/apache/spark/scheduler/cluster/ExecutorInfo.scala
     47 ./scala/org/apache/spark/scheduler/cluster/SchedulerBackendUtils.scala
    264 ./scala/org/apache/spark/scheduler/cluster/StandaloneSchedulerBackend.scala
   2495 ./scala/org/apache/spark/scheduler/DAGScheduler.scala
    107 ./scala/org/apache/spark/scheduler/DAGSchedulerEvent.scala
     52 ./scala/org/apache/spark/scheduler/DAGSchedulerSource.scala
    617 ./scala/org/apache/spark/scheduler/dynalloc/ExecutorMonitor.scala
    322 ./scala/org/apache/spark/scheduler/EventLoggingListener.scala
     40 ./scala/org/apache/spark/scheduler/ExecutorDecommissionInfo.scala
     54 ./scala/org/apache/spark/scheduler/ExecutorFailuresInTaskSet.scala
     78 ./scala/org/apache/spark/scheduler/ExecutorLossReason.scala
     40 ./scala/org/apache/spark/scheduler/ExecutorResourceInfo.scala
     62 ./scala/org/apache/spark/scheduler/ExternalClusterManager.scala
    491 ./scala/org/apache/spark/scheduler/HealthTracker.scala
    183 ./scala/org/apache/spark/scheduler/InputFormatInfo.scala
     28 ./scala/org/apache/spark/scheduler/JobListener.scala
     32 ./scala/org/apache/spark/scheduler/JobResult.scala
     72 ./scala/org/apache/spark/scheduler/JobWaiter.scala
    306 ./scala/org/apache/spark/scheduler/LiveListenerBus.scala
    181 ./scala/org/apache/spark/scheduler/local/LocalSchedulerBackend.scala
    283 ./scala/org/apache/spark/scheduler/MapStatus.scala
    235 ./scala/org/apache/spark/scheduler/OutputCommitCoordinator.scala
     24 ./scala/org/apache/spark/scheduler/package.scala
    128 ./scala/org/apache/spark/scheduler/Pool.scala
    157 ./scala/org/apache/spark/scheduler/ReplayListenerBus.scala
     68 ./scala/org/apache/spark/scheduler/ResultStage.scala
     97 ./scala/org/apache/spark/scheduler/ResultTask.scala
     50 ./scala/org/apache/spark/scheduler/Schedulable.scala
    205 ./scala/org/apache/spark/scheduler/SchedulableBuilder.scala
    115 ./scala/org/apache/spark/scheduler/SchedulerBackend.scala
     75 ./scala/org/apache/spark/scheduler/SchedulingAlgorithm.scala
     29 ./scala/org/apache/spark/scheduler/SchedulingMode.scala
     97 ./scala/org/apache/spark/scheduler/ShuffleMapStage.scala
    105 ./scala/org/apache/spark/scheduler/ShuffleMapTask.scala
    575 ./scala/org/apache/spark/scheduler/SparkListener.scala
    104 ./scala/org/apache/spark/scheduler/SparkListenerBus.scala
     84 ./scala/org/apache/spark/scheduler/SplitInfo.scala
    126 ./scala/org/apache/spark/scheduler/Stage.scala
    113 ./scala/org/apache/spark/scheduler/StageInfo.scala
    199 ./scala/org/apache/spark/scheduler/StatsReportListener.scala
    242 ./scala/org/apache/spark/scheduler/Task.scala
    197 ./scala/org/apache/spark/scheduler/TaskDescription.scala
    125 ./scala/org/apache/spark/scheduler/TaskInfo.scala
     32 ./scala/org/apache/spark/scheduler/TaskLocality.scala
     86 ./scala/org/apache/spark/scheduler/TaskLocation.scala
    108 ./scala/org/apache/spark/scheduler/TaskResult.scala
    176 ./scala/org/apache/spark/scheduler/TaskResultGetter.scala
    133 ./scala/org/apache/spark/scheduler/TaskScheduler.scala
   1236 ./scala/org/apache/spark/scheduler/TaskSchedulerImpl.scala
     36 ./scala/org/apache/spark/scheduler/TaskSet.scala
    164 ./scala/org/apache/spark/scheduler/TaskSetExcludeList.scala
   1195 ./scala/org/apache/spark/scheduler/TaskSetManager.scala
     36 ./scala/org/apache/spark/scheduler/WorkerOffer.scala
    288 ./scala/org/apache/spark/security/CryptoStreamUtils.scala
     38 ./scala/org/apache/spark/security/GroupMappingServiceProvider.scala
     56 ./scala/org/apache/spark/security/HadoopDelegationTokenProvider.scala
     24 ./scala/org/apache/spark/security/SecurityConfigurationLock.scala
     46 ./scala/org/apache/spark/security/ShellBasedGroupsMappingProvider.scala
    116 ./scala/org/apache/spark/security/SocketAuthHelper.scala
    148 ./scala/org/apache/spark/security/SocketAuthServer.scala
    403 ./scala/org/apache/spark/SecurityManager.scala
     48 ./scala/org/apache/spark/SerializableWritable.scala
    163 ./scala/org/apache/spark/serializer/GenericAvroSerializer.scala
    160 ./scala/org/apache/spark/serializer/JavaSerializer.scala
    633 ./scala/org/apache/spark/serializer/KryoSerializer.scala
     25 ./scala/org/apache/spark/serializer/package.scala
    423 ./scala/org/apache/spark/serializer/SerializationDebugger.scala
    200 ./scala/org/apache/spark/serializer/Serializer.scala
    214 ./scala/org/apache/spark/serializer/SerializerManager.scala
     28 ./scala/org/apache/spark/shuffle/BaseShuffleHandle.scala
    152 ./scala/org/apache/spark/shuffle/BlockStoreShuffleReader.scala
    279 ./scala/org/apache/spark/shuffle/DigestIndexShuffleBlockResolver.scala
     72 ./scala/org/apache/spark/shuffle/FetchFailedException.scala
    390 ./scala/org/apache/spark/shuffle/IndexShuffleBlockResolver.scala
     52 ./scala/org/apache/spark/shuffle/metrics.scala
     48 ./scala/org/apache/spark/shuffle/MigratableResolver.scala
     28 ./scala/org/apache/spark/shuffle/ShuffleBlockInfo.scala
     44 ./scala/org/apache/spark/shuffle/ShuffleBlockResolver.scala
     42 ./scala/org/apache/spark/shuffle/ShuffleDataIOUtils.scala
     28 ./scala/org/apache/spark/shuffle/ShuffleHandle.scala
     96 ./scala/org/apache/spark/shuffle/ShuffleManager.scala
    135 ./scala/org/apache/spark/shuffle/ShufflePartitionPairsWriter.scala
     33 ./scala/org/apache/spark/shuffle/ShuffleReader.scala
     74 ./scala/org/apache/spark/shuffle/ShuffleWriteProcessor.scala
     34 ./scala/org/apache/spark/shuffle/ShuffleWriter.scala
    280 ./scala/org/apache/spark/shuffle/sort/SortShuffleManager.scala
    108 ./scala/org/apache/spark/shuffle/sort/SortShuffleWriter.scala
    838 ./scala/org/apache/spark/SparkConf.scala
   3259 ./scala/org/apache/spark/SparkContext.scala
    524 ./scala/org/apache/spark/SparkEnv.scala
     52 ./scala/org/apache/spark/SparkException.scala
     39 ./scala/org/apache/spark/SparkFiles.scala
    123 ./scala/org/apache/spark/SparkStatusTracker.scala
    248 ./scala/org/apache/spark/SSLOptions.scala
    437 ./scala/org/apache/spark/status/api/v1/api.scala
    180 ./scala/org/apache/spark/status/api/v1/ApiRootResource.scala
     67 ./scala/org/apache/spark/status/api/v1/ApplicationListResource.scala
     90 ./scala/org/apache/spark/status/api/v1/JacksonMessageWriter.scala
    195 ./scala/org/apache/spark/status/api/v1/OneApplicationResource.scala
    122 ./scala/org/apache/spark/status/api/v1/PrometheusResource.scala
     48 ./scala/org/apache/spark/status/api/v1/SimpleDateParam.scala
    229 ./scala/org/apache/spark/status/api/v1/StagesResource.scala
     43 ./scala/org/apache/spark/status/AppHistoryServerPlugin.scala
   1385 ./scala/org/apache/spark/status/AppStatusListener.scala
     94 ./scala/org/apache/spark/status/AppStatusSource.scala
    595 ./scala/org/apache/spark/status/AppStatusStore.scala
     75 ./scala/org/apache/spark/status/AppStatusUtils.scala
    209 ./scala/org/apache/spark/status/ElementTrackingStore.scala
     86 ./scala/org/apache/spark/status/KVUtils.scala
    914 ./scala/org/apache/spark/status/LiveEntity.scala
    515 ./scala/org/apache/spark/status/storeTypes.scala
     46 ./scala/org/apache/spark/StatusAPIImpl.scala
    100 ./scala/org/apache/spark/StdLogMonitor.scala
     22 ./scala/org/apache/spark/storage/BlockException.scala
    167 ./scala/org/apache/spark/storage/BlockId.scala
    446 ./scala/org/apache/spark/storage/BlockInfoManager.scala
   2084 ./scala/org/apache/spark/storage/BlockManager.scala
    425 ./scala/org/apache/spark/storage/BlockManagerDecommissioner.scala
    150 ./scala/org/apache/spark/storage/BlockManagerId.scala
     70 ./scala/org/apache/spark/storage/BlockManagerManagedBuffer.scala
    292 ./scala/org/apache/spark/storage/BlockManagerMaster.scala
    881 ./scala/org/apache/spark/storage/BlockManagerMasterEndpoint.scala
     58 ./scala/org/apache/spark/storage/BlockManagerMasterHeartbeatEndpoint.scala
    150 ./scala/org/apache/spark/storage/BlockManagerMessages.scala
     64 ./scala/org/apache/spark/storage/BlockManagerSource.scala
    105 ./scala/org/apache/spark/storage/BlockManagerStorageEndpoint.scala
     20 ./scala/org/apache/spark/storage/BlockNotFoundException.scala
    222 ./scala/org/apache/spark/storage/BlockReplicationPolicy.scala
     21 ./scala/org/apache/spark/storage/BlockSavedOnDecommissionedBlockManagerException.scala
     45 ./scala/org/apache/spark/storage/BlockUpdatedInfo.scala
    192 ./scala/org/apache/spark/storage/DiskBlockManager.scala
    307 ./scala/org/apache/spark/storage/DiskBlockObjectWriter.scala
    350 ./scala/org/apache/spark/storage/DiskStore.scala
    174 ./scala/org/apache/spark/storage/FallbackStorage.scala
     32 ./scala/org/apache/spark/storage/FileSegment.scala
    916 ./scala/org/apache/spark/storage/memory/MemoryStore.scala
     73 ./scala/org/apache/spark/storage/RDDInfo.scala
   1134 ./scala/org/apache/spark/storage/ShuffleBlockFetcherIterator.scala
    243 ./scala/org/apache/spark/storage/StorageLevel.scala
    256 ./scala/org/apache/spark/storage/StorageUtils.scala
     86 ./scala/org/apache/spark/storage/TopologyMapper.scala
    248 ./scala/org/apache/spark/TaskContext.scala
    185 ./scala/org/apache/spark/TaskContextImpl.scala
    286 ./scala/org/apache/spark/TaskEndReason.scala
     29 ./scala/org/apache/spark/TaskKilledException.scala
     23 ./scala/org/apache/spark/TaskNotSerializableException.scala
     23 ./scala/org/apache/spark/TaskOutputFileAlreadyExistException.scala
     31 ./scala/org/apache/spark/TaskState.scala
    443 ./scala/org/apache/spark/TestUtils.scala
    127 ./scala/org/apache/spark/ui/ConsoleProgressBar.scala
    179 ./scala/org/apache/spark/ui/env/EnvironmentPage.scala
     59 ./scala/org/apache/spark/ui/exec/ExecutorsTab.scala
    108 ./scala/org/apache/spark/ui/exec/ExecutorThreadDumpPage.scala
    169 ./scala/org/apache/spark/ui/GraphUIData.scala
    134 ./scala/org/apache/spark/ui/HttpSecurityFilter.scala
    608 ./scala/org/apache/spark/ui/JettyUtils.scala
    575 ./scala/org/apache/spark/ui/jobs/AllJobsPage.scala
    160 ./scala/org/apache/spark/ui/jobs/AllStagesPage.scala
     38 ./scala/org/apache/spark/ui/jobs/JobDataUtil.scala
    479 ./scala/org/apache/spark/ui/jobs/JobPage.scala
     64 ./scala/org/apache/spark/ui/jobs/JobsTab.scala
     68 ./scala/org/apache/spark/ui/jobs/PoolPage.scala
     74 ./scala/org/apache/spark/ui/jobs/PoolTable.scala
    822 ./scala/org/apache/spark/ui/jobs/StagePage.scala
     66 ./scala/org/apache/spark/ui/jobs/StagesTab.scala
    391 ./scala/org/apache/spark/ui/jobs/StageTable.scala
     35 ./scala/org/apache/spark/ui/jobs/TaskDetailsClassNames.scala
    399 ./scala/org/apache/spark/ui/PagedTable.scala
    269 ./scala/org/apache/spark/ui/scope/RDDOperationGraph.scala
    186 ./scala/org/apache/spark/ui/SparkUI.scala
    270 ./scala/org/apache/spark/ui/storage/RDDPage.scala
    249 ./scala/org/apache/spark/ui/storage/StoragePage.scala
     29 ./scala/org/apache/spark/ui/storage/StorageTab.scala
     42 ./scala/org/apache/spark/ui/storage/ToolTips.scala
    102 ./scala/org/apache/spark/ui/ToolTips.scala
    689 ./scala/org/apache/spark/ui/UIUtils.scala
    124 ./scala/org/apache/spark/ui/UIWorkloadGenerator.scala
    243 ./scala/org/apache/spark/ui/WebUI.scala
    494 ./scala/org/apache/spark/util/AccumulatorV2.scala
     75 ./scala/org/apache/spark/util/ByteBufferInputStream.scala
     60 ./scala/org/apache/spark/util/ByteBufferOutputStream.scala
     36 ./scala/org/apache/spark/util/CausedBy.scala
    101 ./scala/org/apache/spark/util/Clock.scala
    876 ./scala/org/apache/spark/util/ClosureCleaner.scala
    301 ./scala/org/apache/spark/util/collection/AppendOnlyMap.scala
    241 ./scala/org/apache/spark/util/collection/BitSet.scala
    161 ./scala/org/apache/spark/util/collection/CompactBuffer.scala
    648 ./scala/org/apache/spark/util/collection/ExternalAppendOnlyMap.scala
    899 ./scala/org/apache/spark/util/collection/ExternalSorter.scala
     93 ./scala/org/apache/spark/util/collection/MedianHeap.scala
    165 ./scala/org/apache/spark/util/collection/OpenHashMap.scala
    328 ./scala/org/apache/spark/util/collection/OpenHashSet.scala
     28 ./scala/org/apache/spark/util/collection/PairsWriter.scala
     40 ./scala/org/apache/spark/util/collection/PartitionedAppendOnlyMap.scala
    101 ./scala/org/apache/spark/util/collection/PartitionedPairBuffer.scala
    133 ./scala/org/apache/spark/util/collection/PrimitiveKeyOpenHashMap.scala
     91 ./scala/org/apache/spark/util/collection/PrimitiveVector.scala
    105 ./scala/org/apache/spark/util/collection/SizeTracker.scala
     41 ./scala/org/apache/spark/util/collection/SizeTrackingAppendOnlyMap.scala
     39 ./scala/org/apache/spark/util/collection/SizeTrackingVector.scala
    112 ./scala/org/apache/spark/util/collection/SortDataFormat.scala
     39 ./scala/org/apache/spark/util/collection/Sorter.scala
    150 ./scala/org/apache/spark/util/collection/Spillable.scala
     39 ./scala/org/apache/spark/util/collection/Utils.scala
     96 ./scala/org/apache/spark/util/collection/WritablePartitionedPairCollection.scala
     47 ./scala/org/apache/spark/util/CollectionsUtils.scala
     46 ./scala/org/apache/spark/util/CommandLineUtils.scala
     50 ./scala/org/apache/spark/util/CompletionIterator.scala
     93 ./scala/org/apache/spark/util/Distribution.scala
    142 ./scala/org/apache/spark/util/EventLoop.scala
     77 ./scala/org/apache/spark/util/GenericOptionsParser.scala
    370 ./scala/org/apache/spark/util/HadoopFSUtils.scala
     31 ./scala/org/apache/spark/util/IdGenerator.scala
     31 ./scala/org/apache/spark/util/IntParam.scala
    284 ./scala/org/apache/spark/util/io/ChunkedByteBuffer.scala
     82 ./scala/org/apache/spark/util/io/ChunkedByteBufferFileRegion.scala
    123 ./scala/org/apache/spark/util/io/ChunkedByteBufferOutputStream.scala
   1287 ./scala/org/apache/spark/util/JsonProtocol.scala
     69 ./scala/org/apache/spark/util/KeyLock.scala
    163 ./scala/org/apache/spark/util/ListenerBus.scala
    215 ./scala/org/apache/spark/util/logging/DriverLogger.scala
    178 ./scala/org/apache/spark/util/logging/FileAppender.scala
    187 ./scala/org/apache/spark/util/logging/RollingFileAppender.scala
    139 ./scala/org/apache/spark/util/logging/RollingPolicy.scala
     71 ./scala/org/apache/spark/util/ManualClock.scala
     32 ./scala/org/apache/spark/util/MemoryParam.scala
     49 ./scala/org/apache/spark/util/MutablePair.scala
     90 ./scala/org/apache/spark/util/NextIterator.scala
     23 ./scala/org/apache/spark/util/package.scala
    192 ./scala/org/apache/spark/util/PeriodicCheckpointer.scala
     23 ./scala/org/apache/spark/util/random/package.scala
     30 ./scala/org/apache/spark/util/random/Pseudorandom.scala
    340 ./scala/org/apache/spark/util/random/RandomSampler.scala
    169 ./scala/org/apache/spark/util/random/SamplingUtils.scala
    332 ./scala/org/apache/spark/util/random/StratifiedSamplingUtils.scala
     67 ./scala/org/apache/spark/util/random/XORShiftRandom.scala
     78 ./scala/org/apache/spark/util/RpcUtils.scala
     69 ./scala/org/apache/spark/util/SecurityUtils.scala
     54 ./scala/org/apache/spark/util/SerializableBuffer.scala
     47 ./scala/org/apache/spark/util/SerializableConfiguration.scala
     41 ./scala/org/apache/spark/util/SerializableJobConf.scala
    216 ./scala/org/apache/spark/util/ShutdownHookManager.scala
    141 ./scala/org/apache/spark/util/SignalUtils.scala
    403 ./scala/org/apache/spark/util/SizeEstimator.scala
     32 ./scala/org/apache/spark/util/SparkExitCode.scala
     27 ./scala/org/apache/spark/util/SparkFatalException.scala
     77 ./scala/org/apache/spark/util/SparkUncaughtExceptionHandler.scala
    162 ./scala/org/apache/spark/util/StatCounter.scala
     70 ./scala/org/apache/spark/util/taskListeners.scala
    380 ./scala/org/apache/spark/util/ThreadUtils.scala
    103 ./scala/org/apache/spark/util/UninterruptibleThread.scala
     55 ./scala/org/apache/spark/util/UninterruptibleThreadRunner.scala
   3319 ./scala/org/apache/spark/util/Utils.scala
     66 ./scala/org/apache/spark/util/VersionUtils.scala
     75 ./scala-2.12/org/apache/spark/util/BoundedPriorityQueue.scala
    150 ./scala-2.12/org/apache/spark/util/TimeStampedHashMap.scala
     73 ./scala-2.13/org/apache/spark/util/BoundedPriorityQueue.scala
    143 ./scala-2.13/org/apache/spark/util/TimeStampedHashMap.scala
 122043 total


```

### core-java - 10771 total
```
    30 ./java/org/apache/spark/api/java/function/CoGroupFunction.java
    29 ./java/org/apache/spark/api/java/function/DoubleFlatMapFunction.java
    28 ./java/org/apache/spark/api/java/function/DoubleFunction.java
    30 ./java/org/apache/spark/api/java/function/FilterFunction.java
    29 ./java/org/apache/spark/api/java/function/FlatMapFunction.java
    29 ./java/org/apache/spark/api/java/function/FlatMapFunction2.java
    29 ./java/org/apache/spark/api/java/function/FlatMapGroupsFunction.java
    30 ./java/org/apache/spark/api/java/function/ForeachFunction.java
    29 ./java/org/apache/spark/api/java/function/ForeachPartitionFunction.java
    30 ./java/org/apache/spark/api/java/function/Function.java
    28 ./java/org/apache/spark/api/java/function/Function0.java
    28 ./java/org/apache/spark/api/java/function/Function2.java
    28 ./java/org/apache/spark/api/java/function/Function3.java
    28 ./java/org/apache/spark/api/java/function/Function4.java
    28 ./java/org/apache/spark/api/java/function/MapFunction.java
    29 ./java/org/apache/spark/api/java/function/MapGroupsFunction.java
    29 ./java/org/apache/spark/api/java/function/MapPartitionsFunction.java
    23 ./java/org/apache/spark/api/java/function/package-info.java
    32 ./java/org/apache/spark/api/java/function/PairFlatMapFunction.java
    31 ./java/org/apache/spark/api/java/function/PairFunction.java
    28 ./java/org/apache/spark/api/java/function/ReduceFunction.java
    28 ./java/org/apache/spark/api/java/function/VoidFunction.java
    28 ./java/org/apache/spark/api/java/function/VoidFunction2.java
    33 ./java/org/apache/spark/api/java/JavaFutureAction.java
   188 ./java/org/apache/spark/api/java/Optional.java
    56 ./java/org/apache/spark/api/java/StorageLevels.java
   111 ./java/org/apache/spark/api/plugin/DriverPlugin.java
    99 ./java/org/apache/spark/api/plugin/ExecutorPlugin.java
    89 ./java/org/apache/spark/api/plugin/PluginContext.java
    53 ./java/org/apache/spark/api/plugin/SparkPlugin.java
    63 ./java/org/apache/spark/api/resource/ResourceDiscoveryPlugin.java
   137 ./java/org/apache/spark/io/NioBufferedFileInputStream.java
   400 ./java/org/apache/spark/io/ReadAheadInputStream.java
    31 ./java/org/apache/spark/JobExecutionStatus.java
   161 ./java/org/apache/spark/memory/MemoryConsumer.java
    26 ./java/org/apache/spark/memory/MemoryMode.java
    36 ./java/org/apache/spark/memory/SparkOutOfMemoryError.java
   467 ./java/org/apache/spark/memory/TaskMemoryManager.java
    24 ./java/org/apache/spark/memory/TooLargePageException.java
    23 ./java/org/apache/spark/package-info.java
    92 ./java/org/apache/spark/serializer/DummySerializerInstance.java
    63 ./java/org/apache/spark/shuffle/api/metadata/MapOutputCommitMessage.java
    30 ./java/org/apache/spark/shuffle/api/metadata/MapOutputMetadata.java
    55 ./java/org/apache/spark/shuffle/api/ShuffleDataIO.java
    64 ./java/org/apache/spark/shuffle/api/ShuffleDriverComponents.java
    78 ./java/org/apache/spark/shuffle/api/ShuffleExecutorComponents.java
    81 ./java/org/apache/spark/shuffle/api/ShuffleMapOutputWriter.java
    98 ./java/org/apache/spark/shuffle/api/ShufflePartitionWriter.java
    36 ./java/org/apache/spark/shuffle/api/SingleSpillShuffleMapOutputWriter.java
    41 ./java/org/apache/spark/shuffle/api/WritableByteChannelWrapper.java
   320 ./java/org/apache/spark/shuffle/sort/BypassMergeSortShuffleWriter.java
    46 ./java/org/apache/spark/shuffle/sort/io/LocalDiskShuffleDataIO.java
    49 ./java/org/apache/spark/shuffle/sort/io/LocalDiskShuffleDriverComponents.java
    91 ./java/org/apache/spark/shuffle/sort/io/LocalDiskShuffleExecutorComponents.java
   279 ./java/org/apache/spark/shuffle/sort/io/LocalDiskShuffleMapOutputWriter.java
    55 ./java/org/apache/spark/shuffle/sort/io/LocalDiskSingleSpillMapOutputWriter.java
   102 ./java/org/apache/spark/shuffle/sort/PackedRecordPointer.java
   438 ./java/org/apache/spark/shuffle/sort/ShuffleExternalSorter.java
   203 ./java/org/apache/spark/shuffle/sort/ShuffleInMemorySorter.java
    78 ./java/org/apache/spark/shuffle/sort/ShuffleSortDataFormat.java
    37 ./java/org/apache/spark/shuffle/sort/SpillInfo.java
   547 ./java/org/apache/spark/shuffle/sort/UnsafeShuffleWriter.java
    37 ./java/org/apache/spark/SparkExecutorInfo.java
   222 ./java/org/apache/spark/SparkFirehoseListener.java
    32 ./java/org/apache/spark/SparkJobInfo.java
    37 ./java/org/apache/spark/SparkStageInfo.java
    30 ./java/org/apache/spark/status/api/v1/ApplicationStatus.java
    32 ./java/org/apache/spark/status/api/v1/StageStatus.java
    48 ./java/org/apache/spark/status/api/v1/TaskSorting.java
    32 ./java/org/apache/spark/status/api/v1/TaskStatus.java
    76 ./java/org/apache/spark/storage/TimeTrackingOutputStream.java
  1012 ./java/org/apache/spark/unsafe/map/BytesToBytesMap.java
    47 ./java/org/apache/spark/unsafe/map/HashMapGrowthStrategy.java
    68 ./java/org/apache/spark/util/ChildFirstURLClassLoader.java
   966 ./java/org/apache/spark/util/collection/TimSort.java
    29 ./java/org/apache/spark/util/collection/unsafe/sort/PrefixComparator.java
   174 ./java/org/apache/spark/util/collection/unsafe/sort/PrefixComparators.java
   261 ./java/org/apache/spark/util/collection/unsafe/sort/RadixSort.java
    39 ./java/org/apache/spark/util/collection/unsafe/sort/RecordComparator.java
    31 ./java/org/apache/spark/util/collection/unsafe/sort/RecordPointerAndKeyPrefix.java
   802 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeExternalSorter.java
   387 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeInMemorySorter.java
    92 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeSortDataFormat.java
    39 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeSorterIterator.java
   107 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeSorterSpillMerger.java
   156 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeSorterSpillReader.java
   165 ./java/org/apache/spark/util/collection/unsafe/sort/UnsafeSorterSpillWriter.java
    38 ./java/org/apache/spark/util/EnumUtil.java
    40 ./java/org/apache/spark/util/MutableURLClassLoader.java
    42 ./java/org/apache/spark/util/ParentClassLoader.java
    21 ./scala/org/apache/spark/api/java/package-info.java
    21 ./scala/org/apache/spark/broadcast/package-info.java
    21 ./scala/org/apache/spark/executor/package-info.java
    21 ./scala/org/apache/spark/io/package-info.java
    21 ./scala/org/apache/spark/rdd/package-info.java
    21 ./scala/org/apache/spark/scheduler/package-info.java
    21 ./scala/org/apache/spark/serializer/package-info.java
    21 ./scala/org/apache/spark/util/package-info.java
    21 ./scala/org/apache/spark/util/random/package-info.java
 10771 total


```





### yarn模块 - scala -  7415 total
```
 wc -l `find ./resource-managers/yarn/src/main -name '*.scala'`


   180 ./scala/org/apache/spark/deploy/yarn/AMCredentialRenewer.scala
  1085 ./scala/org/apache/spark/deploy/yarn/ApplicationMaster.scala
   108 ./scala/org/apache/spark/deploy/yarn/ApplicationMasterArguments.scala
    50 ./scala/org/apache/spark/deploy/yarn/ApplicationMasterSource.scala
  1803 ./scala/org/apache/spark/deploy/yarn/Client.scala
    86 ./scala/org/apache/spark/deploy/yarn/ClientArguments.scala
   186 ./scala/org/apache/spark/deploy/yarn/ClientDistributedCacheManager.scala
   441 ./scala/org/apache/spark/deploy/yarn/config.scala
   246 ./scala/org/apache/spark/deploy/yarn/ExecutorRunnable.scala
   229 ./scala/org/apache/spark/deploy/yarn/LocalityPreferredContainerPlacementStrategy.scala
   251 ./scala/org/apache/spark/deploy/yarn/ResourceRequestHelper.scala
   119 ./scala/org/apache/spark/deploy/yarn/SparkRackResolver.scala
   973 ./scala/org/apache/spark/deploy/yarn/YarnAllocator.scala
   203 ./scala/org/apache/spark/deploy/yarn/YarnAllocatorNodeHealthTracker.scala
    81 ./scala/org/apache/spark/deploy/yarn/YarnProxyRedirectFilter.scala
   159 ./scala/org/apache/spark/deploy/yarn/YarnRMClient.scala
   227 ./scala/org/apache/spark/deploy/yarn/YarnSparkHadoopUtil.scala
    85 ./scala/org/apache/spark/executor/YarnCoarseGrainedExecutorBackend.scala
    39 ./scala/org/apache/spark/launcher/YarnCommandBuilderUtils.scala
   178 ./scala/org/apache/spark/scheduler/cluster/YarnClientSchedulerBackend.scala
    56 ./scala/org/apache/spark/scheduler/cluster/YarnClusterManager.scala
    38 ./scala/org/apache/spark/scheduler/cluster/YarnClusterScheduler.scala
    45 ./scala/org/apache/spark/scheduler/cluster/YarnClusterSchedulerBackend.scala
    39 ./scala/org/apache/spark/scheduler/cluster/YarnScheduler.scala
   385 ./scala/org/apache/spark/scheduler/cluster/YarnSchedulerBackend.scala
   123 ./scala/org/apache/spark/util/YarnContainerInfoHelper.scala
  7415 total


```






### sql模块 - scala -  116995 total
```
 wc -l `find ./sql/core/src/main/ -name '*.scala'`


     23 ./sql/core/src/main/scala/org/apache/spark/sql/api/package.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/api/python/PythonSQLUtils.scala
    252 ./sql/core/src/main/scala/org/apache/spark/sql/api/r/SQLUtils.scala
    592 ./sql/core/src/main/scala/org/apache/spark/sql/catalog/Catalog.scala
    147 ./sql/core/src/main/scala/org/apache/spark/sql/catalog/interface.scala
    191 ./sql/core/src/main/scala/org/apache/spark/sql/catalyst/analysis/CreateViewAnalysis.scala
    769 ./sql/core/src/main/scala/org/apache/spark/sql/catalyst/analysis/ResolveSessionCatalog.scala
   1497 ./sql/core/src/main/scala/org/apache/spark/sql/Column.scala
    343 ./sql/core/src/main/scala/org/apache/spark/sql/columnar/CachedBatchSerializer.scala
    535 ./sql/core/src/main/scala/org/apache/spark/sql/DataFrameNaFunctions.scala
   1026 ./sql/core/src/main/scala/org/apache/spark/sql/DataFrameReader.scala
    609 ./sql/core/src/main/scala/org/apache/spark/sql/DataFrameStatFunctions.scala
   1017 ./sql/core/src/main/scala/org/apache/spark/sql/DataFrameWriter.scala
    345 ./sql/core/src/main/scala/org/apache/spark/sql/DataFrameWriterV2.scala
   3761 ./sql/core/src/main/scala/org/apache/spark/sql/Dataset.scala
     45 ./sql/core/src/main/scala/org/apache/spark/sql/DatasetHolder.scala
    730 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/AdaptiveSparkPlanExec.scala
    138 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/AdaptiveSparkPlanHelper.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/AQEOptimizer.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/CoalesceShufflePartitions.scala
     32 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/costing.scala
    198 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/CustomShuffleReaderExec.scala
     33 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/CustomShuffleReaderRule.scala
     57 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/DemoteBroadcastHashJoin.scala
     57 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/EliminateJoinToEmptyRelation.scala
    153 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/InsertAdaptiveSparkPlan.scala
     55 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/LogicalQueryStage.scala
     68 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/LogicalQueryStageStrategy.scala
    159 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/OptimizeLocalShuffleReader.scala
    330 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/OptimizeSkewedJoin.scala
     45 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/PlanAdaptiveSubqueries.scala
    250 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/QueryStageExec.scala
     43 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/ReuseAdaptiveSubquery.scala
    173 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/ShufflePartitionsUtil.scala
     48 ./sql/core/src/main/scala/org/apache/spark/sql/execution/adaptive/simpleCosting.scala
    306 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/AggregationIterator.scala
    367 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/AggUtils.scala
     98 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/BaseAggregateExec.scala
   1117 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/HashAggregateExec.scala
    178 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/HashMapGenerator.scala
    321 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/ObjectAggregationIterator.scala
    108 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/ObjectAggregationMap.scala
    144 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/ObjectHashAggregateExec.scala
    194 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/RowBasedHashMapGenerator.scala
    105 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/SortAggregateExec.scala
    166 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/SortBasedAggregationIterator.scala
    463 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/TungstenAggregationIterator.scala
    288 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/TypedAggregateExpression.scala
    101 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/typedaggregators.scala
    532 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/udaf.scala
    219 ./sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/VectorizedHashMapGenerator.scala
    275 ./sql/core/src/main/scala/org/apache/spark/sql/execution/AggregatingAccumulator.scala
     73 ./sql/core/src/main/scala/org/apache/spark/sql/execution/AliasAwareOutputExpression.scala
    177 ./sql/core/src/main/scala/org/apache/spark/sql/execution/analysis/DetectAmbiguousSelfJoin.scala
    284 ./sql/core/src/main/scala/org/apache/spark/sql/execution/arrow/ArrowConverters.scala
    387 ./sql/core/src/main/scala/org/apache/spark/sql/execution/arrow/ArrowWriter.scala
    366 ./sql/core/src/main/scala/org/apache/spark/sql/execution/BaseScriptTransformationExec.scala
    862 ./sql/core/src/main/scala/org/apache/spark/sql/execution/basicPhysicalOperators.scala
    176 ./sql/core/src/main/scala/org/apache/spark/sql/execution/bucketing/CoalesceBucketsInJoin.scala
    162 ./sql/core/src/main/scala/org/apache/spark/sql/execution/bucketing/DisableUnnecessaryBucketedScan.scala
    309 ./sql/core/src/main/scala/org/apache/spark/sql/execution/CacheManager.scala
     91 ./sql/core/src/main/scala/org/apache/spark/sql/execution/CoGroupedIterator.scala
     93 ./sql/core/src/main/scala/org/apache/spark/sql/execution/CollectMetricsExec.scala
    176 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/ColumnAccessor.scala
    198 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/ColumnBuilder.scala
    354 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/ColumnStats.scala
    771 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/ColumnType.scala
     43 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/compression/CompressibleColumnAccessor.scala
    114 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/compression/CompressibleColumnBuilder.scala
     84 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/compression/CompressionScheme.scala
    857 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/compression/compressionSchemes.scala
    236 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/GenerateColumnAccessor.scala
    413 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/InMemoryRelation.scala
    161 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/InMemoryTableScanExec.scala
     59 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/NullableColumnAccessor.scala
     88 ./sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/NullableColumnBuilder.scala
    538 ./sql/core/src/main/scala/org/apache/spark/sql/execution/Columnar.scala
    149 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/AnalyzeColumnCommand.scala
    156 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/AnalyzePartitionCommand.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/AnalyzeTableCommand.scala
    119 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/cache.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/CommandCheck.scala
    203 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/commands.scala
    397 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/CommandUtils.scala
    227 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/createDataSourceTables.scala
     99 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/DataWritingCommand.scala
    951 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/ddl.scala
    290 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/functions.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/InsertIntoDataSourceDirCommand.scala
    102 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/resources.scala
    190 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/SetCommand.scala
   1404 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/tables.scala
    638 ./sql/core/src/main/scala/org/apache/spark/sql/execution/command/views.scala
     49 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/AsyncClosedRecordReaderIterator.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/AsyncFileScanRDD.scala
    183 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/BasicWriteStatsTracker.scala
    198 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/binaryfile/BinaryFileFormat.scala
     53 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/BucketingUtils.scala
    110 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/CatalogFileIndex.scala
    101 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/CodecStreams.scala
    245 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/csv/CSVDataSource.scala
    167 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/csv/CSVFileFormat.scala
     49 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/csv/CsvOutputWriter.scala
    133 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/csv/CSVUtils.scala
    865 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/DataSource.scala
    796 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/DataSourceStrategy.scala
    270 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/DataSourceUtils.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/DaysWritable.scala
    113 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/ddl.scala
     49 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FallBackFileSourceV2.scala
    184 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileFormat.scala
    338 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileFormatDataWriter.scala
    326 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileFormatWriter.scala
     85 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileIndex.scala
     98 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FilePartition.scala
    258 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileScanRDD.scala
    240 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileSourceStrategy.scala
    181 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/FileStatusCache.scala
     74 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/HadoopFileLinesReader.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/HadoopFileWholeTextReader.scala
     77 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/HadoopFsRelation.scala
    167 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/InMemoryFileIndex.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/InsertIntoDataSourceCommand.scala
    357 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/InsertIntoHadoopFsRelationCommand.scala
    215 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/InsertOptimizer.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/BasicConnectionProvider.scala
     75 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/ConnectionProvider.scala
     55 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/DB2ConnectionProvider.scala
     30 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/MariaDBConnectionProvider.scala
     82 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/MSSQLConnectionProvider.scala
     56 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/OracleConnectionProvider.scala
     35 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/PostgresConnectionProvider.scala
     91 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/connection/SecureConnectionProvider.scala
     73 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/DriverRegistry.scala
     48 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/DriverWrapper.scala
    269 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/JDBCOptions.scala
    358 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/JDBCRDD.scala
    289 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/JDBCRelation.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/JdbcRelationProvider.scala
   1568 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/jdbc/JdbcUtils.scala
    232 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/json/JsonDataSource.scala
    160 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/json/JsonFileFormat.scala
     61 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/json/JsonOutputWriter.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/json/JsonUtils.scala
     85 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/LogicalRelation.scala
     93 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/noop/NoopDataSource.scala
    249 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcDeserializer.scala
    281 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcFileFormat.scala
    276 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcFilters.scala
     88 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcFiltersBase.scala
     83 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcOptions.scala
     60 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcOutputWriter.scala
    218 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcSerializer.scala
     67 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcShimUtils.scala
    254 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcUtils.scala
     70 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/OutputWriter.scala
     55 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetColumn.scala
    545 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetFileFormat.scala
    782 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetFilters.scala
    117 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetOptions.scala
     42 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetOutputWriter.scala
    539 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetReadSupport.scala
     62 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetRecordMaterializer.scala
    847 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetRowConverter.scala
    729 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetSchemaConverter.scala
    197 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetUtils.scala
    491 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/parquet/ParquetWriteSupport.scala
    252 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/PartitioningAwareFileIndex.scala
    625 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/PartitioningUtils.scala
    161 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/pathFilters.scala
    130 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/PruneFileSourcePartitions.scala
     66 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/RecordReaderIterator.scala
    550 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/rules.scala
     61 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/SaveIntoDataSourceCommand.scala
    108 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/SchemaMergeUtils.scala
    204 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/SchemaPruning.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/SourceOptions.scala
     70 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/SQLHadoopMapReduceCommitProtocol.scala
    143 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/text/TextFileFormat.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/text/TextOptions.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/text/TextOutputWriter.scala
    375 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/thive/rules.scala
     40 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AlterNamespaceSetPropertiesExec.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AlterTableAddPartitionExec.scala
     57 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AlterTableDropPartitionExec.scala
     45 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AlterTableExec.scala
     47 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AlterViewExec.scala
     92 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AsyncDataSourceRDD.scala
    128 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/AsyncPartitionReaderStream.scala
    125 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/BatchScanExec.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/CatalystRowHelper.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ContinuousScanExec.scala
     59 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/CreateNamespaceExec.scala
     54 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/CreateTableExec.scala
     89 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/CreateViewExec.scala
     45 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVDataSourceV2.scala
     76 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVPartitionReaderFactory.scala
    114 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVScan.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVScanBuilder.scala
     64 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVTable.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/csv/CSVWriteBuilder.scala
     56 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DataSourcePartitioning.scala
    137 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DataSourceRDD.scala
    113 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DataSourceV2ScanExecBase.scala
    409 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DataSourceV2Strategy.scala
     86 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DataSourceV2Utils.scala
     37 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DeleteFromTableExec.scala
     64 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DescribeNamespaceExec.scala
    106 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DescribeTableExec.scala
     59 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DescribeViewExec.scala
     72 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DistributionAndOrderingUtils.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DropNamespaceExec.scala
     47 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DropTableExec.scala
     44 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/DropViewExec.scala
     34 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/EmptyPartitionReader.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileBatchWrite.scala
    114 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileDataSourceV2.scala
    116 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FilePartitionReader.scala
     61 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FilePartitionReaderFactory.scala
    216 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileScan.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileScanBuilder.scala
    154 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileTable.scala
    143 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileWriteBuilder.scala
     56 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/FileWriterFactory.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/jdbc/JDBCScan.scala
     70 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/jdbc/JDBCScanBuilder.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/jdbc/JDBCTable.scala
    331 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/jdbc/JDBCTableCatalog.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/jdbc/JDBCWriteBuilder.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonDataSourceV2.scala
     68 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonPartitionReaderFactory.scala
    109 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonScan.scala
     56 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonScanBuilder.scala
     73 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonTable.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/json/JsonWriteBuilder.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/MicroBatchScanExec.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcDataSourceV2.scala
    175 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcPartitionReaderFactory.scala
     75 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcScan.scala
     63 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcScanBuilder.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcTable.scala
     72 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/orc/OrcWriteBuilder.scala
     47 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetDataSourceV2.scala
    258 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetPartitionReaderFactory.scala
    112 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetScan.scala
     91 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetScanBuilder.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetTable.scala
    119 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/parquet/ParquetWriteBuilder.scala
     37 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/PartitionReaderFromIterator.scala
     53 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/PartitionReaderWithPartitionValues.scala
     31 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/PartitionRecordReader.scala
    122 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/PushDownUtils.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/RefreshTableExec.scala
     57 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/RenameTableExec.scala
     39 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/RenameViewExec.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ReplaceTableExec.scala
     42 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/SetCatalogAndNamespaceExec.scala
     35 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowCreateViewExec.scala
     41 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowCurrentNamespaceExec.scala
     57 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowNamespacesExec.scala
     66 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowPartitionsExec.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowTablePropertiesExec.scala
     54 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowTablesExec.scala
     44 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/ShowViewPropertiesExec.scala
    103 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/TableCapabilityCheck.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextDataSourceV2.scala
     73 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextPartitionReaderFactory.scala
     85 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextScan.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextScanBuilder.scala
     48 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextTable.scala
     70 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/text/TextWriteBuilder.scala
     40 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/TextBasedFileScan.scala
    127 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/V1FallbackWriters.scala
     62 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/V2CommandExec.scala
     98 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/V2ScanRelationPushDown.scala
    334 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/V2SessionCatalog.scala
    509 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/v2/WriteToDataSourceV2Exec.scala
    121 ./sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/WriteStatsTracker.scala
    651 ./sql/core/src/main/scala/org/apache/spark/sql/execution/DataSourceScanExec.scala
    292 ./sql/core/src/main/scala/org/apache/spark/sql/execution/debug/package.scala
     53 ./sql/core/src/main/scala/org/apache/spark/sql/execution/dynamicpruning/CleanupDynamicPruningFilters.scala
    247 ./sql/core/src/main/scala/org/apache/spark/sql/execution/dynamicpruning/PartitionPruning.scala
     91 ./sql/core/src/main/scala/org/apache/spark/sql/execution/dynamicpruning/PlanDynamicPruningFilters.scala
    221 ./sql/core/src/main/scala/org/apache/spark/sql/execution/exchange/BroadcastExchangeExec.scala
    260 ./sql/core/src/main/scala/org/apache/spark/sql/execution/exchange/EnsureRequirements.scala
    139 ./sql/core/src/main/scala/org/apache/spark/sql/execution/exchange/Exchange.scala
    402 ./sql/core/src/main/scala/org/apache/spark/sql/execution/exchange/ShuffleExchangeExec.scala
    166 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ExistingRDD.scala
    207 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ExpandExec.scala
     72 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ExplainMode.scala
    257 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ExplainUtils.scala
    227 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ExternalAppendOnlyUnsafeRowArray.scala
     28 ./sql/core/src/main/scala/org/apache/spark/sql/execution/FileRelation.scala
    176 ./sql/core/src/main/scala/org/apache/spark/sql/execution/fusion/FusionUnionExec.scala
    331 ./sql/core/src/main/scala/org/apache/spark/sql/execution/GenerateExec.scala
    167 ./sql/core/src/main/scala/org/apache/spark/sql/execution/GroupedIterator.scala
    147 ./sql/core/src/main/scala/org/apache/spark/sql/execution/history/SQLEventFilterBuilder.scala
    122 ./sql/core/src/main/scala/org/apache/spark/sql/execution/HiveResult.scala
    141 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/AsyncPartitionedFileReadStream.scala
     36 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/ExecutorIOManager.scala
     69 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/IOMemoryHelper.scala
     48 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/IOMemoryManager.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/IOMetrics.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/io/IOMetricsTaskHandler.scala
     56 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/BaseJoinExec.scala
    257 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/BroadcastHashJoinExec.scala
    385 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/BroadcastNestedLoopJoinExec.scala
    106 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/CartesianProductExec.scala
   1150 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/HashedRelation.scala
    812 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/HashJoin.scala
    323 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/ShuffledHashJoinExec.scala
     64 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/ShuffledJoin.scala
   1213 ./sql/core/src/main/scala/org/apache/spark/sql/execution/joins/SortMergeJoinExec.scala
    240 ./sql/core/src/main/scala/org/apache/spark/sql/execution/limit.scala
     94 ./sql/core/src/main/scala/org/apache/spark/sql/execution/LocalTableScanExec.scala
     30 ./sql/core/src/main/scala/org/apache/spark/sql/execution/metric/SQLMetricInfo.scala
    248 ./sql/core/src/main/scala/org/apache/spark/sql/execution/metric/SQLMetrics.scala
    152 ./sql/core/src/main/scala/org/apache/spark/sql/execution/metric/SQLShuffleMetricsReporter.scala
    626 ./sql/core/src/main/scala/org/apache/spark/sql/execution/objects.scala
    182 ./sql/core/src/main/scala/org/apache/spark/sql/execution/OptimizeMetadataOnlyQuery.scala
     25 ./sql/core/src/main/scala/org/apache/spark/sql/execution/package.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/execution/PartitionedFileUtil.scala
    157 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/AggregateInPandasExec.scala
     97 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/ArrowEvalPythonExec.scala
    121 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/ArrowPythonRunner.scala
    106 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/BatchEvalPythonExec.scala
    117 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/CoGroupedArrowPythonRunner.scala
    140 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/EvalPythonExec.scala
    306 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/EvaluatePython.scala
    300 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/ExtractPythonUDFs.scala
    106 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/FlatMapCoGroupsInPandasExec.scala
     97 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/FlatMapGroupsInPandasExec.scala
     96 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/MapInPandasExec.scala
    123 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PandasGroupUtils.scala
    109 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PythonArrowOutput.scala
    158 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PythonForeachWriter.scala
    115 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PythonUDAF.scala
    201 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PythonUDAFRunner.scala
    114 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/PythonUDFRunner.scala
    294 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/RowQueue.scala
     36 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/UserDefinedPythonAggregateFunction.scala
     44 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/UserDefinedPythonFunction.scala
    404 ./sql/core/src/main/scala/org/apache/spark/sql/execution/python/WindowInPandasExec.scala
    409 ./sql/core/src/main/scala/org/apache/spark/sql/execution/QueryExecution.scala
     21 ./sql/core/src/main/scala/org/apache/spark/sql/execution/QueryExecutionException.scala
    197 ./sql/core/src/main/scala/org/apache/spark/sql/execution/r/ArrowRRunner.scala
     66 ./sql/core/src/main/scala/org/apache/spark/sql/execution/r/MapPartitionsRWrapper.scala
    113 ./sql/core/src/main/scala/org/apache/spark/sql/execution/RemoveRedundantProjects.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/execution/RemoveRedundantSorts.scala
    222 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ShuffledRowRDD.scala
    205 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SortExec.scala
    168 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SortPrefixUtils.scala
    100 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkOptimizer.scala
    594 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkPlan.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkPlanInfo.scala
    109 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkPlanner.scala
    668 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkSqlParser.scala
    755 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SparkStrategies.scala
    205 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SQLExecution.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SQLExecutionRDD.scala
    126 ./sql/core/src/main/scala/org/apache/spark/sql/execution/stat/FrequentItems.scala
    299 ./sql/core/src/main/scala/org/apache/spark/sql/execution/stat/StatFunctions.scala
    367 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/CheckpointFileManager.scala
     88 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/CommitLog.scala
    398 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/CompactibleFileStreamLog.scala
     88 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/console.scala
    108 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousDataSourceRDD.scala
    438 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousExecution.scala
    208 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousQueuedDataReader.scala
    161 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousRateStreamSource.scala
     26 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousTaskRetryException.scala
    291 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousTextSocketSource.scala
     95 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/ContinuousWriteRDD.scala
    270 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/EpochCoordinator.scala
     65 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/EpochTracker.scala
     31 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/WriteToContinuousDataSource.scala
     73 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/continuous/WriteToContinuousDataSourceExec.scala
     71 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/ContinuousRecordEndpoint.scala
    128 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/EventTimeWatermarkExec.scala
    136 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamOptions.scala
    188 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamSink.scala
    127 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamSinkLog.scala
    577 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamSource.scala
    152 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamSourceLog.scala
     54 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FileStreamSourceOffset.scala
    249 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/FlatMapGroupsWithStateExec.scala
    208 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/GroupStateImpl.scala
    330 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/HDFSMetadataLog.scala
    199 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/IncrementalExecution.scala
     38 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/LongOffset.scala
    156 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/ManifestFileCommitProtocol.scala
    299 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/memory.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/MetadataLog.scala
     74 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/MetadataLogFileIndex.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/MetadataVersionUtil.scala
     72 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/MetricsReporter.scala
    626 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/MicroBatchExecution.scala
    169 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/OffsetSeq.scala
     92 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/OffsetSeqLog.scala
    375 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/ProgressReporter.scala
     32 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/RateStreamOffset.scala
     29 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/SerializedOffset.scala
     60 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/Sink.scala
     80 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/Source.scala
     72 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/ConsoleWrite.scala
    187 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/ContinuousMemoryStream.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/ForeachBatchSink.scala
    166 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/ForeachWriterTable.scala
    201 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/memory.scala
     50 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/MicroBatchWrite.scala
     68 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/PackedRowWriterFactory.scala
    198 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/RateStreamMicroBatchStream.scala
    141 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/RateStreamProvider.scala
    182 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/TextSocketMicroBatchStream.scala
    106 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/TextSocketSourceProvider.scala
     39 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/sources/WriteToMicroBatchDataSource.scala
    247 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/FlatMapGroupsWithStateExecHelper.scala
    753 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/HDFSBackedStateStoreProvider.scala
    121 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/package.scala
    118 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StateSchemaCompatibilityChecker.scala
    621 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StateStore.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StateStoreConf.scala
    158 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StateStoreCoordinator.scala
    129 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StateStoreRDD.scala
    205 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/StreamingAggregationStateManager.scala
    682 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/SymmetricHashJoinStateManager.scala
    518 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/statefulOperators.scala
    692 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamExecution.scala
    136 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/streamingLimits.scala
    148 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamingQueryListenerBus.scala
    107 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamingQueryWrapper.scala
     99 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamingRelation.scala
    623 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamingSymmetricHashJoinExec.scala
    263 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamingSymmetricHashJoinHelper.scala
     97 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/StreamMetadata.scala
     90 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/TriggerExecutor.scala
    109 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/Triggers.scala
    138 ./sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/WatermarkTracker.scala
    224 ./sql/core/src/main/scala/org/apache/spark/sql/execution/subquery.scala
    121 ./sql/core/src/main/scala/org/apache/spark/sql/execution/SubqueryBroadcastExec.scala
    419 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/AllExecutionsPage.scala
    148 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/ExecutionPage.scala
    235 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SparkPlanGraph.scala
    570 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SQLAppStatusListener.scala
    149 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SQLAppStatusStore.scala
     39 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SQLHistoryServerPlugin.scala
    115 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SQLListener.scala
     37 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/SQLTab.scala
     43 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/StreamingQueryHistoryServerPlugin.scala
     53 ./sql/core/src/main/scala/org/apache/spark/sql/execution/ui/StreamingQueryStatusStore.scala
    184 ./sql/core/src/main/scala/org/apache/spark/sql/execution/UnsafeRowSerializer.scala
    947 ./sql/core/src/main/scala/org/apache/spark/sql/execution/WholeStageCodegenExec.scala
    161 ./sql/core/src/main/scala/org/apache/spark/sql/execution/window/AggregateProcessor.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/execution/window/BoundOrdering.scala
    214 ./sql/core/src/main/scala/org/apache/spark/sql/execution/window/WindowExec.scala
    267 ./sql/core/src/main/scala/org/apache/spark/sql/execution/window/WindowExecBase.scala
    550 ./sql/core/src/main/scala/org/apache/spark/sql/execution/window/WindowFunctionFrame.scala
     55 ./sql/core/src/main/scala/org/apache/spark/sql/ExperimentalMethods.scala
    109 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/Aggregator.scala
     68 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/ReduceAggregator.scala
     74 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/scalalang/typed.scala
    171 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/udaf.scala
    175 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/UserDefinedFunction.scala
    238 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/Window.scala
    219 ./sql/core/src/main/scala/org/apache/spark/sql/expressions/WindowSpec.scala
    136 ./sql/core/src/main/scala/org/apache/spark/sql/ForeachWriter.scala
   5086 ./sql/core/src/main/scala/org/apache/spark/sql/functions.scala
    463 ./sql/core/src/main/scala/org/apache/spark/sql/fusion/GroupBySubqueryFusion.scala
    114 ./sql/core/src/main/scala/org/apache/spark/sql/fusion/UnionSubQueryFusion.scala
    386 ./sql/core/src/main/scala/org/apache/spark/sql/internal/BaseSessionStateBuilder.scala
    595 ./sql/core/src/main/scala/org/apache/spark/sql/internal/CatalogImpl.scala
    139 ./sql/core/src/main/scala/org/apache/spark/sql/internal/HiveSerDe.scala
     24 ./sql/core/src/main/scala/org/apache/spark/sql/internal/package.scala
    227 ./sql/core/src/main/scala/org/apache/spark/sql/internal/SessionState.scala
    275 ./sql/core/src/main/scala/org/apache/spark/sql/internal/SharedState.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/internal/VariableSubstitution.scala
     79 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/AggregatedDialect.scala
     82 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/DB2Dialect.scala
     59 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/DerbyDialect.scala
     48 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/H2Dialect.scala
     33 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/HiveQLDialect.scala
     64 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/JdbcConnectionProvider.scala
    371 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/JdbcDialects.scala
    121 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/MsSqlServerDialect.scala
     97 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/MySQLDialect.scala
    143 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/OracleDialect.scala
    145 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/PostgresDialect.scala
     58 ./sql/core/src/main/scala/org/apache/spark/sql/jdbc/TeradataDialect.scala
    632 ./sql/core/src/main/scala/org/apache/spark/sql/KeyValueGroupedDataset.scala
     69 ./sql/core/src/main/scala/org/apache/spark/sql/package.scala
    147 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/Authorizer.scala
     33 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/BaseRangerRequest.scala
     27 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/Constants.scala
     27 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/RangerDatasourceExtension.scala
     87 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/RangerDatasourceRules.scala
     52 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/RelationRequest.scala
     51 ./sql/core/src/main/scala/org/apache/spark/sql/ranger/URLRequest.scala
    654 ./sql/core/src/main/scala/org/apache/spark/sql/RelationalGroupedDataset.scala
    159 ./sql/core/src/main/scala/org/apache/spark/sql/RuntimeConfig.scala
    311 ./sql/core/src/main/scala/org/apache/spark/sql/sources/interfaces.scala
     22 ./sql/core/src/main/scala/org/apache/spark/sql/sources/package.scala
   1241 ./sql/core/src/main/scala/org/apache/spark/sql/SparkSession.scala
    269 ./sql/core/src/main/scala/org/apache/spark/sql/SparkSessionExtensions.scala
   1095 ./sql/core/src/main/scala/org/apache/spark/sql/SQLContext.scala
    253 ./sql/core/src/main/scala/org/apache/spark/sql/SQLImplicits.scala
    614 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/DataStreamReader.scala
    596 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/DataStreamWriter.scala
    325 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/GroupState.scala
    257 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/progress.scala
    172 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/StreamingQuery.scala
     46 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/StreamingQueryException.scala
    117 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/StreamingQueryListener.scala
    450 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/StreamingQueryManager.scala
     68 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/StreamingQueryStatus.scala
    267 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/ui/StreamingQueryPage.scala
    537 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/ui/StreamingQueryStatisticsPage.scala
    163 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/ui/StreamingQueryStatusListener.scala
     40 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/ui/StreamingQueryTab.scala
     76 ./sql/core/src/main/scala/org/apache/spark/sql/streaming/ui/UIUtils.scala
     67 ./sql/core/src/main/scala/org/apache/spark/sql/test/ExamplePointUDT.scala
   1163 ./sql/core/src/main/scala/org/apache/spark/sql/UDFRegistration.scala
    175 ./sql/core/src/main/scala/org/apache/spark/sql/util/QueryExecutionListener.scala
     42 ./sql/core/src/main/scala/org/apache/spark/status/api/v1/sql/api.scala
     34 ./sql/core/src/main/scala/org/apache/spark/status/api/v1/sql/ApiSqlRootResource.scala
    157 ./sql/core/src/main/scala/org/apache/spark/status/api/v1/sql/SqlResource.scala
     54 ./sql/core/src/main/scala-2.12/org/apache/spark/sql/execution/streaming/StreamProgress.scala
     53 ./sql/core/src/main/scala-2.13/org/apache/spark/sql/execution/streaming/StreamProgress.scala
 116995 total

```

### sql模块 - java -   11075 total

```
 wc -l `find ./sql/core/src/main/ -name '*.java'`


57 ./sql/core/src/main/java/org/apache/parquet/filter2/predicate/SparkFilterApi.java
    40 ./sql/core/src/main/java/org/apache/parquet/io/ColumnIOUtil.java
    39 ./sql/core/src/main/java/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.java
    38 ./sql/core/src/main/java/org/apache/spark/api/java/function/MapGroupsWithStateFunction.java
    21 ./sql/core/src/main/java/org/apache/spark/sql/api/java/package-info.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF0.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF1.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF10.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF11.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF12.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF13.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF14.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF15.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF16.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF17.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF18.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF19.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF2.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF20.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF21.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF22.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF3.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF4.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF5.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF6.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF7.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF8.java
    30 ./sql/core/src/main/java/org/apache/spark/sql/api/java/UDF9.java
    43 ./sql/core/src/main/java/org/apache/spark/sql/connector/read/V1Scan.java
    45 ./sql/core/src/main/java/org/apache/spark/sql/connector/write/V1WriteBuilder.java
    98 ./sql/core/src/main/java/org/apache/spark/sql/execution/BufferedRowIterator.java
    58 ./sql/core/src/main/java/org/apache/spark/sql/execution/columnar/ColumnDictionary.java
   216 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/orc/AsyncOrcColumnarBatchReader.java
   210 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/orc/OrcColumnarBatchReader.java
   208 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/orc/OrcColumnVector.java
    36 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/orc/OrcReaderBuffer.java
   402 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetColumnVector.java
    76 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetDictionary.java
    56 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetFooterReader.java
    72 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetLogRedirector.java
   189 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetReadState.java
    94 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetVectorUpdater.java
  1121 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetVectorUpdaterFactory.java
   286 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/SpecificParquetRecordReaderBase.java
   363 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedColumnReader.java
    77 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedIcebergParquetBuilder.java
   393 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedIcebergParquetRecordReader.java
    49 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedIcebergPositionColumnReader.java
   405 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedParquetRecordReader.java
   394 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedPlainValuesReader.java
   937 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedRleValuesReader.java
    66 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/VectorizedValuesReader.java
    62 ./sql/core/src/main/java/org/apache/spark/sql/execution/datasources/SchemaColumnConvertNotSupportedException.java
    33 ./sql/core/src/main/java/org/apache/spark/sql/execution/io/IOBuffer.java
    51 ./sql/core/src/main/java/org/apache/spark/sql/execution/io/IOManager.java
    25 ./sql/core/src/main/java/org/apache/spark/sql/execution/io/IOStream.java
   136 ./sql/core/src/main/java/org/apache/spark/sql/execution/io/IOTask.java
    86 ./sql/core/src/main/java/org/apache/spark/sql/execution/RecordBinaryComparator.java
    27 ./sql/core/src/main/java/org/apache/spark/sql/execution/streaming/Offset.java
   257 ./sql/core/src/main/java/org/apache/spark/sql/execution/UnsafeExternalRowSorter.java
   252 ./sql/core/src/main/java/org/apache/spark/sql/execution/UnsafeFixedWidthAggregationMap.java
   331 ./sql/core/src/main/java/org/apache/spark/sql/execution/UnsafeKVExternalSorter.java
   112 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/AggregateHashMap.java
   236 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/ColumnVectorUtils.java
    34 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/Dictionary.java
   281 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/MutableColumnarRow.java
   584 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/OffHeapColumnVector.java
   598 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/OnHeapColumnVector.java
   845 ./sql/core/src/main/java/org/apache/spark/sql/execution/vectorized/WritableColumnVector.java
    74 ./sql/core/src/main/java/org/apache/spark/sql/expressions/javalang/typed.java
    39 ./sql/core/src/main/java/org/apache/spark/sql/internal/NonClosableMutableURLClassLoader.java
    58 ./sql/core/src/main/java/org/apache/spark/sql/SaveMode.java
   153 ./sql/core/src/main/java/org/apache/spark/sql/streaming/Trigger.java
    22 ./sql/core/src/main/scala/org/apache/spark/sql/internal/package-info.java
 11075 total


```

### mllib
```
源码解析：https://github.com/endymecy/spark-ml-source-analysis/blob/master/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B/data-type.md

矩阵存储效率：https://www.cnblogs.com/xbinworld/p/4273506.html?utm_source=tuicool&utm_medium=referral



概率论与统计
/github/spark/mllib/src/main/scala/org/apache/spark/ml/stat

均值和方差在线计算
【1】[Algorithms for calculating variance](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance)

【2】[Updating mean and variance estimates: an improved method](http://people.xiph.org/~tterribe/tmp/homs/West79-_Updating_Mean_and_Variance_Estimates-_An_Improved_Method.pdf)

【3】[Weighted arithmetic mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)

```




### 纵向拆解 Spark 读数据
```
val spark = SparkSession.builder.appName("ParquetExample").getOrCreate()
// 读取Parquet文件
val df = spark.read.parquet("path/to/your/parquet/file")

主要路线
parquet csv orc输入inputPath即可
jdbc 符合jdbc协议即可
hive 数仓类型，需要通过sql解析来读取，用hive-client

实现函数
DataFrameReader
↓
DataSource.lookupDataSourceV2
↓
DataSourceV2Utils.loadV2Source
↓
实现一套基础算子
ParquetDataSourceV2
ParquetPartitionReaderFactory
ParquetScan
ParquetScanBuilder
ParquetTable
ParquetWrite

hive数仓加载
HiveTableScanExec
↓
makeRDDForTable
makeRDDForPartitionedTable
↓
createNewHadoopRDD
NewHadoopRDD
↓
RDD.compute 触发
↓
hadoop-client
createRecordReader
  hasNext
  next
  close
  getCurrentKey
  getCurrentValue





```

### 纵向拆解 spark 写数据
1. orc
   1. sql/core/src/main/scala/org/apache/spark/sql/execution/datasources/orc/OrcOutputWriter.scala
2. parquet
   1. 
```
核心类
DataFrameWriterV2
  overwrite
  append

V2WriteCommand
  AppendData
  各个执行命令
  ......


RDD 如何落盘到磁盘


```

### 纵向拆解 spark 拼表实现
```
新增拼表算子：https://zhuanlan.zhihu.com/p/271910611

BroadcastHashJoinExec
BroadcastNestedLoopJoinExec
ShuffledHashJoinExec
SortMergeJoinExec
  doExecute
  doProduce
  codegenAnti
  codegenExistence


```
### 极客学习总结
1. RDD的4大属性又可以划分为两类，横向属性和纵向属性。其中，横向属性锚定数据分片实体，并规定了数据分片在分布式集群中如何分布；纵向属性用于在纵深方向构建DAG，通过提供重构RDD的容错能力保障内存计算的稳定性
2. 第一层含义就是众所周知的分布式数据缓存，第二层含义是Stage内的流水线式计算模式。

### 纵向拆解 优化规则
1. Catalyst总共有81条优化规则（Rules），这81条规则会分成27组（Batches）
2. 谓词下推（Predicate Pushdown）
   1. “谓词”指代的是像用户表上“age < 30”这样的过滤条件，“下推”指代的是把这些谓词沿着执行计划向下，推到离数据源最近的地方，从而在源头就减少数据扫描量
3. 列剪裁（Column Pruning）
   1. 列剪裁就是扫描数据源的时候，只读取那些与查询相关的字段
4. 常量替换 （Constant Folding）
   1. “age < 12 + 18”，Catalyst会使用ConstantFolding规则，自动帮我们把条件变成“age < 30”
5. Cache Manager优化
6. 为了让查询计划（Query Plan）变得可操作、可执行，Catalyst的物理优化阶段（Physical Planning）可以分为两个环节：优化Spark Plan和生成Physical Plan。
   1. 在优化Spark Plan的过程中，Catalyst基于既定的优化策略（Strategies），把逻辑计划中的关系操作符一一映射成物理操作符，生成Spark Plan
   2. 在生成Physical Plan过程中，Catalyst再基于事先定义的Preparation Rules，对Spark Plan做进一步的完善、生成可执行的Physical Plan。
7. 从数量上来说，Catalyst有14类优化策略，其中有6类和流计算有关，剩下的8类适用于所有的计算场景，如批处理、数据分析、机器学习和图计算，当然也包括流计算。因此，我们只需了解这8类优化策略。
8. 结合Joins的实现机制和数据的分发方式，Catalyst在运行时总共支持5种Join策略，分别是Broadcast Hash Join（BHJ）、Shuffle Sort Merge Join（SMJ）、Shuffle Hash Join（SHJ）、Broadcast Nested Loop Join（BNLJ）和Shuffle Cartesian Product Join（CPJ）。
9. 这些信息分为两大类，第一类是“条件型”信息，用来判决5大Join策略的先决条件。第二类是“指令型”信息，也就是开发者提供的Join Hints。
10. 第一种是Join类型，也就是是否等值、连接形式等，这种信息的来源是查询语句本身。第二种是内表尺寸，这些信息的来源就比较广泛了，可以是Hive表之上的ANALYZE TABLE语句，也可以是Spark对于Parquet、ORC、CSV等源文件的尺寸预估，甚至是来自AQE的动态统计信息。
11. Preparation Rules有6组规则，这些规则作用到Spark Plan之上就会生成Physical Plan，而Physical Plan最终会由Tungsten转化为用于计算RDD的分布式任务。
12. ER原则
    1.  子节点的输出数据要满足父节点的输入要求
13. BHJ > SMJ > SHJ > BNLJ > CPJ
14. 在生成Physical Plan这个环节，Catalyst基于既定的几组Preparation Rules，把优化过后的Spark Plan转换成可以交付执行的物理计划，也就是Physical Plan。在这些既定的Preparation Rules当中，你需要重点掌握EnsureRequirements规则。
15. EnsureRequirements用来确保每一个操作符的输入条件都能够得到满足，在必要的时候，会把必需的操作符强行插入到Physical Plan中。比如对于Shuffle Sort Merge Join来说，这个操作符对于子节点的数据分布和顺序都是有明确要求的，因此，在子节点之上，EnsureRequirements会引入新的操作符如Exchange和Sort。



```

```

### 纵向拆解 AQE
1. AQE既定的规则和策略主要有4个，分为1个逻辑优化规则和3个物理优化策略
2. Join策略调整：如果某张表在过滤之后，尺寸小于广播变量阈值，这张表参与的数据关联就会从Shuffle Sort Merge Join降级（Demote）为执行效率更高的Broadcast Hash Join。
   1. DemoteBroadcastHashJoin规则的作用，是把Shuffle Joins降级为Broadcast Joins。需要注意的是，这个规则仅适用于Shuffle Sort Merge Join这种关联机制，其他机制如Shuffle Hash Join、Shuffle Nested Loop Join都不支持
   2. 中间文件尺寸总和小于广播阈值spark.sql.autoBroadcastJoinThreshold
   3. 空文件占比小于配置项spark.sql.adaptive.nonEmptyPartitionRatioForBroadcastJoin
   4. 在这样的背景下，OptimizeLocalShuffleReader物理策略就非常重要了。既然大表已经完成Shuffle Map阶段的计算，这些计算可不能白白浪费掉。采取OptimizeLocalShuffleReader策略可以省去Shuffle常规步骤中的网络分发，Reduce Task可以就地读取本地节点（Local）的中间文件，完成与广播小表的关联操作。
   5. 不过，需要我们特别注意的是，OptimizeLocalShuffleReader物理策略的生效与否由一个配置项决定。这个配置项是spark.sql.adaptive.localShuffleReader.enabled，尽管它的默认值是True，但是你千万不要把它的值改为False
3. 自动分区合并：在Shuffle过后，Reduce Task数据分布参差不齐，AQE将自动合并过小的数据分区。
   1. 在Reduce阶段，当Reduce Task从全网把数据分片拉回，AQE按照分区编号的顺序，依次把小于目标尺寸的分区合并在一起。
   2. spark.sql.adaptive.advisoryPartitionSizeInBytes，由开发者指定分区合并后的推荐尺寸。
   3. spark.sql.adaptive.coalescePartitions.minPartitionNum，分区合并后，分区数不能低于该值。
4. 自动倾斜处理：结合配置项，AQE自动拆分Reduce阶段过大的数据分区，降低单个Reduce Task的工作负载。
   1. spark.sql.adaptive.skewJoin.skewedPartitionFactor，判定倾斜的膨胀系数
   2. spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes，判定倾斜的最低阈值
   3. spark.sql.adaptive.advisoryPartitionSizeInBytes，以字节为单位，定义拆分粒度

```
总的来说，当应用场景中的数据倾斜比较简单，比如虽然有倾斜但数据分布相对均匀，或是关联计算中只有一边倾斜，我们完全可以依赖AQE的自动倾斜处理机制。但是，当我们的场景中数据倾斜变得复杂，比如数据中不同Key的分布悬殊，或是参与关联的两表都存在大量的倾斜，我们就需要衡量AQE的自动化机制与手工处理倾斜之间的利害得失

如果用一句话来概括AQE的定义，就是每当Shuffle Map阶段执行完毕，它都会结合这个阶段的统计信息，根据既定的规则和策略动态地调整、修正尚未执行的逻辑计划和物理计划，从而完成对原始查询语句的运行时优化。也因此，只有当你的查询语句会引入Shuffle操作的时候，Spark SQL才会触发AQE。

AQE支持的三种优化特性分别是Join策略调整、自动分区合并和自动倾斜处理。

关于Join策略调整，我们首先要知道DemoteBroadcastHashJoin规则仅仅适用于Shuffle Sort Merge Join这种关联机制，对于其他Shuffle Joins类型，AQE暂不支持把它们转化为Broadcast Joins。其次，为了确保AQE的Join策略调整正常运行，我们要确保spark.sql.adaptive.localShuffleReader.enabled配置项始终为开启状态。

关于自动分区合并，我们要知道，在Shuffle Map阶段完成之后，结合分区推荐尺寸与分区数量限制，AQE会自动帮我们完成分区合并的计算过程。

关于AQE的自动倾斜处理我们要知道，它只能以Task为粒度缓解数据倾斜，并不能解决不同Executors之间的负载均衡问题。针对场景较为简单的倾斜问题，比如关联计算中只涉及单边倾斜，我们完全可以依赖AQE的自动倾斜处理机制。但是，当数据倾斜问题变得复杂的时候，我们需要衡量AQE的自动化机制与手工处理倾斜之间的利害得失。


```

### 纵向拆解 ShuffleWriteProcessor
1. 一次shuffle异常入口：https://github.com/apache/spark/pull/33721/files

```



```

### 纵向拆解 Sort shuffle manager
1. Map阶段是如何输出中间文件的？
   1. Map阶段最终生产的数据会以中间文件的形式物化到磁盘中，这些中间文件就存储在spark.local.dir设置的文件目录里。中间文件包含两种类型：一类是后缀为data的数据文件，存储的内容是Map阶段生产的待分发数据；另一类是后缀为index的索引文件，它记录的是数据文件中不同分区的偏移地址。这里的分区是指Reduce阶段的分区，因此，分区数量与Reduce阶段的并行度保持一致。
   2. 因此，中间文件的数量与Map阶段的并行度保持一致。换句话说，有多少个Task，Map阶段就会生产相应数量的数据文件和索引文件。
2. 目标分区计算好之后，Map Task会把每条数据记录和它的目标分区，放到一个特殊的数据结构里，这个数据结构叫做“PartitionedPairBuffer”，它本质上就是一种数组形式的缓存结构。它是怎么存储数据记录的呢？
3. Spark需要一种计算机制，来保障在数据总量超出可用内存的情况下，依然能够完成计算。这种机制就是：排序、溢出、归并。
   1. 对于分片中的数据记录，逐一计算其目标分区，并将其填充到PartitionedPairBuffer；
   2. PartitionedPairBuffer填满后，如果分片中还有未处理的数据记录，就对Buffer中的数据记录按（目标分区ID，Key）进行排序，将所有数据溢出到临时文件，同时清空缓存；
   3. 重复步骤1、2，直到分片中所有的数据记录都被处理；
   4. 对所有临时文件和PartitionedPairBuffer归并排序，最终生成数据文件和索引文件。
4. reduceByKey采用一种叫做PartitionedAppendOnlyMap的数据结构来填充数据记录。这个数据结构是一种Map，而Map的Value值是可累加、可更新的
5. 依靠高效的内存数据结构、更少的磁盘文件、更小的文件尺寸，我们就能大幅降低了Shuffle过程中的磁盘和网络开销。
6. Reduce Task通过网络拉取中间文件的过程，实际上就是不同Stages之间数据分发的过程
   

```
对于分片中的数据记录，逐一计算其目标分区，然后填充内存数据结构（PartitionedPairBuffer或PartitionedAppendOnlyMap）；
当数据结构填满后，如果分片中还有未处理的数据记录，就对结构中的数据记录按（目标分区ID，Key）排序，将所有数据溢出到临时文件，同时清空数据结构；
重复前2个步骤，直到分片中所有的数据记录都被处理；
对所有临时文件和内存数据结构中剩余的数据记录做归并排序，最终生成数据文件和索引文件。



```

### 纵向拆解 push based shuffle

### 纵向拆解 spark 压测
1. spark/core/benchmarks

```

CoalescedRDDBenchmark-jdk11-results.txt  KryoSerializerBenchmark-jdk11-results.txt       PropertiesCloneBenchmark-jdk11-results.txt  ZStandardBenchmark-jdk11-results.txt
CoalescedRDDBenchmark-jdk17-results.txt 

```
### 纵向拆解 spark 数据结构
1. ExternalAppendOnlyMap
   1. 应用：src/main/scala/org/apache/spark/rdd/CoGroupedRDD.scala#createExternalMap
   2. 需要实现combine
   3. 需要实现spill
2. ExternalSorter
   1. 
3. BytesToBytesMap
4. 
```

```


### 纵向拆解 window
1. Tumbling Window划分出来的时间窗口“不重不漏”，而Sliding Window划分出来的窗口，可能会重叠、也可能会有遗漏
2. 由于有Late data的存在，流处理引擎就需要一个机制，来判定Late data的有效性，从而决定是否让晚到的消息，参与到之前窗口的计算。
3. 为了解决Late data的问题，Structured Streaming采用了一种叫作Watermark的机制来应对。为了让你能够更容易地理解Watermark机制的原理，在去探讨它之前，我们先来澄清两个极其相似但是又完全不同的概念：水印和水位线。
4. 延迟容忍度T是Watermark机制中的决定性因素

### Calalog 注册 - 如何全方位感知外部元数据
```
SessionCatalog 
ExternalCatalog

```

### aggregate 聚合实现


### 窗口实现
1. 源码位置
   1. src/main/scala/org/apache/spark/sql/expressions/Window.scala
   2. src/main/scala/org/apache/spark/sql/catalyst/expressions/windowExpressions.scala
   3. src/main/scala/org/apache/spark/sql/execution/window/WindowExec.scala
   4. src/main/scala/org/apache/spark/sql/execution/window/WindowFunctionFrame.scala 
   5. 定义层
      1. Window WindowSpec WindowFrame
   6. 执行层
      1. WindowExec WindowFunctionFrame
2. 聚合窗口函数
   1. AggregateWindowFunction
      1. denseRank
      2. PercentRank
         1. 计算表达式 
         2. If(n > one, (rank - one).cast(DoubleType) / (n - one).cast(DoubleType), 0.0d)
      3. 
   2. DeclarativeAggregate
   3. ImperativeAggregate
   4. 
   5. NTile 
3. 资料
   1. 【spark原理系列】Spark Window窗口计算原理用法示例源码分析 - SparkML的文章 - 知乎https://zhuanlan.zhihu.com/p/658865590
   2. 窗口函数为什么更容易出现性能问题：https://cloud.tencent.com/developer/article/2234156
   3. SparkSql窗口函数源码分析（第一部分） - 小萝卜算子的文章 - 知乎 https://zhuanlan.zhihu.com/p/559731615
   4. sparksql比hivesql优化的点（窗口函数） - 小萝卜算子的文章 - 知乎 https://zhuanlan.zhihu.com/p/126594370




## 性能总结
1. Tungsten
   1. UnsafeRow 内存管理和二进制处理：利用应用程序语义显式管理内存并消除 JVM 对象模型和垃圾收集的开销
   2. UnsafeExternalSorter UnsafeInMemorySorter 缓存感知计算：利用内存层次结构的算法和数据结构
   3. WSCG 代码生成：使用代码生成来利用现代编译器和 CPU
   4. 无虚函数分派：这减少了多次 CPU 调用，这在分派数十亿次时会对性能产生深远影响。
   5. 内存中的中间数据与 CPU 寄存器：内存中的中间数据与 CPU 寄存器：Tungsten Phase 2 将中间数据放入 CPU 寄存器中。这是从 CPU 寄存器而不是从内存中获取数据的周期数减少了一个数量级
   6. 循环展开和 SIMD：优化 Apache Spark 的执行引擎，以利用现代编译器和 CPU 高效编译和执行简单 for 循环（相对于复杂函数调用图）的能力。其中最主要的是内存管理和二进制处理，缓存感知计算以及代码生成。而无虚函数分派、内存中的中间数据与 CPU 寄存器和循环展开和 SIMD都包括在动态代码生成中。
2. [SPARK][SQL] Tungsten优化带来的福报 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/553731823

### AQE
1. 目标：全局上消除数据倾斜、降低IO和提高资源利用率
2. [SPARK][SQL] 一切梦的开始Spark AQE的源码初探 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/535174818
3. SPARK AQE 梳理 - 大数据孔乙己的文章 - 知乎 https://zhuanlan.zhihu.com/p/548331874
4. [SPARK][SQL] 面试问题之Spark AQE新特性 - 天天来了的文章 - 知乎https://zhuanlan.zhihu.com/p/533982903
5. spark3 AQE 源码解析一 - AQE 执行流程 - 终日而思一的文章 - 知乎 https://zhuanlan.zhihu.com/p/639537850
6. 提效 7 倍，Apache Spark 自适应查询优化在网易的深度实践及改进 - 网易数帆的文章 - 知乎 https://zhuanlan.zhihu.com/p/313411006
```
动态选择join策略、自动的分区合并和自动处理数据倾斜的join

你知道AQE是如何处理数据倾斜的吗？如果倾斜的Task全部都集中到同一个Executor那么AQE还能处理吗？
数据倾斜的方式针对的是Task级别的数据倾斜，主要是将同一个executor内的倾斜task进行拆分，而对于数据全集中在个别executor内的情况就无济于事了。


我们知道，AQE 依赖的统计信息来源于 Shuffle Map 阶段输出的中间文件。你觉得，在运行时，AQE 还有其他渠道可以获得同样的统计信息吗？



首先明确一个核心概念，AQE 的设计和优化完全围绕着 shuffle，也就是说如果执行计划里不包含 shuffle，那么 AQE 是无效的。常见的可能产生 shuffle 的算子比如 Aggregate(group by), Join, Repartition。

一是动态修改执行计划；二是动态生成 shuffle reader

map 负责写 shuffle 数据，reduce 负责读取 shuffle 数据

触发入口
QueryExecution#prepareExecutedPlan()

执行入口
AdaptiveSparkPlanExec#doExecute()

核心方法
AdaptiveSparkPlanExec#getFinalPhysicalPlan

功能
通过cost信息优化plan
replaceWithQueryStagesInLogicalPlan

AdaptiveSparkPlanExec

InsertAdaptiveSparkPlan

计算逻辑 getFinalPhysicalPlan


迭代生成新的stage
createQueryStages
newQueryStage
QueryExecution.preparations


从上面的代码可以看出判断是否可以应用AQE有以下几步：

[1] 判断是否开启AQE
[2] 首先和数据写入相关的命令算子不会应用AQE
[3] 其次判断是否满足以下条件之一可以应用AQE
[4] 验证是否支持AQE
开启AQE需要满足以下至少其中一个：

开启AQE强制应用的开关；
query中包含子查询；
query 包含Exchange算子或者是否需要添加Exchange算子，即存在shuffle or broadcast事件。


commit优化
SPARK-35239，这个 issue 可以描述为当输入的 RDD 分区是空的时候无法对其 shuffle 的分区合并。看起来影响并不大，如果是空表的话那么就算空跑一些任务也是非常快的。但是在 Add hoc 场景下，默认的 spark.sql.shuffle.partitions 配置调整很大，这就会造成严重的 task 资源浪费，并且加重 Driver 的负担

SPARK-34899，当我们发现某些 shuffle 分区在被 AQE 的分区合并规则成功优化后，分区数居然没有下降，一度怀疑是没有找到正确使用 AQE 的姿势

SPARK-35168，一些 Hive 转过来的同学可能会遇到的 issue，理论上 MapReduce 中 reduce 的数量等价于 Spark 的 shuffle 分区数，所以 Spark 做了一些配置映射。但是在映射中出现了 bug 这肯定是不能容忍的。

SPARK-35214，使得 Join 倾斜优化在覆盖维度上得到了提升。


kyuubi 和 aqe
https://kyuubi.readthedocs.io/en/master/deployment/spark/aqe.html?highlight=aqe

https://books.japila.pl/spark-sql-internals/physical-optimizations/InsertAdaptiveSparkPlan/#physical-plans-supporting-adaptive-query-execution

```
#### 类解释
简单类
AdaptiveRulesHolder： A holder to warp the SQL extension rules of adaptive query execution.
  queryStagePrepRules
  runtimeOptimizerRules
  queryStageOptimizerRules

AdaptiveSparkPlanHelper：工具类，用于遍历自适应的树节点，对比 TreeNode QueryPlan更方便

AQEOptimizer
AQEUtils
ShufflePartitionsUtil

规则类
AdjustShuffleExchangePosition
  在 AQE 框架中，为了保留用户指定的重分区，可能会在重新优化过程中添加回 shuffle，这就需要调整 shuffle 的位置。
  具体的调整方式是，将 shuffle 的子节点替换为 shuffle 本身，同时将 shuffle 的子节点的子节点替换为 shuffle 的子节点。这样，shuffle 就被移动到了其子节点的位置。

AQEPropagateEmptyRelation
AQEShuffleReadRule
CoalesceShufflePartitions
DynamicJoinSelection
LogicalQueryStageStrategy
OptimizeShuffleWithLocalRead
OptimizeSkewedJoin
OptimizeSkewInRebalancePartitions
PlanAdaptiveDynamicPruningFilters
PlanAdaptiveSubqueries
ReuseAdaptiveSubquery
ValidateSparkPlan

核心类
AdaptiveSparkPlanExec
AQEShuffleReadExec
InsertAdaptiveSparkPlan
LogicalQueryStage
QueryStageExec



遗留
DeserializeToObjectExec
Cost CostEvaluator
SimpleCost


### 过滤优化技术 DPP 动态分区裁剪
1. [SPARK][SQL] 聊一聊Spark 3.0中的DPP特性 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/548757324
2. [SPARK][SQL] 聊聊Spark 3.3 中的Runtime Filter Joins - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/542468151
3. 基于min-max索引的Data-skiping技术：它指的是在元数据中都记录这数据文件中的每一列的最小值和最大值，通过查询中列上的谓词来决定当前的数据文件是否可能包含满足谓词的任何records，是否可以跳过读取当前数据文件。
4. [Delta][SQL] 全面分析下Delta付费功能ZOrder的源码实现 - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/539656969
```
运行时数据过滤策略
动态分区修剪（dynamic partition pruning，DPP）
动态文件修剪（dynamic file pruning，DFP）
以适应动态文件跳过（dynamic file skipping）



DynamicPruningSubquery
PartitionPruning

PlanDynamicPruningFilters
RowLevelOperationRuntimeGroupFiltering

分区剪裁往往能更好地提升磁盘访问的I/O效率。

这是因为，谓词下推操作往往是根据文件注脚中的统计信息完成对文件的过滤，过滤效果取决于文件中内容的“纯度”。分区剪裁则不同，它的分区表可以把包含不同内容的文件，隔离到不同的文件系统目录下。这样一来，包含分区键的过滤条件能够以文件系统目录为粒度对磁盘文件进行过滤，从而大幅提升磁盘访问的I/O效率。

而动态分区剪裁这个功能主要用在星型模型数仓的数据关联场景中，它指的是在运行的时候，Spark SQL利用维度表提供的过滤信息，来减少事实表中数据的扫描量、降低I/O开销，从而提升执行性能。

动态分区剪裁运作的背后逻辑，是把维度表中的过滤条件，通过关联关系传导到事实表，来完成事实表的优化。在数据关联的场景中，开发者要想利用好动态分区剪裁特性，需要注意3点：

事实表必须是分区表，并且分区字段必须包含Join Key
动态分区剪裁只支持等值Joins，不支持大于、小于这种不等值关联关系
维度表过滤之后的数据集，必须要小于广播阈值，因此，开发者要注意调整配置项spark.sql.autoBroadcastJoinThreshold

```

### 向量化计算
1. https://engineering.fb.com/2024/02/20/developer-tools/velox-apache-arrow-15-composable-data-management/
```
查看指令集
cat /proc/cpuinfo | grep --color -wE "bmi|bmi2|f16c|avx|avx2|sse"


聚合时Shuffle阶段OOM
SIMD指令crash


支持ORC并优化读写性能
Native HDFS客户端优化
Shuffle重构
适配HBO


```

### CPU
```
首先，在一个Executor中，每个CPU线程能够申请到的内存比例是有上下限的，最高不超过1/N，最低不少于1/N/2，其中N代表线程池大小。

其次，在给定线程池大小和执行内存的时候，并行度较低、数据分片较大容易导致CPU线程挂起，线程频繁挂起不利于提升CPU利用率，而并行度过高、数据过于分散会让调度开销更显著，也利于提升CPU利用率。

最后，在给定执行内存M、线程池大小N和数据总量D的时候，想要有效地提升CPU利用率，我们就要计算出最佳并行度P，计算方法是让数据分片的平均大小D/P坐落在（M/N/2, M/N）区间。这样，在运行时，我们的CPU利用率往往不会太差。



```

### 内存
```

第一步是预估内存占用。

求出User Memory区域的内存消耗，公式为：#User=#size乘以Executor线程池的大小。
求出每个Executor中Storage Memory区域的内存消耗，公式为：#Storage = #bc + #cache / #E。
求出执行内存区域的内存消耗，公式为：#Execution = #threads * #dataset / #N。
第二步是调整内存配置项：根据公式得到的3个内存区域的预估大小#User、#Storage、#Execution，去调整（spark.executor.memory – 300MB）* spark.memory.fraction * spark.memory.storageFraction公式中涉及的所有配置项。

spark.memory.fraction可以由公式（#Storage + #Execution）/（#User + #Storage + #Execution）计算得到。
spark.memory.storageFraction的数值应该参考（#Storage）/（#Storage + #Execution）。
spark.executor.memory的设置，可以通过公式300MB + #User + #Storage + #Execution得到。
这里，我还想多说几句，内存规划两步走终归只是手段，它最终要达到的效果和目的，是确保不同内存区域的占比与不同类型的数据消耗保持一致，从而实现内存利用率的最大化。



```

## codegen
```
codegen含义参考 横向拆解 代码生成

```
### 表达式生成
1. 一部分是最基本表达式的代码生成
2. 全阶段代码生成，即WSCG
3. 向量化
```


```



## 机器调优
```
并行度
压缩
序例化
数据倾斜
JVM调优 (例如 JVM 数据结构化优化)
内存调优
Task性能调优 (例如包含 Mapper 和 Reducer 两种类型的 Task)
Shuffle 网络调优 (例如小文件合并)
RDD 算子调优 (例如 RDD 复用、自定义 RDD)
数据本地性
容错调优
参数调优

作者：Andy
链接：https://www.zhihu.com/question/42924755/answer/538139206
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```
## RBO 优化规则
1. 核心类
2. RuleExecutor 规则执行引擎 重试次数/策略/配置
3. RuleIdCollection 所有的规则集合 分析 优化 执行计划等
4. SparkOptimizer 
5. [SPARK][SQL] 聊聊Spark 3.3 中的Runtime Filter Joins - Tim在路上的文章 - 知乎 https://zhuanlan.zhihu.com/p/542468151
```
参考 纵向拆解 优化规则

```

### stage 如何并发执行

### 高速读写优化点
1. 读取数据湖数据时，尤其是在读取update的数据时，数据的有序性对读取的性能影响是非常大的。
2. Sort策略时，Iceberg还支持在创建表插入数据前设置表的排序字段，提前优化数据的组织方式，提升了读取的效率，不过也影响了写入的速度。
3. Zorder排序压缩策略使得多个排序字段时，每个字段的优先级是相等的。
4. Zorder排序压缩策略优点是对于多个经常使用的字段可以提升读取的性能，缺点是合并压缩的时间较长。

## 经验总结
1. 数据一致性
2. 数据重复写入
3. 离线和在线架构本质的区别
4. 性能调优总结：https://zhuanlan.zhihu.com/p/668815239

### 聚合优化
```
groupBy 是重操作
可以
PairRDDFunctions.aggregateByKey
PairRDDFunctions.reduceByKey
来替代

聚合实现原理
https://www.jianshu.com/p/d42b4defc71c

```


### 长序列特征计算优化
1. 

### 笛卡尔积性能

### push-based shuffle架构
1. shuffle read阶段存在大量小block随机读和磁盘热点问题，而单节点HDD盘的IOPS非常有限
2. 


### ORC读数据优化


### 向量化执行

### HBO二期

### count distinct性能优化
1. sparksql源码系列 | 一文搞懂with one count distinct 执行原理 - 小萝卜算子的文章 - 知乎 https://zhuanlan.zhihu.com/p/529695118


### 

## 设计
### schema 优良设计
```
元数据
StructType {
  StructField(StructType(可嵌套) IntegerType StringType ......)
}

行数据实体
Row


示例代码：https://mungingdata.com/apache-spark/dataframe-schema-structfield-structtype/

```

### 算子通用性设计
```
逻辑算子



gpt问：总结归纳，类名，方法，输入输出参数，属性。形成树形结构打印出来
物理执行算子
核心实现：SparkContext.union
类名：UnionRDD
类名：UnionPartition

类名: UnionExec
方法:
output: 计算UnionExec的输出属性。
doExecute: 执行UnionExec。
supportsColumnar: 检查UnionExec是否支持列式执行。
supportsRowBased: 检查UnionExec是否支持行式执行。
doExecuteColumnar: 执行UnionExec的列式版本。
withNewChildrenInternal: 创建一个新的UnionExec实例，用新的children替换现有的children。
输入参数:

children: 一个Seq[SparkPlan]类型的参数，用于初始化UnionExec的子计划。
输出参数:

Seq[Attribute]: UnionExec的输出属性。
属性:

children: 子计划列表。


```

### FileScanRDD
```


```

### spark如何开启hive  enableHiveSupport()
1. 如何将这套逻辑映射其他服务中呢
2. 可以支持任意hivesql读写


### spark如何一行可以同时应用在多个udf上面，具体实现逻辑
1. 入口
   1. WindowExec.doExecute
2. 流程
   1. 输入 InternalRow
   2. 处理算子如 AggregateProcessor
   3. AggregateProcessor 传入 functions: Array[Expression]
   4. initialize
      1. 初始化 输出 Row
      2. initialProjection(buffer)
   5. update
      1. JoinedRow 如果有拼接则拼接
      2. updateProjection(join(buffer, input))
   6. evaluate
      1. evaluateProjection.target(target)(buffer)
3. 核心类
   1. MutableProjection
   2. GenerateMutableProjection
   3. InterpretedMutableProjection
   4. UnsafeProjection
   5. UnsafeRow

### spark ui设计
1. 入口
   1. src/main/scala/org/apache/spark/sql/execution/ui/SQLTab.scala
   2. src/main/scala/org/apache/spark/sql/execution/ui/ExecutionPage.scala




### MAP - REDUCE原理
1. 


### 分布式累加器如何实现

## 后端架构 + Spark


## 应用
### 代码片段
1. 使用Java创建一个Row：https://code-cookbook.readthedocs.io/zh-cn/main/Blog%20Here/[Spark]%E4%BD%BF%E7%94%A8Java%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AARow.html


### Blaze：SparkSQL Native算子优化在快手的深度优化及大规模应用实践
```
https://mp.weixin.qq.com/s/ne5FCgFDK29BWbLHjm0ZqA

```


### 数据湖
1. 核心能力：https://mp.weixin.qq.com/s/BKfB1ooYp6vdlDvMKQuccQ
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



