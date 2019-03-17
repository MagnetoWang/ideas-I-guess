## 《C++ Concurrency In Action》读书笔记

- 多线程一直都是初级工程师和中级工程师的一个分水岭
- 掌握了多线程编程可以说这位工程师能够独当一面
- 所以，这篇笔记主要是提取并发编程实战的精髓，方便以后快速回顾多线程的知识点
- 因为对多线程概念的理解要求准确和到位，所以这个笔记尽量会用英文解释一个概念和描述设计思维

## 看书技巧

- 这本书说实话，很不适合中国人的阅读习惯
- 看书需要方法
- 先看目录，然后选你想看的标题
- 看到标题后，自己思考一下场景和解决方案
- 再继续看标题中代码清单，这本书基本上都有代码案例

### Introduction concurrency in C++

### Managing thread

### Sharing data between threads

### Synchronizing concurrent operations



## 问题列表

### 环境

- macbookpro 2017版本
- 4.sdk/usr/include/c++/4.2.1
- Apple LLVM version 10.0.0 (clang-1000.10.44.2)
- Target: x86_64-apple-darwin18.0.0
- Thread model: posix
- InstalledDir: /Library/Developer/CommandLineTools/usr/bin

### list5.5

- 这里和书中不一样，代码实际运行不可能等于0
- 除非注释 while(!y.load(std::memory_order_relaxed));

### list5.7

- 这里和书中不一样，代码实际运行不可能等于0
- 除非注释下面任意代码
  - while(!x.load(std::memory_order_acquire));
  - while(!y.load(std::memory_order_acquire));

## 本书已读完

- 一气呵成，获益良多

- 现阶段，因为有论文要写，所以笔记将会用零碎的时间进行填充
