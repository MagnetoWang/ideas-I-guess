![spring and kafka](https://github.com/MagnetoWang/ideas-I-guess/blob/master/markdown-for-document-organization-management/manage-pictures/kafka.png)



[TOC]



## Kafka with Spring

### 参考链接

- 官方文档：https://docs.spring.io/spring-boot/docs/2.0.3.RELEASE/reference/htmlsingle/#boot-features-kafka
- kafka配置
  - http://www.54tianzhisheng.cn/2018/01/05/SpringBoot-Kafka/
  - https://blog.csdn.net/ldy1016/article/details/72852179/
  - https://www.cnblogs.com/niechen/p/8687206.html
  - https://blog.csdn.net/clypm/article/details/79498646
- spring-kafka快速入门（含有代码）：https://docs.spring.io/spring-kafka/docs/2.1.7.RELEASE/reference/html/
- spring-kafka-clien文档：https://docs.spring.io/spring-kafka/reference/htmlsingle/#_kafka_client_version
- Kafka原理
  - https://blog.xiaoxiaomo.com/2016/05/14/Kafka-Consumer%E6%B6%88%E8%B4%B9%E8%80%85/
  - https://segmentfault.com/a/1190000003922549
- Kafka入门简介
  - https://zhuanlan.zhihu.com/p/31731892
  - http://dataunion.org/6275.html
  - https://www.jianshu.com/p/f56b794ccc4c
  - https://www.cnblogs.com/kangoroo/p/7353330.html
- kafka进阶：
  - https://blog.csdn.net/lizhitao/article/details/39499283
  - https://blog.csdn.net/xingfulangren/article/details/74185282
  - https://blog.csdn.net/u011622226/article/details/72500713
  - http://www.cnblogs.com/huxi2b/p/6124937.html
- kafka中文笔记：http://www.cnblogs.com/cyfonly/p/5954614.html
- 安装kafka：https://zhuanlan.zhihu.com/p/32780543
- Kafka Shell基本命令（包括topic的增删改查）：https://www.cnblogs.com/xiaodf/p/6093261.html
- 消费者代码
  - http://www.cnblogs.com/qizhelongdeyang/p/7354183.html
  - http://www.54tianzhisheng.cn/2018/01/05/SpringBoot-Kafka/

### 配置

- 查看kafka数据
- 再用本地kafka进行连接测试
- 最后抓取测试
- 再和spring cloud data stream 结合



### 异常问题

- java.lang.IllegalStateException: ApplicationEventMulticaster not initialized
  - 依赖问题，有冲突。重新检查

- java.lang.[NoClassDefFoundError](https://blog.csdn.net/u014427391/article/details/79743318):org/springframework/cloud/stream/binding/StreamListenerSetupMethodOrchestrator
  - 在运行时JVM加载不到类或者找不到类 

- ClassNotfoundException 
  - 在编译时JVM加载不到类或者找不到类导致的 

- @Autowired-could not autowire

- Unregistering JMX-exposed beans

  - 这是启动的正常信息。因为你刚刚生成的项目，没有加载任何的模块 

  - ```
    <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```

