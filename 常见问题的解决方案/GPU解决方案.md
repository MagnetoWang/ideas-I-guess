## GPU解决方案

### 资料
1. 入门
   1. CUDATutorial：https://github.com/PaddleJitLab/CUDATutorial?tab=readme-ov-file
   2. 如何系统地学习CUDA？ - Kedreamix的回答 - 知乎 https://www.zhihu.com/question/263832290/answer/3322864217
   3. https://github.com/Kedreamix/pytorch-cppcuda-tutorial
   4. cuda编程示例：https://face2ai.com/program-blog/#GPU%E7%BC%96%E7%A8%8B%EF%BC%88CUDA%EF%BC%89
   5. CUDATutorial：https://cuda.keter.top/
2. 优化
   1. [CUDA 学习笔记] GEMM 优化: 双缓冲 (Prefetch) 和 Bank Conflict 解决 - PeakCrosser的文章 - 知乎 https://zhuanlan.zhihu.com/p/696844342
```











CUDA还能走多远？ - 王振邦的回答 - 知乎
https://www.zhihu.com/question/30597217/answer/3024851394


如何系统学习GPU架构？ - Bruce 仗剑走天涯的回答 - 知乎
https://www.zhihu.com/question/319355296/answer/3374307130


gpu计算：https://www.bilibili.com/video/BV1hE41187Mb?p=3


HPC 中kernel fusion是什么，该怎么学习呢? - 有了琦琦的棍子的回答 - 知乎
https://www.zhihu.com/question/514144710/answer/2491596085


高性能计算工程师需要什么技术堆栈？ opencl dsp neon perf profile tvm？ - 有了琦琦的棍子的回答 - 知乎
https://www.zhihu.com/question/481648758/answer/2206937333

CUDA WarpReduce学习 - zzk again的文章 - 知乎
https://zhuanlan.zhihu.com/p/492560229


GPU硬件的发展与特性分析---Tesla系列汇总 - kaiyuan的文章 - 知乎
https://zhuanlan.zhihu.com/p/515584277


cuda笔记
https://github.com/DefTruth/CUDA-Learn-Note



如何学习cuda编程？ - DefTruth的回答 - 知乎
https://www.zhihu.com/question/62996995/answer/3369541594


[C++][3W字]💡静态链接和静态库实践指北-原理篇 - DefTruth的文章 - 知乎
https://zhuanlan.zhihu.com/p/595527528

推理部署工程师面试题库 - 进击的Killua的文章 - 知乎
https://zhuanlan.zhihu.com/p/673046520


OneFlow技术年货：800+页免费“大模型”电子书 - OneFlow的文章 - 知乎
https://zhuanlan.zhihu.com/p/675561734


[AI编译器后端优化]循环优化 - 守夜人的文章 - 知乎
https://zhuanlan.zhihu.com/p/685444117



理解Tensor Core - Frank Wang的文章 - 知乎
https://zhuanlan.zhihu.com/p/75753718

CUDA Programming model: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html

An Even Easier Introduction to CUDA: https://devblogs.nvidia.com/even-easier-introduction-cuda/

CUSTOM C++ AND CUDA EXTENSIONS: https://pytorch.org/tutorials/advanced/cpp_extension.html


AutoTM: Automatic Tensor Movement in Heterogeneous Memory Systems using Integer Linear Programming

Training Deep Nets with Sublinear Memory Cost

Capuchin: Tensor-based GPU Memory Management for Deep Learning

XLA. https://www.tensorflow.org/xla

TVM: An automated end to-end optimizing compiler for deep learn

Learning to optimize tensor programs

Halide: A language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines.

Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations

Tensor comprehensions: Framework-agnostic high-performance machine learning abstractions.

Akg: Automatic kernel generation for neural processing units using polyhedral transformations.

Ansor: Generating high-performance tensor programs for deep learning.

Flextensor: An automatic schedule exploration and optimization framework for tensor computation on heterogeneous system.


Rammer: Enabling Holistic Deep Learning Compiler Optimizations with rTasks

Juggler: A dependence-aware task-based execution framework for gpus

Clipper: A low-latency online prediction serving system

A study of persistent threads style gpu programming for gpgpu workloads.

Enabling and exploiting flexible task assignment on gpu through sm-centric program transformations.

```

### 深度思考
1. 千卡训练任务下通信开销占比和分析
2. 千卡并行策略下显存开销计算
3. 千卡集群下MFU的预估与优化
4. 如何用1024张显卡训练一个模型
   1. 如何判断候选人有没有千卡GPU集群的训练经验？ - 你的真实姓名的回答 - 知乎 https://www.zhihu.com/question/650979052/answer/3501160453
5. 大规模GPU推理系统
6. 自动推理性能优化 TVM
7. 分布式通信 PS
8. 大规模GPU训练系统
9. 机器学习调度系统

### 命令行
```
nvidia-smi


安装nvcc
apt install nvidia-cuda-toolkit

查看ubuntu版本号
lsb_release -a

Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy




离线安装cuda nvcc
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local
```

### cuda配置
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.02              Driver Version: 560.94         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   38C    P0             10W /   80W |       0MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

```


### paddle验证gpu
```
import paddle


# 打印 PaddlePaddle 版本信息
print("PaddlePaddle 版本信息：", paddle.__version__)

# 判断是否有可用的 GPU
if paddle.device.is_compiled_with_cuda():
    print("GPU 可用")
else:
    print("GPU 不可用")

# 获取当前可用的 GPU 数量
device_count = paddle.device.cuda.device_count()
print("当前可用的 GPU 数量：", device_count)

# 获取当前使用的 GPU 的计算能力
device_capability = paddle.device.cuda.get_device_capability()
print("当前使用的 GPU 的计算能力：", device_capability)

# 获取当前使用的 GPU 的属性
device_properties = paddle.device.cuda.get_device_properties(paddle.get_device())
print("当前使用的 GPU 的属性：", device_properties)

# 获取当前使用的 GPU 名称
device_name = paddle.device.cuda.get_device_name(paddle.get_device())
print("当前使用的 GPU 名称：", device_name)

# 获取所有可用的设备
available_devices = paddle.device.get_available_device()
print("所有可用的设备：", available_devices)

```

### 显卡

```
特斯拉t4：http://detail.zol.com.cn/vga/index1242654.shtml
raven显卡：http://www.fishheadscanada.net/raven-t4/
```

### GPU 和 Cuda关系
1. gpu不是cuda，cuda是gpu的编程语言

```
cuda介绍：https://zhuanlan.zhihu.com/p/34587739
```

### 笔记

```
===================================================================================
bank 冲突，影响访问时间



===================================================================================
cpu gpu混合编程
host device的代码和内存管理 有点类似spark的driver机器和excutor机器

分配host内存，数据初始化
分配device内存，host数据拷贝到device
cuda核函数 在device中计算
返回device的结果
程序结束，释放内存

真的和spark的map reduce思想一模一样
可以做个对比表


===================================================================================
cuda核函数 kernel
__gloabal__ <grid,block>
threadID
返回类型只能是void

===================================================================================
grid block是dim3类型的变量
(x,y,z)结构体变量

dim3 grid(3,2) 6个block
dim3 block(5,3) 15个线程 总共90个线程

dim3 grid(128) 128个block
dim3 block(256) 256个线程 总共128 * 256个线程


===================================================================================
__device__ device上执行
__host__ host上执行
__global__ 异步执行


===================================================================================
一个线程块上的线程是放在同一个流失处理器SM上的


===================================================================================
向量加法


===================================================================================
共享内存
有竞争问题
void __synch 设置屏障点

内存分成bank，bank只是将共享内存划分不同的小内存块
多个线程访问多个bank，如果都没有冲突，那么就是效率最大化了
如果多个线程同时访问一个bank，为了数据一致性，多个线程会变成顺序执行，性能变得很差


===================================================================================
统一(unified)内存分配释放
cudaMallocManaged
cudaFree
cudaMemcpy 内存拷贝

===================================================================================
wrap 是sm的基本执行单位，有32个线程
有独立的指令地址计数器，独立的执行路径
分支结构可能出现死等
线程束中的所有线程在同一周期执行相同指令
极小化命令的分化

===================================================================================
线程块 划分为多个线程束


===================================================================================
规约算法
类似树的结构，比如求和，两两个节点相加求和

每一层的结果需要同步



===================================================================================
充分利用gpu性能
提高浮点数运算
提高内存带宽

让同一个wrap执行一样的指令，不要分化

不要数据访问冲突，改善bank数据访问

优化全局内存访问，在求和的时候，同时访问两个数据

一个wrap是32个线程，当计算的时候不需要32个线程，小于32个线程，可以把计算方式展开
不用循环和相关指令，数据同步

用switch方式，把所有情况都展开出来，不使用for循环做加法

volatile 可以防止编译器提前优化代码，因为共享内存的方面的计算会出现优化的可能性
===================================================================================
优化策略
算法最大化并行执行
优化内存使用
优化编译指令




===================================================================================


===================================================================================
```


## 算子优化
1. TensorFlow Graph Optimizations:https://www.tensorflow.org/guide/graph_optimization
2. Graph Optimizations in ONNX Runtimes: https://onnxruntime.ai/docs/performance/graph-optimizations.html
```



[CUDA 学习笔记] Reduce 算子优化 - PeakCrosser的文章 - 知乎
https://zhuanlan.zhihu.com/p/688610091

英伟达官方文档
https://developer.download.nvidia.cn/assets/cuda/files/reduction.pdf

深入浅出GPU优化系列：reduce优化 - 有了琦琦的棍子的文章 - 知乎
https://zhuanlan.zhihu.com/p/426978026

漫谈高性能计算与性能优化：计算 - 有了琦琦的棍子的文章 - 知乎
https://zhuanlan.zhihu.com/p/688613416


如何看待DeepMind最新的AI系统AlphaTensor可以发现矩阵相乘的求解方法？ - 有了琦琦的棍子的回答 - 知乎
https://www.zhihu.com/question/557880171/answer/2705627296


如何实现一个高效的Softmax CUDA kernel？——OneFlow 性能优化分享 - OneFlow的文章 - 知乎
https://zhuanlan.zhihu.com/p/341059988


高效CUDA Scan算法浅析 - 熊勒个猫的文章 - 知乎
https://zhuanlan.zhihu.com/p/499963645


FasterTransformer Decoding 源码分析(八)-FFNLayer MoE(下篇) - 进击的Killua的文章 - 知乎
https://zhuanlan.zhihu.com/p/672189305

FlashAttention 的速度优化原理是怎样的？ - DefTruth的回答 - 知乎
https://www.zhihu.com/question/611236756/answer/3410300997


CUDA优化之LayerNorm性能优化实践 - OneFlow的文章 - 知乎
https://zhuanlan.zhihu.com/p/443026261

[施工中] CUDA GEMM 理论性能分析与 kernel 优化 - 李少侠的文章 - 知乎
https://zhuanlan.zhihu.com/p/441146275


FlashAttention v2核心代码解析(一） - 进击的Killua的文章 - 知乎
https://zhuanlan.zhihu.com/p/686225377


有没有大模型推理加速引擎FasterTransformer入门级教程？ - 进击的Killua的回答 - 知乎
https://www.zhihu.com/question/602468960/answer/3315182172


flash-attention快速实现
https://github.com/tspeterkim/flash-attention-minimal


ops(2)：SoftMax 算子的 CUDA 实现与优化 - 紫气东来的文章 - 知乎
https://zhuanlan.zhihu.com/p/695307283

```

## 内存优化
### 基于拓扑序的最小内存分配
```
计算图中的张量内存分配可以分成两个部分：张量生命期的分析和内存分配。首先，给定计算图之后，唯一决定张量生命期的就是节点（算子）的执行顺序。在计算框架中，由于执行顺序是运行时决定的，所以内存也都是运行时分配的。但在编译器中，我们可以通过生成固定顺序的代码来保证最终的节点以确定的顺序执行，因此在编译期就可以为所有张量决定内存分配的方案。一般只要以某种拓扑序要遍历计算图就可以生成一个依赖正确的节点的执行顺序，如BFS、Reverse DFS等，进而决定出每个张量的生命期，即分配和释放的时间点。

接下来，就是根据每个张量的分配和释放顺序分配对应的内存空间，使得总内存占用最小。一种常用的内存分配方法是建立一个内存池，由一个块内存分配管理器（如BFC内存分配器）管理起来，然后按照每个张量的分配和释放顺序依次向内存池申请和释放对应大小的内存空间，并记录每个张量分配的地址偏移。当一个张量被释放回内存池时，后续的张量分配就可以自动复用前面的空间。当所有张量分配完时，内存池使用到的最大内存空间即为执行该计算图所需要的最小内存。在真实的运行时，我们只需要在内存中申请一块该大小的内存空间，并按照之前的记录的地址偏移为每个张量分配内存即可。这样即可以优化总内存的占用量，也可以避免运行时的内存分配维护开销。 值得注意的是，不同拓扑序的选择会同时影响模型的计算时间和最大内存占用，同时也强制了运行时算子的执行顺序，可难会带来一定的性能损失。
```

### 张量换入换出
```
上面的方法中只考虑了张量放置在加速器（如GPU）的内存中，而实际上如果内存不够的话，我们还可以将一部分张量放置到外存中（如CPU的内存中），等需要的时候再移动回GPU的内存中即可。虽然从CPU的内存到GPU的内存的拷贝延时和带宽都比较受限，但是因为计算图中有些张量的产生到消费中间会经过较长的时间，我们可以合理安排内存的搬运时机使得其和其它算子的计算重叠起来。
如利用整数线性规划优化计算图内存分配

```

### 张量重计算
```
深度学习计算图的大多算子都是确定性的，即给定相同的输入其计算结果也是相同的。因此，我们可以进一步利用这个特点来优化内存的使用。当我们对连续的多个张量决定换入换出的方案时，如果产生这些张量的算子都具有计算确定性的话，我们可以选择只换出其中一个或一少部分张量，并把剩下的张量直接释放，当到了这些张量使用的时机，我们可以再换入这些少量的张量，并利用确定性的特点重新计算之前被释放的张量，这样就可以一定程序上缓解CPU和GPU之前的贷款压力，也为内存优化提供了更大的空间。如果考虑上换入换出，内存优化方案需要更加仔细的考虑每个算子的执行时间，从而保证重计算出的张量在需要的时候能及时的计算完成。

```
## 内核优化与生成
### 算子表达式
```
对深度学习中的大多数算子，其计算逻辑都可以描述成针对输出张量中的每一个元素的独立同构计算。以矩阵乘算子为例（如图5-4-1所示），矩阵C中的每一个元素（如坐标为[i,j])的值都可以通过对应的一行（第i行）和一列（第j列）的内积来计算得出。也就是说，大多数的算子的计算逻辑都要以通过描述其中的元素的计算逻辑来表示，这就是算子表达式的作用。

矩阵乘	C = t.compute((m, n), lambda i, j: t.sum(A[i, k] * B[k, j]), axis=k)

仿射变换	C = t.compute((m, n), lambda i, j: C[i, j] + bias[i])

卷积	C = t.compute((c, h, w), lambda i, x, y: t.sum(data[kc, x+kx, y+ky] * w[i, kx, ky]), axis=[kx, ky, kc])

ReLU	C = t.compute((m, n), lambda i, j: t.max(0, A[i, j])
```

### 算子表示与调度逻辑的分离
```
有了算子表达式之后，我们就得到了一个算子的计算逻辑。为了生成硬件上的最终代码，我们需要把算子表达式的逻辑计算变化成符合硬件编程模型的代码，并考虑硬件特性进行代码优化，这个过程就叫作表达式的调度（Schedule）。 通常来说，一个最简单的调度方案就是通过生成多重循环来遍历一个算子表达式中输出张量中的每一个元素，然后调用其提供的lambda函数，即可完成一个简单的内核代码的生成。图5-4-2展示了一个简单的张量加算子的表达式，以及为其在TVM中创建一个默认调度的示例（上半部分），同时调度后产生出的内核代码（下半部分）。

```

### 自动调度搜索与代码生成
```
有了算子表达式和对表达式的调度机制，我们就可以较容易的在一个新的硬件设备上生成一个算子的内核代码了。然而，我们可以看到，在调度的时候，有非常多种决定需要抉择，而且这些决定都会根据硬件的不同而产生不一样的性能影响，这些都需要经验非常丰富的专家才能知道一个较好的调度方案。为了进一步克复这个问题，一类利用机器学习进行自动调度搜索的方法被广泛应用。


```

## 并行训练
### 算子内并行
```
算子内并行主要利用线性计算和卷积等操作内部的并行性。通常一个算子包含多个并行维度，常见的例如：批次（Batch）维度（不同的输入样本（Sample））、空间维度（图像的空间划分）、时间维度（RNN网络的时序展开）。在目前主流的深度学习框架中，这些并行的维度通过SIMD架构等多执行单元达到同时并行运算的目的。


```

### 算子间并行
```
算子内并行依然将思考的范围限定在单个算子上。而在深度学习训练中，并行的潜力广泛存在于多个算子之间。根据获得并行的方式，算子间并行的形式主要包含：

数据并行：多个样本并行执行

模型并行：多个算子并行执行

组合并行：多种并行方案组合叠加


NVIDIA Tensor Core GPUs Train BERT in Less Than An Hour

Large Batch Optimization for Deep Learning: Training BERT in 76 minutes (ICLR’20)

Joseph E. Gonzalez AI-Systems Distributed Training
```

### 数据并行
1. https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC6%E7%AB%A0-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%AE%97%E6%B3%95%E4%B8%8E%E7%B3%BB%E7%BB%9F/6.2-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%AE%97%E6%B3%95%E5%88%86%E7%B1%BB.md
2. 不同设备上读取不同数据
3. 执行相同计算图
4. 跨设备聚合梯度
5. 利用聚合后梯度更新模型
```








```


### 模型并行
```


```




### 调度并行
```


```

### 同步并行 类似spark的MR
1. https://ucbrise.github.io/cs294-ai-sys-fa19/assets/lectures/lec06/06_distributed_training.pdf
```
同步并行是采用具有同步障的通信协调并行。例如在下图中，每个工作节点(Worker)的在进行了一些本地计算之后需要与其它工作节点通信协调。在通信协调的过程中，所有的工作节点都必须等全部工作节点完成了本次通信之后才能继续下一轮本地计算。阻止工作节点在全部通信完成之前继续下一轮计算是同步障。这样的同步方式也称BSP，其优点是本地计算和通信同步严格顺序化，能够容易地保证并行的执行逻辑于串行相同。但完成本地计算更早的工作节点需要等待其它工作节点处理，造成了计算硬件的浪费。

```
### 异步并行
```
采用不含同步障的通信协调并行。相比于同步并行执行，异步并行执行下各个工作节点完全采用灵活的方式协调。如下图所示，时间轴上并没有统一的时刻用于通信或者本地计算，而是工作节点各自分别随时处理自己收到的消息，并且随时发出所需的消息，以此完成节点间的协调。这样做的好处是没有全局同步障带来的相互等待开销。



```
### 半同步并行
```
采用具有限定的宽松同步障的通信协调并行。半同步的基本思路是在严格同步和完全不受限制的异步并行之间取一个这种方案——受到限制的宽松同步。例如, 在 Stale Synchronous Parallel (SSP)中，系统跟踪各个工作节点的进度并维护最慢进度，通过动态限制进度推进的范围，保证最快进度和最慢进度的差距在一个预定的范围内。这个范围就称为“新旧差阈值”staleness threshold如下图所示，在新旧差阈值为3时，最快进度的工作节点会停下来等待最慢的工作节点。

```
### 
```


```
### 
```


```


### 分布式框架
```
https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC6%E7%AB%A0-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%AE%97%E6%B3%95%E4%B8%8E%E7%B3%BB%E7%BB%9F/6.4-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%B3%BB%E7%BB%9F%E7%AE%80%E4%BB%8B.md

TensorFlow Distributed Training
TensorFlow ClusterSpec
Fast Distributed Deep Learning over RDMA. (EuroSys'19)
PyTorch Distributed Tutorial
Horovod: fast and easy distributed deep learning in TensorFlow
Horovod on Github
PyTorch MNIST 测试用例
Horovod on GPU
NCCL2 download
OpenMPI

```


### 分布式通信
```
https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC6%E7%AB%A0-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%AE%97%E6%B3%95%E4%B8%8E%E7%B3%BB%E7%BB%9F/6.5-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E7%9A%84%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%B0%83.md

```



### GEMM（矩阵乘）的优化
1. Spmv（稀疏矩阵乘）

## 性能分析
1. 【模型分析】Nsight Systems使用 - Arthur的文章 - 知乎 https://zhuanlan.zhihu.com/p/721868054
2. 【模型分析】Nsight Compute使用入门 - Arthur的文章 - 知乎 https://zhuanlan.zhihu.com/p/721868889
3. 利用Nsight System 和 Nsight Compute进行性能优化分析 - 进击的Killua的文章 - 知乎 https://zhuanlan.zhihu.com/p/673282220
4. 【推理引擎】NN模型部署框架/推理引擎总结 - eyesighting的文章 - 知乎 https://zhuanlan.zhihu.com/p/672617025
5. Optimize softmax cuda kernel https://github.com/Oneflow-Inc/oneflow/pull/4058
6. 【分布式训练技术分享七】聊聊字节 AML 万卡工作 MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs - 无恶不作的文章 - 知乎 https://zhuanlan.zhihu.com/p/684619370
7. 混合输入矩阵乘法的性能优化 - OneFlow的文章 - 知乎 https://zhuanlan.zhihu.com/p/685893061
8. DeepSpeed-FastGen：通过 MII 和 DeepSpeed-Inference 实现 LLM 高吞吐量文本生成 - 微软DeepSpeed的文章 - 知乎 https://zhuanlan.zhihu.com/p/665494115
9. [Transformer 101系列] LLM模型量化世界观(上) - aaronxic的文章 - 知乎 https://zhuanlan.zhihu.com/p/686232369
10. 利用Nsight System 和 Nsight Compute进行性能优化分析 - 进击的Killua的文章 - 知乎 https://zhuanlan.zhihu.com/p/673282220
11. 大白话解说Continous Batching - Gnuey Iup的文章 - 知乎 https://zhuanlan.zhihu.com/p/680123256
```





```



### 
```

```

### 
```


```







## 调度
1. https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC7%E7%AB%A0-%E5%BC%82%E6%9E%84%E8%AE%A1%E7%AE%97%E9%9B%86%E7%BE%A4%E8%B0%83%E5%BA%A6%E4%B8%8E%E8%B5%84%E6%BA%90%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/7.3-%E8%B0%83%E5%BA%A6.md
2. https://www.usenix.org/sites/default/files/conference/protected-files/osdi20_slides_zhao.pdf
3. 群调度（Gang Scheduling)[1] 的 Wiki 定义是：一种用于并行系统的调度算法，用于调度相关线程或进程,在不同处理器上同时启动并运行。
4. 
```
调度（Scheduling）是分配资源以执行任务的动作。在深度学习平台中，资源可以是处理器、GPU、内存等，任务是用户提交的作业。 调度活动（Scheduling Activity）由称为调度器的进程执行。

调度器中的调度算法通常被设计为使所有计算机资源保持忙碌，让多个用户高效地共享系统资源，或实现目标服务质量（Quality-of-Service）。

在运行深度学习作业的集群服务器上，会部署一个“操作系统”进行作业管理与调度，也就是异构资源管理系统，也称作深度学习平台。相比传统操作系统，其特点是，运行的“进程”一般为深度学习作业，所以是一个专有操作系统。管理的资源不仅是一台机器，而是多台服务器构成的集群资源池。每台服务器挂载了多块商用 GPU，InfiniBand 网卡等异构硬件。深度学习平台也是要对作业提供整体所管理的硬件的“一定抽象层次”上的多路复用（Multiplexing）。同时由于整个系统不仅一个用户会提交多个作业，整个资源池被多个公司内部组和用户共享，也就是我们所说的多租（Multi-Tenancy）系统。

Ali Ghodsi, Matei Zaharia, Benjamin Hindman, Andy Konwinski, Scott Shenker, and Ion Stoica. 2011. Dominant resource fairness: fair allocation of multiple resource types. In Proceedings of the 8th USENIX conference on Networked systems design and implementation (NSDI'11). USENIX Association, USA, 323–336.
Hadoop: Capacity Scheduler
Myeongjae Jeon, Shivaram Venkataraman, Amar Phanishayee, unjie Qian, Wencong Xiao, and Fan Yang. 2019. Analysis of large-scale multi-tenant GPU clusters for DNN training workloads. In Proceedings of the 2019 USENIX Conference on Usenix Annual Technical Conference (USENIX ATC '19). USENIX Association, USA, 947–960.

```



### 单作业调度-群调度
```
群调度（Gang Scheduling)[1] 的 Wiki 定义是：一种用于并行系统的调度算法，用于调度相关线程或进程,在不同处理器上同时启动并运行。

深度学习作业通常会持续数小时，有些甚至会持续数周。深度学习作业通常需要群调度，直到所有必需的加速设备都被授予后才能开始训练过程。

如果不使用群调度会产生什么问题? 深度学习作业可以同时执行多个任务，如果有依赖任务没启动，已启动任务会在同步点忙于等待或者频繁上下文切换 (如下图所示)。首先会造成训练任务无法训练，由于等待不能启动的任务，如下图所示两个作业都申请了部分资源，但是还需要其他资源才能启动，产生了死锁现象。同时已启动的任务不释放资源，造成资源浪费。



```

### 作业间调度-主导资源公平 DRF（Dominant Resource Fairness）调度
```
目前深度学习平台其实包含多种异构资源（CPU，GPU，主存等）以及被多用户使用是一个多租的环境。在调度过程中用户会细粒度的申请不同资源的用量，我们在满足用户异构资源需求的同时，也希望在多租的环境下兼顾一定的公平。

问题：包含异构资源类型的系统中如何进行多作业公平（Fairness）的资源调度？
挑战：相比传统单资源公平调度，深度学习作业也需要使用多种异构资源 (CPU，主存等)，并且需要调度 GPU 及 GPU memory


主导资源公平简称DRF（Dominant Resource Fairness）[2]调度使用优势资源的概念来比较多维（CPU，GPU，内存等）资源。这个想法是在多资源环境中，资源分配应该由作业（用户或队列）的主导份额决定，这是作业已分配的任何资源（内存或 CPU）的最大份额。其论文中介绍，与其他可能的策略不同，DRF 满足几个较为理想的属性。

DRF 调度策略的简要总结是：

通过同类型资源在集群整体资源中的份额确定主导资源 (Dominant Resource)。
基于最大最小公平（Max-Min Fairness）的针对多资源类型（例如 GPU，CPU）的调度算法。



```



### 组间作业调度-容量调度（Capacity Scheduling）
```
挑战：相比传统容量调度调度，深度学习作业也需要考虑调度 GPU 及 GPU 显存

容量调度器（Capacity Scheduler）[3]在大数据平台常常作为主流调度器使用，从作业类型角度，大数据作业和深度学习训练作业，都可以看成是批处理作业。它允许多租户安全地共享一个大型集群，以便在分配容量的限制下及时为他们的应用程序分配资源。

所以，容量调度为了支持支持多租（Multi-Tenant）资源共享设计了以下的策略集合：

提升利用率（Utilization）:
虚拟集群（Virtual Cluster）：组能看到视图是虚拟资源，并不绑定具体机器，等作业启动后分配相应的资源，这样有助于提升资源利用率。
层级队列（Hierarchical Queues）: 支持队列分层结构，以确保在允许其他队列使用空闲资源之前在组织的子队列之间共享资源，从而提供更多的控制和可预测性。
队列内可以正交组合其他作业间调度算法，例如，先进先出（FIFO），DRF 等。对异构计算场景，扔可以采用适合多维资源调度或其他自定义调度器。满足下面介绍的约束情况下，仍旧可以采用DRF等调度策略进行具体作业之间的调度与资源分配。
多租与提升公平性（Fairness）:
多租与用户限制因素（User Limit Factor）：
从某种意义上说，队列将分配到网格容量的一小部分，因为它们可以使用一定容量的资源。 提交到队列的所有应用程序都可以访问分配给队列的容量。管理员可以对分配给每个队列的容量配置软限制和可选的硬限制。
允许多用户多组以多租形式使用集群。控制单用户的可以消耗的最大资源，放止占用资源过多，造成其他进程无法申请资源。
弹性（Elasitcity）和 SLA
奖励资源（Bonus Resource）：对其他组没有使用的资源可以临时免费出让给有需要的团队，但是当资源持有者需要，则需要抢占资源归还给持有者。
抢占（Preemption）：配合奖励资源使用，保证对用户提供的服务等级协议（SLA）。

```

### 虚拟集群（Virtual Cluster）机制
```
在集群内，组和用户所看到的的资源配额一般情况下，并没有绑定到具体的物理机器，而是在调度后决定作业部署的物理机器。这背后是通过虚拟集群 (Virtual Cluster) 映射所实现的。而虚拟集群和我们之前介绍的控制组（Cgroups）的设计较为类似。我们会看到很多集群产生的问题，在传统的操作系统中都能找到类似的设计问题与原则。



针对深度学习作业调度的虚拟集群策略可以总结为：

虚拟集群根据小组的配额进行定义
每个租户（Tenant）构成了一个虚拟集群（VC）
资源被分配给租户（Tenant）
将虚拟集群绑定到物理集群

```



### 抢占式调度（Preemptive Scheduling）
```
一些集群管理员为了减少组内空闲资源的浪费，希望通过一定的策略共享虚拟集群内的空闲资源，但是单纯出让资源但是不能保证原有用户随时能回收对应配额资源，产生相应新的问题即不能保证对原用户的 SLA （Service Level Agreement）。这种问题一般可以通过抢占调度解决，也就是当资源的原有用户需要资源时，终止使用奖励资源的作业进程，回收资源给原配额用户。

强占调度一般用于以下场景：

（1）让资源饥饿的作业，或短作业强占一定资源，降低作业的平均响应时间。由于深度学习作业的韧性（Resilience）并不完善，一般不为此类需求使用强占调度。
```
## 负载
1. https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC7%E7%AB%A0-%E5%BC%82%E6%9E%84%E8%AE%A1%E7%AE%97%E9%9B%86%E7%BE%A4%E8%B0%83%E5%BA%A6%E4%B8%8E%E8%B5%84%E6%BA%90%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/7.4-%E9%9D%A2%E5%90%91%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%9A%84%E9%9B%86%E7%BE%A4%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F.md
### 单个深度学习训练作业特点
```
执行时间长：训练时间持续数小时甚至几天。
迭代计算：作业主干部分是迭代的计算，每轮迭代可以切分为小时间窗口的任务。这样让作业本身有机会以更小的任务粒度触发调度和抢占策略。
内存数据量动态变化：在训练过程中不同的时间点做检查点有不同的内存数据量，这给做检查点提供了优化机会。如果有检查点的支持，可以让平台或框架本身支持更加激进的调度策略，例如，动态迁移作业，装箱作业到同一块 GPU，时分复用等。
性能可预测性：资源消耗可预测性，可以通过运行时监控获取。由于其算法为迭代过程且具有一定的可预测性，让调度器有机会可以根据资源消耗做更加优化的作业放置和装箱。

```

### 分布式深度学习训练作业特点
```
对 GPU 拓扑结构敏感：数据并行策略通信传递梯度，模型并行策略通信传递中间结果张量，GPU 与 GPU 之间传输带宽容易形成瓶颈。所以考虑 GPU 亲和性（Affinity）的任务放置策略，对降低分布式训练作业的完工时间有帮助。但会引发新的问题，由于调度是一批 GPU，满足亲和性的同时，可能会产生更多资源碎片。


```

### 批量深度学习训练作业特点
```
反馈驱动探索：自动化机器学习场景下，用户会一次性提交大量的深度学习作业。自动机器学习训练作业的一个关键特征是反馈驱动探索。由于深度学习实验固有的反复试验方法，用户通常会尝试多个作业配置（多项工作），并利用这些工作的早期反馈（准确度，误差等）来决定是否优先考虑或终止其中的某些作业。这种有条件的探索，称为超参数搜索或神经网络结构搜索，可以是手动的，也可以是系统自动调度。所以我们经常可以看到集群中有大量相似作业和被提前取消的作业。

```

### 约束
```
通过以上调度经典算法的脉络，我们可以看到，在深度学习集群调度问题中充满了不同的设计目标的权衡和需要满足的约束，之前我们已经总结过调度算法的设计目标，接下来我们可以总结调度问题设计过程中常常可以追加和需要满足的硬约束（Hard constraint）和软约束（Soft constraint）。

配额（Quota）约束：虚拟集群等多租环境有严格的配额约束保证公平性。保证作业的 GPU，GPU 内存，CPU，主存等资源需要有空闲资源保证能分配给作业使用。此类约束一般可以设计为硬约束（Hard Constraint），需要必须满足。但是可以通过抢占等底层机制的支持，适当放松。
最小资源保证约束：容量调度等场景有虚拟集群的最小资源佩配额约束保证公平性。此类约束一般可以设计为硬约束（Hard Constraint），需要必须满足。
资源局部性（Locality）：GPU 亲和性约束有助于降低分布式或多卡训练作业的通信开销，降低完工时间。此类约束一般可以设计为软约束（Soft Constraint），不需要必须满足。
完工时间约束：例如，保证排队时间低于一定条件，对排队较久或执行时间更短的作业优先调度。此类约束一般可以认为是软约束（Soft Constraint）。

```

### 反应模式（Reactive Mode）
```
类似传统调度器事件驱动的设计，根据不同事件和状态（作业到达（Arrivals）, 离开（Departures）, 失效（Failures））触发调度策略，可以抽象理解其整体策略为一个状态机（State Machine）。


当触发调度时，其使用考虑亲和性（Affinity）的调度策略： 在调度过程中按以下优先级考虑和排序节点进行作业分配，这样能够更多的考虑 GPU 的亲和性和拓扑结构，让深度学习作业减少数据 I/O 的开销，提升性能。 其优先考虑的待分配节点优先级为： “

拥有相同亲和性的节点。
还未标注亲和性的节点。
有不同亲和性的节点。
进行超额订阅（Oversubscription），在有相同亲和性的节点暂停和恢复其他作业。
不满足之前条件，则作业排队等待。 ”



```

### 内省模式（Introspective Mode）
```
装箱 (Bin Packing）：在保证 GPU 显存约束的情况下，根据浮点运算量，将更多的作业装箱到相同 GPU，提升资源利用率。

时分复用（Time Slicing）：利用框架层或底层实现的检查点和恢复机制，多个作业可以通过时分复用，共享单块GPU。我们可以类比于一种粗粒度的进程的上下文切换（Context Switching）机制。

迁移 (Migration）：利用框架层或底层实现的检查点和恢复机制，当有空闲资源或奖励资源，动态迁移作业使用奖励资源，加速训练。当作业需要被抢占以归还资源，迁移作业保证作业之前训练不失效。


利用运行时信息反馈和框架与平台协同设计的调度器工作还有：

基于在线（Online）作业信息反馈，进行调度算法优化设计的调度器 Optimus EuroSys '18[3] 等。
需要框架和平台协同设计提供支持的调度器还有 AntMan OSDI '20[4] 等。

```


## 存储
### 大数据平台存储路线
```
分布式文件系统: 例如，开源人工智能平台 OpenPAI 中采用 Hadoop HDFS[1] 作为存储方案。HDFS 是一种分布式文件系统，最初是作为 Apache Nutch 网络搜索引擎项目的基础设施而构建的，是广泛用于大数据系统的文件系统。它与已有的分布式文件系统有很多相似之处。HDFS 通过副本机制，具有高度容错性，旨在部署在低成本硬件上。HDFS 提供对应用程序数据的高吞吐量访问，适用于拥有大量数据集的应用程序。HDFS 放宽了一些 POSIX 要求，以支持对文件系统数据的流式访问。HDFS 本身适合顺序读写，不适合随机读写，不建议对小文件访问。其主要为主存和磁盘之间数据读写而设计，没有针对 GPU 显存和主存之间的数据读写进行特定支持和优化，这些劣势会造成深度学习负载下的一些性能问题和瓶颈。

```

### 高性能计算平台存储路线
```
网络文件系统（Network File System）：简称 NFS[7] 文件系统是由 Sun 公司研发的网络文件系统，其基本原理是将某个设备本地文件系统通过以太网的方式共享给其它计算节点使用。也就是说，计算机节点通过 NFS 存储的数据是通过网络存储在另外一个设备，而不是存储在本地磁盘。其比较适合在平台部署早期数据量不大的阶段提供文件系统支持，方便部署，技术成熟，访问接口优化，挂载到计算节点提供给算法工程师友好的体验。不足是随着数据量的增长，难以支持更大的存储空间和访问吞吐，同时权限管理需要平台层协同设计进行管理。例如，很多团队小规模平台中或者针对特定的租户部署和采用 NFS 作为存储方案。



利用高速网卡等异构硬件的 HPC 文件系统：Lustre[8]文件系统是高性能计算平台部署最为广泛的商用文件系统。Lustre 是一种并行分布式文件系统，一般用于大规模高性能集群计算场景。Lustre 这个名字是源自 Linux 和集群（Cluster）的组合词。Lustre 原生支持和利用 InfiniBand（IB）高速网卡，可以利用深度学习平台中的 IB 网络，提供更加高效的数据访问。同时支持高性能的 mmap() I/O 调用，容器化的支持与数据隔离，小文件的支持等，一系列的优化使得 Lustre 在人工智能场景也取得了不俗的性能和用户体验。在公有云场景，亚马逊 AWS 也推出了 Amazon FSx 服务，作为一项完全托管的服务，Amazon FSx让用户可以更轻松地将 Lustre 用于存储速度很重要的工作负载。FSx for Lustre 消除了设置和管理 Lustre 文件系统的传统复杂性，使用户能够在几分钟内启动并运行经过测试的高性能文件系统。


```

### 面向深度学习的存储
```
深度学习场景下，首先从硬件来说，内存层级以 GPU 显存为传统主存的地位，硬盘和 GPU 显存之间还有主存中转数据，与 GPU 显存最近的存储并不是像之前和主存交互的块存储设备。
从深度学习作业访存特点是，迭代式执行不断读取一个批次（Batch）的数据，并且访存模式受每轮数据随机洗牌（Shuffle）的影响是随机读取。
从数据结构来看，数据大部分场景下为统一格式规整的张量。同时每次读取的数据并没有像数据库或者大数据系统的针对特定列的过滤机会。
从用户侧用户体验与开发水平的现状出发，用户也更倾向于使用单机文件系统一样通过 FUSE 方式进行数据访问。


高效文件格式（Layout）的设计：一般文件格式有几点设计思路（1）合并为大文件，减少文件数量，减少文件打开开销。（2）减少随机读写转为顺序读写。（3）高效的格式和序列化库，降低序列化与反序列化开销。例如，TFRecord等针对深度学习负载设计的文件格式，将原来多张图片（每个都是一个文件），序列化为一个二进制文件。


并发执行（Concurrent Execution）和并行（Parallel）加载：I/O 和计算形成流水线协同配合，减少 I/O 成为瓶颈的几率，同时利用多核进行并行加载。如图所示，未经优化的数据加载流程，一个训练迭代含有三个阶段：文件打开（Open），迭代每个批次读取（Read）数据和训练（Train）。框架原生支持跨多种数据源并能异步与并行数据加载的高性能数据加载器模块，例如，并发执行的TensorFlow Data API，tf.data。并行执行的PyTorch 数据加载器（Dataloader）。


统一文件系统接口（Unified File System API）与多数据源管理：对用户透明，保持兼容性（例如，POSIX 标准，NFS 标准，HDFS 接口兼容），统一管理多级，多数据源异构存储。

```
## 推理服务
1. 模型被部署为长期运行的服务
2. 推理有更苛刻的资源约束
3. 推理不需要反向传播梯度下降
4. 部署的设备型号更加多样
5. https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC8%E7%AB%A0-%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F/8.1-%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F%E7%AE%80%E4%BB%8B.md
```
提供可以被用户调用的接口
能够完成一定的数据处理将输入处理为输出
能够在指定低延迟要求下返回用户响应
能够利用多样的加速器进行一定的加速
能够随着用户的增长保持高吞吐的服务响应和动态进行扩容
能够可靠的提供服务，应对软硬件的失效
能够支持算法工程师不断更新迭代模型，应对不断变化的新框架


深度学习模型的生命周期（Life Cycle）包含以下几个阶段：首先，需要从存储系统或其他数据源收集和准备训练数据。之后进入训练阶段，开始训练模型，一旦模型满足一定的学习性能（例如，准确度超过 
K
，或者错误率降低到 
M
 以下），则终止训练，并保存模型文件。完成训练之后，模型文件会被优化（例如，压缩，量化等），编译（例如，内核调优与代码生成），加载部署在推理系统中。推理系统对外暴露接口（例如，Http 或 gRPC 等），接收用户请求或系统调用，模型通过推理（Inference）处理完请求后，返回给用户相应的响应结果，完成推理任务。

 训练阶段，深度学习模型常常采用梯度下降算法或类似的优化算法进行模型训练，我们可以将其拆解为三个阶段:
 前向传播（Forward Propagation）过程将输入样本（Sample）计算为输出标签（Label）。
反向传播（Back Propagation）过程求解权重的梯度。
梯度更新（Weight Update）阶段将模型权重通过一定的步长和梯度进行更新。

```
### TensorRT
1. 如何自学TensorRT? - chamber的回答 - 知乎 https://www.zhihu.com/question/567947309/answer/3184968930
2. onnx：https://onnx.ai/

### 组件与结构
1. 请求与响应处理：系统需要序列化与反序列化请求，并通过后端高效执行，满足一定的响应延迟。相比传统的 Web 服务，推理系统常常需要接受图像，文本，音频等非结构化数据，单请求或响应数据量一般更大，这就需要对这类数据有高效的传输，序列化，压缩与解压缩机制。
2. 请求调度：系统可以根据后端资源利用率，动态调整批尺寸，模型的资源分配，进而提升资源利用率，吞吐量。同时如果是通过加速器进行的加速推理，还要考虑主存与加速器内存之间的数据拷贝，通过调度或预取等策略在计算的间歇做好数据的准备。
3. 后端框架执行：框架将请求映射到模型作为输入，并在运行时调度深度学习模型的内核进行多阶段的处理。如果是部署在异构硬件或多样化的环境，还可以利用编译器进行代码生成与内核算子优化，让模型自动化转换为高效的特定平台的可执行的机器码。
4. 模型版本管理：在云端算法工程师不断验证和开发新的版本模型，需要有一定的协议保证版本更新与回滚。定期或满足一定条件的新模型不断上线替换线上模型，以提升推理服务的效果，但是由于有些指标只能线上测试，有可能线上测试效果较差还需要支持回滚机制，让模型能回滚到稳定的旧版本模型。
5. 健康汇报：云端的服务系统应该是可观测的，才能让服务端工程师监控，报警和修复服务，保证服务的稳定性和 SLA。例如，一段时间内响应变慢，通过可观测的日志，运维工程师能诊断是哪个环节成为瓶颈，进而可以快速定位，应用策略，防止整个服务突发性无法响应（例如，OOM 造成服务程序崩溃）。
6. 推理芯片与代码编译：在边缘端等场景会面对更多样的硬件，驱动和开发库，需要通过编译器进行一定代码生成让模型可以跨设备高效运行，并通过编译器实现性能优化。
7. 推理系统和训练系统间可以通过模型库与上线的协议建立起联系，一般训练系统有一套完整的 DevOps 流水线，也被称作 MLOps，在 8.5 章节我们将进行介绍。算法工程师不断在训练流水线中提交模型设计与算法调优的实验，待满足一定的精度需求后，模型进入模型库并触发上线动作。之后就是模型被压缩优化或加载进推理系统了。

```


```

### 推理专有芯片
1. https://github.com/microsoft/AI-System/blob/main/Textbook/%E7%AC%AC8%E7%AB%A0-%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%8E%A8%E7%90%86%E7%B3%BB%E7%BB%9F/8.6-%E6%8E%A8%E7%90%86%E4%B8%93%E6%9C%89%E8%8A%AF%E7%89%87.md
```
CPU 部署：也有很多推理场景选择使用 CPU 推理，其中有几点原因。（1）推理阶段批尺寸小，造成浮点运算量低，常常 CPU 能满足需求。(2) CPU 的 x86 指令集架构和操作系统对软件的管理更加成熟，虚拟化也做的更好，更容易做装箱甚至数据中心混部推理负载。（3）软件栈兼容性更好，减少数据序列化开销。（4）硬件层面减少跨 PCIe 搬运到 GPU 的开销。所以如果 GPU 推理本身延迟和吞吐指标上没能超越现有 CPU，常常推理系统也会选择使用 CPU 进行推理

GPU 部署：如图，相比CPU，NVIDIA 的 GPU 采用 SIMT 的架构，其抽象调度单位为束（Warp），也就是一组线程按 SIMD 模型执行，进一步精简指令流水线让出更多面积放入计算核，同时减少指令访存。同时我们从图中可以看到：“CPU 面向单线程尽可能降低延迟，同时其线程上下文切换一般由软件辅助完成同时要保存寄存器造成访存开销，则其尽可能让当前线程多执行一段，则线程的访存变为了同步等待。GPU则采取另一种设计，在线程要访存的时间窗口让给其他线程，同时由硬件支持线程切换尽可能不产生访存，这样虽然会造成单线程一定拖延（Delay），但是其靠计算屏蔽 I/O（当前线程I/O则切换到其他线程进行计算）的设计，让整体线程的完工时间减低。”这种模式非常适合矩阵运算，假设每个线程完成局部运算，我们只拿一个线程结果没有意义，而是需要整体运算结果，所以我们宁愿单个线程变慢但是整体一批线程更快完成。


ASIC 部署：如图所示，相比 GPU，ASIC 一般可以根据负载特点设计脉动阵列（Systolic Array）架构，其根据负载的数据流特点设计计算器件的排布，让计算单元输入与输出流水线化，减少访存。其在单指令多数据流（SIMD）的基础之上，进一步降低访存，尽量在片上做更多的计算缓存中间结果，这样进一步提升芯片吞吐与降低延迟。我们可以通俗的理解为，将原来指令流水线执行完成单指令后的访存（Memory Access）步骤去掉，连接更多 ALU，或通过片上缓存持续利用当前 ALU，直到不得已才回写内存，这样就将之前的数据流运算尽可能在片上完成。

```

## MLOps
```
    

```

### 
```


```





## 面试
1. 推理部署工程师面试题库 - 进击的Killua的文章 - 知乎 https://zhuanlan.zhihu.com/p/673046520
2. 