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
2. 注册一个UDTF都麻烦的要死！文档稍微好好写都不会这样来回调试，还要调研flink怎么注册UDTF
3. 必看代码
   1. core/src/test/java/org/apache/calcite/sql/parser/SqlParserTest.java
   2. core/src/test/java/org/apache/calcite/test/SqlValidatorTest.java
   3. core/src/test/java/org/apache/calcite/rel/rules/SortRemoveRuleTest.java
   4. core/src/test/java/org/apache/calcite/tools/PlannerTest.java
   5. core/src/test/java/org/apache/calcite/test/HepPlannerTest.java
   6. core/src/test/java/org/apache/calcite/test/MutableRelTest.java
   7. core/src/test/java/org/apache/calcite/test/RelBuilderTest.java
   8. core/src/test/java/org/apache/calcite/test/RelOptRulesTest.java
   9. core/src/test/java/org/apache/calcite/rel/rel2sql/RelToSqlConverterTest.java
   10. core/src/test/java/org/apache/calcite/test/SqlToRelConverterTest.java



### 概念地图
1. 概念图解：https://www.cnblogs.com/wcgstudy/p/11795886.html
2. 物化视图-数据格框架(Lattice Framework)：https://cloud.tencent.com/developer/article/2450528
3. Thunk：程序地址
4. RexNode：行表达式（标量表达式），蕴含的是对一行数据的处理逻辑。每个行表达式都有数据的类型
   1. RexProgram：表达式管理 组件 可以做到全局表达式融合
   2. RexBuilder：构建RexNode 组件
   3. RexUtil：类型推导工具
   4. RexShuttle：
   5. RexLiteral
   6. RexVariable
   7. RexCall
   8. 
5. SqlToRelConverter：sql转换关系表达式 组件
   1. SubQueryConverter：子查询转换器 组件
   2. SqlNodeToRexConverter：sql转换标量表达式 组件 抽象接口
   3. SqlNodeToRexConverterImpl：sql转换标量表达式 组件 具体实现逻辑
   4. SqlRexConvertlet：sql转换标量表达式 抽象接口
   5. SqlRexConvertletTable：sql转换标量表达式 表 抽象接口
   6. ReflectiveConvertletTable：sql转换标量表达式 表 通过反射机制实现
      1. 反射是为了调用UDF函数，UDF也属于表达式一个计算逻辑
   7. StandardConvertletTable：sql转换标量表达式 表 内置表达式实现 比如 加减乘除
6. RelDataType 关系表达式数据类型
   1. SqlOperandTypeChecker
   2. Consistency：Strategy used to make arguments consistent
   3. SqlOperandTypeInference
   4. SqlReturnTypeInference
```




ConverterRule：它是 RelOptRule 的子类，专门用来做 数据源之间的转换（Calling convention），ConverterRule 一般会调用对应的 Converter 来完成工作，比如说：JdbcToSparkConverterRule 调用 JdbcToSparkConverter 来完成对 JDBC Table 到 Spark RDD 的转换。
RelNode：relational expression，which contains input RelNode。代表了对数据的一个处理操作，常见的操作有 Sort、Join、Project、Filter、Scan 等。它蕴含的是对整个 Relation 的操作，而不是对具体数据的处理逻辑。
Converter： 用来把一种 RelTrait 转换为另一种 RelTrait 的 RelNode。如 JdbcToSparkConverter 可以把 JDBC 里的 table 转换为 Spark RDD。如果需要在一个 RelNode 中处理来源于异构系统的逻辑表，Calcite 要求先用 Converter 把异构系统的逻辑表转换为同一种 Convention。

RelTrait： 用来定义逻辑表的物理相关属性（physical property），三种主要的 trait 类型是：Convention、RelCollation、RelDistribution；
Convention：继承自 RelTrait，类型很少，代表一个单一的数据源，一个 relational expression 必须在同一个 convention 中；
RelTraitDef：主要有三种： ConventionTraitDef：用来代表数据源。 RelCollationTraitDef：用来定义参与排序的字段。 RelDistributionTraitDef：用来定义数据在物理存储上的分布方式（比如：single、hash、range、random 等）；
RelOptCluster： palnner 运行时的环境，保存上下文信息；
RelOptPlanner：也就是 优化器，Calcite 支持 RBO（Rule-Based Optimizer） 和 CBO（Cost-Based Optimizer）。Calcite 的 RBO （HepPlanner）称为 启发式优化器（heuristic implementation ）， 它简单地按 AST 树结构匹配所有已知规则，直到没有规则能够匹配为止；Calcite 的 CBO 称为 火山式优化器（VolcanoPlanner）成本优化器也会匹配并应用规则，当整棵树的成本降低趋于稳定后，优化完成，成本优化器依赖于比较准确的成本估算。RelOptCost 和 Statistic 与成本估算相关；
RelOptCost： 优化器成本模型会依赖。

```


### 参考资料
1. 工业应用：https://www.victorchu.info/posts/121d8993/#%E5%B7%A5%E4%B8%9A%E5%92%8C%E5%AD%A6%E6%9C%AF%E9%87%87%E7%94%A8
2. javaCC官网；https://javacc.github.io/javacc/#introduction
3. javaCC文档：https://javacc.github.io/javacc/documentation/
4. javaCC语法：https://github.com/javacc/javacc/blob/master/docs/documentation/grammar.md
5. calcite官网：https://calcite.apache.org/
6. Apache Calcite 学习文档：https://github.com/quxiucheng/apache-calcite-tutorial
7. Calcite原理和代码讲解(一)：https://blog.csdn.net/qq_35494772/article/details/118887267
8. What is cost based optimization：https://www.programmerinterview.com/database-sql/what-is-cost-based-optimization/
9. Apache Calcite：https://arxiv.org/pdf/1802.10233.pdf
10. Hadoop 中新型大数据查询引擎：https://www.infoq.cn/article/new-big-data-hadoop-query-engine-apache-calcite/
11. calcite物化视图详解：https://zhuanlan.zhihu.com/p/484146629
12. Lattices概念：https://calcite.apache.org/docs/lattice.html
13. 一文详解物化视图改写：https://zhuanlan.zhihu.com/p/366658996
14. 一条 SQL 的查询优化之旅【下】：https://juejin.cn/post/7174735770572292157
15. paper推荐
    1.  《Optimizing Queries Using Materialized Views: A Practical, Scalable Solution》
16. calcite教程
    1. 2021：https://github.com/zabetak/calcite-tutorial/tree/boss21?tab=readme-ov-file
17. Apache Calcite简介：https://km.woa.com/articles/show/383477?kmref=search&from_page=1&no=5
18. 【天穹】SuperSQL技术系列之八：Calcite规则体系与算子优化：https://km.woa.com/group/supersql/articles/show/413307
19. Oceanus团队对Apache Calcite的定制开发介绍：https://km.woa.com/group/36209/articles/show/358664?kmref=search&from_page=1&no=10
20. 灵渊实时计算系统—实现篇：SQL强化模块介绍：https://km.woa.com/group/22680/articles/show/444399?kmref=search&from_page=1&no=2
21. 【Calcite源码解析】SqlNode方言转换：https://km.woa.com/group/51922/articles/show/511978?kmref=search&from_page=1&no=9
22. blog
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


### 代码块截图
```java

        SqlParser parser = SqlParser.create(sql,
                SqlParser.configBuilder()
                        .setParserFactory(SampleLakeSqlParserImpl.FACTORY)
                        .setQuoting(Quoting.BACK_TICK)
                        .setUnquotedCasing(Casing.TO_UPPER)
                        .setQuotedCasing(Casing.UNCHANGED)
                        .setConformance(SqlConformanceEnum.DEFAULT)
                        .build());

        try {
            // 解析SQL语句
            SqlNode sqlNode = parser.parseQuery();
            // 输出解析后的SQL节点
            System.out.println("Parsed SQL Node: " + sqlNode);
        } catch (SqlParseException e) {
            e.printStackTrace();
        }
```

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
4. 概念
   1. SqlConformance：用来判断不同SQL的兼容模式，比如mySQL oracle，对groupby limit是否是支持
   2. 

### 配置文件
```shell
├── pom.xml
└── src
    └── main
        ├── codegen  // template code
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

### coral扩展示例
1. https://github.com/linkedin/coral

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
2. 掺入进select中
3. 比较耗时间，需要验证






## 横向拆解 - validate
1. 文章必看
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
9.  源码必看
   1. SqlValidatorTest
   2. core/src/test/java/org/apache/calcite/test/MaterializedViewTester.java
      1. toRel 测试
   3. SqlParserTest
10. 概念
   1. SchemaPlus：元数据描述
   2. Frameworks： 可独立调用calcite模块的工具框架
      1. 创建元数据
      2. 获取计划图
   3. FrameworkConfig
      1. 框架基础配置
   4. AbstractTable
      1. 注册元数据的抽象表定义
   5. RelDataType
      1. 注册calcite元数据的数据类型 - 行级
   6.  RelDataTypeFactory
       1. 通过工厂定义calcite的数据类型 - 行级
   7.  BasicSqlType
       1.  calcite对应的SQL数据类型 - 字段级
   8. SqlTypeFactoryImpl
       1.  通过工厂定义calcite的数据类型 - 字段级
   9. CalciteConnectionConfig  
   10. CalciteCatalogReader
       1.  
   11. SqlValidator
       1. SQL校验器
   12. SqlValidatorUtil
       1. 校验工具
   13. SqlValidatorCatalogReader：元数据读取器
   14. SqlValidatorNamespace：描述了 SQL 查询返回的关系，一个 SQL 查询可以拆分为多个部分，查询的列组合，表名等等，当中每个部分都有一个对应的 SqlValidatorNamespace
   15. 
11. 进阶概念
    1. SqlValidatorScope：可以认为是校验流程中每个 SqlNode 的工作上下文，当校验表达式时，通过 SqlValidatorScope 的 resolve 方法进行解析，如果成功的话会返回对应的 SqlValidatorNamespace 描述结果类型
    2. CatalogScope：

```
相关类
import org.apache.calcite.sql.validate.SqlValidator;
import org.apache.calcite.sql.validate.SqlValidatorCatalogReader;
import org.apache.calcite.sql.validate.SqlValidatorImpl;
import org.apache.calcite.sql.validate.SqlValidatorScope;
import org.apache.calcite.sql.validate.SqlValidatorUtil;

SqlValidatorUtil


```

### calcite 定义一个schema 示例
1. 源码参考
   1. core/src/test/java/org/apache/calcite/schemas/HrClusteredSchema.java
```
 public HrClusteredSchema() {
    tables = ImmutableMap.<String, Table>builder()
        .put("emps",
            new PkClusteredTable(
                factory ->
                    new RelDataTypeFactory.Builder(factory)
                        .add("empid", factory.createJavaType(int.class))
                        .add("deptno", factory.createJavaType(int.class))
                        .add("name", factory.createJavaType(String.class))
                        .add("salary", factory.createJavaType(int.class))
                        .add("commission", factory.createJavaType(Integer.class))
                        .build(),
                ImmutableBitSet.of(0),
                Arrays.asList(
                    new Object[]{100, 10, "Bill", 10000, 1000},
                    new Object[]{110, 10, "Theodore", 11500, 250},
                    new Object[]{150, 10, "Sebastian", 7000, null},
                    new Object[]{200, 20, "Eric", 8000, 500})))
        .put("depts",
            new PkClusteredTable(
                factory ->
                    new RelDataTypeFactory.Builder(factory)
                        .add("deptno", factory.createJavaType(int.class))
                        .add("name", factory.createJavaType(String.class))
                        .build(),
                ImmutableBitSet.of(0),
                Arrays.asList(
                    new Object[]{10, "Sales"},
                    new Object[]{30, "Marketing"},
                    new Object[]{40, "HR"})))
        .build();
  }

```

### validate流程
1. validate
2. validateScopedExpression
   1. SqlSelect.validate
      1. validateQuery -> validateNamespace -> AbstractNamespace.validate
      2. validateSelect -> validateFrom -> validateQuery -> IdentifierNamespace.validateImpl -> resolveImpl -> newValidationError
3. validateQuery
   1. validateNamespace
   2. validateModality
   3. validateAccess
4. validateSelect
   1. validateFrom
   2. validateWhereClause
   3. validateGroupClause
   4. validateHavingClause
   5. validateWindowClause

### calcite 测试用例如何执行元数据和校验
1. 元数据相当于 namespaceScope
2. 从 SqlNode 中提取 table和列，然后进行lookup查询，来进行最基础的校验逻辑


### calcite新增一个数据类型

### 新增校验逻辑规则


### 新增 UDF
1. 参考calcite源码：
   1. 官方文档：https://github.com/julianhyde/calcite/blob/1095-not-precedence/site/_docs/reference.md#operator-precedence
   2. 函数集：core/src/main/java/org/apache/calcite/sql/fun/SqlStdOperatorTable.java
   3. 定义类，动态加载函数：core/src/test/java/org/apache/calcite/tools/PlannerTest.java#testValidateUserDefinedAggregate
   4. udf测试：core/src/test/java/org/apache/calcite/test/UdfTest.java
   5. 定义同名不同参数函数：core/src/test/java/org/apache/calcite/util/Smalls.java
   6. 查询udf测试代码：core/src/test/java/org/apache/calcite/prepare/LookupOperatorOverloadsTest.java
2. 函数全流程
   1. 定义函数 Function -> 再定义 Sqlfunction
      1. Function
         1. ScalarFunction ScalarFunctionImpl
         2. AggregateFunction AggregateFunctionImpl
         3. TableFunction TableFunctionImpl
      2. Sqlfunction
         1. SqlUserDefinedFunction 
         2. SqlUserDefinedAggFunction
         3. SqlUserDefinedTableFunction
         4. LookupOperatorOverloadsTest
   2. 注册函数表  Sqlfunction 注册到 SqlOperatorTable 
      1. 如 ReflectiveSqlOperatorTable 通过class就可以自动注册
         1. 也可以用 register(SqlOperator op)
      2. ListSqlOperatorTable 可以直接 add sqlfunction，适合动态化加载函数到函数表
      3. ChainedSqlOperatorTable
         1. add(SqlOperatorTable table) 整合一张更大函数宽表
   3. 函数表 注册到 FrameConfig 至此 全流程完成
   4. 初始化plan 执行SQL验证
3. CalciteCatalogReader
   1. 注册UDF lookupOperatorOverloads
   2. 支持 classname 转 Function 再转 SqlOperator
   3. 加载元数据实现 ModelHandler.addFunctions
   4. 反射方式加载函数
      1. TableFunctionImpl.create(clazz, Util.first(methodName, "eval"));
      2. AggregateFunctionImpl.create(clazz);
      3. ScalarFunctionImpl.create(clazz, Util.first(methodName, "eval"));
   5. toOp Converts a function to a {@link org.apache.calcite.sql.SqlOperator}.
      1. 
4. SqlOperatorTable
   1. 需要实现 lookupOperatorOverloads
   2. SqlStdOperatorTable：所有内置函数表
   3. ReflectiveSqlOperatorTable：注册表，业务需要继承，参考flink 和 OracleSqlOperatorTable
   4. ChainedSqlOperatorTable：链式方法，加载所有函数表，参考flink
5. 内置函数
   1. BuiltInMethod
6. 聚合函数
   1. 定义
      1. SqlSumAggFunction —> SqlAggFunction -> SqlFunction
   2. 注册到函数表 ReflectiveSqlOperatorTable
      1. public static final SqlAggFunction SUM = new SqlSumAggFunction(null);
7. Sqlfunction详解
   1. SqlIdentifier：自定义必须初始化，不然校验过程会失败
      1. A user-defined function will have a value for {@code sqlIdentifier}; for a built-in function it will be null.
   2. OperandTypes：
      1. SqlSingleOperandTypeChecker NILADIC = family();
         1. 对 niladic 函数（例如 CURRENT_DATE）的调用不接受括号。在某些一致性级别中，可以接受带括号的调用（例如 CURRENT_DATE()）
         2. 无参数的函数通常也叫做 Niladic Function
         3. https://strongduanmu.com/wiki/calcite/reference.html
         4. https://strongduanmu.com/blog/apache-calcite-catalog-udf-function-implementation-and-extension.html
      2. SqlOperandTypeChecker VARIADIC
   3. returnTypeInference  strategy to use for return type inference
   4. operandTypeInference strategy to use for parameter type inference
   5. operandTypeChecker   strategy to use for parameter type checking
8. 函数定义：接受参数并返回结果的命名表达式
#### 函数类型
1. SqlLibrary 函数集合
   1. SqlLibraryOperators
   2. SqlStdOperatorTable
2. SqlFunction 函数种类
   1. SqlAggFunction
   2. SqlUserDefinedFunction 需要实现一个实体类class作为参数，才能被解析
   3. SqlUserDefinedTableMacro 需要实现一个实体类class作为参数，才能被解析
   4. SqlUserDefinedTableFunction 需要实现一个实体类class作为参数，才能被解析
   5. SqlUserDefinedAggFunction 需要实现一个实体类class作为参数，才能被解析
3. 


#### 函数类型 - 输出结果校验示例
```

        returnTypesMap.put("BOOLEAN", ReturnTypes.BOOLEAN);
        returnTypesMap.put("DATE", ReturnTypes.DATE);
        returnTypesMap.put("TIME", ReturnTypes.TIME);
        returnTypesMap.put("DOUBLE", ReturnTypes.DOUBLE);
        returnTypesMap.put("INTEGER", ReturnTypes.INTEGER);
        returnTypesMap.put("BIGINT", ReturnTypes.BIGINT);
        returnTypesMap.put("VARCHAR_2000", ReturnTypes.VARCHAR_2000);

```


#### 函数类型 - 输入参数校验示例
1. SqlOperandTypeChecker
   1. FamilyOperandTypeChecker
   2. SqlSingleOperandTypeChecker
   3. LiteralOperandTypeChecker
```
可变形参

DECODE
  /** The "DECODE(v, v1, result1, [v2, result2, ...], resultN)" function. */
  @LibraryOperator(libraries = {ORACLE})
  public static final SqlFunction DECODE =
      new SqlFunction("DECODE", SqlKind.DECODE, DECODE_RETURN_TYPE, null,
          OperandTypes.VARIADIC, SqlFunctionCategory.SYSTEM);


  /** Operand type-checking strategy that allows one or more operands. */
  public static final SqlOperandTypeChecker ONE_OR_MORE =
      variadic(SqlOperandCountRanges.from(1));
new SqlFunction("DECODE", SqlKind.DECODE, DECODE_RETURN_TYPE, null,
          OperandTypes.ONE_OR_MORE, SqlFunctionCategory.SYSTEM)
```


#### 函数类型 - 标量函数示例
```


  /**
   * Uses SqlOperatorTable.useDouble for its return type since we don't know
   * what the result type will be by just looking at the operand types. For
   * example POW(int, int) can return a non integer if the second operand is
   * negative.
   */
  public static final SqlFunction POWER =
      new SqlFunction(
          "POWER",
          SqlKind.OTHER_FUNCTION,
          ReturnTypes.DOUBLE_NULLABLE,
          null,
          OperandTypes.NUMERIC_NUMERIC,
          SqlFunctionCategory.NUMERIC);



  public SqlCoalesceFunction() {
    // NOTE jvs 26-July-2006:  We fill in the type strategies here,
    // but normally they are not used because the validator invokes
    // rewriteCall to convert COALESCE into CASE early.  However,
    // validator rewrite can optionally be disabled, in which case these
    // strategies are used.
    super("COALESCE",
        SqlKind.COALESCE,
        ReturnTypes.cascade(ReturnTypes.LEAST_RESTRICTIVE,
            SqlTypeTransforms.LEAST_NULLABLE),
        null,
        OperandTypes.SAME_VARIADIC,
        SqlFunctionCategory.SYSTEM);
  }

```


#### 函数类型 - udaf 示例
1. core/src/main/java/org/apache/calcite/sql/fun/SqlStdOperatorTable.java
2. calcite
   1. SqlUserDefinedAggFunction -> SqlAggFunction -> SqlFunction
```
/** Creates a built-in or user-defined SqlAggFunction or window function.
   *
   * <p>A user-defined function will have a value for {@code sqlIdentifier}; for
   * a built-in function it will be null. */
  protected SqlAggFunction(
      String name,
      SqlIdentifier sqlIdentifier,
      SqlKind kind,
      SqlReturnTypeInference returnTypeInference,
      SqlOperandTypeInference operandTypeInference,
      SqlOperandTypeChecker operandTypeChecker,
      SqlFunctionCategory funcType,
      boolean requiresOrder,
      boolean requiresOver,
      Optionality requiresGroupOrder) {
    super(name, sqlIdentifier, kind, returnTypeInference, operandTypeInference,
        operandTypeChecker, null, funcType);
    this.requiresOrder = requiresOrder;
    this.requiresOver = requiresOver;
    this.requiresGroupOrder = Objects.requireNonNull(requiresGroupOrder);
  }

SUM函数
public SqlSumAggFunction(RelDataType type) {
    super(
        "SUM",
        null,
        SqlKind.SUM,
        ReturnTypes.AGG_SUM,
        null,
        OperandTypes.NUMERIC,
        SqlFunctionCategory.NUMERIC,
        false,
        false,
        Optionality.FORBIDDEN);
    this.type = type;
  }


COLLECT 函数
new SqlAggFunction("COLLECT",
          null,
          SqlKind.COLLECT,
          ReturnTypes.TO_MULTISET,
          null,
          OperandTypes.ANY,
          SqlFunctionCategory.SYSTEM, false, false,
          Optionality.OPTIONAL) {
      };

Count

  public SqlCountAggFunction(String name) {
    this(name, CalciteSystemProperty.STRICT.value() ? OperandTypes.ANY : OperandTypes.ONE_OR_MORE);
  }

  public SqlCountAggFunction(String name,
      SqlOperandTypeChecker sqlOperandTypeChecker) {
    super(name, null, SqlKind.COUNT, ReturnTypes.BIGINT, null,
        sqlOperandTypeChecker, SqlFunctionCategory.NUMERIC, false, false,
        Optionality.FORBIDDEN);
  }


MinMax
  /** Creates a SqlMinMaxAggFunction. */
  public SqlMinMaxAggFunction(SqlKind kind) {
    super(kind.name(),
        null,
        kind,
        ReturnTypes.ARG0_NULLABLE_IF_EMPTY,
        null,
        OperandTypes.COMPARABLE_ORDERED,
        SqlFunctionCategory.SYSTEM,
        false,
        false,
        Optionality.FORBIDDEN);
    this.argTypes = ImmutableList.of();
    this.minMaxKind = MINMAX_COMPARABLE;
    Preconditions.checkArgument(kind == SqlKind.MIN
        || kind == SqlKind.MAX);
  }


JSON
  public SqlJsonArrayFunction() {
    super("JSON_ARRAY", SqlKind.OTHER_FUNCTION, ReturnTypes.VARCHAR_2000,
        InferTypes.ANY_NULLABLE, OperandTypes.VARIADIC, SqlFunctionCategory.SYSTEM);
  }


  public SqlJsonArrayAggAggFunction(SqlKind kind,
      SqlJsonConstructorNullClause nullClause) {
    super(kind + "_" + nullClause.name(), null, kind, ReturnTypes.VARCHAR_2000,
        InferTypes.ANY_NULLABLE, OperandTypes.family(SqlTypeFamily.ANY),
        SqlFunctionCategory.SYSTEM, false, false, Optionality.OPTIONAL);
    this.nullClause = Objects.requireNonNull(nullClause);
  }


substring
 SqlSubstringFunction() {
    super(
        "SUBSTRING",
        SqlKind.OTHER_FUNCTION,
        ReturnTypes.ARG0_NULLABLE_VARYING,
        null,
        null,
        SqlFunctionCategory.STRING);
  }


lead lag
  private static final SqlSingleOperandTypeChecker OPERAND_TYPES =
      OperandTypes.or(
          OperandTypes.ANY,
          OperandTypes.family(SqlTypeFamily.ANY, SqlTypeFamily.NUMERIC),
          OperandTypes.and(
              OperandTypes.family(SqlTypeFamily.ANY, SqlTypeFamily.NUMERIC,
                  SqlTypeFamily.ANY),
              // Arguments 1 and 3 must have same type
              new SameOperandTypeChecker(3) {
                @Override protected List<Integer>
                getOperandList(int operandCount) {
                  return ImmutableList.of(0, 2);
                }
              }));

  private static final SqlReturnTypeInference RETURN_TYPE =
      ReturnTypes.cascade(ReturnTypes.ARG0, (binding, type) -> {
        // Result is NOT NULL if NOT NULL default value is provided
        SqlTypeTransform transform;
        if (binding.getOperandCount() < 3) {
          transform = SqlTypeTransforms.FORCE_NULLABLE;
        } else {
          RelDataType defValueType = binding.getOperandType(2);
          transform = defValueType.isNullable()
              ? SqlTypeTransforms.FORCE_NULLABLE
              : SqlTypeTransforms.TO_NOT_NULLABLE;
        }
        return transform.transformType(binding, type);
      });

  public SqlLeadLagAggFunction(SqlKind kind) {
    super(kind.name(),
        null,
        kind,
        RETURN_TYPE,
        null,
        OPERAND_TYPES,
        SqlFunctionCategory.NUMERIC,
        false,
        true,
        Optionality.FORBIDDEN);
    Preconditions.checkArgument(kind == SqlKind.LEAD
        || kind == SqlKind.LAG);
  }
```



#### 函数类型 - udtf 示例
1. 和其他函数的区别
   1. 注册返回值，可以是多个字段，且不同类型
2. Java UDTF：https://help.aliyun.com/zh/maxcompute/user-guide/java-udtfs?spm=a2c4g.11186623.0.0.477d4e0bN1XLri#concept-2105833
3. Python 用户定义表函数 (UDTF)：https://learn.microsoft.com/zh-cn/azure/databricks/udf/python-udtf
4. UDTF需求分析文档：https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=165221503
5. calcite 支持udtf
   1. https://issues.apache.org/jira/browse/CALCITE-1309
   2. https://issues.apache.org/jira/browse/CALCITE-1838
   3. https://issues.apache.org/jira/browse/CALCITE-1581
   4. SqlUserDefinedTableFunction -> SqlUserDefinedFunction -> SqlFunction SqlFunctionCategory.USER_DEFINED_TABLE_FUNCTION
   5. 源码：core/src/test/java/org/apache/calcite/test/TableFunctionTest.java
   6. https://github.com/apache/calcite/pull/1138 closed
   7. https://github.com/apache/calcite/pull/2092 open 还没有合并，可能因为拖延症吧
6. calcite目前找不到很好示例，只能从flink应用calcite最广泛的项目中找
   1. calcite 需要集成tablefunction 返回 QueryableTable，为什么到了flink却不需要，如何做到的？？？
7. flink文档：https://github.com/apachecn/flink-doc-zh/blob/master/docs/1.7/71.md
8. flink自定义udtf：https://www.cnblogs.com/felixzh/p/16846624.html
   1. 源码：flink-table/flink-table-planner-blink/src/test/scala/org/apache/flink/table/planner/runtime/batch/sql/MiscITCase.scala
   2. flink-connectors/flink-connector-hive/src/main/java/org/apache/flink/table/functions/hive/HiveGenericUDTF.java
9.  UDTF要比其他函数更复杂，它需要自定义一个Function，不像标量函数，可以统一是SqlFunction即可，再更新输入输出参数就行
10. 常见引擎开发，都是定义一个class，再反解析 class 的输入输出类型，然后注册到函数表
11. flink工具 class -> function
   1. UserDefinedFunctionUtils
   2. FunctionDefinitionUtil
   3. UserDefinedFunctionHelper
   4. TemporalTableFunctionImpl

```
 
hive支持，calcite 不支持，有人实现过，但是没有合进master https://github.com/apache/calcite/pull/2092
select udtf(arg1, arg2) as (seg1, seg2, seg3) from table

flink SQL语法参考
select name,content_type,url
from kafka_table CROSS JOIN lateral TABLE (ParserJsonArrayTest(`data`)) AS t (content_type,url)
 

select name,content_type,url
from kafka_table, lateral TABLE (ParserJsonArrayTest(`data`)) AS t (content_type,url)
 

select name,content_type,url
from kafka_table left join lateral TABLE (ParserJsonArrayTest(`data`)) AS t (content_type,url) on true


calcite 的 udtf 实现，需要返回 QueryableTable
全局搜 public static QueryableTable generateStrings(final Integer count)

基于 QueryableTable 在实现 getElementType getRowType 方法，拿到输入输出
calcite udtf -> calcite TableFunctionImpl -> calcite TableFunction

flink udtf

@SerialVersionUID(1L)
class IntExplodeTableFunc extends TableFunction[Int] {
  def eval(arr: Array[Int]): Unit = {
    arr.foreach(collect)
  }

  def eval(map: util.Map[Int, Integer]): Unit = {
    CommonCollect.collect(map, collect)
  }
}

函数初始化
IntExplodeTableFunc -> flink TableFunction<T> ->  UserDefinedFunction -> FunctionDefinition

flink function -> calcite function 转化过程
IntExplodeTableFunc -> ExplodeFunctionUtil.explodeTableFuncFromType -> DeferredTypeFlinkTableFunction -> FlinkTableFunction -> org.apache.calcite.schema.TableFunction


codegen 生成的函数 -> calcite function
代码生成 TableFunctionCallGen -> TableSqlFunction(flink TableFunction<T>, FlinkTableFunctionImpl) -> org.apache.flink.table.plan.schema.FlinkTableFunctionImpl -> org.apache.calcite.schema.TableFunction


org.apache.flink.table.planner.plan.schema.FlinkTableFunction -> FlinkTableFunction

解析 result
getExternalResultType


需要实现函数
getElementType
getRowType


flink 中的 explode

          val explodeSqlFunc = UserDefinedFunctionUtils.createTableSqlFunction(
            FunctionIdentifier.of("explode"),
            "explode",
            explodeTableFunc,
            fromLogicalTypeToDataType(toLogicalType(componentType)),
            cluster.getTypeFactory.asInstanceOf[FlinkTypeFactory])

val explodeFunction = ExplodeFunctionUtil.explodeTableFuncFromType(mapTypeInfo)
              (componentType, explodeFunction)


函数定义
@SerialVersionUID(1L)
class IntExplodeTableFunc extends TableFunction[Int] {
  def eval(arr: Array[Int]): Unit = {
    arr.foreach(collect)
  }

  def eval(map: util.Map[Int, Integer]): Unit = {
    CommonCollect.collect(map, collect)
  }
}


calcite 

```

#### UDTF总结
1. calcite TableFunction
   1. calcite TableFunctionImpl calicte内置的，对接起来困难
   2. flink DeferredTypeFlinkTableFunction -> FlinkTableFunction 实现一个方法，flink会通过反射解析数据类型，注册到calcite
      1. 业务自定义就会继承这个类，比较方便
   3. flink FlinkTableFunctionImpl flink一般用这个类做codegen


#### hive udtf示例
1. flink-connectors/flink-connector-hive/src/test/java/org/apache/flink/table/functions/hive/HiveGenericUDTFTest.java
```
	/**
	 * Test split udtf.
	 */
	public static class TestSplitUDTF extends GenericUDTF {

		@Override
		public StructObjectInspector initialize(ObjectInspector[] argOIs) throws UDFArgumentException {
			return ObjectInspectorFactory.getStandardStructObjectInspector(
				Collections.singletonList("col1"),
				Collections.singletonList(PrimitiveObjectInspectorFactory.javaStringObjectInspector));
		}

		@Override
		public void process(Object[] args) throws HiveException {
			String str = (String) args[0];
			for (String s : str.split(",")) {
				forward(s);
			}
		}

		@Override
		public void close() {
		}
	}

```





#### 反射机制实现加载函数
1. ReflectiveFunctionBase
2. ReflectiveSchema

#### 注册不同数据源函数表
```
1. core/src/test/java/org/apache/calcite/sql/test/SqlOperatorBaseTest.java


  protected SqlTester oracleTester() {
    return tester.withOperatorTable(
        ChainedSqlOperatorTable.of(OracleSqlOperatorTable.instance(),
            SqlStdOperatorTable.instance()))
        .withConnectionFactory(
            CalciteAssert.EMPTY_CONNECTION_FACTORY
                .with(new CalciteAssert
                    .AddSchemaSpecPostProcessor(CalciteAssert.SchemaSpec.HR))
                .with(CalciteConnectionProperty.FUN, "oracle"));
  }

```

#### 注册count函数
```
比如注册 MyCountAggFunction
初始化函数表
final SqlStdOperatorTable stdOpTab = SqlStdOperatorTable.instance();
    SqlOperatorTable opTab =
        ChainedSqlOperatorTable.of(stdOpTab,
            new ListSqlOperatorTable(
                ImmutableList.of(new MyCountAggFunction())));


第二种注册
  /**
   * String concatenation operator, '<code>||</code>'.
   */
  public static final SqlBinaryOperator CONCAT =
      new SqlBinaryOperator(
          "||",
          SqlKind.OTHER,
          60,
          true,
          ReturnTypes.DYADIC_STRING_SUM_PRECISION_NULLABLE,
          null,
          OperandTypes.STRING_SAME_SAME);


public class SqlSumEmptyIsZeroAggFunction extends SqlAggFunction {
  //~ Constructors -----------------------------------------------------------

  public SqlSumEmptyIsZeroAggFunction() {
    super("$SUM0",
        null,
        SqlKind.SUM0,
        ReturnTypes.AGG_SUM_EMPTY_IS_ZERO,
        null,
        OperandTypes.NUMERIC,
        SqlFunctionCategory.NUMERIC,
        false,
        false,
        Optionality.FORBIDDEN);
  }



自定义
  /** User-defined aggregate function. */
  public static class MyCountAggFunction extends SqlAggFunction {
    public MyCountAggFunction() {
      super("MY_COUNT", null, SqlKind.OTHER_FUNCTION, ReturnTypes.BIGINT, null,
          OperandTypes.ANY, SqlFunctionCategory.NUMERIC, false, false,
          Optionality.FORBIDDEN);
    }

    @SuppressWarnings("deprecation")
    public List<RelDataType> getParameterTypes(RelDataTypeFactory typeFactory) {
      return ImmutableList.of(typeFactory.createSqlType(SqlTypeName.ANY));
    }

    @SuppressWarnings("deprecation")
    public RelDataType getReturnType(RelDataTypeFactory typeFactory) {
      return typeFactory.createSqlType(SqlTypeName.BIGINT);
    }

    public RelDataType deriveType(SqlValidator validator,
        SqlValidatorScope scope, SqlCall call) {
      // Check for COUNT(*) function.  If it is we don't
      // want to try and derive the "*"
      if (call.isCountStar()) {
        return validator.getTypeFactory().createSqlType(SqlTypeName.BIGINT);
      }
      return super.deriveType(validator, scope, call);
    }
  }


函数表注册到Config中
return Frameworks.newConfigBuilder()
                .defaultSchema(rootSchema.plus())
                .parserConfig(sqlParserConfig)
//                .costFactory(new FlinkCostFactory())
                .typeSystem(typeSystem)
                .sqlToRelConverterConfig(getSqlToRelConverterConfig())
                .operatorTable(getSqlOperatorTable())
                // set the executor to evaluate constant expressions
//                .executor(new ExpressionReducer(tableConfig, false))
//                .context(context)
                .traitDefs(traitDefs)
                .build();
```

 
#### 动态注册函数
1. ListSqlOperatorTable 可以支持add function
2. 业务自己初始化好funciont即可
```

  /** Creates an operator table that contains functions in the given class.
   *
   * @see ModelHandler#addFunctions */
  public static SqlOperatorTable operatorTable(String className) {
    // Dummy schema to collect the functions
    final CalciteSchema schema =
        CalciteSchema.createRootSchema(false, false);
    ModelHandler.addFunctions(schema.plus(), null, ImmutableList.of(),
        className, "*", true);

    // The following is technical debt; see [CALCITE-2082] Remove
    // RelDataTypeFactory argument from SqlUserDefinedAggFunction constructor
    final SqlTypeFactoryImpl typeFactory =
        new SqlTypeFactoryImpl(RelDataTypeSystem.DEFAULT);

    final ListSqlOperatorTable table = new ListSqlOperatorTable();
    for (String name : schema.getFunctionNames()) {
      for (Function function : schema.getFunctions(name, true)) {
        final SqlIdentifier id = new SqlIdentifier(name, SqlParserPos.ZERO);
        table.add(
            toOp(typeFactory, id, function));
      }
    }
    return table;
  }



```


### 内置函数和自定义函数的区别
1. USER_DEFINED_FUNCTION 需要实现 sqlIdentifier
   1. 自定义函数需要实现 operandTypeChecker
2. SqlFunctionCategory.SYSTEM 则不需要
```
    public static final SqlFunction GET_COLUMNS =
            new SqlFunction(
                    "GET_COLUMNS",
                    SqlKind.OTHER_FUNCTION,
                    ReturnTypes.DOUBLE_NULLABLE,
                    null,
                    OperandTypes.ONE_OR_MORE,
                    SqlFunctionCategory.USER_DEFINED_FUNCTION
            );

    public static final SqlFunction STANDARD_FEATURES_GENERATION =
            new SqlFunction(
//                    "STANDARD_FEATURES_GENERATION",
                    "standard_features_generation",
                    SqlKind.OTHER_FUNCTION,
                    ReturnTypes.DOUBLE_NULLABLE,
                    null,
                    OperandTypes.ANY,
                    SqlFunctionCategory.SYSTEM
            );


  

```



### 新增RelTraitDef
1. 参考flink源码：flink-table/flink-table-planner-blink/src/test/java/org/apache/flink/table/planner/expressions/converter/ExpressionConverterTest.java

```
Arrays.asList(
					ConventionTraitDef.INSTANCE,
					FlinkRelDistributionTraitDef.INSTANCE(),
					RelCollationTraitDef.INSTANCE
			)


FlinkRelDistributionTraitDef 并没有过多扩展这方面能力
```

### 新增元数据connnect 和 adapt
1. csv：https://github.com/zzzzming95/calcite-demo/tree/master/src/main/java/pers/shezm/calcite/csv
2. schema 以及 schemaFactory
3. table 以及 tableFactory
   1. 多个table类型，用于scan filter或者更负责的操作
4. metaFile：元数据文件，可以是json格式，用于初始化Connection，相当于注册了元数据


### 业务数据类型 和 Calcite数据类型
1. 业务自定义类型都需要映射成 SqlType
2. 参考源码
   1. JavaTypeFactoryImpl.toSql


### SqlNameMatcher 表名匹配器



。

### flink如何元数据注册
1. FlinkCalciteCatalogReaderTest 初始化元数据
   1. 初始化 CalciteConnectionConfigImpl
   2. 初始化 FlinkTypeFactory
   3. 初始化 SchemaPlus
2. planner模块
   1. class CatalogReader extends CalciteCatalogReader 
3. blink模块
   1. class FlinkCalciteCatalogReader extends CalciteCatalogReader
```
public void init() {
		rootSchemaPlus = CalciteSchema.createRootSchema(true, false).plus();
		Properties prop = new Properties();
		prop.setProperty(CalciteConnectionProperty.CASE_SENSITIVE.camelName(), "false");
		CalciteConnectionConfigImpl calciteConnConfig = new CalciteConnectionConfigImpl(prop);
		catalogReader = new FlinkCalciteCatalogReader(
			CalciteSchema.from(rootSchemaPlus),
			Collections.emptyList(),
			typeFactory,
			calciteConnConfig);
	}

```


### flink 函数注册
1. 入口
   1. FunctionCatalogOperatorTable
   2. FlinkSqlOperatorTable：继承calcite，并注册业务自己function
   3. CalciteSqlFunction
2. 官方文档：https://nightlies.apache.org/flink/flink-docs-master/zh/docs/dev/table/functions/udfs/#%E8%A1%A8%E5%80%BC%E5%87%BD%E6%95%B0
3. Flink SQL UDF 调用：https://tech.qimao.com/flink-gui-ze-yin-qing-ji-zhu-fang-an-she-ji/

#### 初始化函数表
```

	/**
	 * Returns the operator table for this environment including a custom Calcite configuration.
	 */
	private SqlOperatorTable getSqlOperatorTable(CalciteConfig calciteConfig) {
		return JavaScalaConversionUtil.toJava(calciteConfig.getSqlOperatorTable()).map(operatorTable -> {
					if (calciteConfig.replacesSqlOperatorTable()) {
						return operatorTable;
					} else {
						return ChainedSqlOperatorTable.of(getBuiltinSqlOperatorTable(), operatorTable);
					}
				}
		).orElseGet(this::getBuiltinSqlOperatorTable);
	}

	/**
	 * Returns builtin the operator table and external the operator for this environment.
	 */
	private SqlOperatorTable getBuiltinSqlOperatorTable() {
		return ChainedSqlOperatorTable.of(
				new FunctionCatalogOperatorTable(
						context.getFunctionCatalog(),
						typeFactory),
				FlinkSqlOperatorTable.instance());
	}

```


#### CREATE FUNCTION 实现


#### 接口注册函数 实现
1. 函数catalog
   1. FunctionCatalog registerTempSystemScalarFunction
   2. FunctionCatalogOperatorTable convertToSqlFunction
      1. FunctionDefinition -> SqlFunction
      2. convertTableFunction 
      3. convertScalarFunction
      4. convertAggregateFunction 
   3. UserDefinedFunctionUtils 创建各种SqlFunction
      1. createScalarSqlFunction
      2. createTableSqlFunction
      3. createAggregateSqlFunction
   4. return type解析
      1. val (fieldNames, fieldIndexes, _) = UserDefinedFunctionUtils.getFieldInfo(resultType)
      2. flink typeInfo -> RelDataType
      3. hiveUdtf LogicalType -> typeInfo -> RelDataType
      4. RelDataType 可以嵌套多个类型
      5. createEvalOperandTypeInference
      6. createEvalOperandTypeChecker
   5. input type 解析
      1. FieldInfoUtils
2. 函数定义
   1. 表函数
      1. TableFunction
      2. TableFunctionDefinition
      3. TemporalTableFunctionImpl
   2. 内置函数
      1. BuiltInFunctionDefinitions
   3. calcite 中的父类函数
      1. SqlUserDefinedAggFunction
      2. SqlFunction
      3. SqlUserDefinedTableFunction
3. 函数定义工具
   1. UserDefinedFunctionHelper
   2. FunctionDefinitionUtil
4. 函数类型转换
   1. TypeInfoLogicalTypeConverter.fromLogicalTypeToTypeInfo
   2. UserDefinedFunctionUtils.fromLogicalTypeToDataType
   3. LogicalTypeDataTypeConverter.fromDataTypeToLogicalType
5. 代码生成
   1. FunctionCodeGenerator
6. 函数注册后如何运用到校验逻辑
   1. SqlValidatorImpl implements SqlValidatorWithHints
7. 源码
   1. flink-table/flink-table-planner-blink/src/test/scala/org/apache/flink/table/planner/expressions/UserDefinedScalarFunctionTest.scala
   2. 
```
// 注册函数
StreamTableEnvironment tEnv = ...
tEnv.registerFunction("top2", new Top2());

Correlate 示例
 private[flink] def generateFunction[T <: Function](
    config: TableConfig,
    inputSchema: RowSchema,
    udtfTypeInfo: TypeInformation[Any],
    returnSchema: RowSchema,
    joinType: JoinRelType,
    rexCall: RexCall,
    pojoFieldMapping: Option[Array[Int]],
    ruleDescription: String,
    functionClass: Class[T]):
  GeneratedFunction[T, Row] = {

generateFunction -> FunctionCodeGenerator



```

#### 注册没有返回值的函数



#### 注册动态数量形参的函数
1. https://issues.apache.org/jira/browse/CALCITE-3485

#### 注册Row方法
1. BuiltInMethods
2. FunctionGenerator
```

val ASIN = Types.lookupMethod(classOf[Math], "asin", classOf[Double])


addSqlFunctionMethod(
    ABS,
    Seq(DOUBLE),
    BuiltInMethods.ABS)

```

### flink 动态加载UDF
1. registerTableFunctionInternal


#### createTemporarySystemFunction
```

    /** Merges two rows as efficient as possible using internal data structures. */
    private static void executeInternalRowMergerFunction(TableEnvironment env) {
        // create a table with example data
        final Table customers =
                env.fromValues(
                        DataTypes.of(
                                "ROW<name STRING, data1 ROW<birth_date DATE>, data2 ROW<city STRING, phone STRING>>"),
                        Row.of(
                                "Guillermo Smith",
                                Row.of(LocalDate.parse("1992-12-12")),
                                Row.of("New Jersey", "816-443-8010")),
                        Row.of(
                                "Valeria Mendoza",
                                Row.of(LocalDate.parse("1970-03-28")),
                                Row.of("Los Angeles", "928-264-9662")),
                        Row.of(
                                "Leann Holloway",
                                Row.of(LocalDate.parse("1989-05-21")),
                                Row.of("Eugene", "614-889-6038")));
        env.createTemporaryView("customers", customers);

        // register and execute the function
        env.createTemporarySystemFunction(
                "InternalRowMergerFunction", InternalRowMergerFunction.class);
        env.executeSql("SELECT name, InternalRowMergerFunction(data1, data2) FROM customers")
                .print();

        // clean up
        env.dropTemporaryView("customers");
    }
```


### flink如何复用validator能力
1. FlinkCalciteSqlValidator




### flink如何处理复杂类型，如array<int>
1. 参考源码
   1. flink-table/flink-sql-parser/src/test/java/org/apache/flink/sql/parser/FlinkSqlParserImplTest.java#testCreateTableWithNestedComplexType
   2. FlinkDDLDataTypeTest
2. FlinkTypeFactory：flink数据类型工程
3. RelDataTypeSystem：calcite relnode数据类型系统




## 横向拆解 - plan optimize
1. 必看
   1. 优化器概念介绍：https://guimy.tech/calcite/2021/01/02/introduction-to-apache-calcite.html
2. rbo介绍：https://strongduanmu.com/blog/deep-understand-of-apache-calcite-hep-planner.html
3. 优化器详解：https://matt33.com/2019/03/17/apache-calcite-planner/
4. Rel概念介绍：https://www.cnblogs.com/wcgstudy/p/11795886.html
5. 启发式planner：https://zhuanlan.zhihu.com/p/61661909
6. HepRelVertex 启发式图顶点：https://liebing.org.cn/apache-calcite-hepplanner.html
7. 基础概念
   1. SqlToRelConverter：将SqlNode转换为RelNode
   2. RelOptCluster：优化器上下文
   3. ConventionTraitDef：表示由何种数据处理引擎处理，对应的 RelTrait 类型为 Convention
   4. RelCollationTraitDef：表示排序规则的定义，对应的 RelTrait 为 RelCollation。比如对于排序表达式（也称算子） org.apache.calcite.rel.core.Sort，就存在一个 RelCollation 类型的属性 collation。
   5. RelDistributionTraitDef，表示数据在物理存储上的分布方式，对应的 RelTrait 为 RelDistribution。
   6. Programs：
   7. Planner：
   8. RelRoot：RelNode根节点
   9. RelNode：代表了对数据的一个处理操作，常见的操作有 Sort、Join、Project、Filter、Scan 等。它蕴含的是对整个 Relation 的操作，而不是对具体数据的处理逻辑。
   10. RelTrait：用来定义逻辑表的物理相关属性（physical property），三种主要的 trait 类型是：Convention、RelCollation、RelDistribution；
   11. Convention：继承自 RelTrait，类型很少，代表一个单一的数据源，一个 relational expression 必须在同一个 convention 中；
   12. RelTraitSet：RelTrait集合
   13. RelOptRule：根据传递给它的 RelOptRuleOperand 来对目标 RelNode 树进行 规则匹配，匹配成功后，会再次调用 matches() 方法进行进一步检查。如果 mathes结果为真，则调用 onMatch() 进行转换。
8. 进阶概念
   1. VolcanoPlanner
   2. Dumpers
   3. Holder
   4. HepProgram
   5. RelFieldTrimmer
   6. RelHint
9. 规则集
   1. RuleSet：rbo优化规则集
   2. CoreRules：核心规则集
   3. EnumerableRules：插件式加入规则集
   4. Fixture：测试Rule框架，快速验证规则正确性和是否生效
   5. RelOptUtil：工具类，方便对rule操作和导出，静态方法
10. 源码必看
   1. core/src/test/java/org/apache/calcite/rel/rules/SortRemoveRuleTest.java


### rbo概念
```
BeginGroup, EndGroup: 开始和结束一组指令组
CommonRelSubExprRels: 寻找公共子关系表达式的指令
ConverterRules: 
MatchLimit: 修改当前 Program 匹配 limit 的指令
MatchOrder: 修改当前 Program 匹配次序的指令
Placeholder: 
RuleClass: 执行 rules 中符合指定规则类型 allRules 的规则的指令(对 allRules 的过滤)
RuleCollection: 执行多个 rules 的指令(不必在 allRules 中)
RuleInstance: 执行一个 rule 的指令(不必在 allRules 中)
RuleLookup: 
SubProgram: 用来执行子 HepProgram 的指令


```


###  SQL -> RelNode 代码示例
1. 核心
   1. Planner planner = Frameworks.getPlanner(config);
   2. 有了planner就能任意介入到oaser validate 和 optimize阶段了
```

    /**
     * The default schema that is used in these tests provides tables sorted on the primary key. Due
     * to this scan operators always come with a {@link org.apache.calcite.rel.RelCollation} trait.
     */
    RelNode plan() throws Exception {
      final SchemaPlus rootSchema = Frameworks.createRootSchema(true);
      final SchemaPlus defSchema = rootSchema.add("hr", new HrClusteredSchema());
      final FrameworkConfig config = Frameworks.newConfigBuilder()
          .parserConfig(SqlParser.Config.DEFAULT)
          .sqlToRelConverterConfig(
              sqlToRelConfigTransform.apply(SqlToRelConverter.config()))
          .defaultSchema(defSchema)
          .traitDefs(ConventionTraitDef.INSTANCE, RelCollationTraitDef.INSTANCE)
          .programs(
              Programs.of(prepareRules),
              Programs.ofRules(CoreRules.SORT_REMOVE))
          .build();
      Planner planner = Frameworks.getPlanner(config);
      SqlNode parse = planner.parse(sql);
      SqlNode validate = planner.validate(parse);
      RelRoot planRoot = planner.rel(validate);
      RelNode planBefore = planRoot.rel;
      RelTraitSet desiredTraits = planBefore.getTraitSet()
          .replace(EnumerableConvention.INSTANCE);
      RelNode planAfter = planner.transform(0, desiredTraits, planBefore);
      return planner.transform(1, desiredTraits, planAfter);
    }

```

### 新增Rule流程


### RexNode 语法测试
1. core/src/test/java/org/apache/calcite/rel/rules/DateRangeRulesTest.java
```
  
  @Test void testExtractYearFromDateColumn() {
    final Fixture2 f = new Fixture2();

    final RexNode e = f.eq(f.literal(2014), f.exYearD);
    assertThat(DateRangeRules.extractTimeUnits(e),
        is(set(TimeUnitRange.YEAR)));
    assertThat(DateRangeRules.extractTimeUnits(f.dec), is(set()));
    assertThat(DateRangeRules.extractTimeUnits(f.literal(1)), is(set()));

    // extract YEAR from a DATE column
    checkDateRange(f, e, is("AND(>=($8, 2014-01-01), <($8, 2015-01-01))"));
    checkDateRange(f, f.eq(f.exYearD, f.literal(2014)),
        is("AND(>=($8, 2014-01-01), <($8, 2015-01-01))"));
    checkDateRange(f, f.ge(f.exYearD, f.literal(2014)),
        is(">=($8, 2014-01-01)"));
    checkDateRange(f, f.gt(f.exYearD, f.literal(2014)),
        is(">=($8, 2015-01-01)"));
    checkDateRange(f, f.lt(f.exYearD, f.literal(2014)),
        is("<($8, 2014-01-01)"));
    checkDateRange(f, f.le(f.exYearD, f.literal(2014)),
        is("<($8, 2015-01-01)"));
    checkDateRange(f, f.ne(f.exYearD, f.literal(2014)),
        is("<>(EXTRACT(FLAG(YEAR), $8), 2014)"));
  }


```


### 计划图变化
```

Root: rel#118:RelSubset#6.ENUMERABLE.[1]
Original rel:
LogicalSort(subset=[rel#118:RelSubset#6.ENUMERABLE.[1]], sort0=[$1], dir0=[ASC]): rowcount = 1.7999999999999998, cumulative cost = {1.7999999999999998 rows, 36.0 cpu, 0.0 io}, id = 116
  LogicalProject(subset=[rel#115:RelSubset#5.NONE.[]], deptno=[$1], empid=[$0]): rowcount = 1.7999999999999998, cumulative cost = {1.7999999999999998 rows, 3.5999999999999996 cpu, 0.0 io}, id = 114
    LogicalJoin(subset=[rel#113:RelSubset#4.NONE.[]], condition=[=($1, $5)], joinType=[inner]): rowcount = 1.7999999999999998, cumulative cost = {1.7999999999999998 rows, 0.0 cpu, 0.0 io}, id = 112
      LogicalTableScan(subset=[rel#106:RelSubset#0.NONE.[0]], table=[[hr, emps]]): rowcount = 4.0, cumulative cost = {4.0 rows, 5.0 cpu, 0.0 io}, id = 99
      LogicalAggregate(subset=[rel#111:RelSubset#3.NONE.[]], group=[{0}]): rowcount = 3.0, cumulative cost = {3.0 rows, 0.0 cpu, 0.0 io}, id = 110
        LogicalProject(subset=[rel#109:RelSubset#2.NONE.[0]], deptno=[$0]): rowcount = 3.0, cumulative cost = {3.0 rows, 3.0 cpu, 0.0 io}, id = 108
          LogicalTableScan(subset=[rel#107:RelSubset#1.NONE.[0]], table=[[hr, depts]]): rowcount = 3.0, cumulative cost = {3.0 rows, 4.0 cpu, 0.0 io}, id = 100

```

### calcite 规则集
1. RelOptRulesTest
2. CoreRules

### calcite 可视化
1. 静态方法：core/src/main/java/org/apache/calcite/plan/volcano/Dumpers.java#dumpGraphviz
2. Graphvia 语法：https://leojhonsong.github.io/zh-CN/2020/03/12/Graphviz%E7%AE%80%E8%A6%81%E8%AF%AD%E6%B3%95/
3. 手绘风格：https://sketchviz.com/new
4. 可视化工具集合：https://graphviz.org/Gallery/directed/Genetic_Programming.html
5. gvmap工具：https://graphviz.org/Gallery/undirected/gd_1994_2007.html
6. 神经网络工具：https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network
7. Graphviz 格式如下
```
示例链接

https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%20%20%20%20%09root%20%5Bstyle%3Dfilled%2Clabel%3D%22Root%22%5D%3B%0A%20%20%20%20%09subgraph%20cluster0%7B%0A%20%20%20%20%09%09label%3D%22Set%200%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission)%22%3B%0A%20%20%20%20%09%09rel99%20%5Blabel%3D%22rel%2399%3ALogicalTableScan%5Cntable%3D%5Bhr%2C%20emps%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel120%20%5Blabel%3D%22rel%23120%3AEnumerableTableScan%5Cntable%3D%5Bhr%2C%20emps%5D%5Cnrows%3D4.0%2C%20cost%3D%7B4.0%20rows%2C%205.0%20cpu%2C%200.0%20io%7D%22%2Ccolor%3Dblue%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset106%20%5Blabel%3D%22rel%23106%3ARelSubset%230.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset121%20%5Blabel%3D%22rel%23121%3ARelSubset%230.ENUMERABLE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster1%7B%0A%20%20%20%20%09%09label%3D%22Set%201%20RecordType(JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name)%22%3B%0A%20%20%20%20%09%09rel100%20%5Blabel%3D%22rel%23100%3ALogicalTableScan%5Cntable%3D%5Bhr%2C%20depts%5D%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel122%20%5Blabel%3D%22rel%23122%3AEnumerableTableScan%5Cntable%3D%5Bhr%2C%20depts%5D%5Cnrows%3D3.0%2C%20cost%3D%7B3.0%20rows%2C%204.0%20cpu%2C%200.0%20io%7D%22%2Ccolor%3Dblue%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset107%20%5Blabel%3D%22rel%23107%3ARelSubset%231.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset123%20%5Blabel%3D%22rel%23123%3ARelSubset%231.ENUMERABLE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster2%7B%0A%20%20%20%20%09%09label%3D%22Set%202%20RecordType(JavaType(int)%20deptno)%22%3B%0A%20%20%20%20%09%09rel108%20%5Blabel%3D%22rel%23108%3ALogicalProject%5Cninput%3DRelSubset%23107%2Cinputs%3D0%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset109%20%5Blabel%3D%22rel%23109%3ARelSubset%232.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster3%7B%0A%20%20%20%20%09%09label%3D%22Set%203%20RecordType(JavaType(int)%20deptno)%22%3B%0A%20%20%20%20%09%09rel110%20%5Blabel%3D%22rel%23110%3ALogicalAggregate%5Cninput%3DRelSubset%23109%2Cgroup%3D%7B0%7D%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset111%20%5Blabel%3D%22rel%23111%3ARelSubset%233.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster4%7B%0A%20%20%20%20%09%09label%3D%22Set%204%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission%2C%20JavaType(int)%20deptno0)%22%3B%0A%20%20%20%20%09%09rel112%20%5Blabel%3D%22rel%23112%3ALogicalJoin%5Cnleft%3DRelSubset%23106%2Cright%3DRelSubset%23111%2Ccondition%3D%3D(%241%2C%20%245)%2CjoinType%3Dinner%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel129%20%5Blabel%3D%22rel%23129%3ALogicalSort%5Cninput%3DRelSubset%23113%2Csort0%3D%240%2Cdir0%3DASC%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset113%20%5Blabel%3D%22rel%23113%3ARelSubset%234.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%09subset131%20%5Blabel%3D%22rel%23131%3ARelSubset%234.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset113%20-%3E%20subset131%3B%09%7D%0A%20%20%20%20%09subgraph%20cluster5%7B%0A%20%20%20%20%09%09label%3D%22Set%205%20RecordType(JavaType(int)%20deptno%2C%20JavaType(int)%20empid)%22%3B%0A%20%20%20%20%09%09rel114%20%5Blabel%3D%22rel%23114%3ALogicalProject%5Cninput%3DRelSubset%23113%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel128%20%5Blabel%3D%22rel%23128%3ALogicalProject%5Cninput%3DRelSubset%23127%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset115%20%5Blabel%3D%22rel%23115%3ARelSubset%235.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster6%7B%0A%20%20%20%20%09%09label%3D%22Set%206%20RecordType(JavaType(int)%20deptno%2C%20JavaType(int)%20empid)%22%3B%0A%20%20%20%20%09%09rel116%20%5Blabel%3D%22rel%23116%3ALogicalSort%5Cninput%3DRelSubset%23115%2Csort0%3D%241%2Cdir0%3DASC%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel119%20%5Blabel%3D%22rel%23119%3AAbstractConverter%5Cninput%3DRelSubset%23117%2Cconvention%3DENUMERABLE%2Csort%3D%5B1%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel132%20%5Blabel%3D%22rel%23132%3ALogicalProject%5Cninput%3DRelSubset%23131%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel136%20%5Blabel%3D%22rel%23136%3ALogicalProject%5Cninput%3DRelSubset%23135%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset117%20%5Blabel%3D%22rel%23117%3ARelSubset%236.NONE.%5B1%5D%22%5D%0A%20%20%20%20%09%09subset118%20%5Blabel%3D%22rel%23118%3ARelSubset%236.ENUMERABLE.%5B1%5D%22%2Ccolor%3Dred%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster7%7B%0A%20%20%20%20%09%09label%3D%22Set%207%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission)%22%3B%0A%20%20%20%20%09%09rel126%20%5Blabel%3D%22rel%23126%3ALogicalJoin%5Cnleft%3DRelSubset%23106%2Cright%3DRelSubset%23109%2Ccondition%3D%3D(%241%2C%20%245)%2CjoinType%3Dsemi%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel133%20%5Blabel%3D%22rel%23133%3ALogicalSort%5Cninput%3DRelSubset%23127%2Csort0%3D%240%2Cdir0%3DASC%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset127%20%5Blabel%3D%22rel%23127%3ARelSubset%237.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%09subset135%20%5Blabel%3D%22rel%23135%3ARelSubset%237.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset127%20-%3E%20subset135%3B%09%7D%0A%20%20%20%20%09root%20-%3E%20subset118%3B%0A%20%20%20%20%09subset106%20-%3E%20rel99%3B%0A%20%20%20%20%09subset121%20-%3E%20rel120%5Bcolor%3Dblue%5D%3B%0A%20%20%20%20%09subset107%20-%3E%20rel100%3B%0A%20%20%20%20%09subset123%20-%3E%20rel122%5Bcolor%3Dblue%5D%3B%0A%20%20%20%20%09subset109%20-%3E%20rel108%3B%20rel108%20-%3E%20subset107%3B%0A%20%20%20%20%09subset111%20-%3E%20rel110%3B%20rel110%20-%3E%20subset109%3B%0A%20%20%20%20%09subset113%20-%3E%20rel112%3B%20rel112%20-%3E%20subset106%5Blabel%3D%220%22%5D%3B%20rel112%20-%3E%20subset111%5Blabel%3D%221%22%5D%3B%0A%20%20%20%20%09subset131%20-%3E%20rel129%3B%20rel129%20-%3E%20subset113%3B%0A%20%20%20%20%09subset115%20-%3E%20rel114%3B%20rel114%20-%3E%20subset113%3B%0A%20%20%20%20%09subset115%20-%3E%20rel128%3B%20rel128%20-%3E%20subset127%3B%0A%20%20%20%20%09subset117%20-%3E%20rel116%3B%20rel116%20-%3E%20subset115%3B%0A%20%20%20%20%09subset118%20-%3E%20rel119%3B%20rel119%20-%3E%20subset117%3B%0A%20%20%20%20%09subset117%20-%3E%20rel132%3B%20rel132%20-%3E%20subset131%3B%0A%20%20%20%20%09subset117%20-%3E%20rel136%3B%20rel136%20-%3E%20subset135%3B%0A%20%20%20%20%09subset127%20-%3E%20rel126%3B%20rel126%20-%3E%20subset106%5Blabel%3D%220%22%5D%3B%20rel126%20-%3E%20subset109%5Blabel%3D%221%22%5D%3B%0A%20%20%20%20%09subset135%20-%3E%20rel133%3B%20rel133%20-%3E%20subset127%3B%0A%20%20%20%20%7D




```

### flink 动态加载rule
1. 广播流支持加rule：https://stackoverflow.com/questions/63152612/how-can-i-create-dynamic-rule-in-apache-flink

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
2. SqlNode方言转换：https://cloud.tencent.com/developer/article/2007781
3. 方言互转图：https://blog.csdn.net/it_dx/article/details/115904782
4. 核心思路
   1. rel2sql
   2. rel -> sqlnode -> dialect sqlnode -> sql unparse 
   3. 每一个sqlnode只需要实现一个unparse即可
   4. dialect 调用unparseCall 这里需要对特殊的sqlnode进行翻译和转换
  
### presto的unparseCall 对特殊语法的处理
```
  @Override public void unparseCall(SqlWriter writer, SqlCall call,
      int leftPrec, int rightPrec) {
    if (call.getOperator() == SqlStdOperatorTable.SUBSTRING) {
      RelToSqlConverterUtil.specialOperatorByName("SUBSTR")
          .unparse(writer, call, 0, 0);
    } else if (call.getOperator() == SqlStdOperatorTable.APPROX_COUNT_DISTINCT) {
      RelToSqlConverterUtil.specialOperatorByName("APPROX_DISTINCT")
          .unparse(writer, call, 0, 0);
    } else {
      switch (call.getKind()) {
      case MAP_VALUE_CONSTRUCTOR:
        unparseMapValue(writer, call, leftPrec, rightPrec);
        break;
      default:
        // Current impl is same with Postgresql.
        PostgresqlSqlDialect.DEFAULT.unparseCall(writer, call, leftPrec, rightPrec);
      }
    }
  }

```


### starrocks的unparseCall 对特殊语法的处理
```
@Override public void unparseCall(SqlWriter writer, SqlCall call, int leftPrec, int rightPrec) {
    switch (call.getKind()) {
    case ARRAY_VALUE_CONSTRUCTOR:
      final SqlWriter.Frame arrayFrame = writer.startList("[", "]");
      for (SqlNode operand : call.getOperandList()) {
        writer.sep(",");
        operand.unparse(writer, leftPrec, rightPrec);
      }
      writer.endList(arrayFrame);
      break;
    case MAP_VALUE_CONSTRUCTOR:
      writer.keyword(call.getOperator().getName());
      final SqlWriter.Frame mapFrame = writer.startList("{", "}");
      for (int i = 0; i < call.operandCount(); i++) {
        String sep = i % 2 == 0 ? "," : ":";
        writer.sep(sep);
        call.operand(i).unparse(writer, leftPrec, rightPrec);
      }
      writer.endList(mapFrame);
      break;
    case TRIM:
      unparseHiveTrim(writer, call, leftPrec, rightPrec);
      break;
    case FLOOR:
      if (call.operandCount() != 2) {
        super.unparseCall(writer, call, leftPrec, rightPrec);
        return;
      }
      final SqlLiteral timeUnitNode = call.operand(1);
      final TimeUnitRange timeUnit = timeUnitNode.getValueAs(TimeUnitRange.class);
      SqlCall newCall =
          SqlFloorFunction.replaceTimeUnitOperand(call, timeUnit.name(),
              timeUnitNode.getParserPosition());
      SqlFloorFunction.unparseDatetimeFunction(writer, newCall, "DATE_TRUNC", false);
      break;
    default:
      super.unparseCall(writer, call, leftPrec, rightPrec);
      break;
    }
  }


```



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
1. 必看
   1. 如何使用calcite rule做SQL重写（上）：http://dafei1288.com/2023/08/10/1003-calcite-sql-rule/
   2. 如何使用calcite rule做SQL重写（下）：http://dafei1288.com/2023/08/18/1004-calcite-sql-custom-rule/
   3. RBO和CBO应用：https://www.cnblogs.com/listenfwind/p/13192259.html
2. 源码示例
   1. filter下推：https://github.com/zzzzming95/calcite-demo/blob/master/src/main/java/pers/shezm/calcite/test/Test5.java
   2. 自定义一个新的project并替换：
      1. 添加规则：https://github.com/zzzzming95/calcite-demo/blob/db9883fa37ae8ffe396f48980a4c21dcb9bc592a/src/main/java/pers/shezm/calcite/test/Test6.java#L79
      2. onmatch：https://github.com/zzzzming95/calcite-demo/blob/db9883fa37ae8ffe396f48980a4c21dcb9bc592a/src/main/java/pers/shezm/calcite/optimizer/converter/CSVNewProjectRule.java#L40


## 纵向拆解 - 关系代数
1. Calcite关系代数：https://liebing.org.cn/apache-calcite-relational-algebra.html
2. RelBuilder介绍：https://izualzhy.cn/calcite-example
### 概念
1. RelNode：Calcite中的IR
2. SingleRel：一元算子Project, Filter, Aggregate
3. SetOp：集合算子Union, Intersect, Minus.
4. EnumerableRel：物理算子
5. BindableRel：物理算子
6. 核心
   1. RelBuilder：是Calcite中的关系算子生成器，生成RelNode和RexNode
   2. 示例：https://github.com/apache/calcite/blob/main/core/src/test/java/org/apache/calcite/examples/RelBuilderExample.java
   3. https://github.com/LB-Yu/data-systems-learning/blob/master/sql/calcite-learning/calcite-parser/src/test/java/org/apache/calcite/example/rel/RelBuilderTest.java


### 构建计划图 示例
```

  /**
   * Sometimes the stack becomes so deeply nested it gets confusing. To keep
   * things straight, you can remove expressions from the stack. For example,
   * here we are building a bushy join:
   *
   * <blockquote><pre>
   *                join
   *              /      \
   *         join          join
   *       /      \      /      \
   *     EMP     DEPT  EMP    BONUS
   * </pre></blockquote>
   *
   * <p>We build it in three stages. Store the intermediate results in variables
   * `left` and `right`, and use `push()` to put them back on the stack when it
   * is time to create the final `Join`.
   */
  private RelBuilder example4(RelBuilder builder) {
    final RelNode left = builder
        .scan("EMP")
        .scan("DEPT")
        .join(JoinRelType.INNER, "DEPTNO")
        .build();

    final RelNode right = builder
        .scan("EMP")
        .scan("BONUS")
        .join(JoinRelType.INNER, "ENAME")
        .build();

    return builder
        .push(left)
        .push(right)
        .join(JoinRelType.INNER, "ENAME");
  }

```

### RelBuilder 新建scan算子
```java
  public RelBuilder scan(Iterable<String> tableNames) {
    final List<String> names = ImmutableList.copyOf(tableNames);
    requireNonNull(relOptSchema, "relOptSchema");
    final RelOptTable relOptTable = relOptSchema.getTableForMember(names);
    if (relOptTable == null) {
      throw RESOURCE.tableNotFound(String.join(".", names)).ex();
    }
    final RelNode scan =
        struct.scanFactory.createScan(
            ViewExpanders.toRelContext(viewExpander, cluster),
            relOptTable);
    push(scan);
    rename(relOptTable.getRowType().getFieldNames());

    // When the node is not a TableScan but from expansion,
    // we need to explicitly add the alias.
    if (!(scan instanceof TableScan)) {
      as(Util.last(ImmutableList.copyOf(tableNames)));
    }
    return this;
  }

```

### RelBuilder 新建join算子
```java
public RelBuilder join(JoinRelType joinType, RexNode condition,
      Set<CorrelationId> variablesSet) {
    Frame right = stack.pop();
    final Frame left = stack.pop();
    final RelNode join;
    final boolean correlate = checkIfCorrelated(variablesSet, joinType, left.rel, right.rel);
    RexNode postCondition = literal(true);
    if (config.simplify()) {
      // Normalize expanded versions IS NOT DISTINCT FROM so that simplifier does not
      // transform the expression to something unrecognizable
      if (condition instanceof RexCall) {
        condition =
            RelOptUtil.collapseExpandedIsNotDistinctFromExpr((RexCall) condition,
                getRexBuilder());
      }
      condition = simplifier.simplifyUnknownAsFalse(condition);
    }
    if (correlate) {
      final CorrelationId id = Iterables.getOnlyElement(variablesSet);
      // Correlate does not have an ON clause.
      switch (joinType) {
      case LEFT:
      case SEMI:
      case ANTI:
        // For a LEFT/SEMI/ANTI, predicate must be evaluated first.
        stack.push(right);
        filter(condition.accept(new Shifter(left.rel, id, right.rel)));
        right = stack.pop();
        break;
      case INNER:
        // For INNER, we can defer.
        postCondition = condition;
        break;
      default:
        throw new IllegalArgumentException("Correlated " + joinType + " join is not supported");
      }
      final ImmutableBitSet requiredColumns = RelOptUtil.correlationColumns(id, right.rel);
      join =
          struct.correlateFactory.createCorrelate(left.rel, right.rel, ImmutableList.of(), id,
              requiredColumns, joinType);
    } else {
      RelNode join0 =
          struct.joinFactory.createJoin(left.rel, right.rel,
              ImmutableList.of(), condition, variablesSet, joinType, false);

      if (join0 instanceof Join && config.pushJoinCondition()) {
        join = RelOptUtil.pushDownJoinConditions((Join) join0, this);
      } else {
        join = join0;
      }
    }
    final PairList<ImmutableSet<String>, RelDataTypeField> fields =
        PairList.of();
    fields.addAll(left.fields);
    fields.addAll(right.fields);
    stack.push(new Frame(join, fields));
    filter(postCondition);
    return this;
  }

```



### RelBuilder 模块初始化，测试和修改
1. core/src/test/java/org/apache/calcite/sql2rel/CorrelateProjectExtractorTest.java
```
@Test void testSingleCorrelationCallOverVariableInFilter() {
    final RelBuilder builder = RelBuilder.create(config().build());
    final Holder<@Nullable RexCorrelVariable> v = Holder.empty();
    RelNode before = builder.scan("EMP")
        .variable(v::set)
        .scan("DEPT")
        .filter(
            builder.equals(builder.field(0),
                builder.call(
                    SqlStdOperatorTable.PLUS,
                    builder.literal(10),
                    builder.field(v.get(), "DEPTNO"))))
        .correlate(JoinRelType.LEFT, v.get().id, builder.field(2, 0, "DEPTNO"))
        .build();

    final String planBefore = ""
        + "LogicalCorrelate(correlation=[$cor0], joinType=[left], requiredColumns=[{7}])\n"
        + "  LogicalTableScan(table=[[scott, EMP]])\n"
        + "  LogicalFilter(condition=[=($0, +(10, $cor0.DEPTNO))])\n"
        + "    LogicalTableScan(table=[[scott, DEPT]])\n";
    assertThat(before, hasTree(planBefore));

    RelNode after = before.accept(new CorrelateProjectExtractor(RelFactories.LOGICAL_BUILDER));
    final String planAfter = ""
        + "LogicalProject(EMPNO=[$0], ENAME=[$1], JOB=[$2], MGR=[$3], HIREDATE=[$4], SAL=[$5], COMM=[$6], DEPTNO=[$7], DEPTNO0=[$9], DNAME=[$10], LOC=[$11])\n"
        + "  LogicalCorrelate(correlation=[$cor0], joinType=[left], requiredColumns=[{8}])\n"
        + "    LogicalProject(EMPNO=[$0], ENAME=[$1], JOB=[$2], MGR=[$3], HIREDATE=[$4], SAL=[$5], COMM=[$6], DEPTNO=[$7], $f8=[+(10, $7)])\n"
        + "      LogicalTableScan(table=[[scott, EMP]])\n"
        + "    LogicalFilter(condition=[=($0, $cor0.$f8)])\n"
        + "      LogicalTableScan(table=[[scott, DEPT]])\n";
    assertThat(after, hasTree(planAfter));
  }

```

## 纵向拆解 - 物化视图


## 纵向拆解 - lattice


## 纵向拆解 - 血缘解析
1. 通过relNode解析血缘：https://github.com/HamaWhiteGG/flink-sql-lineage/blob/main/lineage-flink1.16.x/src/main/java/com/hw/lineage/flink/LineageServiceImpl.java#L163
2. 技术难点
   1. SqlNode是没有物理和逻辑属性，只有关键词和语法，所以区分数表名和列名是需要很多加工逻辑
   2. 但是calcite的校验器确能做到校验表和列能力，意味着有一段代码是可以解析出血缘的
3. registerQuery：Registers a query in a parent scope.
4. node.getKind()：用于SqlNode分类
```
能识别出表和列，找这个思路改即可


Caused by: org.apache.calcite.runtime.CalciteContextException: From line 2, column 6 to line 2, column 17: Object 'ad' not found
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	at org.apache.calcite.runtime.Resources$ExInstWithCause.ex(Resources.java:463)
	at org.apache.calcite.sql.SqlUtil.newContextException(SqlUtil.java:787)
	at org.apache.calcite.sql.SqlUtil.newContextException(SqlUtil.java:772)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.newValidationError(SqlValidatorImpl.java:4825)
	at org.apache.calcite.sql.validate.IdentifierNamespace.resolveImpl(IdentifierNamespace.java:172)
	at org.apache.calcite.sql.validate.IdentifierNamespace.validateImpl(IdentifierNamespace.java:177)
	at org.apache.calcite.sql.validate.AbstractNamespace.validate(AbstractNamespace.java:84)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateNamespace(SqlValidatorImpl.java:994)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateQuery(SqlValidatorImpl.java:954)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateFrom(SqlValidatorImpl.java:3087)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateFrom(SqlValidatorImpl.java:3069)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateSelect(SqlValidatorImpl.java:3339)
	at org.apache.calcite.sql.validate.SelectNamespace.validateImpl(SelectNamespace.java:60)
	at org.apache.calcite.sql.validate.AbstractNamespace.validate(AbstractNamespace.java:84)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateNamespace(SqlValidatorImpl.java:994)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateQuery(SqlValidatorImpl.java:954)
	at org.apache.calcite.sql.SqlSelect.validate(SqlSelect.java:242)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validateScopedExpression(SqlValidatorImpl.java:929)
	at org.apache.calcite.sql.validate.SqlValidatorImpl.validate(SqlValidatorImpl.java:633)
	at org.apache.calcite.prepare.PlannerImpl.validate(PlannerImpl.java:188)
	... 26 more

```
## 纵向拆解 - Type概念理解
1. OperandTypes
2. ReturnTypes
3. InferTypes
4. SqlTypeFamily


## 纵向拆解 - 灵活的数据类型系统
1. SqlTypeUtil：Contains utility methods used during SQL validation or type derivation.
2. 类型
   1. SqlTypeName：所有sql类型字面值
   2. RelDataType 
   3. JavaType
3. 类型工厂
   1. SqlTypeFactoryImpl：sql类型工厂，基础类型创建和复杂类型创建
   2. JavaTypeFactoryImpl：java类型工厂，基础类型创建和复杂类型创建，可以转SQL类型 
      1. 方法：getJavaClass 和 toSql
   3. RelDataTypeFactory
4. RelOptUtil：rel工具，判断类型是否匹配，类型转换
5. RelCollationImpl
   1. addCharsetAndCollation createTypeWithCharsetAndCollation 
6. RelDataType
   1. getCharset 默认字符集 DEFAULT_CHARSET
   2. getCollation 默认排序规则
7. RelDataTypeImpl
8. DynamicRecordType
9. DynamicRecordTypeImpl
10. DelegatingTypeSystem
11. SqlTypeUtil.canCastFrom 类型强转
12. 非标量类型：https://strongduanmu.com/wiki/calcite/reference.html#%E9%9D%9E%E6%A0%87%E9%87%8F%E7%B1%BB%E5%9E%8B
13. 参考源码
   1. core/src/test/java/org/apache/calcite/test/CollectionTypeTest.java#getRowType
### 创建复杂类型
```
初始化 类型工厂
final RelDataTypeFactory typeFactory =
        new SqlTypeFactoryImpl(org.apache.calcite.rel.type.RelDataTypeSystem.DEFAULT);



初始化 array<int>
RelDataType nullableIntegerType = typeFactory
          .createTypeWithNullability(typeFactory.createSqlType(SqlTypeName.INTEGER), true);
  typeFactory.createArrayType(nullableIntegerType, -1L)

初始化 array<string> 可null值
typeFactory.createTypeWithNullability(
                  typeFactory.createArrayType(nullableVarcharType, -1L), true)


初始化 map<string, int>
typeFactory.createMapType(nullableVarcharType, nullableIntegerType)





```


### 显示创建返回值
```
  /**
   * Creates an inference rule which returns a type with no precision or scale,
   * such as {@code DATE}.
   */
  public static ExplicitReturnTypeInference explicit(SqlTypeName typeName) {
    return explicit(RelDataTypeImpl.proto(typeName, false));
  }

```


## 纵向拆解 - RelNode

### RelFactories -> RelBuilder -> RelNode
1. 构建逻辑算子，业务可以继承这个类型，实现自己relnode工厂
2. Contains factory interface and default implementation for creating various rel nodes.
3. RelFactories
   1. ProjectFactoryImpl
   2. FilterFactoryImpl
   3. CorrelateFactoryImpl
4. 应用
   1. 参考 FlinkLogicalRelFactories & FlinkRelFactories，flink继承这个方法 relNode -> flinkLogicalNode
  
### Where流程 -> Filter -> logicalFilter -> Calc算子（condition）
1. Project & Filter Node 转成 FlinkLogicalCalc （input, expression, output and condition）
2. Calc算子本质就是 输入字段，输出字段，字段之间的表达式和过滤表达式的集合，所以这些算子可以融合在一起
2. Calc算子融合也就好理解了，就是为了做全局最优的表达式合并，减少中间结果集
3. calcite
   1. RelNode Filter
   2. LogicalFilter
   3. EnumerableFilterRule
   4. EnumerableFilter
   5. EnumerableFilterToCalcRule
   6. EnumerableCalc
   7. 
4. flink
   1. 
   2. FlinkLogicalRelFactories
   3. FlinkLogicalCalc
   4. StreamExecCalcRule
   5. StreamExecCalc
```
SqlToRelConverter


 /**
   * Converts a WHERE clause.
   *
   * @param bb    Blackboard
   * @param where WHERE clause, may be null
   */
  private void convertWhere(
      final Blackboard bb,
      final SqlNode where) {
    if (where == null) {
      return;
    }
    SqlNode newWhere = pushDownNotForIn(bb.scope, where);
    replaceSubQueries(bb, newWhere, RelOptUtil.Logic.UNKNOWN_AS_FALSE);
    final RexNode convertedWhere = bb.convertExpression(newWhere);
    final RexNode convertedWhere2 =
        RexUtil.removeNullabilityCast(typeFactory, convertedWhere);

    // only allocate filter if the condition is not TRUE
    if (convertedWhere2.isAlwaysTrue()) {
      return;
    }

    final RelFactories.FilterFactory filterFactory =
        RelFactories.DEFAULT_FILTER_FACTORY;
    final RelNode filter = filterFactory.createFilter(bb.root, convertedWhere2);
    final RelNode r;
    final CorrelationUse p = getCorrelationUse(bb, filter);
    if (p != null) {
      assert p.r instanceof Filter;
      Filter f = (Filter) p.r;
      r = LogicalFilter.create(f.getInput(), f.getCondition(),
          ImmutableSet.of(p.id));
    } else {
      r = filter;
    }

    bb.setRoot(r, false);
  }



```




### Join算子流程
1. sqlnode join -> logicalJoin -> EnumerableJoin
2. EnumerableJoinRule
3. EnumerableMergeJoinRule
```
  /**
   * Implementation of {@link JoinFactory} that returns a vanilla
   * {@link org.apache.calcite.rel.logical.LogicalJoin}.
   */
  private static class JoinFactoryImpl implements JoinFactory {
    public RelNode createJoin(RelNode left, RelNode right,
        RexNode condition, Set<CorrelationId> variablesSet,
        JoinRelType joinType, boolean semiJoinDone) {
      return LogicalJoin.create(left, right, condition, variablesSet, joinType,
          semiJoinDone, ImmutableList.of());
    }
  }




logical join可以转换多种join hash nested loop 等等

@Override public RelNode convert(RelNode rel) {
    LogicalJoin join = (LogicalJoin) rel;
    List<RelNode> newInputs = new ArrayList<>();
    for (RelNode input : join.getInputs()) {
      if (!(input.getConvention() instanceof EnumerableConvention)) {
        input =
            convert(
                input,
                input.getTraitSet()
                    .replace(EnumerableConvention.INSTANCE));
      }
      newInputs.add(input);
    }
    final RelOptCluster cluster = join.getCluster();
    final RelNode left = newInputs.get(0);
    final RelNode right = newInputs.get(1);
    final JoinInfo info = JoinInfo.of(left, right, join.getCondition());
    if (!info.isEqui() && join.getJoinType() != JoinRelType.INNER) {
      // EnumerableJoinRel only supports equi-join. We can put a filter on top
      // if it is an inner join.
      try {
        return EnumerableNestedLoopJoin.create(
            left,
            right,
            join.getCondition(),
            join.getVariablesSet(),
            join.getJoinType());
      } catch (InvalidRelException e) {
        EnumerableRules.LOGGER.debug(e.toString());
        return null;
      }
    } else {
      RelNode newRel;
      try {
        newRel = EnumerableHashJoin.create(
            left,
            right,
            info.getEquiCondition(left, right, cluster.getRexBuilder()),
            join.getVariablesSet(),
            join.getJoinType());
      } catch (InvalidRelException e) {
        EnumerableRules.LOGGER.debug(e.toString());
        return null;
      }
      if (!info.isEqui()) {
        newRel = new EnumerableFilter(cluster, newRel.getTraitSet(),
            newRel, info.getRemaining(cluster.getRexBuilder()));
      }
      return newRel;
    }
  }



判断join是 等价join还是不等价
public static JoinInfo of(RelNode left, RelNode right, RexNode condition) {
        List<Integer> leftKeys = new ArrayList();
        List<Integer> rightKeys = new ArrayList();
        List<Boolean> filterNulls = new ArrayList();
        RexNode remaining = RelOptUtil.splitJoinCondition(left, right, condition, leftKeys, rightKeys, filterNulls);
        return (JoinInfo)(remaining.isAlwaysTrue() ? new EquiJoinInfo(ImmutableIntList.copyOf(leftKeys), ImmutableIntList.copyOf(rightKeys)) : new NonEquiJoinInfo(ImmutableIntList.copyOf(leftKeys), ImmutableIntList.copyOf(rightKeys), remaining));
    }

```


### Union算子流程
```




```


## 纵向拆解 - RexNode
1. RexProgram：A collection of expressions which read inputs, compute output expressions and optionally use a condition to filter rows.
### Rexbuilder
1. 标量逻辑表达式
2. 存放整个UDF函数表，用于构建表达式
3. 应用在
   1. where/filter 的条件表达式
   2. join on 条件表达式
   3. udf 表达式


### RexProgram & RexProgramBuilder
1. RexProgram：表达整个计算逻辑 获取输入字段，输出字段，并整合成表达式
   1. A collection of expressions which read inputs, compute output expressions,and optionally use a condition to filter rows.
2. sql
   1. SELECT concat(a,b), c * 20 + 19 FROM MyTableRow WHERE c < 3
   2. table schame a b c
3. RexInputRef
   1. 输入的字段 a=$0 b=$1 c=$2 
4. RexCall 
   1. 比如 $3=CONCAT($t0, $t1)
5. RexLiteral
   1. 比如 $4=20
   2. $5=c * 20=*($t2, $t4)
   3. $6=19
   4. $7=c * 20 + 19=+($t5, $t6)
   5. $8=3
   6. $9=c < 3=<($t2, $t8)
6. RexLocalRef
   1. 输出字段 $3 $7
7. 


### 表达式创建 - addExpr & makeCall
1. 关键实现方法
   1. 构建program：createProg
```java

 /**
   * Creates a program, depending on variant:
   *
   * <ol>
   * <li><code>select (x + y) + (x + 1) as a, (x + x) as b from t(x, y)</code>
   * <li><code>select (x + y) + (x + 1) as a, (x + (x + 1)) as b
   * from t(x, y)</code>
   * <li><code>select (x + y) + (x + 1) as a, (x + x) as b from t(x, y)
   * where ((x + y) &gt; 1) and ((x + y) &gt; 1)</code>
   * <li><code>select (x + y) + (x + 1) as a, (x + x) as b from t(x, y)
   * where not case
   *           when x + 1 &gt; 5 then true
   *           when y is null then null
   *           else false
   *           end</code>
   * </ol>
   */
  private RexProgramBuilder createProg(int variant) {
    assert variant >= 0 && variant <= 4;
    List<RelDataType> types =
        Arrays.asList(
            typeFactory.createSqlType(SqlTypeName.INTEGER),
            typeFactory.createSqlType(SqlTypeName.INTEGER));
    List<String> names = Arrays.asList("x", "y");
    RelDataType inputRowType = typeFactory.createStructType(types, names);
    final RexProgramBuilder builder =
        new RexProgramBuilder(inputRowType, rexBuilder);
    // $t0 = x
    // $t1 = y
    // $t2 = $t0 + 1 (i.e. x + 1)
    final RexNode i0 = rexBuilder.makeInputRef(
        types.get(0), 0);
    final RexLiteral c1 = rexBuilder.makeExactLiteral(BigDecimal.ONE);
    final RexLiteral c5 = rexBuilder.makeExactLiteral(BigDecimal.valueOf(5L));
    RexLocalRef t2 =
        builder.addExpr(
            rexBuilder.makeCall(
                SqlStdOperatorTable.PLUS,
                i0,
                c1));
    // $t3 = 77 (not used)
    final RexLiteral c77 =
        rexBuilder.makeExactLiteral(
            BigDecimal.valueOf(77));
    RexLocalRef t3 =
        builder.addExpr(
            c77);
    Util.discard(t3);
    // $t4 = $t0 + $t1 (i.e. x + y)
    final RexNode i1 = rexBuilder.makeInputRef(
        types.get(1), 1);
    RexLocalRef t4 =
        builder.addExpr(
            rexBuilder.makeCall(
                SqlStdOperatorTable.PLUS,
                i0,
                i1));
    RexLocalRef t5;
    final RexLocalRef t1;
    switch (variant) {
    case 0:
    case 2:
      // $t5 = $t0 + $t0 (i.e. x + x)
      t5 = builder.addExpr(
          rexBuilder.makeCall(
              SqlStdOperatorTable.PLUS,
              i0,
              i0));
      t1 = null;
      break;
    case 1:
    case 3:
    case 4:
      // $tx = $t0 + 1
      t1 =
          builder.addExpr(
              rexBuilder.makeCall(
                  SqlStdOperatorTable.PLUS,
                  i0,
                  c1));
      // $t5 = $t0 + $tx (i.e. x + (x + 1))
      t5 =
          builder.addExpr(
              rexBuilder.makeCall(
                  SqlStdOperatorTable.PLUS,
                  i0,
                  t1));
      break;
    default:
      throw new AssertionError("unexpected variant " + variant);
    }
    // $t6 = $t4 + $t2 (i.e. (x + y) + (x + 1))
    RexLocalRef t6 =
        builder.addExpr(
            rexBuilder.makeCall(
                SqlStdOperatorTable.PLUS,
                t4,
                t2));
    builder.addProject(t6.getIndex(), "a");
    builder.addProject(t5.getIndex(), "b");

    final RexLocalRef t7;
    final RexLocalRef t8;
    switch (variant) {
    case 2:
      // $t7 = $t4 > $i0 (i.e. (x + y) > 0)
      t7 =
          builder.addExpr(
              rexBuilder.makeCall(
                  SqlStdOperatorTable.GREATER_THAN,
                  t4,
                  i0));
      // $t8 = $t7 AND $t7
      t8 =
          builder.addExpr(
              and(t7, t7));
      builder.addCondition(t8);
      builder.addCondition(t7);
      break;
    case 3:
    case 4:
      // $t7 = 5
      t7 = builder.addExpr(c5);
      // $t8 = $t2 > $t7 (i.e. (x + 1) > 5)
      t8 = builder.addExpr(gt(t2, t7));
      // $t9 = true
      final RexLocalRef t9 =
          builder.addExpr(trueLiteral);
      // $t10 = $t1 is not null (i.e. y is not null)
      assert t1 != null;
      final RexLocalRef t10 =
          builder.addExpr(
              rexBuilder.makeCall(SqlStdOperatorTable.IS_NOT_NULL, t1));
      // $t11 = false
      final RexLocalRef t11 =
          builder.addExpr(falseLiteral);
      // $t12 = unknown
      final RexLocalRef t12 =
          builder.addExpr(nullBool);
      // $t13 = case when $t8 then $t9 when $t10 then $t11 else $t12 end
      final RexLocalRef t13 =
          builder.addExpr(case_(t8, t9, t10, t11, t12));
      // $t14 = not $t13 (i.e. not case ... end)
      final RexLocalRef t14 =
          builder.addExpr(not(t13));
      // don't add 't14 is true' - that is implicit
      if (variant == 3) {
        builder.addCondition(t14);
      } else {
        // $t15 = $14 is true
        final RexLocalRef t15 =
            builder.addExpr(
                isTrue(t14));
        builder.addCondition(t15);
      }
    }
    return builder;
  }

```

### 表达式映射 - Select 映射 输入表和输出表
1. 输入表字段 15个 RelDataType
2. 表达式描述 8个 RexNode
3. 输出表字段 8个 = 表达式描述个数 RelDataType
4. RexProgramBuilder 融合 表达式和输出表字段名
5. RexBuilder RexProgram不再需要RexBuilder了 
   1. RexNode 已经足够描述整个表达式描述信息了
6. RexProgram
```

ProjectToCalcRule 会把rowtype 合并到 rexprogram
  public void onMatch(RelOptRuleCall call) {
    final LogicalProject project = call.rel(0);
    final RelNode input = project.getInput();
    final RexProgram program =
        RexProgram.create(
            input.getRowType(),
            project.getProjects(),
            null,
            project.getRowType(),
            project.getCluster().getRexBuilder());
    final LogicalCalc calc = LogicalCalc.create(input, program);
    call.transformTo(calc);
  }

```

### 表达式合并 - RexProgramBuilder
```java


/**
   * Merges two programs together.
   *
   * <p>All expressions become common sub-expressions. For example, the query
   *
   * <blockquote><pre>SELECT x + 1 AS p, x + y AS q FROM (
   *   SELECT a + b AS x, c AS y
   *   FROM t
   *   WHERE c = 6)}</pre></blockquote>
   *
   * <p>would be represented as the programs
   *
   * <blockquote><pre>
   *   Calc:
   *       Projects={$2, $3},
   *       Condition=null,
   *       Exprs={$0, $1, $0 + 1, $0 + $1})
   *   Calc(
   *       Projects={$3, $2},
   *       Condition={$4}
   *       Exprs={$0, $1, $2, $0 + $1, $2 = 6}
   * </pre></blockquote>
   *
   * <p>The merged program is
   *
   * <blockquote><pre>
   *   Calc(
   *      Projects={$4, $5}
   *      Condition=$6
   *      Exprs={0: $0       // a
   *             1: $1        // b
   *             2: $2        // c
   *             3: ($0 + $1) // x = a + b
   *             4: ($3 + 1)  // p = x + 1
   *             5: ($3 + $2) // q = x + y
   *             6: ($2 = 6)  // c = 6
   * </pre></blockquote>
   *
   * <p>Another example:</p>
   *
   * <blockquote>
   * <pre>SELECT *
   * FROM (
   *   SELECT a + b AS x, c AS y
   *   FROM t
   *   WHERE c = 6)
   * WHERE x = 5</pre>
   * </blockquote>
   *
   * <p>becomes
   *
   * <blockquote>
   * <pre>SELECT a + b AS x, c AS y
   * FROM t
   * WHERE c = 6 AND (a + b) = 5</pre>
   * </blockquote>
   *
   * @param topProgram    Top program. Its expressions are in terms of the
   *                      outputs of the bottom program.
   * @param bottomProgram Bottom program. Its expressions are in terms of the
   *                      result fields of the relational expression's input
   * @param rexBuilder    Rex builder
   * @param normalize     Whether to convert program to canonical form
   * @return Merged program
   */
  public static RexProgram mergePrograms(
      RexProgram topProgram,
      RexProgram bottomProgram,
      RexBuilder rexBuilder,
      boolean normalize) {
    // Initialize a program builder with the same expressions, outputs
    // and condition as the bottom program.
    assert bottomProgram.isValid(Litmus.THROW, null);
    assert topProgram.isValid(Litmus.THROW, null);
    final RexProgramBuilder progBuilder =
        RexProgramBuilder.forProgram(bottomProgram, rexBuilder, false);

    // Drive from the outputs of the top program. Register each expression
    // used as an output.
    final List<RexLocalRef> projectRefList =
        progBuilder.registerProjectsAndCondition(topProgram);

    // Switch to the projects needed by the top program. The original
    // projects of the bottom program are no longer needed.
    progBuilder.clearProjects();
    final RelDataType outputRowType = topProgram.getOutputRowType();
    for (Pair<RexLocalRef, String> pair
        : Pair.zip(projectRefList, outputRowType.getFieldNames(), true)) {
      progBuilder.addProject(pair.left, pair.right);
    }
    RexProgram mergedProg = progBuilder.getProgram(normalize);
    assert mergedProg.isValid(Litmus.THROW, null);
    assert mergedProg.getOutputRowType() == topProgram.getOutputRowType();
    return mergedProg;
  }

```

### 表达式简化 - program.normalize(rexBuilder, simplify)
```java

  /**
   * Tests how the condition is simplified.
   */
  @Test public void testSimplifyCondition() {
    final RexProgram program = createProg(3).getProgram(false);
    assertThat(program.toString(),
        is("(expr#0..1=[{inputs}], expr#2=[+($0, 1)], expr#3=[77], "
            + "expr#4=[+($0, $1)], expr#5=[+($0, 1)], expr#6=[+($0, $t5)], "
            + "expr#7=[+($t4, $t2)], expr#8=[5], expr#9=[>($t2, $t8)], "
            + "expr#10=[true], expr#11=[IS NOT NULL($t5)], expr#12=[false], "
            + "expr#13=[null:BOOLEAN], expr#14=[CASE($t9, $t10, $t11, $t12, $t13)], "
            + "expr#15=[NOT($t14)], a=[$t7], b=[$t6], $condition=[$t15])"));

    assertThat(program.normalize(rexBuilder, simplify).toString(),
        is("(expr#0..1=[{inputs}], expr#2=[+($t0, $t1)], expr#3=[1], "
            + "expr#4=[+($t0, $t3)], expr#5=[+($t2, $t4)], "
            + "expr#6=[+($t0, $t4)], expr#7=[5], expr#8=[<=($t4, $t7)], "
            + "a=[$t5], b=[$t6], $condition=[$t8])"));
  }

```


### 表达式反推到具体字段 - RexInputRef
1. 行表达式：https://juejin.cn/post/7113828979567493133
```java
创建每个表达式的唯一标识
 /**
   * Creates a program that projects its input fields but with possibly
   * different names for the output fields.
   */
  public static RexProgram createIdentity(
      RelDataType rowType,
      RelDataType outputRowType) {
    if (rowType != outputRowType
        && !Pair.right(rowType.getFieldList()).equals(
            Pair.right(outputRowType.getFieldList()))) {
      throw new IllegalArgumentException(
          "field type mismatch: " + rowType + " vs. " + outputRowType);
    }
    final List<RelDataTypeField> fields = rowType.getFieldList();
    final List<RexLocalRef> projectRefs = new ArrayList<>();
    final List<RexInputRef> refs = new ArrayList<>();
    for (int i = 0; i < fields.size(); i++) {
      final RexInputRef ref = RexInputRef.of(i, fields);
      refs.add(ref);
      projectRefs.add(new RexLocalRef(i, ref.getType()));
    }
    return new RexProgram(rowType, refs, projectRefs, null, outputRowType);
  }



jon下推表达式
 /**
   * Test {@link RelOptUtil#pushDownJoinConditions(org.apache.calcite.rel.core.Join, RelBuilder)}
   * where the join condition contains a complex expression
   */
  @Test public void testPushDownJoinConditionsWithExpandedIsNotDistinctUsingCase() {
    int leftJoinIndex = empScan.getRowType().getFieldNames().indexOf("DEPTNO");
    int rightJoinIndex = deptRow.getFieldNames().indexOf("DEPTNO");

    RexInputRef leftKeyInputRef = RexInputRef.of(leftJoinIndex, empDeptJoinRelFields);
    RexInputRef rightKeyInputRef =
        RexInputRef.of(empRow.getFieldCount() + rightJoinIndex, empDeptJoinRelFields);
    RexNode joinCond = relBuilder.call(SqlStdOperatorTable.CASE,
        relBuilder.call(SqlStdOperatorTable.IS_NULL,
            relBuilder.call(SqlStdOperatorTable.PLUS, leftKeyInputRef, relBuilder.literal(1))),
        relBuilder.call(SqlStdOperatorTable.IS_NULL, rightKeyInputRef),
        relBuilder.call(SqlStdOperatorTable.IS_NULL, rightKeyInputRef),
        relBuilder.call(SqlStdOperatorTable.IS_NULL,
            relBuilder.call(SqlStdOperatorTable.PLUS, leftKeyInputRef, relBuilder.literal(1))),
        relBuilder.call(SqlStdOperatorTable.EQUALS,
            relBuilder.call(SqlStdOperatorTable.PLUS, leftKeyInputRef, relBuilder.literal(1)),
            rightKeyInputRef));


    // Build the join operator and push down join conditions
    relBuilder.push(empScan);
    relBuilder.push(deptScan);
    relBuilder.join(JoinRelType.INNER, joinCond);
    Join join = (Join) relBuilder.build();
    RelNode transformed = RelOptUtil.pushDownJoinConditions(join, relBuilder);

    // Assert the new join operator
    assertThat(transformed.getRowType(), is(join.getRowType()));
    assertThat(transformed, is(instanceOf(Project.class)));
    RelNode transformedInput = transformed.getInput(0);
    assertThat(transformedInput, is(instanceOf(Join.class)));
    Join newJoin = (Join) transformedInput;
    assertThat(newJoin.getCondition().toString(),
        is(
            relBuilder.call(
                SqlStdOperatorTable.IS_NOT_DISTINCT_FROM,
                // Computed field is added at the end (and index start at 0)
                RexInputRef.of(empRow.getFieldCount(), join.getRowType()),
                // Right side is shifted by 1
                RexInputRef.of(empRow.getFieldCount() + 1 + rightJoinIndex, join.getRowType()))
              .toString()));
    assertThat(newJoin.getLeft(), is(instanceOf(Project.class)));
    Project leftInput = (Project) newJoin.getLeft();
    assertThat(leftInput.getChildExps().get(empRow.getFieldCount()).toString(),
        is(relBuilder.call(SqlStdOperatorTable.PLUS, leftKeyInputRef, relBuilder.literal(1))
            .toString()));
  }
}

```


### 业务自定义表达式 - 字段映射
1. 输入字段12个，输出字段12个，实现一个简单映射的表达式
```java
RelDataType inputRowType = typeFactory.createStructType(types, names);

final RexProgramBuilder builder =
        new RexProgramBuilder(inputRowType, rexBuilder);

// 简单映射 x -> 字段第0个
final RexNode i0 = rexBuilder.makeInputRef(
        types.get(0), 0);
// 定义常量 1 -> 字段第1个
final RexLiteral c1 = rexBuilder.makeExactLiteral(BigDecimal.ONE);

// x + 1 -> 字段第2个
RexLocalRef t2 =
        builder.addExpr(
            rexBuilder.makeCall(
                SqlStdOperatorTable.PLUS,
                i0,
                c1));


字段映射如下
            for (int i = 0; i < inputRowType.getFieldList().size(); i++) {
                RelDataTypeField field = (RelDataTypeField) inputRowType.getFieldList().get(i);
                final RexNode i0 = rexBuilder.makeInputRef(field.getType(), i);
                builder.addProject(i0, field.getName());
            }

//            RexNode rexNode =
            RexProgram program = builder.getProgram();
```

## 纵向拆解 - RelOptRule
1. RelOptRuleCall：是对一次优化规则执行参数的封装，它会作为优化规则方法matches和onMatch方法的参数。封装了当前调用需要的算子（rels），RelOptRuleOperand等执行规则的必要参数。
2. VolcanoRuleCall
3. DeferringRuleCall
4. 优化规则的实现：https://guimy.tech/calcite/2021/04/05/RelOptRule-of-calcite.html
5. RelOptRuleOperand：operand that determines whether a {@link RelOptRule}  can be applied to a particular expression.
6. RelOptRuleOperandChildPolicy
7. RelOptTableImpl

### 算子应用 - 自定义流程
1. 定义算子 业务自己实现
2. 定义规则 业务自己实现
3. 加载规则 calcite已实现
4. 运行规则引擎 calcite已实现
```java

 /**
   * Custom implementation of {@link Filter} for use
   * in test case to verify that {@link FilterMultiJoinMergeRule}
   * can be created with any {@link Filter} and not limited to
   * {@link org.apache.calcite.rel.logical.LogicalFilter}
   */
  private static class MyFilter extends Filter {

    MyFilter(
        RelOptCluster cluster,
        RelTraitSet traitSet,
        RelNode child,
        RexNode condition) {
      super(cluster, traitSet, child, condition);
    }

    public MyFilter copy(RelTraitSet traitSet, RelNode input,
        RexNode condition) {
      return new MyFilter(getCluster(), traitSet, input, condition);
    }

  }


  /**
   * Rule to transform {@link LogicalFilter} into
   * custom MyFilter
   */
  private static class MyFilterRule extends RelOptRule {
    static final MyFilterRule INSTANCE =
        new MyFilterRule(LogicalFilter.class, RelFactories.LOGICAL_BUILDER);

    private MyFilterRule(Class<? extends Filter> clazz,
        RelBuilderFactory relBuilderFactory) {
      super(RelOptRule.operand(clazz, RelOptRule.any()), relBuilderFactory, null);
    }

    @Override public void onMatch(RelOptRuleCall call) {
      final LogicalFilter logicalFilter = call.rel(0);
      final RelNode input = logicalFilter.getInput();
      final MyFilter myFilter = new MyFilter(input.getCluster(), input.getTraitSet(), input,
          logicalFilter.getCondition());
      call.transformTo(myFilter);
    }
  }
  


filter 和 project 规则应用
@Test public void testFilterAndProjectWithMultiJoin() throws Exception {
    final HepProgram preProgram = new HepProgramBuilder()
        .addRuleCollection(Arrays.asList(MyFilterRule.INSTANCE, MyProjectRule.INSTANCE))
        .build();

    final FilterMultiJoinMergeRule filterMultiJoinMergeRule =
        new FilterMultiJoinMergeRule(MyFilter.class, RelFactories.LOGICAL_BUILDER);

    final ProjectMultiJoinMergeRule projectMultiJoinMergeRule =
        new ProjectMultiJoinMergeRule(MyProject.class, RelFactories.LOGICAL_BUILDER);

    HepProgram program = new HepProgramBuilder()
        .addRuleCollection(
            Arrays.asList(
                JoinToMultiJoinRule.INSTANCE,
                filterMultiJoinMergeRule,
                projectMultiJoinMergeRule))
        .build();

    sql("select * from emp e1 left outer join dept d on e1.deptno = d.deptno where d.deptno > 3")
        .withPre(preProgram).with(program).check();
  }


  protected void checkPlanning(Tester tester, HepProgram preProgram,
      RelOptPlanner planner, String sql, boolean unchanged) {
    final DiffRepository diffRepos = getDiffRepos();
    String sql2 = diffRepos.expand("sql", sql);
    final RelRoot root = tester.convertSqlToRel(sql2);
    final RelNode relInitial = root.rel;

    assertTrue(relInitial != null);

    List<RelMetadataProvider> list = new ArrayList<>();
    list.add(DefaultRelMetadataProvider.INSTANCE);
    planner.registerMetadataProviders(list);
    RelMetadataProvider plannerChain =
        ChainedRelMetadataProvider.of(list);
    final RelOptCluster cluster = relInitial.getCluster();
    cluster.setMetadataProvider(plannerChain);

    RelNode relBefore;
    if (preProgram == null) {
      relBefore = relInitial;
    } else {
      HepPlanner prePlanner = new HepPlanner(preProgram);
      prePlanner.setRoot(relInitial);
      relBefore = prePlanner.findBestExp();
    }

    assertThat(relBefore, notNullValue());

    final String planBefore = NL + RelOptUtil.toString(relBefore);
    diffRepos.assertEquals("planBefore", "${planBefore}", planBefore);
    SqlToRelTestBase.assertValid(relBefore);

    planner.setRoot(relBefore);
    RelNode r = planner.findBestExp();
    if (tester.isLateDecorrelate()) {
      final String planMid = NL + RelOptUtil.toString(r);
      diffRepos.assertEquals("planMid", "${planMid}", planMid);
      SqlToRelTestBase.assertValid(r);
      final RelBuilder relBuilder =
          RelFactories.LOGICAL_BUILDER.create(cluster, null);
      r = RelDecorrelator.decorrelateQuery(r, relBuilder);
    }
    final String planAfter = NL + RelOptUtil.toString(r);
    if (unchanged) {
      assertThat(planAfter, is(planBefore));
    } else {
      diffRepos.assertEquals("planAfter", "${planAfter}", planAfter);
      if (planBefore.equals(planAfter)) {
        throw new AssertionError("Expected plan before and after is the same.\n"
            + "You must use unchanged=true or call checkUnchanged");
      }
    }
    SqlToRelTestBase.assertValid(r);
  }

```
### 算子转换 - ConverterRule
```java
public ConverterRule(Class<? extends RelNode> clazz, RelTrait in,
      RelTrait out, String description) {
    this(clazz, (Predicate<RelNode>) r -> true, in, out,
        RelFactories.LOGICAL_BUILDER, description);
  }


  public class EnumerableTableScanRule extends ConverterRule {

  @Deprecated // to be removed before 2.0
  public EnumerableTableScanRule() {
    this(RelFactories.LOGICAL_BUILDER);
  }

  /**
   * Creates an EnumerableTableScanRule.
   *
   * @param relBuilderFactory Builder for relational expressions
   */
  public EnumerableTableScanRule(RelBuilderFactory relBuilderFactory) {
    super(LogicalTableScan.class, (Predicate<RelNode>) r -> true,
        Convention.NONE, EnumerableConvention.INSTANCE, relBuilderFactory,
        "EnumerableTableScanRule");
  }

  @Override public RelNode convert(RelNode rel) {
    LogicalTableScan scan = (LogicalTableScan) rel;
    final RelOptTable relOptTable = scan.getTable();
    final Table table = relOptTable.unwrap(Table.class);
    if (!EnumerableTableScan.canHandle(table)) {
      return null;
    }
    final Expression expression = relOptTable.getExpression(Object.class);
    if (expression == null) {
      return null;
    }
    return EnumerableTableScan.create(scan.getCluster(), relOptTable);
  }
}




```
### 算子合并 - CalcMergeRule
1. 比较常见的 filter 和 project 算子合并到 calc计算算子中
2. FilterToCalcRule
3. ProjectToCalcRule
4. FilterCalcMergeRule
5. ProjectCalcMergeRule
6. CalcMergeRule
```java

filte 算子 和 calc合并

  public FilterCalcMergeRule(RelBuilderFactory relBuilderFactory) {
    super(
        operand(
            Filter.class,
            operand(LogicalCalc.class, any())),
        relBuilderFactory, null);
  }

  //~ Methods ----------------------------------------------------------------

  public void onMatch(RelOptRuleCall call) {
    final LogicalFilter filter = call.rel(0);
    final LogicalCalc calc = call.rel(1);

    // Don't merge a filter onto a calc which contains windowed aggregates.
    // That would effectively be pushing a multiset down through a filter.
    // We'll have chance to merge later, when the over is expanded.
    if (calc.getProgram().containsAggs()) {
      return;
    }

    // Create a program containing the filter.
    final RexBuilder rexBuilder = filter.getCluster().getRexBuilder();
    final RexProgramBuilder progBuilder =
        new RexProgramBuilder(
            calc.getRowType(),
            rexBuilder);
    progBuilder.addIdentity();
    progBuilder.addCondition(filter.getCondition());
    RexProgram topProgram = progBuilder.getProgram();
    RexProgram bottomProgram = calc.getProgram();

    // Merge the programs together.
    RexProgram mergedProgram =
        RexProgramBuilder.mergePrograms(
            topProgram,
            bottomProgram,
            rexBuilder);
    final LogicalCalc newCalc =
        LogicalCalc.create(calc.getInput(), mergedProgram);
    call.transformTo(newCalc);
  }
}


filter合并

 @Test public void testMergeFilter() throws Exception {
    HepProgram program = new HepProgramBuilder()
        .addRuleInstance(FilterProjectTransposeRule.INSTANCE)
        .addRuleInstance(FilterMergeRule.INSTANCE)
        .build();

    checkPlanning(program,
        "select name from (\n"
            + "  select *\n"
            + "  from dept\n"
            + "  where deptno = 10)\n"
            + "where deptno = 10\n");
  }


project 算子 和 calc算子合并
  /**
   * Creates a ProjectToCalcRule.
   *
   * @param relBuilderFactory Builder for relational expressions
   */
  public ProjectToCalcRule(RelBuilderFactory relBuilderFactory) {
    super(operand(LogicalProject.class, any()), relBuilderFactory, null);
  }

  //~ Methods ----------------------------------------------------------------

  public void onMatch(RelOptRuleCall call) {
    final LogicalProject project = call.rel(0);
    final RelNode input = project.getInput();
    final RexProgram program =
        RexProgram.create(
            input.getRowType(),
            project.getProjects(),
            null,
            project.getRowType(),
            project.getCluster().getRexBuilder());
    final LogicalCalc calc = LogicalCalc.create(input, program);
    call.transformTo(calc);
  }

union合并
 @Test
  public void testUnionMergeRule() throws Exception {
    HepProgram program = new HepProgramBuilder()
            .addRuleInstance(ProjectSetOpTransposeRule.INSTANCE)
            .addRuleInstance(ProjectRemoveRule.INSTANCE)
            .addRuleInstance(UnionMergeRule.INSTANCE)
            .build();

    checkPlanning(program,
            "select * from (\n"
                    + "select * from (\n"
                    + "  select name, deptno from dept\n"
                    + "  union all\n"
                    + "  select name, deptno from\n"
                    + "  (\n"
                    + "    select name, deptno, count(1) from dept group by name, deptno\n"
                    + "    union all\n"
                    + "    select name, deptno, count(1) from dept group by name, deptno\n"
                    + "  ) subq\n"
                    + ") a\n"
                    + "union all\n"
                    + "select name, deptno from dept\n"
                    + ") aa\n");
  }

```

### 算子位置互换 - FilterProjectTransposeRule
```java

 public void onMatch(RelOptRuleCall call) {
    final Filter filter = call.rel(0);
    final Project project = call.rel(1);

    if (RexOver.containsOver(project.getProjects(), null)) {
      // In general a filter cannot be pushed below a windowing calculation.
      // Applying the filter before the aggregation function changes
      // the results of the windowing invocation.
      //
      // When the filter is on the PARTITION BY expression of the OVER clause
      // it can be pushed down. For now we don't support this.
      return;
    }
    // convert the filter to one that references the child of the project
    RexNode newCondition =
        RelOptUtil.pushPastProject(filter.getCondition(), project);

    final RelBuilder relBuilder = call.builder();
    RelNode newFilterRel;
    if (copyFilter) {
      final RelNode input = project.getInput();
      final RelTraitSet traitSet = filter.getTraitSet()
          .replaceIfs(RelCollationTraitDef.INSTANCE,
              () -> Collections.singletonList(
                      input.getTraitSet().getTrait(RelCollationTraitDef.INSTANCE)))
          .replaceIfs(RelDistributionTraitDef.INSTANCE,
              () -> Collections.singletonList(
                      input.getTraitSet().getTrait(RelDistributionTraitDef.INSTANCE)));
      newFilterRel = filter.copy(traitSet, input, simplifyFilterCondition(newCondition, call));
    } else {
      newFilterRel =
          relBuilder.push(project.getInput()).filter(newCondition).build();
    }

    RelNode newProjRel =
        copyProject
            ? project.copy(project.getTraitSet(), newFilterRel,
                project.getProjects(), project.getRowType())
            : relBuilder.push(newFilterRel)
                .project(project.getProjects(), project.getRowType().getFieldNames())
                .build();

    call.transformTo(newProjRel);
  }

```


### 算子拆分 - CalcSplitRule
1. 插入算子需要借助 relbuilder
2. JoinProjectTransposeRule
3. JoinAddRedundantSemiJoinRule
4. 
```java

calc被拆分 project filter
public class CalcSplitRule extends RelOptRule {
  public static final CalcSplitRule INSTANCE =
      new CalcSplitRule(RelFactories.LOGICAL_BUILDER);

  /**
   * Creates a CalcSplitRule.
   *
   * @param relBuilderFactory Builder for relational expressions
   */
  public CalcSplitRule(RelBuilderFactory relBuilderFactory) {
    super(operand(Calc.class, any()), relBuilderFactory, null);
  }

  @Override public void onMatch(RelOptRuleCall call) {
    final Calc calc = call.rel(0);
    final Pair<ImmutableList<RexNode>, ImmutableList<RexNode>> projectFilter =
        calc.getProgram().split();
    final RelBuilder relBuilder = call.builder();
    relBuilder.push(calc.getInput());
    relBuilder.filter(projectFilter.right);
    relBuilder.project(projectFilter.left, calc.getRowType().getFieldNames());
    call.transformTo(relBuilder.build());
  }
}


JoinProjectTransposeRule
join 和 project 互换



  // finally, create the projection on top of the join
    final RelBuilder relBuilder = call.builder();
    relBuilder.push(newJoinRel);
    relBuilder.project(newProjExprs, joinRel.getRowType().getFieldNames());
    // if the join was outer, we might need a cast after the
    // projection to fix differences wrt nullability of fields
    if (joinType.isOuterJoin()) {
      relBuilder.convert(joinRel.getRowType(), false);
    }

    call.transformTo(relBuilder.build());


JoinAddRedundantSemiJoinRule
 public JoinAddRedundantSemiJoinRule(Class<? extends Join> clazz,
      RelBuilderFactory relBuilderFactory) {
    super(operand(clazz, any()), relBuilderFactory, null);
  }

  //~ Methods ----------------------------------------------------------------

  public void onMatch(RelOptRuleCall call) {
    Join origJoinRel = call.rel(0);
    if (origJoinRel.isSemiJoinDone()) {
      return;
    }

    // can't process outer joins using semijoins
    if (origJoinRel.getJoinType() != JoinRelType.INNER) {
      return;
    }

    // determine if we have a valid join condition
    final JoinInfo joinInfo = origJoinRel.analyzeCondition();
    if (joinInfo.leftKeys.size() == 0) {
      return;
    }

    RelNode semiJoin =
        LogicalJoin.create(origJoinRel.getLeft(),
            origJoinRel.getRight(),
            origJoinRel.getCondition(),
            ImmutableSet.of(),
            JoinRelType.SEMI);

    RelNode newJoinRel =
        origJoinRel.copy(
            origJoinRel.getTraitSet(),
            origJoinRel.getCondition(),
            semiJoin,
            origJoinRel.getRight(),
            JoinRelType.INNER,
            true);

    call.transformTo(newJoinRel);
  }

```

### 算子关联 - 基于 RelBuilder
```java

  /**
   * Sometimes the stack becomes so deeply nested it gets confusing. To keep
   * things straight, you can remove expressions from the stack. For example,
   * here we are building a bushy join:
   *
   * <blockquote><pre>
   *                join
   *              /      \
   *         join          join
   *       /      \      /      \
   * CUSTOMERS ORDERS LINE_ITEMS PRODUCTS
   * </pre></blockquote>
   *
   * <p>We build it in three stages. Store the intermediate results in variables
   * `left` and `right`, and use `push()` to put them back on the stack when it
   * is time to create the final `Join`.
   */
  private RelBuilder example4(RelBuilder builder) {
    final RelNode left = builder
        .scan("CUSTOMERS")
        .scan("ORDERS")
        .join(JoinRelType.INNER, "ORDER_ID")
        .build();

    final RelNode right = builder
        .scan("LINE_ITEMS")
        .scan("PRODUCTS")
        .join(JoinRelType.INNER, "PRODUCT_ID")
        .build();

    return builder
        .push(left)
        .push(right)
        .join(JoinRelType.INNER, "ORDER_ID");
  }



栈维护node顺序，join 关联栈的前两个node
  /** Creates a {@link Join} with correlating
   * variables. */
  public RelBuilder join(JoinRelType joinType, RexNode condition,
      Set<CorrelationId> variablesSet) {
    Frame right = stack.pop();
    final Frame left = stack.pop();
    final RelNode join;
    final boolean correlate = variablesSet.size() == 1;
    RexNode postCondition = literal(true);
    if (simplify) {
      // Normalize expanded versions IS NOT DISTINCT FROM so that simplifier does not
      // transform the expression to something unrecognizable
      if (condition instanceof RexCall) {
        condition = RelOptUtil.collapseExpandedIsNotDistinctFromExpr((RexCall) condition,
            getRexBuilder());
      }
      condition = simplifier.simplifyUnknownAsFalse(condition);
    }
    if (correlate) {
      final CorrelationId id = Iterables.getOnlyElement(variablesSet);
      final ImmutableBitSet requiredColumns =
          RelOptUtil.correlationColumns(id, right.rel);
      if (!RelOptUtil.notContainsCorrelation(left.rel, id, Litmus.IGNORE)) {
        throw new IllegalArgumentException("variable " + id
            + " must not be used by left input to correlation");
      }
      switch (joinType) {
      case LEFT:
        // Correlate does not have an ON clause.
        // For a LEFT correlate, predicate must be evaluated first.
        // For INNER, we can defer.
        stack.push(right);
        filter(condition.accept(new Shifter(left.rel, id, right.rel)));
        right = stack.pop();
        break;
      default:
        postCondition = condition;
      }
      join = correlateFactory.createCorrelate(left.rel, right.rel, id,
          requiredColumns, joinType);
    } else {
      join = joinFactory.createJoin(left.rel, right.rel, condition,
          variablesSet, joinType, false);
    }
    final ImmutableList.Builder<Field> fields = ImmutableList.builder();
    fields.addAll(left.fields);
    fields.addAll(right.fields);
    stack.push(new Frame(join, fields.build()));
    filter(postCondition);
    return this;
  }

栈维护node顺序，union关联整个栈列表node
 private RelBuilder setOp(boolean all, SqlKind kind, int n) {
    List<RelNode> inputs = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      inputs.add(0, build());
    }
    switch (kind) {
    case UNION:
    case INTERSECT:
    case EXCEPT:
      if (n < 1) {
        throw new IllegalArgumentException(
            "bad INTERSECT/UNION/EXCEPT input count");
      }
      break;
    default:
      throw new AssertionError("bad setOp " + kind);
    }
    switch (n) {
    case 1:
      return push(inputs.get(0));
    default:
      return push(setOpFactory.createSetOp(kind, inputs, all));
    }
  }

```

### 算子描述 - 实现一个ToString
1. calcite有digest，目的就是描述算子基本信息
```


```

### 优化流程 - program应用
```java
  @Test public void trimEmptyUnion32viaRelBuidler() throws Exception {
    RelBuilder relBuilder = RelBuilder.create(RelBuilderTest.config().build());

    // This somehow blows up (see trimEmptyUnion32, the second case)
    // (values(1) union all select * from (values(3)) where false)
    // union all values(2)

    // Non-trivial filter is important for the test to fail
    RelNode relNode = relBuilder
        .values(new String[]{"x"}, "1")
        .values(new String[]{"x"}, "3")
        .filter(relBuilder.equals(relBuilder.field("x"), relBuilder.literal("30")))
        .union(true)
        .values(new String[]{"x"}, "2")
        .union(true)
        .build();

    RelOptPlanner planner = relNode.getCluster().getPlanner();
    RuleSet ruleSet =
        RuleSets.ofList(
            PruneEmptyRules.UNION_INSTANCE,
            ValuesReduceRule.FILTER_INSTANCE,
            EnumerableRules.ENUMERABLE_PROJECT_RULE,
            EnumerableRules.ENUMERABLE_FILTER_RULE,
            EnumerableRules.ENUMERABLE_VALUES_RULE,
            EnumerableRules.ENUMERABLE_UNION_RULE);
    Program program = Programs.of(ruleSet);

    RelTraitSet toTraits = relNode.getTraitSet()
        .replace(EnumerableConvention.INSTANCE);

    RelNode output = program.run(planner, relNode, toTraits,
        ImmutableList.of(), ImmutableList.of());

    // Expected outcomes are:
    // 1) relation is optimized to simple VALUES
    // 2) the number of rule invocations is reasonable
    // 3) planner does not throw OutOfMemoryError
    assertThat("empty union should be pruned out of " + toString(relNode),
        Util.toLinux(toString(output)),
        equalTo("EnumerableUnion(all=[true])\n"
            + "  EnumerableValues(type=[RecordType(INTEGER EXPR$0)], tuples=[[{ 1 }]])\n"
            + "  EnumerableValues(type=[RecordType(INTEGER EXPR$0)], tuples=[[{ 2 }]])\n"));
  }
```
### 应用 - 在SQL中嵌入一个样本算子
1. RexProgramTest 行表达式如何构建
2. RelBuilder
```java
参考
public void onMatch(RelOptRuleCall call) {
    final Join join = call.rel(0);

    if (join.getJoinType() != JoinRelType.INNER) {
      return;
    }

    if (join.getCondition().isAlwaysTrue()) {
      return;
    }

    if (!join.getSystemFieldList().isEmpty()) {
      // FIXME Enable this rule for joins with system fields
      return;
    }

    final RelBuilder builder = call.builder();

    // NOTE jvs 14-Mar-2006:  See JoinCommuteRule for why we
    // preserve attribute semiJoinDone here.

    final RelNode cartesianJoin =
        join.copy(
            join.getTraitSet(),
            builder.literal(true),
            join.getLeft(),
            join.getRight(),
            join.getJoinType(),
            join.isSemiJoinDone());

    builder.push(cartesianJoin)
        .filter(join.getCondition());

    call.transformTo(builder.build());
  }


remove
public AggregateJoinJoinRemoveRule(
      Class<? extends Aggregate> aggregateClass,
      Class<? extends Join> joinClass, RelBuilderFactory relBuilderFactory) {
    super(
        operand(aggregateClass,
            operandJ(joinClass, null,
                join -> join.getJoinType() == JoinRelType.LEFT,
                operandJ(joinClass, null,
                    join -> join.getJoinType() == JoinRelType.LEFT, any()))),
        relBuilderFactory, null);
  }

    final RelBuilder relBuilder = call.builder();
    RexNode condition = RexUtil.shift(topJoin.getCondition(),
        leftBottomChildSize, -offset);
    RelNode join = relBuilder.push(bottomJoin.getLeft())
        .push(topJoin.getRight())
        .join(topJoin.getJoinType(), condition)
        .build();
    RelNode newAggregate = relBuilder.push(join)
        .aggregate(relBuilder.groupKey(groupSet), aggCalls.build())
        .build();




 public AggregateJoinRemoveRule(
      Class<? extends Aggregate> aggregateClass,
      Class<? extends Join> joinClass, RelBuilderFactory relBuilderFactory) {
    super(
        operand(aggregateClass,
            operandJ(joinClass, null,
                join -> join.getJoinType() == JoinRelType.LEFT
                    || join.getJoinType() == JoinRelType.RIGHT, any())),
        relBuilderFactory, null);
  }



  public ProjectJoinJoinRemoveRule(
      Class<? extends Project> projectClass,
      Class<? extends Join> joinClass, RelBuilderFactory relBuilderFactory) {
    super(
        operand(projectClass,
            operandJ(joinClass, null,
                join -> join.getJoinType() == JoinRelType.LEFT,
                operandJ(joinClass, null,
                    join -> join.getJoinType() == JoinRelType.LEFT, any()))),
        relBuilderFactory, null);
  }
```



### 应用 - 在SQL中嵌入一个触发器算子



### 应用 - 实现一个算子类似count(*)


## 纵向拆解 - 计划图优化
1. RBO 规则：https://strongduanmu.com/blog/deep-understand-of-apache-calcite-hep-planner.html
### HepPlanner
1. HepPlanner：基于规则的启发式优化器，实现了 RelOptPlanner 优化器接口；
2. HepProgram：提供了维护各种类型 HepInstruction 的容器，并支持指定 HepInstruction 被 HepPlanner 优化时处理的顺序；
3. HepProgramBuilder：用于创建 HepProgram；
4. HepInstruction：代表了 HepProgram 中的一个指令，目前包含了许多实现类，具体实现类的用途如下表所示：
5. hep维护自己vertex节点关系图，和 relnode完全不一样，两者结合有许多要注意的
   1. 比如 算子转化，算子新增在 hepPlanner中需要用 transformTo


### HepPlanner - 算子转换流程
1. RelNode -> HepRelVertex

### HepPlanner - transformTo 原理



## 纵向拆解 - 视图的validate
1. calcite 不支持DDL 包括创建view。但是有测试用例，从relnode层，扩展视图语法树
2. 参考源码
   1. ServerParserTest：Tests SQL parser extensions for DDL. 视图的测试用例
   2. core/src/test/java/org/apache/calcite/test/CalciteAssert.java
   3. testUserDefinedFunctionInView
   4. testModelWithModifiableView
   5. MaterializationTest#checkMaterialize
   6. ReflectiveSchemaTest#testView
   7. ReflectiveSchemaTest#testViewPath
3. 核心类
   1. ViewTable
   2. PlannerImpl.expandView 视图注册
   3. 

### 视图注册
```java
final SchemaPlus post =
          rootSchema.add(schema.schemaName, new AbstractSchema());
      post.add("EMP",
          ViewTable.viewMacro(post,
              "select * from (values\n"
                  + "    ('Jane', 10, 'F'),\n"
                  + "    ('Bob', 10, 'M'),\n"
                  + "    ('Eric', 20, 'M'),\n"
                  + "    ('Susan', 30, 'F'),\n"
                  + "    ('Alice', 30, 'F'),\n"
                  + "    ('Adam', 50, 'M'),\n"
                  + "    ('Eve', 50, 'F'),\n"
                  + "    ('Grace', 60, 'F'),\n"
                  + "    ('Wilma', cast(null as integer), 'F'))\n"
                  + "  as t(ename, deptno, gender)",
              ImmutableList.of(), ImmutableList.of("POST", "EMP"),
              null));
      post.add("DEPT",
          ViewTable.viewMacro(post,
              "select * from (values\n"
                  + "    (10, 'Sales'),\n"
                  + "    (20, 'Marketing'),\n"
                  + "    (30, 'Engineering'),\n"
                  + "    (40, 'Empty')) as t(deptno, dname)",
              ImmutableList.of(), ImmutableList.of("POST", "DEPT"),
              null));
      post.add("DEPT30",
          ViewTable.viewMacro(post,
              "select * from dept where deptno = 30",
              ImmutableList.of("POST"), ImmutableList.of("POST", "DEPT30"),
              null));
      post.add("EMPS",
          ViewTable.viewMacro(post,
              "select * from (values\n"
                  + "    (100, 'Fred',  10, CAST(NULL AS CHAR(1)), CAST(NULL AS VARCHAR(20)), 40,               25, TRUE,    FALSE, DATE '1996-08-03'),\n"
                  + "    (110, 'Eric',  20, 'M',                   'San Francisco',           3,                80, UNKNOWN, FALSE, DATE '2001-01-01'),\n"
                  + "    (110, 'John',  40, 'M',                   'Vancouver',               2, CAST(NULL AS INT), FALSE,   TRUE,  DATE '2002-05-03'),\n"
                  + "    (120, 'Wilma', 20, 'F',                   CAST(NULL AS VARCHAR(20)), 1,                 5, UNKNOWN, TRUE,  DATE '2005-09-07'),\n"
                  + "    (130, 'Alice', 40, 'F',                   'Vancouver',               2, CAST(NULL AS INT), FALSE,   TRUE,  DATE '2007-01-01'))\n"
                  + " as t(empno, name, deptno, gender, city, empid, age, slacker, manager, joinedat)",
              ImmutableList.of(), ImmutableList.of("POST", "EMPS"),
              null));


调用SQL示例

post.add("V_EMP",
        ViewTable.viewMacro(post, viewSql, ImmutableList.of(),
            ImmutableList.of("POST", "V_EMP"), null));

ResultSet viewResultSet =
        statement.executeQuery("select * from \"POST\".\"V_EMP\"");

```


### 视图 是以function维度 注册到schema
1. 校验过程中，会临时调用 function.apply，返回复杂的TranslatableTable
```

String viewSql = "select * from CUBE2L_IB00040010_CN000";
ViewTableMacro vtm = ViewTable.viewMacro(rootSchema, viewSql, ImmutableList.of(), ImmutableList.of("ad_inner_loop_live_order_fg_channel_view_table"), null);
  rootSchema.add("vtm_view_name", vtm);

```


## 纵向拆解 - SqlToRelConverter 
1. 基本组件
   1. SqlValidator 负责校验
   2. RexBuilder 表达式解析器
   3. RelBuilder node构建器
   4. CatalogReader 对接元数据
   5. RelOptCluster 物理节点信息
   6. SqlOperatorTable 全局函数表
   7. RelDataTypeFactory 数据类型工厂
   8. ViewExpander 视图管理器
2. 翻译组件
   1. SubQueryConverter 子查询转换器
   2. SqlNodeToRexConverter 表达式转换器
   3. Blackboard Workspace for translating an individual SELECT statement (or sub-SELECT).
3. 对外输出API能力 - convert主线
   1. convertQuery
   2. convertQueryRecursive
   3. requiredCollation
   4. checkConvertedType
   5. getValidatedNodeType
   6. RelRoot 最终输出的结果
      1. RelNode RelDataType（经过校验生成的结果） SqlKind RelCollation 组合而成


### visit设计模式 - 获取sqlnode信息
```
visit(SqlIdentifier): Void
visit(SqlNodeList): Void
visit(SqlLiteral): Void
visit(SqlDataTypeSpec): Void
visit(SqlDynamicParam): Void
visit(SqlIntervalQualifier): Void
visit(SqlCall): Void

```

### convert能力
```
convertAgg(Blackboard, SqlSelect, List<SqlNode>): void
convertCollectionTable(Blackboard, SqlCall): void
convertColumnList(SqlInsert, RelNode): RelNode
convertCursor(Blackboard, SubQuery): RelNode
convertDelete(SqlDelete): RelNode
convertDynamicParam(SqlDynamicParam): RexDynamicParam
convertExists(SqlNode, SubQueryType, Logic, boolean, RelDataType): Exists
convertExpression(SqlNode): RexNode
convertExpression(SqlNode, Map<String, RexNode>): RexNode
convertExtendedExpression(SqlNode, Blackboard): RexNode
convertFrom(Blackboard, SqlNode): void
convertIdentifier(Blackboard, SqlIdentifier): RexNode
convertIdentifier(Blackboard, SqlIdentifier, SqlNodeList): void
convertInsert(SqlInsert): RelNode
convertInToOr(Blackboard, List<RexNode>, SqlNodeList, SqlInOperator): RexNode
convertJoinCondition(Blackboard, SqlValidatorNamespace, SqlValidatorNamespace, SqlNode, JoinConditionType, RelNode, RelNode): RexNode
convertJoinType(JoinType): JoinRelType
convertLiteralInValuesList(SqlNode, Blackboard, RelDataType, int): RexLiteral
convertMatchRecognize(Blackboard, SqlCall): void
convertMerge(SqlMerge): RelNode
convertMultisets(List<SqlNode>, Blackboard): RelNode
convertNonCorrelatedSubQuery(SubQuery, Blackboard, RelNode, boolean): boolean
convertOrder(SqlSelect, Blackboard, RelCollation, List<SqlNode>, SqlNode, SqlNode): void
convertOrderItem(SqlSelect, SqlNode, List<SqlNode>, Direction, NullDirection): RelFieldCollation
convertOver(Blackboard, SqlNode): RexNode
convertQuery(SqlNode, boolean, boolean): RelRoot
convertQueryOrInList(Blackboard, SqlNode, RelDataType): RelNode
convertQueryRecursive(SqlNode, boolean, RelDataType): RelRoot
convertRowConstructor(Blackboard, SqlCall): RelNode
convertRowValues(Blackboard, SqlNode, Collection<SqlNode>, boolean, RelDataType): RelNode
convertSelect(SqlSelect, boolean): RelNode
convertSelectImpl(Blackboard, SqlSelect): void
convertSelectList(Blackboard, SqlSelect, List<SqlNode>): void
convertSetOp(SqlCall): RelNode
convertToSingleValueSubq(SqlNode, RelNode): RelNode
convertUpdate(SqlUpdate): RelNode
convertUsing(SqlValidatorNamespace, SqlValidatorNamespace, List<String>): RexNode
convertValues(SqlCall, RelDataType): RelNode
convertValuesImpl(Blackboard, SqlCall, RelDataType): void
convertWhere(Blackboard, SqlNode): void
convertWith(SqlWith, boolean): RelRoot


Blackboard
  convertExpression(SqlNode): RexNode
  convertInterval(SqlIntervalQualifier): RexNode
  convertLiteral(SqlLiteral): RexNode
  convertSortExpression(SqlNode, Direction, NullDirection): RexFieldCollation

SqlNodeToRexConverter
  convertCall(SqlRexContext, SqlCall): RexNode
  convertInterval(SqlRexContext, SqlIntervalQualifier): RexLiteral
  convertLiteral(SqlRexContext, SqlLiteral): RexNode

```


### 构建相关组件
```

createAggImpl(Blackboard, AggConverter, SqlNodeList, SqlNodeList, SqlNode, List<SqlNode>): void
createAggregate(Blackboard, ImmutableBitSet, ImmutableList<ImmutableBitSet>, List<AggregateCall>): RelNode
createBlackboard(SqlValidatorScope, Map<String, RexNode>, boolean): Blackboard
createInsertBlackboard(RelOptTable, RexNode, List<String>): Blackboard
createJoin(Blackboard, RelNode, RelNode, RexNode, JoinRelType): RelNode
createModify(RelOptTable, RelNode): RelNode
createSource(RelOptTable, RelNode, ModifiableView, RelDataType): RelNode
createToRelContext(): ToRelContext

```


### 一个异常栈看 调用链路和函数执行顺序
```
sql = select xx join on conditon

Caused by: java.lang.RuntimeException: while converting CONCAT(`event`.`llsid`, '_', `event`.`device_id`) = `ad_pv_context_entity`.`user_hash`
	at org.apache.calcite.sql2rel.ReflectiveConvertletTable.lambda$registerNodeTypeMethod$0(ReflectiveConvertletTable.java:86)
	at org.apache.calcite.sql2rel.SqlNodeToRexConverterImpl.convertCall(SqlNodeToRexConverterImpl.java:63)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4708)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4013)
	at org.apache.calcite.sql.SqlCall.accept(SqlCall.java:138)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.convertExpression(SqlToRelConverter.java:4577)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertJoinCondition(SqlToRelConverter.java:2627)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertFrom(SqlToRelConverter.java:2060)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertSelectImpl(SqlToRelConverter.java:646)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertSelect(SqlToRelConverter.java:627)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertQueryRecursive(SqlToRelConverter.java:3100)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertQuery(SqlToRelConverter.java:563)
	at org.apache.calcite.prepare.PlannerImpl.rel(PlannerImpl.java:235)
	at com.kuaishou.kaiworks.table.planner.delegation.PlannerContext.rel(PlannerContext.java:130)
	at com.kuaishou.kaiworks.sql.parser.impl.InsertParser.parseSql(InsertParser.java:83)
	... 26 more
Caused by: java.lang.AssertionError
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.getRootField(SqlToRelConverter.java:4369)
	at org.apache.calcite.sql2rel.SqlToRelConverter.adjustInputRef(SqlToRelConverter.java:3682)
	at org.apache.calcite.sql2rel.SqlToRelConverter.convertIdentifier(SqlToRelConverter.java:3654)
	at org.apache.calcite.sql2rel.SqlToRelConverter.access$2100(SqlToRelConverter.java:217)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4717)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4013)
	at org.apache.calcite.sql.SqlIdentifier.accept(SqlIdentifier.java:334)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.convertExpression(SqlToRelConverter.java:4577)
	at org.apache.calcite.sql2rel.StandardConvertletTable.convertCast(StandardConvertletTable.java:518)
	at org.apache.calcite.sql2rel.SqlNodeToRexConverterImpl.convertCall(SqlNodeToRexConverterImpl.java:63)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4708)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.visit(SqlToRelConverter.java:4013)
	at org.apache.calcite.sql.SqlCall.accept(SqlCall.java:138)
	at org.apache.calcite.sql2rel.SqlToRelConverter$Blackboard.convertExpression(SqlToRelConverter.java:4577)
	at org.apache.calcite.sql2rel.StandardConvertletTable.convertExpressionList(StandardConvertletTable.java:790)
	at org.apache.calcite.sql2rel.StandardConvertletTable.convertCall(StandardConvertletTable.java:766)
	at org.apache.calcite.sql2rel.StandardConvertletTable.convertCall(StandardConvertletTable.java:750)
	... 45 more
```


## 纵向拆解 - RelToSqlConverter

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

## 应用场景
### Flink使用Calcite
1. PlannerContext：封装calcite planner能力 
2. FlinkSqlParserImpl：Flink解析器
3. FlinkSqlConformance：Flink SQL部分语法兼容情况
4. FlinkCostFactory：用于CBO，计算cpu和network带宽成本，使用较少，但是依然实现了简单的类，方便修改扩展
5. FlinkTypeSystem：自定义数据类型系统，基于calcite扩展
6. FlinkTypeFactory：基于JavaTypeFactoryImpl 扩展生成数据类型
   1. 贡献者
      1. Jingsong Lee https://github.com/JingsongLi
      2. wuchong：https://github.com/wuchong
7. SqlToRelConverter.Config：
8. SqlExprToRexConverter：
9. SqlOperatorTable：查询算子和函数的全局表
   1. ChainedSqlOperatorTable
   2. SqlStdOperatorTable：比如union join group等等
   3. ListSqlOperatorTable：比如count udf等等
10. ExpressionReducer：常量表达式代码生成，扩展RexExecutor
   1. godfreyhe：https://github.com/godfreyhe
11. FlinkContext：
12. PlannerContext
    1.  CatalogManager
    2.  FunctionCatalog
    3.  TableConfig
13. RelTraitDef：物理属性，比如FlinkRelDistribution
14. FlinkRelFactories：基于RelBuilderFactory扩展，新建RelNode类，比如RankRel 和 SinkRel