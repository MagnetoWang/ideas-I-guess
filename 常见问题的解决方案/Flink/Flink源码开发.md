## 开发路线
1. 代码打印
   1. FlinkGraph
      1. streamgraph
      2. jobgraph
      3. executegraph
   2. FlinkPlan
   3. StreamRecord结构
2. 扩展SQL语法能力
   1. flink sql如何集成calcite
   2. 注册数据源
   3. 解析sql，拿到sqlnode
   4. 复用validate能力 并测试
   5.  
3. 扩展算子能力
4. 无缝对接新元数据识别能力
5. 版本特性总结，跟踪整个设计路线
   


## Flink编译和开发
```
编译命令
mvn clean package -DskipTests -Dcheckstyle.skip=true -Dmaven.enforcer.skip=true



 -Dmaven.enforcer.skip=true

```

### 查看执行图
1. flink sql 可视化网站
   2. https://wints.github.io/flink-web//visualizer/
2. 
```

{"nodes":[{"id":1,"type":"Source: Collection Source","pact":"Data Source","contents":"Source: Collection Source","parallelism":1},{"id":2,"type":"Map","pact":"Operator","contents":"Map","parallelism":128,"predecessors":[{"id":1,"ship_strategy":"REBALANCE","side":"second"}]},{"id":4,"type":"Window(TumblingProcessingTimeWindows(10000), , SumAggregator, PassThroughWindowFunction)","pact":"Operator","contents":"Window(TumblingProcessingTimeWindows(10000), , SumAggregator, PassThroughWindowFunction)","parallelism":128,"predecessors":[{"id":2,"ship_strategy":"HASH","side":"second"}]},{"id":6,"type":"Sink: Print to Std. Out","pact":"Data Sink","contents":"Sink: Print to Std. Out","parallelism":128,"predecessors":[{"id":4,"ship_strategy":"FORWARD","side":"second"}]}]}


```



### 造数
```
    public List<Row> fakeRows() {
        // 创建虚拟行列表
        List<Row> rows = new ArrayList<>();
        rows.add(Row.of("15030140049", "wangzixian", 18));
        rows.add(Row.of("5030140049", "wangzixian", 19));
        rows.add(Row.of("15030140049", "wangzixian", 20));
        return rows;
    }

    public RowTypeInfo rowTypeInfo() {
        TypeInformation<?>[] types = {
                BasicTypeInfo.STRING_TYPE_INFO,
                BasicTypeInfo.STRING_TYPE_INFO,
                BasicTypeInfo.INT_TYPE_INFO
        };
        String[] names = {"a", "b", "c"};
        RowTypeInfo typeInfo = new RowTypeInfo(types, names);
        return typeInfo;
    }

private static final List<Row> testData = new ArrayList<>();
    private static final RowTypeInfo testTypeInfo =
            new RowTypeInfo(
                    new TypeInformation[] {Types.INT, Types.LONG, Types.STRING},
                    new String[] {"a", "b", "c"});

    static {
        testData.add(Row.of(1, 1L, "Hi"));
        testData.add(Row.of(2, 2L, "Hello"));
        testData.add(Row.of(3, 2L, "Hello world"));
        testData.add(Row.of(3, 3L, "Hello world!"));
    }




```


### WordCount 实现
```
public class WordCount {
   public static void main(String[] args) throws Exception {
      // StreamExecutionEnvironment初始化
      final StreamExecutionEnvironment env = StreamExecutionEnvironment.
         getExecutionEnvironment();
      // 业务逻辑转换代码
      DataStream<String> text = env.readTextFile("the_path_for_input");
      DataStream<Tuple2<String, Integer>> counts =
         text.flatMap(new Tokenizer())
         .keyBy(0).sum(1);
      counts.writeAsText("the_path_for_output");
      // 执行应用程序
      env.execute("Streaming WordCount");
   }
}

核心类
StreamExecutionEnvironment
DataStream
```


## 扩展SQL语法能力
1. 作者推荐方式，修改config.fmpp：https://github.com/apache/calcite/blob/master/core/src/test/codegen/config.fmpp
2. Flink语法扩展--SqlRichExplain为例：https://blog.csdn.net/blackjjcat/article/details/124226170
3. Apache Calcite SQL解析及语法扩展：https://liebing.org.cn/apache-calcite-sql-parser.html
4. Flink源码阅读之Flinksql执行流程：https://zhuxiaoshang.github.io/2020/07/03/Flink%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB%E4%B9%8BFlinksql%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B/
5. Flink 自定义拓展 SQL 语法 - 猫猫爱吃小鱼粮的文章 - 知乎 https://zhuanlan.zhihu.com/p/663263244
6. 



### 文件格式
```
codegen
├── config.fmpp
├── default_config.fmpp
├── includes
│   ├── compoundIdentifier.ftl
│   └── parserImpls.ftl
└── templates
    └── Parser.jj		# 模板Parser.jj

```

### TableImpl实现算子能力 select
1. 参考：org.apache.flink.table.api.internal.TableImpl
```

	@Override
	public Table select(String fields) {
		return select(ExpressionParser.parseExpressionList(fields).toArray(new Expression[0]));
	}


```






### 知乎AI总结
```
要在Flink的Calcite中新增SQL语法，您需要遵循以下步骤：

定义SqlNode节点类：

在Flink的源码或您的项目中，创建一个新的Java类（例如SqlShowCatalogs），继承自SqlNode。
实现unparse方法，定义如何将这个SQL节点转换为字符串输出。
修改FTL文件：

在parserImpls.ftl文件中，添加新的语法逻辑。例如，为“SHOW CATALOGS”命令创建解析规则。
使用FTL语法定义新的解析路径，如SqlShowCatalogs SqlShowCatalogs() : {...}，匹配您的SQL语法结构。
配置FMPP：

复制并修改config.fmpp文件到您的项目src/main/codegen目录下。
在该文件中配置需要的扩展文件和路径，确保它指向您的.ftl文件。
使用Parser.tdd简化配置：

创建或修改Parser.tdd文件来指定生成解析器的包路径和相关设置，这可以简化config.fmpp的编写。
编译和生成解析器：

编译项目，FMPP工具会根据config.fmpp和相关FTL文件自动生成解析器代码，实现对新SQL语法的支持。
测试新语法：

在Flink SQL客户端或应用中尝试使用新定义的SQL语法，确保一切按预期工作。
确保在进行这些更改时，您的开发环境已正确设置，并且对Apache Calcite和Flink的SQL解析机制有基本的理解。



```


## 动态加载代码 JaninoCompiler
1. sparkadapt 需要加载calcite代码
```

 public ArrayBindable compile(ClassDeclaration expr, String s) {
    final String className = "CalciteProgram" + classId.getAndIncrement();
    final String classFileName = className + ".java";
    String source = "public class " + className + "\n"
        + "    implements " + ArrayBindable.class.getName()
        + ", " + Serializable.class.getName()
        + " {\n"
        + s + "\n"
        + "}\n";

    if (CalciteSystemProperty.DEBUG.value()) {
      Util.debugCode(System.out, source);
    }

    JaninoCompiler compiler = new JaninoCompiler();
    compiler.getArgs().setDestdir(CLASS_DIR.getAbsolutePath());
    compiler.getArgs().setSource(source, classFileName);
    compiler.getArgs().setFullClassName(className);
    compiler.compile();
    try {
      @SuppressWarnings("unchecked")
      final Class<ArrayBindable> clazz =
          (Class<ArrayBindable>) Class.forName(className);
      final Constructor<ArrayBindable> constructor = clazz.getConstructor();
      return constructor.newInstance();
    } catch (ClassNotFoundException | InstantiationException
        | IllegalAccessException | NoSuchMethodException
        | InvocationTargetException e) {
      throw new RuntimeException(e);
    }
  }

```



## 版本总结
1. 展望Flink各版本及新特性：https://blog.csdn.net/qq_36470898/article/details/130451864 
```


```



### calcite 
```


```


## 流计算组件
1. fluss：https://github.com/alibaba/fluss
2. paimon：https://github.com/apache/paimon
3. Flash向量化引擎：
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

