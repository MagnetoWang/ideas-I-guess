## GPU解决方案

### 资料
```

[CUDA 学习笔记] GEMM 优化: 双缓冲 (Prefetch) 和 Bank Conflict 解决 - PeakCrosser的文章 - 知乎
https://zhuanlan.zhihu.com/p/696844342


如何系统地学习CUDA？ - Kedreamix的回答 - 知乎
https://www.zhihu.com/question/263832290/answer/3322864217
https://github.com/Kedreamix/pytorch-cppcuda-tutorial


cuda编程示例
https://face2ai.com/program-blog/#GPU%E7%BC%96%E7%A8%8B%EF%BC%88CUDA%EF%BC%89



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



```

### cuda 查看
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

### 并行计算

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

### GEMM（矩阵乘）的优化
1. Spmv（稀疏矩阵乘）

## 性能分析
```


利用Nsight System 和 Nsight Compute进行性能优化分析 - 进击的Killua的文章 - 知乎
https://zhuanlan.zhihu.com/p/673282220


【推理引擎】NN模型部署框架/推理引擎总结 - eyesighting的文章 - 知乎
https://zhuanlan.zhihu.com/p/672617025


Optimize softmax cuda kernel
https://github.com/Oneflow-Inc/oneflow/pull/4058


【分布式训练技术分享七】聊聊字节 AML 万卡工作 MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs - 无恶不作的文章 - 知乎
https://zhuanlan.zhihu.com/p/684619370


混合输入矩阵乘法的性能优化 - OneFlow的文章 - 知乎
https://zhuanlan.zhihu.com/p/685893061



DeepSpeed-FastGen：通过 MII 和 DeepSpeed-Inference 实现 LLM 高吞吐量文本生成 - 微软DeepSpeed的文章 - 知乎
https://zhuanlan.zhihu.com/p/665494115


[Transformer 101系列] LLM模型量化世界观(上) - aaronxic的文章 - 知乎
https://zhuanlan.zhihu.com/p/686232369


```



### 

### 


## TensorRT
1. 如何自学TensorRT? - chamber的回答 - 知乎 https://www.zhihu.com/question/567947309/answer/3184968930
2. onnx：https://onnx.ai/

## 面试
1. 推理部署工程师面试题库 - 进击的Killua的文章 - 知乎 https://zhuanlan.zhihu.com/p/673046520
2. 