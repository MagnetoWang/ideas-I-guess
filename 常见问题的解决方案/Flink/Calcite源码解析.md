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
2. 物化视图-数据格框架(Lattice Framework)：https://cloud.tencent.com/developer/article/2450528
3. 
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
   15. SqlValidatorScope：可以认为是校验流程中每个 SqlNode 的工作上下文，当校验表达式时，通过 SqlValidatorScope 的 resolve 方法进行解析，如果成功的话会返回对应的 SqlValidatorNamespace 描述结果类型

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

### calcite 
```


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
2. Graphviz 格式
```
示例链接

https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%20%20%20%20%09root%20%5Bstyle%3Dfilled%2Clabel%3D%22Root%22%5D%3B%0A%20%20%20%20%09subgraph%20cluster0%7B%0A%20%20%20%20%09%09label%3D%22Set%200%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission)%22%3B%0A%20%20%20%20%09%09rel99%20%5Blabel%3D%22rel%2399%3ALogicalTableScan%5Cntable%3D%5Bhr%2C%20emps%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel120%20%5Blabel%3D%22rel%23120%3AEnumerableTableScan%5Cntable%3D%5Bhr%2C%20emps%5D%5Cnrows%3D4.0%2C%20cost%3D%7B4.0%20rows%2C%205.0%20cpu%2C%200.0%20io%7D%22%2Ccolor%3Dblue%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset106%20%5Blabel%3D%22rel%23106%3ARelSubset%230.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset121%20%5Blabel%3D%22rel%23121%3ARelSubset%230.ENUMERABLE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster1%7B%0A%20%20%20%20%09%09label%3D%22Set%201%20RecordType(JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name)%22%3B%0A%20%20%20%20%09%09rel100%20%5Blabel%3D%22rel%23100%3ALogicalTableScan%5Cntable%3D%5Bhr%2C%20depts%5D%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel122%20%5Blabel%3D%22rel%23122%3AEnumerableTableScan%5Cntable%3D%5Bhr%2C%20depts%5D%5Cnrows%3D3.0%2C%20cost%3D%7B3.0%20rows%2C%204.0%20cpu%2C%200.0%20io%7D%22%2Ccolor%3Dblue%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset107%20%5Blabel%3D%22rel%23107%3ARelSubset%231.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset123%20%5Blabel%3D%22rel%23123%3ARelSubset%231.ENUMERABLE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster2%7B%0A%20%20%20%20%09%09label%3D%22Set%202%20RecordType(JavaType(int)%20deptno)%22%3B%0A%20%20%20%20%09%09rel108%20%5Blabel%3D%22rel%23108%3ALogicalProject%5Cninput%3DRelSubset%23107%2Cinputs%3D0%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset109%20%5Blabel%3D%22rel%23109%3ARelSubset%232.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster3%7B%0A%20%20%20%20%09%09label%3D%22Set%203%20RecordType(JavaType(int)%20deptno)%22%3B%0A%20%20%20%20%09%09rel110%20%5Blabel%3D%22rel%23110%3ALogicalAggregate%5Cninput%3DRelSubset%23109%2Cgroup%3D%7B0%7D%5Cnrows%3D3.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset111%20%5Blabel%3D%22rel%23111%3ARelSubset%233.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster4%7B%0A%20%20%20%20%09%09label%3D%22Set%204%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission%2C%20JavaType(int)%20deptno0)%22%3B%0A%20%20%20%20%09%09rel112%20%5Blabel%3D%22rel%23112%3ALogicalJoin%5Cnleft%3DRelSubset%23106%2Cright%3DRelSubset%23111%2Ccondition%3D%3D(%241%2C%20%245)%2CjoinType%3Dinner%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel129%20%5Blabel%3D%22rel%23129%3ALogicalSort%5Cninput%3DRelSubset%23113%2Csort0%3D%240%2Cdir0%3DASC%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset113%20%5Blabel%3D%22rel%23113%3ARelSubset%234.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%09subset131%20%5Blabel%3D%22rel%23131%3ARelSubset%234.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset113%20-%3E%20subset131%3B%09%7D%0A%20%20%20%20%09subgraph%20cluster5%7B%0A%20%20%20%20%09%09label%3D%22Set%205%20RecordType(JavaType(int)%20deptno%2C%20JavaType(int)%20empid)%22%3B%0A%20%20%20%20%09%09rel114%20%5Blabel%3D%22rel%23114%3ALogicalProject%5Cninput%3DRelSubset%23113%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel128%20%5Blabel%3D%22rel%23128%3ALogicalProject%5Cninput%3DRelSubset%23127%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset115%20%5Blabel%3D%22rel%23115%3ARelSubset%235.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster6%7B%0A%20%20%20%20%09%09label%3D%22Set%206%20RecordType(JavaType(int)%20deptno%2C%20JavaType(int)%20empid)%22%3B%0A%20%20%20%20%09%09rel116%20%5Blabel%3D%22rel%23116%3ALogicalSort%5Cninput%3DRelSubset%23115%2Csort0%3D%241%2Cdir0%3DASC%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel119%20%5Blabel%3D%22rel%23119%3AAbstractConverter%5Cninput%3DRelSubset%23117%2Cconvention%3DENUMERABLE%2Csort%3D%5B1%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel132%20%5Blabel%3D%22rel%23132%3ALogicalProject%5Cninput%3DRelSubset%23131%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D1.7999999999999998%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel136%20%5Blabel%3D%22rel%23136%3ALogicalProject%5Cninput%3DRelSubset%23135%2Cexprs%3D%5B%241%2C%20%240%5D%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset117%20%5Blabel%3D%22rel%23117%3ARelSubset%236.NONE.%5B1%5D%22%5D%0A%20%20%20%20%09%09subset118%20%5Blabel%3D%22rel%23118%3ARelSubset%236.ENUMERABLE.%5B1%5D%22%2Ccolor%3Dred%5D%0A%20%20%20%20%09%7D%0A%20%20%20%20%09subgraph%20cluster7%7B%0A%20%20%20%20%09%09label%3D%22Set%207%20RecordType(JavaType(int)%20empid%2C%20JavaType(int)%20deptno%2C%20JavaType(class%20java.lang.String)%20name%2C%20JavaType(int)%20salary%2C%20JavaType(class%20java.lang.Integer)%20commission)%22%3B%0A%20%20%20%20%09%09rel126%20%5Blabel%3D%22rel%23126%3ALogicalJoin%5Cnleft%3DRelSubset%23106%2Cright%3DRelSubset%23109%2Ccondition%3D%3D(%241%2C%20%245)%2CjoinType%3Dsemi%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09rel133%20%5Blabel%3D%22rel%23133%3ALogicalSort%5Cninput%3DRelSubset%23127%2Csort0%3D%240%2Cdir0%3DASC%5Cnrows%3D4.0%2C%20cost%3D%7Binf%7D%22%2Cshape%3Dbox%5D%0A%20%20%20%20%09%09subset127%20%5Blabel%3D%22rel%23127%3ARelSubset%237.NONE.%5B%5D%22%5D%0A%20%20%20%20%09%09subset135%20%5Blabel%3D%22rel%23135%3ARelSubset%237.NONE.%5B0%5D%22%5D%0A%20%20%20%20%09%09subset127%20-%3E%20subset135%3B%09%7D%0A%20%20%20%20%09root%20-%3E%20subset118%3B%0A%20%20%20%20%09subset106%20-%3E%20rel99%3B%0A%20%20%20%20%09subset121%20-%3E%20rel120%5Bcolor%3Dblue%5D%3B%0A%20%20%20%20%09subset107%20-%3E%20rel100%3B%0A%20%20%20%20%09subset123%20-%3E%20rel122%5Bcolor%3Dblue%5D%3B%0A%20%20%20%20%09subset109%20-%3E%20rel108%3B%20rel108%20-%3E%20subset107%3B%0A%20%20%20%20%09subset111%20-%3E%20rel110%3B%20rel110%20-%3E%20subset109%3B%0A%20%20%20%20%09subset113%20-%3E%20rel112%3B%20rel112%20-%3E%20subset106%5Blabel%3D%220%22%5D%3B%20rel112%20-%3E%20subset111%5Blabel%3D%221%22%5D%3B%0A%20%20%20%20%09subset131%20-%3E%20rel129%3B%20rel129%20-%3E%20subset113%3B%0A%20%20%20%20%09subset115%20-%3E%20rel114%3B%20rel114%20-%3E%20subset113%3B%0A%20%20%20%20%09subset115%20-%3E%20rel128%3B%20rel128%20-%3E%20subset127%3B%0A%20%20%20%20%09subset117%20-%3E%20rel116%3B%20rel116%20-%3E%20subset115%3B%0A%20%20%20%20%09subset118%20-%3E%20rel119%3B%20rel119%20-%3E%20subset117%3B%0A%20%20%20%20%09subset117%20-%3E%20rel132%3B%20rel132%20-%3E%20subset131%3B%0A%20%20%20%20%09subset117%20-%3E%20rel136%3B%20rel136%20-%3E%20subset135%3B%0A%20%20%20%20%09subset127%20-%3E%20rel126%3B%20rel126%20-%3E%20subset106%5Blabel%3D%220%22%5D%3B%20rel126%20-%3E%20subset109%5Blabel%3D%221%22%5D%3B%0A%20%20%20%20%09subset135%20-%3E%20rel133%3B%20rel133%20-%3E%20subset127%3B%0A%20%20%20%20%7D

```

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
```
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
```
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