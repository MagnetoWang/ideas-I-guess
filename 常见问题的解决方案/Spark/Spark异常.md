
## SparkException: Error communicating with MapOutputTracker
```
spark bulkload hbase异常挂
7~9小时报异常


可能分区太多，driver管理不过来了
https://bourneli.github.io/scala/spark/2016/09/20/Spark-Error-communicating-with-MapOutputTracker.html


最终原因 join后的rdd 并发数太多有13万个task，改成8万就可以正常运行了
https://issues.apache.org/jira/browse/SPARK-32210
https://github.com/apache/spark/pull/33721

--conf spark.io.compression.zstd.level=15 --conf spark.default.parallelism=80000

20/07/07 02:22:26,366 ERROR [map-output-dispatcher-3] spark.MapOutputTrackerMaster:91 :
java.lang.NegativeArraySizeException
        at org.apache.commons.io.output.ByteArrayOutputStream.toByteArray(ByteArrayOutputStream.java:322)
        at org.apache.spark.MapOutputTracker$.serializeMapStatuses(MapOutputTracker.scala:984)
        at org.apache.spark.ShuffleStatus$$anonfun$serializedMapStatus$2.apply$mcV$sp(MapOutputTracker.scala:228)
        at org.apache.spark.ShuffleStatus$$anonfun$serializedMapStatus$2.apply(MapOutputTracker.scala:222)
        at org.apache.spark.ShuffleStatus$$anonfun$serializedMapStatus$2.apply(MapOutputTracker.scala:222)
        at org.apache.spark.ShuffleStatus.withWriteLock(MapOutputTracker.scala:72)
        at org.apache.spark.ShuffleStatus.serializedMapStatus(MapOutputTracker.scala:222)
        at org.apache.spark.MapOutputTrackerMaster$MessageLoop.run(MapOutputTracker.scala:493)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)


24/06/12 03:22:41 INFO Thread-6 ApplicationMaster: Unregistering ApplicationMaster with FAILED (diag message: User class threw exception: java.lang.Exception: Job aborted due to stage failure: Task 2 in stage 12.0 failed 4 times, most recent failure: Lost task 2.3 in stage 12.0 (TID 142954, hlsc-data-hdp-dn03295.mt, executor 783): org.apache.spark.SparkException: Error communicating with MapOutputTracker
	at org.apache.spark.MapOutputTracker.askTracker(MapOutputTracker.scala:668)
	at org.apache.spark.MapOutputTrackerWorker.$anonfun$getStatuses$7(MapOutputTracker.scala:1696)
	at org.apache.spark.util.KeyLock.withLock(KeyLock.scala:64)
	at org.apache.spark.MapOutputTrackerWorker.getStatuses(MapOutputTracker.scala:1692)
	at org.apache.spark.MapOutputTrackerWorker.getMapSizesByExecutorIdImpl(MapOutputTracker.scala:1522)
	at org.apache.spark.MapOutputTrackerWorker.getMapSizesByExecutorId(MapOutputTracker.scala:1492)
	at org.apache.spark.shuffle.sort.SortShuffleManager.getReader(SortShuffleManager.scala:144)
	at org.apache.spark.shuffle.ShuffleManager.getReader(ShuffleManager.scala:63)
	at org.apache.spark.shuffle.ShuffleManager.getReader$(ShuffleManager.scala:57)
	at org.apache.spark.shuffle.sort.SortShuffleManager.getReader(SortShuffleManager.scala:73)
	at org.apache.spark.rdd.CoGroupedRDD.$anonfun$compute$2(CoGroupedRDD.scala:148)
	at scala.collection.TraversableLike$WithFilter.$anonfun$foreach$1(TraversableLike.scala:877)
	at scala.collection.immutable.List.foreach(List.scala:392)
	at scala.collection.TraversableLike$WithFilter.foreach(TraversableLike.scala:876)
	at org.apache.spark.rdd.CoGroupedRDD.compute(CoGroupedRDD.scala:136)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:52)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:349)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:313)
	at org.apache.spark.shuffle.ShuffleWriteProcessor.write(ShuffleWriteProcessor.scala:59)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:102)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:54)
	at org.apache.spark.scheduler.Task.run(Task.scala:130)
	at org.apache.spark.executor.Executor$TaskRunner.$anonfun$run$3(Executor.scala:477)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1428)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:480)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
Caused by: org.apache.spark.rpc.RpcTimeoutException: Futures timed out after [120 seconds]. This timeout is controlled by spark.rpc.askTimeout
	at org.apache.spark.rpc.RpcTimeout.org$apache$spark$rpc$RpcTimeout$$createRpcTimeoutException(RpcTimeout.scala:47)
	at org.apache.spark.rpc.RpcTimeout$$anonfun$addMessageIfTimeout$1.applyOrElse(RpcTimeout.scala:62)
	at org.apache.spark.rpc.RpcTimeout$$anonfun$addMessageIfTimeout$1.applyOrElse(RpcTimeout.scala:58)
	at scala.runtime.AbstractPartialFunction.apply(AbstractPartialFunction.scala:38)
	at org.apache.spark.rpc.RpcTimeout.awaitResult(RpcTimeout.scala:76)
	at org.apache.spark.rpc.RpcEndpointRef.askSync(RpcEndpointRef.scala:105)
	at org.apache.spark.rpc.RpcEndpointRef.askSync(RpcEndpointRef.scala:89)
	at org.apache.spark.MapOutputTracker.askTracker(MapOutputTracker.scala:664)
	... 41 more
Caused by: java.util.concurrent.TimeoutException: Futures timed out after [120 seconds]
	at scala.concurrent.impl.Promise$DefaultPromise.ready(Promise.scala:259)
	at scala.concurrent.impl.Promise$DefaultPromise.result(Promise.scala:263)
	at org.apache.spark.util.ThreadUtils$.awaitResult(ThreadUtils.scala:294)
	at org.apache.spark.rpc.RpcTimeout.awaitResult(RpcTimeout.scala:75)
	... 44 more

Driver stacktrace:
	at com.meituan.aios.dmx.DmxMultiImporterMain$.main(DmxMultiImporterMain.scala:77)
	at com.meituan.aios.dmx.DmxMultiImporterMain.main(DmxMultiImporterMain.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.spark.deploy.yarn.ApplicationMaster$$anon$2.run(ApplicationMaster.scala:750)
)

```


## 高效判断not in Cannot broadcast the table over 357913941 rows: 670984004 rows
```


    WITH stag AS (
    SELECT *
    FROM mart_aiosupply.supply_app_yiyao_sku_recommend_STAG_20240625_dmx
      where  product_status = 0 and sell_status = 0
    ),
    prod AS (
    SELECT *
    FROM mart_aiosupply.supply_app_yiyao_sku_recommend_PROD_20240625_dmx
      where  product_status = 0 and sell_status = 0
    )
    
    select * from prod where product_id not in (
    select product_id from stag
    )

    


2024-06-25 17:02:52 Start diagnosing the cause of the failure...
org.apache.spark.SparkException: Cannot broadcast the table over 357913941 rows: 670984004 rows



```


## 视图join，会扫全表的坑 - presto可以下推视图join条件，spark不行
```
It is possible the underlying files have been updated. You can explicitly invalidate the cache in Spark by running 'REFRESH TABLE tableName' command in SQL or by recreating the Dataset/DataFrame involved

[DMXLOG] 2024-07-11 12:10:23 [ERROR] com.meituan.aios.dmx.importer.spark.fuse.AbstractFuse.fuse:143 - fuse exception:org.apache.spark.SparkException: Job aborted due to stage failure: Task 901193 in stage 7.0 failed 4 times, most recent failure: Lost task 901193.3 in stage 7.0 (TID 903811, hlsc-data-hdp-dn03567.mt, executor 368): java.io.FileNotFoundException: File does not exist: /zw01nn09/warehouse/mart_lingshou.db/dim_prod_product_spu_s_snapshot/dt=20220718/part-00418-f5f7cd12-6bef-4417-946a-0ca2f9406084-c000
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)
Caused by: org.apache.hadoop.ipc.RemoteException(java.io.FileNotFoundException): File does not exist: /zw01nn09/warehouse/mart_lingshou.db/dim_prod_product_spu_s_snapshot/dt=20220718/part-00418-f5f7cd12-6bef-4417-946a-0ca2f9406084-c000
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.hdfs.protocol.proto.ClientNamenodeProtocolProtos$ClientNamenodeProtocol$2.callBlockingMethod(ClientNamenodeProtocolProtos.java)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)

	at org.apache.hadoop.ipc.Client.extractCallException(Client.java:2059)
	at org.apache.hadoop.ipc.Client.access$3500(Client.java:120)
	at org.apache.hadoop.ipc.Client$Connection.lambda$receiveRpcResponse$6(Client.java:1647)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

It is possible the underlying files have been updated. You can explicitly invalidate the cache in Spark by running 'REFRESH TABLE tableName' command in SQL or by recreating the Dataset/DataFrame involved.
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.org$apache$spark$sql$execution$datasources$FileScanRDD$$anon$$readCurrentFile(FileScanRDD.scala:166)
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.processNextFile(FileScanRDD.scala:214)
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.hasNext(FileScanRDD.scala:121)
	at org.apache.spark.sql.execution.FileSourceScanExec$$anon$1.hasNext(DataSourceScanExec.scala:526)
	at org.apache.spark.sql.catalyst.expressions.GeneratedClass$GeneratedIteratorForCodegenStage3.columnartorow_nextBatch_0$(Unknown Source)
	at org.apache.spark.sql.catalyst.expressions.GeneratedClass$GeneratedIteratorForCodegenStage3.processNext(Unknown Source)
	at org.apache.spark.sql.execution.BufferedRowIterator.hasNext(BufferedRowIterator.java:43)
	at org.apache.spark.sql.execution.WholeStageCodegenExec$$anon$1.hasNext(WholeStageCodegenExec.scala:729)
	at scala.collection.Iterator$$anon$10.hasNext(Iterator.scala:458)
	at org.apache.spark.shuffle.sort.UnsafeShuffleWriter.write(UnsafeShuffleWriter.java:179)
	at org.apache.spark.shuffle.ShuffleWriteProcessor.write(ShuffleWriteProcessor.scala:59)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:102)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:54)
	at org.apache.spark.scheduler.Task.run(Task.scala:130)
	at org.apache.spark.executor.Executor$TaskRunner.$anonfun$run$3(Executor.scala:477)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1428)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:480)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

Driver stacktrace:
	at org.apache.spark.scheduler.DAGScheduler.failJobAndIndependentStages(DAGScheduler.scala:2737)
	at org.apache.spark.scheduler.DAGScheduler.$anonfun$abortStage$2(DAGScheduler.scala:2673)
	at org.apache.spark.scheduler.DAGScheduler.$anonfun$abortStage$2$adapted(DAGScheduler.scala:2672)
	at scala.collection.mutable.ResizableArray.foreach(ResizableArray.scala:62)
	at scala.collection.mutable.ResizableArray.foreach$(ResizableArray.scala:55)
	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:49)
	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:2672)
	at org.apache.spark.scheduler.DAGScheduler.$anonfun$handleTaskSetFailed$1(DAGScheduler.scala:1083)
	at org.apache.spark.scheduler.DAGScheduler.$anonfun$handleTaskSetFailed$1$adapted(DAGScheduler.scala:1083)
	at scala.Option.foreach(Option.scala:407)
	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:1083)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:2926)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:2866)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:2855)
	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:49)
	at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:861)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:2155)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:2176)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:2195)
	at org.apache.spark.sql.execution.SparkPlan.executeTake(SparkPlan.scala:467)
	at org.apache.spark.sql.execution.SparkPlan.executeTake(SparkPlan.scala:420)
	at org.apache.spark.sql.execution.CollectLimitExec.executeCollect(limit.scala:47)
	at org.apache.spark.sql.Dataset.collectFromPlan(Dataset.scala:3631)
	at org.apache.spark.sql.Dataset.$anonfun$head$1(Dataset.scala:2701)
	at org.apache.spark.sql.Dataset.$anonfun$withAction$1(Dataset.scala:3622)
	at org.apache.spark.sql.execution.SQLExecution$.withNewQueryId(SQLExecution.scala:58)
	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$5(SQLExecution.scala:125)
	at org.apache.spark.sql.execution.SQLExecution$.withSQLConfPropagated(SQLExecution.scala:185)
	at org.apache.spark.sql.execution.SQLExecution$.$anonfun$withNewExecutionId$1(SQLExecution.scala:112)
	at org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:767)
	at org.apache.spark.sql.execution.SQLExecution$.withNewExecutionId(SQLExecution.scala:89)
	at org.apache.spark.sql.Dataset.withAction(Dataset.scala:3620)
	at org.apache.spark.sql.Dataset.head(Dataset.scala:2701)
	at org.apache.spark.sql.Dataset.head(Dataset.scala:2708)
	at org.apache.spark.sql.Dataset.first(Dataset.scala:2715)
	at com.meituan.aios.dmx.importer.spark.fuse.HiveFuse.getData(HiveFuse.scala:85)
	at com.meituan.aios.dmx.importer.spark.fuse.AbstractFuse.$anonfun$fuse$2(AbstractFuse.scala:45)
	at scala.util.control.Breaks.breakable(Breaks.scala:42)
	at com.meituan.aios.dmx.importer.spark.fuse.AbstractFuse.$anonfun$fuse$1(AbstractFuse.scala:44)
	at com.meituan.aios.dmx.importer.spark.fuse.AbstractFuse.$anonfun$fuse$1$adapted(AbstractFuse.scala:43)
	at scala.collection.IndexedSeqOptimized.foreach(IndexedSeqOptimized.scala:36)
	at scala.collection.IndexedSeqOptimized.foreach$(IndexedSeqOptimized.scala:33)
	at scala.collection.mutable.ArrayOps$ofRef.foreach(ArrayOps.scala:198)
	at com.meituan.aios.dmx.importer.spark.fuse.AbstractFuse.fuse(AbstractFuse.scala:43)
	at com.meituan.aios.dmx.importer.spark.loader.plugin.HiveDataLoader.loadData(HiveDataLoader.scala:53)
	at com.meituan.aios.dmx.importer.spark.DmxMultiSourceImportTask.$anonfun$run$1(DmxMultiSourceImportTask.scala:93)
	at scala.collection.immutable.Range.foreach$mVc$sp(Range.scala:158)
	at com.meituan.aios.dmx.importer.spark.DmxMultiSourceImportTask.run(DmxMultiSourceImportTask.scala:90)
	at com.meituan.aios.dmx.DmxMultiImporterMain$.main(DmxMultiImporterMain.scala:33)
	at com.meituan.aios.dmx.DmxMultiImporterMain.main(DmxMultiImporterMain.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.spark.deploy.yarn.ApplicationMaster$$anon$2.run(ApplicationMaster.scala:750)
Caused by: java.io.FileNotFoundException: File does not exist: /zw01nn09/warehouse/mart_lingshou.db/dim_prod_product_spu_s_snapshot/dt=20220718/part-00418-f5f7cd12-6bef-4417-946a-0ca2f9406084-c000
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)
Caused by: org.apache.hadoop.ipc.RemoteException(java.io.FileNotFoundException): File does not exist: /zw01nn09/warehouse/mart_lingshou.db/dim_prod_product_spu_s_snapshot/dt=20220718/part-00418-f5f7cd12-6bef-4417-946a-0ca2f9406084-c000
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.hdfs.protocol.proto.ClientNamenodeProtocolProtos$ClientNamenodeProtocol$2.callBlockingMethod(ClientNamenodeProtocolProtos.java)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)

	at org.apache.hadoop.ipc.Client.extractCallException(Client.java:2059)
	at org.apache.hadoop.ipc.Client.access$3500(Client.java:120)
	at org.apache.hadoop.ipc.Client$Connection.lambda$receiveRpcResponse$6(Client.java:1647)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

It is possible the underlying files have been updated. You can explicitly invalidate the cache in Spark by running 'REFRESH TABLE tableName' command in SQL or by recreating the Dataset/DataFrame involved.
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.org$apache$spark$sql$execution$datasources$FileScanRDD$$anon$$readCurrentFile(FileScanRDD.scala:166)
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.processNextFile(FileScanRDD.scala:214)
	at org.apache.spark.sql.execution.datasources.FileScanRDD$$anon$1.hasNext(FileScanRDD.scala:121)
	at org.apache.spark.sql.execution.FileSourceScanExec$$anon$1.hasNext(DataSourceScanExec.scala:526)
	at org.apache.spark.sql.catalyst.expressions.GeneratedClass$GeneratedIteratorForCodegenStage3.columnartorow_nextBatch_0$(Unknown Source)
	at org.apache.spark.sql.catalyst.expressions.GeneratedClass$GeneratedIteratorForCodegenStage3.processNext(Unknown Source)
	at org.apache.spark.sql.execution.BufferedRowIterator.hasNext(BufferedRowIterator.java:43)
	at org.apache.spark.sql.execution.WholeStageCodegenExec$$anon$1.hasNext(WholeStageCodegenExec.scala:729)
	at scala.collection.Iterator$$anon$10.hasNext(Iterator.scala:458)
	at org.apache.spark.shuffle.sort.UnsafeShuffleWriter.write(UnsafeShuffleWriter.java:179)
	at org.apache.spark.shuffle.ShuffleWriteProcessor.write(ShuffleWriteProcessor.scala:59)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:102)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:54)
	at org.apache.spark.scheduler.Task.run(Task.scala:130)
	at org.apache.spark.executor.Executor$TaskRunner.$anonfun$run$3(Executor.scala:477)
	at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1428)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:480)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

```


## FileFormatWriter算子不能写入null，需要过滤 row == null
```
Caused by: java.lang.NullPointerException
24/07/29 14:47:30 ERROR Driver ApplicationMaster: User class threw exception: org.apache.spark.SparkException: Job aborted.
org.apache.spark.SparkException: Job aborted.
	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$write$1.apply(FileFormatWriter.scala:274)
	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$write$1.apply(FileFormatWriter.scala:209)
	at org.apache.spark.sql.execution.SQLExecution$.withNewQueryId(SQLExecution.scala:57)
	at org.apache.spark.sql.execution.SQLExecution$.withNewExecutionId(SQLExecution.scala:101)
	at org.apache.spark.sql.execution.datasources.FileFormatWriter$.write(FileFormatWriter.scala:209)
	at org.apache.spark.sql.execution.datasources.InsertIntoHadoopFsRelationCommand.run(InsertIntoHadoopFsRelationCommand.scala:152)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.sideEffectResult$lzycompute(commands.scala:58)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.sideEffectResult(commands.scala:56)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.doExecute(commands.scala:74)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$execute$1.apply(SparkPlan.scala:117)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$execute$1.apply(SparkPlan.scala:117)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$executeQuery$1.apply(SparkPlan.scala:138)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:151)
	at org.apache.spark.sql.execution.SparkPlan.executeQuery(SparkPlan.scala:135)
	at org.apache.spark.sql.execution.SparkPlan.execute(SparkPlan.scala:116)
	at org.apache.spark.sql.execution.QueryExecution.toRdd$lzycompute(QueryExecution.scala:102)
	at org.apache.spark.sql.execution.QueryExecution.toRdd(QueryExecution.scala:98)
	at org.apache.spark.sql.execution.datasources.DataSource.writeInFileFormat(DataSource.scala:438)
	at org.apache.spark.sql.execution.datasources.DataSource.writeAndRead(DataSource.scala:454)
	at org.apache.spark.sql.execution.command.CreateDataSourceTableAsSelectCommand.saveDataIntoTable(createDataSourceTables.scala:198)
	at org.apache.spark.sql.execution.command.CreateDataSourceTableAsSelectCommand.run(createDataSourceTables.scala:158)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.sideEffectResult$lzycompute(commands.scala:58)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.sideEffectResult(commands.scala:56)
	at org.apache.spark.sql.execution.command.ExecutedCommandExec.doExecute(commands.scala:74)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$execute$1.apply(SparkPlan.scala:117)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$execute$1.apply(SparkPlan.scala:117)
	at org.apache.spark.sql.execution.SparkPlan$$anonfun$executeQuery$1.apply(SparkPlan.scala:138)
	at org.apache.spark.rdd.RDDOperationScope$.withScope(RDDOperationScope.scala:151)
	at org.apache.spark.sql.execution.SparkPlan.executeQuery(SparkPlan.scala:135)
	at org.apache.spark.sql.execution.SparkPlan.execute(SparkPlan.scala:116)
	at org.apache.spark.sql.execution.QueryExecution.toRdd$lzycompute(QueryExecution.scala:102)
	at org.apache.spark.sql.execution.QueryExecution.toRdd(QueryExecution.scala:98)
	at org.apache.spark.sql.DataFrameWriter.runCommand(DataFrameWriter.scala:610)
	at org.apache.spark.sql.DataFrameWriter.createTable(DataFrameWriter.scala:420)
	at org.apache.spark.sql.DataFrameWriter.saveAsTable(DataFrameWriter.scala:399)
	at org.apache.spark.sql.DataFrameWriter.saveAsTable(DataFrameWriter.scala:354)
	at com.meituan.supply.offline.biz.dmx.DumpHive$.main(DumpHive.scala:108)
	at com.meituan.supply.offline.biz.dmx.DumpHive.main(DumpHive.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.spark.deploy.yarn.ApplicationMaster$$anon$2.run(ApplicationMaster.scala:688)
Caused by: org.apache.spark.SparkException: Job aborted due to stage failure: Task 1 in stage 1.0 failed 4 times, most recent failure: Lost task 1.3 in stage 1.0 (TID 7, zw06-data-hdp-dn06559.mt, executor 1): java.lang.NullPointerException

Driver stacktrace:
	at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1667)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1655)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1654)
	at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:48)
	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1654)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:842)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:842)
	at scala.Option.foreach(Option.scala:257)
	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:842)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:1884)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1833)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1822)
	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:48)
	at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:650)
	at org.apache.spark.SparkContext.runJob(SparkContext.scala:2070)
	at org.apache.spark.sql.execution.datasources.FileFormatWriter$$anonfun$write$1.apply(Fil

```

## executor心跳超时
```
作业失败直接原因是这个，executor心跳超时

Job aborted due to stage failure: Task 507 in stage 19.0 failed 4 times, most recent failure: Lost task 507.3 in stage 19.0 (TID 5104, yg-data-hdp-dn00350.mt, executor 298): ExecutorLostFailure (executor 298 exited caused by one of the running tasks) Reason: Executor heartbeat timed out after 137713 ms

2024-08-04 17:07:06 GCTime(ms): 114
2024-08-04 17:17:27 GCTime(ms): 503379
2024-08-04 17:27:42  GCTime(ms): 1109147

executor内存严重不足， 根据日志看，每隔10分钟统计的gc时间，分别为8分钟和10分钟

```


## File does not exist
```
24/08/07 12:24:55 INFO task-result-getter-0 TaskSetManager: Lost task 5637.1 in stage 21.0 (TID 27557) on zw01-data-hdp-dn05225.mt, executor 2280: java.io.FileNotFoundException (File does not exist: /zw02nn93/warehouse/mart_aiosupply.db/supply_selection_tag_relation_v2/dt=20240807/item_type=PoiNormal/part-00399-44c0ee32-1288-4d8e-8bb0-bcbc522c79a9.c000
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)
Caused by: org.apache.hadoop.ipc.RemoteException(java.io.FileNotFoundException): File does not exist: /xx/warehouse/xx.db/xx/dt=xx
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:88)
	at org.apache.hadoop.hdfs.server.namenode.INodeFile.valueOf(INodeFile.java:78)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocationsInt(FSNamesystem.java:2571)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2544)
	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getBlockLocations(FSNamesystem.java:2409)
	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.getBlockLocations(NameNodeRpcServer.java:780)
	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.getBlockLocations(ClientNamenodeProtocolServerSideTranslatorPB.java:448)
	at org.apache.hadoop.hdfs.protocol.proto.ClientNamenodeProtocolProtos$ClientNamenodeProtocol$2.callBlockingMethod(ClientNamenodeProtocolProtos.java)
	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:713)
	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:975)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:1002)
	at org.apache.hadoop.ipc.Server$RpcCall.run(Server.java:923)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.Subject.doAs(Subject.java:422)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1726)
	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2786)

	at org.apache.hadoop.ipc.Client.extractCallException(Client.java:2059)
	at org.apache.hadoop.ipc.Client.access$3500(Client.java:120)
	at org.apache.hadoop.ipc.Client$Connection.lambda$receiveRpcResponse$6(Client.java:1647)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```





##
```


```


##
```


```


##
```


```


##
```


```




