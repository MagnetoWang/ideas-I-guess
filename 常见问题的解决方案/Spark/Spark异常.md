
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




