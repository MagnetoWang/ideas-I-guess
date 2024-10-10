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

### 核心思考
1. calcite为什么那么难用：https://shenzhu.github.io/calcite-user-perspective/



### 入门概念
1. 概念图解：https://www.cnblogs.com/wcgstudy/p/11795886.html
2. RelOptRule：根据传递给它的 RelOptRuleOperand 来对目标 RelNode 树进行 规则匹配，匹配成功后，会再次调用 matches() 方法进行进一步检查。如果 mathes结果为真，则调用 onMatch() 进行转换。
3. 物化视图-数据格框架(Lattice Framework)：https://cloud.tencent.com/developer/article/2450528
4. 
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
9.  Hadoop 中新型大数据查询引擎：https://www.infoq.cn/article/new-big-data-hadoop-query-engine-apache-calcite/
10. calcite物化视图详解：https://zhuanlan.zhihu.com/p/484146629
11. Lattices概念：https://calcite.apache.org/docs/lattice.html
12. 一文详解物化视图改写：https://zhuanlan.zhihu.com/p/366658996
13. 一条 SQL 的查询优化之旅【下】：https://juejin.cn/post/7174735770572292157
14. paper推荐
    1.  《Optimizing Queries Using Materialized Views: A Practical, Scalable Solution》
15. calcite教程
    1. 2021：https://github.com/zabetak/calcite-tutorial/tree/boss21?tab=readme-ov-file
16. Apache Calcite简介：https://km.woa.com/articles/show/383477?kmref=search&from_page=1&no=5
17. 【天穹】SuperSQL技术系列之八：Calcite规则体系与算子优化：https://km.woa.com/group/supersql/articles/show/413307
18. Oceanus团队对Apache Calcite的定制开发介绍：https://km.woa.com/group/36209/articles/show/358664?kmref=search&from_page=1&no=10
19. 灵渊实时计算系统—实现篇：SQL强化模块介绍：https://km.woa.com/group/22680/articles/show/444399?kmref=search&from_page=1&no=2
20. 【Calcite源码解析】SqlNode方言转换：https://km.woa.com/group/51922/articles/show/511978?kmref=search&from_page=1&no=9
21. blog
    1. Julian Hyde
        1.  项目作者解答：https://stackoverflow.com/users/172836/julian-hyde
        2.  语法扩展插件：https://stackoverflow.com/questions/44382826/how-to-change-calcites-default-sql-grammar/44467850#44467850
    2. tsangpo：https://www.zhihu.com/column/tsangpo
    3. dafei1288：http://dafei1288.com/
    4. https://www.zhihu.com/people/yu-qi-30-65
    5. wuyiwen：https://cloud.tencent.com/developer/user/1350579


### 技术流图
1. hivesql 转mapreduce：https://tech.meituan.com/2014/02/12/hive-sql-to-mapreduce.html

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
1. core是核心模块
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
## 横向拆解
1. parser
2. validate
3. optimize
4. execute
5. adapter
6. 必看源码
   1. flink自定义createTable：https://github.com/apache/flink/pull/8548#discussion_r287703560
   2. flink添加水位线：https://github.com/apache/flink/pull/9952

## 横向拆解 - parser
1. 实现一个upload jar语法：https://issues.apache.org/jira/browse/CALCITE-1384
   1. https://github.com/apache/calcite/pull/322
2. 实现一个CREATE MATERIALIZED VIEW语法：https://juejin.cn/post/7209862607975546917
   1. 编写 parserImpls.ftl
   2. 编写 config.fmpp
   3. FreeMarker 生成 parser.jj
   4. JavaCC 解析jj文件 生成 最终java代码
   5. 最终demo：https://github.com/chunyiKit/shared/blob/main/calcite_demo/pom.xml
3. 配置文件说明：https://www.cnblogs.com/rongfengliang/p/16985715.html

### 配置文件
```
├── pom.xml
└── src
    └── main
        ├── codegen  // 模版代码
        │   ├── config.fmpp
        │   ├── data
        │   │   ├── app.json
        │   │   └── style.tdd
        │   ├── includes
        │   │   ├── footer.html
        │   │   ├── func
        │   │   │   └── agg.ftl
        │   │   └── macros
        │   │       └── login.ftl
        │   └── templates
        │       ├── app.jj
        │       └── index.html
        ├── java
        └── resources



```

### 如何基于Calcite的Select语法，扩展新关键词比如distributed和sorted，不改动calcite的parser.jj
#### 原始参考
```
/**
 * Parses a leaf SELECT expression without ORDER BY.
 */
SqlSelect SqlSelect() :
{
    final List<SqlLiteral> keywords = new ArrayList<SqlLiteral>();
    final SqlLiteral keyword;
    final SqlNodeList keywordList;
    final List<SqlNode> selectList = new ArrayList<SqlNode>();
    final SqlNode fromClause;
    final SqlNode where;
    final SqlNodeList groupBy;
    final SqlNode having;
    final SqlNodeList windowDecls;
    final SqlNode qualify;
    final List<SqlNode> hints = new ArrayList<SqlNode>();
    final Span s;
}
{
    <SELECT> { s = span(); }
    [ <HINT_BEG> AddHint(hints) ( <COMMA> AddHint(hints) )* <COMMENT_END> ]
    SqlSelectKeywords(keywords)
    (
        <STREAM> {
            keywords.add(SqlSelectKeyword.STREAM.symbol(getPos()));
        }
    )?
    (
        keyword = AllOrDistinct() { keywords.add(keyword); }
    )?
    {
        keywordList = new SqlNodeList(keywords, s.addAll(keywords).pos());
    }
    AddSelectItem(selectList)
    ( <COMMA> AddSelectItem(selectList) )*
    (
        <FROM> fromClause = FromClause()
        ( where = Where() | { where = null; } )
        ( groupBy = GroupBy() | { groupBy = null; } )
        ( having = Having() | { having = null; } )
        ( windowDecls = Window() | { windowDecls = null; } )
        ( qualify = Qualify() | { qualify = null; } )
    |
        E() {
            fromClause = null;
            where = null;
            groupBy = null;
            having = null;
            windowDecls = null;
            qualify = null;
        }
    )
    {
        return new SqlSelect(s.end(this), keywordList,
            new SqlNodeList(selectList, Span.of(selectList).pos()),
            fromClause, where, groupBy, having, windowDecls, qualify,
            null, null, null, new SqlNodeList(hints, getPos()));
    }
}



<#if (parser.createStatementParserMethods!default.parser.createStatementParserMethods)?size != 0>
/**
 * Parses a CREATE statement.
 */
SqlCreate SqlCreate() :
{
    final Span s;
    boolean replace = false;
    final SqlCreate create;
}
{
    <CREATE> { s = span(); }
    [
        <OR> <REPLACE> {
            replace = true;
        }
    ]
    (
<#-- additional literal parser methods are included here -->
<#list (parser.createStatementParserMethods!default.parser.createStatementParserMethods) as method>
        create = ${method}(s, replace)
        <#sep>| LOOKAHEAD(2) </#sep>
</#list>
    )
    {
        return create;
    }
}
</#if>


```

#### flink在SqlCreate基础上，新增 SqlCreateTable
```

SqlCreate SqlCreateTable(Span s, boolean replace) :
{
    final SqlParserPos startPos = s.pos();
    SqlIdentifier tableName;
    SqlNodeList primaryKeyList = SqlNodeList.EMPTY;
    List<SqlNodeList> uniqueKeysList = new ArrayList<SqlNodeList>();
    SqlWatermark watermark = null;
    SqlNodeList columnList = SqlNodeList.EMPTY;
	SqlCharStringLiteral comment = null;

    SqlNodeList propertyList = SqlNodeList.EMPTY;
    SqlNodeList partitionColumns = SqlNodeList.EMPTY;
    SqlParserPos pos = startPos;
}
{
    <TABLE>

    tableName = CompoundIdentifier()
    [
        <LPAREN> { pos = getPos(); TableCreationContext ctx = new TableCreationContext();}
        TableColumn(ctx)
        (
            <COMMA> TableColumn(ctx)
        )*
        {
            pos = pos.plus(getPos());
            columnList = new SqlNodeList(ctx.columnList, pos);
            primaryKeyList = ctx.primaryKeyList;
            uniqueKeysList = ctx.uniqueKeysList;
            watermark = ctx.watermark;
        }
        <RPAREN>
    ]
    [ <COMMENT> <QUOTED_STRING> {
        String p = SqlParserUtil.parseString(token.image);
        comment = SqlLiteral.createCharString(p, getPos());
    }]
    [
        <PARTITIONED> <BY>
        partitionColumns = ParenthesizedSimpleIdentifierList() {
            if (!((FlinkSqlConformance) this.conformance).allowCreatePartitionedTable()) {
                throw SqlUtil.newContextException(getPos(),
                    ParserResource.RESOURCE.createPartitionedTableIsOnlyAllowedForHive());
            }
        }
    ]
    [
        <WITH>
        propertyList = TableProperties()
    ]
    {
        return new SqlCreateTable(startPos.plus(getPos()),
                tableName,
                columnList,
                primaryKeyList,
                uniqueKeysList,
                propertyList,
                partitionColumns,
                watermark,
                comment);
    }
}


```

#### 可行方案
1. 新增一个SqlTableDistributed
2. 参入进select中
3. 比较耗时间，需要验证


## 横向拆解 - validate
1. 必看
   1. https://shenzhu.github.io/calcite-user-perspective/
2. Calcite SQL验证流程：https://liebing.org.cn/apache-calcite-sql-validator.html
3. catalog 原理：https://strongduanmu.com/blog/explore-apache-calcite-system-catalog-implementation.html
4. 校验器整体设计：https://strongduanmu.com/blog/in-depth-exploration-of-implementation-principle-of-apache-calcite-sql-validator.html
5. Calcite系列(七)：执行流程-合法性校验：https://cloud.tencent.com/developer/article/2410893
6. 校验流程：https://github.com/Mulavar/note_selina/blob/38533dade5f30ca29a83ef490b2bb88d2658310c/%E6%BA%90%E7%A0%81%E7%AC%94%E8%AE%B0/Calcite/Calcite%E6%A0%A1%E9%AA%8C%E6%B5%81%E7%A8%8B.md
7. drill自定义的校验器：https://github.com/hboutemy/drill/blob/3bbef5d961fe568f9797abbea0c785ee2eedaaad/exec/java-exec/src/main/java/org/apache/drill/exec/planner/sql/conversion/DrillValidator.java#L24
8. 校验处理可简化为:  validate = Namespace#validate + Scope#validateExpr + 额外校验
   1. 表是否存在
   2. 字段类型是否匹配
   3. Function校验
   4. 隐式转换
   5. DQL校验：SqlValidator#deriveType
   6. DML校验：SqlValidator#checkTypeAssignment
9.  源码case
   1. SqlValidatorTest
   2. core/src/test/java/org/apache/calcite/test/MaterializedViewTester.java
      1. toRel 测试
   3. SqlParserTest
10. 概念
   1. SqlValidatorCatalogReader：元数据读取器
   2. SqlValidatorNamespace：描述了 SQL 查询返回的关系，一个 SQL 查询可以拆分为多个部分，查询的列组合，表名等等，当中每个部分都有一个对应的 SqlValidatorNamespace
   3. SqlValidatorScope：可以认为是校验流程中每个 SqlNode 的工作上下文，当校验表达式时，通过 SqlValidatorScope 的 resolve 方法进行解析，如果成功的话会返回对应的 SqlValidatorNamespace 描述结果类型

```
相关类
import org.apache.calcite.sql.validate.SqlValidator;
import org.apache.calcite.sql.validate.SqlValidatorCatalogReader;
import org.apache.calcite.sql.validate.SqlValidatorImpl;
import org.apache.calcite.sql.validate.SqlValidatorScope;
import org.apache.calcite.sql.validate.SqlValidatorUtil;

SqlValidatorUtil


```

### calcite 测试用例如何执行元数据和校验



### flink如何元数据注册
1. FlinkCalciteCatalogReaderTest 初始化元数据
2. planner模块
   1. class CatalogReader extends CalciteCatalogReader 
3. blink模块
   1. class FlinkCalciteCatalogReader extends CalciteCatalogReader
```

```


### flink如何复用validator能力
1. FlinkCalciteSqlValidator

## 横向拆解 - optimize

### calcite 规则集
1. RelOptRulesTest
2. CoreRules


## 横向拆解 - execute


## 横向拆解 - adapter
### 学习路径
1. 自定义数据库
   1. 编写 model.json
   2. 自定义 SchemaFactory
   3. 自定义 Schema（像一个“没有存储层的databse”一样，Calcite不会去了解任何文件格式）
   4. 自定义Table
   5. 自定义 Enumerator
2. demo参考
   1. 用sql查询csv文件：https://github.com/objcoding/calcite-demo
   2. 双表查询+打印执行计划：http://dafei1288.com/2023/06/22/1001_calcite-sql-parser-demo/

### adapter - ScannableTable FilterableTable TranslatableTable
1. 概念说明：https://objcoding.com/2021/01/17/calcite/


### adapter - spark
1. 核心类：SparkHandlerImpl


### adapter - csv
1. 源码位置：example/csv/src/test/java/org/apache/calcite/test/CsvTest.java
2. 如何新增csv格式的SQL解析：https://strongduanmu.com/wiki/calcite/tutorial.html
3. CsvTable：csv表定义
4. CsvTableFactory： model.json文件定义表
5. Flavor：calcite表含义


### adapter - csv文件读取流程
1. ModelHandler.ExtraOperand.BASE_DIRECTORY.camelName
2. File
3. org.apache.calcite.util.Sources -> Source
   1. reader 支持解析gz文件
4. CsvScannableTable

### adapter - csv文件Schema解析流程
1. 个人代码截图：https://d7pii8p7gc.feishu.cn/wiki/EIZYw7c9di4hdWkJSEJcdC6nnKh
2. schema介绍：https://github.com/quxiucheng/apache-calcite-tutorial/tree/master/calcite-tutorial-3-schema
3. schmea发现：https://dongzl.github.io/2020/11/10/35-Apache-Calcite-Overview-Tutorial/index.html
4. schema是延迟解析，可以从json文件解析字段类型，也可以在第一次执行sql的时候，再解析出字段类型
   1. 关键代码 calciteConnection.prepareStatement(sql)
5. 具体实现流程
   1. 继承父类： CsvSchema extends AbstractSchema
   2. 实现方法：getTableMap 和 createTableMap
   3. 解析字段：getFieldTypes —> CsvEnumerator.deduceRowType






## 纵向拆解
1. javacc
2. 规则集
   1. RuleSetBuilder
   2. SparkHandler
   3. RelOptRule

## 纵向拆解 - JavaCC
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
## 纵向拆解 - 方言互转
1. 介绍：https://blog.csdn.net/skyyws/article/details/124828049
2. SparkSqlDialect
3. 



## 纵向拆解 - calcite 元数据机制 schema
1. calaog原理：https://strongduanmu.com/blog/explore-apache-calcite-system-catalog-implementation.html
2. presto注册catalog：https://github.com/baibaichen/Blog2/blob/0c23b6a3636b6fc46fed7f4a231d9db959186615/Optimizer/Inside%20Presto%20Optimizer.md

### Schema实现
```
TranslatableTable 、ProjectableFilterableTable 和 FilterableTable extends AbstractTable


```

### Table实现
```
CalciteSchema extends SchemaPlus extends Schema


```

## 纵向拆解 - 规则重写
1. 如何使用calcite rule做SQL重写（上）：http://dafei1288.com/2023/08/10/1003-calcite-sql-rule/



## 竞品对比
### anltr 和 javacc 区别
1. anltr场景：
   1. coral：https://github.com/linkedin/coral/blob/b50776111910a9a3857dd516651b611f39ddc33a/coral-hive/src/main/antlr/roots/com/linkedin/coral/hive/hive2rel/parsetree/parser/HiveParser.g
   2. hiveSQL：https://github.com/apache/hive/blob/master/hplsql/src/main/antlr4/org/apache/hive/hplsql/Hplsql.g4
   3. 


### flink兼容hive语法
1. 比如Sort/Cluster/Distributed by Clause 暂不支持
   1. The Hive dialect is mainly used in batch mode. Some Hive’s syntax (Sort/Cluster/Distributed BY, Transform, etc.) haven’t been supported in streaming mode yet.
2. flinkSQL是没有的，hiveSQL 2 FlinkSQL 通过calcite