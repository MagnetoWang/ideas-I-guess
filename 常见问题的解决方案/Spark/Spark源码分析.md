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
4. 



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


### 

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

### 纵向拆解 AQE

### 纵向拆解 ShuffleWriteProcessor
1. 一次shuffle异常入口：https://github.com/apache/spark/pull/33721/files

```



```

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


### count distinct性能优化
1. sparksql源码系列 | 一文搞懂with one count distinct 执行原理 - 小萝卜算子的文章 - 知乎 https://zhuanlan.zhihu.com/p/529695118

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



