## 网络内存申请失败
set `taskmanager.memory.network.fraction` = `0.4`;
set `taskmanager.memory.network.min` = `100mb`;
set `taskmanager.memory.network.max` = `1740mb`;


2023-11-08 12:40:56
java.io.IOException: Insufficient number of network buffers: required 2, but only 0 available. The total number of network buffers is currently set to 13926 of 32768 bytes each. You can increase this number by setting the configuration keys 'taskmanager.memory.network.fraction', 'taskmanager.memory.network.min', and 'taskmanager.memory.network.max'.
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.tryRedistributeBuffers(NetworkBufferPool.java:443)
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.requestMemorySegments(NetworkBufferPool.java:178)
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.requestMemorySegments(NetworkBufferPool.java:60)
	at org.apache.flink.runtime.io.network.partition.consumer.BufferManager.requestExclusiveBuffers(BufferManager.java:132)
	at org.apache.flink.runtime.io.network.partition.consumer.RemoteInputChannel.setup(RemoteInputChannel.java:161)
	at org.apache.flink.runtime.io.network.partition.consumer.RemoteRecoveredInputChannel.toInputChannelInternal(RemoteRecoveredInputChannel.java:77)
	at org.apache.flink.runtime.io.network.partition.consumer.RecoveredInputChannel.toInputChannel(RecoveredInputChannel.java:106)
	at org.apache.flink.runtime.io.network.partition.consumer.SingleInputGate.convertRecoveredInputChannels(SingleInputGate.java:306)
	at org.apache.flink.runtime.io.network.partition.consumer.SingleInputGate.requestPartitions(SingleInputGate.java:289)
	at org.apache.flink.runtime.taskmanager.InputGateWithMetrics.requestPartitions(InputGateWithMetrics.java:94)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$1.runThrowing(StreamTaskActionExecutor.java:50)
	at org.apache.flink.streaming.runtime.tasks.mailbox.Mail.run(Mail.java:90)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.processMail(MailboxProcessor.java:297)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:189)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)

## Slot request bulk is not fulfillable
队列无资源，换一个队列

2023-11-08 15:20:23
java.util.concurrent.CompletionException: org.apache.flink.runtime.jobmanager.scheduler.NoResourceAvailableException: Slot request bulk is not fulfillable! Could not allocate the required slot within slot request timeout
	at java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:292)
	at java.util.concurrent.CompletableFuture.completeThrowable(CompletableFuture.java:308)
	at java.util.concurrent.CompletableFuture.uniApply(CompletableFuture.java:607)
	at java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:591)
	at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:488)
	at java.util.concurrent.CompletableFuture.completeExceptionally(CompletableFuture.java:1990)
	at org.apache.flink.runtime.scheduler.SharedSlot.cancelLogicalSlotRequest(SharedSlot.java:223)
	at org.apache.flink.runtime.scheduler.SlotSharingExecutionSlotAllocator.cancelLogicalSlotRequest(SlotSharingExecutionSlotAllocator.java:177)
	at org.apache.flink.runtime.scheduler.SharingPhysicalSlotRequestBulk.cancel(SharingPhysicalSlotRequestBulk.java:86)
	at org.apache.flink.runtime.jobmaster.slotpool.PhysicalSlotRequestBulkWithTimestamp.cancel(PhysicalSlotRequestBulkWithTimestamp.java:66)
	at org.apache.flink.runtime.jobmaster.slotpool.PhysicalSlotRequestBulkCheckerImpl.lambda$schedulePendingRequestBulkWithTimestampCheck$0(PhysicalSlotRequestBulkCheckerImpl.java:91)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRunAsync(AkkaRpcActor.java:440)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:208)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)
Caused by: org.apache.flink.runtime.jobmanager.scheduler.NoResourceAvailableException: Slot request bulk is not fulfillable! Could not allocate the required slot within slot request timeout
	at org.apache.flink.runtime.jobmaster.slotpool.PhysicalSlotRequestBulkCheckerImpl.lambda$schedulePendingRequestBulkWithTimestampCheck$0(PhysicalSlotRequestBulkCheckerImpl.java:86)
	... 24 more
Caused by: java.util.concurrent.TimeoutException: Timeout has occurred: 300000 ms
	... 25 more


## 资源耗尽
33554432 = 32GB
扩容kafka客户端缓冲区

2023-11-08 15:29:52
com.meituan.kafka.javaclient.clients.producer.BufferExhaustedException: You have exhausted the 33554432 bytes of memory you configured for the client and the client is configured to error rather than block when memory is exhausted.
	at com.meituan.kafka.javaclient.clients.producer.internals.BufferPool.allocate(BufferPool.java:124)
	at com.meituan.kafka.javaclient.clients.producer.internals.RecordAccumulator.append(RecordAccumulator.java:180)
	at com.meituan.kafka.javaclient.clients.producer.KafkaProducer.send(KafkaProducer.java:536)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doAsyncKafkaSend(DefaultProducerProcessor.java:1686)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doSendAsync(DefaultProducerProcessor.java:1606)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1454)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1420)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1407)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1402)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaProducer.invoke(FlinkMafkaProducer.java:172)
	at org.apache.flink.streaming.api.operators.StreamSink.processElement(StreamSink.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.TimestampedCollector.collect(TimestampedCollector.java:50)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:60)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:15)
	at org.apache.flink.streaming.api.operators.ProcessOperator.processElement(ProcessOperator.java:66)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:252)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)

## Cannot send after the producer
2023-11-08 16:01:20
com.meituan.kafka.javaclient.common.errors.ProducerClosedException: Cannot send after the producer is closed.
	at com.meituan.kafka.javaclient.clients.producer.internals.RecordAccumulator.append(RecordAccumulator.java:164)
	at com.meituan.kafka.javaclient.clients.producer.KafkaProducer.send(KafkaProducer.java:536)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doAsyncKafkaSend(DefaultProducerProcessor.java:1686)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doSendAsync(DefaultProducerProcessor.java:1606)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1454)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1420)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1407)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1402)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaProducer.invoke(FlinkMafkaProducer.java:172)
	at org.apache.flink.streaming.api.operators.StreamSink.processElement(StreamSink.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.TimestampedCollector.collect(TimestampedCollector.java:50)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:60)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:15)
	at org.apache.flink.streaming.api.operators.ProcessOperator.processElement(ProcessOperator.java:66)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:252)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)



## 客户端资源消耗殆尽
33554432 = 32GB
扩容kafka客户端缓冲区

2023-11-08 19:01:55
com.meituan.kafka.javaclient.clients.producer.BufferExhaustedException: You have exhausted the 33554432 bytes of memory you configured for the client and the client is configured to error rather than block when memory is exhausted.
	at com.meituan.kafka.javaclient.clients.producer.internals.BufferPool.allocate(BufferPool.java:124)
	at com.meituan.kafka.javaclient.clients.producer.internals.RecordAccumulator.append(RecordAccumulator.java:180)
	at com.meituan.kafka.javaclient.clients.producer.KafkaProducer.send(KafkaProducer.java:536)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doAsyncKafkaSend(DefaultProducerProcessor.java:1686)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.doSendAsync(DefaultProducerProcessor.java:1606)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1454)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1420)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1407)
	at com.meituan.mafka.client.producer.DefaultProducerProcessor.sendAsyncMessage(DefaultProducerProcessor.java:1402)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaProducer.invoke(FlinkMafkaProducer.java:172)
	at org.apache.flink.streaming.api.operators.StreamSink.processElement(StreamSink.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:85)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.TimestampedCollector.collect(TimestampedCollector.java:50)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:60)
	at com.meituan.data.rt.xflow.formats.SerializeFunction.processElement(SerializeFunction.java:15)
	at org.apache.flink.streaming.api.operators.ProcessOperator.processElement(ProcessOperator.java:66)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:252)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)


## ack 超时
2023-11-08 19:19:15
java.util.concurrent.CompletionException: java.util.concurrent.TimeoutException: Invocation of public abstract java.util.concurrent.CompletableFuture org.apache.flink.runtime.taskexecutor.TaskExecutorGateway.submitTask(org.apache.flink.runtime.deployment.TaskDeploymentDescriptor,org.apache.flink.runtime.jobmaster.JobMasterId,org.apache.flink.api.common.time.Time) timed out.
	at java.util.concurrent.CompletableFuture.encodeRelay(CompletableFuture.java:326)
	at java.util.concurrent.CompletableFuture.completeRelay(CompletableFuture.java:338)
	at java.util.concurrent.CompletableFuture.uniRelay(CompletableFuture.java:925)
	at java.util.concurrent.CompletableFuture$UniRelay.tryFire(CompletableFuture.java:913)
	at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:488)
	at java.util.concurrent.CompletableFuture.completeExceptionally(CompletableFuture.java:1990)
	at org.apache.flink.runtime.rpc.akka.AkkaInvocationHandler.lambda$invokeRpc$0(AkkaInvocationHandler.java:234)
	at java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:774)
	at java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:750)
	at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:488)
	at java.util.concurrent.CompletableFuture.completeExceptionally(CompletableFuture.java:1990)
	at org.apache.flink.runtime.concurrent.FutureUtils$1.onComplete(FutureUtils.java:1044)
	at akka.dispatch.OnComplete.internal(Future.scala:263)
	at akka.dispatch.OnComplete.internal(Future.scala:261)
	at akka.dispatch.japi$CallbackBridge.apply(Future.scala:191)
	at akka.dispatch.japi$CallbackBridge.apply(Future.scala:188)
	at scala.concurrent.impl.CallbackRunnable.run(Promise.scala:36)
	at org.apache.flink.runtime.concurrent.Executors$DirectExecutionContext.execute(Executors.java:73)
	at scala.concurrent.impl.CallbackRunnable.executeWithValue(Promise.scala:44)
	at scala.concurrent.impl.Promise$DefaultPromise.tryComplete(Promise.scala:252)
	at akka.pattern.PromiseActorRef$$anonfun$1.apply$mcV$sp(AskSupport.scala:644)
	at akka.actor.Scheduler$$anon$4.run(Scheduler.scala:205)
	at scala.concurrent.Future$InternalCallbackExecutor$.unbatchedExecute(Future.scala:601)
	at scala.concurrent.BatchingExecutor$class.execute(BatchingExecutor.scala:109)
	at scala.concurrent.Future$InternalCallbackExecutor$.execute(Future.scala:599)
	at akka.actor.LightArrayRevolverScheduler$TaskHolder.executeTask(LightArrayRevolverScheduler.scala:328)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.executeBucket$1(LightArrayRevolverScheduler.scala:279)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.nextTick(LightArrayRevolverScheduler.scala:283)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.run(LightArrayRevolverScheduler.scala:235)
	at java.lang.Thread.run(Thread.java:748)
Caused by: java.util.concurrent.TimeoutException: Invocation of public abstract java.util.concurrent.CompletableFuture org.apache.flink.runtime.taskexecutor.TaskExecutorGateway.submitTask(org.apache.flink.runtime.deployment.TaskDeploymentDescriptor,org.apache.flink.runtime.jobmaster.JobMasterId,org.apache.flink.api.common.time.Time) timed out.
	at org.apache.flink.runtime.jobmaster.RpcTaskManagerGateway.submitTask(RpcTaskManagerGateway.java:68)
	at org.apache.flink.runtime.executiongraph.Execution.lambda$deploy$10(Execution.java:832)
	at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1604)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	... 1 more
Caused by: akka.pattern.AskTimeoutException: Ask timed out on [Actor[akka.tcp://flink@hlsc-data-hdp-dn-ssd-rtyarn00097.mt:25369/user/rpc/taskmanager_0#1061796427]] after [10000 ms]. Message of type [org.apache.flink.runtime.rpc.messages.RemoteRpcInvocation]. A typical reason for `AskTimeoutException` is that the recipient actor didn't send a reply.
	at akka.pattern.PromiseActorRef$$anonfun$2.apply(AskSupport.scala:635)
	at akka.pattern.PromiseActorRef$$anonfun$2.apply(AskSupport.scala:635)
	at akka.pattern.PromiseActorRef$$anonfun$1.apply$mcV$sp(AskSupport.scala:648)
	at akka.actor.Scheduler$$anon$4.run(Scheduler.scala:205)
	at scala.concurrent.Future$InternalCallbackExecutor$.unbatchedExecute(Future.scala:601)
	at scala.concurrent.BatchingExecutor$class.execute(BatchingExecutor.scala:109)
	at scala.concurrent.Future$InternalCallbackExecutor$.execute(Future.scala:599)
	at akka.actor.LightArrayRevolverScheduler$TaskHolder.executeTask(LightArrayRevolverScheduler.scala:328)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.executeBucket$1(LightArrayRevolverScheduler.scala:279)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.nextTick(LightArrayRevolverScheduler.scala:283)
	at akka.actor.LightArrayRevolverScheduler$$anon$4.run(LightArrayRevolverScheduler.scala:235)
	... 1 more


## job 超时
2023-11-09 01:37:31
java.util.concurrent.TimeoutException: The heartbeat of JobManager with id 20cc89b3e7b69f48c0249ed0ac4b6f66 timed out.
	at org.apache.flink.runtime.taskexecutor.TaskExecutor$JobManagerHeartbeatListener.notifyHeartbeatTimeout(TaskExecutor.java:2309)
	at org.apache.flink.runtime.heartbeat.HeartbeatMonitorImpl.run(HeartbeatMonitorImpl.java:111)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRunAsync(AkkaRpcActor.java:440)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:208)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)



## checkpoint失败
checkpoint 慢 - 查查可能有哪些原因
2023-11-09 13:54:56
org.apache.flink.util.FlinkRuntimeException: Exceeded checkpoint tolerable failure threshold.
	at org.apache.flink.runtime.checkpoint.CheckpointFailureManager.handleCheckpointException(CheckpointFailureManager.java:98)
	at org.apache.flink.runtime.checkpoint.CheckpointFailureManager.handleJobLevelCheckpointException(CheckpointFailureManager.java:67)
	at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.abortPendingCheckpoint(CheckpointCoordinator.java:1985)
	at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.abortPendingCheckpoint(CheckpointCoordinator.java:1958)
	at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.access$600(CheckpointCoordinator.java:102)
	at org.apache.flink.runtime.checkpoint.CheckpointCoordinator$CheckpointCanceller.run(CheckpointCoordinator.java:2099)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	at java.lang.Thread.run(Thread.java:748)

### flinkSQL 字段异常
按照类定义的变量名，重新写SQL，而不是json字段名

2023-11-13 10:35:08,815 [INFO] Caused by: org.apache.flink.table.api.ValidationException: user_id is not a field of type PojoType<com.meituan.kugget.flink.job.executor.feature.DqSessionExecutor$SqlMsg, fields = [eventTimestamp: String, sessionId: String, userId: String]>. Expected: eventTimestamp, sessionId, userId}
2023-11-13 10:35:08,818 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils$ExprToFieldInfo.fieldNotFound(FieldInfoUtils.java:637)
2023-11-13 10:35:08,822 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils$ExprToFieldInfo.lambda$createFieldInfo$1(FieldInfoUtils.java:686)
2023-11-13 10:35:08,825 [INFO] at java.util.Optional.orElseThrow(Optional.java:290)
2023-11-13 10:35:08,828 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils$ExprToFieldInfo.createFieldInfo(FieldInfoUtils.java:686)
2023-11-13 10:35:08,831 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils$ExprToFieldInfo.visit(FieldInfoUtils.java:644)
2023-11-13 10:35:08,835 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils$ExprToFieldInfo.visit(FieldInfoUtils.java:625)
2023-11-13 10:35:08,838 [INFO] at org.apache.flink.table.expressions.ApiExpressionVisitor.visit(ApiExpressionVisitor.java:29)
2023-11-13 10:35:08,841 [INFO] at org.apache.flink.table.expressions.UnresolvedReferenceExpression.accept(UnresolvedReferenceExpression.java:59)
2023-11-13 10:35:08,844 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils.lambda$extractFieldInfosByNameReference$8(FieldInfoUtils.java:508)
2023-11-13 10:35:08,848 [INFO] at java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:193)
2023-11-13 10:35:08,851 [INFO] at java.util.Spliterators$ArraySpliterator.forEachRemaining(Spliterators.java:948)
2023-11-13 10:35:08,854 [INFO] at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:481)
2023-11-13 10:35:08,858 [INFO] at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:471)
2023-11-13 10:35:08,861 [INFO] at java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:708)
2023-11-13 10:35:08,864 [INFO] at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)
2023-11-13 10:35:08,867 [INFO] at java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:499)
2023-11-13 10:35:08,871 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils.extractFieldInfosByNameReference(FieldInfoUtils.java:509)
2023-11-13 10:35:08,874 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils.extractFieldInformation(FieldInfoUtils.java:292)
2023-11-13 10:35:08,877 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils.getFieldsInfo(FieldInfoUtils.java:258)
2023-11-13 10:35:08,880 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.lambda$asQueryOperation$3(StreamTableEnvironmentImpl.java:411)
2023-11-13 10:35:08,884 [INFO] at java.util.Optional.map(Optional.java:215)
2023-11-13 10:35:08,887 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.asQueryOperation(StreamTableEnvironmentImpl.java:408)
2023-11-13 10:35:08,890 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.fromDataStream(StreamTableEnvironmentImpl.java:255)
2023-11-13 10:35:08,893 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.fromDataStream(StreamTableEnvironmentImpl.java:249)
2023-11-13 10:35:08,896 [INFO] at com.meituan.kugget.flink.job.executor.feature.DqSessionExecutor.execute(DqSessionExecutor.java:49)
2023-11-13 10:35:08,900 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2023-11-13 10:35:08,903 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2023-11-13 10:35:08,906 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2023-11-13 10:35:08,909 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2023-11-13 10:35:08,913 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2023-11-13 10:35:08,916 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2023-11-13 10:35:08,919 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2023-11-13 10:35:08,922 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2023-11-13 10:35:08,925 [INFO] ... 11 more


### Janino 初始化失败
全部calcite 和 flink相关jar包都为 provided


2023-11-13 15:09:00,748 [INFO] Caused by: java.lang.IllegalStateException: Unable to instantiate java compiler
2023-11-13 15:09:00,750 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:428)
2023-11-13 15:09:00,752 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.load3(JaninoRelMetadataProvider.java:374)
2023-11-13 15:09:00,754 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.lambda$static$0(JaninoRelMetadataProvider.java:109)
2023-11-13 15:09:00,756 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.CacheLoader$FunctionToCacheLoader.load(CacheLoader.java:165)
2023-11-13 15:09:00,757 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LoadingValueReference.loadFuture(LocalCache.java:3529)
2023-11-13 15:09:00,759 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.loadSync(LocalCache.java:2278)
2023-11-13 15:09:00,761 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.lockedGetOrLoad(LocalCache.java:2155)
2023-11-13 15:09:00,763 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.get(LocalCache.java:2045)
2023-11-13 15:09:00,764 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.get(LocalCache.java:3951)
2023-11-13 15:09:00,766 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.getOrLoad(LocalCache.java:3974)
2023-11-13 15:09:00,768 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LocalLoadingCache.get(LocalCache.java:4958)
2023-11-13 15:09:00,770 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.create(JaninoRelMetadataProvider.java:469)
2023-11-13 15:09:00,772 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.revise(JaninoRelMetadataProvider.java:481)
2023-11-13 15:09:00,773 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQueryBase.revise(RelMetadataQueryBase.java:95)
2023-11-13 15:09:00,775 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQuery.getPulledUpPredicates(RelMetadataQuery.java:784)
2023-11-13 15:09:00,777 [INFO] at org.apache.calcite.rel.rules.ReduceExpressionsRule$ProjectReduceExpressionsRule.onMatch(ReduceExpressionsRule.java:303)
2023-11-13 15:09:00,779 [INFO] at org.apache.calcite.plan.AbstractRelOptPlanner.fireRule(AbstractRelOptPlanner.java:333)
2023-11-13 15:09:00,781 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRule(HepPlanner.java:542)
2023-11-13 15:09:00,783 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRules(HepPlanner.java:407)
2023-11-13 15:09:00,784 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeInstruction(HepPlanner.java:243)
2023-11-13 15:09:00,786 [INFO] at org.apache.calcite.plan.hep.HepInstruction$RuleInstance.execute(HepInstruction.java:127)
2023-11-13 15:09:00,788 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeProgram(HepPlanner.java:202)
2023-11-13 15:09:00,790 [INFO] at org.apache.calcite.plan.hep.HepPlanner.findBestExp(HepPlanner.java:189)
2023-11-13 15:09:00,792 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepProgram.optimize(FlinkHepProgram.scala:69)
2023-11-13 15:09:00,793 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepRuleSetProgram.optimize(FlinkHepRuleSetProgram.scala:87)
2023-11-13 15:09:00,795 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:62)
2023-11-13 15:09:00,797 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:58)
2023-11-13 15:09:00,799 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2023-11-13 15:09:00,801 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2023-11-13 15:09:00,802 [INFO] at scala.collection.Iterator$class.foreach(Iterator.scala:891)
2023-11-13 15:09:00,804 [INFO] at scala.collection.AbstractIterator.foreach(Iterator.scala:1334)
2023-11-13 15:09:00,806 [INFO] at scala.collection.IterableLike$class.foreach(IterableLike.scala:72)
2023-11-13 15:09:00,808 [INFO] at scala.collection.AbstractIterable.foreach(Iterable.scala:54)
2023-11-13 15:09:00,810 [INFO] at scala.collection.TraversableOnce$class.foldLeft(TraversableOnce.scala:157)
2023-11-13 15:09:00,812 [INFO] at scala.collection.AbstractTraversable.foldLeft(Traversable.scala:104)
2023-11-13 15:09:00,814 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram.optimize(FlinkChainedProgram.scala:57)
2023-11-13 15:09:00,815 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.optimizeTree(StreamCommonSubGraphBasedOptimizer.scala:163)
2023-11-13 15:09:00,817 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.doOptimize(StreamCommonSubGraphBasedOptimizer.scala:79)
2023-11-13 15:09:00,819 [INFO] at org.apache.flink.table.planner.plan.optimize.CommonSubGraphBasedOptimizer.optimize(CommonSubGraphBasedOptimizer.scala:83)
2023-11-13 15:09:00,821 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.optimize(PlannerBase.scala:287)
2023-11-13 15:09:00,823 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.translate(PlannerBase.scala:160)
2023-11-13 15:09:00,824 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toDataStream(StreamTableEnvironmentImpl.java:357)
2023-11-13 15:09:00,826 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toAppendStream(StreamTableEnvironmentImpl.java:315)
2023-11-13 15:09:00,828 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toAppendStream(StreamTableEnvironmentImpl.java:305)
2023-11-13 15:09:00,830 [INFO] at com.meituan.kugget.flink.job.executor.feature.DqSessionExecutor.execute(DqSessionExecutor.java:65)
2023-11-13 15:09:00,832 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2023-11-13 15:09:00,833 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2023-11-13 15:09:00,835 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2023-11-13 15:09:00,837 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2023-11-13 15:09:00,839 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2023-11-13 15:09:00,841 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2023-11-13 15:09:00,843 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2023-11-13 15:09:00,845 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2023-11-13 15:09:00,846 [INFO] ... 11 more
2023-11-13 15:09:00,848 [INFO] Caused by: java.lang.ClassCastException: org.codehaus.janino.CompilerFactory cannot be cast to org.codehaus.commons.compiler.ICompilerFactory
2023-11-13 15:09:00,850 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getCompilerFactory(CompilerFactoryFactory.java:129)
2023-11-13 15:09:00,852 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getDefaultCompilerFactory(CompilerFactoryFactory.java:79)
2023-11-13 15:09:00,854 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:426)
2023-11-13 15:09:00,856 [INFO] ... 63 more


## 自定义sink-序列化问题 - 再闭包环境新建对象，不要出作用域即可解决
ERROR org.apache.flink.client.cli.CliFrontend                       - Error while running the command.
2024-01-24 22:11:37,598 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: java.lang.ThreadLocal@343e225a is not serializable. The object probably contains or references non serializable fields.
2024-01-24 22:11:37,598 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-01-24 22:11:37,599 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-01-24 22:11:37,599 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-01-24 22:11:37,608 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-01-24 22:11:37,609 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-01-24 22:11:37,609 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-01-24 22:11:37,609 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-01-24 22:11:37,610 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-01-24 22:11:37,610 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-01-24 22:11:37,610 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-01-24 22:11:37,610 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-01-24 22:11:37,611 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-01-24 22:11:37,611 [INFO] Caused by: org.apache.flink.api.common.InvalidProgramException: java.lang.ThreadLocal@343e225a is not serializable. The object probably contains or references non serializable fields.
2024-01-24 22:11:37,611 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:164)
2024-01-24 22:11:37,611 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
2024-01-24 22:11:37,611 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
2024-01-24 22:11:37,612 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:69)
2024-01-24 22:11:37,612 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.clean(StreamExecutionEnvironment.java:2012)
2024-01-24 22:11:37,612 [INFO] at org.apache.flink.streaming.api.datastream.DataStream.clean(DataStream.java:203)
2024-01-24 22:11:37,612 [INFO] at org.apache.flink.streaming.api.datastream.DataStream.addSink(DataStream.java:1243)
2024-01-24 22:11:37,613 [INFO] at com.meituan.kugget.flink.job.executor.sink.UdsSink.execute(UdsSink.java:32)
2024-01-24 22:11:37,613 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-01-24 22:11:37,613 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-01-24 22:11:37,613 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-01-24 22:11:37,613 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-01-24 22:11:37,614 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-01-24 22:11:37,614 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-01-24 22:11:37,614 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-01-24 22:11:37,614 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-01-24 22:11:37,614 [INFO] ... 11 more
2024-01-24 22:11:37,615 [INFO] Caused by: java.io.NotSerializableException: java.lang.ThreadLocal
2024-01-24 22:11:37,615 [INFO] at java.io.ObjectOutputStream.writeObject0(ObjectOutputStream.java:1184)
2024-01-24 22:11:37,615 [INFO] at java.io.ObjectOutputStream.writeObject(ObjectOutputStream.java:348)
2024-01-24 22:11:37,615 [INFO] at org.apache.flink.util.InstantiationUtil.serializeObject(InstantiationUtil.java:624)
2024-01-24 22:11:37,615 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:143)
2024-01-24 22:11:37,616 [INFO] ... 26 more
2024-01-24 22:11:37,616 [INFO] ------------------------------------------------------------


### threadlocal
ERROR org.apache.flink.client.cli.CliFrontend                       - Error while running the command.
2024-01-24 23:02:00,847 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: java.lang.ThreadLocal@93824eb is not serializable. The object probably contains or references non serializable fields.
2024-01-24 23:02:00,848 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-01-24 23:02:00,848 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-01-24 23:02:00,848 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-01-24 23:02:00,849 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-01-24 23:02:00,849 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-01-24 23:02:00,849 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-01-24 23:02:00,856 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-01-24 23:02:00,856 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-01-24 23:02:00,857 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-01-24 23:02:00,857 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-01-24 23:02:00,857 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-01-24 23:02:00,858 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-01-24 23:02:00,858 [INFO] Caused by: org.apache.flink.api.common.InvalidProgramException: java.lang.ThreadLocal@93824eb is not serializable. The object probably contains or references non serializable fields.
2024-01-24 23:02:00,858 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:164)
2024-01-24 23:02:00,858 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
2024-01-24 23:02:00,859 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
2024-01-24 23:02:00,859 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:69)
2024-01-24 23:02:00,859 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.clean(StreamExecutionEnvironment.java:2012)
2024-01-24 23:02:00,859 [INFO] at org.apache.flink.streaming.api.datastream.DataStream.clean(DataStream.java:203)
2024-01-24 23:02:00,860 [INFO] at org.apache.flink.streaming.api.datastream.DataStream.addSink(DataStream.java:1243)
2024-01-24 23:02:00,860 [INFO] at com.meituan.kugget.flink.job.executor.sink.UdsSink.execute(UdsSink.java:32)
2024-01-24 23:02:00,860 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-01-24 23:02:00,860 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-01-24 23:02:00,861 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-01-24 23:02:00,861 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-01-24 23:02:00,861 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-01-24 23:02:00,862 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-01-24 23:02:00,862 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-01-24 23:02:00,862 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-01-24 23:02:00,862 [INFO] ... 11 more
2024-01-24 23:02:00,863 [INFO] Caused by: java.io.NotSerializableException: java.lang.ThreadLocal
2024-01-24 23:02:00,863 [INFO] at java.io.ObjectOutputStream.writeObject0(ObjectOutputStream.java:1184)
2024-01-24 23:02:00,863 [INFO] at java.io.ObjectOutputStream.writeObject(ObjectOutputStream.java:348)
2024-01-24 23:02:00,863 [INFO] at org.apache.flink.util.InstantiationUtil.serializeObject(InstantiationUtil.java:624)
2024-01-24 23:02:00,863 [INFO] at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:143)
2024-01-24 23:02:00,864 [INFO] ... 26 more
2024-01-24 23:02:00,864 [INFO] ------------------------------------------------------------

### java.lang.NoSuchMethodError: org.apache.commons.io.IOUtils.closeQuietly
org.apache.flink.runtime.client.JobExecutionException: Job execution failed.

	at org.apache.flink.runtime.jobmaster.JobResult.toJobExecutionResult(JobResult.java:144)
	at org.apache.flink.runtime.minicluster.MiniClusterJobClient.lambda$getJobExecutionResult$2(MiniClusterJobClient.java:117)
	at java.util.concurrent.CompletableFuture.uniApply(CompletableFuture.java:602)
	at java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:577)
	at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:474)
	at java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:1962)
	at org.apache.flink.runtime.rpc.akka.AkkaInvocationHandler.lambda$invokeRpc$0(AkkaInvocationHandler.java:237)
	at java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:760)
	at java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:736)
	at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:474)
	at java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:1962)
	at org.apache.flink.runtime.concurrent.FutureUtils$1.onComplete(FutureUtils.java:1046)
	at akka.dispatch.OnComplete.internal(Future.scala:264)
	at akka.dispatch.OnComplete.internal(Future.scala:261)
	at akka.dispatch.japi$CallbackBridge.apply(Future.scala:191)
	at akka.dispatch.japi$CallbackBridge.apply(Future.scala:188)
	at scala.concurrent.impl.CallbackRunnable.run(Promise.scala:60)
	at org.apache.flink.runtime.concurrent.Executors$DirectExecutionContext.execute(Executors.java:73)
	at scala.concurrent.impl.CallbackRunnable.executeWithValue(Promise.scala:68)
	at scala.concurrent.impl.Promise$DefaultPromise.$anonfun$tryComplete$1(Promise.scala:284)
	at scala.concurrent.impl.Promise$DefaultPromise.$anonfun$tryComplete$1$adapted(Promise.scala:284)
	at scala.concurrent.impl.Promise$DefaultPromise.tryComplete(Promise.scala:284)
	at akka.pattern.PromiseActorRef.$bang(AskSupport.scala:573)
	at akka.pattern.PipeToSupport$PipeableFuture$$anonfun$pipeTo$1.applyOrElse(PipeToSupport.scala:22)
	at akka.pattern.PipeToSupport$PipeableFuture$$anonfun$pipeTo$1.applyOrElse(PipeToSupport.scala:21)
	at scala.concurrent.Future.$anonfun$andThen$1(Future.scala:532)
	at scala.concurrent.impl.Promise.liftedTree1$1(Promise.scala:29)
	at scala.concurrent.impl.Promise.$anonfun$transform$1(Promise.scala:29)
	at scala.concurrent.impl.CallbackRunnable.run(Promise.scala:60)
	at akka.dispatch.BatchingExecutor$AbstractBatch.processBatch(BatchingExecutor.scala:55)
	at akka.dispatch.BatchingExecutor$BlockableBatch.$anonfun$run$1(BatchingExecutor.scala:91)
	at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:12)
	at scala.concurrent.BlockContext$.withBlockContext(BlockContext.scala:81)
	at akka.dispatch.BatchingExecutor$BlockableBatch.run(BatchingExecutor.scala:91)
	at akka.dispatch.TaskInvocation.run(AbstractDispatcher.scala:40)
	at akka.dispatch.ForkJoinExecutorConfigurator$AkkaForkJoinTask.exec(ForkJoinExecutorConfigurator.scala:44)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)
Caused by: org.apache.flink.runtime.JobException: Recovery is suppressed by NoRestartBackoffTimeStrategy
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.handleFailure(ExecutionFailureHandler.java:118)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getFailureHandlingResult(ExecutionFailureHandler.java:80)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.handleTaskFailure(DefaultScheduler.java:233)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.maybeHandleTaskFailure(DefaultScheduler.java:224)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.updateTaskExecutionStateInternal(DefaultScheduler.java:215)
	at org.apache.flink.runtime.scheduler.SchedulerBase.updateTaskExecutionState(SchedulerBase.java:669)
	at org.apache.flink.runtime.scheduler.SchedulerNG.updateTaskExecutionState(SchedulerNG.java:89)
	at org.apache.flink.runtime.jobmaster.JobMaster.updateTaskExecutionState(JobMaster.java:447)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcInvocation(AkkaRpcActor.java:305)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:212)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction.applyOrElse(PartialFunction.scala:123)
	at scala.PartialFunction.applyOrElse$(PartialFunction.scala:122)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:172)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:172)
	at akka.actor.Actor.aroundReceive(Actor.scala:517)
	at akka.actor.Actor.aroundReceive$(Actor.scala:515)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	... 4 more
Caused by: java.lang.NoSuchMethodError: org.apache.commons.io.IOUtils.closeQuietly(Ljava/io/Closeable;)V
	at org.apache.flink.streaming.api.operators.StreamTaskStateInitializerImpl.operatorStateBackend(StreamTaskStateInitializerImpl.java:289)
	at org.apache.flink.streaming.api.operators.StreamTaskStateInitializerImpl.streamOperatorStateContext(StreamTaskStateInitializerImpl.java:173)
	at org.apache.flink.streaming.api.operators.AbstractStreamOperator.initializeState(AbstractStreamOperator.java:272)
	at org.apache.flink.streaming.runtime.tasks.OperatorChain.initializeStateAndOpenOperators(OperatorChain.java:427)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.lambda$beforeInvoke$2(StreamTask.java:543)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$1.runThrowing(StreamTaskActionExecutor.java:50)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.beforeInvoke(StreamTask.java:533)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:573)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:755)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:570)
	at java.lang.Thread.run(Thread.java:748)


## java.lang.NoSuchMethodError: javax.xml.parsers.DocumentBuilder.parse
2024-01-25 14:01:31
org.apache.flink.runtime.JobException: Recovery is suppressed by org.apache.flink.runtime.executiongraph.failover.flip1.FixedDelayFullRestartBackoffTimeStrategy@42b03cd8
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.handleFailure(ExecutionFailureHandler.java:124)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getGlobalFailureHandlingResult(ExecutionFailureHandler.java:99)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getFailureHandlingResult(ExecutionFailureHandler.java:83)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.handleTaskFailure(DefaultScheduler.java:253)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.maybeHandleTaskFailure(DefaultScheduler.java:244)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.updateTaskExecutionStateInternal(DefaultScheduler.java:235)
	at org.apache.flink.runtime.scheduler.SchedulerBase.updateTaskExecutionState(SchedulerBase.java:674)
	at org.apache.flink.runtime.scheduler.SchedulerNG.updateTaskExecutionState(SchedulerNG.java:91)
	at org.apache.flink.runtime.jobmaster.JobMaster.updateTaskExecutionState(JobMaster.java:471)
	at sun.reflect.GeneratedMethodAccessor36.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcInvocation(AkkaRpcActor.java:305)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:212)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)
Caused by: org.springframework.beans.factory.BeanDefinitionStoreException: Unexpected exception parsing XML document from URL [jar:file:/data1/hadoop/yarn/nm-local-dir/usercache/hadoop-cloudsearch-data-bjsearch/appcache/application_1705476120112_336707/blobStore-for-permanentBlobCache/job_c1c9201dca10dc82630a52c5369aad00/blob_p-3133614861af8b47bce5f369b00dfe5afdd1d50d-1281e0c121e6a969bd6345351df2b5f4!/uds-client-prod.xml]; nested exception is java.lang.NoSuchMethodError: javax.xml.parsers.DocumentBuilder.parse(Lorg/xml/sax/InputSource;)Lcom/sankuai/search/relocation/org/w3c/dom/Document;
	at org.springframework.beans.factory.xml.XmlBeanDefinitionReader.doLoadBeanDefinitions(XmlBeanDefinitionReader.java:414)
	at org.springframework.beans.factory.xml.XmlBeanDefinitionReader.loadBeanDefinitions(XmlBeanDefinitionReader.java:336)
	at org.springframework.beans.factory.xml.XmlBeanDefinitionReader.loadBeanDefinitions(XmlBeanDefinitionReader.java:304)
	at org.springframework.beans.factory.support.AbstractBeanDefinitionReader.loadBeanDefinitions(AbstractBeanDefinitionReader.java:181)
	at org.springframework.beans.factory.support.AbstractBeanDefinitionReader.loadBeanDefinitions(AbstractBeanDefinitionReader.java:217)
	at org.springframework.beans.factory.support.AbstractBeanDefinitionReader.loadBeanDefinitions(AbstractBeanDefinitionReader.java:188)
	at org.springframework.beans.factory.support.AbstractBeanDefinitionReader.loadBeanDefinitions(AbstractBeanDefinitionReader.java:252)
	at org.springframework.context.support.AbstractXmlApplicationContext.loadBeanDefinitions(AbstractXmlApplicationContext.java:127)
	at org.springframework.context.support.AbstractXmlApplicationContext.loadBeanDefinitions(AbstractXmlApplicationContext.java:93)
	at org.springframework.context.support.AbstractRefreshableApplicationContext.refreshBeanFactory(AbstractRefreshableApplicationContext.java:129)
	at org.springframework.context.support.AbstractApplicationContext.obtainFreshBeanFactory(AbstractApplicationContext.java:614)
	at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:515)
	at org.springframework.context.support.ClassPathXmlApplicationContext.<init>(ClassPathXmlApplicationContext.java:139)
	at org.springframework.context.support.ClassPathXmlApplicationContext.<init>(ClassPathXmlApplicationContext.java:83)
	at com.meituan.kugget.flink.job.function.sink.uds.UdsClosureClient.open(UdsClosureClient.java:119)
	at com.meituan.kugget.flink.job.function.sink.uds.UdsSinkFunction.open(UdsSinkFunction.java:41)
	at org.apache.flink.api.common.functions.util.FunctionUtils.openFunction(FunctionUtils.java:34)
	at org.apache.flink.streaming.api.operators.AbstractUdfStreamOperator.open(AbstractUdfStreamOperator.java:102)
	at org.apache.flink.streaming.api.operators.StreamSink.open(StreamSink.java:46)
	at org.apache.flink.streaming.runtime.tasks.OperatorChain.initializeStateAndOpenOperators(OperatorChain.java:478)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.lambda$beforeInvoke$2(StreamTask.java:547)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$SynchronizedStreamTaskActionExecutor.runThrowing(StreamTaskActionExecutor.java:93)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.beforeInvoke(StreamTask.java:537)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:577)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)
Caused by: java.lang.NoSuchMethodError: javax.xml.parsers.DocumentBuilder.parse(Lorg/xml/sax/InputSource;)Lcom/sankuai/search/relocation/org/w3c/dom/Document;
	at org.springframework.beans.factory.xml.DefaultDocumentLoader.loadDocument(DefaultDocumentLoader.java:76)
	at org.springframework.beans.factory.xml.XmlBeanDefinitionReader.doLoadDocument(XmlBeanDefinitionReader.java:429)
	at org.springframework.beans.factory.xml.XmlBeanDefinitionReader.doLoadBeanDefinitions(XmlBeanDefinitionReader.java:391)
	... 26 more



## json字符串 转 flink table
```
结论：不修复，日志还有其他问题，解决其他问题即可，不影响任务执行

sink - 修复NoClassDefFoundError com/sankuai/inf/dayu/dye/routing/core/utils/Close
 <dependency>
            <groupId>com.sankuai.inf.dayu</groupId>
            <artifactId>dye-routing-all</artifactId>
            <version>1.0.8</version>
        </dependency>

The program finished with the following exception:
2024-03-22 15:48:22,253 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: An input of GenericTypeInfo<Row> cannot be converted to Table. Please specify the type of the input with a RowTypeInfo.
2024-03-22 15:48:22,256 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-03-22 15:48:22,258 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-03-22 15:48:22,261 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-03-22 15:48:22,263 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-03-22 15:48:22,266 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-03-22 15:48:22,269 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-03-22 15:48:22,271 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-03-22 15:48:22,274 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-03-22 15:48:22,277 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-03-22 15:48:22,279 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-03-22 15:48:22,282 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-03-22 15:48:22,285 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-03-22 15:48:22,287 [INFO] Caused by: org.apache.flink.table.api.ValidationException: An input of GenericTypeInfo<Row> cannot be converted to Table. Please specify the type of the input with a RowTypeInfo.
2024-03-22 15:48:22,290 [INFO] at org.apache.flink.table.typeutils.FieldInfoUtils.getFieldsInfo(FieldInfoUtils.java:215)
2024-03-22 15:48:22,292 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.lambda$asQueryOperation$4(StreamTableEnvironmentImpl.java:418)
2024-03-22 15:48:22,295 [INFO] at java.util.Optional.orElseGet(Optional.java:267)
2024-03-22 15:48:22,298 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.asQueryOperation(StreamTableEnvironmentImpl.java:418)
2024-03-22 15:48:22,300 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.fromDataStream(StreamTableEnvironmentImpl.java:241)
2024-03-22 15:48:22,303 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.createTemporaryView(StreamTableEnvironmentImpl.java:267)
2024-03-22 15:48:22,306 [INFO] at com.meituan.kugget.flink.job.executor.feature.StreamWithJsonFormatToFlinkTable.execute(StreamWithJsonFormatToFlinkTable.java:72)
2024-03-22 15:48:22,308 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-03-22 15:48:22,311 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-03-22 15:48:22,314 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-03-22 15:48:22,316 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-03-22 15:48:22,319 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-03-22 15:48:22,322 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-03-22 15:48:22,324 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-03-22 15:48:22,327 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-03-22 15:48:22,330 [INFO] ... 11 more
2024-03-22 15:48:22,332 [INFO] Exception in thread "Thread-12" java.lang.NoClassDefFoundError: com/sankuai/inf/dayu/dye/routing/core/utils/Close
2024-03-22 15:48:22,335 [INFO] at com.sankuai.inf.dayu.dye.routing.core.extension.ExtensionContext.close(ExtensionContext.java:64)
2024-03-22 15:48:22,338 [INFO] at com.sankuai.inf.dayu.dye.routing.core.DefaultDyeRoutingContext$1.run(DefaultDyeRoutingContext.java:66)
2024-03-22 15:48:22,340 [INFO] at java.lang.Thread.run(Thread.java:745)
2024-03-22 15:48:22,343 [INFO] Caused by: java.lang.ClassNotFoundException: com.sankuai.inf.dayu.dye.routing.core.utils.Close
2024-03-22 15:48:22,346 [INFO] at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
2024-03-22 15:48:22,348 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
2024-03-22 15:48:22,351 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
2024-03-22 15:48:22,354 [INFO] at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
2024-03-22 15:48:22,356 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
2024-03-22 15:48:22,359 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
2024-03-22 15:48:22,361 [INFO] ... 3 more




2024-03-22 17:40:47,821 [INFO] Exception in thread "Thread-12" java.lang.NoClassDefFoundError: com/sankuai/inf/dayu/dye/routing/core/utils/Close
2024-03-22 17:40:47,824 [INFO] at com.sankuai.inf.dayu.dye.routing.core.extension.ExtensionContext.close(ExtensionContext.java:64)
2024-03-22 17:40:47,826 [INFO] at com.sankuai.inf.dayu.dye.routing.core.DefaultDyeRoutingContext$1.run(DefaultDyeRoutingContext.java:66)
2024-03-22 17:40:47,829 [INFO] at java.lang.Thread.run(Thread.java:745)
2024-03-22 17:40:47,832 [INFO] Caused by: java.lang.ClassNotFoundException: com.sankuai.inf.dayu.dye.routing.core.utils.Close
2024-03-22 17:40:47,835 [INFO] at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
2024-03-22 17:40:47,837 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
2024-03-22 17:40:47,840 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
2024-03-22 17:40:47,843 [INFO] at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
2024-03-22 17:40:47,845 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
2024-03-22 17:40:47,848 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
2024-03-22 17:40:47,851 [INFO] ... 3 more





还有额外异常

2024-03-22 15:45:13,323 [INFO] Exception in thread "Thread-13" java.lang.NoClassDefFoundError: com/meituan/mafka/client/consumer/RunStatus
2024-03-22 15:45:13,326 [INFO] at com.meituan.mafka.client.consumer.DefaultConsumerProcessor.close(DefaultConsumerProcessor.java:1630)
2024-03-22 15:45:13,329 [INFO] at com.meituan.mafka.client.consumer.AbstractConsumerProcessor$ShutDownHook.run(AbstractConsumerProcessor.java:30)
2024-03-22 15:45:13,332 [INFO] Caused by: java.lang.ClassNotFoundException: com.meituan.mafka.client.consumer.RunStatus
2024-03-22 15:45:13,335 [INFO] at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
2024-03-22 15:45:13,338 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
2024-03-22 15:45:13,341 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
2024-03-22 15:45:13,344 [INFO] at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
2024-03-22 15:45:13,347 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
2024-03-22 15:45:13,350 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
2024-03-22 15:45:13,353 [INFO] ... 2 more

```


## The main method caused an error: null
```


2024-03-25 01:42:28,389 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: null
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-03-25 01:42:28,390 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-03-25 01:42:28,391 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-03-25 01:42:28,391 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-03-25 01:42:28,391 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-03-25 01:42:28,391 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-03-25 01:42:28,391 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-03-25 01:42:28,392 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-03-25 01:42:28,392 [INFO] Caused by: java.lang.IllegalArgumentException
2024-03-25 01:42:28,392 [INFO] at com.google.common.base.Preconditions.checkArgument(Preconditions.java:108)
2024-03-25 01:42:28,392 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.getExactOneInput(StageExecutor.java:61)
2024-03-25 01:42:28,392 [INFO] at com.meituan.kugget.flink.job.executor.feature.FlinkSQL.execute(FlinkSQL.java:42)
2024-03-25 01:42:28,393 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-03-25 01:42:28,393 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-03-25 01:42:28,393 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-03-25 01:42:28,393 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-03-25 01:42:28,393 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-03-25 01:42:28,394 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-03-25 01:42:28,394 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-03-25 01:42:28,394 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-03-25 01:42:28,394 [INFO] ... 11 more
2024-03-25 01:42:28,394 [INFO] Exception in thread "Thread-12" java.lang.NoClassDefFoundError: com/sankuai/inf/dayu/dye/routing/core/utils/Close
2024-03-25 01:42:28,395 [INFO] at com.sankuai.inf.dayu.dye.routing.core.extension.ExtensionContext.close(ExtensionContext.java:64)
2024-03-25 01:42:28,395 [INFO] at com.sankuai.inf.dayu.dye.routing.core.DefaultDyeRoutingContext$1.run(DefaultDyeRoutingContext.java:66)
2024-03-25 01:42:28,395 [INFO] at java.lang.Thread.run(Thread.java:745)
2024-03-25 01:42:28,395 [INFO] Caused by: java.lang.ClassNotFoundException: com.sankuai.inf.dayu.dye.routing.core.utils.Close
2024-03-25 01:42:28,395 [INFO] at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
2024-03-25 01:42:28,396 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
2024-03-25 01:42:28,396 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
2024-03-25 01:42:28,396 [INFO] at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
2024-03-25 01:42:28,396 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
2024-03-25 01:42:28,396 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
2024-03-25 01:42:28,397 [INFO] ... 3 more
2024-03-25 01:42:28,763 [INFO] start kill process[50196] and subProcess...
2024-03-25 01:42:28,789 [INFO] ==========================Mon Mar 25 01:42:28 CST 2024==========================
2024-03-25 01:42:28,834 [INFO] process 50196 has finished.
2024-03-25 01:42:28,834 [INFO] ==========================kill process finish==========================
2024-03-25 01:42:28,835 [INFO] kill process[50196] and subProcess success,
2024-03-25 01:42:28,835 [INFO] exec [submit] command failed. shell exitCode=1
2024-03-25 01:42:28,835 [INFO] submit job[daocan_seckill_1711107166330] to yarn application[application_1706167263224_5142839] failed.
2024-03-25 01:42:28,835 [INFO] submit job[daocan_seckill_1711107166330] failed.
2024-03-25 01:42:29,843 [INFO] {"result":{"applicationID":"application_1706167263224_5142839","flinkInnerJob":null,"jobName":"daocan_seckill_1711107166330","state":"RUNNING","trackingUrl":"http://hlsc-data-hdp-rm-rtflinkha01.sankuai.com:8088/proxy/application_1706167263224_5142839/"}}
2024-03-25 01:42:29,858 [INFO] finished to submit jar for job {daocan_seckill_1711107166330}
2024-03-25 01:42:29,859 [INFO] start update flink job[daocan_seckill_1711107166330] queue...
2024-03-25 01:42:29,871 [INFO] start update flink job[daocan_seckill_1711107166330] running status......
2024-03-25 01:42:29,884 [INFO] flink_running_status.tracking_url: http://hlsc-data-hdp-rm-rtflinkha01.sankuai.com:8088/proxy/application_1706167263224_5142839/
2024-03-25 01:42:29,891 [INFO] job.tracking_url: http://hlsc-data-hdp-rm-rtflinkha01.sankuai.com:8088/proxy/application_1706167263224_5142839/
2024-03-25 01:42:29,891 [INFO] start log error
2024-03-25 01:42:29,892 [ERROR] deploy job[daocan_seckill_1711107166330] failed!!! flinkInnerJob is null
```


## Make sure a planner module is on the classpath
```
结论 本地调试问题，跳过

org.apache.flink.table.api.TableException: Could not instantiate the executor. Make sure a planner module is on the classpath

	at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.lookupExecutor(StreamTableEnvironmentImpl.java:176)
	at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.create(StreamTableEnvironmentImpl.java:138)
	at org.apache.flink.table.api.bridge.java.StreamTableEnvironment.create(StreamTableEnvironment.java:113)
	at org.apache.flink.table.api.bridge.java.StreamTableEnvironment.create(StreamTableEnvironment.java:85)
	at com.meituan.kugget.flink.job.executor.feature.JsonTest.testMafkaJson(JsonTest.java:222)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:47)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:325)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:78)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:57)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:290)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:71)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:288)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:58)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:268)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:69)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater$1.execute(IdeaTestRunner.java:38)
	at com.intellij.rt.execution.junit.TestsRepeater.repeat(TestsRepeater.java:11)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:35)
	at com.intellij.rt.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:235)
	at com.intellij.rt.junit.JUnitStarter.main(JUnitStarter.java:54)
Caused by: org.apache.flink.table.api.NoMatchingTableFactoryException: Could not find a suitable table factory for 'org.apache.flink.table.delegation.ExecutorFactory' in
the classpath.

Reason: No factory implements 'org.apache.flink.table.delegation.ExecutorFactory'.

The following properties are requested:
class-name=org.apache.flink.table.planner.delegation.BlinkExecutorFactory
streaming-mode=true

The following factories have been considered:
org.apache.flink.table.sources.CsvBatchTableSourceFactory
org.apache.flink.table.sources.CsvAppendTableSourceFactory
org.apache.flink.table.sinks.CsvBatchTableSinkFactory
org.apache.flink.table.sinks.CsvAppendTableSinkFactory
org.apache.flink.table.catalog.GenericInMemoryCatalogFactory
org.apache.flink.table.module.CoreModuleFactory
org.apache.flink.formats.json.JsonRowFormatFactory
org.apache.flink.streaming.connectors.kafka.Kafka010TableSourceSinkFactory
	at org.apache.flink.table.factories.TableFactoryService.filterByFactoryClass(TableFactoryService.java:216)
	at org.apache.flink.table.factories.TableFactoryService.filter(TableFactoryService.java:177)
	at org.apache.flink.table.factories.TableFactoryService.findAllInternal(TableFactoryService.java:165)
	at org.apache.flink.table.factories.TableFactoryService.findAll(TableFactoryService.java:122)
	at org.apache.flink.table.factories.ComponentFactoryService.find(ComponentFactoryService.java:50)
	at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.lookupExecutor(StreamTableEnvironmentImpl.java:167)
	... 28 more


Process finished with exit code 255


```


## java.lang.IllegalArgumentException: Hash collision on user-specified ID "mafka-source-id". Most likely cause is a non-unique ID. Please check that all IDs specified via `uid(String)` are unique.
```
原因
        return context.getEnvironment().addSource(consumer).uid("mafka-source-id");
输入两个mafka算子，这里没有做到唯一命名



The program finished with the following exception:
2024-03-25 03:30:52,683 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Hash collision on user-specified ID "mafka-source-id". Most likely cause is a non-unique ID. Please check that all IDs specified via `uid(String)` are unique.
2024-03-25 03:30:52,687 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-03-25 03:30:52,690 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-03-25 03:30:52,693 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-03-25 03:30:52,697 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-03-25 03:30:52,700 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-03-25 03:30:52,704 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-03-25 03:30:52,707 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-03-25 03:30:52,710 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-03-25 03:30:52,714 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-03-25 03:30:52,717 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-03-25 03:30:52,720 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-03-25 03:30:52,724 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-03-25 03:30:52,727 [INFO] Caused by: java.lang.IllegalArgumentException: Hash collision on user-specified ID "mafka-source-id". Most likely cause is a non-unique ID. Please check that all IDs specified via `uid(String)` are unique.
2024-03-25 03:30:52,731 [INFO] at org.apache.flink.streaming.api.graph.StreamGraphHasherV2.generateNodeHash(StreamGraphHasherV2.java:185)
2024-03-25 03:30:52,734 [INFO] at org.apache.flink.streaming.api.graph.StreamGraphHasherV2.traverseStreamGraphAndGenerateHashes(StreamGraphHasherV2.java:110)
2024-03-25 03:30:52,737 [INFO] at org.apache.flink.streaming.api.graph.StreamingJobGraphGenerator.createJobGraph(StreamingJobGraphGenerator.java:171)
2024-03-25 03:30:52,741 [INFO] at org.apache.flink.streaming.api.graph.StreamingJobGraphGenerator.createJobGraph(StreamingJobGraphGenerator.java:116)
2024-03-25 03:30:52,744 [INFO] at org.apache.flink.streaming.api.graph.StreamGraph.getJobGraph(StreamGraph.java:923)
2024-03-25 03:30:52,747 [INFO] at org.apache.flink.client.StreamGraphTranslator.translateToJobGraph(StreamGraphTranslator.java:50)
2024-03-25 03:30:52,751 [INFO] at org.apache.flink.client.FlinkPipelineTranslationUtil.getJobGraph(FlinkPipelineTranslationUtil.java:39)
2024-03-25 03:30:52,754 [INFO] at org.apache.flink.client.deployment.executors.PipelineExecutorUtils.getJobGraph(PipelineExecutorUtils.java:56)
2024-03-25 03:30:52,758 [INFO] at org.apache.flink.client.deployment.executors.AbstractSessionClusterExecutor.execute(AbstractSessionClusterExecutor.java:86)
2024-03-25 03:30:52,761 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.executeAsync(StreamExecutionEnvironment.java:1912)
2024-03-25 03:30:52,764 [INFO] at org.apache.flink.client.program.StreamContextEnvironment.executeAsync(StreamContextEnvironment.java:135)
2024-03-25 03:30:52,768 [INFO] at org.apache.flink.client.program.StreamContextEnvironment.execute(StreamContextEnvironment.java:76)
2024-03-25 03:30:52,771 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:1789)
2024-03-25 03:30:52,774 [INFO] at com.meituan.kugget.flink.job.context.TaskContext.execute(TaskContext.java:156)
2024-03-25 03:30:52,778 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:21)
2024-03-25 03:30:52,781 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-03-25 03:30:52,784 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-03-25 03:30:52,788 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-03-25 03:30:52,791 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-03-25 03:30:52,794 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-03-25 03:30:52,798 [INFO] ... 11 more
```


## NoMatchingTableFactoryException
```
参考
https://blog.csdn.net/qq_38363255/article/details/111320607

原因
SPI 找不到想要的接口

解决 参考flink源码配置
新增配置文件
/root/projects/kugget_job_executor/executor-flink/src/main/resources/META-INF/services/org.apache.flink.table.factories.TableFactory
添加下面
org.apache.flink.table.module.CoreModuleFactory
org.apache.flink.table.catalog.hive.factories.HiveCatalogFactory
org.apache.flink.table.sources.CsvBatchTableSourceFactory
org.apache.flink.table.sources.CsvAppendTableSourceFactory
org.apache.flink.table.sinks.CsvBatchTableSinkFactory
org.apache.flink.table.sinks.CsvAppendTableSinkFactory
org.apache.flink.formats.json.JsonRowFormatFactory
org.apache.flink.table.catalog.GenericInMemoryCatalogFactory
org.apache.flink.table.module.hive.HiveModuleFactory
org.apache.flink.streaming.connectors.kafka.Kafka01




org.apache.flink.table.api.NoMatchingTableFactoryException: Could not find a suitable table factory for 'org.apache.flink.table.delegation.ExecutorFactory' in
the classpath.

Reason: No factory implements 'org.apache.flink.table.delegation.ExecutorFactory'.

The following properties are requested:
class-name=org.apache.flink.table.planner.delegation.BlinkExecutorFactory
streaming-mode=true

The following factories have been considered:
org.apache.flink.table.sources.CsvBatchTableSourceFactory
org.apache.flink.table.sources.CsvAppendTableSourceFactory
org.apache.flink.table.sinks.CsvBatchTableSinkFactory
org.apache.flink.table.sinks.CsvAppendTableSinkFactory
org.apache.flink.formats.json.JsonRowFormatFactory
org.apache.flink.table.module.CoreModuleFactory
org.apache.flink.table.catalog.GenericInMemoryCatalogFactory
org.apache.flink.table.catalog.hive.factories.HiveCatalogFactory
org.apache.flink.table.module.hive.HiveModuleFactory
org.apache.flink.streaming.connectors.kafka.Kafka010TableSourceSinkFactory


```


##  Failed to create Hive Metastore client
```
原因 找不到hive配置
解决 复制flink源码测试用例的配置
同时缺少包
 org.datanucleus:datanucleus-api-jdo:jar:4.2.4:provided



org.apache.flink.table.catalog.exceptions.CatalogException: Failed to create Hive Metastore client

	at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:52)
	at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.createMetastoreClient(HiveMetastoreClientWrapper.java:274)
	at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.<init>(HiveMetastoreClientWrapper.java:79)
	at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientFactory.create(HiveMetastoreClientFactory.java:32)
	at org.apache.flink.table.catalog.hive.HiveCatalog.open(HiveCatalog.java:265)
	at org.apache.flink.table.catalog.CatalogManager.registerCatalog(CatalogManager.java:186)
	at org.apache.flink.table.api.internal.TableEnvironmentImpl.registerCatalog(TableEnvironmentImpl.java:351)
	at com.meituan.kugget.flink.job.executor.hive.HiveTest.setup(HiveTest.java:65)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:47)
	at org.junit.internal.runners.statements.RunBefores.evaluate(RunBefores.java:24)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:69)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater$1.execute(IdeaTestRunner.java:38)
	at com.intellij.rt.execution.junit.TestsRepeater.repeat(TestsRepeater.java:11)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:35)
	at com.intellij.rt.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:235)
	at com.intellij.rt.junit.JUnitStarter.main(JUnitStarter.java:54)
Caused by: java.lang.reflect.InvocationTargetException
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:50)
	... 23 more
Caused by: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.metastore.HiveMetaStoreClient
	at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1708)
	at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.<init>(RetryingMetaStoreClient.java:83)
	at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:133)
	at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:89)
	... 28 more
Caused by: java.lang.reflect.InvocationTargetException
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1706)
	... 31 more
Caused by: MetaException(message:Class org.datanucleus.api.jdo.JDOPersistenceManagerFactory was not found.)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.<init>(RetryingHMSHandler.java:83)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.getProxy(RetryingHMSHandler.java:92)
	at org.apache.hadoop.hive.metastore.HiveMetaStore.newRetryingHMSHandler(HiveMetaStore.java:6891)
	at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.<init>(HiveMetaStoreClient.java:164)
	... 36 more
Caused by: MetaException(message:Class org.datanucleus.api.jdo.JDOPersistenceManagerFactory was not found.)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.invokeInternal(RetryingHMSHandler.java:211)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.invoke(RetryingHMSHandler.java:107)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.<init>(RetryingHMSHandler.java:79)
	... 39 more
Caused by: javax.jdo.JDOFatalUserException: Class org.datanucleus.api.jdo.JDOPersistenceManagerFactory was not found.
NestedThrowables:
java.lang.ClassNotFoundException: org.datanucleus.api.jdo.JDOPersistenceManagerFactory
	at javax.jdo.JDOHelper.invokeGetPersistenceManagerFactoryOnImplementation(JDOHelper.java:1175)
	at javax.jdo.JDOHelper.getPersistenceManagerFactory(JDOHelper.java:808)
	at javax.jdo.JDOHelper.getPersistenceManagerFactory(JDOHelper.java:701)
	at org.apache.hadoop.hive.metastore.ObjectStore.getPMF(ObjectStore.java:519)
	at org.apache.hadoop.hive.metastore.ObjectStore.getPersistenceManager(ObjectStore.java:548)
	at org.apache.hadoop.hive.metastore.ObjectStore.initializeHelper(ObjectStore.java:403)
	at org.apache.hadoop.hive.metastore.ObjectStore.initialize(ObjectStore.java:340)
	at org.apache.hadoop.hive.metastore.ObjectStore.setConf(ObjectStore.java:301)
	at org.apache.hadoop.util.ReflectionUtils.setConf(ReflectionUtils.java:76)
	at org.apache.hadoop.util.ReflectionUtils.newInstance(ReflectionUtils.java:136)
	at org.apache.hadoop.hive.metastore.RawStoreProxy.<init>(RawStoreProxy.java:58)
	at org.apache.hadoop.hive.metastore.RawStoreProxy.getProxy(RawStoreProxy.java:67)
	at org.apache.hadoop.hive.metastore.HiveMetaStore$HMSHandler.newRawStoreForConf(HiveMetaStore.java:628)
	at org.apache.hadoop.hive.metastore.HiveMetaStore$HMSHandler.getMSForConf(HiveMetaStore.java:594)
	at org.apache.hadoop.hive.metastore.HiveMetaStore$HMSHandler.getMS(HiveMetaStore.java:588)
	at org.apache.hadoop.hive.metastore.HiveMetaStore$HMSHandler.createDefaultDB(HiveMetaStore.java:659)
	at org.apache.hadoop.hive.metastore.HiveMetaStore$HMSHandler.init(HiveMetaStore.java:431)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.hadoop.hive.metastore.RetryingHMSHandler.invokeInternal(RetryingHMSHandler.java:148)
	... 41 more
Caused by: java.lang.ClassNotFoundException: org.datanucleus.api.jdo.JDOPersistenceManagerFactory
	at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	at java.lang.Class.forName0(Native Method)
	at java.lang.Class.forName(Class.java:348)
	at javax.jdo.JDOHelper$18.run(JDOHelper.java:2018)
	at javax.jdo.JDOHelper$18.run(JDOHelper.java:2016)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.jdo.JDOHelper.forName(JDOHelper.java:2015)
	at javax.jdo.JDOHelper.invokeGetPersistenceManagerFactoryOnImplementation(JDOHelper.java:1162)
	... 62 more


```


## No operators defined in streaming topology. Cannot generate StreamGraph.
```

源码分析看，是一定要有transformations 
        if (transformations.size() <= 0) {
            throw new IllegalStateException(
                    "No operators defined in streaming topology. Cannot generate StreamGraph.");
        }

2024-04-02 01:14:15,987 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: No operators defined in streaming topology. Cannot generate StreamGraph.
2024-04-02 01:14:15,990 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-02 01:14:15,993 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 01:14:15,996 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 01:14:15,999 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 01:14:16,002 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 01:14:16,004 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 01:14:16,007 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 01:14:16,010 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 01:14:16,013 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 01:14:16,016 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 01:14:16,019 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 01:14:16,022 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 01:14:16,025 [INFO] Caused by: java.lang.IllegalStateException: No operators defined in streaming topology. Cannot generate StreamGraph.
2024-04-02 01:14:16,027 [INFO] at org.apache.flink.table.planner.utils.ExecutorUtils.generateStreamGraph(ExecutorUtils.java:42)
2024-04-02 01:14:16,030 [INFO] at org.apache.flink.table.planner.delegation.StreamExecutor.createPipeline(StreamExecutor.java:50)
2024-04-02 01:14:16,033 [INFO] at org.apache.flink.table.api.internal.TableEnvironmentImpl.execute(TableEnvironmentImpl.java:1276)
2024-04-02 01:14:16,036 [INFO] at com.meituan.kugget.flink.job.context.TaskContext.execute(TaskContext.java:160)
2024-04-02 01:14:16,039 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:21)
2024-04-02 01:14:16,042 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 01:14:16,045 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 01:14:16,048 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 01:14:16,050 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 01:14:16,053 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 01:14:16,056 [INFO] ... 11 more
2024-04-02 01:14:16,059 [INFO] ------------------------------------------------------------
2024-04-02 01:14:16,062 [INFO] The program finished with the following exception:
2024-04-02 01:14:16,065 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: No operators defined in streaming topology. Cannot generate StreamGraph.
2024-04-02 01:14:16,067 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-02 01:14:16,070 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 01:14:16,073 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 01:14:16,076 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 01:14:16,079 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 01:14:16,082 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 01:14:16,085 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 01:14:16,087 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 01:14:16,090 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 01:14:16,093 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 01:14:16,096 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 01:14:16,099 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 01:14:16,102 [INFO] Caused by: java.lang.IllegalStateException: No operators defined in streaming topology. Cannot generate StreamGraph.
2024-04-02 01:14:16,105 [INFO] at org.apache.flink.table.planner.utils.ExecutorUtils.generateStreamGraph(ExecutorUtils.java:42)
2024-04-02 01:14:16,108 [INFO] at org.apache.flink.table.planner.delegation.StreamExecutor.createPipeline(StreamExecutor.java:50)
2024-04-02 01:14:16,111 [INFO] at org.apache.flink.table.api.internal.TableEnvironmentImpl.execute(TableEnvironmentImpl.java:1276)
2024-04-02 01:14:16,114 [INFO] at com.meituan.kugget.flink.job.context.TaskContext.execute(TaskContext.java:160)
2024-04-02 01:14:16,117 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:21)
2024-04-02 01:14:16,120 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 01:14:16,122 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 01:14:16,125 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 01:14:16,128 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 01:14:16,131 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 01:14:16,134 [INFO] ... 11 more
2024-04-02 01:14:16,386 [INFO] start kill process[32161] and subProcess...
2024-04-02 01:14:16,420 [INFO] ==========================Tue Apr 2 01:14:16 CST 2024==========================
2024-04-02 01:14:16,490 [INFO] process 32161 has finished.
2024-04-02 01:14:16,493 [INFO] ==========================kill process finish==========================
2024-04-02 01:14:16,496 [INFO] kill process[32161] and subProcess success,
2024-04-02 01:14:16,499 [INFO] exec [submit] command failed. shell exitCode=1
2024-04-02 01:14:16,502 [INFO] submit job[flink_with_hive_1711988725406] to yarn application[application_1711348622573_317497] failed.
2024-04-02 01:14:16,505 [INFO] submit job[flink_with_hive_1711988725406] failed.
2024-04-02 01:14:17,517 [INFO] {"result":{"applicationID":"application_1711348622573_317497","flinkInnerJob":null,"jobName":"flink_with_hive_1711988725406","state":"RUNNING","trackingUrl":"http://hlsc-data-hdp-rm-rtflinkha01.sankuai.com:8088/proxy/application_1711348622573_317497/"}}
2024-04-02 01:14:17,540 [INFO] finished to submit jar for job {flink_with_hive_1711988725406}
2024-04-02 01:14:17,543 [INFO] start update flink job[flink_with_hive_1711988725406] queue...
2024-04-02 01:14:17,556 [INFO] start update flink job[flink_with_hive_1711988725406] running status......
2024-04-02 01:14:17,570 [INFO] flink_running_status.tracking_url: http://hlsc-data-hdp-rm-rtflinkha01.sankuai.com:8088/proxy/application_1711348622573_317497/






2024-04-02 10:12:05,880 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: No operators defined in streaming topology. Cannot execute.
2024-04-02 10:12:05,883 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-02 10:12:05,886 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 10:12:05,890 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 10:12:05,893 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 10:12:05,896 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 10:12:05,899 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 10:12:05,902 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 10:12:05,905 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 10:12:05,908 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 10:12:05,911 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 10:12:05,914 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 10:12:05,917 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 10:12:05,920 [INFO] Caused by: java.lang.IllegalStateException: No operators defined in streaming topology. Cannot execute.
2024-04-02 10:12:05,923 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.getStreamGraphGenerator(StreamExecutionEnvironment.java:1974)
2024-04-02 10:12:05,926 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.getStreamGraph(StreamExecutionEnvironment.java:1965)
2024-04-02 10:12:05,929 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.getStreamGraph(StreamExecutionEnvironment.java:1950)
2024-04-02 10:12:05,932 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:1789)
2024-04-02 10:12:05,935 [INFO] at com.meituan.kugget.flink.job.context.TaskContext.execute(TaskContext.java:161)
2024-04-02 10:12:05,938 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:21)
2024-04-02 10:12:05,941 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 10:12:05,944 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 10:12:05,947 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 10:12:05,950 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 10:12:05,953 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 10:12:05,956 [INFO] ... 11 more


```


## HiveCatalog 初始化失败
```





Trying to connect to metastore with URI thrift://hivemetastore.data.sankuai.com:9000
2024-04-02 11:15:09,926 [INFO] INFO  hive.metastore                                                - Opened a connection to metastore, current connections: 1
2024-04-02 11:15:09,990 [INFO] WARN  hive.metastore                                                - set_ugi() not successful, Likely cause: new client talking to old server. Continuing without it.
2024-04-02 11:15:09,991 [INFO] org.apache.thrift.transport.TTransportException
2024-04-02 11:15:09,991 [INFO] at org.apache.thrift.transport.TIOStreamTransport.read(TIOStreamTransport.java:132)
2024-04-02 11:15:09,991 [INFO] at org.apache.thrift.transport.TTransport.readAll(TTransport.java:86)
2024-04-02 11:15:09,991 [INFO] at org.apache.thrift.protocol.TBinaryProtocol.readStringBody(TBinaryProtocol.java:380)
2024-04-02 11:15:09,992 [INFO] at org.apache.thrift.protocol.TBinaryProtocol.readMessageBegin(TBinaryProtocol.java:230)
2024-04-02 11:15:09,992 [INFO] at org.apache.thrift.TServiceClient.receiveBase(TServiceClient.java:77)
2024-04-02 11:15:09,992 [INFO] at org.apache.hadoop.hive.metastore.api.ThriftHiveMetastore$Client.recv_set_ugi(ThriftHiveMetastore.java:4214)
2024-04-02 11:15:09,992 [INFO] at org.apache.hadoop.hive.metastore.api.ThriftHiveMetastore$Client.set_ugi(ThriftHiveMetastore.java:4200)
2024-04-02 11:15:09,992 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.open(HiveMetaStoreClient.java:498)
2024-04-02 11:15:09,993 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.access$000(HiveMetaStoreClient.java:94)
2024-04-02 11:15:09,993 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient$1.run(HiveMetaStoreClient.java:227)
2024-04-02 11:15:09,993 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient$1.run(HiveMetaStoreClient.java:224)
2024-04-02 11:15:09,993 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:15:09,994 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:15:09,994 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:15:09,994 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.<init>(HiveMetaStoreClient.java:223)
2024-04-02 11:15:09,994 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
2024-04-02 11:15:09,994 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
2024-04-02 11:15:09,995 [INFO] at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
2024-04-02 11:15:09,995 [INFO] at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
2024-04-02 11:15:09,995 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1706)
2024-04-02 11:15:09,995 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.<init>(RetryingMetaStoreClient.java:83)
2024-04-02 11:15:09,995 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:133)
2024-04-02 11:15:09,996 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:89)
2024-04-02 11:15:09,996 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:09,996 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:09,996 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:09,997 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:09,997 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:50)
2024-04-02 11:15:09,997 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.createMetastoreClient(HiveMetastoreClientWrapper.java:274)
2024-04-02 11:15:09,997 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.<init>(HiveMetastoreClientWrapper.java:80)
2024-04-02 11:15:09,997 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientFactory.create(HiveMetastoreClientFactory.java:32)
2024-04-02 11:15:09,998 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.open(HiveCatalog.java:265)
2024-04-02 11:15:09,998 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.mockHiveSource(HiveSource.java:81)
2024-04-02 11:15:09,998 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.execute(HiveSource.java:52)
2024-04-02 11:15:09,998 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-02 11:15:09,998 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-02 11:15:09,999 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-02 11:15:09,999 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:09,999 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:09,999 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:09,999 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,000 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 11:15:10,000 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 11:15:10,000 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 11:15:10,000 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 11:15:10,000 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 11:15:10,001 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 11:15:10,001 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 11:15:10,001 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:15:10,001 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:15:10,002 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:15:10,002 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 11:15:10,002 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 11:15:10,003 [INFO] INFO  hive.metastore                                                - Connected to metastore.
2024-04-02 11:15:10,003 [INFO] ERROR hive.metastore                                                - Error while setting delegation token for hadoop-cloudsearch-data-bjsearch
2024-04-02 11:15:10,003 [INFO] org.apache.thrift.transport.TTransportException
2024-04-02 11:15:10,003 [INFO] at org.apache.thrift.transport.TIOStreamTransport.read(TIOStreamTransport.java:132)
2024-04-02 11:15:10,003 [INFO] at org.apache.thrift.transport.TTransport.readAll(TTransport.java:86)
2024-04-02 11:15:10,004 [INFO] at org.apache.thrift.protocol.TBinaryProtocol.readAll(TBinaryProtocol.java:429)
2024-04-02 11:15:10,004 [INFO] at org.apache.thrift.protocol.TBinaryProtocol.readI32(TBinaryProtocol.java:318)
2024-04-02 11:15:10,004 [INFO] at org.apache.thrift.protocol.TBinaryProtocol.readMessageBegin(TBinaryProtocol.java:219)
2024-04-02 11:15:10,005 [INFO] at org.apache.thrift.TServiceClient.receiveBase(TServiceClient.java:77)
2024-04-02 11:15:10,005 [INFO] at org.apache.hadoop.hive.metastore.api.ThriftHiveMetastore$Client.recv_get_delegation_token(ThriftHiveMetastore.java:4241)
2024-04-02 11:15:10,005 [INFO] at org.apache.hadoop.hive.metastore.api.ThriftHiveMetastore$Client.get_delegation_token(ThriftHiveMetastore.java:4227)
2024-04-02 11:15:10,005 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.getDelegationToken(HiveMetaStoreClient.java:2042)
2024-04-02 11:15:10,005 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.<init>(HiveMetaStoreClient.java:232)
2024-04-02 11:15:10,006 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
2024-04-02 11:15:10,006 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
2024-04-02 11:15:10,006 [INFO] at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
2024-04-02 11:15:10,006 [INFO] at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
2024-04-02 11:15:10,006 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1706)
2024-04-02 11:15:10,007 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.<init>(RetryingMetaStoreClient.java:83)
2024-04-02 11:15:10,007 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:133)
2024-04-02 11:15:10,007 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:89)
2024-04-02 11:15:10,007 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,007 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,008 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,008 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,008 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:50)
2024-04-02 11:15:10,008 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.createMetastoreClient(HiveMetastoreClientWrapper.java:274)
2024-04-02 11:15:10,008 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.<init>(HiveMetastoreClientWrapper.java:80)
2024-04-02 11:15:10,009 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientFactory.create(HiveMetastoreClientFactory.java:32)
2024-04-02 11:15:10,009 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.open(HiveCatalog.java:265)
2024-04-02 11:15:10,009 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.mockHiveSource(HiveSource.java:81)
2024-04-02 11:15:10,009 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.execute(HiveSource.java:52)
2024-04-02 11:15:10,009 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-02 11:15:10,010 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-02 11:15:10,010 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-02 11:15:10,010 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,010 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,010 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,011 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,011 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 11:15:10,011 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 11:15:10,011 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 11:15:10,011 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 11:15:10,012 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 11:15:10,012 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 11:15:10,012 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 11:15:10,012 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:15:10,012 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:15:10,013 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:15:10,013 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 11:15:10,013 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 11:15:10,013 [INFO] ERROR org.apache.flink.client.cli.CliFrontend                       - Error while running the command.
2024-04-02 11:15:10,013 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Failed to create Hive Metastore client
2024-04-02 11:15:10,014 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-02 11:15:10,014 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 11:15:10,014 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 11:15:10,014 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 11:15:10,014 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 11:15:10,015 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 11:15:10,015 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 11:15:10,015 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:15:10,015 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:15:10,016 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:15:10,016 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 11:15:10,016 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 11:15:10,016 [INFO] Caused by: org.apache.flink.table.catalog.exceptions.CatalogException: Failed to create Hive Metastore client
2024-04-02 11:15:10,016 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:52)
2024-04-02 11:15:10,017 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.createMetastoreClient(HiveMetastoreClientWrapper.java:274)
2024-04-02 11:15:10,017 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.<init>(HiveMetastoreClientWrapper.java:80)
2024-04-02 11:15:10,017 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientFactory.create(HiveMetastoreClientFactory.java:32)
2024-04-02 11:15:10,017 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.open(HiveCatalog.java:265)
2024-04-02 11:15:10,017 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.mockHiveSource(HiveSource.java:81)
2024-04-02 11:15:10,018 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.execute(HiveSource.java:52)
2024-04-02 11:15:10,018 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-02 11:15:10,018 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-02 11:15:10,018 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-02 11:15:10,019 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,019 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,019 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,019 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,019 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 11:15:10,020 [INFO] ... 11 more
2024-04-02 11:15:10,020 [INFO] Caused by: java.lang.reflect.InvocationTargetException
2024-04-02 11:15:10,020 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,020 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,020 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,021 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,021 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:50)
2024-04-02 11:15:10,021 [INFO] ... 25 more
2024-04-02 11:15:10,022 [INFO] Caused by: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.metastore.HiveMetaStoreClient
2024-04-02 11:15:10,022 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1708)
2024-04-02 11:15:10,022 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.<init>(RetryingMetaStoreClient.java:83)
2024-04-02 11:15:10,022 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:133)
2024-04-02 11:15:10,022 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:89)
2024-04-02 11:15:10,023 [INFO] ... 30 more
2024-04-02 11:15:10,023 [INFO] Caused by: java.lang.reflect.InvocationTargetException
2024-04-02 11:15:10,023 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
2024-04-02 11:15:10,023 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
2024-04-02 11:15:10,023 [INFO] at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
2024-04-02 11:15:10,024 [INFO] at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
2024-04-02 11:15:10,024 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1706)
2024-04-02 11:15:10,024 [INFO] ... 33 more
2024-04-02 11:15:10,024 [INFO] Caused by: MetaException(message:null)
2024-04-02 11:15:10,024 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.<init>(HiveMetaStoreClient.java:242)
2024-04-02 11:15:10,025 [INFO] ... 38 more
2024-04-02 11:15:10,025 [INFO] ------------------------------------------------------------
2024-04-02 11:15:10,025 [INFO] The program finished with the following exception:
2024-04-02 11:15:10,025 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Failed to create Hive Metastore client
2024-04-02 11:15:10,025 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-02 11:15:10,026 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 11:15:10,026 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 11:15:10,026 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 11:15:10,026 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 11:15:10,026 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 11:15:10,027 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 11:15:10,027 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:15:10,027 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:15:10,027 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:15:10,027 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 11:15:10,028 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 11:15:10,028 [INFO] Caused by: org.apache.flink.table.catalog.exceptions.CatalogException: Failed to create Hive Metastore client
2024-04-02 11:15:10,028 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:52)
2024-04-02 11:15:10,028 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.createMetastoreClient(HiveMetastoreClientWrapper.java:274)
2024-04-02 11:15:10,028 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientWrapper.<init>(HiveMetastoreClientWrapper.java:80)
2024-04-02 11:15:10,029 [INFO] at org.apache.flink.table.catalog.hive.client.HiveMetastoreClientFactory.create(HiveMetastoreClientFactory.java:32)
2024-04-02 11:15:10,029 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.open(HiveCatalog.java:265)
2024-04-02 11:15:10,029 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.mockHiveSource(HiveSource.java:81)
2024-04-02 11:15:10,029 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.execute(HiveSource.java:52)
2024-04-02 11:15:10,029 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-02 11:15:10,030 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-02 11:15:10,030 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-02 11:15:10,030 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,030 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,030 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,031 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,031 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 11:15:10,031 [INFO] ... 11 more
2024-04-02 11:15:10,031 [INFO] Caused by: java.lang.reflect.InvocationTargetException
2024-04-02 11:15:10,032 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:15:10,032 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:15:10,032 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:15:10,032 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:15:10,032 [INFO] at org.apache.flink.table.catalog.hive.client.HiveShimV230.getHiveMetastoreClient(HiveShimV230.java:50)
2024-04-02 11:15:10,033 [INFO] ... 25 more
2024-04-02 11:15:10,033 [INFO] Caused by: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.metastore.HiveMetaStoreClient
2024-04-02 11:15:10,033 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1708)
2024-04-02 11:15:10,033 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.<init>(RetryingMetaStoreClient.java:83)
2024-04-02 11:15:10,034 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:133)
2024-04-02 11:15:10,034 [INFO] at org.apache.hadoop.hive.metastore.RetryingMetaStoreClient.getProxy(RetryingMetaStoreClient.java:89)
2024-04-02 11:15:10,034 [INFO] ... 30 more
2024-04-02 11:15:10,034 [INFO] Caused by: java.lang.reflect.InvocationTargetException
2024-04-02 11:15:10,034 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
2024-04-02 11:15:10,035 [INFO] at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
2024-04-02 11:15:10,035 [INFO] at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
2024-04-02 11:15:10,035 [INFO] at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
2024-04-02 11:15:10,035 [INFO] at org.apache.hadoop.hive.metastore.MetaStoreUtils.newInstance(MetaStoreUtils.java:1706)
2024-04-02 11:15:10,035 [INFO] ... 33 more
2024-04-02 11:15:10,036 [INFO] Caused by: MetaException(message:null)
2024-04-02 11:15:10,036 [INFO] at org.apache.hadoop.hive.metastore.HiveMetaStoreClient.<init>(HiveMetaStoreClient.java:242)
2024-04-02 11:15:10,036 [INFO] ... 38 more
2024-04-02 11:15:10,398 [INFO] start kill process[11433] and subProcess...
2024-04-02 11:15:10,424 [INFO] ==========================Tue Apr 2 11:15:10 CST 2024==========================
2024-04-02 11:15:10,469 [INFO] process 11433 has finished.
2024-04-02 11:15:10,469 [INFO] ==========================kill process finish==========================










2024-04-02 11:06:36,683 [INFO] INFO  org.apache.flink.table.catalog.hive.HiveCatalog               - Created HiveCatalog 'hive'
2024-04-02 11:06:36,686 [INFO] java.lang.NullPointerException
2024-04-02 11:06:36,689 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.getHiveTable(HiveCatalog.java:667)
2024-04-02 11:06:36,693 [INFO] at org.apache.flink.table.catalog.hive.HiveCatalog.getTable(HiveCatalog.java:428)
2024-04-02 11:06:36,695 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.getTableSource(HiveSource.java:109)
2024-04-02 11:06:36,699 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.mockHiveSource(HiveSource.java:85)
2024-04-02 11:06:36,702 [INFO] at com.meituan.kugget.flink.job.executor.source.HiveSource.execute(HiveSource.java:52)
2024-04-02 11:06:36,705 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-02 11:06:36,708 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-02 11:06:36,711 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-02 11:06:36,714 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-02 11:06:36,717 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-02 11:06:36,720 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-02 11:06:36,723 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-02 11:06:36,725 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-02 11:06:36,728 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-02 11:06:36,731 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-02 11:06:36,734 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-02 11:06:36,737 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-02 11:06:36,740 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-02 11:06:36,743 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-02 11:06:36,746 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-02 11:06:36,749 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-02 11:06:36,752 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-02 11:06:36,755 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-02 11:06:36,758 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-02 11:06:36,761 [INFO] INFO  com.meituan.kugget.flink.job.context.StageLooper              - Execute done:HiveSource:NOD1774833831929581568
2024-04-02 11:06:36,764 [INFO] INFO  com.meituan.kugget.flink.job.context.TaskContext              - execute job: flink_with_hive_1711988725406

```


## set offset failed,
```

mafkaa版本问题

2024-04-08 15:03:43
java.lang.RuntimeException: Mafka consumer set offset failed. Failed topics and reason: set offset failed, reason:  BrokerAPI.commitOffsetToKafkaWithGenerationIdOfBroker exception,topic:[mafka.waimai.ad.poitob.poi.update_prod],group:[supplycenter.shangou.poi.realtime],groupAppkey:[com.sankuai.dataapp.data.supplypool],cluster:[txbj-mafka2-waimaidrill]partitionAndOffsetInfo:{{}:{},{}:{},{}:{},{}:{},{}:{},{}:{}}

	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.checkSetOffsetSuccess(MafkaFetcher.java:526)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.setOffsetForCommonConsumer(MafkaFetcher.java:414)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.setOffsetForConsumer(MafkaFetcher.java:334)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.createMafkaConsumer(MafkaFetcher.java:265)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.<init>(MafkaFetcher.java:99)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaConsumer.run(FlinkMafkaConsumer.java:192)
	at org.apache.flink.streaming.api.operators.StreamSource.run(StreamSource.java:110)
	at org.apache.flink.streaming.api.operators.StreamSource.run(StreamSource.java:66)
	at org.apache.flink.streaming.runtime.tasks.SourceStreamTask$LegacySourceFunctionThread.run(SourceStreamTask.java:263)


```


## Unable to instantiate java compiler
```
provided级别 flink相关包，不要包含janin的相关


2024-04-09 15:32:02,948 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Unable to instantiate java compiler
2024-04-09 15:32:02,951 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-09 15:32:02,953 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-09 15:32:02,956 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-09 15:32:02,959 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-09 15:32:02,961 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-09 15:32:02,964 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-09 15:32:02,967 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-09 15:32:02,969 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-09 15:32:02,972 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-09 15:32:02,975 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-09 15:32:02,978 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-09 15:32:02,980 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-09 15:32:02,983 [INFO] Caused by: java.lang.IllegalStateException: Unable to instantiate java compiler
2024-04-09 15:32:02,986 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:428)
2024-04-09 15:32:02,989 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.load3(JaninoRelMetadataProvider.java:374)
2024-04-09 15:32:02,991 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.lambda$static$0(JaninoRelMetadataProvider.java:109)
2024-04-09 15:32:02,994 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.CacheLoader$FunctionToCacheLoader.load(CacheLoader.java:165)
2024-04-09 15:32:02,997 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LoadingValueReference.loadFuture(LocalCache.java:3529)
2024-04-09 15:32:02,999 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.loadSync(LocalCache.java:2278)
2024-04-09 15:32:03,002 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.lockedGetOrLoad(LocalCache.java:2155)
2024-04-09 15:32:03,005 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.get(LocalCache.java:2045)
2024-04-09 15:32:03,007 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.get(LocalCache.java:3951)
2024-04-09 15:32:03,010 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.getOrLoad(LocalCache.java:3974)
2024-04-09 15:32:03,013 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LocalLoadingCache.get(LocalCache.java:4958)
2024-04-09 15:32:03,016 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.create(JaninoRelMetadataProvider.java:469)
2024-04-09 15:32:03,018 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.revise(JaninoRelMetadataProvider.java:481)
2024-04-09 15:32:03,021 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQueryBase.revise(RelMetadataQueryBase.java:95)
2024-04-09 15:32:03,024 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQuery.getPulledUpPredicates(RelMetadataQuery.java:784)
2024-04-09 15:32:03,026 [INFO] at org.apache.calcite.rel.rules.ReduceExpressionsRule$FilterReduceExpressionsRule.onMatch(ReduceExpressionsRule.java:151)
2024-04-09 15:32:03,029 [INFO] at org.apache.calcite.plan.AbstractRelOptPlanner.fireRule(AbstractRelOptPlanner.java:333)
2024-04-09 15:32:03,032 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRule(HepPlanner.java:542)
2024-04-09 15:32:03,035 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRules(HepPlanner.java:407)
2024-04-09 15:32:03,037 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeInstruction(HepPlanner.java:243)
2024-04-09 15:32:03,040 [INFO] at org.apache.calcite.plan.hep.HepInstruction$RuleInstance.execute(HepInstruction.java:127)
2024-04-09 15:32:03,043 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeProgram(HepPlanner.java:202)
2024-04-09 15:32:03,045 [INFO] at org.apache.calcite.plan.hep.HepPlanner.findBestExp(HepPlanner.java:189)
2024-04-09 15:32:03,048 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepProgram.optimize(FlinkHepProgram.scala:69)
2024-04-09 15:32:03,051 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepRuleSetProgram.optimize(FlinkHepRuleSetProgram.scala:87)
2024-04-09 15:32:03,053 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:62)
2024-04-09 15:32:03,056 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:58)
2024-04-09 15:32:03,059 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2024-04-09 15:32:03,062 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2024-04-09 15:32:03,064 [INFO] at scala.collection.Iterator$class.foreach(Iterator.scala:891)
2024-04-09 15:32:03,067 [INFO] at scala.collection.AbstractIterator.foreach(Iterator.scala:1334)
2024-04-09 15:32:03,070 [INFO] at scala.collection.IterableLike$class.foreach(IterableLike.scala:72)
2024-04-09 15:32:03,073 [INFO] at scala.collection.AbstractIterable.foreach(Iterable.scala:54)
2024-04-09 15:32:03,075 [INFO] at scala.collection.TraversableOnce$class.foldLeft(TraversableOnce.scala:157)
2024-04-09 15:32:03,078 [INFO] at scala.collection.AbstractTraversable.foldLeft(Traversable.scala:104)
2024-04-09 15:32:03,081 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram.optimize(FlinkChainedProgram.scala:57)
2024-04-09 15:32:03,084 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.optimizeTree(StreamCommonSubGraphBasedOptimizer.scala:163)
2024-04-09 15:32:03,086 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.doOptimize(StreamCommonSubGraphBasedOptimizer.scala:79)
2024-04-09 15:32:03,089 [INFO] at org.apache.flink.table.planner.plan.optimize.CommonSubGraphBasedOptimizer.optimize(CommonSubGraphBasedOptimizer.scala:83)
2024-04-09 15:32:03,092 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.optimize(PlannerBase.scala:287)
2024-04-09 15:32:03,094 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.translate(PlannerBase.scala:160)
2024-04-09 15:32:03,097 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toDataStream(StreamTableEnvironmentImpl.java:357)
2024-04-09 15:32:03,100 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toRetractStream(StreamTableEnvironmentImpl.java:332)
2024-04-09 15:32:03,103 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toRetractStream(StreamTableEnvironmentImpl.java:321)
2024-04-09 15:32:03,105 [INFO] at com.meituan.kugget.flink.job.executor.feature.FlinkTableToStreamWithJsonFormat.execute(FlinkTableToStreamWithJsonFormat.java:48)
2024-04-09 15:32:03,108 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-09 15:32:03,111 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-09 15:32:03,113 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-09 15:32:03,116 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-09 15:32:03,119 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-09 15:32:03,121 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-09 15:32:03,124 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-09 15:32:03,127 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-09 15:32:03,130 [INFO] ... 11 more
2024-04-09 15:32:03,132 [INFO] Caused by: java.lang.ClassCastException: org.codehaus.janino.CompilerFactory cannot be cast to org.codehaus.commons.compiler.ICompilerFactory
2024-04-09 15:32:03,135 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getCompilerFactory(CompilerFactoryFactory.java:129)
2024-04-09 15:32:03,138 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getDefaultCompilerFactory(CompilerFactoryFactory.java:79)
2024-04-09 15:32:03,140 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:426)
2024-04-09 15:32:03,143 [INFO] ... 63 more
2024-04-09 15:32:03,146 [INFO] ------------------------------------------------------------
2024-04-09 15:32:03,148 [INFO] The program finished with the following exception:
2024-04-09 15:32:03,151 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Unable to instantiate java compiler
2024-04-09 15:32:03,154 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-04-09 15:32:03,156 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-04-09 15:32:03,159 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-04-09 15:32:03,162 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-04-09 15:32:03,164 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-04-09 15:32:03,167 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-04-09 15:32:03,170 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-04-09 15:32:03,172 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-04-09 15:32:03,175 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-04-09 15:32:03,178 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-04-09 15:32:03,180 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-04-09 15:32:03,183 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-04-09 15:32:03,186 [INFO] Caused by: java.lang.IllegalStateException: Unable to instantiate java compiler
2024-04-09 15:32:03,189 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:428)
2024-04-09 15:32:03,191 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.load3(JaninoRelMetadataProvider.java:374)
2024-04-09 15:32:03,194 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.lambda$static$0(JaninoRelMetadataProvider.java:109)
2024-04-09 15:32:03,197 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.CacheLoader$FunctionToCacheLoader.load(CacheLoader.java:165)
2024-04-09 15:32:03,199 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LoadingValueReference.loadFuture(LocalCache.java:3529)
2024-04-09 15:32:03,202 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.loadSync(LocalCache.java:2278)
2024-04-09 15:32:03,205 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.lockedGetOrLoad(LocalCache.java:2155)
2024-04-09 15:32:03,207 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$Segment.get(LocalCache.java:2045)
2024-04-09 15:32:03,210 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.get(LocalCache.java:3951)
2024-04-09 15:32:03,213 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache.getOrLoad(LocalCache.java:3974)
2024-04-09 15:32:03,215 [INFO] at org.apache.flink.calcite.shaded.com.google.common.cache.LocalCache$LocalLoadingCache.get(LocalCache.java:4958)
2024-04-09 15:32:03,218 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.create(JaninoRelMetadataProvider.java:469)
2024-04-09 15:32:03,221 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.revise(JaninoRelMetadataProvider.java:481)
2024-04-09 15:32:03,224 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQueryBase.revise(RelMetadataQueryBase.java:95)
2024-04-09 15:32:03,226 [INFO] at org.apache.calcite.rel.metadata.RelMetadataQuery.getPulledUpPredicates(RelMetadataQuery.java:784)
2024-04-09 15:32:03,229 [INFO] at org.apache.calcite.rel.rules.ReduceExpressionsRule$FilterReduceExpressionsRule.onMatch(ReduceExpressionsRule.java:151)
2024-04-09 15:32:03,232 [INFO] at org.apache.calcite.plan.AbstractRelOptPlanner.fireRule(AbstractRelOptPlanner.java:333)
2024-04-09 15:32:03,234 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRule(HepPlanner.java:542)
2024-04-09 15:32:03,237 [INFO] at org.apache.calcite.plan.hep.HepPlanner.applyRules(HepPlanner.java:407)
2024-04-09 15:32:03,240 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeInstruction(HepPlanner.java:243)
2024-04-09 15:32:03,242 [INFO] at org.apache.calcite.plan.hep.HepInstruction$RuleInstance.execute(HepInstruction.java:127)
2024-04-09 15:32:03,245 [INFO] at org.apache.calcite.plan.hep.HepPlanner.executeProgram(HepPlanner.java:202)
2024-04-09 15:32:03,248 [INFO] at org.apache.calcite.plan.hep.HepPlanner.findBestExp(HepPlanner.java:189)
2024-04-09 15:32:03,251 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepProgram.optimize(FlinkHepProgram.scala:69)
2024-04-09 15:32:03,253 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkHepRuleSetProgram.optimize(FlinkHepRuleSetProgram.scala:87)
2024-04-09 15:32:03,256 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:62)
2024-04-09 15:32:03,259 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram$$anonfun$optimize$1.apply(FlinkChainedProgram.scala:58)
2024-04-09 15:32:03,262 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2024-04-09 15:32:03,264 [INFO] at scala.collection.TraversableOnce$$anonfun$foldLeft$1.apply(TraversableOnce.scala:157)
2024-04-09 15:32:03,267 [INFO] at scala.collection.Iterator$class.foreach(Iterator.scala:891)
2024-04-09 15:32:03,270 [INFO] at scala.collection.AbstractIterator.foreach(Iterator.scala:1334)
2024-04-09 15:32:03,273 [INFO] at scala.collection.IterableLike$class.foreach(IterableLike.scala:72)
2024-04-09 15:32:03,275 [INFO] at scala.collection.AbstractIterable.foreach(Iterable.scala:54)
2024-04-09 15:32:03,278 [INFO] at scala.collection.TraversableOnce$class.foldLeft(TraversableOnce.scala:157)
2024-04-09 15:32:03,281 [INFO] at scala.collection.AbstractTraversable.foldLeft(Traversable.scala:104)
2024-04-09 15:32:03,284 [INFO] at org.apache.flink.table.planner.plan.optimize.program.FlinkChainedProgram.optimize(FlinkChainedProgram.scala:57)
2024-04-09 15:32:03,286 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.optimizeTree(StreamCommonSubGraphBasedOptimizer.scala:163)
2024-04-09 15:32:03,289 [INFO] at org.apache.flink.table.planner.plan.optimize.StreamCommonSubGraphBasedOptimizer.doOptimize(StreamCommonSubGraphBasedOptimizer.scala:79)
2024-04-09 15:32:03,292 [INFO] at org.apache.flink.table.planner.plan.optimize.CommonSubGraphBasedOptimizer.optimize(CommonSubGraphBasedOptimizer.scala:83)
2024-04-09 15:32:03,294 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.optimize(PlannerBase.scala:287)
2024-04-09 15:32:03,297 [INFO] at org.apache.flink.table.planner.delegation.PlannerBase.translate(PlannerBase.scala:160)
2024-04-09 15:32:03,300 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toDataStream(StreamTableEnvironmentImpl.java:357)
2024-04-09 15:32:03,303 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toRetractStream(StreamTableEnvironmentImpl.java:332)
2024-04-09 15:32:03,305 [INFO] at org.apache.flink.table.api.bridge.java.internal.StreamTableEnvironmentImpl.toRetractStream(StreamTableEnvironmentImpl.java:321)
2024-04-09 15:32:03,308 [INFO] at com.meituan.kugget.flink.job.executor.feature.FlinkTableToStreamWithJsonFormat.execute(FlinkTableToStreamWithJsonFormat.java:48)
2024-04-09 15:32:03,311 [INFO] at com.meituan.kugget.flink.job.executor.StageExecutor.executeStage(StageExecutor.java:54)
2024-04-09 15:32:03,314 [INFO] at com.meituan.kugget.flink.job.context.StageLooper.loopStage(StageLooper.java:82)
2024-04-09 15:32:03,316 [INFO] at com.meituan.kugget.flink.job.FlinkApplication.main(FlinkApplication.java:20)
2024-04-09 15:32:03,319 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-04-09 15:32:03,322 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-04-09 15:32:03,325 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-04-09 15:32:03,327 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-04-09 15:32:03,330 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-04-09 15:32:03,333 [INFO] ... 11 more
2024-04-09 15:32:03,336 [INFO] Caused by: java.lang.ClassCastException: org.codehaus.janino.CompilerFactory cannot be cast to org.codehaus.commons.compiler.ICompilerFactory
2024-04-09 15:32:03,338 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getCompilerFactory(CompilerFactoryFactory.java:129)
2024-04-09 15:32:03,341 [INFO] at org.codehaus.commons.compiler.CompilerFactoryFactory.getDefaultCompilerFactory(CompilerFactoryFactory.java:79)
2024-04-09 15:32:03,344 [INFO] at org.apache.calcite.rel.metadata.JaninoRelMetadataProvider.compile(JaninoRelMetadataProvider.java:426)
2024-04-09 15:32:03,346 [INFO] ... 63 more
2024-04-09 15:32:03,349 [INFO] Exception in thread "Thread-12" java.lang.NoClassDefFoundError: com/sankuai/inf/dayu/dye/routing/core/utils/Close
2024-04-09 15:32:03,352 [INFO] at com.sankuai.inf.dayu.dye.routing.core.extension.ExtensionContext.close(ExtensionContext.java:64)
2024-04-09 15:32:03,354 [INFO] at com.sankuai.inf.dayu.dye.routing.core.DefaultDyeRoutingContext$1.run(DefaultDyeRoutingContext.java:66)
2024-04-09 15:32:03,357 [INFO] at java.lang.Thread.run(Thread.java:745)
2024-04-09 15:32:03,360 [INFO] Caused by: java.lang.ClassNotFoundException: com.sankuai.inf.dayu.dye.routing.core.utils.Close
2024-04-09 15:32:03,363 [INFO] at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
2024-04-09 15:32:03,365 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
2024-04-09 15:32:03,368 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClassWithoutExceptionHandling(FlinkUserCodeClassLoader.java:64)
2024-04-09 15:32:03,371 [INFO] at org.apache.flink.util.ChildFirstClassLoader.loadClassWithoutExceptionHandling(ChildFirstClassLoader.java:74)
2024-04-09 15:32:03,373 [INFO] at org.apache.flink.util.FlinkUserCodeClassLoader.loadClass(FlinkUserCodeClassLoader.java:48)
2024-04-09 15:32:03,376 [INFO] at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
2024-04-09 15:32:03,379 [INFO] ... 3 more
2024-04-09 15:32:03,382 [INFO] start kill process[422489] and subProcess...
2024-04-09 15:32:03,384 [INFO] ==========================Tue Apr 9 15:32:03 CST 2024==========================
2024-04-09 15:32:03,403 [INFO] process 422489 has finished.
2024-04-09 15:32:03,406 [INFO] ==========================kill process finish==========================

```


## Recovery is suppressed by org.apache.flink.runtime.executiongraph.failover.flip1.
```
重启解决


2024-04-09 23:41:49
org.apache.flink.runtime.JobException: Recovery is suppressed by org.apache.flink.runtime.executiongraph.failover.flip1.FixedDelayFullRestartBackoffTimeStrategy@509e4fb8
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.handleFailure(ExecutionFailureHandler.java:124)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getGlobalFailureHandlingResult(ExecutionFailureHandler.java:99)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getFailureHandlingResult(ExecutionFailureHandler.java:83)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.handleTaskFailure(DefaultScheduler.java:253)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.maybeHandleTaskFailure(DefaultScheduler.java:244)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.updateTaskExecutionStateInternal(DefaultScheduler.java:235)
	at org.apache.flink.runtime.scheduler.SchedulerBase.updateTaskExecutionState(SchedulerBase.java:674)
	at org.apache.flink.runtime.scheduler.SchedulerNG.updateTaskExecutionState(SchedulerNG.java:91)
	at org.apache.flink.runtime.jobmaster.JobMaster.updateTaskExecutionState(JobMaster.java:471)
	at sun.reflect.GeneratedMethodAccessor83.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcInvocation(AkkaRpcActor.java:305)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:212)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)
Caused by: java.lang.NullPointerException
	at com.meituan.kugget.flink.job.executor.feature.StreamWithJsonFormatToFlinkTable.lambda$jsonToRow$d7c9a53a$1(StreamWithJsonFormatToFlinkTable.java:86)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:252)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)


```

## create mafka consumer failed.
```
应该是授权超时导致的


2024-04-10 23:20:32
java.util.concurrent.TimeoutException: The heartbeat of TaskManager with id container_e27_1693377093611_16291924_01_000037(yg-data-hdp-dn-rtyarn8404.mt:8043)  timed out.
	at org.apache.flink.runtime.resourcemanager.ResourceManager$TaskManagerHeartbeatListener.notifyHeartbeatTimeout(ResourceManager.java:1631)
	at org.apache.flink.runtime.heartbeat.HeartbeatMonitorImpl.run(HeartbeatMonitorImpl.java:111)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRunAsync(AkkaRpcActor.java:440)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:208)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)





2024-04-10 23:24:22,202 ERROR com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher  - create mafka consumer failed.
java.lang.InterruptedException
	at java.lang.Object.wait(Native Method)
	at java.lang.Object.wait(Object.java:502)
	at org.apache.flink.shaded.curator4.org.apache.curator.framework.recipes.barriers.DistributedDoubleBarrier.internalEnter(DistributedDoubleBarrier.java:339)
	at org.apache.flink.shaded.curator4.org.apache.curator.framework.recipes.barriers.DistributedDoubleBarrier.enter(DistributedDoubleBarrier.java:128)
	at org.apache.flink.shaded.curator4.org.apache.curator.framework.recipes.barriers.DistributedDoubleBarrier.enter(DistributedDoubleBarrier.java:107)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.createMafkaConsumer(MafkaFetcher.java:249)
	at com.meituan.flink.streaming.connectors.mafka.internal.MafkaFetcher.<init>(MafkaFetcher.java:99)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaConsumer.run(FlinkMafkaConsumer.java:192)
	at org.apache.flink.streaming.api.operators.StreamSource.run(StreamSource.java:110)
	at org.apache.flink.streaming.api.operators.StreamSource.run(StreamSource.java:66)
	at org.apache.flink.streaming.runtime.tasks.SourceStreamTask$LegacySourceFunctionThread.run(SourceStreamTask.java:263)

```


## RowSerializer.copy npe
```
2024-04-11 22:25:24
org.apache.flink.runtime.JobException: Recovery is suppressed by org.apache.flink.runtime.executiongraph.failover.flip1.FixedDelayFullRestartBackoffTimeStrategy@6049b50c
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.handleFailure(ExecutionFailureHandler.java:124)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getGlobalFailureHandlingResult(ExecutionFailureHandler.java:99)
	at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getFailureHandlingResult(ExecutionFailureHandler.java:83)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.handleTaskFailure(DefaultScheduler.java:253)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.maybeHandleTaskFailure(DefaultScheduler.java:244)
	at org.apache.flink.runtime.scheduler.DefaultScheduler.updateTaskExecutionStateInternal(DefaultScheduler.java:235)
	at org.apache.flink.runtime.scheduler.SchedulerBase.updateTaskExecutionState(SchedulerBase.java:674)
	at org.apache.flink.runtime.scheduler.SchedulerNG.updateTaskExecutionState(SchedulerNG.java:91)
	at org.apache.flink.runtime.jobmaster.JobMaster.updateTaskExecutionState(JobMaster.java:471)
	at sun.reflect.GeneratedMethodAccessor47.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcInvocation(AkkaRpcActor.java:305)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:212)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)
Caused by: java.lang.NullPointerException
	at org.apache.flink.api.java.typeutils.runtime.RowSerializer.copy(RowSerializer.java:115)
	at org.apache.flink.api.java.typeutils.runtime.RowSerializer.copy(RowSerializer.java:61)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:77)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:252)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)

```


## Buffer pool is destroyed
```

可能是数据读写问题
流数据需要指定读取历史数据

for task Source: app.data_fact_log_sdk_result_event_mt_home_search (272/400)#1 b58f014a41c4f90cbfb37da596b95208.
2024-04-15 13:35:09,206 ERROR com.meituan.kugget.flink.job.util.udf.ParseIntentionPairByIdsV1  - jsonArrayString error:14,12,4,412,304,314,33,166,250,2150,10314,6250,30314,414,50314,350,341,141,80314,241,55,66,61,50,57,147,47,13,247,22,122,432,466, search key : null
org.apache.flink.streaming.runtime.tasks.ExceptionInChainedOperatorException: Could not forward element to next operator
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:103)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.runtime.tasks.BroadcastingOutputCollector.collect(BroadcastingOutputCollector.java:75)
	at org.apache.flink.streaming.runtime.tasks.BroadcastingOutputCollector.collect(BroadcastingOutputCollector.java:32)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.table.runtime.util.StreamRecordCollector.collect(StreamRecordCollector.java:44)
	at org.apache.flink.table.runtime.collector.TableFunctionCollector.outputResult(TableFunctionCollector.java:68)
	at StreamExecCorrelate$667$TableFunctionCollector$654.collect(Unknown Source)
	at org.apache.flink.table.runtime.collector.WrappingCollector.outputResult(WrappingCollector.java:39)
	at StreamExecCorrelate$667$TableFunctionResultConverterCollector$665.collect(Unknown Source)
	at org.apache.flink.table.functions.TableFunction.collect(TableFunction.java:196)
	at com.meituan.kugget.flink.job.util.udf.ParseIntentionPairByIdsV1.eval(ParseIntentionPairByIdsV1.java:127)
	at StreamExecCorrelate$667.processElement(Unknown Source)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:81)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.runtime.tasks.BroadcastingOutputCollector.collect(BroadcastingOutputCollector.java:75)
	at org.apache.flink.streaming.runtime.tasks.BroadcastingOutputCollector.collect(BroadcastingOutputCollector.java:32)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at StreamExecCalc$651.processElement(Unknown Source)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:81)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:54)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.collect(ProcessTimeTrackingCopyingChainingOutput.java:29)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.TimestampedCollector.collect(TimestampedCollector.java:50)
	at org.apache.flink.table.runtime.operators.join.stream.StreamingJoinOperator.outputNullPadding(StreamingJoinOperator.java:393)
	at org.apache.flink.table.runtime.operators.join.stream.StreamingJoinOperator.processElement(StreamingJoinOperator.java:267)
	at org.apache.flink.table.runtime.operators.join.stream.StreamingJoinOperator.processElement1(StreamingJoinOperator.java:167)
	at org.apache.flink.streaming.runtime.io.StreamTwoInputProcessorFactory.processRecord1(StreamTwoInputProcessorFactory.java:237)
	at org.apache.flink.streaming.runtime.io.StreamTwoInputProcessorFactory.lambda$create$0(StreamTwoInputProcessorFactory.java:172)
	at org.apache.flink.streaming.runtime.io.StreamTwoInputProcessorFactory$StreamTaskNetworkOutput.emitRecord(StreamTwoInputProcessorFactory.java:315)
	at org.apache.flink.streaming.runtime.io.StreamTwoInputProcessorFactory$ProcessTimeTrackingStreamTaskNetworkOutput.emitRecord(StreamTwoInputProcessorFactory.java:391)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.io.StreamTwoInputProcessor.processInput(StreamTwoInputProcessor.java:95)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)
Caused by: java.lang.RuntimeException: Buffer pool is destroyed.
	at org.apache.flink.streaming.runtime.io.RecordWriterOutput.pushToRecordWriter(RecordWriterOutput.java:125)
	at org.apache.flink.streaming.runtime.io.RecordWriterOutput.collect(RecordWriterOutput.java:109)
	at org.apache.flink.streaming.runtime.io.RecordWriterOutput.collect(RecordWriterOutput.java:45)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at StreamExecCalc$733.processElement(Unknown Source)
	at org.apache.flink.streaming.runtime.tasks.ProcessTimeTrackingCopyingChainingOutput.pushToOperator(ProcessTimeTrackingCopyingChainingOutput.java:81)
	... 46 more
Caused by: java.lang.IllegalStateException: Buffer pool is destroyed.
	at org.apache.flink.runtime.io.network.buffer.LocalBufferPool.requestMemorySegment(LocalBufferPool.java:333)
	at org.apache.flink.runtime.io.network.buffer.LocalBufferPool.requestBufferBuilder(LocalBufferPool.java:280)
	at org.apache.flink.runtime.io.network.partition.BufferWritingResultPartition.requestNewBufferBuilderFromPool(BufferWritingResultPartition.java:330)
	at org.apache.flink.runtime.io.network.partition.BufferWritingResultPartition.requestNewUnicastBufferBuilder(BufferWritingResultPartition.java:313)
	at org.apache.flink.runtime.io.network.partition.BufferWritingResultPartition.appendUnicastDataForNewRecord(BufferWritingResultPartition.java:245)
	at org.apache.flink.runtime.io.network.partition.BufferWritingResultPartition.emitRecord(BufferWritingResultPartition.java:144)
	at org.apache.flink.runtime.io.network.api.writer.RecordWriter.emit(RecordWriter.java:104)
	at org.apache.flink.runtime.io.network.api.writer.ChannelSelectorRecordWriter.emit(ChannelSelectorRecordWriter.java:54)
	at org.apache.flink.streaming.runtime.io.RecordWriterOutput.pushToRecordWriter(RecordWriterOutput.java:123)
	... 52 more

```


##  UTF-8 is not serializable
```

org.apache.flink.api.common.InvalidProgramException: UTF-8 is not serializable. The object probably contains or references non serializable fields.

	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:164)
	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:132)
	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:69)
	at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.clean(StreamExecutionEnvironment.java:2000)
	at org.apache.flink.streaming.api.datastream.DataStream.clean(DataStream.java:203)
	at org.apache.flink.streaming.api.datastream.DataStream.map(DataStream.java:577)
	at com.meituan.supply.flink.executor.retriever.HbaseKvRetriever.execute(HbaseKvRetriever.java:74)
	at com.meituan.supply.flink.executor.PipelineExecutor.execute(PipelineExecutor.java:79)
	at com.meituan.supply.flink.GraphTest.testRunHbaseOneNode(GraphTest.java:89)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:59)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:56)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
	at org.junit.runners.ParentRunner$3.evaluate(ParentRunner.java:306)
	at org.junit.runners.BlockJUnit4ClassRunner$1.evaluate(BlockJUnit4ClassRunner.java:100)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:366)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:103)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:63)
	at org.junit.runners.ParentRunner$4.run(ParentRunner.java:331)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:79)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:329)
	at org.junit.runners.ParentRunner.access$100(ParentRunner.java:66)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:293)
	at org.junit.runners.ParentRunner$3.evaluate(ParentRunner.java:306)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:413)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:69)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater$1.execute(IdeaTestRunner.java:38)
	at com.intellij.rt.execution.junit.TestsRepeater.repeat(TestsRepeater.java:11)
	at com.intellij.rt.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:35)
	at com.intellij.rt.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:235)
	at com.intellij.rt.junit.JUnitStarter.main(JUnitStarter.java:54)
Caused by: java.io.NotSerializableException: sun.nio.cs.UTF_8
	at java.io.ObjectOutputStream.writeObject0(ObjectOutputStream.java:1184)
	at java.io.ObjectOutputStream.writeObject(ObjectOutputStream.java:348)
	at org.apache.flink.util.InstantiationUtil.serializeObject(InstantiationUtil.java:624)
	at org.apache.flink.api.java.ClosureCleaner.clean(ClosureCleaner.java:143)
	... 37 more

```


## restartStrategyConfiguration 
```

flink启动缺少重启策略配置
原因是美团和开源flink版本不一致，有新增内容

2024-05-07 00:26:30
java.lang.IllegalArgumentException: restartStrategyConfiguration should be NoRestartStrategyConfiguration or ForceFullRestartStrategyConfiguration(FailureRateFullRestartStrategyConfiguration or FixedDelayFullRestartStrategyConfiguration)
	at org.apache.flink.util.Preconditions.checkArgument(Preconditions.java:138)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaConsumer.checkRestartStrategy(FlinkMafkaConsumer.java:308)
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaConsumer.open(FlinkMafkaConsumer.java:136)
	at org.apache.flink.api.common.functions.util.FunctionUtils.openFunction(FunctionUtils.java:34)
	at org.apache.flink.streaming.api.operators.AbstractUdfStreamOperator.open(AbstractUdfStreamOperator.java:102)
	at org.apache.flink.streaming.runtime.tasks.OperatorChain.initializeStateAndOpenOperators(OperatorChain.java:478)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.lambda$beforeInvoke$2(StreamTask.java:547)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$SynchronizedStreamTaskActionExecutor.runThrowing(StreamTaskActionExecutor.java:93)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.beforeInvoke(StreamTask.java:537)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:577)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)

```


## Caused by: java.lang.ClassNotFoundException: com.meituan.flink.track.service.ConfigOption

```
新增
<dependency>
            <groupId>com.meituan.flink.track</groupId>
            <artifactId>flink-track</artifactId>
            <version>0.0.3</version>
        </dependency>


Caused by: java.lang.NoClassDefFoundError: com/meituan/flink/track/service/ConfigOption
	at org.apache.flink.runtime.track.TrackTags.<clinit>(TrackTags.java:8)
	at org.apache.flink.runtime.dispatcher.Dispatcher.updateTrackContext(Dispatcher.java:348)
	at org.apache.flink.runtime.dispatcher.Dispatcher.submitJob(Dispatcher.java:320)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcInvocation(AkkaRpcActor.java:305)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleRpcMessage(AkkaRpcActor.java:212)
	at org.apache.flink.runtime.rpc.akka.FencedAkkaRpcActor.handleRpcMessage(FencedAkkaRpcActor.java:77)
	at org.apache.flink.runtime.rpc.akka.AkkaRpcActor.handleMessage(AkkaRpcActor.java:158)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:26)
	at akka.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:21)
	at scala.PartialFunction$class.applyOrElse(PartialFunction.scala:123)
	at akka.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:21)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:170)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:171)
	at akka.actor.Actor$class.aroundReceive(Actor.scala:517)
	at akka.actor.AbstractActor.aroundReceive(AbstractActor.scala:225)
	at akka.actor.ActorCell.receiveMessage(ActorCell.scala:592)
	at akka.actor.ActorCell.invoke(ActorCell.scala:561)
	at akka.dispatch.Mailbox.processMailbox(Mailbox.scala:258)
	at akka.dispatch.Mailbox.run(Mailbox.scala:225)
	at akka.dispatch.Mailbox.exec(Mailbox.scala:235)
	at akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)
	at akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)
	at akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)
	at akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)

```


## : Origin: InterruptedException
```
[WARN ] 2024-05-08 14:06:35,445 Map -> jsonToRow -> Map -> replaceByHbaseKv -> Map -> Sink: Print to Std. Out (5/16)#9 (8af9e66514e5bb628b2751546e90f531) switched from RUNNING to FAILED. - method:org.apache.flink.runtime.taskmanager.Task.transitionState(Task.java:1045)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
java.lang.ClassCastException: java.lang.String cannot be cast to java.lang.Long
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.api.common.typeutils.base.LongSerializer.copy(LongSerializer.java:30)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.api.java.typeutils.runtime.RowSerializer.copy(RowSerializer.java:128)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.api.java.typeutils.runtime.RowSerializer.copy(RowSerializer.java:61)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.pushToOperator(CopyingChainingOutput.java:69)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:46)
	at java.lang.Thread.run(Thread.java:748)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:26)
Caused by: java.io.InterruptedIOException: Origin: InterruptedException
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.hadoop.hbase.util.ExceptionUtil.asInterrupt(ExceptionUtil.java:66)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.hadoop.hbase.protobuf.ProtobufUtil.makeIOExceptionOfException(ProtobufUtil.java:2737)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.hadoop.hbase.protobuf.ProtobufUtil.handleRemoteException(ProtobufUtil.java:2728)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.pushToOperator(CopyingChainingOutput.java:71)
	at org.apache.hadoop.hbase.client.RegionServerCallable.call(RegionServerCallable.java:130)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:46)
	at org.apache.hadoop.hbase.client.RpcRetryingCallerImpl.callWithRetries(RpcRetryingCallerImpl.java:103)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:26)
	at org.apache.hadoop.hbase.client.HTable.get(HTable.java:866)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.hadoop.hbase.client.HTable.get(HTable.java:836)
	at com.meituan.service.hbase.AbstractHBaseClient.get(AbstractHBaseClient.java:172)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	... 33 more
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.pushToOperator(CopyingChainingOutput.java:71)
Caused by: java.lang.InterruptedException
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:46)
	at java.lang.Object.wait(Native Method)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:26)
	at org.apache.hadoop.hbase.ipc.RpcClientImpl.call(RpcClientImpl.java:1278)
	at org.apache.hadoop.hbase.ipc.AbstractRpcClient.callBlockingMethod(AbstractRpcClient.java:253)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	at org.apache.hadoop.hbase.ipc.AbstractRpcClient$BlockingRpcChannelImplementation.callBlockingMethod(AbstractRpcClient.java:364)
	at org.apache.flink.streaming.api.operators.StreamFilter.processElement(StreamFilter.java:39)
	at org.apache.hadoop.hbase.shaded.protobuf.generated.ClientProtos$ClientService$BlockingStub.get(ClientProtos.java:40224)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.pushToOperator(CopyingChainingOutput.java:71)
	at org.apache.hadoop.hbase.client.ClientServiceCallable.doGet(ClientServiceCallable.java:49)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:46)
	at org.apache.hadoop.hbase.client.HTable$2.rpcCall(HTable.java:857)
	at org.apache.flink.streaming.runtime.tasks.CopyingChainingOutput.collect(CopyingChainingOutput.java:26)
	at org.apache.hadoop.hbase.client.HTable$2.rpcCall(HTable.java:852)
	at org.apache.hadoop.hbase.client.RegionServerCallable.call(RegionServerCallable.java:128)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:50)
	at org.apache.flink.streaming.api.operators.CountingOutput.collect(CountingOutput.java:28)
	... 37 more
	at org.apache.flink.streaming.api.operators.StreamMap.processElement(StreamMap.java:38)
	at org.apache.flink.streaming.runtime.tasks.OneInputStreamTask$StreamTaskNetworkOutput.emitRecord(OneInputStreamTask.java:213)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.processElement(StreamTaskNetworkInput.java:204)
	at org.apache.flink.streaming.runtime.io.StreamTaskNetworkInput.emitNext(StreamTaskNetworkInput.java:174)
	at org.apache.flink.streaming.runtime.io.StreamOneInputProcessor.processInput(StreamOneInputProcessor.java:65)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.processInput(StreamTask.java:400)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:191)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)

```


## Caused by: java.lang.IllegalStateException: Failed to rollback to checkpoint/savepoint viewfs://hadoop-meituan/user/hadoop-rt/flink-bj/checkpoints/hadoop-rt/retained/1514974/48264439b38feffb0fba555cf98a9b1e/chk-91945. Cannot map checkpoint/savepoint state for operator e70bbd798b564e0a50e10e343f1ac56b to the new program, because the operator is not available in the new program. If you want to allow to skip this, you can set the --allowNonRestoredState option on the CLI.
```
不能从checkpoint 恢复。只能丢弃数据

代码修改 operator 图有改动，所以原来的状态无法读取
只能回溯消息，重新生成新的state


 ERROR org.apache.flink.shaded.curator4.org.apache.curator.ConnectionState  - Authentication failed
2024-06-10 15:22:11,321 [INFO] INFO  com.meituan.flink.utils.haservices.leaderservice.MtLeaderRetrievalService  - Notify to org.apache.flink.runtime.webmonitor.retriever.LeaderRetriever directly with default leader information: leader id b67c68c7-f997-3070-a836-6f33076efbd2, leader address http://zf-data-hdp-dn-rtyarn2522.mt:13367, leader startTime 0
2024-06-10 15:22:11,323 [INFO] INFO  org.apache.flink.shaded.zookeeper3.org.apache.zookeeper.ClientCnxn  - Socket connection established to zf-data-zk-flink02.mt/10.56.22.15:2181, initiating session
2024-06-10 15:22:11,325 [INFO] INFO  org.apache.flink.shaded.zookeeper3.org.apache.zookeeper.ClientCnxn  - Session establishment complete on server zf-data-zk-flink02.mt/10.56.22.15:2181, sessionid = 0x272cbcd3c43dc71, negotiated timeout = 40000
2024-06-10 15:22:11,328 [INFO] INFO  org.apache.flink.shaded.curator4.org.apache.curator.framework.state.ConnectionStateManager  - State change: CONNECTED
2024-06-10 15:22:11,330 [INFO] INFO  com.meituan.flink.utils.haservices.leaderservice.MtLeaderRetrievalService  - Connected to ZooKeeper quorum. Leader retrieval can start.
2024-06-10 15:22:11,333 [INFO] INFO  com.meituan.flink.utils.haservices.leaderservice.MtLeaderRetrievalService  - Listening znode at /leader/rest_server_lock
2024-06-10 15:22:18,291 [INFO] INFO  com.meituan.flink.utils.haservices.leaderservice.MtLeaderRetrievalService  - Stopping MtLeaderRetrievalService MtLeaderRetrievalService{lastLeaderAddress='http://zf-data-hdp-dn-rtyarn2522.mt:13367', lastLeaderSessionID=b67c68c7-f997-3070-a836-6f33076efbd2, lastLeaderStartTime=0, running=true, leaderListener=org.apache.flink.runtime.webmonitor.retriever.LeaderRetriever, leaderRetrievalDriver=MtLeaderRetrievalDriver{retrievalPath='/leader/rest_server_lock'}} for org.apache.flink.runtime.webmonitor.retriever.LeaderRetriever.
2024-06-10 15:22:18,293 [INFO] INFO  com.meituan.flink.utils.haservices.leaderservice.MtLeaderRetrievalService  - Closing MtLeaderRetrievalDriver{retrievalPath='/leader/rest_server_lock'}.
2024-06-10 15:22:18,296 [INFO] INFO  org.apache.flink.shaded.curator4.org.apache.curator.framework.imps.CuratorFrameworkImpl  - backgroundOperationsLoop exiting
2024-06-10 15:22:18,299 [INFO] INFO  org.apache.flink.shaded.zookeeper3.org.apache.zookeeper.ZooKeeper  - Session: 0x272cbcd3c43dc71 closed
2024-06-10 15:22:18,301 [INFO] INFO  org.apache.flink.shaded.zookeeper3.org.apache.zookeeper.ClientCnxn  - EventThread shut down for session: 0x272cbcd3c43dc71
2024-06-10 15:22:18,304 [INFO] ERROR org.apache.flink.client.cli.CliFrontend                       - Error while running the command.
2024-06-10 15:22:18,306 [INFO] org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Failed to execute job 'Flink Streaming Job'.
2024-06-10 15:22:18,309 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:366)
2024-06-10 15:22:18,311 [INFO] at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:219)
2024-06-10 15:22:18,313 [INFO] at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:114)
2024-06-10 15:22:18,316 [INFO] at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:867)
2024-06-10 15:22:18,318 [INFO] at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:263)
2024-06-10 15:22:18,342 [INFO] at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1109)
2024-06-10 15:22:18,344 [INFO] at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1188)
2024-06-10 15:22:18,347 [INFO] at java.security.AccessController.doPrivileged(Native Method)
2024-06-10 15:22:18,349 [INFO] at javax.security.auth.Subject.doAs(Subject.java:422)
2024-06-10 15:22:18,352 [INFO] at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1717)
2024-06-10 15:22:18,354 [INFO] at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
2024-06-10 15:22:18,357 [INFO] at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1188)
2024-06-10 15:22:18,359 [INFO] Caused by: org.apache.flink.util.FlinkException: Failed to execute job 'Flink Streaming Job'.
2024-06-10 15:22:18,361 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.executeAsync(StreamExecutionEnvironment.java:1925)
2024-06-10 15:22:18,364 [INFO] at org.apache.flink.client.program.StreamContextEnvironment.executeAsync(StreamContextEnvironment.java:135)
2024-06-10 15:22:18,366 [INFO] at org.apache.flink.client.program.StreamContextEnvironment.execute(StreamContextEnvironment.java:76)
2024-06-10 15:22:18,369 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:1789)
2024-06-10 15:22:18,371 [INFO] at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:1772)
2024-06-10 15:22:18,373 [INFO] at com.meituan.aios.dtx.builder.stream.flink.FlinkJobMain.main(FlinkJobMain.java:26)
2024-06-10 15:22:18,376 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2024-06-10 15:22:18,378 [INFO] at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2024-06-10 15:22:18,381 [INFO] at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2024-06-10 15:22:18,383 [INFO] at java.lang.reflect.Method.invoke(Method.java:498)
2024-06-10 15:22:18,385 [INFO] at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:349)
2024-06-10 15:22:18,388 [INFO] ... 11 more
2024-06-10 15:22:18,390 [INFO] Caused by: java.lang.RuntimeException: org.apache.flink.runtime.client.JobInitializationException: Could not instantiate JobManager.
2024-06-10 15:22:18,393 [INFO] at org.apache.flink.util.ExceptionUtils.rethrow(ExceptionUtils.java:316)
2024-06-10 15:22:18,395 [INFO] at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedFunction$2(FunctionUtils.java:75)
2024-06-10 15:22:18,398 [INFO] at java.util.concurrent.CompletableFuture.uniApply(CompletableFuture.java:602)
2024-06-10 15:22:18,400 [INFO] at java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:577)
2024-06-10 15:22:18,402 [INFO] at java.util.concurrent.CompletableFuture$Completion.exec(CompletableFuture.java:443)
2024-06-10 15:22:18,405 [INFO] at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
2024-06-10 15:22:18,407 [INFO] at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
2024-06-10 15:22:18,410 [INFO] at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
2024-06-10 15:22:18,412 [INFO] at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:157)
2024-06-10 15:22:18,415 [INFO] Caused by: org.apache.flink.runtime.client.JobInitializationException: Could not instantiate JobManager.
2024-06-10 15:22:18,417 [INFO] at org.apache.flink.runtime.dispatcher.Dispatcher.lambda$createJobManagerRunner$5(Dispatcher.java:545)
2024-06-10 15:22:18,419 [INFO] at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1604)
2024-06-10 15:22:18,422 [INFO] at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
2024-06-10 15:22:18,424 [INFO] at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
2024-06-10 15:22:18,427 [INFO] at java.lang.Thread.run(Thread.java:748)
2024-06-10 15:22:18,429 [INFO] Caused by: java.lang.IllegalStateException: Failed to rollback to checkpoint/savepoint viewfs://hadoop-meituan/user/hadoop-rt/flink-bj/checkpoints/hadoop-rt/retained/1514974/48264439b38feffb0fba555cf98a9b1e/chk-91945. Cannot map checkpoint/savepoint state for operator e70bbd798b564e0a50e10e343f1ac56b to the new program, because the operator is not available in the new program. If you want to allow to skip this, you can set the --allowNonRestoredState option on the CLI.
2024-06-10 15:22:18,431 [INFO] at org.apache.flink.runtime.checkpoint.Checkpoints.throwNonRestoredStateException(Checkpoints.java:226)
2024-06-10 15:22:18,434 [INFO] at org.apache.flink.runtime.checkpoint.Checkpoints.loadAndValidateCheckpoint(Checkpoints.java:190)
2024-06-10 15:22:18,436 [INFO] at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.restoreSavepoint(CheckpointCoordinator.java:1692)
2024-06-10 15:22:18,439 [INFO] at org.apache.flink.runtime.scheduler.SchedulerBase.tryRestoreExecutionGraphFromSavepoint(SchedulerBase.java:362)
2024-06-10 15:22:18,442 [INFO] at org.apache.flink.runtime.scheduler.SchedulerBase.createAndRestoreExecutionGraph(SchedulerBase.java:292)
2024-06-10 15:22:18,444 [INFO] at org.apache.flink.runtime.scheduler.SchedulerBase.<init>(SchedulerBase.java:249)
2024-06-10 15:22:18,447 [INFO] at org.apache.flink.runtime.scheduler.DefaultScheduler.<init>(DefaultScheduler.java:149)
2024-06-10 15:22:18,449 [INFO] at org.apache.flink.runtime.scheduler.DefaultSchedulerFactory.createInstance(DefaultSchedulerFactory.java:112)
2024-06-10 15:22:18,451 [INFO] at org.apache.flink.runtime.jobmaster.JobMaster.createScheduler(JobMaster.java:366)
2024-06-10 15:22:18,454 [INFO] at org.apache.flink.runtime.jobmaster.JobMaster.<init>(JobMaster.java:346)
2024-06-10 15:22:18,456 [INFO] at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.createJobMasterService(DefaultJobMasterServiceFactory.java:95)
2024-06-10 15:22:18,459 [INFO] at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.createJobMasterService(DefaultJobMasterServiceFactory.java:39)
2024-06-10 15:22:18,461 [INFO] at org.apache.flink.runtime.jobmaster.JobManagerRunnerImpl.<init>(JobManagerRunnerImpl.java:162)
2024-06-10 15:22:18,464 [INFO] at org.apache.flink.runtime.dispatcher.DefaultJobManagerRunnerFactory.createJobManagerRunner(DefaultJobManagerRunnerFactory.java:86)
2024-06-10 15:22:18,466 [INFO] at org.apache.flink.runtime.dispatcher.Dispatcher.lambda$createJobManagerRunner$5(Dispatcher.java:526)
2024-06-10 15:22:18,468 [INFO] ... 4 more
2024-06-10 15:22:18,471 [INFO] ------------------------------------------------------------

```


##  Insufficient number of network buffers
```
2024-06-12 13:27:00
java.io.IOException: Insufficient number of network buffers: required 2, but only 0 available. The total number of network buffers is currently set to 8192 of 32768 bytes each. You can increase this number by setting the configuration keys 'taskmanager.memory.network.fraction', 'taskmanager.memory.network.min', and 'taskmanager.memory.network.max'.
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.tryRedistributeBuffers(NetworkBufferPool.java:443)
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.requestMemorySegments(NetworkBufferPool.java:178)
	at org.apache.flink.runtime.io.network.buffer.NetworkBufferPool.requestMemorySegments(NetworkBufferPool.java:60)
	at org.apache.flink.runtime.io.network.partition.consumer.BufferManager.requestExclusiveBuffers(BufferManager.java:132)
	at org.apache.flink.runtime.io.network.partition.consumer.RemoteInputChannel.setup(RemoteInputChannel.java:161)
	at org.apache.flink.runtime.io.network.partition.consumer.RemoteRecoveredInputChannel.toInputChannelInternal(RemoteRecoveredInputChannel.java:77)
	at org.apache.flink.runtime.io.network.partition.consumer.RecoveredInputChannel.toInputChannel(RecoveredInputChannel.java:106)
	at org.apache.flink.runtime.io.network.partition.consumer.SingleInputGate.convertRecoveredInputChannels(SingleInputGate.java:306)
	at org.apache.flink.runtime.io.network.partition.consumer.SingleInputGate.requestPartitions(SingleInputGate.java:289)
	at org.apache.flink.runtime.taskmanager.InputGateWithMetrics.requestPartitions(InputGateWithMetrics.java:94)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$1.runThrowing(StreamTaskActionExecutor.java:50)
	at org.apache.flink.streaming.runtime.tasks.mailbox.Mail.run(Mail.java:90)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.processMail(MailboxProcessor.java:297)
	at org.apache.flink.streaming.runtime.tasks.mailbox.MailboxProcessor.runMailboxLoop(MailboxProcessor.java:189)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.runMailboxLoop(StreamTask.java:629)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:585)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)


```


##  The launcher environment and the runtime environment are inconsistent.
```
机器的jdk版本和jar包版本不兼容
换个队列就解决了

2024-06-26 22:13:40
java.lang.RuntimeException: The launcher environment and the runtime environment are inconsistent.
	at com.meituan.flink.streaming.connectors.mafka.FlinkMafkaConsumer.open(FlinkMafkaConsumer.java:134)
	at org.apache.flink.api.common.functions.util.FunctionUtils.openFunction(FunctionUtils.java:34)
	at org.apache.flink.streaming.api.operators.AbstractUdfStreamOperator.open(AbstractUdfStreamOperator.java:102)
	at org.apache.flink.streaming.runtime.tasks.OperatorChain.initializeStateAndOpenOperators(OperatorChain.java:478)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.lambda$beforeInvoke$2(StreamTask.java:547)
	at org.apache.flink.streaming.runtime.tasks.StreamTaskActionExecutor$SynchronizedStreamTaskActionExecutor.runThrowing(StreamTaskActionExecutor.java:93)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.beforeInvoke(StreamTask.java:537)
	at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:577)
	at org.apache.flink.runtime.taskmanager.Task.doRun(Task.java:767)
	at org.apache.flink.runtime.taskmanager.Task.run(Task.java:578)
	at java.lang.Thread.run(Thread.java:748)


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




