## Velox
### 理解时间
```
2025年11月04号启动

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


完整理解Velox项目
如果只是在搜索引擎 搜 Velox是远远不够的
Velox + 架构图

Velox + 概念关键词

Velox + 问题排查

Velox + 面试汇总

Velox + 极客挑战赛

Velox + 论坛会议

Velox + 论文

Velox + 前沿分享

Velox + 场景应用

Velox + Velox大佬名字

Velox + 公司项目
等等才能完全熟悉Velox


```

## 参考资料
1. 源码：https://github.dev/facebookincubator/velox/tree/main/velox
2. https://github.dev/apache/arrow

## 纵向拆解 - 内部数据结构
1. 主要是指 velox在读写和计算是操作的数据结构对象
2. RowVectorPtr 是核心数据结构，所有外部文件比如parquet orc arrow都需要先转化成 RowVectorPtr，再能融合到velox向量化生态中
```cpp

using RowVectorPtr = std::shared_ptr<RowVector>;
using ArrayVectorPtr = std::shared_ptr<ArrayVector>;
using MapVectorPtr = std::shared_ptr<MapVector>;




```


## 纵向拆解 - 执行计划
### 示例参考 - 构建plan
```cpp

TEST_F(AggregationTest, groupingSetsEmptyInput) {
  auto data = makeRowVector(
      {"c1", "c2"},
      {makeFlatVector<int64_t>({0, 1, 2, 3, 4}),
       makeFlatVector<std::string>({"", "x", "xx", "xxx", "xxxx"})});

  createDuckDbTable({data});

  auto plan =
      PlanBuilder()
          .values({data})
          .filter("c1 < 0")
          .groupId({"c1"}, {{"c1"}, {}}, {"c2"})
          .singleAggregation({"c1", "group_id"}, {"count(c2) as count_c2"}, {})
          .project({"count_c2"})
          .planNode();

  assertQuery(
      plan,
      "SELECT count(c2) as count_c2 FROM tmp WHERE c1 < 0 GROUP BY GROUPING SETS ((c1), ())");

  plan =
      PlanBuilder()
          .values({data})
          .filter("c1 < 0")
          .groupId({"c1"}, {{"c1"}, {}}, {"c2"})
          .partialAggregation({"c1", "group_id"}, {"count(c2) as count_c2"}, {})
          .finalAggregation()
          .project({"count_c2"})
          .planNode();

  assertQuery(
      plan,
      "SELECT count(c2) as count_c2 FROM tmp WHERE c1 < 0 GROUP BY GROUPING SETS ((c1), ())");

  plan =
      PlanBuilder()
          .values({data})
          .filter("c1 < 0")
          .groupId({"c1"}, {{"c1"}, {}}, {"c2"})
          .partialAggregation({"c1", "group_id"}, {"count(c2) as count_c2"}, {})
          .intermediateAggregation()
          .finalAggregation()
          .project({"count_c2"})
          .planNode();

  assertQuery(
      plan,
      "SELECT count(c2) as count_c2 FROM tmp WHERE c1 < 0 GROUP BY GROUPING SETS ((c1), ())");

  // Distinct aggregations with GROUPING SETS.
  plan = PlanBuilder()
             .values({data})
             .filter("c1 < 0")
             .groupId({"c1"}, {{"c1"}, {}}, {})
             .partialAggregation({"c1", "group_id"}, {}, {})
             .finalAggregation()
             .project({"c1"})
             .planNode();

  assertQuery(
      plan,
      "SELECT c1 FROM tmp WHERE c1 < 0 GROUP BY GROUPING SETS ((c1), ())");

  plan =
      PlanBuilder()
          .values({data})
          .filter("c1 < 0")
          .groupId({"c1"}, {{}, {}}, {"c2"})
          .partialAggregation({"c1", "group_id"}, {"count(c2) as count_c2"}, {})
          .intermediateAggregation()
          .finalAggregation()
          .project({"count_c2"})
          .planNode();

  assertQuery(plan, makeRowVector({makeFlatVector<int64_t>({0, 0})}));

  // Distinct aggregations over empty input with global GROUPING SETs.
  plan = PlanBuilder()
             .values({data})
             .filter("c1 < 0")
             .groupId({"c1"}, {{}, {}}, {})
             .singleAggregation({"c1", "group_id"}, {}, {})
             .planNode();

  assertQuery(
      plan,
      makeRowVector({
          makeAllNullFlatVector<int64_t>(2),
          makeFlatVector<int64_t>({0, 1}),
      }));

  // Aggregations over distinct inputs over empty input with global grouping
  // sets.
  plan = PlanBuilder()
             .values({data})
             .filter("c1 < 0")
             .groupId({"c1"}, {{}, {}}, {"c2"})
             .singleAggregation(
                 {"c1", "group_id"}, {"count(distinct c2)", "min(distinct c2)"})
             .planNode();

  assertQuery(
      plan,
      makeRowVector({
          makeAllNullFlatVector<int64_t>(2),
          makeFlatVector<int64_t>({0, 1}),
          makeFlatVector<int64_t>({0, 0}),
          makeAllNullFlatVector<std::string>(2),
      }));

  // Aggregations over sorted inputs over empty input with global grouping sets.
  plan =
      PlanBuilder()
          .values({data})
          .filter("c1 < 0")
          .groupId({"c1"}, {{}, {}}, {"c2"})
          .singleAggregation({"c1", "group_id"}, {"array_agg(c2 order by c2)"})
          .planNode();

  assertQuery(
      plan,
      makeRowVector({
          makeAllNullFlatVector<int64_t>(2),
          makeFlatVector<int64_t>({0, 1}),
          makeAllNullArrayVector(2, VARCHAR()),
      }));
}

```

### PlanBuilder拆解 - 构建 datasource
```cpp

PlanBuilder& PlanBuilder::values(
    const std::vector<RowVectorPtr>& values,
    bool parallelizable,
    size_t repeatTimes) {
  VELOX_CHECK_NULL(planNode_, "Values must be the source node");
  auto valuesCopy = values;
  planNode_ = std::make_shared<core::ValuesNode>(
      nextPlanNodeId(), std::move(valuesCopy), parallelizable, repeatTimes);
  VELOX_CHECK(!planNode_->supportsBarrier());
  return *this;
}

```

### PlanBuilder拆解 - 构建 filter
```cpp
PlanBuilder& PlanBuilder::filter(const std::string& filter) {
  VELOX_CHECK_NOT_NULL(planNode_, "Filter cannot be the source node");
  auto expr = parseExpr(filter, planNode_->outputType(), options_, pool_);
  planNode_ =
      std::make_shared<core::FilterNode>(nextPlanNodeId(), expr, planNode_);
  VELOX_CHECK(planNode_->supportsBarrier());
  return *this;
}

```
### PlanBuilder拆解 - 构建 project
```cpp
PlanBuilder& PlanBuilder::project(const std::vector<std::string>& projections) {
  VELOX_CHECK_NOT_NULL(planNode_, "Project cannot be the source node");
  std::vector<std::shared_ptr<const core::IExpr>> expressions;
  expressions.reserve(projections.size());
  for (auto i = 0; i < projections.size(); ++i) {
    expressions.push_back(parse::parseExpr(projections[i], options_));
  }
  return projectExpressions(expressions);
}

```

## 纵向拆解 - PlanNode && PlanFragment && Operator
### PlanNode
```cpp


```
### ProjectNode
```cpp


```
### FilterNode
```cpp


```


### 
```cpp


```

### 
```cpp


```

## 纵向拆解 - DuckDbSql
### 执行sql
1. DuckDbQueryRunner
```cpp
void assertResults(
    const std::vector<RowVectorPtr>& results,
    const RowTypePtr& resultType,
    const std::string& duckDbSql,
    DuckDbQueryRunner& duckDbQueryRunner) {
  MaterializedRowMultiset actualRows;
  MaterializedRowMultiset expectedRows;
  for (const auto& vector : results) {
    auto rows = materialize(vector);
    std::copy(
        rows.begin(), rows.end(), std::inserter(actualRows, actualRows.end()));
  }

  if (!duckDbSql.empty()) {
    expectedRows = duckDbQueryRunner.execute(duckDbSql, resultType);
  }
  const auto& actualType =
      (results.size() == 0) ? nullptr : results.at(0)->type();
  assertEqualResults(
      expectedRows,
      resultType,
      actualRows,
      actualType,
      kDuckDbTimestampWarning + "\nDuckDB query: " + duckDbSql);
}

```
### 
```cpp


```
### 
```cpp


```
### 
```cpp


```


## 纵向拆解 - filter 算子


## 纵向拆解 - join 算子


## 纵向拆解 - reader 算子


## 纵向拆解 - writer 算子


## 纵向拆解 - TaskCursor && Task
```cpp
std::unique_ptr<TaskCursor> TaskCursor::create(const CursorParameters& params) {
  if (params.serialExecution) {
    return std::make_unique<SingleThreadedTaskCursor>(params);
  }
  return std::make_unique<MultiThreadedTaskCursor>(params);
}

```

## 应用拆解 - arrow数据格式集成到velox
1. https://engineering.fb.com/2024/02/20/developer-tools/velox-apache-arrow-15-composable-data-management/
### read arrow
```cpp


std::vector<RowVectorPtr> SparkQueryRunner::readArrowData(
    const std::string& data) {
  auto buffer = std::make_shared<arrow::Buffer>(data);
  auto bufferReader = std::make_shared<arrow::io::BufferReader>(buffer);
  arrow::Result<std::shared_ptr<arrow::ipc::RecordBatchReader>> result =
      arrow::ipc::RecordBatchStreamReader::Open(bufferReader);
  VELOX_CHECK(
      result.ok(),
      "Failed to open RecordBatchReader: {}.",
      result.status().ToString());

  std::shared_ptr<arrow::ipc::RecordBatchReader> reader = result.ValueUnsafe();
  std::shared_ptr<arrow::Schema> schema = reader->schema();

  ArrowSchema arrowSchema;
  auto status = arrow::ExportSchema(*schema, &arrowSchema);
  VELOX_CHECK(status.ok(), "Failed to export schema: {}.", status.ToString());

  arrow::Result<std::shared_ptr<arrow::RecordBatch>> batchResult;
  std::vector<RowVectorPtr> results;
  while ((batchResult = reader->Next()).ok() && batchResult.ValueUnsafe()) {
    std::shared_ptr<arrow::RecordBatch> batch = batchResult.ValueUnsafe();
    ArrowArray arrowArray;
    status = ExportRecordBatch(*batch, &arrowArray);
    VELOX_CHECK(status.ok(), "Failed to export array: {}.", status.ToString());
    auto rv = std::dynamic_pointer_cast<RowVector>(
        importFromArrowAsOwner(arrowSchema, arrowArray, pool()));
    auto copy =
        BaseVector::create<RowVector>(rv->type(), rv->size(), copyPool_.get());
    copy->copy(rv.get(), 0, 0, rv->size());
    results.push_back(copy);
  }
  VELOX_CHECK(
      batchResult.ok(),
      "Failed to read batch: {}.",
      batchResult.status().ToString());
  return results;
}

```

### arrow to velox
1. recordbatch 结构转 ArrowArray 转 velox std::vector<RowVectorPtr>
```cpp


PYBIND11_MODULE(arrow, m) {
  using namespace facebook;

  py::module::import("pyvelox.vector");

  arrow::py::import_pyarrow();
  velox::py::initializeVeloxMemory();

  static auto rootPool = velox::memory::memoryManager()->addRootPool();
  static auto leafPool = rootPool->addLeafChild("py_velox_arrow_pool");

  /// Converts a pyarrow.Array into a pyvelox.vector.Vector using Velox's arrow
  /// bridge.
  m.def(
      "to_velox",
      [](py::object& batchObject) {
        ArrowSchema schema;
        ArrowArray data;
        std::shared_ptr<arrow::Array> array;
        std::shared_ptr<arrow::RecordBatch> batch;

        if (arrow::py::is_array(batchObject.ptr())) {
          array = *arrow::py::unwrap_array(batchObject.ptr());
          auto statusType = arrow::ExportType(*array->type(), &schema);
          auto statusArray = arrow::ExportArray(*array, &data);

          if (!statusArray.ok() || !statusType.ok()) {
            throw std::runtime_error("Unable to convert Arrow Array to C ABI.");
          }
        } else if (arrow::py::is_batch(batchObject.ptr())) {
          batch = *arrow::py::unwrap_batch(batchObject.ptr());
          auto statusType = arrow::ExportSchema(*batch->schema(), &schema);
          auto statusArray = arrow::ExportRecordBatch(*batch, &data);

          if (!statusArray.ok() || !statusType.ok()) {
            throw std::runtime_error(
                "Unable to convert Arrow RecorBatch to C ABI.");
          }
        } else {
          throw std::runtime_error("Unknown input Arrow structure.");
        }
        return velox::py::PyVector{
            velox::importFromArrowAsViewer(schema, data, leafPool.get()),
            leafPool};
      },
      R"pbdoc(
Converts an arrow object to a velox vector.

:param vector: Input arrow object.

:examples:

.. doctest::

    >>> array = pyarrow.array([1, 2, 3, 4, 5, 6])
    >>> vector = to_velox(array)

)pbdoc");


VectorPtr importFromArrowAsViewer(
    const ArrowSchema& arrowSchema,
    const ArrowArray& arrowArray,
    memory::MemoryPool* pool) {
  return importFromArrowImpl(
      const_cast<ArrowSchema&>(arrowSchema),
      const_cast<ArrowArray&>(arrowArray),
      pool,
      true);
}

VectorPtr importFromArrowAsOwner(
    ArrowSchema& arrowSchema,
    ArrowArray& arrowArray,
    memory::MemoryPool* pool) {
  return importFromArrowImpl(arrowSchema, arrowArray, pool, false);
}

```

### velox project
```cpp


```

### velox filter
```cpp


```

### velox to ArrowArray to recordbatch bytes
1. exportToArrow
2. ImportRecordBatch
```cpp

 m.def(
      "to_arrow",
      [](velox::py::PyVector& vector) {
        ArrowSchema schema;
        ArrowArray data;

        velox::exportToArrow(vector.vector(), schema);
        velox::exportToArrow(vector.vector(), data, leafPool.get());

        auto arrowType = *arrow::ImportType(&schema);
        auto arrowArray = *arrow::ImportArray(&data, arrowType);
        return py::reinterpret_steal<py::object>(
            arrow::py::wrap_array(arrowArray));
      },
      R"pbdoc(
Converts a velox vector to an arrow object.

:param vector: Input arrow object.

:examples:

.. doctest::

    >>> import pyvelox.legacy as pv
    >>> vec = pv.from_list([1, 2, 3, 4, 5])
    >>> arrow = to_arrow(vec)

)pbdoc");
}


ARROW_EXPORT
Result<std::shared_ptr<RecordBatch>> ImportRecordBatch(struct ArrowArray* array,
                                                       std::shared_ptr<Schema> schema);

/// \brief Import C++ record batch and its schema from the C data interface.
///
/// The type represented by the ArrowSchema struct must be a struct type array.
/// The ArrowArray struct has its contents moved (as per the C data interface
/// specification) to a private object held alive by the resulting record batch.
/// The ArrowSchema struct is released, even if this function fails.
///
/// \param[in,out] array C data interface struct holding the record batch data
/// \param[in,out] schema C data interface struct holding the record batch schema
/// \return Imported record batch object
ARROW_EXPORT
Result<std::shared_ptr<RecordBatch>> ImportRecordBatch(struct ArrowArray* array,
             



```

## 应用拆解 - Benchmark
1. veloxy自带性能测试工具

### format_datetime UDF测试
```cpp
#include <folly/Benchmark.h>  // 引入Folly库的Benchmark模块，用于性能测试
#include <folly/init/Init.h>  // 引入Folly库的初始化模块
#include "velox/benchmarks/ExpressionBenchmarkBuilder.h"  // 引入Velox库的表达式基准测试构建器
#include "velox/functions/prestosql/registration/RegistrationFunctions.h"  // 引入Velox库的Presto SQL函数注册模块

using namespace facebook;  // 使用facebook命名空间
using namespace facebook::velox;  // 使用facebook::velox命名空间

int main(int argc, char** argv) {
  folly::Init init(&argc, &argv);  // 初始化Folly库
  memory::MemoryManager::initialize(memory::MemoryManager::Options{});  // 初始化内存管理器
  functions::prestosql::registerDateTimeFunctions("");  // 注册日期时间函数

  ExpressionBenchmarkBuilder benchmarkBuilder;  // 创建表达式基准测试构建器对象
  VectorFuzzer::Options options;  // 创建向量模糊器选项对象
  options.vectorSize = 1000;  // 设置向量大小为1000
  auto* pool = benchmarkBuilder.pool();  // 获取内存池
  VectorFuzzer fuzzer(options, pool);  // 创建向量模糊器对象
  auto vectorMaker = benchmarkBuilder.vectorMaker();  // 获取向量创建器

  benchmarkBuilder
      .addBenchmarkSet(
          "Benchmark format_datetime",  // 添加基准测试集，名称为"Benchmark format_datetime"
          vectorMaker.rowVector({fuzzer.fuzz(TIMESTAMP())}))  // 创建一个行向量，包含模糊化的时间戳数据
      .addExpression("", "format_datetime(c0, 'yyyy-MM-dd HH:mm:ss.SSS')")  // 添加表达式，格式化时间戳
      .disableTesting();  // 禁用测试

  benchmarkBuilder.registerBenchmarks();  // 注册基准测试
  folly::runBenchmarks();  // 运行基准测试
  return 0;  // 返回0，表示程序成功执行
}

```

## 应用拆解 - VectorTestBase 代码分析 懂这个测试工具，相当于对velox了解一半了
1. VectorTestBase 是测试工具类，几乎涵盖了velox所有用法，看懂这个测试工具，相当于对velox了解一半了
当然可以，以下是对`VectorTestBase`类代码结构的中文说明：

---

### `VectorTestBase`类代码结构说明

`VectorTestBase`类是一个用于测试和操作向量数据结构的基类。它提供了一系列工具函数，帮助用户创建和操作不同类型的向量。以下是该类的详细结构说明：

#### 构造函数和析构函数

- **构造函数**：`VectorTestBase()`，默认构造函数。
- **析构函数**：`~VectorTestBase()`，用于清理资源。

#### 静态方法

- **`makeRowType`**：用于创建行类型的静态方法。
- **`nullEvery`**：返回一个函数，用于每隔n个元素设置空值。

#### 成员方法

- **`setNulls`**：设置向量中的空值。
- **`compareValues`**：比较两个值的辅助函数，支持不同类型的比较。
- **`makeRowVector`**：提供多种重载方法，用于创建行向量。
- **`createVectors`**：创建多个行向量，支持不同的参数组合。
- **`split`**：将输入向量分割成多个向量。
- **`asArray`**：将元素包装成数组向量。
- **`makeFlatVector`**：创建平面向量，支持多种数据类型和输入格式。
- **`makeNullableFlatVector`**：创建可空平面向量。
- **`makeArrayVector`**：创建数组向量，支持从嵌套数据结构或JSON创建。
- **`makeNullableArrayVector`**：创建可空数组向量。
- **`makeMapVector`**：创建映射向量，支持从嵌套数据结构或JSON创建。
- **`makeNullableMapVector`**：创建可空映射向量。
- **`makeConstant`**：创建常量向量，支持不同的数据类型。
- **`makeIndices`**：创建索引缓冲区，支持多种索引生成方式。
- **`makeNulls`**：创建空值缓冲区。
- **`wrapInDictionary`**：将向量包装成字典形式。
- **`flatten`**：扁平化向量。
- **`createMapOfArraysVector`**：创建包含数组的映射向量。
- **`pool`**：获取内存池。
- **`makeLazyFlatVector`**：创建延迟加载的平面向量。
- **`wrapInLazyDictionary`**：包装延迟加载的字典。

#### 成员变量

- **`rootPool_`**：根内存池，用于管理内存分配。
- **`pool_`**：叶子内存池，继承自根内存池。
- **`vectorMaker_`**：`VectorMaker`对象，用于创建向量。
- **`executor_`**：执行器，用于管理线程池。
- **`spillExecutor_`**：溢出执行器，用于处理溢出任务。

---

以上是`VectorTestBase`类的代码结构说明。该类通过提供丰富的工具函数，简化了向量数据结构的创建和操作过程，非常适合用于测试和验证向量相关的功能。

### rootPool_和pool_的作用
```cpp

rootPool_：这是一个根内存池，通常用于管理整个应用程序的内存分配。它是内存管理的顶层对象，负责分配较大的内存块。
pool_：这是一个叶子内存池，继承自rootPool_。它用于具体的内存分配任务，通常在一个特定的上下文中使用，例如在一个测试用例中。


简单初始化
class VectorTestBase {
 protected:
  // 构造函数
  VectorTestBase() {
    // 初始化根内存池
    rootPool_ = memory::memoryManager()->addRootPool();
    // 初始化叶子内存池
    pool_ = rootPool_->addLeafChild("leaf");
    // 初始化VectorMaker对象
    vectorMaker_ = velox::test::VectorMaker(pool_.get());
  }

  // 析构函数
  ~VectorTestBase() {
    // 释放叶子内存池
    pool_.reset();
    // 释放根内存池
    rootPool_.reset();
  }

  // 成员变量
  std::shared_ptr<memory::MemoryPool> rootPool_;
  std::shared_ptr<memory::MemoryPool> pool_;
  velox::test::VectorMaker vectorMaker_;
};

// 使用示例
void exampleUsage() {
  VectorTestBase testBase;

  // 创建一个平面向量
  auto flatVector = testBase.vectorMaker_.flatVector<int64_t>({1, 2, 3, 4, 5});

  // 使用flatVector进行测试...

  // 测试结束，内存会在VectorTestBase析构时自动释放
}
```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```

## 应用拆解 - 
```cpp


```



