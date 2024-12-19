## 目录参考
1. 理解时间
2. 背景介绍
3. 参考资料
4. 核心思考问题
5. 入门概念
6. 阅读笔记
7. 项目工作流
8. 技术流图和图解
9.  源码目录
10. 模块拆解-横向
11. 模块拆解-纵向
12. 性能总结
13. 设计总结
14. 经验总结
15. 相同框架能力对比
16. 第三方依赖
17. 应用场景
18. 业务通点
19. 行业实践
20. case代码

## FlinkCDC源码解析

### 模块化构图，每一个模块对应一个标题
### 理解时间
```
2024年12月18号启动

永远带着问题/需求/目标/兴趣/收益看代码

源码理解角度
   高层次流图分析 - 更好把握主次
    比如大数据框架 考虑流式计算范式
    比如机器学习框架 考虑数学计算流图
    共性分析数据格式 存储 读写 和 网络流图
    业务使用流程图和场景图
   横向梳理所有模块
   纵向梳理某个功能点
   编译角度
   使用角度
   性能角度
   底层数据结构角度

完整理解FlinkCDC项目
如果只是在搜索引擎 搜 FlinkCDC是远远不够的
FlinkCDC + 架构图

FlinkCDC + 概念关键词

FlinkCDC + 问题排查

FlinkCDC + 面试汇总

FlinkCDC + 极客挑战赛

FlinkCDC + 论坛会议

FlinkCDC + 论文

FlinkCDC + 前沿分享

FlinkCDC + 场景应用

FlinkCDC + FlinkCDC大佬名字

FlinkCDC + 公司项目
等等才能完全熟悉FlinkCDC




```

## 源码编译
1. https://github.com/apache/flink-cdc
### 编译顺序
```
[INFO] Reactor Summary for flink-cdc-parent 3.3-SNAPSHOT:
[INFO] 
[INFO] flink-cdc-parent ................................... SUCCESS [  4.727 s]
[INFO] flink-cdc-common ................................... SUCCESS [  6.869 s]
[INFO] flink-cdc-pipeline-udf-examples .................... SUCCESS [ 14.530 s]
[INFO] flink-cdc-pipeline-model ........................... SUCCESS [  0.665 s]
[INFO] flink-cdc-runtime .................................. SUCCESS [  3.093 s]
[INFO] flink-cdc-connect .................................. SUCCESS [  0.137 s]
[INFO] flink-cdc-pipeline-connectors ...................... SUCCESS [  0.181 s]
[INFO] flink-cdc-pipeline-connector-values ................ SUCCESS [  2.255 s]
[INFO] flink-cdc-composer ................................. SUCCESS [  3.064 s]
[INFO] flink-cdc-cli ...................................... SUCCESS [  0.867 s]
[INFO] flink-cdc-dist ..................................... SUCCESS [  8.602 s]
[INFO] flink-cdc-source-connectors ........................ SUCCESS [  0.123 s]
[INFO] flink-connector-debezium ........................... SUCCESS [  1.021 s]
[INFO] flink-cdc-base ..................................... SUCCESS [  1.314 s]
[INFO] flink-connector-test-util .......................... SUCCESS [  0.939 s]
[INFO] flink-connector-db2-cdc ............................ SUCCESS [  1.120 s]
[INFO] flink-connector-mongodb-cdc ........................ SUCCESS [  1.382 s]
[INFO] flink-connector-mysql-cdc .......................... SUCCESS [  2.808 s]
[INFO] flink-connector-oceanbase-cdc ...................... SUCCESS [  1.042 s]
[INFO] flink-connector-oracle-cdc ......................... SUCCESS [  1.668 s]
[INFO] flink-connector-postgres-cdc ....................... SUCCESS [  1.173 s]
[INFO] flink-connector-sqlserver-cdc ...................... SUCCESS [  0.949 s]
[INFO] flink-connector-tidb-cdc ........................... SUCCESS [  0.681 s]
[INFO] flink-connector-vitess-cdc ......................... SUCCESS [  0.645 s]
[INFO] flink-sql-connector-db2-cdc ........................ SUCCESS [  6.082 s]
[INFO] flink-sql-connector-mongodb-cdc .................... SUCCESS [  4.093 s]
[INFO] flink-sql-connector-mysql-cdc ...................... SUCCESS [  4.665 s]
[INFO] flink-sql-connector-oceanbase-cdc .................. SUCCESS [  4.009 s]
[INFO] flink-sql-connector-oracle-cdc ..................... SUCCESS [  4.482 s]
[INFO] flink-sql-connector-postgres-cdc ................... SUCCESS [  4.288 s]
[INFO] flink-sql-connector-sqlserver-cdc .................. SUCCESS [  4.132 s]
[INFO] flink-sql-connector-tidb-cdc ....................... SUCCESS [ 11.927 s]
[INFO] flink-sql-connector-vitess-cdc ..................... SUCCESS [ 11.085 s]
[INFO] flink-cdc-pipeline-connector-mysql ................. SUCCESS [  6.622 s]
[INFO] flink-cdc-pipeline-connector-doris ................. SUCCESS [  5.655 s]
[INFO] flink-cdc-pipeline-connector-starrocks ............. SUCCESS [  3.803 s]
[INFO] flink-cdc-pipeline-connector-kafka ................. SUCCESS [  2.826 s]
[INFO] flink-cdc-pipeline-connector-paimon ................ SUCCESS [ 18.858 s]
[INFO] flink-cdc-pipeline-connector-elasticsearch ......... SUCCESS [ 10.047 s]
[INFO] flink-cdc-e2e-tests ................................ SUCCESS [  0.101 s]
[INFO] flink-cdc-e2e-utils ................................ SUCCESS [  0.167 s]
[INFO] flink-cdc-source-e2e-tests ......................... SUCCESS [  1.723 s]
[INFO] flink-cdc-pipeline-e2e-tests ....................... SUCCESS [  0.981 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  02:46 min
[INFO] Finished at: 2024-12-18T11:03:07+08:00
[INFO] ------------------------------------------------------------------------

```



### 纵向拆解 - YamlPipeline 解析流程
1. parser
   1. yamlparser
   2. TransformParser
2. composer + connector
   1. 
3. runtime
   1. 
4. pipeline model + udf
   1. 
5. flink runtime
   1. 转成 DataStream 逻辑，然后执行
6. 数据实体
   1. event StreamRecord<Event>
7. 计算逻辑
   1. PostTransformOperator extends AbstractStreamOperator
   2. PreTransformOperator extends AbstractStreamOperator
8.  


### 纵向拆解 - 性能优化