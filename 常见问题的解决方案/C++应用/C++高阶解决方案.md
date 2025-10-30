## 异步编程




## 异步编程 - Arrow Future设计

### functional
这个代码片段定义了两个主要的组件：`Empty` 结构体和 `call_traits` 结构体，以及一个类型擦除的可调用对象 `FnOnce`。这些组件主要用于处理函数调用和类型推断。以下是对这些组件的详细分析：

#### 为什么这样设计
```
Empty 结构体
用途：Empty 结构体用于表示一个空的结果。这在某些情况下非常有用，比如当一个操作成功但没有返回值时，可以使用 Empty 来表示这种情况。
优势：通过使用 Empty，可以统一处理返回值和状态，简化代码逻辑。例如，函数可以返回 Result<Empty> 来表示成功或失败，而不需要返回具体的值。

call_traits 结构体
用途：call_traits 结构体用于检查和推断可调用对象（如 lambda 函数）的特性，包括参数类型、返回类型和是否重载。
优势：
类型推断：通过 call_traits，可以自动推断出可调用对象的参数和返回类型，这对于泛型编程非常有用。
重载检测：能够检测可调用对象是否重载，这在处理复杂的函数对象时非常有帮助。
灵活性：提供了一种机制来根据函数特性启用或禁用某些功能，使得代码更加灵活。


FnOnce 类型擦除的可调用对象
用途：FnOnce 提供了一种机制来存储和调用只能被调用一次的可调用对象（如 lambda 函数）。它通过类型擦除来实现这一点。
优势：
资源管理：FnOnce 在调用后立即销毁存储的可调用对象，释放任何关联的资源。这对于管理生命周期和避免资源泄漏非常有用。
简化接口：通过类型擦除，FnOnce 可以存储任何符合签名的可调用对象，而不需要关心其具体类型。这简化了接口设计。
性能优化：在某些情况下，调用一次后立即销毁可调用对象可以提高性能，因为减少了不必要的存储和管理开销。

```

####  `Empty` 结构体

- **功能**：`Empty` 是一个简单的结构体，用于表示一个空的结果。
- **方法**：`ToResult(Status s)` 方法用于将一个 `Status` 转换为 `Result<Empty>`。如果状态是 OK，则返回一个 `Empty` 对象，否则返回状态。

####  `call_traits` 结构体

- **功能**：`call_traits` 是一个辅助结构体，用于检查 lambda 和其他可调用对象的特性。
- **方法**：
  - `is_overloaded_impl`：检查一个函数是否是重载的。
  - `return_type_impl`：获取函数的返回类型。
  - `argument_type_impl`：获取函数的参数类型。
  - `argument_count_impl`：获取函数的参数数量。
- **类型定义**：
  - `is_overloaded`：判断一个可调用对象是否有多个可能的签名。
  - `enable_if_overloaded` 和 `disable_if_overloaded`：用于启用或禁用重载的可调用对象。
  - `argument_type`、`argument_count`、`return_type`：用于提取非重载可调用对象的参数类型、参数数量和返回类型。
  - `enable_if_return`：用于启用返回类型匹配的可调用对象。
  - `enable_if_empty` 和 `enable_if_not_empty`：用于启用或禁用 `Empty` 类型。

####  `FnOnce` 类模板

- **功能**：`FnOnce` 是一个类型擦除的可调用对象，只能被调用一次。它可以从任何匹配提供的调用签名的 lambda 构造。
- **构造函数**：
  - 默认构造函数：创建一个空的 `FnOnce` 对象。
  - 带参数构造函数：从一个 lambda 构造 `FnOnce`，并存储在 `impl_` 中。
- **运算符**：
  - `operator bool()`：检查 `FnOnce` 是否包含有效的可调用对象。
  - `operator()(A... a)`：调用存储的 lambda，并销毁它。
- **内部实现**：
  - `Impl` 结构体：定义了一个虚基类，用于实现类型擦除。
  - `FnImpl` 结构体：从 `Impl` 派生，用于存储具体的 lambda 并实现调用逻辑。

####  总结

这个代码片段提供了一种灵活的机制来处理函数调用和类型推断。`Empty` 结构体用于表示空结果，`call_traits` 结构体用于检查可调用对象的特性，而 `FnOnce` 类模板提供了一种类型擦除的方式来处理只能调用一次的可调用对象。这些组件结合在一起，为处理复杂的函数调用场景提供了强大的支持。

### result 类设计
这个代码片段定义了一个模板类 `Result<T>`，用于表示一个可能包含有效值或错误状态的对象。它的设计目的是在函数执行过程中可能失败的情况下，提供一种返回值的机制。以下是该架构的详细分析：

#### 为什么这样设计
```

1. 统一处理成功和失败的结果
在许多编程场景中，函数可能会成功返回一个值，也可能会失败并返回一个错误状态。传统的处理方式可能包括返回特殊值、抛出异常或使用输出参数来传递错误信息。Result 类提供了一种统一的方式来处理这些情况：

成功：Result 对象包含一个有效的值。
失败：Result 对象包含一个错误状态。


2. 简化错误处理逻辑
使用 Result 类可以简化错误处理逻辑，使代码更加清晰和易于维护。例如，使用 Result 类可以避免嵌套的条件检查和复杂的错误处理代码：


3. 提高代码的可读性和可维护性
通过使用 Result 类，函数的返回类型明确地表示了可能的失败情况，使得代码更加自文档化。调用者可以清晰地看到函数可能返回错误状态，并且必须处理这些状态：

4. 避免异常处理的开销
在某些编程语言和环境中，异常处理可能会带来性能开销。Result 类提供了一种替代方案，通过显式地返回错误状态来避免异常处理的开销，同时仍然提供了丰富的错误信息。


5. 提供丰富的操作方法
Result 类提供了多种操作方法，使得处理结果更加灵活和方便：

ValueOrDie()：获取存储的值，如果状态不是 OK，则中止程序。
ValueOr(T alternative)：获取存储的值，如果状态不是 OK，则返回替代值。
ValueOrElse(G&& generate_alternative)：获取存储的值，如果状态不是 OK，则调用提供的函数生成替代值。
Map(M&& m)：对存储的值应用函数，并返回新的 Result。


6. 支持移动语义
Result 类支持移动语义，使得处理包含移动类型（如 std::unique_ptr）的结果更加高效：


arrow::Result<std::unique_ptr<Foo>> result = CalculateFoo();
if (result.ok()) {
  std::unique_ptr<Foo> foo = std::move(result).ValueOrDie();
  foo->DoSomethingCool();
} else {
  ARROW_LOG(ERROR) << result.status();
}


总结
Result 类提供了一种统一、简洁和高效的方式来处理函数调用的结果，特别是在函数可能失败的情况下。它简化了错误处理逻辑，提高了代码的可读性和可维护性，避免了异常处理的开销，并提供了丰富的操作方法和对移动语义的支持。这些优势使得 Result 类在处理复杂的函数调用和结果管理场景中非常有用。

```

####  类的基本结构

- **模板参数**：`Result<T>` 是一个模板类，`T` 是结果的值类型。`T` 必须是可复制构造或可移动构造的。
- **状态管理**：`Result` 对象要么包含一个类型为 `T` 的值，要么包含一个 `Status` 对象，后者解释了为什么没有值。

####  构造函数

- **默认构造函数**：创建一个包含非 OK 状态的 `Result` 对象。
- **状态构造函数**：接受一个非 OK 的 `Status` 对象来初始化 `Result`，如果传入 OK 状态则会导致程序中止。
- **值构造函数**：接受一个值 `U`，并将其存储在 `Result` 中，状态被设置为 OK。
- **复制构造函数**：从另一个 `Result` 对象复制构造。
- **移动构造函数**：从另一个 `Result` 对象移动构造。

####  成员函数

- **状态检查**：`ok()` 方法用于检查 `Result` 是否包含有效值。
- **状态获取**：`status()` 方法返回内部的 `Status` 对象。
- **值获取**：`ValueOrDie()` 方法返回存储的值，如果状态不是 OK，则会中止程序。
- **值操作**：`ValueOr()` 和 `ValueOrElse()` 提供了在状态非 OK 时返回替代值的机制。
- **映射操作**：`Map()` 方法允许对存储的值应用函数，并返回新的 `Result`。

####  运算符重载

- **赋值运算符**：支持复制和移动赋值。
- **比较运算符**：`Equals()` 方法用于比较两个 `Result` 对象。

####  宏定义

- **`ARROW_ASSIGN_OR_RAISE`**：用于简化从 `Result` 中提取值的过程，如果状态不是 OK，则返回错误状态。

####  内部实现细节

- **存储管理**：使用 `internal::AlignedStorage<T>` 来管理存储的值。
- **辅助函数**：`ConstructValue()` 和 `Destroy()` 用于构造和销毁存储的值。

####  用途

`Result<T>` 类的设计目的是在函数可能失败的情况下提供一种返回值的机制，避免使用异常处理。通过这种方式，调用者可以明确地检查函数调用的结果，并根据状态采取相应的操作。这种模式在需要高性能和明确错误处理的系统中非常有用。

总的来说，这个架构提供了一种安全、灵活的方式来处理可能失败的操作，并且通过模板和宏的使用，提供了很高的可扩展性和易用性。


### Future
#### 为什么这样设计
```
Future类是核心，表示异步计算的结果。它支持泛型，通过模板参数T来表示结果的类型。
提供了生产者和消费者API。生产者API用于创建和完成Future，消费者API用于等待和获取结果。


状态管理：

使用FutureState枚举来表示Future的状态（如PENDING、SUCCESS、FAILURE）。
FutureImpl类负责管理Future的状态和结果存储。


回调机制：

支持添加回调函数，当Future完成时执行。回调可以根据Future的状态执行不同的逻辑。
ContinueFuture结构用于处理回调的返回值，并决定如何继续执行。


同步和异步处理：

SyncType结构用于将异步结果转换为同步结果。
ShouldSchedule枚举和CallbackOptions结构用于控制回调的执行方式（同步或异步）。


辅助功能：

提供了多个辅助函数，如WaitForAll、WaitForAny、Loop等，用于处理多个Future的情况。

```

#### 关键类
```
EnsureFuture：这是一个模板结构，用于确保某个类型可以转换为Future。它使用decltype和ToFuture函数来推断类型。
is_future：这是一个模板结构，用于判断某个类型是否为Future。通过特化is_future<Future<T>>为std::true_type来实现。

result_of：用于推断函数调用的返回类型。通过decltype和std::declval来实现。
result_of_t：是result_of的简化版本，直接获取返回类型。

SyncType：用于将异步结果转换为同步结果。对于普通类型，返回Result<T>；对于internal::Empty，返回Status。

MarkNextFinished：这是一个模板结构，用于创建一个回调，将源Future的结果传递给目标Future。
根据源和目标是否为空，提供不同的实现方式。

ContinueFuture：用于处理回调的返回值，并决定如何继续执行。
    ForReturnImpl：根据回调的返回类型，决定返回的Future类型。
    operator()：根据回调的返回类型，执行不同的逻辑。

FutureImpl：这是Future的底层实现，负责管理状态和结果存储。
    state()：返回当前的Future状态。
    MarkFinished/MarkFailed：用于标记Future完成或失败。
    AddCallback：添加回调函数，当Future完成时执行。


FutureWaiter：用于等待多个Future完成。
    Wait：等待所有Future完成或超时。
    MoveFinishedFutures：返回已完成的Future的索引。


Future：表示异步计算的结果。
    Make/MakeFinished：用于创建Future。
    Wait：等待Future完成。
    AddCallback：添加回调函数。
    Then：注册一个延续，当Future完成时执行。


WaitForAll/WaitForAny：用于等待多个Future完成。
    All/AllComplete/AllFinished：创建一个Future，当所有Future完成时完成。
    Loop：用于循环异步操作，直到某个条件满足。

```


#### 使用Future的模版
使用`Future`类的关键在于理解它如何帮助管理异步操作的结果。以下是一些常见的使用场景和如何调用相关函数的指南：

#####  1. 创建和完成`Future`

- **创建一个未完成的`Future`**：
  ```cpp
  auto future = Future<int>::Make();
  ```
  使用`Make()`方法创建一个新的`Future`对象。此时，`Future`处于`PENDING`状态。

- **标记`Future`完成**：
  ```cpp
  future.MarkFinished(Result<int>(42));
  ```
  使用`MarkFinished()`方法将`Future`标记为完成，并设置其结果。

#####  2. 等待`Future`完成

- **等待`Future`完成**：
  ```cpp
  future.Wait();
  ```
  使用`Wait()`方法阻塞当前线程，直到`Future`完成。

- **带超时的等待**：
  ```cpp
  bool completed = future.Wait(5.0);  // 等待5秒
  ```
  使用带超时的`Wait()`方法，可以在指定时间内等待`Future`完成。

#####  3. 获取结果

- **获取结果**：
  ```cpp
  auto result = future.result();
  if (result.ok()) {
    int value = result.ValueOrDie();
  } else {
    // 处理错误
  }
  ```
  使用`result()`方法获取`Future`的结果，结果是一个`Result<T>`对象。

#####  4. 添加回调

- **添加回调函数**：
  ```cpp
  future.AddCallback([](const Result<int>& result) {
    if (result.ok()) {
      std::cout << "Result: " << result.ValueOrDie() << std::endl;
    } else {
      std::cerr << "Error: " << result.status() << std::endl;
    }
  });
  ```
  使用`AddCallback()`方法为`Future`添加一个回调函数，当`Future`完成时执行。

#####  5. 使用`Then`注册延续

- **注册延续**：
  ```cpp
  auto next_future = future.Then([](const int& value) {
    return value * 2;  // 返回一个新的结果
  });
  ```
  使用`Then()`方法注册一个延续，当`Future`完成时执行。延续可以返回一个新的结果或`Future`。

#####  6. 等待多个`Future`

- **等待所有`Future`完成**：
  ```cpp
  std::vector<Future<int>> futures = {future1, future2, future3};
  WaitForAll(futures);
  ```
  使用`WaitForAll()`函数等待多个`Future`完成。

- **等待任意一个`Future`完成**：
  ```cpp
  auto completed_indices = WaitForAny(futures);
  ```
  使用`WaitForAny()`函数等待任意一个`Future`完成，并获取已完成的`Future`的索引。

#####  7. 异步循环

- **使用`Loop`进行异步循环**：
  ```cpp
  auto loop_future = Loop([]() -> Future<ControlFlow<>> {
    // 执行异步操作
    return Future<>::MakeFinished(Continue());
  });
  ```
  使用`Loop()`函数进行异步循环，直到某个条件满足。

#####  使用场景

- **异步计算**：在需要执行耗时操作而不阻塞主线程时使用`Future`。
- **并发任务管理**：在需要管理多个并发任务的结果时，使用`WaitForAll`和`WaitForAny`。
- **回调链**：使用`Then`方法创建回调链，以便在异步操作完成后执行一系列操作。
- **错误处理**：通过`Result`对象处理异步操作中的错误。

通过这些功能，`Future`类可以帮助你有效地管理异步操作，简化并发编程的复杂性。



#### Future测试用例解读
```cpp
TEST(FutureSyncTest, Int) {
  {
    // 测试 MarkFinished(int)
    auto fut = Future<int>::Make();  // 创建一个未完成的 Future<int>
    AssertNotFinished(fut);  // 断言 Future 尚未完成
    fut.MarkFinished(42);  // 将 Future 标记为完成，结果为 42
    AssertSuccessful(fut);  // 断言 Future 成功完成
    auto res = fut.result();  // 获取 Future 的结果
    ASSERT_OK(res);  // 断言结果状态为成功
    ASSERT_EQ(*res, 42);  // 断言结果值为 42
    res = std::move(fut).result();  // 移动 Future 并获取结果
    ASSERT_OK(res);  // 断言结果状态为成功
    ASSERT_EQ(*res, 42);  // 断言结果值为 42
  }
  {
    // 测试 MakeFinished(int)
    auto fut = Future<int>::MakeFinished(42);  // 创建一个结果为 42 的完成的 Future<int>
    AssertSuccessful(fut);  // 断言 Future 成功完成
    auto res = fut.result();  // 获取 Future 的结果
    ASSERT_OK(res);  // 断言结果状态为成功
    ASSERT_EQ(*res, 42);  // 断言结果值为 42
    res = std::move(fut.result());  // 移动 Future 并获取结果
    ASSERT_OK(res);  // 断言结果状态为成功
    ASSERT_EQ(*res, 42);  // 断言结果值为 42
  }
  {
    // 测试 MarkFinished(Result<int>)
    auto fut = Future<int>::Make();  // 创建一个未完成的 Future<int>
    AssertNotFinished(fut);  // 断言 Future 尚未完成
    fut.MarkFinished(Result<int>(43));  // 将 Future 标记为完成，结果为 Result<int>(43)
    AssertSuccessful(fut);  // 断言 Future 成功完成
    ASSERT_OK_AND_ASSIGN(auto value, fut.result());  // 获取 Future 的结果并断言状态为成功
    ASSERT_EQ(value, 43);  // 断言结果值为 43
  }
  {
    // 测试 MarkFinished(failed Result<int>)
    auto fut = Future<int>::Make();  // 创建一个未完成的 Future<int>
    AssertNotFinished(fut);  // 断言 Future 尚未完成
    fut.MarkFinished(Result<int>(Status::IOError("xxx")));  // 将 Future 标记为失败，错误为 IOError
    AssertFailed(fut);  // 断言 Future 失败
    ASSERT_RAISES(IOError, fut.result());  // 断言获取结果时抛出 IOError
  }
  {
    // 测试 MakeFinished(Status)
    auto fut = Future<int>::MakeFinished(Status::IOError("xxx"));  // 创建一个失败的 Future<int>
    AssertFailed(fut);  // 断言 Future 失败
    ASSERT_RAISES(IOError, fut.result());  // 断言获取结果时抛出 IOError
  }
  {
    // 测试 MarkFinished(Status)
    auto fut = Future<int>::Make();  // 创建一个未完成的 Future<int>
    AssertNotFinished(fut);  // 断言 Future 尚未完成
    fut.MarkFinished(Status::IOError("xxx"));  // 将 Future 标记为失败，错误为 IOError
    AssertFailed(fut);  // 断言 Future 失败
    ASSERT_RAISES(IOError, fut.result());  // 断言获取结果时抛出 IOError
  }
}

```


#### Future 回调机制 测试用例解读
```cpp

测试目的：代码旨在测试Future对象的回调机制，确保在不同的线程环境下，回调能够正确执行，并且在高负载情况下（即大量回调被添加时），系统能够正常工作。

条件编译：代码使用了条件编译指令#ifdef ARROW_VALGRIND，这意味着在使用Valgrind进行内存检查时，测试迭代次数NITERS会减少到2次，以减少测试时间和资源消耗。在正常情况下，迭代次数为1000次。

回调添加线程：代码启动了一个线程callback_adder，不断向Future对象添加回调函数。回调函数会检查当前线程是否与添加回调的线程相同，并根据结果更新计数器count_finished_immediately或count_finished_deferred。

计数器：使用了多个std::atomic计数器来记录回调的状态：

    count_finished_immediately：记录在添加回调的线程中立即完成的回调数量。
    count_finished_deferred：记录在其他线程中完成的回调数量。
    callbacks_added：记录添加的回调总数。

同步机制：主线程会等待直到至少一个回调被添加，然后标记Future对象为完成状态fut.MarkFinished()。这会触发所有已添加的回调。

结束条件：主线程会等待直到至少一个回调在添加线程中完成，然后设置finished标志为true，以通知callback_adder线程结束。

验证：最后，测试验证添加的回调总数是否等于立即完成和延迟完成的回调总数之和，确保所有回调都被正确执行。


TEST(FutureStressTest, Callback) {
#ifdef ARROW_VALGRIND
  // 如果使用Valgrind进行内存检查，减少迭代次数以节省资源
  const int NITERS = 2;
#else
  // 正常情况下的迭代次数
  const int NITERS = 1000;
#endif

  // 进行NITERS次测试迭代
  for (unsigned int n = 0; n < NITERS; n++) {
    // 创建一个Future对象
    auto fut = Future<>::Make();
    // 原子计数器，用于记录立即完成的回调数量
    std::atomic<unsigned int> count_finished_immediately(0);
    // 原子计数器，用于记录延迟完成的回调数量
    std::atomic<unsigned int> count_finished_deferred(0);
    // 原子计数器，用于记录添加的回调总数
    std::atomic<unsigned int> callbacks_added(0);
    // 标志位，用于指示回调添加线程是否应该停止
    std::atomic<bool> finished(false);

    // 创建一个线程，用于不断添加回调到Future对象
    std::thread callback_adder([&] {
      // 获取当前线程的ID
      auto test_thread = std::this_thread::get_id();
      // 当finished标志为false时，持续添加回调
      while (!finished.load()) {
        // 添加回调函数到Future对象
        fut.AddCallback([&test_thread, &count_finished_immediately,
                         &count_finished_deferred](const Status& status) {
          // 检查状态是否OK
          ARROW_EXPECT_OK(status);
          // 判断回调是否在添加回调的线程中执行
          if (std::this_thread::get_id() == test_thread) {
            // 如果是，增加立即完成计数器
            count_finished_immediately++;
          } else {
            // 否则，增加延迟完成计数器
            count_finished_deferred++;
          }
        });
        // 增加回调添加计数器
        callbacks_added++;
        // 如果添加的回调数量超过10000，且主线程尚未注意到，稍作休眠
        if (callbacks_added.load() > 10000) {
          // 休眠一段时间以帮助主线程
          SleepABit();
        }
      }
    });

    // 主线程等待，直到至少一个回调被添加
    while (callbacks_added.load() == 0) {
      // 自旋等待回调添加线程开始运行
    }

    // 确保在Future标记完成之前没有回调被延迟完成
    ASSERT_EQ(0, count_finished_deferred.load());
    ASSERT_EQ(0, count_finished_immediately.load());

    // 标记Future对象为完成状态，触发回调执行
    fut.MarkFinished();

    // 主线程等待，直到至少一个回调在添加线程中完成
    while (count_finished_immediately.load() == 0) {
      // 自旋等待回调添加线程添加至少一个回调
    }

    // 设置finished标志为true，通知回调添加线程结束
    finished.store(true);
    // 等待回调添加线程结束
    callback_adder.join();
    // 获取添加的回调总数
    auto total_added = callbacks_added.load();
    // 获取立即完成的回调总数
    auto total_immediate = count_finished_immediately.load();
    // 获取延迟完成的回调总数
    auto total_deferred = count_finished_deferred.load();
    // 验证添加的回调总数是否等于立即完成和延迟完成的回调总数之和
    ASSERT_EQ(total_added, total_immediate + total_deferred);
  }
}




TEST(FutureStressTest, TryAddCallback) {
  // 进行一次测试迭代
  for (unsigned int n = 0; n < 1; n++) {
    // 创建一个Future对象
    auto fut = Future<>::Make();
    // 原子计数器，用于记录成功添加的回调数量
    std::atomic<unsigned int> callbacks_added(0);
    // 标志位，用于指示回调添加线程是否完成
    std::atomic<bool> finished(false);
    // 互斥锁和条件变量，用于线程同步
    std::mutex mutex;
    std::condition_variable cv;
    // 用于存储回调添加线程的ID
    std::thread::id callback_adder_thread_id;

    // 创建一个线程，用于不断尝试添加回调到Future对象
    std::thread callback_adder([&] {
      // 获取并存储当前线程的ID
      callback_adder_thread_id = std::this_thread::get_id();
      // 定义一个回调函数
      std::function<void(const Status&)> callback =
          [&callback_adder_thread_id](const Status& st) {
            // 检查状态是否OK
            ARROW_EXPECT_OK(st);
            // 如果回调在添加回调的线程中同步执行，则测试失败
            if (std::this_thread::get_id() == callback_adder_thread_id) {
              FAIL() << "TryAddCallback allowed a callback to be run synchronously";
            }
          };
      // 定义一个回调工厂函数，返回回调函数
      std::function<std::function<void(const Status&)>()> callback_factory =
          [&callback]() { return callback; };
      // 不断尝试添加回调，直到失败
      while (true) {
        auto callback_added = fut.TryAddCallback(callback_factory);
        if (callback_added) {
          // 如果成功添加回调，增加计数器
          callbacks_added++;
          // 如果添加的回调数量超过10000，且主线程尚未注意到，稍作休眠
          if (callbacks_added.load() > 10000) {
            // 休眠一段时间以帮助主线程
            SleepABit();
          }
        } else {
          // 如果无法添加回调，退出循环
          break;
        }
      }
      {
        // 使用锁保护对finished标志的修改
        std::lock_guard<std::mutex> lg(mutex);
        finished.store(true);
      }
      // 通知主线程回调添加线程已完成
      cv.notify_one();
    });

    // 主线程等待，直到至少一个回调被添加
    while (callbacks_added.load() == 0) {
      // 自旋等待回调添加线程开始运行
    }

    // 标记Future对象为完成状态，触发回调执行
    fut.MarkFinished();

    // 等待回调添加线程完成，最多等待0.5秒
    std::unique_lock<std::mutex> lk(mutex);
    cv.wait_for(lk, std::chrono::duration<double>(0.5),
                [&finished] { return finished.load(); });
    lk.unlock();

    // 验证回调添加线程已完成
    ASSERT_TRUE(finished);
    // 等待回调添加线程结束
    callback_adder.join();
  }
}
```


#### Future Then机制测试用例解读
```cpp

Future:

Future对象代表一个异步操作的结果，它可能在未来的某个时间点完成。
Future通常用于表示一个尚未完成的计算或操作，允许程序继续执行而不必等待该操作完成。
Then:

Then方法用于在Future对象完成后执行某个回调函数。
当Future对象完成时，Then方法会触发回调函数，并将Future的结果传递给回调函数。
Then方法返回一个新的Future对象，代表回调函数的执行结果。这使得可以创建一个Future链，依次执行多个异步操作。

TEST(FutureRefTest, ChainRemoved) {
  // 创建一个future链不应该阻止这些future被删除，如果整个链被删除
  std::weak_ptr<FutureImpl> ref;
  std::weak_ptr<FutureImpl> ref2;
  {
    // 创建一个Future对象
    auto fut = Future<>::Make();
    // 创建一个链式Future对象
    auto fut2 = fut.Then([]() { return Status::OK(); });
    // 获取Future对象的弱引用
    ref = fut.impl_;
    ref2 = fut2.impl_;
  }
  // 验证Future对象已经被删除
  ASSERT_TRUE(ref.expired());
  ASSERT_TRUE(ref2.expired());

  {
    // 创建另一个Future对象
    auto fut = Future<>::Make();
    // 创建另一个链式Future对象
    auto fut2 = fut.Then([]() { return Future<>::Make(); });
    // 获取Future对象的弱引用
    ref = fut.impl_;
    ref2 = fut2.impl_;
  }
  // 验证Future对象已经被删除
  ASSERT_TRUE(ref.expired());
  ASSERT_TRUE(ref2.expired());
}

TEST(FutureRefTest, TailRemoved) {
  // 保留future链的头部应该保持整个链的存活
  std::shared_ptr<Future<>> ref;
  std::weak_ptr<FutureImpl> ref2;
  bool side_effect_run = false;
  {
    // 创建一个共享的Future对象
    ref = std::make_shared<Future<>>(Future<>::Make());
    // 创建一个链式Future对象，并设置副作用
    auto fut2 = ref->Then([&side_effect_run]() {
      side_effect_run = true;
      return Status::OK();
    });
    // 获取链式Future对象的弱引用
    ref2 = fut2.impl_;
  }
  // 验证链式Future对象仍然存活
  ASSERT_FALSE(ref2.expired());

  // 标记Future对象为完成状态，触发副作用
  ref->MarkFinished();
  // 验证副作用已经运行
  ASSERT_TRUE(side_effect_run);
  // 验证链式Future对象已经被删除
  ASSERT_TRUE(ref2.expired());
}

TEST(FutureRefTest, HeadRemoved) {
  // 保留future链的尾部不应该保持整个链的存活。如果没有人引用头部，那么future被放弃。
  // TODO (ARROW-12207): 检测放弃。
  std::weak_ptr<FutureImpl> ref;
  std::shared_ptr<Future<>> ref2;
  {
    // 创建一个共享的Future对象
    auto fut = std::make_shared<Future<>>(Future<>::Make());
    // 获取Future对象的弱引用
    ref = fut->impl_;
    // 创建一个链式Future对象
    ref2 = std::make_shared<Future<>>(fut->Then([]() {}));
  }
  // 验证Future对象已经被删除
  ASSERT_TRUE(ref.expired());

  {
    // 创建另一个Future对象
    auto fut = Future<>::Make();
    // 创建一个链式Future对象，并设置中间Future对象
    ref2 = std::make_shared<Future<>>(fut.Then([&]() {
      auto intermediate = Future<>::Make();
      ref = intermediate.impl_;
      return intermediate;
    }));
    // 标记Future对象为完成状态
    fut.MarkFinished();
  }
  // 验证中间Future对象已经被删除
  ASSERT_TRUE(ref.expired());
}


```


#### Future Then机制测试用例解读
```cpp
FutureSchedulingTest类:

该类继承自testing::Test，用于定义测试用例。
executor()方法返回mock_executor指针。
spawn_count()方法返回捕获的任务数量。
AssertRunSynchronously()和AssertScheduled()方法用于断言回调函数是否同步运行或被调度。
AssertIds()方法用于断言回调函数的ID是否符合预期。
callback()方法返回一个回调函数，该函数会将ID插入callbacks_run_synchronously集合。
mock_executor是一个共享的DelayedExecutor对象，用于模拟执行器。
callbacks_run_synchronously是一个集合，用于存储同步运行的回调函数ID。
ScheduleNever测试用例:

配置回调选项options，设置should_schedule为ShouldSchedule::Never，并指定执行器。
测试成功的Future对象，添加回调函数并标记为完成状态，验证没有任务被调度，回调函数同步运行。
测试失败的Future对象，添加回调函数并标记为失败状态，验证没有任务被调度，回调函数同步运行。


设计FutureSchedulingTest的目的是为了测试和验证Future对象在不同调度策略下的行为。具体来说，FutureSchedulingTest旨在确保Future对象的回调函数在预期的调度条件下正确执行。以下是设计该测试的几个主要目的：

验证调度策略:

测试不同的调度策略（例如，永不调度、总是调度等）对Future对象的影响。
确保在设置为不调度时，回调函数能够同步执行。
确保正确执行:

确保回调函数在Future对象完成后能够正确执行，无论Future是成功还是失败。
验证回调函数是否按照预期的同步或异步方式执行。
测试执行器行为:

使用模拟执行器（mock_executor）来捕获和验证任务的调度行为。
确保在特定调度策略下，执行器不会调度任何任务。



// 定义一个名为FutureSchedulingTest的测试类，继承自testing::Test
class FutureSchedulingTest : public testing::Test {
 public:
  // 返回mock_executor指针
  internal::Executor* executor() { return mock_executor.get(); }

  // 返回捕获的任务数量
  int spawn_count() { return static_cast<int>(mock_executor->captured_tasks.size()); }

  // 断言回调函数同步运行
  void AssertRunSynchronously(const std::vector<int>& ids) { AssertIds(ids, true); }

  // 断言回调函数被调度
  void AssertScheduled(const std::vector<int>& ids) { AssertIds(ids, false); }

  // 断言回调函数的ID是否符合预期
  void AssertIds(const std::vector<int>& ids, bool should_be_synchronous) {
    for (auto id : ids) {
      ASSERT_EQ(should_be_synchronous, callbacks_run_synchronously.find(id) !=
                                           callbacks_run_synchronously.end());
    }
  }

  // 返回一个回调函数，该函数会将ID插入callbacks_run_synchronously集合
  std::function<void(const Status&)> callback(int id) {
    return [this, id](const Status&) { callbacks_run_synchronously.insert(id); };
  }

  // 创建一个共享的DelayedExecutor对象
  std::shared_ptr<DelayedExecutor> mock_executor = std::make_shared<DelayedExecutor>();
  // 用于存储同步运行的回调函数ID
  std::unordered_set<int> callbacks_run_synchronously;
};

// 定义一个名为ScheduleNever的测试用例，使用FutureSchedulingTest类
TEST_F(FutureSchedulingTest, ScheduleNever) {
  // 配置回调选项
  CallbackOptions options;
  options.should_schedule = ShouldSchedule::Never;
  options.executor = executor();
  
  // 测试成功的Future对象
  {
    auto fut = Future<>::Make();
    // 添加回调函数，使用配置的选项
    fut.AddCallback(callback(1), options);
    // 标记Future对象为完成状态
    fut.MarkFinished();
    // 添加另一个回调函数
    fut.AddCallback(callback(2), options);
    // 验证没有任务被调度
    ASSERT_EQ(0, spawn_count());
    // 验证回调函数同步运行
    AssertRunSynchronously({1, 2});
  }
  
  // 测试失败的Future对象
  {
    auto fut = Future<>::Make();
    // 添加回调函数，使用配置的选项
    fut.AddCallback(callback(3), options);
    // 标记Future对象为失败状态
    fut.MarkFinished(Status::Invalid("XYZ"));
    // 添加另一个回调函数
    fut.AddCallback(callback(4), options);
    // 验证没有任务被调度
    ASSERT_EQ(0, spawn_count());
    // 验证回调函数同步运行
    AssertRunSynchronously({3, 4});
  }
}

```

#### 深度理解 - MakeFinished 和 MarkFinished 区别是什么
```
MakeFinished和MarkFinished都是用于处理Future对象的方法，但它们在使用场景和功能上有所不同。

MakeFinished
    功能：MakeFinished用于创建一个已经完成的Future对象。它在创建时就已经有了结果或状态。
    使用场景：当你已经有了计算结果或错误状态，并且希望立即创建一个完成的Future时使用。
示例：
auto fut = Future<int>::MakeFinished(42);  // 创建一个结果为42的完成的Future
auto fut_error = Future<int>::MakeFinished(Status::IOError("xxx"));  // 创建一个失败的Future


MarkFinished
    功能：MarkFinished用于将一个已经创建但未完成的Future对象标记为完成，并设置其结果或状态。
    使用场景：当你有一个未完成的Future对象，并且在某个时刻获得了结果或错误状态时使用。
示例：
auto fut = Future<int>::Make();  // 创建一个未完成的Future
fut.MarkFinished(42);  // 将Future标记为完成，结果为42
fut.MarkFinished(Status::IOError("xxx"));  // 将Future标记为失败

总结
    MakeFinished：用于创建一个立即完成的Future，适合在结果已知的情况下使用。
    MarkFinished：用于标记一个未完成的Future为完成，适合在异步计算结束后使用。

```

#### 深度理解 - CallbackOptions 和 ShouldSchedule 和 回调函数 是什么
```
 std::function<void(const Status&)> callback(int id) {
    return [this, id](const Status&) { callbacks_run_synchronously.insert(id); };
  }

执行动作
    就是往 一个集合写入一个数字
    验证只需要判断集合里面的数字即可

函数签名:
    std::function<void(const Status&)> callback(int id)：这是一个返回类型为std::function<void(const Status&)>的函数，接受一个整数id作为参数。
    std::function<void(const Status&)>表示一个函数对象，它接受一个Status类型的参数并返回void。


Lambda表达式:
    [this, id](const Status&) { callbacks_run_synchronously.insert(id); }：这是一个捕获this指针和id的lambda表达式。
    this指针用于访问当前类的成员变量callbacks_run_synchronously。
    id是传递给callback函数的参数，用于标识回调函数。


回调函数行为:

    当回调函数被调用时，它会将传入的Status对象忽略（因为没有使用），并将id插入到callbacks_run_synchronously集合中。
    callbacks_run_synchronously是一个std::unordered_set<int>类型的集合，用于记录哪些回调函数是同步运行的。

```


#### 深度理解 - wait 和 TimedWait 和 Completed

### async_util

这段代码是一个C++库的一部分，提供了一些用于异步编程的工具和类。它主要涉及到异步对象的销毁、任务组管理和任务序列化。以下是对代码中主要部分的解释：

#### 主要组件

1. **`AsyncDestroyable`类**:
   - 这是一个基类，设计用于需要在销毁前异步关闭的对象。
   - 子类需要实现`DoDestroy()`方法，该方法返回一个`Future<>`，表示对象何时可以安全销毁。
   - 提供了`on_closed()`方法，返回一个`Future<>`，用于等待对象完成所有工作并准备好销毁。

2. **`DestroyingDeleter`结构体**:
   - 自定义删除器，用于异步销毁对象。
   - 当对象指针被删除时，调用对象的`Destroy()`方法。

3. **`MakeSharedAsync`和`MakeUniqueAsync`函数**:
   - 用于创建`AsyncDestroyable`对象的智能指针。
   - 确保对象在销毁前正确地异步关闭。

4. **`AsyncTaskGroup`类**:
   - 管理一组异步任务，提供结构化并发。
   - 可以添加任务并等待所有任务完成。
   - 提供`End()`方法，表示不再添加新的顶级任务，并返回一个`Future<>`，在所有任务完成时完成。

5. **`SerializedAsyncTaskGroup`类**:
   - 管理一组按顺序执行的异步任务。
   - 确保任务按添加顺序执行。
   - 提供`End()`方法，表示所有任务已添加，并返回一个`Future<>`，在所有任务完成时完成。
   - 提供`Abort()`方法，用于中止任务组，丢弃未开始的任务。

这段代码中的英文注释为每个类和函数提供了背景信息和使用说明，帮助开发者理解这些工具的设计目的和使用方法。以下是对这些注释的解释，以及为什么需要这些工具：


1. **`AsyncDestroyable`类**:
   - 注释解释了这个类的用途：确保在对象销毁前异步完成关闭操作。这对于需要在销毁前完成异步清理的对象非常重要。
   - 提供了如何使用这个类的指导，特别是通过`MakeSharedAsync`或`MakeUniqueAsync`来构造对象。

2. **`DestroyingDeleter`结构体**:
   - 注释说明了这是一个自定义删除器，用于在对象指针被删除时调用对象的`Destroy()`方法。

3. **`MakeSharedAsync`和`MakeUniqueAsync`函数**:
   - 注释指出这些函数用于创建`AsyncDestroyable`对象的智能指针，并确保对象在销毁前正确地异步关闭。

4. **`AsyncTaskGroup`类**:
   - 注释描述了这个类用于管理一组异步任务，提供结构化并发。
   - 解释了如何添加任务、结束任务添加以及等待所有任务完成。

5. **`SerializedAsyncTaskGroup`类**:
   - 注释说明了这个类用于按顺序执行异步任务，确保任务按添加顺序执行。
   - 提供了如何添加任务、结束任务添加以及中止任务组的说明。



6. **异步资源管理**:
   - 在异步编程中，资源的生命周期管理变得复杂。`AsyncDestroyable`类及其相关工具帮助开发者确保资源在销毁前完成所有必要的异步清理工作，避免资源泄漏或未完成的操作。

7. **任务管理和协调**:
   - `AsyncTaskGroup`和`SerializedAsyncTaskGroup`提供了一种结构化的方式来管理和协调多个异步任务。这对于需要同时处理多个异步操作的应用程序非常重要，确保任务按预期顺序执行，并在所有任务完成后进行清理或继续后续操作。

8. **提高代码可读性和维护性**:
   - 这些工具通过提供一致的接口和行为，简化了异步编程的复杂性，提高了代码的可读性和维护性。开发者可以专注于业务逻辑，而不必担心底层的异步管理细节。

总之，这些工具和注释为开发者提供了强大的支持，帮助他们在复杂的异步环境中编写更可靠和可维护的代码。
#### 使用场景

- **异步对象管理**: `AsyncDestroyable`类及其相关工具用于管理需要异步关闭的对象，确保在对象销毁前完成所有必要的清理工作。
- **任务管理**: `AsyncTaskGroup`和`SerializedAsyncTaskGroup`用于管理和协调多个异步任务，确保任务按预期顺序执行，并在所有任务完成后进行清理或继续后续操作。
- 

#### 示例用法

假设你有一个需要异步关闭的资源类`MyResource`，可以继承`AsyncDestroyable`并实现`DoDestroy()`方法。然后使用`MakeSharedAsync`或`MakeUniqueAsync`创建对象，并在需要时等待`on_closed()`完成。

对于任务管理，可以创建一个`AsyncTaskGroup`实例，添加任务并调用`End()`等待所有任务完成。对于需要按顺序执行的任务，可以使用`SerializedAsyncTaskGroup`。

这些工具在异步编程中非常有用，帮助开发者管理复杂的异步操作和资源生命周期。

### AsyncTaskGroup

### AsyncGenerator

## 异步编程 - async_simple 设计


## 异步编程 - Folly Future设计