## Arrow
### 理解时间
```
2024年08月07号启动

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


完整理解Arrow项目
如果只是在搜索引擎 搜 Arrow是远远不够的
Arrow + 架构图

Arrow + 概念关键词

Arrow + 问题排查

Arrow + 面试汇总

Arrow + 极客挑战赛

Arrow + 论坛会议

Arrow + 论文

Arrow + 前沿分享

Arrow + 场景应用

Arrow + Arrow大佬名字

Arrow + 公司项目
等等才能完全熟悉Arrow


```

## 参考资料
1. java编译：https://arrow.apache.org/docs/dev/developers/java/building.html#building-arrow-java
2. 官方文档：https://arrow.apache.org/docs/dev/format/Intro.html
   1. 内存管理：https://arrow.apache.org/docs/java/memory.html
3. 竞品分析
   1. 全票通过｜多语言序列化框架 Fury 正式加入 Apache 孵化器 - Shawn的文章 - 知乎 https://zhuanlan.zhihu.com/p/677061734



## 深度思考
1. 直接看Arrow工具属性特别强的项目，反而并不能真正理解设计理念，结合应用场景，才能明白为什么怎么设计，从而能更快推导出整个代码设计架构
2. 零拷贝序列化协议
3. Buffer零拷贝
4. 堆外内存读写
5. 无需反序列化的行存协议

## 地图

### 功能地图
1.  common in-memory data processing algorithms
2.  many languages are available
3.  Zero-copy shared memory and RPC-based data movement
    1. Sharing Arrow data
    2. Serialization and Interprocess Communication (IPC)
    3. The Arrow C data interface
4.  In-memory analytics and query processing

### 概念地图
1. Array or Vector: a sequence of values with known length all having the same type. These terms are used interchangeably in different Arrow implementations, but we use “array” in this document.
2. Slot: a single logical value in an array of some particular data type
3. Buffer or Contiguous memory region: a sequential virtual address space with a given length. Any byte can be reached via a single pointer offset less than the region’s length.
4. Physical Layout: The underlying memory layout for an array without taking into account any value semantics. For example, a 32-bit signed integer array and 32-bit floating point array have the same layout.
5. Data type: An application-facing semantic value type that is implemented using some physical layout. For example, Decimal128 values are stored as 16 bytes in a fixed-size binary layout. A timestamp may be stored as 64-bit fixed-size layout.
6. Primitive type: a data type having no child types. This includes such types as fixed bit-width, variable-size binary, and null types.
7. Nested type: a data type whose full structure depends on one or more other child types. Two fully-specified nested types are equal if and only if their child types are equal. For example, List<U> is distinct from List<V> iff U and V are different types.
8. Parent and child arrays: names to express relationships between physical value arrays in a nested type structure. For example, a List<T>-type parent array has a T-type array as its child (see more on lists below).
9. Parametric type: a type which requires additional parameters for full determination of its semantics. For example, all nested types are parametric by construction. A timestamp is also parametric as it needs a unit (such as microseconds) and a timezone.

### 代码地图



## 编译顺序
```
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Build Order:
[INFO] 
[INFO] Arrow Bill of Materials                                            [pom]
[INFO] Apache Arrow Java Root POM                                         [pom]
[INFO] Arrow Format                                                       [jar]
[INFO] Arrow Memory                                                       [pom]
[INFO] Arrow Memory - Core                                                [jar]
[INFO] Arrow Memory - Unsafe                                              [jar]
[INFO] Arrow Memory - Netty Buffer                                        [jar]
[INFO] Arrow Memory - Netty                                               [jar]
[INFO] Arrow Vectors                                                      [jar]
[INFO] Arrow Compression                                                  [jar]
[INFO] Arrow Tools                                                        [jar]
[INFO] Arrow JDBC Adapter                                                 [jar]
[INFO] Arrow Flight                                                       [pom]
[INFO] Arrow Flight Core                                                  [jar]
[INFO] Arrow Flight SQL                                                   [jar]
[INFO] Arrow Flight SQL JDBC Driver Core                                  [jar]
[INFO] Arrow Flight SQL JDBC Driver                                       [jar]
[INFO] Arrow Flight Integration Tests                                     [jar]
[INFO] Arrow AVRO Adapter                                                 [jar]
[INFO] Arrow Algorithms                                                   [jar]
[INFO] Arrow Performance Benchmarks                                       [jar]
[INFO] 
[INFO] ---------------------< org.apache.arrow:arrow-bom >---------------------
[INFO] Building Arrow Bill of Materials 18.0.0-SNAPSHOT                  [1/21]
[INFO] --------------------------------[ pom ]---------------------------------


```

## 源码
## 横向拆解


## 纵向拆解

## 纵向拆解 - 列式存储
1. Arrow Columnar Format：https://arrow.apache.org/docs/format/Columnar.html





## 纵向拆解 - 函数
### 实现一个 过滤函数

#### 调用

```cpp
      arrow::compute::Filter(arrow_table, arrow_filter, *arrow_options);

Result<Datum> Filter(const Datum& values, const Datum& filter,
                     const FilterOptions& options, ExecContext* ctx) {
  // Invoke metafunction which deals with Datum kinds other than just Array,
  // ChunkedArray.
  return CallFunction("filter", {values, filter}, &options, ctx);
}

```


#### 注册

```cpp

void RegisterVectorSelection(FunctionRegistry* registry) {
  // Filter kernels
  std::vector<SelectionKernelData> filter_kernels;
  PopulateFilterKernels(&filter_kernels);

  VectorKernel filter_base;
  filter_base.init = FilterState::Init;
  RegisterSelectionFunction("array_filter", array_filter_doc, filter_base,
                            std::move(filter_kernels), GetDefaultFilterOptions(),
                            registry);

  DCHECK_OK(registry->AddFunction(MakeFilterMetaFunction()));

  // Take kernels
  std::vector<SelectionKernelData> take_kernels;
  PopulateTakeKernels(&take_kernels);

  VectorKernel take_base;
  take_base.init = TakeState::Init;
  take_base.can_execute_chunkwise = false;
  RegisterSelectionFunction("array_take", array_take_doc, take_base,
                            std::move(take_kernels), GetDefaultTakeOptions(), registry);

  DCHECK_OK(registry->AddFunction(MakeTakeMetaFunction()));

  // DropNull kernel
  DCHECK_OK(registry->AddFunction(std::make_shared<DropNullMetaFunction>()));

  DCHECK_OK(registry->AddFunction(
      MakeIndicesNonZeroFunction("indices_nonzero", indices_nonzero_doc)));
}

```

#### 实现
1. 每一种数据类型都要实现一遍
```cpp
void PopulateFilterKernels(std::vector<SelectionKernelData>* out) {
  auto plain_filter = InputType(Type::BOOL);
  auto ree_filter = InputType(match::RunEndEncoded(Type::BOOL));

  *out = {
      // * x Boolean
      {InputType(match::Primitive()), plain_filter, PrimitiveFilterExec},
      {InputType(match::BinaryLike()), plain_filter, BinaryFilterExec},
      {InputType(match::LargeBinaryLike()), plain_filter, BinaryFilterExec},
      {InputType(null()), plain_filter, NullFilterExec},
      {InputType(Type::FIXED_SIZE_BINARY), plain_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL32), plain_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL64), plain_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL128), plain_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL256), plain_filter, PrimitiveFilterExec},
      {InputType(Type::DICTIONARY), plain_filter, DictionaryFilterExec},
      {InputType(Type::EXTENSION), plain_filter, ExtensionFilterExec},
      {InputType(Type::LIST), plain_filter, ListFilterExec},
      {InputType(Type::LARGE_LIST), plain_filter, LargeListFilterExec},
      {InputType(Type::LIST_VIEW), plain_filter, ListViewFilterExec},
      {InputType(Type::LARGE_LIST_VIEW), plain_filter, LargeListViewFilterExec},
      {InputType(Type::FIXED_SIZE_LIST), plain_filter, FSLFilterExec},
      {InputType(Type::DENSE_UNION), plain_filter, DenseUnionFilterExec},
      {InputType(Type::SPARSE_UNION), plain_filter, SparseUnionFilterExec},
      {InputType(Type::STRUCT), plain_filter, StructFilterExec},
      {InputType(Type::MAP), plain_filter, MapFilterExec},

      // * x REE(Boolean)
      {InputType(match::Primitive()), ree_filter, PrimitiveFilterExec},
      {InputType(match::BinaryLike()), ree_filter, BinaryFilterExec},
      {InputType(match::LargeBinaryLike()), ree_filter, BinaryFilterExec},
      {InputType(null()), ree_filter, NullFilterExec},
      {InputType(Type::FIXED_SIZE_BINARY), ree_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL32), ree_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL64), ree_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL128), ree_filter, PrimitiveFilterExec},
      {InputType(Type::DECIMAL256), ree_filter, PrimitiveFilterExec},
      {InputType(Type::DICTIONARY), ree_filter, DictionaryFilterExec},
      {InputType(Type::EXTENSION), ree_filter, ExtensionFilterExec},
      {InputType(Type::LIST), ree_filter, ListFilterExec},
      {InputType(Type::LARGE_LIST), ree_filter, LargeListFilterExec},
      {InputType(Type::LIST_VIEW), ree_filter, ListViewFilterExec},
      {InputType(Type::LARGE_LIST_VIEW), ree_filter, LargeListViewFilterExec},
      {InputType(Type::FIXED_SIZE_LIST), ree_filter, FSLFilterExec},
      {InputType(Type::DENSE_UNION), ree_filter, DenseUnionFilterExec},
      {InputType(Type::SPARSE_UNION), ree_filter, SparseUnionFilterExec},
      {InputType(Type::STRUCT), ree_filter, StructFilterExec},
      {InputType(Type::MAP), ree_filter, MapFilterExec},
  };
}

```


## 纵向拆解 - dataset 数据集
### 执行filter算子

```cpp


```




## 纵向拆解 - 表达式计算


### 构建表达式 Expression
```cpp
namespace ds = arrow::dataset;
namespace fs = arrow::fs;
namespace cp = arrow::compute;

示例
b < 4

cp::less(cp::field_ref("b"), cp::literal(4)) 返回 Expression


函数拆解 expression.h 和 expression.cc
构建 字段b
Expression field_ref(FieldRef ref) {
  return Expression(Expression::Parameter{std::move(ref), ValueDescr{}, {-1}});
}


构建常量4
Expression literal(Datum lit) { return Expression(std::move(lit)); }


构建 最终表达式
Expression less(Expression lhs, Expression rhs) {
  return call("less", {std::move(lhs), std::move(rhs)});
}


```


### 执行 标量表达式
```cpp
执行函数
ExecuteScalarExpression
NaiveExecuteScalarExpression

void ExpectExecute(Expression expr, Datum in, Datum* actual_out = NULLPTR) {
  std::shared_ptr<Schema> schm;
  if (in.is_value()) {
    ASSERT_OK_AND_ASSIGN(expr, expr.Bind(in.descr()));
    schm = schema(in.type()->fields());
  } else {
    ASSERT_OK_AND_ASSIGN(expr, expr.Bind(*in.schema()));
    schm = in.schema();
  }

  ASSERT_OK_AND_ASSIGN(Datum actual, ExecuteScalarExpression(expr, *schm, in));

  ASSERT_OK_AND_ASSIGN(Datum expected, NaiveExecuteScalarExpression(expr, in));

  AssertDatumsEqual(actual, expected, /*verbose=*/true);

  if (actual_out) {
    *actual_out = actual;
  }
}


调用标量表达式

TEST(Expression, ExecuteCall) {
  ExpectExecute(call("add", {field_ref("a"), literal(3.5)}),
                ArrayFromJSON(struct_({field("a", float64())}), R"([
    {"a": 6.125},
    {"a": 0.0},
    {"a": -1}
  ])"));

  ExpectExecute(
      call("add", {field_ref("a"), call("subtract", {literal(3.5), field_ref("b")})}),
      ArrayFromJSON(struct_({field("a", float64()), field("b", float64())}), R"([
    {"a": 6.125, "b": 3.375},
    {"a": 0.0,   "b": 1},
    {"a": -1,    "b": 4.75}
  ])"));

  ExpectExecute(call("strptime", {field_ref("a")},
                     compute::StrptimeOptions("%m/%d/%Y", TimeUnit::MICRO, true)),
                ArrayFromJSON(struct_({field("a", utf8())}), R"([
    {"a": "5/1/2020"},
    {"a": null},
    {"a": "12/11/1900"}
  ])"));

  ExpectExecute(project({call("add", {field_ref("a"), literal(3.5)})}, {"a + 3.5"}),
                ArrayFromJSON(struct_({field("a", float64())}), R"([
    {"a": 6.125},
    {"a": 0.0},
    {"a": -1}
  ])"));

  ExpectExecute(
      call("add", {field_ref(FieldRef("a", "a")), field_ref(FieldRef("a", "b"))}),
      ArrayFromJSON(struct_({field("a", struct_({
                                            field("a", float64()),
                                            field("b", float64()),
                                        }))}),
                    R"([
    {"a": {"a": 6.125, "b": 3.375}},
    {"a": {"a": 0.0,   "b": 1}},
    {"a": {"a": -1,    "b": 4.75}}
  ])"));
}


```
### 执行 filter表达式
```cpp
TEST(Expression, SimplifyThenExecute) {
  auto filter =
      or_({equal(field_ref("f32"), literal(0)),
           call("is_in", {field_ref("i64")},
                compute::SetLookupOptions{ArrayFromJSON(int32(), "[1,2,3]"), true})});

  ASSERT_OK_AND_ASSIGN(filter, filter.Bind(*kBoringSchema));
  auto guarantee = greater(field_ref("f32"), literal(0.0));

  ASSERT_OK_AND_ASSIGN(auto simplified, SimplifyWithGuarantee(filter, guarantee));

  auto input = RecordBatchFromJSON(kBoringSchema, R"([
      {"i64": 0, "f32": 0.1},
      {"i64": 0, "f32": 0.3},
      {"i64": 1, "f32": 0.5},
      {"i64": 2, "f32": 0.1},
      {"i64": 0, "f32": 0.1},
      {"i64": 0, "f32": 0.4},
      {"i64": 0, "f32": 1.0}
  ])");

  Datum evaluated, simplified_evaluated;
  ExpectExecute(filter, input, &evaluated);
  ExpectExecute(simplified, input, &simplified_evaluated);
  AssertDatumsEqual(evaluated, simplified_evaluated, /*verbose=*/true);
}



TEST(Expression, Filter) {
  auto ExpectFilter = [](Expression filter, std::string batch_json) {
    ASSERT_OK_AND_ASSIGN(auto s, kBoringSchema->AddField(0, field("in", boolean())));
    auto batch = RecordBatchFromJSON(s, batch_json);
    auto expected_mask = batch->column(0);

    ASSERT_OK_AND_ASSIGN(filter, filter.Bind(*kBoringSchema));
    ASSERT_OK_AND_ASSIGN(Datum mask,
                         ExecuteScalarExpression(filter, *kBoringSchema, batch));

    AssertDatumsEqual(expected_mask, mask);
  };

  ExpectFilter(equal(field_ref("i32"), literal(0)), R"([
      {"i32": 0, "f32": -0.1, "in": 1},
      {"i32": 0, "f32":  0.3, "in": 1},
      {"i32": 1, "f32":  0.2, "in": 0},
      {"i32": 2, "f32": -0.1, "in": 0},
      {"i32": 0, "f32":  0.1, "in": 1},
      {"i32": 0, "f32": null, "in": 1},
      {"i32": 0, "f32":  1.0, "in": 1}
  ])");

  ExpectFilter(
      greater(call("multiply", {field_ref("f32"), field_ref("f64")}), literal(0)), R"([
      {"f64":  0.3, "f32":  0.1, "in": 1},
      {"f64": -0.1, "f32":  0.3, "in": 0},
      {"f64":  0.1, "f32":  0.2, "in": 1},
      {"f64":  0.0, "f32": -0.1, "in": 0},
      {"f64":  1.0, "f32":  0.1, "in": 1},
      {"f64": -2.0, "f32": null, "in": null},
      {"f64":  3.0, "f32":  1.0, "in": 1}
  ])");
}
```


### 执行 project 表达式
```cpp
TEST(Projection, AugmentWithNull) {
  // NB: input contains *no columns* except i32
  auto input = ArrayFromJSON(struct_({kBoringSchema->GetFieldByName("i32")}),
                             R"([{"i32": 0}, {"i32": 1}, {"i32": 2}])");

  auto ExpectProject = [&](Expression proj, Datum expected) {
    ASSERT_OK_AND_ASSIGN(proj, proj.Bind(*kBoringSchema));
    ASSERT_OK_AND_ASSIGN(auto actual,
                         ExecuteScalarExpression(proj, *kBoringSchema, input));
    AssertDatumsEqual(Datum(expected), actual);
  };

  ExpectProject(project({field_ref("f64"), field_ref("i32")},
                        {"projected double", "projected int"}),
                // "projected double" is materialized as a column of nulls
                ArrayFromJSON(struct_({field("projected double", float64()),
                                       field("projected int", int32())}),
                              R"([
                                  [null, 0],
                                  [null, 1],
                                  [null, 2]
                              ])"));

  ExpectProject(
      project({field_ref("f64")}, {"projected double"}),
      // NB: only a scalar was projected, this is *not* automatically broadcast
      // to an array. "projected double" is materialized as a null scalar
      Datum(*StructScalar::Make({MakeNullScalar(float64())}, {"projected double"})));
}

TEST(Projection, AugmentWithKnownValues) {
  auto input = ArrayFromJSON(struct_({kBoringSchema->GetFieldByName("i32")}),
                             R"([{"i32": 0}, {"i32": 1}, {"i32": 2}])");

  auto ExpectSimplifyAndProject = [&](Expression proj, Datum expected,
                                      Expression guarantee) {
    ASSERT_OK_AND_ASSIGN(proj, proj.Bind(*kBoringSchema));
    ASSERT_OK_AND_ASSIGN(proj, SimplifyWithGuarantee(proj, guarantee));
    ASSERT_OK_AND_ASSIGN(auto actual,
                         ExecuteScalarExpression(proj, *kBoringSchema, input));
    AssertDatumsEqual(Datum(expected), actual);
  };

  ExpectSimplifyAndProject(
      project({field_ref("str"), field_ref("f64"), field_ref("i64"), field_ref("i32")},
              {"str", "f64", "i64", "i32"}),
      ArrayFromJSON(struct_({
                        field("str", utf8()),
                        field("f64", float64()),
                        field("i64", int64()),
                        field("i32", int32()),
                    }),
                    // str is explicitly null
                    // f64 is explicitly 3.5
                    // i64 is not specified in the guarantee and implicitly null
                    // i32 is present in the input and passed through
                    R"([
                        {"str": null, "f64": 3.5, "i64": null, "i32": 0},
                        {"str": null, "f64": 3.5, "i64": null, "i32": 1},
                        {"str": null, "f64": 3.5, "i64": null, "i32": 2}
                    ])"),
      and_({
          equal(field_ref("f64"), literal(3.5)),
          is_null(field_ref("str")),
      }));
}


```

### 构建 project 算子
```cpp

Status ScannerBuilder::Project(std::vector<std::string> columns) {
  ARROW_ASSIGN_OR_RAISE(
      auto projection,
      ProjectionDescr::FromNames(std::move(columns), *scan_options_->dataset_schema));
  SetProjection(scan_options_.get(), std::move(projection));
  return Status::OK();
}

void SetProjection(ScanOptions* options, ProjectionDescr projection) {
  options->projection = std::move(projection.expression);
  options->projected_schema = std::move(projection.schema);
}




Result<ProjectionDescr> ProjectionDescr::FromStructExpression(
    const compute::Expression& projection, const Schema& dataset_schema) {
  ARROW_ASSIGN_OR_RAISE(compute::Expression bound_expression,
                        projection.Bind(dataset_schema));

  if (bound_expression.type()->id() != Type::STRUCT) {
    return Status::Invalid("Projection ", projection.ToString(),
                           " cannot yield record batches");
  }
  std::shared_ptr<Schema> projection_schema =
      ::arrow::schema(checked_cast<const StructType&>(*bound_expression.type()).fields(),
                      dataset_schema.metadata());

  return ProjectionDescr{std::move(bound_expression), std::move(projection_schema)};
}

Result<ProjectionDescr> ProjectionDescr::FromExpressions(
    std::vector<compute::Expression> exprs, std::vector<std::string> names,
    const Schema& dataset_schema) {
  compute::MakeStructOptions project_options{std::move(names)};

  for (size_t i = 0; i < exprs.size(); ++i) {
    if (auto ref = exprs[i].field_ref()) {
      // set metadata and nullability for plain field references
      ARROW_ASSIGN_OR_RAISE(auto field, ref->GetOne(dataset_schema));
      project_options.field_nullability[i] = field->nullable();
      project_options.field_metadata[i] = field->metadata();
    }
  }

  return ProjectionDescr::FromStructExpression(
      call("make_struct", std::move(exprs), std::move(project_options)), dataset_schema);
}

字段select
Result<ProjectionDescr> ProjectionDescr::FromNames(std::vector<std::string> names,
                                                   const Schema& dataset_schema) {
  std::vector<compute::Expression> exprs(names.size());
  for (size_t i = 0; i < exprs.size(); ++i) {
    exprs[i] = compute::field_ref(names[i]);
  }
  auto fields = dataset_schema.fields();
  for (const auto& aug_field : kAugmentedFields) {
    fields.push_back(aug_field);
  }
  return ProjectionDescr::FromExpressions(std::move(exprs), std::move(names),
                                          Schema(fields, dataset_schema.metadata()));
}

```



### 实现一个 greater_equal 函数
#### 业务调用
```cpp



业务调用
Expression greater_equal(Expression lhs, Expression rhs) {
  return call("greater_equal", {std::move(lhs), std::move(rhs)});
}





```


#### 注册
```cpp

ARROW_EXPORT Expression project(std::vector<Expression> values,
                                std::vector<std::string> names);

ARROW_EXPORT Expression equal(Expression lhs, Expression rhs);

ARROW_EXPORT Expression not_equal(Expression lhs, Expression rhs);

ARROW_EXPORT Expression less(Expression lhs, Expression rhs);

ARROW_EXPORT Expression less_equal(Expression lhs, Expression rhs);

ARROW_EXPORT Expression greater(Expression lhs, Expression rhs);

ARROW_EXPORT Expression greater_equal(Expression lhs, Expression rhs);

ARROW_EXPORT Expression is_null(Expression lhs, bool nan_is_null = false);

ARROW_EXPORT Expression is_valid(Expression lhs);

ARROW_EXPORT Expression and_(Expression lhs, Expression rhs);
ARROW_EXPORT Expression and_(const std::vector<Expression>&);
ARROW_EXPORT Expression or_(Expression lhs, Expression rhs);
ARROW_EXPORT Expression or_(const std::vector<Expression>&);
ARROW_EXPORT Expression not_(Expression operand);





  enum type {
    NA = 0,
    EQUAL = 1,
    LESS = 2,
    GREATER = 4,
    NOT_EQUAL = LESS | GREATER,
    LESS_EQUAL = LESS | EQUAL,
    GREATER_EQUAL = GREATER | EQUAL,
  };

  static const type* Get(const std::string& function) {
    static std::unordered_map<std::string, type> map{
        {"equal", EQUAL},     {"not_equal", NOT_EQUAL},
        {"less", LESS},       {"less_equal", LESS_EQUAL},
        {"greater", GREATER}, {"greater_equal", GREATER_EQUAL},
    };

    auto it = map.find(function);
    return it != map.end() ? &it->second : nullptr;
  }


```

#### 实现
1. 所有类似算子具体实现位置：apache/arrow/cpp/src/arrow/compute/kernels
```cpp
struct GreaterEqual {
  template <typename T, typename Arg0, typename Arg1>
  static constexpr T Call(KernelContext*, const Arg0& left, const Arg1& right, Status*) {
    static_assert(std::is_same<T, bool>::value && std::is_same<Arg0, Arg1>::value, "");
    return left >= right;
  }
};


template <typename CType>
using Comparator = bool(CType, CType);

template <typename CType>
Comparator<CType>* GetComparator(CompareOperator op) {
  static Comparator<CType>* cmp[] = {
      // EQUAL
      [](CType l, CType r) { return l == r; },
      // NOT_EQUAL
      [](CType l, CType r) { return l != r; },
      // GREATER
      [](CType l, CType r) { return l > r; },
      // GREATER_EQUAL
      [](CType l, CType r) { return l >= r; },
      // LESS
      [](CType l, CType r) { return l < r; },
      // LESS_EQUAL
      [](CType l, CType r) { return l <= r; },
  };
  return cmp[op];
}

```

### 实现一个统计指标 - 用compute库
1. 运用field 和 compute

#### 构建字段
```cpp

TEST(TestParquetStatistics, NullMax) {
  auto field = ::arrow::field("x", float32());
  ASSERT_OK_AND_ASSIGN(std::string dir_string,
                       arrow::internal::GetEnvVar("PARQUET_TEST_DATA"));
  auto reader =
      parquet::ParquetFileReader::OpenFile(dir_string + "/nan_in_stats.parquet");
  auto statistics = reader->RowGroup(0)->metadata()->ColumnChunk(0)->statistics();
  auto stat_expression =
      ParquetFileFragment::EvaluateStatisticsAsExpression(*field, *statistics);
  EXPECT_EQ(stat_expression->ToString(), "(x >= 1)");
}

std::optional<compute::Expression> ParquetFileFragment::EvaluateStatisticsAsExpression(
    const Field& field, const parquet::Statistics& statistics) {
  auto field_name = field.name();
  return EvaluateStatisticsAsExpression(field, FieldRef(std::move(field_name)),
                                        statistics);
}


```

#### 统计实现
```cpp


std::optional<compute::Expression> ParquetFileFragment::EvaluateStatisticsAsExpression(
    const Field& field, const FieldRef& field_ref,
    const parquet::Statistics& statistics) {
  auto field_expr = compute::field_ref(field_ref);

  bool may_have_null = !statistics.HasNullCount() || statistics.null_count() > 0;
  // Optimize for corner case where all values are nulls
  if (statistics.num_values() == 0) {
    // If there are no non-null values, column `field_ref` in the fragment
    // might be empty or all values are nulls. In this case, we also return
    // a null expression.
    return is_null(std::move(field_expr));
  }

  std::shared_ptr<Scalar> min, max;
  if (!StatisticsAsScalars(statistics, &min, &max).ok()) {
    return std::nullopt;
  }

  auto maybe_min = Cast(min, field.type());
  auto maybe_max = Cast(max, field.type());
  if (maybe_min.ok() && maybe_max.ok()) {
    min = maybe_min.MoveValueUnsafe().scalar();
    max = maybe_max.MoveValueUnsafe().scalar();

    if (min->Equals(*max)) {
      auto single_value = compute::equal(field_expr, compute::literal(std::move(min)));

      if (!may_have_null) {
        return single_value;
      }
      return compute::or_(std::move(single_value), is_null(std::move(field_expr)));
    }

    auto lower_bound = compute::greater_equal(field_expr, compute::literal(min));
    auto upper_bound = compute::less_equal(field_expr, compute::literal(max));
    compute::Expression in_range;

    // Since the minimum & maximum values are NaN, useful statistics
    // cannot be extracted for checking the presence of a value within
    // range
    if (IsNan(*min) && IsNan(*max)) {
      return std::nullopt;
    }

    // If either minimum or maximum is NaN, it should be ignored for the
    // range computation
    if (IsNan(*min)) {
      in_range = std::move(upper_bound);
    } else if (IsNan(*max)) {
      in_range = std::move(lower_bound);
    } else {
      in_range = compute::and_(std::move(lower_bound), std::move(upper_bound));
    }
    if (may_have_null) {
      return compute::or_(std::move(in_range), compute::is_null(std::move(field_expr)));
    }
    return in_range;
  }
  return std::nullopt;
}


```

## 纵向拆解 - acero计划图
1. https://juejin.cn/post/7423022386880282633
2. 示例代码：cpp/examples/arrow/acero_register_example.cc
3. 流图计算：https://arrow.apache.org/docs/8.0/cpp/streaming_execution.html
4. 代码示例：https://arrow.apache.org/docs/8.0/cpp/streaming_execution.html#summary

### 定义plan  - 过滤逻辑
```cpp
auto filter_expr = cp::call("invert",
    {cp::call("is_in", {cp::field_ref("homeworld")},
                         cp::SetLookupOptions{
                             *exclusions})});

auto plan = ac::Declaration::Sequence(
    {{"record_batch_reader_source",  
      ac::RecordBatchReaderSourceNodeOptions{
          std::move(rdr)}},
     {"filter", ac::FilterNodeOptions{
           std::move(filter_expr)}},
     {"aggregate", ac::AggregateNodeOptions({{
          {"hash_list", nullptr, "name", "name_list"},
          {"hash_list", nullptr, "species", "species_list"},
          {"hash_mean", nullptr, "height", "avg_height"}}},
     {"homeworld"})}});

作者：数据智能老司机
链接：https://juejin.cn/post/7423022386880282633
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```



## 纵向拆解 - 基于 RecordBatch 做表达式计算
1. 处理数据整体思路
   1. rb 转 eb
   2. 构建 
      1. SourceNodeOptions
      2. ProjectNodeOptions
      3. FilterNodeOptions 
      4. SinkNodeOptions
   3. eb 转 table执行plan
### ExecBatch 和 RecordBatch 区别
```cpp
execbatch 基于 recordbatch 初始化构造函数


初始化 RecordBatch
arrow::Result<std::shared_ptr<arrow::RecordBatch>> GetSampleRecordBatch(
    const arrow::ArrayVector array_vector, const arrow::FieldVector& field_vector) {
  std::shared_ptr<arrow::RecordBatch> record_batch;
  ARROW_ASSIGN_OR_RAISE(auto struct_result,
                        arrow::StructArray::Make(array_vector, field_vector));
  return record_batch->FromStructArray(struct_result);
}


初始化 ExecBatch
cp::ExecBatch batch{*res_batch};


ExecBatch 结构体
struct ARROW_EXPORT ExecBatch {
  ExecBatch() = default;
  ExecBatch(std::vector<Datum> values, int64_t length)
      : values(std::move(values)), length(length) {}

  explicit ExecBatch(const RecordBatch& batch);



```

### 构建 Datum
```cpp
判断字段里的值是否存在，且是否符合预期
ExpectRefIs



TEST(Expression, ExecuteFieldRef) {
  auto ExpectRefIs = [](FieldRef ref, Datum in, Datum expected) {
    auto expr = field_ref(ref);

    ASSERT_OK_AND_ASSIGN(expr, expr.Bind(in.descr()));
    ASSERT_OK_AND_ASSIGN(Datum actual,
                         ExecuteScalarExpression(expr, Schema(in.type()->fields()), in));

    AssertDatumsEqual(actual, expected, /*verbose=*/true);
  };

  ExpectRefIs("a", ArrayFromJSON(struct_({field("a", float64())}), R"([
    {"a": 6.125},
    {"a": 0.0},
    {"a": -1}
  ])"),
              ArrayFromJSON(float64(), R"([6.125, 0.0, -1])"));

  ExpectRefIs("a",
              ArrayFromJSON(struct_({
                                field("a", float64()),
                                field("b", float64()),
                            }),
                            R"([
    {"a": 6.125, "b": 7.5},
    {"a": 0.0,   "b": 2.125},
    {"a": -1,    "b": 4.0}
  ])"),
              ArrayFromJSON(float64(), R"([6.125, 0.0, -1])"));

  ExpectRefIs("b",
              ArrayFromJSON(struct_({
                                field("a", float64()),
                                field("b", float64()),
                            }),
                            R"([
    {"a": 6.125, "b": 7.5},
    {"a": 0.0,   "b": 2.125},
    {"a": -1,    "b": 4.0}
  ])"),
              ArrayFromJSON(float64(), R"([7.5, 2.125, 4.0])"));

  ExpectRefIs(FieldRef(FieldPath({0, 0})),
              ArrayFromJSON(struct_({field("a", struct_({field("b", float64())}))}), R"([
    {"a": {"b": 6.125}},
    {"a": {"b": 0.0}},
    {"a": {"b": -1}}
  ])"),
              ArrayFromJSON(float64(), R"([6.125, 0.0, -1])"));

  ExpectRefIs(FieldRef("a", "b"),
              ArrayFromJSON(struct_({field("a", struct_({field("b", float64())}))}), R"([
    {"a": {"b": 6.125}},
    {"a": {"b": 0.0}},
    {"a": {"b": -1}}
  ])"),
              ArrayFromJSON(float64(), R"([6.125, 0.0, -1])"));

  ExpectRefIs(FieldRef("a", "b"),
              ArrayFromJSON(struct_({field("a", struct_({field("b", float64())}))}), R"([
    {"a": {"b": 6.125}},
    {"a": null},
    {"a": {"b": null}}
  ])"),
              ArrayFromJSON(float64(), R"([6.125, null, null])"));

  ExpectRefIs(
      FieldRef("a", "b"),
      ScalarFromJSON(struct_({field("a", struct_({field("b", float64())}))}), "[[64.0]]"),
      ScalarFromJSON(float64(), "64.0"));

  ExpectRefIs(
      FieldRef("a", "b"),
      ScalarFromJSON(struct_({field("a", struct_({field("b", float64())}))}), "[[null]]"),
      ScalarFromJSON(float64(), "null"));

  ExpectRefIs(
      FieldRef("a", "b"),
      ScalarFromJSON(struct_({field("a", struct_({field("b", float64())}))}), "[null]"),
      ScalarFromJSON(float64(), "null"));
}


Datum 本质结构

/// \class Datum
/// \brief Variant type for various Arrow C++ data structures
struct ARROW_EXPORT Datum {
  enum Kind { NONE, SCALAR, ARRAY, CHUNKED_ARRAY, RECORD_BATCH, TABLE };

  struct Empty {};

  // Datums variants may have a length. This special value indicate that the
  // current variant does not have a length.
  static constexpr int64_t kUnknownLength = -1;

  util::Variant<Empty, std::shared_ptr<Scalar>, std::shared_ptr<ArrayData>,
                std::shared_ptr<ChunkedArray>, std::shared_ptr<RecordBatch>,
                std::shared_ptr<Table>>
      value;

  /// \brief Empty datum, to be populated elsewhere
  Datum() = default;

  Datum(const Datum& other) = default;
  Datum& operator=(const Datum& other) = default;
  Datum(Datum&& other) = default;
  Datum& operator=(Datum&& other) = default;

  Datum(std::shared_ptr<Scalar> value)  // NOLINT implicit conversion
      : value(std::move(value)) {}

  Datum(std::shared_ptr<ArrayData> value)  // NOLINT implicit conversion
      : value(std::move(value)) {}

  Datum(ArrayData arg)  // NOLINT implicit conversion
      : value(std::make_shared<ArrayData>(std::move(arg))) {}

  Datum(const Array& value);                   // NOLINT implicit conversion
  Datum(const std::shared_ptr<Array>& value);  // NOLINT implicit conversion
  Datum(std::shared_ptr<ChunkedArray> value);  // NOLINT implicit conversion
  Datum(std::shared_ptr<RecordBatch> value);   // NOLINT implicit conversion
  Datum(std::shared_ptr<Table> value);         // NOLINT implicit conversion

  // Explicit constructors from const-refs. Can be expensive, prefer the
  // shared_ptr constructors
  explicit Datum(const ChunkedArray& value);
  explicit Datum(const RecordBatch& value);
  explicit Datum(const Table& value);

```

### 构建 RecordBatch
```cpp


 auto GetField = [](std::string name) { return kBoringSchema->GetFieldByName(name); };

  constexpr int64_t kNumRows = 3;
  auto i32 = ArrayFromJSON(int32(), "[1, 2, 3]");
  auto f32 = ArrayFromJSON(float32(), "[1.5, 2.25, 3.125]");

  // empty
  Expect(RecordBatchFromJSON(kBoringSchema, "[]"));

  // subset
  Expect(RecordBatch::Make(schema({GetField("i32"), GetField("f32")}), kNumRows,
                           {i32, f32}));

  // flipped subset
  Expect(RecordBatch::Make(schema({GetField("f32"), GetField("i32")}), kNumRows,
                           {f32, i32}));

  auto duplicated_names =
      RecordBatch::Make(schema({GetField("i32"), GetField("i32")}), kNumRows, {i32, i32});

```

### 构建 RecordBatch 含 array map复杂数据类型
```cpp




```


### 构建 ExecBatch
```cpp
初始化 ExecBatch
cp::ExecBatch batch{*res_batch};


ExecBatch 结构体
struct ARROW_EXPORT ExecBatch {
  ExecBatch() = default;
  ExecBatch(std::vector<Datum> values, int64_t length)
      : values(std::move(values)), length(length) {}

  explicit ExecBatch(const RecordBatch& batch);


```


### 构建 ExecBatch 含 array map和嵌套的复杂数据类型
```cpp
BatchesWithSchema MakeBasicBatches() {
  BatchesWithSchema out;
  out.batches = {
      ExecBatchFromJSON({int32(), boolean()}, "[[null, true], [4, false]]"),
      ExecBatchFromJSON({int32(), boolean()}, "[[5, null], [6, false], [7, false]]")};
  out.schema = schema({field("i32", int32()), field("bool", boolean())});
  return out;
}

BatchesWithSchema MakeNestedBatches() {
  auto ty = struct_({field("i32", int32()), field("bool", boolean())});
  BatchesWithSchema out;
  out.batches = {
      ExecBatchFromJSON(
          {ty},
          R"([[{"i32": null, "bool": true}], [{"i32": 4, "bool": false}], [null]])"),
      ExecBatchFromJSON(
          {ty},
          R"([[{"i32": 5, "bool": null}], [{"i32": 6, "bool": false}], [{"i32": 7, "bool": false}]])")};
  out.schema = schema({field("struct", ty)});
  return out;
}

BatchesWithSchema MakeRandomBatches(const std::shared_ptr<Schema>& schema,
                                    int num_batches, int batch_size) {
  BatchesWithSchema out;

  random::RandomArrayGenerator rng(42);
  out.batches.resize(num_batches);

  for (int i = 0; i < num_batches; ++i) {
    out.batches[i] = ExecBatch(*rng.BatchOf(schema->fields(), batch_size));
    // add a tag scalar to ensure the batches are unique
    out.batches[i].values.emplace_back(i);
  }

  out.schema = schema;
  return out;
}





ExecBatchFromJSON(
              {ValueDescr::Scalar(boolean()), ValueDescr::Scalar(boolean()),
               ValueDescr::Scalar(int64()), ValueDescr::Scalar(float64()),
               ValueDescr::Scalar(int64()), ValueDescr::Scalar(float64()),
               ValueDescr::Scalar(int64()), ValueDescr::Array(float64()),
               ValueDescr::Scalar(float64())},
              R"([[false, true, 6, 5.5, 26250, 0.7637626158259734, 33, 5.0, 0.5833333333333334]])"),
      


  out.batches = {ExecBatchFromJSON({int32(), utf8()}, R"([
                   [12, "alfa"],
                   [7,  "beta"],
                   [3,  "alfa"]
                 ])"),
                 ExecBatchFromJSON({int32(), utf8()}, R"([
                   [-2, "alfa"],
                   [-1, "gama"],
                   [3,  "alfa"]
                 ])"),
                 ExecBatchFromJSON({int32(), utf8()}, R"([
                   [5,  "gama"],
                   [3,  "beta"],
                   [-8, "alfa"]
                 ])")};

```

### 定义 schema

```cpp

  std::shared_ptr<Schema> schema = schema({field("i32", int32()), field("bool", boolean())});

```
### 异步生成数据 ExecBatch
```cpp

  AsyncGenerator<util::optional<ExecBatch>> gen;



struct BatchesWithSchema {
  std::vector<ExecBatch> batches;
  std::shared_ptr<Schema> schema;

  AsyncGenerator<util::optional<ExecBatch>> gen(bool parallel, bool slow) const {
    auto opt_batches = ::arrow::internal::MapVector(
        [](ExecBatch batch) { return util::make_optional(std::move(batch)); }, batches);

    AsyncGenerator<util::optional<ExecBatch>> gen;

    if (parallel) {
      // emulate batches completing initial decode-after-scan on a cpu thread
      gen = MakeBackgroundGenerator(MakeVectorIterator(std::move(opt_batches)),
                                    ::arrow::internal::GetCpuThreadPool())
                .ValueOrDie();

      // ensure that callbacks are not executed immediately on a background thread
      gen =
          MakeTransferredGenerator(std::move(gen), ::arrow::internal::GetCpuThreadPool());
    } else {
      gen = MakeVectorGenerator(std::move(opt_batches));
    }

    if (slow) {
      gen =
          MakeMappedGenerator(std::move(gen), [](const util::optional<ExecBatch>& batch) {
            SleepABit();
            return batch;
          });
    }

    return gen;
  }
};


模版设计
template <typename T>
AsyncGenerator<T> MakeVectorGenerator(std::vector<T> vec) {
  struct State {
    explicit State(std::vector<T> vec_) : vec(std::move(vec_)), vec_idx(0) {}

    std::vector<T> vec;
    std::atomic<std::size_t> vec_idx;
  };

  auto state = std::make_shared<State>(std::move(vec));
  return [state]() {
    auto idx = state->vec_idx.fetch_add(1);
    if (idx >= state->vec.size()) {
      // Eagerly return memory
      state->vec.clear();
      return AsyncGeneratorEnd<T>();
    }
    return Future<T>::MakeFinished(state->vec[idx]);
  };
}


```

### 定义 SourceNodeOptions 处理execBatch
```cpp
  auto source_node_options = cp::SourceNodeOptions{basic_data.schema, basic_data.gen()};


  ARROW_ASSIGN_OR_RAISE(cp::ExecNode * source,
                        cp::MakeExecNode("source", plan.get(), {}, source_node_options));
  ARROW_RETURN_NOT_OK(
      cp::MakeExecNode("sink", plan.get(), {source}, cp::SinkNodeOptions{&sink_gen}));



SourceNodeOptions(std::shared_ptr<Schema> output_schema,
                    std::function<Future<util::optional<ExecBatch>>()> generator)
      : output_schema(std::move(output_schema)), generator(std::move(generator)) {}
```


### 定义 SinkNodeOptions 处理execBatch
```cpp

  explicit SinkNodeOptions(std::function<Future<util::optional<ExecBatch>>()>* generator,
                           BackpressureOptions backpressure = {},
                           BackpressureMonitor** backpressure_monitor = NULLPTR)


  BackpressureOptions(uint32_t resume_if_below, uint32_t pause_if_above)
      : resume_if_below(resume_if_below), pause_if_above(pause_if_above) {}
```

### 定义 ProjectNodeOptions 处理execBatch
```cpp
  explicit ProjectNodeOptions(std::vector<Expression> expressions,
                              std::vector<std::string> names = {}, bool async_mode = true)



```


### 定义 FilterNodeOptions 处理execBatch
```cpp


  explicit FilterNodeOptions(Expression filter_expression, bool async_mode = true)
      : filter_expression(std::move(filter_expression)), async_mode(async_mode) {}

```





### 执行 plan
```cpp

  return ExecutePlanAndCollectAsTable(exec_context, plan, basic_data.schema, sink_gen);


arrow::Status ExecutePlanAndCollectAsTable(
    cp::ExecContext& exec_context, std::shared_ptr<cp::ExecPlan> plan,
    std::shared_ptr<arrow::Schema> schema,
    arrow::AsyncGenerator<arrow::util::optional<cp::ExecBatch>> sink_gen) {
  // translate sink_gen (async) to sink_reader (sync)
  std::shared_ptr<arrow::RecordBatchReader> sink_reader =
      cp::MakeGeneratorReader(schema, std::move(sink_gen), exec_context.memory_pool());

  // validate the ExecPlan
  ARROW_RETURN_NOT_OK(plan->Validate());
  std::cout << "ExecPlan created : " << plan->ToString() << std::endl;
  // start the ExecPlan
  ARROW_RETURN_NOT_OK(plan->StartProducing());

  // collect sink_reader into a Table
  std::shared_ptr<arrow::Table> response_table;

  ARROW_ASSIGN_OR_RAISE(response_table,
                        arrow::Table::FromRecordBatchReader(sink_reader.get()));

  std::cout << "Results : " << response_table->ToString() << std::endl;

  // stop producing
  plan->StopProducing();
  // plan mark finished
  auto future = plan->finished();
  return future.status();
}
```



### 执行 source-filter-sink plan
```cpp
TEST(ExecPlanExecution, SourceFilterSink) {
  auto basic_data = MakeBasicBatches();

  ASSERT_OK_AND_ASSIGN(auto plan, ExecPlan::Make());
  AsyncGenerator<util::optional<ExecBatch>> sink_gen;

  ASSERT_OK(Declaration::Sequence(
                {
                    {"source", SourceNodeOptions{basic_data.schema,
                                                 basic_data.gen(/*parallel=*/false,
                                                                /*slow=*/false)}},
                    {"filter", FilterNodeOptions{equal(field_ref("i32"), literal(6))}},
                    {"sink", SinkNodeOptions{&sink_gen}},
                })
                .AddToPlan(plan.get()));

  ASSERT_THAT(StartAndCollect(plan.get(), sink_gen),
              Finishes(ResultWith(UnorderedElementsAreArray(
                  {ExecBatchFromJSON({int32(), boolean()}, "[]"),
                   ExecBatchFromJSON({int32(), boolean()}, "[[6, false]]")}))));
}


```




```cpp


```
## 纵向拆解 - plan 执行计划
### 执行 source -filter -sink
```cpp

TEST(ExecPlanExecution, SourceFilterSink) {
  auto basic_data = MakeBasicBatches();

  ASSERT_OK_AND_ASSIGN(auto plan, ExecPlan::Make());
  AsyncGenerator<util::optional<ExecBatch>> sink_gen;

  ASSERT_OK(Declaration::Sequence(
                {
                    {"source", SourceNodeOptions{basic_data.schema,
                                                 basic_data.gen(/*parallel=*/false,
                                                                /*slow=*/false)}},
                    {"filter", FilterNodeOptions{equal(field_ref("i32"), literal(6))}},
                    {"sink", SinkNodeOptions{&sink_gen}},
                })
                .AddToPlan(plan.get()));

  ASSERT_THAT(StartAndCollect(plan.get(), sink_gen),
              Finishes(ResultWith(UnorderedElementsAreArray(
                  {ExecBatchFromJSON({int32(), boolean()}, "[]"),
                   ExecBatchFromJSON({int32(), boolean()}, "[[6, false]]")}))));
}

```


### 执行 source - project -sink
```cpp
EST(ExecPlanExecution, SourceProjectSink) {
  auto basic_data = MakeBasicBatches();

  ASSERT_OK_AND_ASSIGN(auto plan, ExecPlan::Make());
  AsyncGenerator<util::optional<ExecBatch>> sink_gen;

  ASSERT_OK(Declaration::Sequence(
                {
                    {"source", SourceNodeOptions{basic_data.schema,
                                                 basic_data.gen(/*parallel=*/false,
                                                                /*slow=*/false)}},
                    {"project",
                     ProjectNodeOptions{{
                                            not_(field_ref("bool")),
                                            call("add", {field_ref("i32"), literal(1)}),
                                        },
                                        {"!bool", "i32 + 1"}}},
                    {"sink", SinkNodeOptions{&sink_gen}},
                })
                .AddToPlan(plan.get()));

  ASSERT_THAT(StartAndCollect(plan.get(), sink_gen),
              Finishes(ResultWith(UnorderedElementsAreArray(
                  {ExecBatchFromJSON({boolean(), int32()}, "[[false, null], [true, 5]]"),
                   ExecBatchFromJSON({boolean(), int32()},
                                     "[[null, 6], [true, 7], [true, 8]]")}))));
}

```


## 纵向拆解 - Source算子

### recordbatch source算子
```cpp
TEST(ExecPlan, RecordBatchReaderSourceSink) {
  ASSERT_OK_AND_ASSIGN(auto plan, ExecPlan::Make());
  AsyncGenerator<util::optional<ExecBatch>> sink_gen;

  // set up a RecordBatchReader:
  auto input = MakeBasicBatches();

  RecordBatchVector batches;
  for (const ExecBatch& exec_batch : input.batches) {
    ASSERT_OK_AND_ASSIGN(auto batch, exec_batch.ToRecordBatch(input.schema));
    batches.push_back(batch);
  }

  ASSERT_OK_AND_ASSIGN(auto table, Table::FromRecordBatches(batches));
  std::shared_ptr<RecordBatchReader> reader = std::make_shared<TableBatchReader>(*table);

  // Map the RecordBatchReader to a SourceNode
  ASSERT_OK_AND_ASSIGN(
      auto batch_gen,
      MakeReaderGenerator(std::move(reader), arrow::io::internal::GetIOThreadPool()));

  ASSERT_OK(
      Declaration::Sequence({
                                {"source", SourceNodeOptions{table->schema(), batch_gen}},
                                {"sink", SinkNodeOptions{&sink_gen}},
                            })
          .AddToPlan(plan.get()));

  ASSERT_THAT(StartAndCollect(plan.get(), sink_gen),
              Finishes(ResultWith(UnorderedElementsAreArray(input.batches))));
}

```

## 纵向拆解 - Sink算子

### 自定义 TableSinkNodeConsumer
1. Consume 消费数据
2. Finish 转成Table表
3. Table表的指针可以是来自外部传递
```cpp

/**
 * @brief This node is an extension on ConsumingSinkNode
 * to facilitate to get the output from an execution plan
 * as a table. We define a custom SinkNodeConsumer to
 * enable this functionality.
 */

struct TableSinkNodeConsumer : public SinkNodeConsumer {
 public:
  TableSinkNodeConsumer(std::shared_ptr<Table>* out, MemoryPool* pool)
      : out_(out), pool_(pool) {}

  Status Init(const std::shared_ptr<Schema>& schema,
              BackpressureControl* backpressure_control) override {
    // If the user is collecting into a table then backpressure is meaningless
    ARROW_UNUSED(backpressure_control);
    schema_ = schema;
    return Status::OK();
  }

  Status Consume(ExecBatch batch) override {
    std::lock_guard<std::mutex> guard(consume_mutex_);
    ARROW_ASSIGN_OR_RAISE(auto rb, batch.ToRecordBatch(schema_, pool_));
    batches_.push_back(rb);
    return Status::OK();
  }

  Future<> Finish() override {
    ARROW_ASSIGN_OR_RAISE(*out_, Table::FromRecordBatches(batches_));
    return Status::OK();
  }

 private:
  std::shared_ptr<Table>* out_;
  MemoryPool* pool_;
  std::shared_ptr<Schema> schema_;
  std::vector<std::shared_ptr<RecordBatch>> batches_;
  std::mutex consume_mutex_;
};

```

### 自定义 multi sink 算子
```cpp



```


## 纵向拆解 - 第三方工具

### ExecBatchFromJSON & RecordBatchFromJSON & ArrayFromJSON 区别
1. 

### ExecBatchFromJSON
```cpp

  input.batches = {
      ExecBatchFromJSON({ValueDescr::Scalar(int32()), int64()},
                        "[[1, 1], [1, 1], [1, 2], [1, 3]]"),
      ExecBatchFromJSON({ValueDescr::Scalar(int32()), int64()},
                        "[[null, 1], [null, 1], [null, 2], [null, 3]]"),
      ExecBatchFromJSON({int32(), int64()}, "[[2, 1], [3, 2], [4, 3]]"),
  };

```

### RecordBatchFromJSON
```cpp

  auto input = RecordBatchFromJSON(kBoringSchema, R"([
      {"i64": 0, "f32": 0.1},
      {"i64": 0, "f32": 0.3},
      {"i64": 1, "f32": 0.5},
      {"i64": 2, "f32": 0.1},
      {"i64": 0, "f32": 0.1},
      {"i64": 0, "f32": 0.4},
      {"i64": 0, "f32": 1.0}
  ])");

  auto batch = RecordBatchFromJSON(
      schema({field("argument", float64()), field("group_id", uint32())}), R"([
    [1.0,   1],
    [null,  1],
    [0.0,   2],
    [null,  3],
    [4.0,   0],
    [3.25,  1],
    [0.125, 2],
    [-0.25, 2],
    [0.75,  0],
    [null,  3]
  ])");



  auto batch = RecordBatchFromJSON(
      schema({field("argument", float64()), field("key", utf8())}), R"([
    [1.0, "alfa"],
    [2.0, "beta"],
    [3.0, "gama"]
  ])");



  auto schema = arrow::schema({
      field("a", null()),
      field("b", int32()),
      field("c", int32()),
      field("d", int32()),
      field("e", int32()),
      field("f", int32()),
      field("g", int32()),
      field("h", int32()),
      field("i", null()),
  });
  auto batch = RecordBatchFromJSON(schema, R"([
    {"a": null, "b": 5, "c": 0, "d": 0, "e": 1, "f": 2, "g": 3, "h": 4, "i": null},
    {"a": null, "b": 5, "c": 1, "d": 0, "e": 1, "f": 2, "g": 3, "h": 4, "i": null},
    {"a": null, "b": 2, "c": 2, "d": 0, "e": 1, "f": 2, "g": 3, "h": 4, "i": null},
    {"a": null, "b": 4, "c": 3, "d": 0, "e": 1, "f": 2, "g": 3, "h": 4, "i": null}
])");
```





### ArrayFromJSON
```cpp
从json数据结构解析转成 Array
比如
auto arr = ArrayFromJSON(int8(), "[]");
  auto i32 = ArrayFromJSON(int32(), "[1, 2, 3]");
  auto f32 = ArrayFromJSON(float32(), "[1.5, 2.25, 3.125]");


ExpectSimplifyAndProject(
      project({field_ref("str"), field_ref("f64"), field_ref("i64"), field_ref("i32")},
              {"str", "f64", "i64", "i32"}),
      ArrayFromJSON(struct_({
                        field("str", utf8()),
                        field("f64", float64()),
                        field("i64", int64()),
                        field("i32", int32()),
                    }),
                    // str is explicitly null
                    // f64 is explicitly 3.5
                    // i64 is not specified in the guarantee and implicitly null
                    // i32 is present in the input and passed through
                    R"([
                        {"str": null, "f64": 3.5, "i64": null, "i32": 0},
                        {"str": null, "f64": 3.5, "i64": null, "i32": 1},
                        {"str": null, "f64": 3.5, "i64": null, "i32": 2}
                    ])"),
      and_({
          equal(field_ref("f64"), literal(3.5)),
          is_null(field_ref("str")),
      }));


  ExpectProject(project({field_ref("f64"), field_ref("i32")},
                        {"projected double", "projected int"}),
                // "projected double" is materialized as a column of nulls
                ArrayFromJSON(struct_({field("projected double", float64()),
                                       field("projected int", int32())}),
                              R"([
                                  [null, 0],
                                  [null, 1],
                                  [null, 2]
                              ])"));



        ArrayFromJSON(struct_({
                          field("hash_stddev", float64()),
                          field("hash_variance", float64()),
                          field("hash_tdigest", fixed_size_list(float64(), 1)),
                          field("hash_stddev", float64()),
                          field("hash_variance", float64()),
                          field("hash_tdigest", fixed_size_list(float64(), 1)),
                          field("key", int64()),
                      }),
                      R"([
         [0.4714045, 0.222222, [1.0], 0.4714045, 0.222222, [1.0], 1],
         [1.0,       1.0,      [1.0], 1.0,       1.0,      [1.0], 2],
         [1.5,       2.25,     [1.0], 1.5,       2.25,     [1.0], 3]
       ])");


  ExpectExecute(call("add", {field_ref("a"), literal(3.5)}),
                ArrayFromJSON(struct_({field("a", float64())}), R"([
    {"a": 6.125},
    {"a": 0.0},
    {"a": -1}
  ])"));

  ExpectExecute(
      call("add", {field_ref("a"), call("subtract", {literal(3.5), field_ref("b")})}),
      ArrayFromJSON(struct_({field("a", float64()), field("b", float64())}), R"([
    {"a": 6.125, "b": 3.375},
    {"a": 0.0,   "b": 1},
    {"a": -1,    "b": 4.75}
  ])"));

  ExpectExecute(call("strptime", {field_ref("a")},
                     compute::StrptimeOptions("%m/%d/%Y", TimeUnit::MICRO, true)),
                ArrayFromJSON(struct_({field("a", utf8())}), R"([
    {"a": "5/1/2020"},
    {"a": null},
    {"a": "12/11/1900"}
  ])"));

  ExpectExecute(project({call("add", {field_ref("a"), literal(3.5)})}, {"a + 3.5"}),
                ArrayFromJSON(struct_({field("a", float64())}), R"([
    {"a": 6.125},
    {"a": 0.0},
    {"a": -1}
  ])"));

  ExpectExecute(
      call("add", {field_ref(FieldRef("a", "a")), field_ref(FieldRef("a", "b"))}),
      ArrayFromJSON(struct_({field("a", struct_({
                                            field("a", float64()),
                                            field("b", float64()),
                                        }))}),
                    R"([
    {"a": {"a": 6.125, "b": 3.375}},
    {"a": {"a": 0.0,   "b": 1}},
    {"a": {"a": -1,    "b": 4.75}}
  ])"));


    CheckDecimalToFloat(func, {ArrayFromJSON(float64(), "[1, 10, 1, 2, null]"),
                               ScalarFromJSON(ty, R"("10.00")")});
    CheckDecimalToFloat(func, {ArrayFromJSON(int64(), "[1, 10, 1, 2, null]"),
                               ScalarFromJSON(ty, R"("10.00")")});

源码实现参考
Result<std::shared_ptr<Array>> ArrayFromJSON(const std::shared_ptr<DataType>& type,
                                             util::string_view json_string) {
  std::shared_ptr<Converter> converter;
  RETURN_NOT_OK(GetConverter(type, &converter));

  rj::Document json_doc;
  json_doc.Parse<kParseFlags>(json_string.data(), json_string.length());
  if (json_doc.HasParseError()) {
    return Status::Invalid("JSON parse error at offset ", json_doc.GetErrorOffset(), ": ",
                           GetParseError_En(json_doc.GetParseError()));
  }

  // The JSON document should be an array, append it
  RETURN_NOT_OK(converter->AppendValues(json_doc));
  std::shared_ptr<Array> out;
  RETURN_NOT_OK(converter->Finish(&out));
  return out;
}
```

### ScalarFromJSON
```cpp
  
```

## 高阶拆解
## 高阶拆解 - Future & Result & AsyncGenerator 设计理念 和 运用
1. 参考C++高阶解决方案 异步设计
2. apache/arrow/cpp/src/arrow/util/async_generator.h
```cpp
  class ARROW_MUST_USE_TYPE Result : public util::EqualityComparable<Result<T>>




```


## 应用
### Flink & Arrow
1. 堆内内存
   1. Java 虚拟机具有一个堆(Heap)，堆是运行时数据区域，所有类实例和数组的内存均从此处分配。堆是在 Java 虚拟机启动时创建的
   2. 堆内内存 = 新生代+老年代+持久代
   3. 完全遵守JVM虚拟机的内存管理机制，采用垃圾回收器（GC）统一进行内存管理
   4. 在这个过程中会对JAVA应用程序的性能造成一定影响，还可能会产生Stop The World
2. 堆外内存
   1. 堆外内存就是把内存对象分配在Java虚拟机的堆以外的内存，这些内存直接受操作系统管理
   2. Java 虚拟机具有一个由所有线程共享的方法区，方法区属于非堆内存。它存储每个类结构，如运行时常数池、字段和方法数据，以及方法和构造方法的代码。它是在 Java 虚拟机启动时创建的。
   3. JIT 编译器需要内存来存储从 Java 虚拟机代码转换而来的本机代码，从而获得高性能
   4. 手动申请和释放：ByteBuffer类提供了一个接口allocateDirect（int capacity）
   5. 自动申请和释放：DirectByteBuffer。每个DirectByteBuffer对象在初始化时，都会创建一个对应的Cleaner对象，这个Cleaner对象会在合适的时候执行unsafe.freeMemory(address)，从而回收这块堆外内存。
   6. https://juejin.cn/post/7178845670109888570
3. 如何执行Flink Java代码
   1. 堆内内存 和 堆外内存 本质都是内存。
   2. Java在只是针对系统内存空间，做了一个标记划分。堆内要执行GC，堆外则不需要，业务自定义。类似提供内存插件，适应业务
   3. 所有内存都可以被代码文件执行，不管是c++ pyhon 还是 Java，最后会转成底层语言。
   4. 程序执行：解决读取内存的权限 + 解决读取内存的协议格式（这也是网络黑客攻克各种软件bug的思路）
   5. 因此跨语言的Arrow设计模式思想，就是提供一个统一的数据访问API，API包含各种逻辑
   6. 从这个角度来看，堆外内存或者Arrow就是共享内存的概念。不管什么语言的进程，只要能获取到访问内存的地址指针
   7. 如何读，如何写，如何计算，全靠业务自己代码保证。为了降低业务代码复杂度，Arrow提供尽可能通用的API，这样相当于替业务实现一部分共享内存操作的访问代码


### Java & C++ & Arrow
1. 不同语言，不同进程，同一机器节点，内存如何交换
2. 零拷贝处理
   1. 内存管理：https://arrow.apache.org/docs/java/memory.html
```
Why Arrow Uses Direct Memory 

Java版本arrow，使用Direct Memory，JNI可以直接访问和修改，做到零拷贝

The JVM can optimize I/O operations when using direct memory/direct buffers; it will attempt to avoid copying buffer contents to/from an intermediate buffer. This can speed up IPC in Arrow.

Since Arrow always uses direct memory, JNI modules can directly wrap native memory addresses instead of copying data. We use this in modules like the C Data Interface.

Conversely, on the C++ side of the JNI boundary, we can directly access the memory in ArrowBuf without copying data.


```

### GC & Arrow


### Protobuf & Arrow
1. 不同进程零拷贝处理
