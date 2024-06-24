## Flink
### 理解时间
```
2023年7月10号启动

完整理解flink项目
如果只是在搜索引擎 搜 flink是远远不够的
flink + 架构图

flink + 概念关键词

flink + 问题排查

flink + 面试汇总

flink + 极客挑战赛

flink + 论坛会议

flink + 论文

flink + 前沿分享

flink + 场景应用

flink + flink大佬名字

flink + 公司项目
等等才能完全熟悉flink


```


### 参考资料
```
xiaogang shi相关paper

watermark内容
watermark 原理：https://zhuanlan.zhihu.com/p/507776567
深入理解流计算中的 Watermark：http://www.whitewood.me/2019/02/24/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%E6%B5%81%E8%AE%A1%E7%AE%97%E4%B8%AD%E7%9A%84-Watermark/
FLIP-126: Unify (and separate) Watermark Assigners：https://cwiki.apache.org/confluence/display/FLINK/FLIP-126%3A+Unify+%28and+separate%29+Watermark+Assigners


state内容
什么是 Flink State Evolution?：http://www.whitewood.me/2019/03/17/%E4%BB%80%E4%B9%88%E6%98%AF-Flink-State-Evolution/


专家带你吃透 Flink 架构：一个新版 Connector 的实现
https://cloud.tencent.com/developer/article/1930263


Apache Flink 必知必会经典课程
https://www.bilibili.com/video/BV1vf4y1x7se/?spm_id_from=333.999.0.0&vd_source=0f9d0e0a195e3352b97b5cb0ca3e57a2

flink官方教程
https://github.com/flink-china/flink-training-course/


有状态流式处理引擎基石
https://files.alicdn.com/tpsservice/b55f732fbc32522ca5394544f3834530.pdf


快手流批一体
https://flink-learning.org.cn/article/detail/110131b6a6c6c707c647459726ef039a?spm=a2csy.flink.0.0.49495badMgiAjD

flink业界用法

自定义jar包

flink sql写法

flink dag用法

流批一体

```
### Streaming System bookNote


Watermarked
- 加入逻辑时间时间戳，每条消息，在in-flight场景中，呈现正态分布
- 正态分布的最左值，也就是最旧的事件时间戳，定义为 watermarked
- 




### 功能架构

1. 客户端
   1. 启动jobManager
   2. 启动taskManager
   3. 启动client
2. 服务端







### 模块架构 - 从底向上
1. Core
2. Table
   1. Common
   2. API Java
3. Connectors
   1. File Sink Common
4. RPC
5. Queryable state
6. FileSystems
7. Runtime
8. Streaming Java
9.  Table
   1.  API bridge base
   2.  API Java bridge
   3.  Code Splitter
10. Optimizer
11. Clients
12. State backends
    1.  RocksDB
    2.  Common
    3.  Changelog
13. Table
    1. Runtime
    2. SQL Parser
    3. Calcite Bridge
    4. API Scala
14. Streaming Scala
15. Connectors
    1.  Base
    2.  Files
16. Table
    1.  Planner
    2.  SQL Gateway : API 
    3.  SQL Gateway
    4.  SQL Client
17. FileSystems
    1.  Hadoop FS shaded
    2.  S3 FS Base
    3.  S3 FS Hadoop
    4.  S3 FS Presto
18. Container
19. Queryable state : Runtime
20. State backends : Heap spillable 
21. Walkthrough
    1.  Common
    2.  Datastream Java

### flink-connectors
- 已实践
- flink-connectors-hbase-1.4
- flink-connectors-hbase-2.2
- flink-connectors-hive

### flink-core
- core
  - 核心类
  - 核心包 memory io fs 内存文件io读写
  - 非核心包 plugin execution
- api
  - common
    - 重要类
      - DistributedCache Plan TaskInfo
    - 核心包 eventtime stat operators functions cache
    - 非核心包 aggregators accumulators externalresource io
  - connector
    -  sink source
  - dag 
    - Pipeline Transformation
- configuration 所有配置和options
  - 如AlgorithmOptions DeploymentOptions HeartbeatManagerOptions
- java
  - tuple keySelector KryoSerializer DataInputViewStream DataOutputViewStream ListTypeInfo
  - ClosureCleaner AvroUtils
- 非核心包 types util

#### 模块详解
1. RowSerializer RowComparator



### flink-table 初识
- common
  - annotation
    - DataTypeHint/FunctionHint
  - api
    - Constraint
    - DataView/ListView/MapView
    - TableColumn/TableSchema/WatermarkSpec
  - catalog
    - CatalogDatabase/CatalogBaseTable/CatalogFunction/CatalogPartition/CatalogView
    - CatalogColumnStatistics
  - connector
    - BulkDecodingFormat/DecodingFormat/EncodingFormat
    - SupportsOverwrite/SupportsPartitioning/SupportsWritingMetadata
    - SupportsFilterPushDown/SupportsLimitPushDown/SupportsPartitionPushDown
  - data/expressions/functions
    - GenericArrayData/GenericMapData
  - 非核心包 descriptors factories module plan types util
- api java
  - api
  - operations 
  - delegation
  - expressions
  - catalog
  - 非核心包 typeutils tsextractors module functions factories descriptors
- api bridge
  - 非核心模块
- code splitter
  - 非核心模块
- 


### RPC/Queryable state/FileSystems
- rpc - 无相关代码，只有依赖
- qs - runtime
  - KvState(client, request, server)
  - KvStateID QueryableStateClient 
- FileSystems
  - hadoop
  - oss
  - s3
  - HadoopFileStatus HadoopFileSystem

### Runtime 核心模块
- runtime
  - checkpoint 核心逻辑 
  - execution
    - FlinkUserCodeClassLoader 用户代码类加载器
      - core模块有工具 ChildFirstClassLoader FlinkUserCodeClassLoader
  - execution graph
    - ExecutionGraph
  - job
    - job graph
    - job manager
    - job master
  - task
    - task executor
    - task manager
  - state
  - scheduler
  - 选主
    - leadereletion
    - leaderretrival
  - dispatcher
  - entrypoint
  - blob 模块
  - broadcast
  - shuffle
  - slots
  - 
  - 优秀设计
    - topology
    - event
  - 中等核心
    - acumulator 累加器 可自定义 
    - io compression disk network
    - iterative
    - memory
    - message
    - metrics
    - operators
    - persistence
    - query
    - security
    - rpc
    - rest
  - 不核心 
    - executionsource heartbeat history instance management minicluster net plugable registration

#### 模块详解
1. checkpoint
   1. Chandy-Lamport算法
   2. CheckpointCoordinator
   3. PendingCheckpoint
   4. CheckpointIDCounter
   5. CompletedCheckpoint
      1. CompletedCheckpointStore
   6. MasterHook
   7. CheckpointStatsTracker
      1. JobStatus
   8. ScheduledExecutor
      1. trigger 设计
      2. CompletableFuture
      3. Clock
      4. isExactlyOnceMode
2. state
   1. filesystem
   2. memory
   3. ttl
   4. KeyedState
   5. KeyGroup
   6. StateBackend



### Streaming Java flink-stream-jave
1. api
   1. functions
   2. SourceFunction
   3. RichParallelSourceFunction
2. runtime
3. util
4. experimental

#### 模块详解
1. CountingOutput

### Optimizer/State backends
1. optimizer 能力比较弱
2. backends主要是堆外内存和rocksdb的管理


#### 模块详解
1. Optimizer 
2. DataStatistics 统计能力用于cost

### flink-state-backends + heap-spillable

#### 模块详解
1. RocksDBStateBackend
2. RocksDBKeyedStateBackend
3. AbstractKeyedStateBackend
4. ColumnFamilyHandle
   1. 封装抽象 list map各种结构
   2. 直接调用rocksdb的接口
5. 状态存储测试验证
   1. RocksDBTestUtils
   2. KVStateRequestSerializerRocksDBTest

### flink-table 进阶
- Runtime
- sql parser
- calcite bridge
- api scala

1. Table 和 TableResult区别
2. 

### flink-table 高阶
- planner
- Planner Loader
- SQL Jdbc Driver
- blink介绍 专注批量计算plan构建
  - https://nightlies.apache.org/flink/flink-docs-release-1.18/release-notes/flink-1.9/
  - https://nightlies.apache.org/flink/flink-docs-release-1.18/release-notes/flink-1.11/


### flink磁盘章节
1. runtime模块
   1. BlockChannelWriter
   2. BulkBlockChannelReader
   3. FileIOChannel
   4. IOManager
2. 磁盘应用的类
   1. ReOpenableHashPartition
### flink内存章节
1. flink-core
   1. DataOutputView
   2. SeekableDataOutputView
   3. dataInputView
   4. MemorySegment
   5. MemorySegmentSource
   6. AbstractPagedOutputView
2. runtime模块
   1. MemoryAllocationException
   2. MemoryManager
3. 应用内存模块的类
   1. MutableHashTable
   2. 

### flink序列化和反序列化章节
1. flink-core
   1. org.apache.flink.api.common.typeutils TypeSerializer
   2. TypeComparator
   3. TypeSerializer
   4. TypePairComparator
   5. SameTypePairComparator


### flink窗口章节


## 应用实现
### 代码示例拆解
```
public class WordCount {
   public static void main(String[] args) throws Exception {
      // StreamExecutionEnvironment初始化
      final StreamExecutionEnvironment env = StreamExecutionEnvironment.
         getExecutionEnvironment();
      // 业务逻辑转换代码
      DataStream<String> text = env.readTextFile("the_path_for_input");
      DataStream<Tuple2<String, Integer>> counts =
         text.flatMap(new Tokenizer())
         .keyBy(0).sum(1);
      counts.writeAsText("the_path_for_output");
      // 执行应用程序
      env.execute("Streaming WordCount");
   }
}

核心类
StreamExecutionEnvironment
DataStream
```

### StreamTableEnvironment
```
Flink SQL 系列 | 5 个 TableEnvironment 我该用哪个
https://developer.aliyun.com/article/719760


datastream -> table
https://github.com/BigDataScholar/TheKingOfBigData/blob/e13c122858756b68807526a4714931a92e2f0776/note/flink/%5B%E5%B9%B2%E8%B4%A7%5D%20%E4%BA%94%E5%8D%83%E5%AD%97%E9%95%BF%E6%96%87%E5%B8%A6%E4%BD%A0%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8FlinkSQL.md



org/apache/flink/table/api/TableEnvironment.java
org/apache/flink/table/api/java/BatchTableEnvironment.java
org/apache/flink/table/api/scala/BatchTableEnvironment.scala
org/apache/flink/table/api/java/StreamTableEnvironment.java
org/apache/flink/table/api/scala/StreamTableEnvironment.scala

TableEnvironment 是顶级接口，是所有 TableEnvironment 的基类 ，BatchTableEnvironment 和 StreamTableEnvironment 都提供了 Java 实现和 Scala 实现 ，分别有两个接口。

TableEnvironment 目前还不支持注册 UDTF 和 UDAF，用户有注册 UDTF 和 UDAF 的需求时，可以选择使用其他 TableEnvironment。

可能大家会疑惑为什么在 API 需要区分 Java 和 Scala 的两个 StreamTableEnvironment（或BatchTableEnvironment ），使用的 DataStream也分为 Java DataStream 和 Scala DataStream。

原因主要是 TableEnvironment 的 registerTableFunction方法（用于注册UDTF） 和 registerAggregateFunction 方法（用户注册UDAF） 需要抽取泛型，而现有的 Java 泛型抽取和 Scala 的泛型抽取机制是不一样的，Java 的抽取是通过反射机制 实现，而 Scala 是通过 Scala macro 实现。此外，由于抽取泛型机制的不一致，作为统一入口的 TableEnvironment 现阶段也不支持注册 UDTF 和 UDAF。针对这个问题，社区已经在计划引入一套新的类型抽取机制来统一 Java 和 Scala 的类型抽取，实现 Java API 和 Scala API 的统一。



```

### TableEnvironment 和 TableEnvironmentImpl 初始化
1. 入口函数：tableEnv = TableEnvironment.create(settings);
2. TableFactoryService 表工厂加载

### 水位线
```
https://juejin.cn/post/6844904195120693262#heading-5

Watermark 定义
完整性（Completeness）：一旦 Watermark 大于某个时间戳 T，那么就代表这个时间戳及之前的数据不会再被处理
可见性（Visibility）：如果一个消息阻塞，那么 Watermark 也会被阻塞（无法递增）

watermark creation
perfect watermark creation 
永远不会出现延迟数据，被丢没有计算的情况
实际上，现实系统不会实现这一要求

Heuristic watermark creation
部分延迟数据可能会丢，导致计算不准
但是可实现，并且尽可能精确



watermark propagation
水位线传播，也就是把水位线信息传输到下游算子，这里会涉及诸多问题
聚合状态和非聚合状态下，非常复杂


Percentile watermark
统计数据分布情况，帮助我们更好选择水位线时间


processing-time watermarks




```

### Left join实现


### Group by实现
- Flink SQL 知其所以然（二十六）：Group 聚合操作 - 大数据羊说的文章 - 知乎https://zhuanlan.zhihu.com/p/531006901
- 




### 动态表
```
大量的工厂类，就是为了解耦多样化数据源，文件格式和多种读写模式

fromDataStream 也可以转table，然后运行sql

核心类 flink-connectors模块
DynamicTableSourceFactory
ScanTableSource
RichSourceFunction
Options 配置

类型转换 flink-formats模块
JsonToRowDataConverters
RowDataToJsonConverters


整体类型
StreamTableEnvironment
BatchTableEnvironment


参考示例类
KafkaDynamicTableFactory
DataFormatConverters

测试可运行的示例
createTemporaryView
FlinkStreamPythonUdfSqlJob
JsonRowDataSerDeSchemaTest
HiveTableSinkITCase





Flink 框架是如何设计的？ - 大数据技术与数仓的回答 - 知乎
https://www.zhihu.com/question/575875502/answer/3436054933


```

### 时态表 Join
1. 官方解释：https://nightlies.apache.org/flink/flink-docs-master/zh/docs/dev/table/concepts/versioned_tables/
2. 时态表join：https://nightlies.apache.org/flink/flink-docs-release-1.16/zh/docs/dev/table/sql/queries/joins/#temporal-joins




### 深入理解字段类型
```
示例代码
DataStream<Row> rowDataStream = source.map(msg -> {
            JsonNode jsonNode = JacksonUtil.readValue(msg, JsonNode.class);
            RowData rowData = (RowData)(runtimeConverter.convert(jsonNode));
            Row actual = convertToExternal(rowData, dataType);
            return actual;
        });


核心类
DataTypes
DataType
RowType
RowType.RowField

类型转换
TypeInfoToSerializerConverter
canSafelyCast
TypeInformation schemaToTypeInfo(TypeDescription schema)



核心方法
DataTypes类中
public static DataType ROW(Field... fields) {
        final List<RowField> logicalFields =
                Stream.of(fields)
                        .map(
                                f ->
                                        Preconditions.checkNotNull(
                                                f, "Field definition must not be null."))
                        .map(f -> new RowField(f.name, f.dataType.getLogicalType(), f.description))
                        .collect(Collectors.toList());
        final List<DataType> fieldDataTypes =
                Stream.of(fields).map(f -> f.dataType).collect(Collectors.toList());
        return new FieldsDataType(new RowType(logicalFields), fieldDataTypes);
    }


```

### schema & 反射的设计 & 自动推断能力
RowTypeInfo
PojoTypeInfo
TypeInformation
TypeExtractor


### flink data结构
1. RowData  JoinedRowData table模块
   1. Base interface for an internal data structure   
   2. org/apache/flink/table/data/RowData.java
2. RowKind Row
   1. A row is a fixed-length, null-aware composite type
   2. Lists all kinds of changes that a row can describe in a changelog
   3. org/apache/flink/types/Row.java
3. GenericRowData GenericArrayData GenericMapData
4. BinaryRowData BinaryArrayData BinaryMapData
5. TimestampData 
6. 类型
   1. DataType
   2. RowType
   3. DistinctType
   4. LogicalType
   5. StructuredType
7.  
8. 
#### data memory设计
1. 参考 flink内存章节



### flink自定义类加载器
```
核心类
FlinkUserCodeClassLoader

```

### flink plan 计划设计
1. 可视化网站
   2. https://wints.github.io/flink-web//visualizer/
3. plan结构设计
   1. org.apache.flink.api.common
   2. Plan
   3. Operator
4. plan工具
   1. org.apache.flink.optimizer.plandump
   2. org.apache.flink.optimizer.plantranslate
   3. ExecutionPlanUtil 转json工具
   4. 
### flink图设计
1. 入口函数
   1. 参考case：testGeneratorWithoutAnyAttachements
   2. FlinkPipelineTranslationUtil.getJobGraph
   3. treamGraphTranslator.translateToJobGraph
   4. StreamGraph.getJobGraph
   5. StreamingJobGraphGenerator.createJobGraph
   6. StreamGraphHasherV2.generateNodeHash
2. 图类型
   1. https://blog.csdn.net/u011047968/article/details/133921646
   2. StreamGraph（数据流图）：是根据用户通过 Stream API 编写的代码生成的最初的图。用来表示程序的拓扑结构。
   3. JobGraph（作业图）：StreamGraph经过优化后生成了 JobGraph，提交给 JobManager 的数据结构。主要的优化为，将多个符合条件的节点 chain 在一起作为一个节点，这样可以减少数据在节点之间流动所需要的序列化/反序列化/传输消耗。
   4. ExecutionGraph（执行图）：JobManager 根据 JobGraph 生成 ExecutionGraph。ExecutionGraph 是 JobGraph 的并行化版本，是调度层最核心的数据结构。
   5. Physical Graph（物理图）：JobManager 根据 ExecutionGraph 对 Job 进行调度后，在各个TaskManager 上部署 Task 后形成的 “图”，并不是一个具体的数据结构。
3. 图结构设计
   1. org.apache.flink.runtime.jobgraph
   2. JobEdge JobGraph JobVertex
   3. JsonPlanGenerator json配置计划生成
   4. node结构
      1. parallelism
      2. trace
   5. ProgramDesc 主图
   6. BlockDesc 子图

### flink ExecutionGraph 执行计划

### flink udf设计
1. UserCodeWrapper
2. InputOutputFormatContainer
3. DistributedRuntimeUDFContext
4. createTemporarySystemFunction 注册函数入口
   1. UserDefinedFunction 可以查到所有继承的udf函数
   2. AddressNormalizer 示例udf

### flink CoProcessFunction & coGroupFunction 设计

## 服务章节
### flink connect hive设计
1. 如何测试hive端
2. 读写hive的代码结构
   1. flink-sql-parser
   2. flink-sql-parser-hive


### flink算子可视化 + flink监控设计 + 监控可视化
1. 核心模块
   1. flink-runtime-web
   2. flink-metrics 非常轻量级的指标系统，可以复用到不同系统中
2. 监控
   1. 类型：Counter、Gauge、Histogram、Meter
   2. https://juejin.cn/post/7037379343248523295
3. Gauge extends Metric 最核心！用户可自定义和注册
   1. 
4. Counter extends Metric
5. Histogram extends Metric
6. LatencyStats
   1. org/apache/flink/streaming/util/LatencyStats.java
7. MetricGroup
8. DescriptiveStatisticsHistogram
9.  LatencyMarker

### flink 任务启动设计


### HistoryServer 历史探查设计
1. The HistoryServer provides a WebInterface and REST API to retrieve information 
2. 主要模块 flink-runtime-web 和 flink-runtime
3. org.apache.flink.runtime.webmonitor.history HistoryServer
4. web启动 netty
5. handle设计 - 处理各种前后端业务逻辑
6. AbstractRestHandler restapi接口设计
7. WebMonitorEndpoint 监控终端
8. org.apache.flink.runtime.rest.handler.router.Router
   1. 路由分发
9.  HttpRequestHandler
10. WebSubmissionExtension 提交器扩展
11. WebFrontendBootstrap 前端启动器
## 算子章节
### flink CopyingChainingOutput CountingOutput 类含义
1. 算子内部报异常，这两个类高频出现，所以想搞清楚是干嘛的

### flink高效实现 cast算子 设计序列化和反序列化


### flink sink算子
#### sink出现的地方
1. org/apache/flink/streaming/runtime/operators/sink
2. org/apache/flink/streaming/api/functions/sink
####  flink async sink实现
- 异步Sink比想的简单（一）：Flink AsyncSinkBase API解析 - 曾中铭的文章 - 知乎 https://zhuanlan.zhihu.com/p/615872927
- Flink Sink中的Bulk Write实现小结 - 曾中铭的文章 - 知乎 https://zhuanlan.zhihu.com/p/607558243

####  sink结合 filesystem
1. 流式写入文件 org/apache/flink/streaming/api/functions/sink/filesystem/StreamingFileSink.java 
2. bucket能力 BucketFactory 数据分区能力 org/apache/flink/streaming/api/functions/sink/filesystem/Bucket.java
3. SinkContextUtil
4. TwoPhaseCommitSinkFunction

### flink window算子
#### window出现的地方
1. org/apache/flink/streaming/runtime/operators/windowing

### runtime - operators模块
1. chaining
2. hash
3. sort
4. 分布式算子调度
   1. AllGroupReduceDriver
   2. AllGroupCombineDriver
   3. AbstractOuterJoinDriver
   4. AbstractCachedBuildSideJoinDriver

### streaming-java - runtime模块
1. runtime模块 和其他模块中子runtime有什么区别
   1. 我感觉可能是一种runtime实现的补充，或者完全两个概念，但是重名极易弄混
2. CopyingChainingOutput 切入口
   1. 经常报错看到这个类，从这里开始了解
3. StreamRecord extends StreamElement
4. StreamStatus extends StreamElement
5. Collector
6. OperatorChain
7. StreamTask

## 第三方集成章节
### flink不错的类
1. DualKeyLinkedMap
2. IntArrayList
3. ExceptionUtils
4. Clock SystemClock ManualClock
5. ClassLoaderUtils 动态加载类工具
6. Formatter 描述符转成html 或者 markdown

### Time 时间解析 org.apache.flink.api.common.time
1. 核心类
   1. TimeFormats
   2. TimeUtils
   3. TimestampFormat
2. Time.hours(1)
3. flink 内部果然实现了 TimeUtils 可以将字符串转成 Duration
4. 比如
5. assertEquals(424562, TimeUtils.parseDuration("424562ns").getNano());
6. 这样就可以复用



###  flink-json 自定义格式转换
官方设计抽象结构
1. JsonFormatFactory
   1. createRuntimeEncoder
      1. JsonRowDataSerializationSchema
         1. RowDataToJsonConverters
            1. convert 核心类 具体实现
      2. 类似还有 JsonRowSerializationSchema
   2. createRuntimeDecoder 同上
      1. JsonTpRowDataConverters

### FunctionalInterface 函数式抽象
1. 示例代码：org/apache/flink/formats/json/JsonToRowDataConverters.java
2. 能解决类型转换的抽象，高可扩展设计

```
    @FunctionalInterface
    public interface JsonToRowDataConverter extends Serializable {
        Object convert(JsonNode jsonNode);
    }

    return jsonNode -> {
            final ArrayNode node = (ArrayNode) jsonNode;
            final Object[] array = (Object[]) Array.newInstance(elementClass, node.size());
            for (int i = 0; i < node.size(); i++) {
                final JsonNode innerNode = node.get(i);
                array[i] = elementConverter.convert(innerNode);
            }
            return new GenericArrayData(array);
        };

```

### flink-parquet
1. ParquetFileFormatFactory 
   1. BulkReaderFormatFactory
   2. BulkWriterFormatFactory
2. ParquetColumnarRowSplitReader
3. Writer
   1. ParquetProtoWriters
   2. ParquetRowDataWriter
   3. ParquetAvroWriters
4. avro 和 protobuf读写能力
5. row格式和向量化写入

### flink-avro
1. AvroValidator Avro
2. AvroFileSystemFormatFactory 依赖解析
```

import org.apache.flink.api.common.io.InputFormat;
import org.apache.flink.configuration.ConfigOption;
import org.apache.flink.core.fs.FileInputSplit;
import org.apache.flink.core.fs.Path;
import org.apache.flink.formats.avro.typeutils.AvroSchemaConverter;
import org.apache.flink.table.data.GenericRowData;
import org.apache.flink.table.data.RowData;
import org.apache.flink.table.factories.FileSystemFormatFactory;
import org.apache.flink.table.types.DataType;
import org.apache.flink.table.types.logical.RowType;
import org.apache.flink.table.utils.PartitionPathUtils;

```

## 痛点
```
低延时
超大规模实时
多维度高并发
准确性
动态可变
快速响应


71 篇 Flink 实战及原理解析文章（面试必备！） - 大数据羊说的文章 - 知乎
https://zhuanlan.zhihu.com/p/467433350
Flink企业级优化全面总结（3万字长文，15张图） - 大数据老哥的文章 - 知乎
https://zhuanlan.zhihu.com/p/428923187
Flink 使用大状态时的一点优化 - Flink 中文社区的文章 - 知乎
https://zhuanlan.zhihu.com/p/164409354
Flink_state 的优化与 remote_state 的探索 - Flink 中文社区的文章 - 知乎
https://zhuanlan.zhihu.com/p/652100408

```
### 去重
```


```
### 双流join
```
Flink 中极其重要的 Time 与 Window 详细解析
https://cloud.tencent.com/developer/article/1779302

万字详述 Flink SQL 4 种时间窗口语义
https://cloud.tencent.com/developer/article/2043021

Flink SQL 知其所以然（二十六）：2w 字详述 Join 操作
https://cloud.tencent.com/developer/article/2043025

原理与实战：AggregateFunction
https://blog.csdn.net/duxu24/article/details/105746110


水位线 

窗口计算

窗口join计算

interval join计算





```

### 维表方案
```

技术实践｜Flink维度表关联方案解析 - 中电金信研究院的文章 - 知乎
https://zhuanlan.zhihu.com/p/694650448

```

## 变更流
### flink核心类
1. DebeziumJsonFormatFactory
2. CanalJsonFormatFactory
### Debezium vs Canal vs Maxwell
1. 数据同步工具之FlinkCDC/Canal/Debezium对比 - 王知无的文章 - 知乎 https://zhuanlan.zhihu.com/p/426489574
2. Debezium监控数据库时，它会将数据库的变更操作（如插入、更新、删除）转换为JSON格式的消息
3. 这些消息包含了变更前的旧值和变更后的新值，以及其他与变更相关的元数据信息
4. Cancel
   1. 阿里巴巴因为杭州和美国双机房部署
   2. 索引构建和实时维护(拆分异构索引、倒排索引等)
   3. 数据库镜像
   4. 数据库实时备份
   5. 业务 cache 刷新
   6. 带业务逻辑的增量数据处理
   7. 
```

{
  "before": {
    "id": 1,
    "name": "John Doe",
    "age": 30
  },
  "after": {
    "id": 1,
    "name": "John Doe",
    "age": 31
  },
  "source": {
    "version": "1.5.0.Final",
    "connector": "mysql",
    "name": "dbserver1",
    "ts_ms": 1642658415000,
    "snapshot": "false",
    "db": "mydb",
    "table": "users",
    "server_id": 1,
    "gtid": null,
    "file": "mysql-bin.000003",
    "pos": 123456,
    "row": 0,
    "thread": 1,
    "query": null
  },
  "op": "u"
}


```


## 行业实践参考
```
Flink 在风控场景实时特征落地实战 - 是咕咕鸡的文章 - 知乎
https://zhuanlan.zhihu.com/p/477262244
微信安全基于 Flink 实时特征开发平台实践 - Flink 中文社区的文章 - 知乎
https://zhuanlan.zhihu.com/p/646114539



```

### 极客挑战赛
```
第三届 Apache Flink 极客挑战赛暨AAIG CUP——电商推荐“抱大腿”攻击识别亚军代码方案
https://github.com/rickyxume/TianChi_RecSys_AntiSpam

```

## case 代码
### 造数
```
    public List<Row> fakeRows() {
        // 创建虚拟行列表
        List<Row> rows = new ArrayList<>();
        rows.add(Row.of("15030140049", "wangzixian", 18));
        rows.add(Row.of("5030140049", "wangzixian", 19));
        rows.add(Row.of("15030140049", "wangzixian", 20));
        return rows;
    }

    public RowTypeInfo rowTypeInfo() {
        TypeInformation<?>[] types = {
                BasicTypeInfo.STRING_TYPE_INFO,
                BasicTypeInfo.STRING_TYPE_INFO,
                BasicTypeInfo.INT_TYPE_INFO
        };
        String[] names = {"a", "b", "c"};
        RowTypeInfo typeInfo = new RowTypeInfo(types, names);
        return typeInfo;
    }

private static final List<Row> testData = new ArrayList<>();
    private static final RowTypeInfo testTypeInfo =
            new RowTypeInfo(
                    new TypeInformation[] {Types.INT, Types.LONG, Types.STRING},
                    new String[] {"a", "b", "c"});

    static {
        testData.add(Row.of(1, 1L, "Hi"));
        testData.add(Row.of(2, 2L, "Hello"));
        testData.add(Row.of(3, 2L, "Hello world"));
        testData.add(Row.of(3, 3L, "Hello world!"));
    }




```