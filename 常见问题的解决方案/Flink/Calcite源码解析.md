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
15. 第三方依赖
16. 应用场景
17. 业务通点
18. 行业实践
19. case代码

## calcite源码解析

### 模块化构图，每一个模块对应一个标题
### 理解时间
```
2023年2月20号启动

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

完整理解calcite项目
如果只是在搜索引擎 搜 calcite是远远不够的
calcite + 架构图

calcite + 概念关键词

calcite + 问题排查

calcite + 面试汇总

calcite + 极客挑战赛

calcite + 论坛会议

calcite + 论文

calcite + 前沿分享

calcite + 场景应用

calcite + calcite大佬名字

calcite + 公司项目
等等才能完全熟悉calcite




```



### 入门概念
1. RelOptRule：根据传递给它的 RelOptRuleOperand 来对目标 RelNode 树进行 规则匹配，匹配成功后，会再次调用 matches() 方法进行进一步检查。如果 mathes结果为真，则调用 onMatch() 进行转换。
2. 物化视图-数据格框架(Lattice Framework)：https://cloud.tencent.com/developer/article/2450528
```




ConverterRule：它是 RelOptRule 的子类，专门用来做 数据源之间的转换（Calling convention），ConverterRule 一般会调用对应的 Converter 来完成工作，比如说：JdbcToSparkConverterRule 调用 JdbcToSparkConverter 来完成对 JDBC Table 到 Spark RDD 的转换。
RelNode：relational expression，which contains input RelNode。代表了对数据的一个处理操作，常见的操作有 Sort、Join、Project、Filter、Scan 等。它蕴含的是对整个 Relation 的操作，而不是对具体数据的处理逻辑。
Converter： 用来把一种 RelTrait 转换为另一种 RelTrait 的 RelNode。如 JdbcToSparkConverter 可以把 JDBC 里的 table 转换为 Spark RDD。如果需要在一个 RelNode 中处理来源于异构系统的逻辑表，Calcite 要求先用 Converter 把异构系统的逻辑表转换为同一种 Convention。
RexNode： 行表达式（标量表达式），蕴含的是对一行数据的处理逻辑。每个行表达式都有数据的类型。这是因为在 Valdiation 的过程中，编译器会推导出表达式的结果类型。常见的行表达式包括字面量 RexLiteral， 变量 RexVariable， 函数或操作符调用 RexCall 等。 RexNode 通过 RexBuilder 进行构建。
RelTrait： 用来定义逻辑表的物理相关属性（physical property），三种主要的 trait 类型是：Convention、RelCollation、RelDistribution；
Convention：继承自 RelTrait，类型很少，代表一个单一的数据源，一个 relational expression 必须在同一个 convention 中；
RelTraitDef：主要有三种： ConventionTraitDef：用来代表数据源。 RelCollationTraitDef：用来定义参与排序的字段。 RelDistributionTraitDef：用来定义数据在物理存储上的分布方式（比如：single、hash、range、random 等）；
RelOptCluster： palnner 运行时的环境，保存上下文信息；
RelOptPlanner：也就是 优化器，Calcite 支持 RBO（Rule-Based Optimizer） 和 CBO（Cost-Based Optimizer）。Calcite 的 RBO （HepPlanner）称为 启发式优化器（heuristic implementation ）， 它简单地按 AST 树结构匹配所有已知规则，直到没有规则能够匹配为止；Calcite 的 CBO 称为 火山式优化器（VolcanoPlanner）成本优化器也会匹配并应用规则，当整棵树的成本降低趋于稳定后，优化完成，成本优化器依赖于比较准确的成本估算。RelOptCost 和 Statistic 与成本估算相关；
RelOptCost： 优化器成本模型会依赖。

```


### 参考资料
1. javaCC官网；https://javacc.github.io/javacc/#introduction
2. javaCC文档：https://javacc.github.io/javacc/documentation/
3. javaCC语法：https://github.com/javacc/javacc/blob/master/docs/documentation/grammar.md
4. calcite官网：https://calcite.apache.org/
5. Apache Calcite 学习文档：https://github.com/quxiucheng/apache-calcite-tutorial
6. Calcite原理和代码讲解(一)：https://blog.csdn.net/qq_35494772/article/details/118887267
7. What is cost based optimization：https://www.programmerinterview.com/database-sql/what-is-cost-based-optimization/
8. Apache Calcite：https://arxiv.org/pdf/1802.10233.pdf
9. Hadoop 中新型大数据查询引擎：https://www.infoq.cn/article/new-big-data-hadoop-query-engine-apache-calcite/
10. calcite物化视图详解：https://zhuanlan.zhihu.com/p/484146629
11. Lattices概念：https://calcite.apache.org/docs/lattice.html
12. 一文详解物化视图改写：https://zhuanlan.zhihu.com/p/366658996
13. 一条 SQL 的查询优化之旅【下】：https://juejin.cn/post/7174735770572292157
14. paper推荐
    1.  《Optimizing Queries Using Materialized Views: A Practical, Scalable Solution》
15. Apache Calcite简介：https://km.woa.com/articles/show/383477?kmref=search&from_page=1&no=5
16. 【天穹】SuperSQL技术系列之八：Calcite规则体系与算子优化：https://km.woa.com/group/supersql/articles/show/413307
17. Oceanus团队对Apache Calcite的定制开发介绍：https://km.woa.com/group/36209/articles/show/358664?kmref=search&from_page=1&no=10
18. 灵渊实时计算系统—实现篇：SQL强化模块介绍：https://km.woa.com/group/22680/articles/show/444399?kmref=search&from_page=1&no=2
19. 【Calcite源码解析】SqlNode方言转换：https://km.woa.com/group/51922/articles/show/511978?kmref=search&from_page=1&no=9


### calcite介绍
```
Calcite本质是一个基于JavaCC的CFG Compiler，对一条给定SQL后，很容易通过自顶向下算法(Recursive Desent Parsing, RDP) 得到该SQL的AST的每个节点

SQL流
SQL–>SqlNode –>RelNode/RexNode



最新版本是 gradle编译
gradle学习成本较高
需要配置翻墙代理，才能正常编译全流程
代理写法
systemProp.http.proxyHost=10.74.176.8
systemProp.http.proxyPort=11080
systemProp.http.nonProxyHosts=localhost|127.0.0.1|*.local
systemProp.https.proxyHost=10.74.176.8
systemProp.https.proxyPort=11080

编译命令
 ./gradlew build

测试用例需要以gradle项目打开才能识别到



1.20.0是mvn编译
https://github.com/apache/calcite/tree/calcite-1.20.0

```

### 编译顺序
```
[INFO] Reactor Summary for Calcite 1.20.0:
[INFO] 
[INFO] Calcite ............................................ SUCCESS [  1.553 s]
[INFO] Calcite Linq4j ..................................... SUCCESS [  0.626 s]
[INFO] Calcite Core ....................................... SUCCESS [  4.086 s]
[INFO] Calcite Babel ...................................... SUCCESS [  0.483 s]
[INFO] Calcite Cassandra .................................. SUCCESS [  0.588 s]
[INFO] Calcite Druid ...................................... SUCCESS [  0.286 s]
[INFO] Calcite Elasticsearch .............................. SUCCESS [  0.480 s]
[INFO] Calcite Examples ................................... SUCCESS [  0.050 s]
[INFO] Calcite Example CSV ................................ SUCCESS [  0.278 s]
[INFO] Calcite Example Function ........................... SUCCESS [  0.263 s]
[INFO] Calcite File ....................................... SUCCESS [  1.461 s]
[INFO] Calcite Geode ...................................... SUCCESS [  0.381 s]
[INFO] calcite kafka ...................................... SUCCESS [  0.314 s]
[INFO] Calcite MongoDB .................................... SUCCESS [  0.246 s]
[INFO] Calcite Pig ........................................ SUCCESS [  0.792 s]
[INFO] Calcite Piglet ..................................... SUCCESS [  0.246 s]
[INFO] Calcite Plus ....................................... SUCCESS [  0.297 s]
[INFO] Calcite Server ..................................... SUCCESS [  0.308 s]
[INFO] Calcite Spark ...................................... SUCCESS [  0.989 s]
[INFO] Calcite Splunk ..................................... SUCCESS [  0.257 s]
[INFO] Calcite Ubenchmark ................................. SUCCESS [  3.101 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------


calcite只有 core和linq4j是核心代码
其余模块都是适配不同数据源代码，可以作为新业务接入代码，以及如何使用calcite能力学习材料


```

### JAVACC文件结构
```
javacc_input ::= javacc_options
                 "PARSER_BEGIN" "(" <IDENTIFIER> ")"
                 java_compilation_unit
                 "PARSER_END" "(" <IDENTIFIER> ")"
                 ( production )*
                 <EOF>

{} java代码
[] 可选表达式
() 表达式
```

### JavaCC生成的文件
```

MyParser.java - The generated parser.
MyParserTokenManager.java - The generated token manager (or scanner/lexical analyzer).
MyParserConstants.java - A bunch of useful constants.
Token.java
TokenMsgError.java
SimpleCharStream.java
ParseException.java
```

### 编写production（SQL语法）
```
production ::= javacode_production
             | regular_expr_production
             | bnf_production
             | token_manager_decls

```


### calcite优化入口
```
SQL -> SQLNode -> RelRoot(AbstractRelNode) -> RelOptCluster -> RelOptPlanner

RelOptPlanner
  HepPlanner
  VolcanoPlanner

主调用图
org.apache.calcite.prepare.CalcitePrepareImpl
  prepare2_
  sqlNode = parser.parseStmt(); 解析
  getPreparedResult 执行计划优化
  rePreparedResult
  CalcitePreparingStmt.prepareQueryable
  CalcitePreparingStmt.prepareRel
  CalcitePreparingStmt.prepareSql



CalcitePreparingStmt.prepareSql extends Prepare
sql 转 关系表达式
物化视图优化
plann优化
关系表达式 转 sql(最优引擎方言)
  SqlToRelConverter.convertQuery
  reloadSqlMVs
  Hook.CONVERTED.run(root.rel);
  Hook.TRIMMED.run(root.rel);
  autoOptimize
  PreparedResult preparedResult = implement(root)
  prepareSql


Prepare.autoOptimize
  simpleOptimize
  mixedOptimize
  optimize


Program.getMixedProgram


415865011558656e60d84811fbb314d1c8982959
--story=863341291 支持tHive语法with语句


f85d271e5158222de86a9ae705aacd44c0e63e3c
-story=855592155 Calcite规则集切分优化
```



### RelNode结构拆解
```
核心类
RelOptTable：a relational dataset关系数据集
RelOptSchema：所有RelOptTable的集合
RelOptPlanner：a query optimizer 查询优化计划
RelOptNode：Node in a planner 执行计划中的节点
RelNode：Relational expression 关系表达式，如Sort, Join, Project, Filter, Scan, Sample
RexNode：Row expression 原始表达式
RelTrait：the manifestation of a relational expression trait within a trait definition 关系表达式的性质
RelTraitDef：表示RelTrait的定义或者声明
RelRoot：Root of a tree RelNode
RelDataType：the type of a scalar expression or entire row returned from a relational expression.
SqlKind：

RelOptCluster：An environment for related relational expressions during the optimization of a query
RelOptCost：计算row cost，CPU cost, and I/O cost
RelCollation：Description of the physical ordering of a relational expression
RelShuttle
RelDecorrelator
RelBuilder：栈结构，存放relnode

BiRel

外部类
Convention：Calling convention trait

VolcanoCost：implements RelOptCost
SqlOperatorBinding


Trait
RelMultipleTrait
RelCompositeTrait
RelTraitSet

RexCorrelVariable
RelOptLattice


Enumerable
EnumerableConvention
EnumerableRel


Jdbc
JdbcRel

RelWriter
RelJsonWriter
RelXmlWriter
RelDigestWriter


Converts a trait to canonical form
将特征转换为规范形式




第一阶段
SQL如何转换为RelNode
SqlToRelConverter
convertQuery

SqlImplementor

第一阶段不同算子的实现
DDL
calcite-server
        Table View Materialized Column Function
Create
Alter
Drop

第二阶段
SqlNodeToRexConverter



```

### SQL2Rel拆解
```

核心类
SqlToRelConverter
RexToLixTranslator

Of 的意思 root of something
创建某物的root


  /** Creates a simple RelRoot. */
  public static RelRoot of(RelNode rel, RelDataType rowType, SqlKind kind) {
    final ImmutableIntList refs =
        ImmutableIntList.identity(rowType.getFieldCount());
    final List<String> names = rowType.getFieldNames();
    return new RelRoot(rel, rowType, kind, Pair.zip(refs, names),
        RelCollations.EMPTY);
  }



执行SQL的回调接口

  /** API to put a result set into a statement, being careful to enforce
   * thread-safety and not to overwrite existing open result sets. */
  interface PrepareCallback {
    Object getMonitor();
    void clear() throws SQLException;
    void assign(Signature signature, Frame firstFrame, long updateCount)
        throws SQLException;
    void execute() throws SQLException;
  }




优化SQL

基本数据结构
RexFieldAccess
Blackboard 保存全局信息
nameToNodeMap
scope
SqlNameMatcher
subQueryList

基本架构
register Registers a relational expression.
lookupExp Returns an expression with which to reference a from-list item.


SqlNode to RelRoot
核心方法：convertQuery
    validate
    convertQueryRecursive
    checkConvertedType
    getHboCols


convertQueryRecursive






```



### 物化视图
```
lattices 是 Calcite 针对星型模型和雪花模型推出的一种物化视图框架，主要可以物化星型模型中部分 cube ，能够智能收集信息并智能决定物化哪些维度等。有点类似 kylin 的思路。

Materialized Views：https://calcite.apache.org/docs/materialized_views.html


0058bbd6cc2f6aa680e490d0c4bc30b0d5671b39
--story=874303897 修复跨源MV使用ImprovedOptimizer时无法自动改写的问题
```
### 非重要类
```
Holder
A mutable slot that can contain one object.
A holder is useful for implementing OUT or IN-OUT parameters
It is possible to sub-class to receive events on get or set.

Dummy 虚拟类
Namespace that allows us to define non-abstract methods inside an interface
THREAD_CONTEXT_STACK 


condenseMini
压缩字符串
  public static String condenseMini(String sql) {
    return sql == null ? null : sql.replaceAll(WHITE_SPACE_PAT_S, BLANK).trim();
  }

```
