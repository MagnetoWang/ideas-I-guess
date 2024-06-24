## Pytorch
### 理解时间
```
2024年2月18号启动

永远带着问题/需求/目标/兴趣/收益看代码

源码理解角度
   横向梳理所有模块
   纵向梳理某个功能点
   编译角度
   使用角度
   性能角度
   底层数据结构角度

完整理解Pytorch项目
如果只是在搜索引擎 搜 Pytorch是远远不够的
Pytorch + 架构图

Pytorch + 概念关键词

Pytorch + 问题排查

Pytorch + 面试汇总

Pytorch + 极客挑战赛

Pytorch + 论坛会议

Pytorch + 论文

Pytorch + 前沿分享

Pytorch + 场景应用

Pytorch + Pytorch大佬名字

Pytorch + 公司项目
等等才能完全熟悉Pytorch





```


### 参考资料
1. PyTorch 2.0 重磅发布：编译、编译、还是编译 https://hyper.ai/news/22891
2. 万字综述，核心开发者全面解读PyTorch内部机制 https://mp.weixin.qq.com/s/8J-vsOukt7xwWQFtwnSnWw
3. 如何提高自己的代码能力以达到熟练使用pytorch? - 王阿骆的回答 - 知乎 https://www.zhihu.com/question/352525266/answer/3395318281
4. PyTorch显存管理介绍与源码解析（一） - kaiyuan的文章 - 知乎 https://zhuanlan.zhihu.com/p/680769942
5. 20天吃透Pytorch https://www.pytorchmaster.com/1-1%2C%E7%BB%93%E6%9E%84%E5%8C%96%E6%95%B0%E6%8D%AE%E5%BB%BA%E6%A8%A1%E6%B5%81%E7%A8%8B%E8%8C%83%E4%BE%8B/
6. Pytorch 模型部署到服务器有没有什么好的方案? - DefTruth的回答 - 知乎 https://www.zhihu.com/question/394121546/answer/2322922488
7. 如何看/学习tensorflow的所有函数C/C++源码？ - DefTruth的回答 - 知乎 https://www.zhihu.com/question/332152176/answer/2285671222
8. Pytorch格式 .pt .pth .bin .onnx 详解 - 薛定谔的问题的文章 - 知乎 https://zhuanlan.zhihu.com/p/620688513
9. 【最全算法工程师面经】工程部署篇 - Alone的文章 - 知乎 https://zhuanlan.zhihu.com/p/689895960
10. pytorch资源：https://zhuanlan.zhihu.com/p/28475866
    1.  attention实现：https://github.com/jadore801120/attention-is-all-you-need-pytorch
    2.  DeepLearningForNLPInPytorch：https://github.com/rguthrie3/DeepLearningForNLPInPytorch
    3.  一个开放领域问答系统DrQA的PyTorch实现：https://github.com/facebookresearch/DrQA
11. PyTorch Metric Learning Overview：https://github.com/KevinMusgrave/pytorch-metric-learning?tab=readme-ov-file



### 源码编译
1. 如何有效地阅读PyTorch的源代码？ - 李辰的回答 - 知乎 https://www.zhihu.com/question/58253344/answer/241864966
2. 
```
镜像
https://github.com/cnstark/pytorch-docker

示例
https://github.com/pytorch/examples


基础镜像docker build
pytorch-linux-focal-cuda12.1-cudnn8-py3-gcc9
https://hud.pytorch.org/pytorch/pytorch/commit/cbeb58b7a354c6d4b98ec1676fe5314a29d6fd90
https://github.com/pytorch/pytorch/actions/runs/7907252100/job/21583884840

action 编译
https://github.com/pytorch/pytorch/actions/runs/7946656440/job/21694626567

```

### ezyang视角下的pytorch
1. 算子
   1. 动态分发
   2. dtype switch double float
2. 硬件
   1. cpu 稀疏cpu
   2. cuda
   3. xla
3. layout
   1. 描述了对物理内存进行逻辑解读的方式。最常用的布局是有步幅的张量（strided tensor），但稀疏张量的布局不同，其涉及到一对张量，一个用于索引，一个用于数据；MKL-DNN 张量的布局更加奇特，比如 blocked layout，仅用步幅不能表示它。
   2. 
4. 自动梯度
5. 并行化device
6. 高效开发流程
   1. 尽量只编辑 cpp 文件，编辑 header 要审慎！
   2. ci镜像 https://github.com/pytorch/ossci-job-dsl
   3. 编译cache https://github.com/pytorch/pytorch/blob/master/CONTRIBUTING.md#use-ccache
   4. 


### 编译顺序 - cmake视角
1. c10
   1. core
   2. util
   3. mobile
2. sleef
   1. sleefdetsse2
   2. sleefsse2
   3. sleefdetavx512f
   4. mkdisp
3. aten
   1. utils
   2. jit
   3. ATen
      1. cpu
      2. detail
      3. functorch
      4. core
      5. native
   4. torch
      1. frontend
      2. onednn

### 编译顺序 - 头文件视角
#### github/pytorch/torch/csrc/api/include/torch/torch.h
```c++
#include <torch/autograd.h>
#include <torch/cuda.h>
#include <torch/data.h>
#include <torch/enum.h>
#include <torch/fft.h>
#include <torch/jit.h>
#include <torch/linalg.h>
#include <torch/mps.h>
#include <torch/nested.h>
#include <torch/nn.h>
#include <torch/optim.h>
#include <torch/serialize.h>
#include <torch/sparse.h>
#include <torch/special.h>
#include <torch/types.h>
#include <torch/utils.h>
#include <torch/version.h>
#include <torch/xpu.h>

```
#### nn层
```c++
#include <torch/nn/cloneable.h>
#include <torch/nn/functional.h>
#include <torch/nn/init.h>
#include <torch/nn/module.h>
#include <torch/nn/modules.h>
#include <torch/nn/options.h>
#include <torch/nn/pimpl.h>
#include <torch/nn/utils.h>


nn.funcional层
#include <torch/nn/functional/batchnorm.h>
#include <torch/nn/functional/conv.h>
#include <torch/nn/functional/distance.h>
#include <torch/nn/functional/dropout.h>
#include <torch/nn/functional/embedding.h>
#include <torch/nn/functional/fold.h>
#include <torch/nn/functional/instancenorm.h>
#include <torch/nn/functional/linear.h>
#include <torch/nn/functional/loss.h>
#include <torch/nn/functional/normalization.h>
#include <torch/nn/functional/padding.h>
#include <torch/nn/functional/pixelshuffle.h>
#include <torch/nn/functional/pooling.h>
#include <torch/nn/functional/upsampling.h>
#include <torch/nn/functional/vision.h>


以 dropout 为例

nn.funcional.dropout层
Tensor feature_alpha_dropout(
    Tensor input,
    double p,
    bool training,
    bool inplace)


下钻到 aten模块 这里有两种功能相同，但是语法不同的函数
at::Tensor feature_alpha_dropout(const at::Tensor & input, double p, bool train)
at::Tensor & feature_alpha_dropout_(at::Tensor & self, double p, bool train)


at::_ops层 是一个结构体
其中 call 函数就是调用函数
目前为止都是 头文件的调用，没有具体实现
确保算子抽象性

struct TORCH_API feature_alpha_dropout {
  using schema = at::Tensor (const at::Tensor &, double, bool);
  using ptr_schema = schema*;
  // See Note [static constexpr char* members for windows NVCC]
  STATIC_CONSTEXPR_STR_INL_EXCEPT_WIN_CUDA(name, "aten::feature_alpha_dropout")
  STATIC_CONSTEXPR_STR_INL_EXCEPT_WIN_CUDA(overload_name, "")
  STATIC_CONSTEXPR_STR_INL_EXCEPT_WIN_CUDA(schema_str, "feature_alpha_dropout(Tensor input, float p, bool train) -> Tensor")
  static at::Tensor call(const at::Tensor & input, double p, bool train);
  static at::Tensor redispatch(c10::DispatchKeySet dispatchKeySet, const at::Tensor & input, double p, bool train);
};



cpp实现
pytorch 自动生成 cpp文件
github/pytorch/build/aten/src/ATen/Operators_0.cpp
github/pytorch/build/aten/src/ATen/Operators_1.cpp
github/pytorch/build/aten/src/ATen/Operators_2.cpp
github/pytorch/build/aten/src/ATen/Operators_3.cpp
github/pytorch/build/aten/src/ATen/Operators_4.cpp

主要是创建op模版 这里看 dispatcher机制章节
// aten::feature_alpha_dropout(Tensor input, float p, bool train) -> Tensor
at::Tensor feature_alpha_dropout::call(const at::Tensor & input, double p, bool train) {
    
    static auto op = create_feature_alpha_dropout_typed_handle();
    return op.call(input, p, train);
}


native具体实现
github/pytorch/aten/src/ATen/native/Dropout.cpp





```
   

## 源码解析 - 横向结构
1. dispatch 机制
2. 算子模版
3. torchgen 原理 github/pytorch/torchgen/packaged/ATen/native/native_functions.yaml


### embedding区别
```

github/pytorch/torch/ao/nn/qat/modules/embedding_ops.py:
  7  
  8: class Embedding(nn.Embedding):
  9      r"""

github/pytorch/torch/ao/nn/quantized/modules/embedding_ops.py:
  69  
  70: class Embedding(torch.nn.Module):
  71      r"""

github/pytorch/torch/ao/nn/quantized/reference/modules/sparse.py:
  8  
  9: class Embedding(nn.Embedding, ReferenceQuantizedModule):
  10      """ A reference quantized Embedding module that fits into the

github/pytorch/torch/nn/modules/sparse.py:
  12  
  13: class Embedding(Module):
  14      r"""A simple lookup table that stores embeddings of a fixed dictionary and size.


github/pytorch/torch/_decomp/decompositions.py:
  1157  @out_wrapper()
  1158: def embedding(
  1159      weight: Tensor,

github/pytorch/torch/_inductor/lowering.py:
  2760  @register_lowering(aten.embedding, type_promotion_kind=None)
  2761: def embedding(weight, indices, padding_idx=-1, scale_grad_by_freq=False, sparse=False):
  2762      assert not sparse

github/pytorch/torch/csrc/jit/runtime/serialized_shape_function_registry.cpp:
  399  )=====")
  400: + std::string(R"=====(def embedding(weight: List[int],
  401      indices: List[int],

github/pytorch/torch/csrc/jit/runtime/symbolic_script.cpp:
  1198  
  1199:         def embedding(weight,
  1200                        indices,

github/pytorch/torch/jit/_shape_functions.py:
  465  
  466: def embedding(
  467      weight: List[int],

github/pytorch/torch/nn/functional.py:
  2153  
  2154: def embedding(
  2155      input: Tensor,

github/pytorch/torch/nn/functional.pyi.in:
  252  def hardswish(input: Tensor, inplace: bool = False) -> Tensor: ...
  253: def embedding(
  254      input: Tensor,

github/pytorch/torch/onnx/symbolic_opset9.py:
  1016  @_beartype.beartype
  1017: def embedding(
  1018      g: jit_utils.GraphContext,




class Embedding(Module):
    num_embeddings: int
    embedding_dim: int
    padding_idx: Optional[int]
    max_norm: Optional[float]
    norm_type: float
    scale_grad_by_freq: bool
    weight: Tensor
    freeze: bool
    sparse: bool


def embedding(
    input: Tensor,
    weight: Tensor,
    padding_idx: Optional[int] = None,
    max_norm: Optional[float] = None,
    norm_type: float = 2.0,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,
) -> Tensor:






```


### torch.distributed & multiprocessing & DistributedDataParallel DDP  分布式分析
```




```


### tensorboard SummaryWriter模型的日志分析工具
```

```


### autugrad
```
torch.autograd.set_detect_anomaly(True)




```
## 横向结构 加减乘除根号平方
1. github/pytorch/build/aten/src/ATen/core/TensorBody.h
2. github/pytorch/build/aten/src/ATen/core/aten_interned_strings.h
3. 
## 横向结构 loss 损失函数
1. Pytorch如何自定义损失函数（Loss Function）？ - 悬鱼铭的回答 - 知乎 https://www.zhihu.com/question/66988664/answer/2809941728
2. 12个必须掌握的Pytorch损失函数 - 汇智网的文章 - 知乎 https://zhuanlan.zhihu.com/p/645453232
3. 19个损失函数汇总，以Pytorch为例 - 极市平台的文章 - 知乎 https://zhuanlan.zhihu.com/p/258395701
4. github/pytorch/torch/nn/functional.py
5. github/pytorch/aten/src/ATen/native/Loss.cpp

### 数学理解
1. BCELoss

### 代码理解
1. poisson_nll_loss
2. binary_cross_entropy_with_logits
3. binary_cross_entropy_cpu
4. huber_loss
5. soft_margin_loss
   1. soft_margin_loss_backward_out
   2. soft_margin_loss_backward
   3. soft_margin_loss_out
6. BCELoss


## 横向结构 op 结构
1. _Ops 所有op加载
   1. github/pytorch/torch/_ops.py
2. github/pytorch/torch/distributed/_tensor/ops
3. github/pytorch/torch/distributed/_tensor/op_schema.py
### torch.ops.fbgemm.asynchronous_complete_cumsum
```

```



####
```

```





## 源码解析 - 纵向结构
1. c10
   1. core
   2. utils
      1. flat_hash_map 结构 github/pytorch/c10/util/flat_hash_map.h 应用于 operatorLookupTable_
      2. LeftRight github/pytorch/c10/util/LeftRight.h 应用于 Dispatcher
      3. 
2. 

## 源码解析 - 测试视角
1. python
2. cpp
   1. 测试各种基础op github/pytorch/test/cpp/api/functional.cpp 
   2. 测试梯度 github/pytorch/test/cpp/api/grad_mode.cpp 
3. cuda

## 项目目录说明
1. torch
   1. python接口封装
   2. csrc python binding
2. aten
   1. tensor 算子实现
   2. 坑 勿看 TH、THC、THNN、THCUNN
3. c10
   1. 核心抽象
4. torchgen
5. functorch
6. tools
   1. pytorch-gdb
   2. Verify-Dynamo


## 开发文档阅读顺序
1. https://pytorch.org/docs/stable/index.html
2. https://pytorch.org/docs/stable/community/contribution_guide.html
3. https://pytorch.org/docs/stable/community/design.html
4. 


## 代码
### c10-core
```


    Allocator.cpp和Allocator.h：实现了内存分配器的相关功能，用于分配和释放张量的内存。

    AutogradState.cpp和AutogradState.h：实现了自动求导状态的管理，包括计算图的构建和反向传播等。

    Backend.h：定义了PyTorch后端的接口和功能，用于支持不同的计算后端，如CPU、CUDA等。

    CPUAllocator.cpp和CPUAllocator.h：实现了CPU内存分配器的相关功能，用于分配和释放CPU张量的内存。

    CompileTimeFunctionPointer.h：定义了编译时函数指针的功能，用于在编译时解析函数指针。

    ConstantSymNodeImpl.cpp和ConstantSymNodeImpl.h：实现了常量符号节点的功能，用于表示计算图中的常量节点。

    Contiguity.h：定义了张量连续性的相关功能，用于判断张量是否是连续存储的。

    CopyBytes.cpp和CopyBytes.h：实现了字节拷贝的功能，用于在张量之间进行数据拷贝。

    DefaultDtype.cpp和DefaultDtype.h：实现了默认数据类型的功能，用于设置和获取默认的张量数据类型。

    DefaultTensorOptions.h：定义了默认张量选项的功能，包括数据类型、设备类型等。

    Device.cpp和Device.h：实现了设备的相关功能，用于表示和管理计算设备，如CPU、CUDA等。

    DeviceArray.h：定义了设备数组的功能，用于在设备上分配和管理内存。

    DeviceGuard.h：定义了设备保护的功能，用于在作用域内设置和恢复设备。

    DeviceType.cpp和DeviceType.h：定义了设备类型的功能，用于表示不同的设备类型，如CPU、CUDA等。

    DispatchKey.cpp和DispatchKey.h：定义了调度键的功能，用于标识和管理不同的调度键。

    DispatchKeySet.cpp和DispatchKeySet.h：定义了调度键集合的功能，用于管理一组调度键。

    DynamicCast.h：定义了动态类型转换的功能，用于在运行时进行类型转换。

    Event.h：定义了事件的功能，用于同步和通信。

    GeneratorImpl.cpp和GeneratorImpl.h：实现了生成器的功能，用于生成随机数。

    GradMode.cpp和GradMode.h：实现了梯度模式的功能，用于控制自动求导的开启和关闭。

    InferenceMode.cpp和InferenceMode.h：实现了推断模式的功能，用于控制模型的推断过程。

    Layout.h：定义了张量布局的功能，用于表示不同的张量布局选项。

    MemoryFormat.h：定义了内存格式的功能，用于表示张量的内存布局。

    OptionalRef.h：定义了可选引用的功能，用于表示可选的对象引用。

    PyHandleCache.h：定义了Python句柄缓存的功能，用于缓存Python对象的句柄。

    QEngine.h：定义了量化引擎的功能，用于支持张量的量化操作。

    QScheme.h：定义了量化方案的功能，用于表示不同的量化方案。

    RefcountedDeleter.cpp和RefcountedDeleter.h：实现了引用计数删除器的功能，用于管理引用计数对象的删除。

    SafePyObject.cpp和SafePyObject.h：实现了安全的Python对象


impl

    COW.cpp和COW.h：实现了写时复制（COW，Copy-on-Write）的功能，用于在多个张量之间共享数据。

    COWDeleter.cpp和COWDeleter.h：实现了写时复制删除器的功能，用于在引用计数降为零时释放共享数据。

    DeviceGuardImplInterface.cpp和DeviceGuardImplInterface.h：定义了设备保护实现接口的功能，用于在设备上设置和恢复保护。

    FakeGuardImpl.h：定义了虚拟保护实现的功能，用于在编译时进行保护。

    GPUTrace.cpp和GPUTrace.h：实现了GPU跟踪的功能，用于记录和分析GPU操作的性能和行为。

    HermeticPyObjectTLS.cpp和HermeticPyObjectTLS.h：实现了Python对象线程本地存储的功能，用于在多线程环境中安全地访问Python对象。

    InlineDeviceGuard.h：定义了内联设备保护的功能，用于在作用域内设置和恢复设备。

    InlineEvent.h：定义了内联事件的功能，用于同步和通信。

    InlineStreamGuard.h：定义了内联流保护的功能，用于在作用域内设置和恢复流。

    LocalDispatchKeySet.cpp和LocalDispatchKeySet.h：实现了本地调度键集合的功能，用于管理本地线程的调度键集合。

    PyObjectSlot.cpp和PyObjectSlot.h：实现了Python对象槽的功能，用于在C++代码中存储和管理Python对象。

    PyInterpreter.cpp和PyInterpreter.h：实现了Python解释器的功能，用于与Python解释器进行交互。

    PythonDispatcherTLS.cpp和PythonDispatcherTLS.h：实现了Python调度器线程本地存储的功能，用于在多线程环境中安全地调度Python函数。

    README-cow.md和README.md：包含关于写时复制功能的说明和文档。

    SizesAndStrides.cpp和SizesAndStrides.h：实现了张量大小和步长的功能，用于描述张量的形状和布局。

    TorchDispatchModeTLS.cpp和TorchDispatchModeTLS.h：实现了Torch调度模式线程本地存储的功能，用于在多线程环境中安全地设置和获取调度模式。


```

### c10-cuda
```


    CUDACachingAllocator.h和CUDACachingAllocator.cpp：实现了CUDA缓存分配器的功能，用于管理CUDA设备上的内存分配和释放。

    CUDADeviceAssertion.h和CUDADeviceAssertionHost.cpp：实现了CUDA设备断言的功能，用于在CUDA设备上进行错误检查和断言。

    CUDAFunctions.cpp和CUDAFunctions.h：实现了CUDA函数的功能，用于调用和执行CUDA相关的操作。

    CUDAGraphsC10Utils.h：定义了与CUDA图相关的功能，用于构建和管理CUDA图。

    CUDAGuard.h：定义了CUDA设备保护的功能，用于在作用域内设置和恢复CUDA设备。

    CUDAMathCompat.h：定义了与CUDA数学函数兼容性相关的功能，用于在不同版本的CUDA上提供一致的数学函数接口。

    CUDAMiscFunctions.cpp和CUDAMiscFunctions.h：实现了一些与CUDA相关的杂项功能，如获取CUDA设备数量、设置CUDA随机种子等。

    CUDAMallocAsyncAllocator.cpp：实现了异步分配器的功能，用于在CUDA设备上异步分配和释放内存。

    CUDAAllocatorConfig.cpp和CUDAAllocatorConfig.h：实现了CUDA分配器配置的功能，用于配置CUDA分配器的行为和选项。

    CUDAException.cpp和CUDAException.h：实现了CUDA异常的功能，用于捕获和处理CUDA运行时错误。

    CUDAStream.cpp和CUDAStream.h：实现了CUDA流的功能，用于管理和同步CUDA操作。

    driver_api.cpp和driver_api.h：实现了CUDA驱动API的功能，用于与CUDA驱动程序进行交互。

    impl：包含了一些内部实现细节的文件。

    test：包含了一些用于测试和验证CUDA相关功能的文件。

    CMakeLists.txt和build.bzl：用于构建和配置PyTorch的构建系统。




    CUDAGuardImpl.cpp和CUDAGuardImpl.h：实现了CUDA设备保护实现的功能，用于在CUDA设备上设置和恢复保护。

    CUDATest.cpp和CUDATest.h：包含了一些用于测试和验证CUDA功能的测试代码。

    cuda_cmake_macros.h.in：包含了一些用于CMake构建系统的CUDA相关宏定义。




    CUDAAssertionsTest_1_var_test.cu：包含了对CUDA断言的测试，测试了对单个变量的断言。

    CUDAAssertionsTest_multiple_writes_from_blocks_and_threads.cu：包含了对CUDA断言的测试，测试了多个线程和块同时写入的情况。

    CUDAAssertionsTest_catches_stream.cu：包含了对CUDA断言的测试，测试了对CUDA流的断言。

    CUDAAssertionsTest_multiple_writes_from_multiple_blocks.cu：包含了对CUDA断言的测试，测试了多个块同时写入的情况。

    CUDAAssertionsTest_catches_thread_and_block_and_device.cu：包含了对CUDA断言的测试，测试了对线程、块和设备的断言。

    CUDAAssertionsTest_multiple_writes_from_same_block.cu：包含了对CUDA断言的测试，测试了同一块中多个线程同时写入的情况。

    CUDAAssertionsTest_from_2_processes.cu：包含了对CUDA断言的测试，测试了来自两个进程的断言。

    CUDATest.cpp：包含了一些用于测试和验证CUDA功能的测试代码。


```

### aten
```
PyTorch Operators篇
https://zasdfgbnm.github.io/2018/06/11/%E4%BB%8E%E5%A4%B4%E5%BC%80%E5%A7%8B%E9%98%85%E8%AF%BBPyTorch%E4%BB%A3%E7%A0%81%20--%20Operators%E7%AF%87/

aten cten torch 关系：https://zhuanlan.zhihu.com/p/55966063#%E8%83%8C%E6%99%AF

ATen的代码生成，是通过gen.py等的Python脚本。根据aten/src/ATen/templates/目录下的文件生成的


ATen.h                     FunctionalStorageImpl.h          ParallelThreadPoolNative.cpp  TypeDefault.h
ATenConfig.cmake.in        FunctionalTensorWrapper.cpp      PythonTorchFunctionTLS.cpp    Utils.cpp
AccumulateType.cpp         FunctionalTensorWrapper.h        PythonTorchFunctionTLS.h      Utils.h
AccumulateType.h           FunctionalizeFallbackKernel.cpp  SavedTensorHooks.cpp          Version.cpp
ArrayRef.h                 Generator.h                      SavedTensorHooks.h            Version.h
Backend.h                  InferSize.h                      Scalar.h                      VmapModeRegistrations.cpp
Backtrace.h                InitialTensorOptions.h           ScalarOps.cpp                 WrapDimUtils.h
CMakeLists.txt             Layout.h                         ScalarOps.h                   WrapDimUtilsMulti.h
CPUApplyUtils.h            LegacyBatchedFallback.cpp        ScalarType.h                  ZeroTensorFallback.cpp
CPUFixedAllocator.h        LegacyBatchedFallback.h          SequenceNumber.cpp            autocast_mode.cpp
CPUGeneratorImpl.cpp       LegacyBatchedTensorImpl.cpp      SequenceNumber.h              autocast_mode.h
CPUGeneratorImpl.h         LegacyBatchedTensorImpl.h        SmallVector.h                 benchmarks
CachedTensorUtils.cpp      LegacyBatchingRegistrations.cpp  SparseCsrTensorImpl.cpp       ceil_div.h
CachedTensorUtils.h        LegacyVmapMode.cpp               SparseCsrTensorImpl.h         code_template.h
CollapseDims.h             LegacyVmapMode.h                 SparseCsrTensorUtils.h        core
Config.h                   LegacyVmapTransforms.cpp         SparseTensorImpl.cpp          cpp_custom_type_hack.h
Config.h.in                LegacyVmapTransforms.h           SparseTensorImpl.h            cpu
ConjugateFallback.cpp      LinalgBackend.h                  Storage.h                     cuda
Context.cpp                MapAllocator.cpp                 StorageUtils.cpp              cudnn
Context.h                  MapAllocator.h                   StorageUtils.h                detail
DLConvertor.cpp            MatrixRef.h                      Tensor.h                      div_rtn.h
DLConvertor.h              MemoryOverlap.cpp                TensorAccessor.h              dlpack.h
Device.h                   MemoryOverlap.h                  TensorGeometry.cpp            function_wrapper.py
DeviceAccelerator.cpp      NamedTensor.h                    TensorGeometry.h              functorch
DeviceAccelerator.h        NamedTensorUtils.cpp             TensorIndexing.cpp            hip
DeviceGuard.h              NamedTensorUtils.h               TensorIndexing.h              jit_macros.h
DimVector.h                NestedTensorImpl.cpp             TensorIterator.cpp            jiterator_macros.h
Dimname.h                  NestedTensorImpl.h               TensorIterator.h              metal
Dispatch.cpp               NumericUtils.h                   TensorIteratorInternal.h      miopen
Dispatch.h                 OpMathType.h                     TensorMeta.cpp                mkl
Dispatch_v2.h              OpaqueTensorImpl.h               TensorMeta.h                  mps
DynamicLibrary.cpp         PTThreadPool.h                   TensorNames.cpp               native
DynamicLibrary.h           PadNd.h                          TensorNames.h                 nnapi
EmptyTensor.cpp            Parallel-inl.h                   TensorOperators.h             ops
EmptyTensor.h              Parallel.h                       TensorOptions.h               quantized
ExpandBase.h               ParallelCommon.cpp               TensorSubclassLikeUtils.h     record_function.cpp
ExpandUtils.cpp            ParallelFuture.h                 TensorUtils.cpp               record_function.h
ExpandUtils.h              ParallelNative.cpp               TensorUtils.h                 templates
Formatting.h               ParallelNative.h                 ThreadLocalPythonObjects.cpp  test
FuncTorchTLS.cpp           ParallelNativeTBB.cpp            ThreadLocalPythonObjects.h    vulkan
FuncTorchTLS.h             ParallelNativeTBB.h              ThreadLocalState.cpp          xpu
FunctionalInverses.cpp     ParallelOpenMP.cpp               ThreadLocalState.h
FunctionalStorageImpl.cpp  ParallelOpenMP.h                 TracerMode.h




```


### aten - torchgen
1. PyTorch ATen代码的动态生成 - Gemfield的文章 - 知乎https://zhuanlan.zhihu.com/p/55966063
2. 重要文件
   1. native_functions.yaml：所有算子注册基本信息和分发能力
      1. https://zhuanlan.zhihu.com/p/349560723
   2. tags.yaml：有的算子会打标签 比如dropout 标签nondeterministic_seeded
      1. nondeterministic_seeded 
      2. This tag indicates if an operator is nondeterministically seeded(i.e., is random) such that the operator intentionally produces   different results when run twice on the same inputs, but this randomnessis controlled by a Generator which, if reseeded would give you the same result.
      3. RegisterSchema.cpp
         1. @generated by torchgen/gen.py from RegisterSchema.cpp
      4. 
```
算子注册层面
gen.py生产多个文件
dropoout为例
github/pytorch/build/aten/src/ATen/ops/feature_alpha_dropout_native.h
github/pytorch/build/aten/src/ATen/ops/feature_alpha_dropout_ops.h
github/pytorch/build/aten/src/ATen/ops/feature_alpha_dropout.h

native文件自动生成的巨多
github/pytorch/build/aten/src/ATen/ops/native_dropout.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_ops.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_native.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward_compositeexplicitautograd_dispatch.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward_cpu_dispatch.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward_cuda_dispatch.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward_native.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward_ops.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_backward.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_compositeexplicitautograd_dispatch.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_cpu_dispatch.h
github/pytorch/build/aten/src/ATen/ops/native_dropout_cuda_dispatch.h

其中 feature_alpha_dropout 和 feature_alpha_dropout_ops 用于 dispatch
feature_alpha_dropout_native 
cpu具体实现映射dropout
github/pytorch/aten/src/ATen/native/Dropout.cpp

cuda具体实现映射dropout
github/pytorch/aten/src/ATen/native/cuda/Dropout.cu






```

### python
1. ops
   1. cpp github/pytorch/torch/include/ATen/ops
   2. python 
2. 

#### ops
```
github/pytorch/torch/nn/qat/modules/embedding_ops.py
github/pytorch/torch/nn/quantized/modules/embedding_ops.py

./distributed/_tensor/ops/pointwise_ops.py
./distributed/_tensor/ops/matrix_ops.py
./distributed/_tensor/ops/math_ops.py
./distributed/_tensor/ops/tensor_ops.py
./distributed/_tensor/ops/conv_ops.py
./distributed/_tensor/ops/experimental_ops.py
./distributed/_tensor/ops/embedding_ops.py
./distributed/_tensor/ops/view_ops.py
./distributed/_tensor/ops/random_ops.py
./distributed/_spmd/experimental_ops.py


fbgemm
github/pytorch/torch/ao/quantization/backend_config/fbgemm.py
torch.ops.fbgemm.asynchronous_complete_cumsum


from torch.ao.nn.quantized.modules.embedding_ops import Embedding
from torch.ao.nn.qat.modules.embedding_ops import Embedding


```

### TorchDynamo
TorchDynamo, a Python frame evaluation tool capable of speeding up existing eager-mode PyTorch programs with minimal user intervention.


### torch_function and torch_dispatch 


### dispatch 机制
```
代码路径
核心实现
github/pytorch/aten/src/ATen/core/dispatch/Dispatcher.cpp

大量调用 dispatch
github/pytorch/build/aten/src/ATen/Operators_1.cpp





Pytorch 源码 Detail 系列】Pytorch 中 dispatch 机制及其实现 - 百夫长的文章 - 知乎 https://zhuanlan.zhihu.com/p/386876377

```



## issue
前置准备
1. how to contributing：https://github.com/pytorch/pytorch/blob/5030913d6aed153afe45c9d9bcb6145093eb5629/CONTRIBUTING.md
2. good first issue：https://github.com/pytorch/pytorch/contribute
3. fork代码
4. pmc建议：一文搞懂 PyTorch 内部机制 - 忆臻的文章 - 知乎 https://zhuanlan.zhihu.com/p/338256656
5. ai = cuda：只有偏执才能生存 – 记录这些年我在PyTorch优化项目上的历程 - Mingfei的文章 - 知乎 https://zhuanlan.zhihu.com/p/634236541
6. 

### 编译和单元测试
```

编译参考
机器学习解决方案

代码补全
PyTorch will generate a compile_commands.json file

单元测试参考
python test/run_test.py
python test/test_jit.py
python test/test_jit.py TestJit.test_Sequential


cpp
./build/bin/FILENAME --gtest_filter=TESTSUITE.TESTNAME
./build/bin/test_jit --gtest_filter=ContainerAliasingTest.MayContainAlias


Profiling with py-spy
pip install py-spy
py-spy record -o profile.svg --native -- python test_tensor_tensor_add.py


ci开发
https://github.com/pytorch/pytorch/wiki/Dev-Infra-Office-Hours

```


## test - 从测试用例看pytorch

### HowToWriteTestsUsingFileCheck.md
```
用于验证ir 和 cse文件格式

CSE（Common Subexpression Elimination）：CSE是一种优化技术，用于消除重复的计算。在计算图中，当多个操作具有相同的输入时，CSE可以识别并消除这些重复的计算，从而减少计算量和内存消耗。通过使用CSE，可以提高计算效率并减少重复计算的开销。

IR（Intermediate Representation）：IR是一种中间表示形式，用于在编译过程中表示计算图。在PyTorch中，计算图是通过IR来表示的，它是一种抽象的表示形式，可以将计算图转换为可以在不同硬件上执行的代码。IR可以提供更高级别的抽象，以便进行优化和转换，从而生成更高效的代码。


什么是contentstore
在PyTorch中，ContentStore是一个用于存储和管理模型的中间结果的类。它是PyTorch的一项实验性功能，旨在帮助优化内存使用和模型训练的效率。

ContentStore通过将模型的中间结果保存在内存中，避免了重复计算这些结果的开销。在模型训练过程中，ContentStore可以在需要时自动缓存和重用中间结果，从而减少计算量和内存使用。

ContentStore可以在PyTorch的上下文管理器中使用，以控制缓存的范围和生命周期。例如，可以使用torch.utils.checkpoint函数将具有ContentStore的模型包装起来，以在需要时自动缓存中间结果。

需要注意的是，ContentStore是一个实验性功能，可能在将来的PyTorch版本中发生变化或被移除。因此，在使用ContentStore时，建议参考PyTorch官方文档以获取最新的信息和使用方法。



什么是aot
在PyTorch中，AOT（Ahead-of-Time）是指在运行时之前对模型进行编译和优化的过程。AOT编译可以提前将模型转换为可执行的机器代码，以便在运行时进行快速的推理或执行。

AOT编译通常包括以下步骤：

模型定义：定义深度学习模型的结构和参数。

模型优化：对模型进行各种优化，例如剪枝、量化和融合等，以减少模型的计算量和内存占用。

模型编译：将优化后的模型转换为可执行的机器代码。这通常涉及将模型转换为特定的硬件或平台的指令集。

通过AOT编译，可以将模型的推理过程提前进行优化和准备，从而在实际运行时获得更快的推理速度和更低的资源消耗。这对于在嵌入式设备或边缘计算环境中部署深度学习模型非常有用。




pytorch中什么是mps
在PyTorch中，MPS（Memory Pooling System）是指一种用于管理GPU内存的技术。MPS允许多个GPU程序共享同一块GPU内存，从而提高GPU的利用率和性能。

MPS通过将GPU内存划分为多个子内存池，并为每个子内存池分配独立的GPU上下文，实现了多个GPU程序之间的内存隔离。这样，即使多个GPU程序同时运行，它们之间也可以共享同一块GPU内存，而不会相互干扰。

具体来说，MPS通过以下方式提高GPU内存的利用率和性能：

内存共享：多个GPU程序可以在同一块GPU内存上进行操作，从而避免了不必要的内存复制和数据传输。

内存复用：MPS可以在不同的GPU程序之间动态分配和回收内存，以满足各个程序的需求，避免了内存碎片化和浪费。

内存管理：MPS负责管理GPU内存的分配和释放，以及内存的回收和重用，从而提供更高效的内存管理和调度。

需要注意的是，MPS是NVIDIA CUDA的一个特性，而不是PyTorch的特定功能。要使用MPS，你需要安装和配置NVIDIA驱动程序和CUDA运行时，并在系统上启用MPS。





pytorch中什么是dispatcher
在PyTorch中，Dispatcher是一个用于分派函数调用的机制。它用于根据输入的参数类型和形状，选择合适的函数来执行操作。

Dispatcher的主要作用是根据函数的输入参数类型和形状，选择匹配的特定函数进行调用。通过Dispatcher，PyTorch能够根据输入的参数类型和形状，自动选择最适合的函数进行计算，从而提高代码的灵活性和效率。

Dispatcher的工作原理如下：

注册函数：在PyTorch中，每个操作（如加法、乘法等）都有一个对应的函数。这些函数会被注册到Dispatcher中，以便根据输入参数的类型和形状进行匹配。

参数匹配：当调用某个操作时，Dispatcher会根据输入参数的类型和形状，寻找最匹配的函数。它会根据参数的类型、形状和其他属性，使用一定的规则进行匹配。

函数调用：一旦找到匹配的函数，Dispatcher会调用该函数来执行操作。函数的具体实现可能会根据不同的设备和硬件进行优化，以提高计算效率。

通过Dispatcher，PyTorch能够根据输入参数的类型和形状，智能地选择最适合的函数进行计算。这使得PyTorch能够处理各种类型和形状的输入，从而提供了更大的灵活性和可扩展性。

需要注意的是，Dispatcher是PyTorch内部的一个机制，通常不需要直接使用或操作Dispatcher。它在PyTorch的底层中起到了重要的作用，使得PyTorch能够提供高效且灵活的计算能力。


pytorch中什么是dlpack
在PyTorch中，DLPack（Deep Learning Pack）是一个用于在不同深度学习框架之间传递张量数据的标准化接口。它提供了一种统一的方式来表示和传递张量数据，使得不同框架之间可以无缝地交互和共享数据。

DLPack的设计目标是提供一个轻量级的、与框架无关的张量表示，以便在不同的深度学习框架之间进行数据传递。它定义了一组规范和接口，用于描述和传递张量的元数据和内存布局。

使用DLPack，可以将PyTorch中的张量数据转换为DLPack格式，并将其传递给其他深度学习框架，如TensorFlow、MXNet等。同样地，也可以接收其他框架中的DLPack数据，并将其转换为PyTorch的张量进行处理。

DLPack提供了以下主要的数据结构和函数：

DLManagedTensor：表示一个被管理的张量，包含了张量的元数据和指向内存的指针。

DLTensor：表示一个张量的元数据，包含了张量的数据类型、形状、内存布局等信息。

dlpack.from_torch：将PyTorch的张量转换为DLPack格式。

dlpack.to_torch：将DLPack格式的张量转换为PyTorch的张量。

通过DLPack，不同的深度学习框架可以共享和交互张量数据，从而实现跨框架的数据传递和集成。这对于深度学习领域的研究和应用具有重要的意义，使得不同框架之间的合作和互操作变得更加容易和高效。





pytorch中什么是itt
在PyTorch中，"ITT" 是 Intel Trace Analyzer and Collector 的缩写。ITT 是一个用于性能分析和调试的工具集，由英特尔开发和提供。它为开发者提供了一组API和工具，用于收集和分析应用程序的性能数据。

ITT 提供了一种可嵌入到应用程序中的轻量级API，开发者可以使用该API在应用程序中插入标记，以便在运行时收集各种性能数据。这些数据包括函数调用、内存访问、线程活动等，可以用于分析应用程序的性能瓶颈和优化机会。

通过使用ITT，开发者可以在应用程序中插入标记，然后使用 Intel Trace Analyzer and Collector 工具对标记的应用程序进行分析。这个工具可以可视化和分析收集到的性能数据，帮助开发者理解应用程序的行为和性能瓶颈，并提供优化建议。

ITT 在 PyTorch 中的应用主要是为了帮助开发者进行性能分析和调试，以优化深度学习模型的训练和推理过程。通过使用ITT，开发者可以更好地理解和优化 PyTorch 应用程序的性能，提高训练和推理的效率。







pytorch中什么是jit fuse
在PyTorch中，"JIT fuse" 是指将多个操作融合（fuse）为一个更高效的操作的过程。这个过程是由JIT（即Just-in-Time）编译器执行的，它可以在运行时对PyTorch的计算图进行优化。

JIT融合的主要目标是减少计算图中的操作数量，从而提高计算的效率。当多个操作可以被合并为一个更大的操作时，可以减少内存访问和计算的开销，并且可以利用硬件的并行性和向量化指令来加速计算。

JIT融合通常应用于一些常见的操作序列，例如卷积和激活函数的组合。通过将这些操作融合为一个更大的操作，可以减少内存传输和计算的次数，从而提高计算的效率。

在PyTorch中，JIT融合可以通过使用torch.jit.script装饰器或者torch.jit.trace函数来实现。这些功能会将计算图转换为JIT表示，并尝试自动进行融合优化。此外，PyTorch还提供了一些手动控制融合的选项，例如使用torch.jit.optimize_cudnn函数来控制卷积和激活函数的融合。

JIT融合可以显著提高计算的效率，特别是在深度学习模型中，其中存在大量的操作序列。通过优化计算图，可以减少不必要的开销，从而加速模型的训练和推理过程。





外积和内积有什么区别，怎么理解
外积（outer product）和内积（inner product）是两种在向量空间中的运算，它们有不同的定义和应用。

1. 内积（Inner Product）：
   内积是两个向量之间的一种运算，也称为点积（dot product）。对于两个向量 a 和 b，内积的计算方式是将对应位置的元素相乘，并将所有乘积相加。内积的结果是一个标量（scalar），表示两个向量之间的相似度或相关性。

   内积的计算方式可以表示为：
   $$\text{inner}(a, b) = \sum_{i=1}^{n} a_i \cdot b_i$$

   内积有很多应用，例如计算向量的长度（模长）、计算两个向量之间的夹角、计算投影、计算相似度等。

2. 外积（Outer Product）：
   外积是两个向量之间的一种运算，也称为张量积（tensor product）。对于两个向量 a 和 b，外积的计算方式是将 a 中的每个元素分别与 b 中的每个元素相乘，得到一个矩阵。外积的结果是一个矩阵，其维度由两个向量的维度确定。

   外积的计算方式可以表示为：
   $$\text{outer}(a, b) = \begin{bmatrix} a_1 \cdot b_1 & a_1 \cdot b_2 & \cdots & a_1 \cdot b_m \\ a_2 \cdot b_1 & a_2 \cdot b_2 & \cdots & a_2 \cdot b_m \\ \vdots & \vdots & \ddots & \vdots \\ a_n \cdot b_1 & a_n \cdot b_2 & \cdots & a_n \cdot b_m \end{bmatrix}$$

   外积在向量和矩阵的计算中有广泛的应用，例如计算协方差矩阵、进行多项式拟合、计算叉乘等。

总结来说，内积是将两个向量的对应位置元素相乘后相加得到一个标量，而外积是将一个向量的元素与另一个向量的所有元素相乘得到一个矩阵。内积用于衡量向量之间的相似度，而外积用于表示向量之间的关系或进行更复杂的计算。



pytorch中什么是MetaConverter
在PyTorch中，MetaConverter 是一个类，用于定义和管理张量之间的数据类型转换。它是PyTorch的内部类，用于支持张量之间的数据类型转换操作。

MetaConverter 类的主要作用是在运行时处理和管理张量的数据类型转换。它提供了一些方法和属性，用于执行类型转换、检查和验证类型转换的合法性，并提供了一些辅助功能来处理不同类型之间的转换逻辑。

在PyTorch中，MetaConverter 类通常与其他类（如 Tensor 类）一起使用，以支持张量之间的数据类型转换。它是PyTorch内部的一部分，用于处理张量的数据类型转换的细节。

需要注意的是，MetaConverter 类是PyTorch内部的实现细节，一般情况下不需要直接使用或操作它。它主要用于支持PyTorch的高级功能，如自动类型转换和混合精度计算。对于一般的张量操作，PyTorch会自动处理类型转换，无需手动操作 MetaConverter 类。




pytorch中什么是mha
在PyTorch中，MHA（Multi-Head Attention，多头注意力）是一种用于构建自注意力机制的模块。自注意力机制是一种用于处理序列数据的机制，它能够在序列中的不同位置之间建立关联，并着重关注与当前位置相关的信息。

MHA模块主要由以下几个组件组成：

Query（查询）：用于表示当前位置的信息，通常是通过线性变换得到的。

Key（键）和Value（值）：用于表示序列中其他位置的信息，也是通过线性变换得到的。Key和Value可以看作是提供上下文信息的参考。

Attention（注意力）：通过计算Query和Key之间的相似度，得到一个权重分布，用于对Value进行加权求和。这样，模块就可以聚焦于与当前位置最相关的信息。

多头（Multi-Head）：为了增加模块的表达能力和泛化能力，通常会使用多个独立的注意力头。每个注意力头都具有独立的Query、Key和Value，通过并行计算得到多个不同的权重分布。最后，将多个注意力头的输出进行合并，得到最终的输出。

MHA模块在自然语言处理（NLP）和计算机视觉（CV）等领域中得到广泛应用。在Transformer模型中，MHA被用于编码器和解码器中，用于对输入序列和输出序列进行自注意力计算，以捕捉序列中的关联信息。

在PyTorch中，可以使用torch.nn.MultiheadAttention类来实现MHA模块。该类提供了一个高级接口，可以方便地构建和使用MHA模块。



pytorch中什么是Scatter 和 Gather
在PyTorch中，scatter和gather是两个用于在张量之间复制和收集数据的函数。

scatter函数：scatter函数用于将一个源张量（source tensor）中的数据按照指定的索引，复制到目标张量（target tensor）的指定位置上。它的函数签名如下：

python
torch.scatter(input, dim, index, src)
其中，input是目标张量，dim是指定的维度，index是用于指定位置的索引张量，src是源张量，用于提供要复制的数据。

例如，可以使用scatter函数将源张量的数据按照索引复制到目标张量的指定位置上。

gather函数：gather函数用于从目标张量中收集指定位置的数据，形成一个新的张量。它的函数签名如下：

python
torch.gather(input, dim, index)
其中，input是目标张量，dim是指定的维度，index是用于指定位置的索引张量。

例如，可以使用gather函数从目标张量的指定位置收集数据，形成一个新的张量。

这两个函数在处理需要根据索引复制或收集数据的情况下非常有用。它们在很多情况下都可以用于数据的重排、排序和分发等操作。

需要注意的是，scatter和gather函数的索引张量（index）的形状和目标张量（input）的形状需要满足一定的条件，以确保正确的复制和收集。具体的使用方法和示例可以参考PyTorch的官方文档和示例代码。




pytorch中什么是SegmentReductions
在PyTorch中，SegmentReductions是一种用于分段聚合操作的函数。它允许对张量的不同段（segments）进行聚合操作，其中每个段可以是连续的一部分或离散的索引。

SegmentReductions提供了以下几种分段聚合操作：

torch.segment_sum(input, segment_ids): 对输入张量的不同段进行求和操作。

torch.segment_mean(input, segment_ids): 对输入张量的不同段进行求平均值操作。

torch.segment_prod(input, segment_ids): 对输入张量的不同段进行求积操作。

torch.segment_min(input, segment_ids): 对输入张量的不同段进行求最小值操作。

torch.segment_max(input, segment_ids): 对输入张量的不同段进行求最大值操作。

这些函数的参数包括：

input: 输入张量，需要进行分段聚合操作的张量。
segment_ids: 分段标识张量，用于指定输入张量中的每个元素属于哪个段。segment_ids的形状应与input的形状相同，每个元素的值表示对应元素所属的段的索引。
这些分段聚合操作在处理序列数据、图数据等需要对不同段进行聚合的场景中非常有用。例如，在自然语言处理中，可以使用segment_sum操作对不同句子的词向量进行求和，以获得句子级别的表示。

需要注意的是，SegmentReductions函数在PyTorch中是作为非标准操作存在的，因此在使用时需要确保PyTorch版本兼容，并参考官方文档和示例代码以正确使用这些函数。





pytorch中什么是Stateless
在PyTorch中，"stateless"（无状态）通常用于描述一些函数或操作，这些函数或操作不包含任何内部状态或可变状态，其输出只取决于输入参数。这意味着给定相同的输入，无状态函数或操作总是产生相同的输出，而不受之前的计算状态或上下文的影响。

在深度学习中，无状态操作对于实现可重复性、可并行性和可移植性非常重要。无状态操作不依赖于任何额外的状态信息，因此可以轻松地在不同的设备上运行，并且可以更容易地进行模型的分布式训练和推理。

PyTorch中的许多函数和操作都是无状态的，例如激活函数（如ReLU、Sigmoid）、归一化操作（如Batch Normalization）和池化操作（如Max Pooling、Average Pooling）等。这些操作的输出只取决于输入，不受模型的训练过程或其他上下文的影响。





pytorch中什么是Vulkan
Vulkan是一种跨平台的图形和计算API（Application Programming Interface，应用程序编程接口），由Khronos Group开发。它提供了高性能的图形渲染和通用计算功能，可以用于游戏开发、图形应用程序和科学计算等领域。

在PyTorch中，Vulkan被用作一种后端（backend）选项，用于加速深度学习模型的训练和推理。通过使用Vulkan后端，PyTorch可以利用GPU的计算能力和并行性，提供更快的模型执行速度和更高的效率。

Vulkan后端的主要优势包括：

高性能：Vulkan是一种底层的图形和计算API，可以直接与GPU硬件交互，提供更低的驱动开销和更高的并行性，从而实现更高的性能。

跨平台：Vulkan是跨平台的，可以在多种操作系统和硬件平台上运行，包括Windows、Linux、Android等。

易于扩展：Vulkan提供了灵活的扩展机制，可以根据需要添加新的功能和特性，以满足不同应用程序的需求。

要在PyTorch中使用Vulkan后端，需要安装Vulkan驱动和相关的PyTorch扩展库。具体的安装和配置步骤可以参考PyTorch官方文档和相关资源。

需要注意的是，Vulkan后端并不适用于所有的硬件和操作系统，它的使用和性能也受到硬件和驱动的限制。在选择使用Vulkan后端时，需要根据具体的硬件和应用场景进行评估和测试。



pytorch中什么是dynamo






```



### linalg 线性代数
```



```

### linear
```
import torch
class LinearMod(torch.nn.Linear):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def forward(self, input):
        return torch._C._nn.linear(input, self.weight, self.bias)

print(torch.jit.trace(LinearMod(20, 20), torch.rand([20, 20])).graph)


graph(%self : __torch__.LinearMod,
      %input : Float(20, 20, strides=[20, 1], requires_grad=0, device=cpu)):
  %bias : Tensor = prim::GetAttr[name="bias"](%self)
  %weight : Tensor = prim::GetAttr[name="weight"](%self)
  %6 : Float(20, 20, strides=[20, 1], requires_grad=1, device=cpu) = aten::linear(%input, %weight, %bias) # /docker/root/projects/demo/github/pytorch/test/linear.py:7:0
  return (%6)


```


### cuda


## 自定义网络结构和模型
### pytorch
1. 官方：https://pytorch.org/docs/stable/notes/modules.html
2. 手写 vs torch vs torch autograd vs nn：https://blog.csdn.net/jiangchao98/article/details/114538161
3. 使用Module类来自定义模型：https://blog.csdn.net/qq_27825451/article/details/90550890

#### LeNet
```
import torch
 
class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()  # 第一句话，调用父类的构造函数
        self.conv1 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.relu1=torch.nn.ReLU()
        self.max_pooling1=torch.nn.MaxPool2d(2,1)
 
        self.conv2 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.relu2=torch.nn.ReLU()
        self.max_pooling2=torch.nn.MaxPool2d(2,1)
 
        self.dense1 = torch.nn.Linear(32 * 3 * 3, 128)
        self.dense2 = torch.nn.Linear(128, 10)
 
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.max_pooling1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.max_pooling2(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x
 
model = MyNet()
print(model)


```


### paddle
1. paddle：https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/advanced/layer_and_model_cn.html#layer
2. 使用 paddle.nn.Sequential 组网
3. 使用 paddle.nn.Layer 组网
4. transformer实现：https://zhuanlan.zhihu.com/p/446809976

#### LeNet
```
from paddle import nn

# 使用 paddle.nn.Sequential 构建 LeNet 模型
lenet_Sequential = nn.Sequential(
    nn.Conv2D(1, 6, 3, stride=1, padding=1),
    nn.ReLU(),
    nn.MaxPool2D(2, 2),
    nn.Conv2D(6, 16, 5, stride=1, padding=0),
    nn.ReLU(),
    nn.MaxPool2D(2, 2),
    nn.Flatten(),
    nn.Linear(400, 120),
    nn.Linear(120, 84), 
    nn.Linear(84, 10)
)
# 可视化模型组网结构和参数
paddle.summary(lenet_Sequential,(1, 1, 28, 28))


---------------------------------------------------------------------------
 Layer (type)       Input Shape          Output Shape         Param #    
===========================================================================
   Conv2D-3       [[1, 1, 28, 28]]      [1, 6, 28, 28]          60       
    ReLU-3        [[1, 6, 28, 28]]      [1, 6, 28, 28]           0       
  MaxPool2D-3     [[1, 6, 28, 28]]      [1, 6, 14, 14]           0       
   Conv2D-4       [[1, 6, 14, 14]]     [1, 16, 10, 10]         2,416     
    ReLU-4       [[1, 16, 10, 10]]     [1, 16, 10, 10]           0       
  MaxPool2D-4    [[1, 16, 10, 10]]      [1, 16, 5, 5]            0       
   Flatten-1      [[1, 16, 5, 5]]          [1, 400]              0       
   Linear-4          [[1, 400]]            [1, 120]           48,120     
   Linear-5          [[1, 120]]            [1, 84]            10,164     
   Linear-6          [[1, 84]]             [1, 10]              850      
===========================================================================
Total params: 61,610
Trainable params: 61,610
Non-trainable params: 0
---------------------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.11
Params size (MB): 0.24
Estimated Total Size (MB): 0.35
---------------------------------------------------------------------------






{'total_params': 61610, 'trainable_params': 61610}



# 使用 Subclass 方式构建 LeNet 模型
class LeNet(nn.Layer):
    def __init__(self, num_classes=10):
        super().__init__()
        self.num_classes = num_classes
        # 构建 features 子网，用于对输入图像进行特征提取
        self.features = nn.Sequential(
            nn.Conv2D(
                1, 6, 3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2D(2, 2),
            nn.Conv2D(
                6, 16, 5, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2D(2, 2))
        # 构建 linear 子网，用于分类
        if num_classes > 0:
            self.linear = nn.Sequential(
                nn.Linear(400, 120),
                nn.Linear(120, 84), 
                nn.Linear(84, num_classes)
            )
    # 执行前向计算
    def forward(self, inputs):
        x = self.features(inputs)

        if self.num_classes > 0:
            x = paddle.flatten(x, 1)
            x = self.linear(x)
        return x
lenet_SubClass = LeNet()

# 可视化模型组网结构和参数
params_info = paddle.summary(lenet_SubClass,(1, 1, 28, 28))
print(params_info)



```


## 应用

### 基础概念
1. stripe
2. dimension 
3. view
4. offset
5. dispatch
6. 



### 自定义loss 
1. 自定义Loss、Metric 及 Callback：https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/advanced/customize_cn.html

### 自定义算子op
1. https://github.com/xiezhongzhao/pytorch_extension?tab=readme-ov-file
2. pytorch算子实现流程分析（持续更新） - 单单野草的文章 - 知乎 https://zhuanlan.zhihu.com/p/647196246
3. Registering a Dispatched Operator in C++：https://pytorch.org/tutorials/advanced/dispatcher.html
4. 单独编译op：https://github.com/sandeepkumar-skb/pytorch_custom_op
5. pytorch中的Dispatch机制 - daydayupzhang的文章 - 知乎https://zhuanlan.zhihu.com/p/689799317
6. Convolution 算子调用 - 知乎 https://zhuanlan.zhihu.com/p/689520605
   


### 自定义pass

### 什么是abi
```
#include <iostream>

int main() {
#ifdef _GLIBCXX_USE_CXX11_ABI
  std::cout << _GLIBCXX_USE_CXX11_ABI;
#else
  std::cout << 0;
#endif
}

在PyTorch中，ABI指的是应用程序二进制接口(Application Binary Interface)。具体来说，ABI定义了PyTorch库与其他代码（如用户编写的扩展模块或其他库）之间的接口规范。

在PyTorch中，ABI确保了不同版本的PyTorch库之间的二进制兼容性。这意味着，如果你的代码是使用一个特定版本的PyTorch编译的，它可以在其他ABI兼容的PyTorch版本上运行，而无需重新编译。

PyTorch的ABI兼容性非常重要，因为它允许用户在不同的PyTorch版本之间无缝地切换，同时保持代码的可移植性和兼容性。这样，用户可以根据需要选择适合自己的PyTorch版本，并利用PyTorch提供的新功能和性能优化，而不会因为版本不兼容而导致代码无法运行。

需要注意的是，虽然ABI保证了二进制兼容性，但在某些情况下，仍然可能需要重新编译代码以适应特定的PyTorch版本。例如，如果PyTorch库的API发生了重大变化，或者你的代码依赖于特定版本的PyTorch的新功能，那么可能需要进行重新编译以确保代码的正确性和性能。
```

## 基础模型结构示例
1. https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py

### 基础操作
```
一维
# Create tensors.
x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)

# Build a computational graph.
y = w * x + b    # y = 2 * x + 3

# Compute gradients.
y.backward()

# Print out the gradients.
print(x.grad)    # x.grad = 2 
print(w.grad)    # w.grad = 1 
print(b.grad)    # b.grad = 1 


二维
# Create tensors of shape (10, 3) and (10, 2).
x = torch.randn(10, 3)
y = torch.randn(10, 2)

# Build a fully connected layer.
linear = nn.Linear(3, 2)
print ('w: ', linear.weight)
print ('b: ', linear.bias)

# Build loss function and optimizer.
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)

# Forward pass.
pred = linear(x)

# Compute loss.
loss = criterion(pred, y)
print('loss: ', loss.item())

# Backward pass.
loss.backward()

# Print out the gradients.
print ('dL/dw: ', linear.weight.grad) 
print ('dL/db: ', linear.bias.grad)

# 1-step gradient descent.
optimizer.step()

# You can also perform gradient descent at the low level.
# linear.weight.data.sub_(0.01 * linear.weight.grad.data)
# linear.bias.data.sub_(0.01 * linear.bias.grad.data)

# Print out the loss after 1-step gradient descent.
pred = linear(x)
loss = criterion(pred, y)
print('loss after 1 step optimization: ', loss.item())

```
### linear_regression
```
维度 
print(x_train.shape)
print(x_train.dtype)
(15, 1)
float32

一般是 B N D + dtype
B 样本批次
N 一批数量
D 不填默认维度是1


x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], 
                    [9.779], [6.182], [7.59], [2.167], [7.042], 
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], 
                    [3.366], [2.596], [2.53], [1.221], [2.827], 
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)
print(x_train.size())


# Loss and optimizer
# nn.CrossEntropyLoss() computes softmax internally
criterion = nn.CrossEntropyLoss()  
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  

loss = criterion(outputs, labels)
# Backward and optimize
optimizer.zero_grad()
loss.backward()
optimizer.step()

```

### 自定义网络层
```
# Fully connected neural network with one hidden layer
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = NeuralNet(input_size, hidden_size, num_classes).to(device)


```

## 高阶模型结构示例
### CNN
```
# Convolutional neural network (two convolutional layers)
class ConvNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc = nn.Linear(7*7*32, num_classes)
        
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out

model = ConvNet(num_classes).to(device)
```

### RNN
```
# Recurrent neural network (many-to-one)
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        # Set initial hidden and cell states 
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device) 
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

model = RNN(input_size, hidden_size, num_layers, num_classes).to(device)


```

### BiRNN
```
# Bidirectional recurrent neural network (many-to-one)
class BiRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(BiRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size*2, num_classes)  # 2 for bidirection
    
    def forward(self, x):
        # Set initial states
        h0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device) # 2 for bidirection 
        c0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size*2)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

model = BiRNN(input_size, hidden_size, num_layers, num_classes).to(device)


```

### ResNet
```

# 3x3 convolution
def conv3x3(in_channels, out_channels, stride=1):
    return nn.Conv2d(in_channels, out_channels, kernel_size=3, 
                     stride=stride, padding=1, bias=False)


# Residual block
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(ResidualBlock, self).__init__()
        self.conv1 = conv3x3(in_channels, out_channels, stride)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(out_channels, out_channels)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample
        
    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        if self.downsample:
            residual = self.downsample(x)
        out += residual
        out = self.relu(out)
        return out

# ResNet
class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=10):
        super(ResNet, self).__init__()
        self.in_channels = 16
        self.conv = conv3x3(3, 16)
        self.bn = nn.BatchNorm2d(16)
        self.relu = nn.ReLU(inplace=True)
        self.layer1 = self.make_layer(block, 16, layers[0])
        self.layer2 = self.make_layer(block, 32, layers[1], 2)
        self.layer3 = self.make_layer(block, 64, layers[2], 2)
        self.avg_pool = nn.AvgPool2d(8)
        self.fc = nn.Linear(64, num_classes)
        
    def make_layer(self, block, out_channels, blocks, stride=1):
        downsample = None
        if (stride != 1) or (self.in_channels != out_channels):
            downsample = nn.Sequential(
                conv3x3(self.in_channels, out_channels, stride=stride),
                nn.BatchNorm2d(out_channels))
        layers = []
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        self.in_channels = out_channels
        for i in range(1, blocks):
            layers.append(block(out_channels, out_channels))
        return nn.Sequential(*layers)
    
    def forward(self, x):
        out = self.conv(x)
        out = self.bn(out)
        out = self.relu(out)
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.avg_pool(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out
    
model = ResNet(ResidualBlock, [2, 2, 2]).to(device)


```

### CTR
1. https://github.com/shenweichen/DeepCTR-Torch
```

```

## 基础模型训练示例


## 高阶模型训练示例
### 论文复现
1. https://github.com/labmlai/annotated_deep_learning_paper_implementations
2. 
### recommenders
1. https://github.com/tensorflow/recommenders/blob/28a28f02e524f14f3e6facd9e276cc82bbb719df/tensorflow_recommenders/tasks/retrieval.py#L156


### SimCSE
1. 电商搜索召回. https://github.com/muyuuuu/E-commerce-Search-Recall?spm=5176.21852664.0.0.79006ebf02bd2j
2. SimCSE pytorch. https://github.com/zhengyanzhao1997/NLP-model/tree/main/model/model/Torch_model/SimCSE-Chinese
3. SimCSE的loss实现源码解读. https://zhuanlan.zhihu.com/p/377862950
4. SimCSE简介以及核心代码详解——无监督文本向量抽取. https://zhuanlan.zhihu.com/p/462763973

### in-match 负采样
1. https://github.com/facebookresearch/DPR/issues/110
2. 样本处理(如何负采样) - 彭红卿的文章 - 知乎 https://zhuanlan.zhihu.com/p/435971582
3. In-batch Negatives 策略的训练数据为语义相似的 Pair 对，策略核心是在 1 个 Batch 内同时基于 N 个负例进行梯度更新，将Batch 内除自身之外其它所有 Source Text 的相似文本 Target Text 作为负例，例如: 上例中“我手机丢了，我想换个手机” 有 1 个正例(”我想买个新手机，求推荐“)，3 个负例(1.求秋色之空全集漫画，2.手机学日语的软件，3.侠盗飞车罪恶都市怎么改车)。
4. 代码示例：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/applications/neural_search/recall/in_batch_negative/batch_negative/model.py
5. https://discuss.pytorch.org/t/implementing-negative-sampling-in-pytorch/65087
```


```

## 附录
### 编译库顺序

### 0218 git pull记录
```
create mode 100644 c10/xpu/XPUStream.h
 create mode 100644 c10/xpu/test/CMakeLists.txt
 create mode 100644 c10/xpu/test/impl/XPUCachingAllocatorTest.cpp
 create mode 100644 c10/xpu/test/impl/XPUDeviceTest.cpp
 create mode 100644 c10/xpu/test/impl/XPUStreamTest.cpp
 create mode 100644 c10/xpu/test/impl/XPUTest.h
 delete mode 100644 caffe2/core/common_test.cc
 delete mode 100644 caffe2/core/static_tracepoint.h
 delete mode 100644 caffe2/core/static_tracepoint_elfx86.h
 create mode 100644 caffe2/perfkernels/adagrad_avx512.cc
 create mode 100644 caffe2/python/test/net_name_test.py
 create mode 100644 cmake/External/oort.cmake
 create mode 100644 cmake/Modules/FindCUSPARSELT.cmake
 create mode 100644 cmake/Modules/FindSYCLToolkit.cmake
 create mode 100644 cmake/public/xpu.cmake
 create mode 100644 docs/source/_static/img/dynamo/flowchart.jpg
 create mode 100644 docs/source/_static/img/onnx/onnx_dynamo_mlp_model.png
 create mode 100644 docs/source/_static/img/onnx/onnx_dynamo_mlp_model_function_body.png
 create mode 100644 docs/source/_static/img/onnx/onnx_dynamo_mlp_model_function_highlight.png
 create mode 100644 docs/source/_static/img/torch_cuda_memory/active_memory_timeline.png
 create mode 100644 docs/source/_static/img/torch_cuda_memory/allocator_state_history.png
 create mode 100644 docs/source/_templates/autosummary/classnoinheritance.rst
 delete mode 100644 docs/source/compile/deep-dive.rst
 delete mode 100644 docs/source/compile/faq.rst
 delete mode 100644 docs/source/compile/fine_grained_apis.rst
 delete mode 100644 docs/source/compile/get-started.rst
 delete mode 100644 docs/source/compile/index.rst
 delete mode 100644 docs/source/compile/inductor_profiling.rst
 delete mode 100644 docs/source/compile/technical-overview.rst
 delete mode 100644 docs/source/compile/torchfunc-and-torchcompile.rst
 create mode 100644 docs/source/cond.rst
 create mode 100644 docs/source/cpu.rst
 create mode 100644 docs/source/cuda_environment_variables.rst
 create mode 100644 docs/source/debugging_environment_variables.rst
 create mode 100644 docs/source/deterministic.rst
 create mode 100644 docs/source/export.ir_spec.rst
 create mode 100644 docs/source/export.rst
 create mode 100644 docs/source/future_mod.rst
 create mode 100644 docs/source/fx.experimental.rst
 create mode 100644 docs/source/meta.rst
 create mode 100644 docs/source/miscellaneous_environment_variables.rst
 create mode 100644 docs/source/nn.attention.bias.rst
 create mode 100644 docs/source/nn.attention.rst
 create mode 100644 docs/source/notes/fsdp.rst
 delete mode 100644 docs/source/onnx_diagnostics.rst
 create mode 100644 docs/source/onnx_dynamo.rst
 create mode 100644 docs/source/onnx_dynamo_onnxruntime_backend.rst
 create mode 100644 docs/source/onnx_torchscript.rst
 rename docs/source/{onnx_supported_aten_ops.rst => onnx_torchscript_supported_aten_ops.rst} (91%)
 create mode 100644 docs/source/scripts/exportdb/blurb.txt
 create mode 100644 docs/source/scripts/exportdb/generate_example_rst.py
 rename docs/source/scripts/onnx/{build_onnx_diagnostics_rules_md.py => build_onnx_dynamo_diagnostics_rules_md.py} (85%)
 rename docs/source/scripts/onnx/{build_onnx_supported_aten_op_csv_table.py => build_onnx_torchscript_supported_aten_op_csv_table.py} (99%)
 create mode 100644 docs/source/threading_environment_variables.rst
 create mode 100644 docs/source/torch.compiler.rst
 create mode 100644 docs/source/torch.compiler_aot_inductor.rst
 rename docs/source/{compiler.rst => torch.compiler_api.rst} (58%)
 create mode 100644 docs/source/torch.compiler_best_practices_for_backends.rst
 rename docs/source/{compile/cudagraph_trees.rst => torch.compiler_cudagraph_trees.rst} (84%)
 rename docs/source/{compile/custom-backends.rst => torch.compiler_custom_backends.rst} (53%)
 create mode 100644 docs/source/torch.compiler_deepdive.rst
 rename docs/source/{compile/dynamic-shapes.rst => torch.compiler_dynamic_shapes.rst} (86%)
 rename docs/source/{compile/fake-tensor.rst => torch.compiler_fake_tensor.rst} (100%)
 create mode 100644 docs/source/torch.compiler_faq.rst
 create mode 100644 docs/source/torch.compiler_fine_grain_apis.rst
 create mode 100644 docs/source/torch.compiler_get_started.rst
 rename docs/source/{compile/guards-overview.rst => torch.compiler_guards_overview.rst} (96%)
 create mode 100644 docs/source/torch.compiler_inductor_profiling.rst
 rename docs/source/{ir.rst => torch.compiler_ir.rst} (98%)
 rename docs/source/{compile/nn-module.rst => torch.compiler_nn_module.rst} (100%)
 rename docs/source/{compile/performance-dashboard.rst => torch.compiler_performance_dashboard.rst} (100%)
 rename docs/source/{compile/profiling_torch_compile.rst => torch.compiler_profiling_torch_compile.rst} (95%)
 rename docs/source/{compile/transformations.rst => torch.compiler_transformations.rst} (99%)
 rename docs/source/{compile/troubleshooting.rst => torch.compiler_troubleshooting.rst} (79%)
 create mode 100644 docs/source/torch_cuda_memory.rst
 create mode 100644 docs/source/torch_environment_variables.rst
 create mode 100644 docs/source/utils.rst
 create mode 100644 docs/source/xpu.rst
 delete mode 100644 functorch/experimental/_cond.py
 rename ios/{LibTorch-Lite.podspec => LibTorch-Lite.podspec.template} (93%)
 rename ios/{LibTorch.podspec => LibTorch.podspec.template} (92%)
 create mode 100755 ios/TestApp/run_on_aws_devicefarm.py
 delete mode 100644 mypy-nofollow.ini
 create mode 100644 mypy_plugins/sympy_mypy_plugin.py
 rename {.circleci/scripts => scripts}/build_android_gradle.sh (94%)
 create mode 100644 scripts/compile_tests/common.py
 create mode 100644 scripts/compile_tests/download_reports.py
 create mode 100644 scripts/compile_tests/failures_histogram.py
 create mode 100644 scripts/compile_tests/passrate.py
 create mode 100755 scripts/compile_tests/update_failures.py
 create mode 100644 scripts/export/update_schema.py
 create mode 100755 scripts/release/apply-release-changes.sh
 delete mode 120000 test/_nvfuser/test_dynamo.py
 delete mode 120000 test/_nvfuser/test_python_frontend.py
 delete mode 120000 test/_nvfuser/test_torchscript.py
 create mode 100644 test/autograd/test_logging.py
 create mode 100644 test/cpp/aot_inductor/aoti_custom_class.cpp
 create mode 100644 test/cpp/aot_inductor/aoti_custom_class.h
 create mode 100644 test/cpp/aot_inductor/compile_model.py
 create mode 100644 test/cpp/api/nested_int.cpp
 create mode 100644 test/cpp_extensions/identity.cpp
 create mode 100644 test/custom_operator/my_custom_ops.py
 create mode 100644 test/custom_operator/my_custom_ops2.py
 create mode 100644 test/custom_operator/pointwise.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_autograd.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_collectives.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_comm.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_frozen.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_init.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_memory.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_mixed_precision.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_overlap.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_state.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_state_dict.py
 create mode 100644 test/distributed/_composable/fsdp/test_fully_shard_training.py
 create mode 100644 test/distributed/_composable/fully_shard/test_fully_shard_compile.py
 create mode 100644 test/distributed/_composable/test_replicate_with_compiler.py
 create mode 100644 test/distributed/_tensor/debug/test_comm_mode.py
 create mode 100644 test/distributed/_tensor/experimental/test_tp_transform.py
 delete mode 100644 test/distributed/_tensor/test_basic_strategy.py
 create mode 100644 test/distributed/_tensor/test_convolution_ops.py
 create mode 100644 test/distributed/_tensor/test_dtensor_compile.py
 create mode 100644 test/distributed/_tensor/test_experimental_ops.py
 create mode 100644 test/distributed/_tensor/test_op_strategy.py
 create mode 100644 test/distributed/_tensor/test_optimizers.py
 create mode 100644 test/distributed/_tensor/test_xla_integration.py
 create mode 100644 test/distributed/checkpoint/e2e/test_e2e_save_and_load.py
 create mode 100644 test/distributed/checkpoint/e2e/test_fine_tuning.py
 create mode 100644 test/distributed/checkpoint/e2e/test_fsdp_ep.py
 create mode 100644 test/distributed/checkpoint/e2e/test_pipeline.py
 delete mode 100644 test/distributed/checkpoint/test_2d_fsdp_dt_checkpoint.py
 create mode 100644 test/distributed/checkpoint/test_compatibility.py
 create mode 100644 test/distributed/checkpoint/test_dtensor_resharding.py
 create mode 100644 test/distributed/checkpoint/test_fsdp_tp_checkpoint_conversion.py
 create mode 100644 test/distributed/checkpoint/test_hsdp_checkpoint.py
 create mode 100644 test/distributed/checkpoint/test_save_load_api.py
 create mode 100644 test/distributed/checkpoint/test_state_dict.py
 create mode 100644 test/distributed/checkpoint/test_state_dict_utils.py
 create mode 100644 test/distributed/checkpoint/test_torch_save_to_dcp.py
 create mode 100644 test/distributed/checkpoint/test_tp_checkpoint.py
 create mode 100644 test/distributed/fsdp/test_fsdp_backward_prefetch.py
 create mode 100644 test/distributed/fsdp/test_hsdp_dtensor_state_dict.py
 delete mode 100644 test/distributed/tensor/parallel/test_2d_parallel.py
 create mode 100644 test/distributed/tensor/parallel/test_ddp_2d_parallel.py
 create mode 100644 test/distributed/tensor/parallel/test_fsdp_2d_parallel.py
 create mode 100644 test/distributed/tensor/parallel/test_tp_random_state.py
 delete mode 100644 test/distributed/tensor/parallel/test_view_sharding_dim_change.py
 create mode 100644 test/distributed/test_c10d_functional_native.py
 create mode 100644 test/distributed/test_collective_utils.py
 create mode 100644 test/distributed/test_compute_comm_reordering.py
 rename test/distributed/{_tensor => }/test_device_mesh.py (57%)
 create mode 100644 test/dynamo/test_backward_higher_order_ops.py
 create mode 100644 test/dynamo/test_base_output.py
 create mode 100644 test/dynamo/test_bytecode_hook.py
 create mode 100644 test/dynamo/test_debug_utils.py
 create mode 100644 test/dynamo/test_exc.py
 create mode 100644 test/dynamo/test_frame_init.py
 create mode 100644 test/dynamo/test_hooks.py
 create mode 100644 test/dynamo/test_input_attr_tracking.py
 create mode 100644 test/dynamo/test_pre_dispatch.py
 create mode 100644 test/dynamo/test_sdpa.py
 create mode 100644 test/dynamo/test_subclasses.py
 create mode 100644 test/dynamo/test_torchrec.py
 create mode 100644 test/dynamo/test_trace_rules.py
 create mode 100644 test/dynamo/test_triton_kernels.py
 delete mode 100644 test/edge/RuntimeContext.h
 create mode 100644 test/edge/event_tracer.h
 create mode 100644 test/edge/event_tracer_hooks.h
 create mode 100644 test/edge/kernel_runtime_context.h
 create mode 100644 test/edge/templates/RegisterKernels.h
 create mode 100644 test/expect/HasDecompTest.test_aten_core_operators.expect
 rename {.circleci/cimodel/data => test/export}/__init__.py (100%)
 create mode 100644 test/export/test_experimental.py
 create mode 100644 test/export/test_export_nonstrict.py
 create mode 100644 test/export/test_functionalized_assertions.py
 create mode 100644 test/export/test_lift_unlift.py
 create mode 100644 test/export/test_retraceability.py
 create mode 100644 test/export/test_safeguard.py
 create mode 100644 test/export/test_schema.py
 create mode 100644 test/export/test_serdes.py
 create mode 100644 test/export/test_torchbind.py
 create mode 100644 test/export/test_tree_utils.py
 create mode 100644 test/export/test_unflatten.py
 create mode 100644 test/export/test_upgrade.py
 create mode 100644 test/export/testing.py
 delete mode 100644 test/functorch/test_functionalize.py
 create mode 100644 test/fx/test_fx_split.py
 create mode 100644 test/fx/test_lazy_graph_module.py
 create mode 100644 test/inductor/extension_backends/extension_codegen_backend.py
 create mode 100644 test/inductor/extension_backends/extension_device.cpp
 create mode 100644 test/inductor/test_aot_inductor.py
 create mode 100644 test/inductor/test_aot_inductor_utils.py
 create mode 100644 test/inductor/test_benchmark_fusion.py
 create mode 100644 test/inductor/test_binary_folding.py
 create mode 100644 test/inductor/test_codecache.py
 create mode 100644 test/inductor/test_codegen_triton.py
 create mode 100644 test/inductor/test_compiled_autograd.py
 create mode 100644 test/inductor/test_compiled_optimizers.py
 create mode 100644 test/inductor/test_control_flow.py
 rename test/inductor/{test_cpp_wrapper.py => test_cpu_cpp_wrapper.py} (53%)
 create mode 100644 test/inductor/test_cuda_cpp_wrapper.py
 create mode 100644 test/inductor/test_cudacodecache.py
 create mode 100644 test/inductor/test_custom_lowering.py
 create mode 100644 test/inductor/test_custom_post_grad_passes.py
 create mode 100644 test/inductor/test_debug_trace.py
 create mode 100644 test/inductor/test_dependencies.py
 create mode 100644 test/inductor/test_distributed_patterns.py
 create mode 100644 test/inductor/test_efficient_conv_bn_eval.py
 create mode 100644 test/inductor/test_extension_backend.py
 create mode 100644 test/inductor/test_fp8.py
 create mode 100644 test/inductor/test_group_batch_fusion.py
 create mode 100644 test/inductor/test_inductor_utils.py
 create mode 100644 test/inductor/test_inplacing_pass.py
 create mode 100644 test/inductor/test_memory_planning.py
 create mode 100644 test/inductor/test_metrics.py
 create mode 100644 test/inductor/test_mmdecomp.py
 create mode 100644 test/inductor/test_move_constructors_to_cuda.py
 create mode 100644 test/inductor/test_multi_kernel.py
 create mode 100644 test/inductor/test_pad_mm.py
 create mode 100644 test/inductor/test_snode_runtime.py
 create mode 100644 test/inductor/test_triton_heuristics.py
 create mode 100644 test/inductor/test_unbacked_symints.py
 create mode 100644 test/inductor/test_utils.py
 create mode 100644 test/jit/test_generator.py
 delete mode 100644 test/jit/test_ivalue.py
 create mode 100644 test/jit/test_union_pep604.py
 create mode 100644 test/lazy/test_functionalization.py
 create mode 100644 test/lazy/test_generator.py
 create mode 100644 test/minioptest_failures_dict.json
 create mode 100644 test/nn/test_load_state_dict.py
 create mode 100644 test/onnx/dynamo/test_dynamo_with_onnxruntime_backend.py
 create mode 100644 test/onnx/dynamo/test_registry_dispatcher.py
 create mode 100644 test/onnx/error_reproduction.py
 create mode 100644 test/onnx/expect/TestOperators.test_meshgrid_indexing.expect
 create mode 100644 test/onnx/test_fx_to_onnx_decomp_skip.py
 create mode 100644 test/onnx/test_fx_type_promotion.py
 create mode 100644 test/onnx/torch_export/test_torch_export_with_onnxruntime.py
 create mode 100644 test/pytest_shard_custom.py
 create mode 100644 test/quantization/core/experimental/test_float8.py
 create mode 100644 test/quantization/pt2e/test_duplicate_dq.py
 create mode 100644 test/quantization/pt2e/test_generate_numeric_debug_handle.py
 create mode 100644 test/quantization/pt2e/test_metadata_porting.py
 delete mode 100644 test/quantization/pt2e/test_quantize_pt2e_fx.py
 create mode 100644 test/quantization/pt2e/test_quantize_pt2e_qat.py
 create mode 100644 test/quantization/pt2e/test_representation.py
 create mode 100644 test/quantization/pt2e/test_xnnpack_quantizer.py
 create mode 100644 test/test_autograd_fallback.py
 create mode 100644 test/test_cuda_multigpu.py
 delete mode 100644 test/test_custom_op_testing.py
 create mode 100644 test/test_custom_ops.py
 delete mode 100644 test/test_jit_cuda_fuser.py
 create mode 100644 test/test_model_exports_to_core_aten.py
 delete mode 100644 test/test_module_init.py
 delete mode 100644 test/test_nvfuser_dynamo.py
 delete mode 100644 test/test_nvfuser_frontend.py
 create mode 100644 test/test_out_dtype_op.py
 create mode 100644 test/test_sparse_semi_structured.py
 create mode 100644 test/test_xpu.py
 rename {.circleci/cimodel/data/simple => test/torch_np}/__init__.py (100%)
 create mode 100644 test/torch_np/check_tests_conform.py
 create mode 100644 test/torch_np/conftest.py
 create mode 100644 test/torch_np/numpy_tests/core/test_dlpack.py
 create mode 100644 test/torch_np/numpy_tests/core/test_dtype.py
 create mode 100644 test/torch_np/numpy_tests/core/test_einsum.py
 create mode 100644 test/torch_np/numpy_tests/core/test_getlimits.py
 create mode 100644 test/torch_np/numpy_tests/core/test_indexing.py
 create mode 100644 test/torch_np/numpy_tests/core/test_multiarray.py
 create mode 100644 test/torch_np/numpy_tests/core/test_numeric.py
 create mode 100644 test/torch_np/numpy_tests/core/test_numerictypes.py
 create mode 100644 test/torch_np/numpy_tests/core/test_scalar_ctors.py
 create mode 100644 test/torch_np/numpy_tests/core/test_scalar_methods.py
 create mode 100644 test/torch_np/numpy_tests/core/test_scalarinherit.py
 create mode 100644 test/torch_np/numpy_tests/core/test_scalarmath.py
 create mode 100644 test/torch_np/numpy_tests/core/test_shape_base.py
 create mode 100644 test/torch_np/numpy_tests/fft/test_helper.py
 create mode 100644 test/torch_np/numpy_tests/fft/test_pocketfft.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_arraypad.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_arraysetops.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_function_base.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_histograms.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_index_tricks.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_shape_base_.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_twodim_base.py
 create mode 100644 test/torch_np/numpy_tests/lib/test_type_check.py
 create mode 100644 test/torch_np/numpy_tests/linalg/test_linalg.py
 create mode 100644 test/torch_np/test_basic.py
 create mode 100644 test/torch_np/test_binary_ufuncs.py
 create mode 100644 test/torch_np/test_dtype.py
 create mode 100644 test/torch_np/test_function_base.py
 create mode 100644 test/torch_np/test_ndarray_methods.py
 create mode 100644 test/torch_np/test_nep50_examples.py
 create mode 100644 test/torch_np/test_random.py
 create mode 100644 test/torch_np/test_reductions.py
 create mode 100644 test/torch_np/test_scalars_0D_arrays.py
 create mode 100644 test/torch_np/test_ufuncs_basic.py
 create mode 100644 test/torch_np/test_unary_ufuncs.py
 rename test/typing/fail/{bitwise_ops.py => disabled_bitwise_ops.py} (100%)
 create mode 100644 test/typing/pass/cuda_steam.py
 create mode 100644 test/typing/pass/disabled_jit.py
 create mode 100644 third_party/cudnn_frontend.BUILD
 create mode 160000 third_party/mimalloc
 delete mode 100644 third_party/nvfuser/CMakeLists.txt
 delete mode 100644 third_party/nvfuser/benchmark/CMakeLists.txt
 delete mode 100644 third_party/nvfuser/benchmark/batch_norm_channels_first.cpp
 delete mode 100644 third_party/nvfuser/benchmark/batch_norm_channels_first_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/batch_norm_channels_last.cpp
 delete mode 100644 third_party/nvfuser/benchmark/batch_norm_channels_last_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/bert.cpp
 delete mode 100644 third_party/nvfuser/benchmark/broadcast.cpp
 delete mode 100644 third_party/nvfuser/benchmark/gelu_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/heuristic_cache.cpp
 delete mode 100644 third_party/nvfuser/benchmark/heuristic_lookup.cpp
 delete mode 100644 third_party/nvfuser/benchmark/instance_norm.cpp
 delete mode 100644 third_party/nvfuser/benchmark/layer_norm.cpp
 delete mode 100644 third_party/nvfuser/benchmark/layer_norm_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/lstm_cell.cpp
 delete mode 100644 third_party/nvfuser/benchmark/main.cpp
 delete mode 100644 third_party/nvfuser/benchmark/matmul.cpp
 delete mode 100644 third_party/nvfuser/benchmark/reduction.cpp
 delete mode 100644 third_party/nvfuser/benchmark/rms_norm.cpp
 delete mode 100644 third_party/nvfuser/benchmark/rms_norm_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/scale_bias_relu.cpp
 delete mode 100644 third_party/nvfuser/benchmark/shape_inference.cpp
 delete mode 100644 third_party/nvfuser/benchmark/softmax.cpp
 delete mode 100644 third_party/nvfuser/benchmark/softmax_backward.cpp
 delete mode 100644 third_party/nvfuser/benchmark/softmax_dropout.cpp
 delete mode 100644 third_party/nvfuser/benchmark/timm.cpp
 delete mode 100644 third_party/nvfuser/benchmark/transpose.cpp
 delete mode 100644 third_party/nvfuser/benchmark/utils.cpp
 delete mode 100644 third_party/nvfuser/benchmark/utils.h
 delete mode 100644 third_party/nvfuser/csrc/arith.cpp
 delete mode 100644 third_party/nvfuser/csrc/arith.h
 delete mode 100644 third_party/nvfuser/csrc/codegen.cpp
 delete mode 100644 third_party/nvfuser/csrc/codegen.h
 delete mode 100644 third_party/nvfuser/csrc/compute_at.cpp
 delete mode 100644 third_party/nvfuser/csrc/compute_at.h
 delete mode 100644 third_party/nvfuser/csrc/compute_at_map.cpp
 delete mode 100644 third_party/nvfuser/csrc/compute_at_map.h
 delete mode 100644 third_party/nvfuser/csrc/contiguity.cpp
 delete mode 100644 third_party/nvfuser/csrc/contiguity.h
 delete mode 100644 third_party/nvfuser/csrc/disjoint_set.h
 delete mode 100644 third_party/nvfuser/csrc/dispatch.cpp
 delete mode 100644 third_party/nvfuser/csrc/dispatch.h
 delete mode 100644 third_party/nvfuser/csrc/docs/.gitignore
 delete mode 100644 third_party/nvfuser/csrc/docs/documentation.h
 delete mode 100644 third_party/nvfuser/csrc/docs/fuser.doxygen
 delete mode 100644 third_party/nvfuser/csrc/docs/images/ir_architecture.png
 delete mode 100644 third_party/nvfuser/csrc/docs/main_page.md
 delete mode 100644 third_party/nvfuser/csrc/dynamic_type.h
 delete mode 100644 third_party/nvfuser/csrc/evaluator_common.cpp
 delete mode 100644 third_party/nvfuser/csrc/evaluator_common.h
 delete mode 100644 third_party/nvfuser/csrc/executor.cpp
 delete mode 100644 third_party/nvfuser/csrc/executor.h
 delete mode 100644 third_party/nvfuser/csrc/executor_kernel_arg.cpp
 delete mode 100644 third_party/nvfuser/csrc/executor_kernel_arg.h
 delete mode 100644 third_party/nvfuser/csrc/executor_launch_params.cpp
 delete mode 100644 third_party/nvfuser/csrc/executor_launch_params.h
 delete mode 100644 third_party/nvfuser/csrc/executor_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/executor_utils.h
 delete mode 100644 third_party/nvfuser/csrc/expr_evaluator.cpp
 delete mode 100644 third_party/nvfuser/csrc/expr_evaluator.h
 delete mode 100644 third_party/nvfuser/csrc/fusion.cpp
 delete mode 100644 third_party/nvfuser/csrc/fusion.h
 delete mode 100644 third_party/nvfuser/csrc/fusion_segmenter.cpp
 delete mode 100644 third_party/nvfuser/csrc/fusion_segmenter.h
 delete mode 100644 third_party/nvfuser/csrc/graph_fuser.cpp
 delete mode 100644 third_party/nvfuser/csrc/grouped_reduction.cpp
 delete mode 100644 third_party/nvfuser/csrc/grouped_reduction.h
 delete mode 100644 third_party/nvfuser/csrc/index_compute.cpp
 delete mode 100644 third_party/nvfuser/csrc/index_compute.h
 delete mode 100644 third_party/nvfuser/csrc/inlining.cpp
 delete mode 100644 third_party/nvfuser/csrc/inlining.h
 delete mode 100644 third_party/nvfuser/csrc/instrumentation.cpp
 delete mode 100644 third_party/nvfuser/csrc/instrumentation.h
 delete mode 100644 third_party/nvfuser/csrc/ir_all_nodes.h
 delete mode 100644 third_party/nvfuser/csrc/ir_base_nodes.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_base_nodes.h
 delete mode 100644 third_party/nvfuser/csrc/ir_builder.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_builder.h
 delete mode 100644 third_party/nvfuser/csrc/ir_cloner.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_cloner.h
 delete mode 100644 third_party/nvfuser/csrc/ir_container.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_container.h
 delete mode 100644 third_party/nvfuser/csrc/ir_graphviz.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_graphviz.h
 delete mode 100644 third_party/nvfuser/csrc/ir_interface_nodes.h
 delete mode 100644 third_party/nvfuser/csrc/ir_internal_nodes.h
 delete mode 100644 third_party/nvfuser/csrc/ir_iostream.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_iostream.h
 delete mode 100644 third_party/nvfuser/csrc/ir_nodes.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_printer.h
 delete mode 100644 third_party/nvfuser/csrc/ir_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/ir_utils.h
 delete mode 100644 third_party/nvfuser/csrc/iter_visitor.cpp
 delete mode 100644 third_party/nvfuser/csrc/iter_visitor.h
 delete mode 100644 third_party/nvfuser/csrc/kernel.cpp
 delete mode 100644 third_party/nvfuser/csrc/kernel.h
 delete mode 100644 third_party/nvfuser/csrc/kernel_cache.cpp
 delete mode 100644 third_party/nvfuser/csrc/kernel_cache.h
 delete mode 100644 third_party/nvfuser/csrc/kernel_expr_evaluator.cpp
 delete mode 100644 third_party/nvfuser/csrc/kernel_expr_evaluator.h
 delete mode 100644 third_party/nvfuser/csrc/kernel_ir.cpp
 delete mode 100644 third_party/nvfuser/csrc/kernel_ir.h
 delete mode 100644 third_party/nvfuser/csrc/kernel_ir_dispatch.cpp
 delete mode 100644 third_party/nvfuser/csrc/kernel_ir_dispatch.h
 delete mode 100644 third_party/nvfuser/csrc/lower2device.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower2device.h
 delete mode 100644 third_party/nvfuser/csrc/lower_alias_memory.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_alias_memory.h
 delete mode 100644 third_party/nvfuser/csrc/lower_allocation.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_allocation.h
 delete mode 100644 third_party/nvfuser/csrc/lower_bank_conflict.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_bank_conflict.h
 delete mode 100644 third_party/nvfuser/csrc/lower_divisible_split.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_divisible_split.h
 delete mode 100644 third_party/nvfuser/csrc/lower_double_buffer.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_double_buffer.h
 delete mode 100644 third_party/nvfuser/csrc/lower_expr_sort.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_expr_sort.h
 delete mode 100644 third_party/nvfuser/csrc/lower_fused_reduction.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_fused_reduction.h
 delete mode 100644 third_party/nvfuser/csrc/lower_fusion_simplifier.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_fusion_simplifier.h
 delete mode 100644 third_party/nvfuser/csrc/lower_index.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_index.h
 delete mode 100644 third_party/nvfuser/csrc/lower_index_compute.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_index_compute.h
 delete mode 100644 third_party/nvfuser/csrc/lower_index_hoist.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_index_hoist.h
 delete mode 100644 third_party/nvfuser/csrc/lower_insert_syncs.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_insert_syncs.h
 delete mode 100644 third_party/nvfuser/csrc/lower_instrument.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_instrument.h
 delete mode 100644 third_party/nvfuser/csrc/lower_loops.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_loops.h
 delete mode 100644 third_party/nvfuser/csrc/lower_magic_zero.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_magic_zero.h
 delete mode 100644 third_party/nvfuser/csrc/lower_misaligned_vectorization.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_misaligned_vectorization.h
 delete mode 100644 third_party/nvfuser/csrc/lower_predicate.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_predicate.h
 delete mode 100644 third_party/nvfuser/csrc/lower_predicate_elimination.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_predicate_elimination.h
 delete mode 100644 third_party/nvfuser/csrc/lower_replace_size.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_replace_size.h
 delete mode 100644 third_party/nvfuser/csrc/lower_shift.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_shift.h
 delete mode 100644 third_party/nvfuser/csrc/lower_sync_information.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_sync_information.h
 delete mode 100644 third_party/nvfuser/csrc/lower_thread_predicate.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_thread_predicate.h
 delete mode 100644 third_party/nvfuser/csrc/lower_trivial_broadcast.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_trivial_broadcast.h
 delete mode 100644 third_party/nvfuser/csrc/lower_trivial_reductions.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_trivial_reductions.h
 delete mode 100644 third_party/nvfuser/csrc/lower_unroll.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_unroll.h
 delete mode 100644 third_party/nvfuser/csrc/lower_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_utils.h
 delete mode 100644 third_party/nvfuser/csrc/lower_validation.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_validation.h
 delete mode 100644 third_party/nvfuser/csrc/lower_warp_reduce.cpp
 delete mode 100644 third_party/nvfuser/csrc/lower_warp_reduce.h
 delete mode 100644 third_party/nvfuser/csrc/manager.cpp
 delete mode 100644 third_party/nvfuser/csrc/manager.h
 delete mode 100644 third_party/nvfuser/csrc/maxinfo_propagator.cpp
 delete mode 100644 third_party/nvfuser/csrc/maxinfo_propagator.h
 delete mode 100644 third_party/nvfuser/csrc/mma_type.cpp
 delete mode 100644 third_party/nvfuser/csrc/mma_type.h
 delete mode 100644 third_party/nvfuser/csrc/mutator.cpp
 delete mode 100644 third_party/nvfuser/csrc/mutator.h
 delete mode 100644 third_party/nvfuser/csrc/non_divisible_split.cpp
 delete mode 100644 third_party/nvfuser/csrc/non_divisible_split.h
 delete mode 100644 third_party/nvfuser/csrc/ops/alias.cpp
 delete mode 100644 third_party/nvfuser/csrc/ops/alias.h
 delete mode 100644 third_party/nvfuser/csrc/ops/all_ops.h
 delete mode 100644 third_party/nvfuser/csrc/ops/composite.cpp
 delete mode 100644 third_party/nvfuser/csrc/ops/composite.h
 delete mode 100644 third_party/nvfuser/csrc/ops/normalization.cpp
 delete mode 100644 third_party/nvfuser/csrc/ops/normalization.h
 delete mode 100644 third_party/nvfuser/csrc/parallel_dimension_map.cpp
 delete mode 100644 third_party/nvfuser/csrc/parallel_dimension_map.h
 delete mode 100644 third_party/nvfuser/csrc/parallel_type_bitmap.cpp
 delete mode 100644 third_party/nvfuser/csrc/parallel_type_bitmap.h
 delete mode 100644 third_party/nvfuser/csrc/parser.cpp
 delete mode 100644 third_party/nvfuser/csrc/parser.h
 delete mode 100644 third_party/nvfuser/csrc/partial_split_map.cpp
 delete mode 100644 third_party/nvfuser/csrc/partial_split_map.h
 delete mode 100644 third_party/nvfuser/csrc/partition.cpp
 delete mode 100644 third_party/nvfuser/csrc/partition.h
 delete mode 100644 third_party/nvfuser/csrc/predicate_compute.cpp
 delete mode 100644 third_party/nvfuser/csrc/predicate_compute.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/README.md
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_cache.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_cache.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_definition.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_definition.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_interface.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_interface.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/fusion_record.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/python_bindings.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/python_bindings.h
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/python_bindings_extension.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/test/test_nvfuser_fusion_cache.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/test/test_nvfuser_fusion_definition.cpp
 delete mode 100644 third_party/nvfuser/csrc/python_frontend/test/test_nvfuser_fusion_record.cpp
 delete mode 100644 third_party/nvfuser/csrc/register_interface.cpp
 delete mode 100644 third_party/nvfuser/csrc/register_interface.h
 delete mode 100644 third_party/nvfuser/csrc/root_domain_map.cpp
 delete mode 100644 third_party/nvfuser/csrc/root_domain_map.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/all_schedulers.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/compile_time_info.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/debug_utils.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/heuristic.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/matmul.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/matmul.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/mma_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/mma_utils.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/normalization.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/normalization.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/pointwise.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/pointwise.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/pointwise_heuristic.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/pointwise_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/pointwise_utils.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/reduction.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/reduction.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/reduction_heuristic.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/reduction_utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/reduction_utils.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/registry.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/registry.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/transpose.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/transpose.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/transpose_heuristic.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/utils.h
 delete mode 100644 third_party/nvfuser/csrc/scheduler/vectorize_helper.cpp
 delete mode 100644 third_party/nvfuser/csrc/scheduler/vectorize_helper.h
 delete mode 100644 third_party/nvfuser/csrc/tensor_view.cpp
 delete mode 100644 third_party/nvfuser/csrc/transform_iter.cpp
 delete mode 100644 third_party/nvfuser/csrc/transform_iter.h
 delete mode 100644 third_party/nvfuser/csrc/transform_replay.cpp
 delete mode 100644 third_party/nvfuser/csrc/transform_replay.h
 delete mode 100644 third_party/nvfuser/csrc/transform_rfactor.cpp
 delete mode 100644 third_party/nvfuser/csrc/transform_rfactor.h
 delete mode 100644 third_party/nvfuser/csrc/transform_view.cpp
 delete mode 100644 third_party/nvfuser/csrc/transform_view.h
 delete mode 100644 third_party/nvfuser/csrc/type.cpp
 delete mode 100644 third_party/nvfuser/csrc/type.h
 delete mode 100644 third_party/nvfuser/csrc/type_inference.cpp
 delete mode 100644 third_party/nvfuser/csrc/type_inference.h
 delete mode 100644 third_party/nvfuser/csrc/type_promotion.cpp
 delete mode 100644 third_party/nvfuser/csrc/type_promotion.h
 delete mode 100644 third_party/nvfuser/csrc/utils.cpp
 delete mode 100644 third_party/nvfuser/csrc/utils.h
 delete mode 100644 third_party/nvfuser/csrc/vectorization_info.h
 delete mode 100644 third_party/nvfuser/examples/sinh_extension/README.md
 delete mode 100644 third_party/nvfuser/examples/sinh_extension/main.cpp
 delete mode 100644 third_party/nvfuser/examples/sinh_extension/setup.py
 delete mode 100644 third_party/nvfuser/examples/sinh_extension/test.py
 delete mode 100644 third_party/nvfuser/examples/sinh_libtorch/CMakeLists.txt
 delete mode 100644 third_party/nvfuser/examples/sinh_libtorch/README.md
 delete mode 100644 third_party/nvfuser/examples/sinh_libtorch/main.cpp
 delete mode 100644 third_party/nvfuser/python/__init__.py
 delete mode 100644 third_party/nvfuser/python_tests/test_dynamo.py
 delete mode 100644 third_party/nvfuser/python_tests/test_python_frontend.py
 delete mode 100644 third_party/nvfuser/python_tests/test_torchscript.py
 delete mode 100644 third_party/nvfuser/runtime/array.cu
 delete mode 100644 third_party/nvfuser/runtime/array_rocm.cu
 delete mode 100644 third_party/nvfuser/runtime/bf16_support.cu
 delete mode 100644 third_party/nvfuser/runtime/bf16_support_rocm.cu
 delete mode 100644 third_party/nvfuser/runtime/block_reduction.cu
 delete mode 100644 third_party/nvfuser/runtime/block_sync_atomic.cu
 delete mode 100644 third_party/nvfuser/runtime/block_sync_default.cu
 delete mode 100644 third_party/nvfuser/runtime/block_sync_default_rocm.cu
 delete mode 100644 third_party/nvfuser/runtime/broadcast.cu
 delete mode 100644 third_party/nvfuser/runtime/fp16_support.cu
 delete mode 100644 third_party/nvfuser/runtime/fused_reduction.cu
 delete mode 100644 third_party/nvfuser/runtime/fused_welford_helper.cu
 delete mode 100644 third_party/nvfuser/runtime/fused_welford_impl.cu
 delete mode 100644 third_party/nvfuser/runtime/grid_broadcast.cu
 delete mode 100644 third_party/nvfuser/runtime/grid_reduction.cu
 delete mode 100644 third_party/nvfuser/runtime/grid_sync.cu
 delete mode 100644 third_party/nvfuser/runtime/helpers.cu
 delete mode 100644 third_party/nvfuser/runtime/index_utils.cu
 delete mode 100644 third_party/nvfuser/runtime/memory.cu
 delete mode 100644 third_party/nvfuser/runtime/random_numbers.cu
 delete mode 100644 third_party/nvfuser/runtime/swizzle.cu
 delete mode 100644 third_party/nvfuser/runtime/tensor.cu
 delete mode 100644 third_party/nvfuser/runtime/tensorcore.cu
 delete mode 100644 third_party/nvfuser/runtime/tuple.cu
 delete mode 100644 third_party/nvfuser/runtime/type_traits.cu
 delete mode 100644 third_party/nvfuser/runtime/warp.cu
 delete mode 100644 third_party/nvfuser/runtime/warp_rocm.cu
 delete mode 100644 third_party/nvfuser/runtime/welford.cu
 delete mode 100644 third_party/nvfuser/test/test_gpu1.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu2.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu3.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_fused_reduction.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_rng.cu
 delete mode 100644 third_party/nvfuser/test/test_gpu_shift.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_tensor_factories.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_tensorcore.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_transpose.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_utils.cpp
 delete mode 100644 third_party/nvfuser/test/test_gpu_validator.h
 delete mode 100644 third_party/nvfuser/test/test_gpu_view.cpp
 delete mode 100644 third_party/nvfuser/test/test_utils.h
 delete mode 100644 third_party/nvfuser/tools/stringify_file.py
 delete mode 160000 third_party/python-enum
 delete mode 160000 third_party/python-six
 create mode 100644 tools/autograd/gen_view_funcs.py
 create mode 100644 tools/autograd/templates/ViewFuncs.cpp
 create mode 100644 tools/autograd/templates/ViewFuncs.h
 rename {torch/csrc/autograd => tools/autograd/templates}/python_return_types.h (70%)
 create mode 100755 tools/build_with_debinfo.py
 rename {.circleci/cimodel/data/simple/util => tools/github}/__init__.py (100%)
 create mode 100644 tools/github/github_utils.py
 delete mode 100644 tools/iwyu/qnnpack.imp
 delete mode 100644 tools/linter/adapters/circleci_linter.py
 create mode 100644 tools/linter/adapters/no_merge_conflict_csv_linter.py
 create mode 100644 tools/linter/adapters/test_has_main_linter.py
 create mode 100644 tools/stats/upload_metrics.py
 create mode 100644 tools/test/heuristics/heuristics_test_mixin.py
 create mode 100644 tools/test/heuristics/test_heuristics.py
 create mode 100644 tools/test/heuristics/test_historical_class_failure_correlation.py
 create mode 100644 tools/test/heuristics/test_interface.py
 delete mode 100644 tools/test/test_import_test_stats.py
 create mode 100644 tools/test/test_test_run.py
 create mode 100644 tools/testing/discover_tests.py
 create mode 100644 tools/testing/target_determination/determinator.py
 create mode 100644 tools/testing/target_determination/heuristics/__init__.py
 create mode 100644 tools/testing/target_determination/heuristics/correlated_with_historical_failures.py
 create mode 100644 tools/testing/target_determination/heuristics/edited_by_pr.py
 create mode 100644 tools/testing/target_determination/heuristics/historical_class_failure_correlation.py
 create mode 100644 tools/testing/target_determination/heuristics/historical_edited_files.py
 create mode 100644 tools/testing/target_determination/heuristics/interface.py
 create mode 100644 tools/testing/target_determination/heuristics/previously_failed_in_pr.py
 create mode 100644 tools/testing/target_determination/heuristics/profiling.py
 create mode 100644 tools/testing/target_determination/heuristics/utils.py
 create mode 100644 tools/testing/test_run.py
 create mode 100644 torch/_C/_aoti.pyi
 create mode 100644 torch/_C/_cpu.pyi
 create mode 100644 torch/_C/_dynamo/compiled_autograd.pyi
 create mode 100644 torch/_C/_dynamo/guards.pyi
 create mode 100644 torch/_compile.py
 create mode 100644 torch/_custom_ops.py
 create mode 100644 torch/_dynamo/_trace_wrapped_higher_order_op.py
 delete mode 100644 torch/_dynamo/allowed_functions.py
 delete mode 100644 torch/_dynamo/backends/ipex.py
 delete mode 100644 torch/_dynamo/backends/nvfuser.py
 create mode 100644 torch/_dynamo/cache_size.py
 create mode 100644 torch/_dynamo/code_context.py
 create mode 100644 torch/_dynamo/compiled_autograd.py
 create mode 100644 torch/_dynamo/current_scope_id.py
 create mode 100644 torch/_dynamo/decorators.py
 create mode 100644 torch/_dynamo/device_interface.py
 create mode 100644 torch/_dynamo/funcname_cache.py
 create mode 100644 torch/_dynamo/polyfill.py
 delete mode 100644 torch/_dynamo/skipfiles.py
 create mode 100644 torch/_dynamo/trace_rules.py
 create mode 100644 torch/_dynamo/variables/distributed.py
 create mode 100644 torch/_dynamo/variables/higher_order_ops.py
 create mode 100644 torch/_dynamo/variables/iter.py
 create mode 100644 torch/_dynamo/variables/lazy.py
 create mode 100644 torch/_dynamo/variables/sdpa.py
 create mode 100644 torch/_dynamo/variables/torch_function.py
 delete mode 100644 torch/_export/constraints.py
 create mode 100644 torch/_export/db/examples/constrain_as_size_example.py
 create mode 100644 torch/_export/db/examples/constrain_as_value_example.py
 create mode 100644 torch/_export/db/examples/model_attr_mutation.py
 create mode 100644 torch/_export/db/examples/optional_input.py
 create mode 100644 torch/_export/db/examples/torch_sym_min.py
 create mode 100644 torch/_export/db/examples/user_input_mutation.py
 create mode 100644 torch/_export/non_strict_utils.py
 create mode 100644 torch/_export/passes/collect_tracepoints_pass.py
 delete mode 100644 torch/_export/passes/const_prop_pass.py
 create mode 100644 torch/_export/passes/functionalize_side_effectful_ops_pass.py
 create mode 100644 torch/_export/passes/lift_constants_pass.py
 create mode 100644 torch/_export/passes/remove_runtime_assertions.py
 create mode 100644 torch/_export/passes/replace_set_grad_with_hop_pass.py
 create mode 100644 torch/_export/serde/schema.yaml
 create mode 100644 torch/_export/serde/schema_check.py
 create mode 100644 torch/_export/serde/union.py
 create mode 100644 torch/_export/serde/upgrade.py
 delete mode 100644 torch/_export/trace.py
 create mode 100644 torch/_export/utils.py
 delete mode 100644 torch/_export/workflow.py
 create mode 100644 torch/_export/wrappers.py
 create mode 100644 torch/_functorch/_aot_autograd/__init__.py
 create mode 100644 torch/_functorch/_aot_autograd/collect_metadata_analysis.py
 create mode 100644 torch/_functorch/_aot_autograd/dispatch_and_compile_graph.py
 create mode 100644 torch/_functorch/_aot_autograd/functional_utils.py
 create mode 100644 torch/_functorch/_aot_autograd/input_output_analysis.py
 create mode 100644 torch/_functorch/_aot_autograd/jit_compile_runtime_wrappers.py
 create mode 100644 torch/_functorch/_aot_autograd/logging_utils.py
 create mode 100644 torch/_functorch/_aot_autograd/runtime_wrappers.py
 create mode 100644 torch/_functorch/_aot_autograd/schemas.py
 create mode 100644 torch/_functorch/_aot_autograd/subclass_utils.py
 create mode 100644 torch/_functorch/_aot_autograd/traced_function_transforms.py
 create mode 100644 torch/_functorch/_aot_autograd/utils.py
 create mode 100644 torch/_functorch/apis.py
 create mode 100644 torch/_higher_order_ops/auto_functionalize.py
 create mode 100644 torch/_higher_order_ops/cond.py
 rename functorch/experimental/_map.py => torch/_higher_order_ops/map.py (50%)
 create mode 100644 torch/_higher_order_ops/out_dtype.py
 create mode 100644 torch/_higher_order_ops/strict_mode.py
 create mode 100644 torch/_higher_order_ops/torchbind.py
 create mode 100644 torch/_higher_order_ops/triton_kernel_wrap.py
 create mode 100644 torch/_higher_order_ops/utils.py
 create mode 100644 torch/_higher_order_ops/while_loop.py
 create mode 100644 torch/_inductor/codegen/aoti_runtime/implementation.cpp
 create mode 100644 torch/_inductor/codegen/aoti_runtime/interface.cpp
 create mode 100644 torch/_inductor/codegen/cpp_wrapper_cpu.py
 create mode 100644 torch/_inductor/codegen/cpp_wrapper_cuda.py
 rename {.circleci/cimodel/lib => torch/_inductor/codegen/cuda}/__init__.py (100%)
 create mode 100644 torch/_inductor/codegen/cuda/cuda_cpp_scheduling.py
 create mode 100644 torch/_inductor/codegen/cuda/cuda_env.py
 create mode 100644 torch/_inductor/codegen/cuda/cuda_kernel.py
 create mode 100644 torch/_inductor/codegen/cuda/cuda_template.py
 create mode 100644 torch/_inductor/codegen/cuda/cutlass_epilogue_gen.py
 rename {test/_nvfuser => torch/_inductor/codegen/cuda/cutlass_lib_extensions}/__init__.py (100%)
 create mode 100644 torch/_inductor/codegen/cuda/cutlass_lib_extensions/gemm_operation_extensions.py
 create mode 100644 torch/_inductor/codegen/cuda/cutlass_utils.py
 create mode 100644 torch/_inductor/codegen/cuda/device_op_overrides.py
 create mode 100644 torch/_inductor/codegen/cuda/gemm_template.py
 create mode 100644 torch/_inductor/codegen/cuda_combined_scheduling.py
 create mode 100644 torch/_inductor/codegen/memory_planning.py
 create mode 100644 torch/_inductor/codegen/multi_kernel.py
 create mode 100644 torch/_inductor/codegen/triton_split_scan.py
 create mode 100644 torch/_inductor/comm_analysis.py
 create mode 100644 torch/_inductor/comms.py
 create mode 100644 torch/_inductor/constant_folding.py
 delete mode 100644 torch/_inductor/cuda_properties.py
 create mode 100644 torch/_inductor/cudagraph_utils.py
 create mode 100644 torch/_inductor/fx_passes/README.md
 create mode 100644 torch/_inductor/fx_passes/binary_folding.py
 create mode 100644 torch/_inductor/fx_passes/dedupe_symint_uses.py
 create mode 100644 torch/_inductor/fx_passes/efficient_conv_bn_eval.py
 create mode 100644 torch/_inductor/fx_passes/freezing_patterns.py
 create mode 100644 torch/_inductor/fx_passes/group_batch_fusion.py
 create mode 100644 torch/_inductor/fx_passes/misc_patterns.py
 create mode 100644 torch/_inductor/fx_passes/numeric_utils.py
 create mode 100644 torch/_inductor/fx_passes/reinplace.py
 rename {third_party/nvfuser/python_tests => torch/_inductor/fx_passes/serialized_patterns}/__init__.py (100%)
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_1.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_10.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_11.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_12.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_13.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_14.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_15.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_16.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_17.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_2.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_3.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_4.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_5.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_6.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_7.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_8.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/_sfdp_pattern_9.py
 create mode 100644 torch/_inductor/fx_passes/serialized_patterns/central_index.py
 create mode 100644 torch/_inductor/kernel/unpack_mixed_mm.py
 delete mode 100644 torch/_inductor/mkldnn.py
 create mode 100644 torch/_inductor/ops_handler.py
 create mode 100644 torch/_inductor/quantized_lowerings.py
 create mode 100644 torch/_inductor/script.ld
 create mode 100644 torch/_inductor/wrapper_benchmark.py
 create mode 100644 torch/_library/__init__.py
 create mode 100644 torch/_library/abstract_impl.py
 create mode 100644 torch/_library/simple_registry.py
 create mode 100644 torch/_library/utils.py
 create mode 100644 torch/_numpy/README.md
 create mode 100644 torch/_numpy/__init__.py
 create mode 100644 torch/_numpy/_binary_ufuncs_impl.py
 create mode 100644 torch/_numpy/_casting_dicts.py
 create mode 100644 torch/_numpy/_dtypes.py
 create mode 100644 torch/_numpy/_dtypes_impl.py
 create mode 100644 torch/_numpy/_funcs.py
 create mode 100644 torch/_numpy/_funcs_impl.py
 create mode 100644 torch/_numpy/_getlimits.py
 create mode 100644 torch/_numpy/_ndarray.py
 create mode 100644 torch/_numpy/_normalizations.py
 create mode 100644 torch/_numpy/_reductions_impl.py
 create mode 100644 torch/_numpy/_ufuncs.py
 create mode 100644 torch/_numpy/_unary_ufuncs_impl.py
 create mode 100644 torch/_numpy/_util.py
 create mode 100644 torch/_numpy/fft.py
 create mode 100644 torch/_numpy/linalg.py
 create mode 100644 torch/_numpy/random.py
 create mode 100644 torch/_numpy/testing/__init__.py
 create mode 100644 torch/_numpy/testing/utils.py
 delete mode 100644 torch/_prims/nvfuser_executor.py
 delete mode 100644 torch/_prims/nvfuser_prims.py
 create mode 100644 torch/_streambase.py
 create mode 100644 torch/_subclasses/fake_impls.py
 create mode 100644 torch/_subclasses/functional_tensor.py
 create mode 100644 torch/_vendor/README.md
 rename torch/{ao/quantization/_pt2e => _vendor}/__init__.py (100%)
 create mode 100644 torch/_vendor/packaging/LICENSE
 create mode 100644 torch/_vendor/packaging/LICENSE.APACHE
 create mode 100644 torch/_vendor/packaging/LICENSE.BSD
 create mode 100644 torch/_vendor/packaging/__init__.py
 create mode 100644 torch/_vendor/packaging/_structures.py
 create mode 100644 torch/_vendor/packaging/version.py
 create mode 100644 torch/amp/grad_scaler.py
 create mode 100644 torch/ao/pruning/_experimental/pruner/FPGM_pruner.py
 delete mode 100644 torch/ao/quantization/_pt2e/_propagate_annotation.py
 delete mode 100644 torch/ao/quantization/_pt2e/prepare.py
 delete mode 100644 torch/ao/quantization/_pt2e/qat_utils.py
 delete mode 100644 torch/ao/quantization/_pt2e/quantizer/qnnpack_quantizer.py
 delete mode 100644 torch/ao/quantization/_pt2e/quantizer/utils.py
 delete mode 100644 torch/ao/quantization/_pt2e/quantizer/x86_inductor_quantizer.py
 delete mode 100644 torch/ao/quantization/_pt2e/utils.py
 delete mode 100644 torch/ao/quantization/_quantize_pt2e.py
 delete mode 100644 torch/ao/quantization/backend_config/_x86_inductor_pt2e.py
 create mode 100644 torch/ao/quantization/pt2e/__init__.py
 create mode 100644 torch/ao/quantization/pt2e/duplicate_dq_pass.py
 create mode 100644 torch/ao/quantization/pt2e/export_utils.py
 create mode 100644 torch/ao/quantization/pt2e/generate_numeric_debug_handle.py
 rename torch/ao/quantization/{_pt2e => pt2e}/graph_utils.py (64%)
 create mode 100644 torch/ao/quantization/pt2e/port_metadata_pass.py
 create mode 100644 torch/ao/quantization/pt2e/prepare.py
 create mode 100644 torch/ao/quantization/pt2e/qat_utils.py
 create mode 100644 torch/ao/quantization/pt2e/representation/__init__.py
 create mode 100644 torch/ao/quantization/pt2e/representation/rewrite.py
 create mode 100644 torch/ao/quantization/pt2e/utils.py
 create mode 100644 torch/ao/quantization/quantize_pt2e.py
 rename torch/ao/quantization/{_pt2e => }/quantizer/__init__.py (55%)
 rename torch/ao/quantization/{_pt2e => }/quantizer/composable_quantizer.py (93%)
 rename torch/ao/quantization/{_pt2e => }/quantizer/embedding_quantizer.py (94%)
 rename torch/ao/quantization/{_pt2e => }/quantizer/quantizer.py (55%)
 create mode 100644 torch/ao/quantization/quantizer/utils.py
 create mode 100644 torch/ao/quantization/quantizer/x86_inductor_quantizer.py
 create mode 100644 torch/ao/quantization/quantizer/xnnpack_quantizer.py
 create mode 100644 torch/ao/quantization/quantizer/xnnpack_quantizer_utils.py
 create mode 100644 torch/backends/mha/__init__.py
 create mode 100644 torch/backends/nnpack/__init__.py
 create mode 100644 torch/cpu/amp/grad_scaler.py
 create mode 100644 torch/csrc/api/include/torch/xpu.h
 create mode 100644 torch/csrc/api/src/xpu.cpp
 create mode 100644 torch/csrc/autograd/input_metadata.cpp
 create mode 100644 torch/csrc/cpu/Module.cpp
 create mode 100644 torch/csrc/cpu/Module.h
 create mode 100644 torch/csrc/distributed/c10d/FakeProcessGroup.hpp
 create mode 100644 torch/csrc/distributed/c10d/Functional.cpp
 create mode 100644 torch/csrc/distributed/c10d/GroupRegistry.cpp
 create mode 100644 torch/csrc/distributed/c10d/GroupRegistry.hpp
 create mode 100644 torch/csrc/distributed/c10d/RankLocal.hpp
 create mode 100644 torch/csrc/distributed/c10d/TCPStoreBackend.cpp
 create mode 100644 torch/csrc/distributed/c10d/TCPStoreBackend.hpp
 create mode 100644 torch/csrc/distributed/c10d/TCPStoreLibUvBackend.cpp
 delete mode 100644 torch/csrc/distributed/c10d/UCCForNCCL.hpp
 delete mode 100644 torch/csrc/distributed/c10d/exception.cpp
 create mode 100644 torch/csrc/distributed/c10d/intra_node_comm.cpp
 create mode 100644 torch/csrc/distributed/c10d/intra_node_comm.cu
 create mode 100644 torch/csrc/distributed/c10d/intra_node_comm.hpp
 create mode 100644 torch/csrc/dynamo/cache_entry.cpp
 create mode 100644 torch/csrc/dynamo/cache_entry.h
 create mode 100644 torch/csrc/dynamo/compiled_autograd.h
 create mode 100644 torch/csrc/dynamo/cpp_shim.cpp
 create mode 100644 torch/csrc/dynamo/cpp_shim.h
 create mode 100644 torch/csrc/dynamo/debug_macros.h
 create mode 100644 torch/csrc/dynamo/extra_state.cpp
 create mode 100644 torch/csrc/dynamo/extra_state.h
 create mode 100644 torch/csrc/dynamo/python_compiled_autograd.cpp
 create mode 100644 torch/csrc/dynamo/python_compiled_autograd.h
 create mode 100644 torch/csrc/dynamo/utils.h
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner.cpp
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner.h
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner_cpu.cpp
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner_cpu.h
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner_cuda.cpp
 create mode 100644 torch/csrc/inductor/aoti_runner/model_container_runner_cuda.h
 create mode 100644 torch/csrc/inductor/aoti_runner/pybind.cpp
 create mode 100644 torch/csrc/inductor/aoti_runner/pybind.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/arrayref_tensor.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/device_utils.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/interface.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/model.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/model_container.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/scalar_to_tensor.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/thread_local.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/utils.h
 create mode 100644 torch/csrc/inductor/aoti_runtime/utils_cuda.h
 create mode 100644 torch/csrc/inductor/aoti_torch/c/shim.h
 create mode 100644 torch/csrc/inductor/aoti_torch/proxy_executor.h
 create mode 100644 torch/csrc/inductor/aoti_torch/shim_common.cpp
 create mode 100644 torch/csrc/inductor/aoti_torch/shim_cuda.cpp
 create mode 100644 torch/csrc/inductor/aoti_torch/tensor_converter.cpp
 create mode 100644 torch/csrc/inductor/aoti_torch/tensor_converter.h
 create mode 100644 torch/csrc/inductor/aoti_torch/utils.h
 create mode 100644 torch/csrc/inductor/inductor_ops.cpp
 create mode 100644 torch/csrc/inductor/inductor_ops.h
 delete mode 100644 torch/csrc/jit/passes/cuda_graph_fuser.cpp
 delete mode 100644 torch/csrc/jit/passes/cuda_graph_fuser.h
 delete mode 100644 torch/csrc/lazy/ts_backend/ops/random_ops.cpp
 delete mode 100644 torch/csrc/lazy/ts_backend/ops/random_ops.h
 create mode 100644 torch/csrc/onnx/back_compat.h
 create mode 100644 torch/csrc/profiler/README.md
 delete mode 100644 torch/csrc/profiler/standalone/execution_graph_observer.h
 rename torch/csrc/profiler/standalone/{execution_graph_observer.cpp => execution_trace_observer.cpp} (80%)
 create mode 100644 torch/csrc/profiler/standalone/execution_trace_observer.h
 create mode 100644 torch/csrc/profiler/unwind/unwind_fb.cpp
 delete mode 100644 torch/csrc/quantized/quantized_backward.cpp
 delete mode 100644 torch/csrc/utils/auto_gil.h
 delete mode 100644 torch/csrc/utils/cuda_lazy_init.cpp
 delete mode 100644 torch/csrc/utils/cuda_lazy_init.h
 create mode 100644 torch/csrc/utils/device_lazy_init.cpp
 create mode 100644 torch/csrc/utils/device_lazy_init.h
 delete mode 100644 torch/csrc/utils/memory.h
 create mode 100644 torch/csrc/utils/pyobject_preservation.cpp
 create mode 100644 torch/csrc/utils/pyobject_preservation.h
 create mode 100644 torch/csrc/xpu/Event.cpp
 create mode 100644 torch/csrc/xpu/Event.h
 create mode 100644 torch/csrc/xpu/Module.cpp
 create mode 100644 torch/csrc/xpu/Module.h
 create mode 100644 torch/csrc/xpu/Stream.cpp
 create mode 100644 torch/csrc/xpu/Stream.h
 create mode 100644 torch/distributed/_composable/fsdp/__init__.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_api.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_collectives.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_common.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_init.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_param.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_param_group.py
 create mode 100644 torch/distributed/_composable/fsdp/_fsdp_state.py
 create mode 100644 torch/distributed/_composable/fsdp/fully_shard.py
 create mode 100644 torch/distributed/_functional_collectives_impl.py
 create mode 100644 torch/distributed/_state_dict_utils.py
 create mode 100644 torch/distributed/_tensor/_collective_utils.py
 create mode 100644 torch/distributed/_tensor/_xla.py
 create mode 100644 torch/distributed/_tensor/debug/comm_mode.py
 create mode 100644 torch/distributed/_tensor/debug/visualize_sharding.py
 create mode 100644 torch/distributed/_tensor/examples/convnext_example.py
 create mode 100644 torch/distributed/_tensor/examples/visualize_sharding_example.py
 create mode 100644 torch/distributed/_tensor/experimental/__init__.py
 create mode 100644 torch/distributed/_tensor/experimental/tp_transform.py
 create mode 100644 torch/distributed/_tensor/ops/conv_ops.py
 create mode 100644 torch/distributed/_tensor/ops/experimental_ops.py
 create mode 100644 torch/distributed/_tensor/tp_conv.py
 create mode 100644 torch/distributed/checkpoint/_checkpointer.py
 create mode 100644 torch/distributed/checkpoint/_dedup_save_plans.py
 create mode 100644 torch/distributed/checkpoint/_storage_utils.py
 create mode 100644 torch/distributed/checkpoint/examples/async_checkpointing_example.py
 create mode 100644 torch/distributed/checkpoint/examples/stateful_example.py
 create mode 100644 torch/distributed/checkpoint/state_dict.py
 create mode 100644 torch/distributed/checkpoint/stateful.py
 create mode 100644 torch/distributed/collective_utils.py
 create mode 100644 torch/distributed/device_mesh.py
 rename torch/distributed/fsdp/{flat_param.py => _flat_param.py} (85%)
 delete mode 100644 torch/distributed/fsdp/_utils.py
 create mode 100644 torch/distributed/tensor/parallel/_data_parallel_utils.py
 delete mode 100644 torch/distributed/tensor/parallel/_view_with_dim_change.py
 create mode 100644 torch/distributed/tensor/parallel/ddp.py
 create mode 100644 torch/distributed/tensor/parallel/input_reshard.py
 delete mode 100644 torch/distributed/tensor/parallel/multihead_attention_tp.py
 create mode 100644 torch/distributions/inverse_gamma.py
 create mode 100644 torch/export/__init__.py
 create mode 100644 torch/export/_safeguard.py
 create mode 100644 torch/export/_trace.py
 create mode 100644 torch/export/_tree_utils.py
 create mode 100644 torch/export/_unlift.py
 create mode 100644 torch/export/custom_obj.py
 create mode 100644 torch/export/dynamic_shapes.py
 create mode 100644 torch/export/exported_program.py
 create mode 100644 torch/export/graph_signature.py
 create mode 100644 torch/export/unflatten.py
 create mode 100644 torch/export/wrapper.py
 create mode 100644 torch/fx/_lazy_graph_module.py
 create mode 100644 torch/fx/experimental/_config.py
 create mode 100644 torch/fx/experimental/_sym_dispatch_mode.py
 create mode 100644 torch/fx/experimental/recording.py
 create mode 100644 torch/fx/experimental/sym_node.py
 create mode 100644 torch/fx/experimental/validator.py
 create mode 100644 torch/fx/passes/utils/matcher_with_name_node_map_utils.py
 create mode 100644 torch/jit/_script.pyi
 create mode 100644 torch/mps/event.py
 create mode 100644 torch/nested/_internal/__init__.py
 create mode 100644 torch/nested/_internal/nested_tensor.py
 create mode 100644 torch/nested/_internal/ops.py
 create mode 100644 torch/nested/_internal/sdpa.py
 create mode 100644 torch/nn/attention/__init__.py
 create mode 100644 torch/nn/attention/_utils.py
 create mode 100644 torch/nn/attention/bias.py
 create mode 100644 torch/onnx/_internal/fx/decomposition_skip.py
 delete mode 100644 torch/onnx/_internal/fx/function_dispatcher.py
 create mode 100644 torch/onnx/_internal/fx/fx_onnx_interpreter.py
 create mode 100644 torch/onnx/_internal/fx/onnxfunction_dispatcher.py
 delete mode 100644 torch/onnx/_internal/fx/passes/fx_to_onnxscript.py
 create mode 100644 torch/onnx/_internal/fx/passes/modularization.py
 create mode 100644 torch/onnx/_internal/fx/passes/readability.py
 delete mode 100644 torch/onnx/_internal/fx/passes/shape_inference.py
 create mode 100644 torch/onnx/_internal/fx/passes/type_promotion.py
 rename torch/onnx/_internal/fx/{context.py => patcher.py} (56%)
 create mode 100644 torch/onnx/_internal/fx/torch_export_graph_extractor.py
 create mode 100644 torch/onnx/_internal/fx/type_utils.py
 create mode 100644 torch/onnx/_internal/onnxruntime.py
 delete mode 100644 torch/optim/optimizer.pyi
 create mode 100644 torch/quantization/_quantized_conversions.py
 create mode 100644 torch/sparse/_semi_structured_conversions.py
 create mode 100644 torch/sparse/_semi_structured_ops.py
 create mode 100644 torch/sparse/_triton_ops_meta.py
 create mode 100644 torch/sparse/semi_structured.py
 delete mode 100644 torch/testing/_internal/codegen/random_topo_test.py
 create mode 100644 torch/testing/_internal/common_mkldnn.py
 create mode 100644 torch/testing/_internal/common_optimizers.py
 create mode 100644 torch/testing/_internal/distributed/common_state_dict.py
 create mode 100644 torch/testing/_internal/dynamo_test_failures.py
 create mode 100644 torch/testing/_internal/optests/autograd_registration.py
 delete mode 100644 torch/testing/_internal/optests/compile_check.py
 create mode 100644 torch/testing/_internal/optests/generate_tests.py
 create mode 100644 torch/testing/_internal/triton_utils.py
 create mode 100644 torch/testing/_internal/two_tensor.py
 rename torch/{_dynamo/config_utils.py => utils/_config_module.py} (53%)
 create mode 100644 torch/utils/_config_typing.pyi
 delete mode 100644 torch/utils/_crash_handler.py
 create mode 100644 torch/utils/_cxx_pytree.py
 create mode 100644 torch/utils/_import_utils.py
 create mode 100644 torch/utils/_sympy/functions.py
 create mode 100644 torch/utils/_sympy/singleton_int.py
 create mode 100644 torch/utils/_sympy/solve.py
 create mode 100644 torch/utils/_triton.py
 create mode 100644 torch/utils/_typing_utils.py
 delete mode 100644 torch/utils/benchmark/examples/blas_compare.py
 delete mode 100644 torch/utils/benchmark/examples/end_to_end.py
 delete mode 100644 torch/utils/data/_utils/serialization.py
 create mode 100644 torch/utils/deterministic.py
 create mode 100644 torch/utils/viz/__init__.py
 create mode 100644 torch/utils/viz/_cycles.py
 create mode 100644 torch/xpu/__init__.py
 create mode 100644 torch/xpu/_utils.py
 create mode 100644 torch/xpu/streams.py
 create mode 100644 torchgen/fuse_attention_patterns/gen_attention_patterns.py
 create mode 100644 ubsan.supp

```

```
[30/8065] Linking CXX static library lib/libprotobuf-lite.a
[110/8065] Linking CXX static library lib/libprotobuf.a
[194/8065] Linking CXX static library lib/libprotoc.a
[206/8065] Linking C static library lib/libpthreadpool.a
[219/8065] Linking C static library lib/libcpuinfo.a
[222/8065] Linking CXX executable bin/protoc-3.13.0.0
[243/8065] Linking C static library lib/libcpuinfo_internals.a
[283/8065] Linking C static library lib/libclog.a
[286/8065] Linking C static library lib/libqnnpack.a
[346/8065] Linking CXX static library lib/libpytorch_qnnpack.a
[351/8065] Linking C static library lib/libnnpack_reference_layers.a
[1440/8065] Linking C static library lib/libnnpack.a
[5298/8065] Linking CXX static library lib/libgtest.a
[5299/8065] Linking CXX static library lib/libgmock.a
[5300/8065] Linking CXX static library lib/libgmock_main.a
[5301/8065] Linking CXX static library lib/libgtest_main.a
[5314/8065] Linking CXX static library lib/libbenchmark.a
[5315/8065] Linking CXX static library lib/libbenchmark_main.a
[5437/8065] Linking CXX static library lib/libXNNPACK.a
[5502/8065] Linking C static library lib/libittnotify.a
[5520/8065] Linking CXX static library lib/libasmjit.a
[5541/8065] Linking C static library lib/libtensorpipe_uv.a
[5594/8065] Linking CXX static library lib/libtensorpipe.a
[5641/8065] Linking C static library lib/libfoxi_loader.a
[5644/8065] Linking CXX static library lib/libgloo.a
[5650/8065] Linking CXX static library lib/libonnx_proto.a
[5705/8065] Linking CXX static library lib/libfbgemm.a
[5730/8065] Linking CXX static library lib/libonnx.a
[6161/8065] Linking CXX static library lib/libfmt.a
[6164/8065] Linking CXX static library lib/libdnnl.a
[6194/8065] Linking CXX static library lib/libkineto.a
[6267/8065] Linking CXX shared library lib/libc10.so
[6268/8065] Linking CXX executable bin/c10_CompileTimeFunctionPointer_test
[6269/8065] Linking CXX executable bin/c10_DeviceGuard_test
[6270/8065] Linking CXX executable bin/c10_Device_test
[6272/8065] Linking CXX executable bin/c10_StreamGuard_test
[6274/8065] Linking CXX executable bin/c10_SymInt_test
[6277/8065] Linking CXX executable bin/c10_Scalar_test
[6278/8065] Linking CXX executable bin/c10_InlineDeviceGuard_test
[6280/8065] Linking CXX executable bin/c10_DispatchKeySet_test
[6282/8065] Linking CXX executable bin/c10_Bitset_test
[6286/8065] Linking CXX executable bin/c10_ConstexprCrc_test
[6287/8065] Linking CXX executable bin/c10_SizesAndStrides_test
[6288/8065] Linking CXX executable bin/c10_InlineStreamGuard_test
[6290/8065] Linking CXX executable bin/c10_DeadlockDetection_test
[6292/8065] Linking CXX executable bin/c10_Half_test
[6294/8065] Linking CXX executable bin/c10_cow_test
[6296/8065] Linking CXX executable bin/c10_LeftRight_test
[6298/8065] Linking CXX executable bin/c10_Synchronized_test
[6300/8065] Linking CXX executable bin/c10_Metaprogramming_test
[6303/8065] Linking CXX executable bin/c10_ThreadLocal_test
[6304/8065] Linking CXX executable bin/c10_TypeIndex_test
[6307/8065] Linking CXX executable bin/c10_TypeList_test
[6308/8065] Linking CXX executable bin/c10_TypeTraits_test
[6310/8065] Linking CXX executable bin/c10_accumulate_test
[6312/8065] Linking CXX executable bin/c10_bit_cast_test
[6314/8065] Linking CXX executable bin/c10_bfloat16_test
[6317/8065] Linking CXX executable bin/c10_complex_math_test
[6318/8065] Linking CXX executable bin/c10_exception_test
[6320/8065] Linking CXX executable bin/c10_flags_test
[6322/8065] Linking CXX executable bin/c10_complex_test
[6324/8065] Linking CXX executable bin/c10_generic_math_test
[6326/8065] Linking CXX executable bin/c10_irange_test
[6328/8065] Linking CXX executable bin/c10_logging_test
[6330/8065] Linking CXX executable bin/c10_registry_test
[6332/8065] Linking CXX executable bin/c10_ordered_preserving_dict_test
[6334/8065] Linking CXX executable bin/c10_ssize_test
[6336/8065] Linking CXX executable bin/c10_optional_test
[6338/8065] Linking CXX executable bin/c10_string_util_test
[6340/8065] Linking CXX executable bin/c10_tempfile_test
[6342/8065] Linking CXX executable bin/c10_string_view_test
[6344/8065] Linking CXX executable bin/c10_intrusive_ptr_benchmark
[6346/8065] Linking C shared library lib/libtorch_global_deps.so
[6348/8065] Linking CXX executable bin/c10_typeid_test
[6353/8065] Linking C executable sleef/bin/addSuffix
[6357/8065] Linking CXX executable bin/c10_intrusive_ptr_test
[6360/8065] Linking C executable sleef/bin/mkrename
[6378/8065] Linking CXX static library lib/libcaffe2_protos.a
[6391/8065] Linking CXX executable bin/c10_small_vector_test
[6405/8065] Linking C executable sleef/bin/mkrename_gnuabi
[6407/8065] Linking C executable sleef/bin/mkmasked_gnuabi
[6409/8065] Linking C executable sleef/bin/mkalias
[6416/8065] Linking C executable sleef/bin/mkdisp
[7728/8065] Linking C static library sleef/lib/libsleef.a
[7729/8065] Linking CXX executable bin/vec_test_all_types_AVX2
[7730/8065] Linking CXX executable bin/vec_test_all_types_DEFAULT
[7731/8065] Linking CXX executable bin/vec_test_all_types_AVX512
[7732/8065] Linking CXX shared library lib/libtorch_cpu.so
[7733/8065] Linking CXX shared library lib/libtorch.so
[7734/8065] Linking CXX executable bin/NamedTensor_test
[7736/8065] Linking CXX executable bin/apply_utils_test
[7737/8065] Linking CXX executable bin/atest
[7738/8065] Linking CXX executable bin/basic
[7739/8065] Linking CXX executable bin/Dict_test
[7740/8065] Linking CXX executable bin/MaybeOwned_test
[7741/8065] Linking CXX executable bin/Dimname_test
[7742/8065] Linking CXX executable bin/broadcast_test
[7743/8065] Linking CXX executable bin/cpu_allocator_test
[7744/8065] Linking CXX executable bin/cpu_generator_test
[7745/8065] Linking CXX executable bin/cpu_profiling_allocator_test
[7746/8065] Linking CXX executable bin/dispatch_key_set_test
[7747/8065] Linking CXX executable bin/cpu_rng_test
[7748/8065] Linking CXX executable bin/half_test
[7749/8065] Linking CXX executable bin/dlconvertor_test
[7750/8065] Linking CXX executable bin/extension_backend_test
[7751/8065] Linking CXX executable bin/ivalue_test
[7752/8065] Linking CXX executable bin/lazy_tensor_test
[7753/8065] Linking CXX executable bin/math_kernel_test
[7755/8065] Linking CXX executable bin/memory_overlapping_test
[7756/8065] Linking CXX executable bin/memory_format_test
[7757/8065] Linking CXX executable bin/mobile_memory_cleanup
[7758/8065] Linking CXX executable bin/operator_name_test
[7759/8065] Linking CXX executable bin/native_test
[7760/8065] Linking CXX executable bin/operators_test
[7761/8065] Linking CXX executable bin/packedtensoraccessor_test
[7762/8065] Linking CXX executable bin/pow_test
[7763/8065] Linking CXX executable bin/quantized_test
[7764/8065] Linking CXX executable bin/reduce_ops_test
[7766/8065] Linking CXX executable bin/reportMemoryUsage_test
[7767/8065] Linking CXX executable bin/scalar_tensor_test
[7768/8065] Linking CXX executable bin/scalar_test
[7769/8065] Linking CXX executable bin/stride_properties_test
[7770/8065] Linking CXX executable bin/StorageUtils_test
[7771/8065] Linking CXX executable bin/tensor_iterator_test
[7772/8065] Linking CXX executable bin/test_parallel
[7773/8065] Linking CXX executable bin/thread_init_test
[7774/8065] Linking CXX executable bin/type_ptr_test
[7775/8065] Linking CXX executable bin/undefined_tensor_test
[7776/8065] Linking CXX executable bin/type_test
[7777/8065] Linking CXX executable bin/verify_api_visibility
[7778/8065] Linking CXX executable bin/legacy_vmap_test
[7779/8065] Linking CXX executable bin/weakref_test
[7780/8065] Linking CXX executable bin/wrapdim_test
[7781/8065] Linking CXX executable bin/xla_tensor_test
[7782/8065] Linking CXX executable bin/IListRef_test
[7783/8065] Linking CXX executable bin/KernelFunction_test
[7784/8065] Linking CXX executable bin/List_test
[7785/8065] Linking CXX executable bin/kernel_function_legacy_test
[7786/8065] Linking CXX executable bin/kernel_function_test
[7787/8065] Linking CXX executable bin/kernel_lambda_legacy_test
[7788/8065] Linking CXX executable bin/kernel_lambda_test
[7789/8065] Linking CXX executable bin/kernel_stackbased_test
[7790/8065] Linking CXX executable bin/make_boxed_from_unboxed_functor_test
[7791/8065] Linking CXX executable bin/CppSignature_test
[7792/8065] Linking CXX executable bin/backend_fallback_test
[7793/8065] Linking CXX static library lib/libunbox_lib.a
[7794/8065] Linking CXX executable bin/op_allowlist_test
[7795/8065] Linking CXX executable bin/op_registration_test
[7796/8065] Linking CXX executable bin/test_edge_op_registration
[7797/8065] Linking CXX executable bin/inline_container_test
[7798/8065] Linking CXX shared library lib/libtorchbind_test.so
[7799/8065] Linking CXX shared library lib/libjitbackend_test.so
[7800/8065] Linking CXX shared library lib/libbackend_with_compiler.so
[7801/8065] Linking CXX executable bin/test_jit
[7817/8065] Linking CXX executable bin/FileStoreTest
[7820/8065] Linking CXX executable bin/TCPStoreTest
[7823/8065] Linking CXX executable bin/tutorial_tensorexpr
[7824/8065] Linking CXX executable bin/HashStoreTest
[7826/8065] Linking CXX executable bin/example_allreduce
[7830/8065] Linking CXX executable bin/ProcessGroupGlooTest
[7831/8065] Linking CXX executable bin/ProcessGroupMPITest
[7835/8065] Linking CXX executable bin/test_tensorexpr
[7837/8065] Linking CXX executable bin/test_dist_autograd
[7842/8065] Linking CXX executable bin/test_cpp_rpc
[7886/8065] Linking CXX executable bin/parallel_benchmark
[7888/8065] Linking CXX executable bin/test_api
[7899/8065] Linking CXX shared library lib/libshm.so
[7903/8065] Linking CXX executable bin/torch_shm_manager
[7912/8065] Linking CXX executable bin/test_lazy
[8061/8065] Linking CXX shared library lib/libtorch_python.so
[8062/8065] Linking CXX shared library lib/libnnapi_backend.so
[8064/8065] Linking CXX shared module functorch/functorch.so
[30/8065] Linking CXX static library lib/libprotobuf-lite.a
[110/8065] Linking CXX static library lib/libprotobuf.a
[194/8065] Linking CXX static library lib/libprotoc.a
[206/8065] Linking C static library lib/libpthreadpool.a
[219/8065] Linking C static library lib/libcpuinfo.a
[222/8065] Linking CXX executable bin/protoc-3.13.0.0
[243/8065] Linking C static library lib/libcpuinfo_internals.a
[283/8065] Linking C static library lib/libclog.a
[286/8065] Linking C static library lib/libqnnpack.a
[346/8065] Linking CXX static library lib/libpytorch_qnnpack.a
[351/8065] Linking C static library lib/libnnpack_reference_layers.a
[1440/8065] Linking C static library lib/libnnpack.a
[5298/8065] Linking CXX static library lib/libgtest.a
[5299/8065] Linking CXX static library lib/libgmock.a
[5300/8065] Linking CXX static library lib/libgmock_main.a
[5301/8065] Linking CXX static library lib/libgtest_main.a
[5314/8065] Linking CXX static library lib/libbenchmark.a
[5315/8065] Linking CXX static library lib/libbenchmark_main.a
[5437/8065] Linking CXX static library lib/libXNNPACK.a
[5502/8065] Linking C static library lib/libittnotify.a
[5520/8065] Linking CXX static library lib/libasmjit.a
[5541/8065] Linking C static library lib/libtensorpipe_uv.a
[5594/8065] Linking CXX static library lib/libtensorpipe.a
[5641/8065] Linking C static library lib/libfoxi_loader.a
[5644/8065] Linking CXX static library lib/libgloo.a
[5650/8065] Linking CXX static library lib/libonnx_proto.a
[5705/8065] Linking CXX static library lib/libfbgemm.a
[5730/8065] Linking CXX static library lib/libonnx.a
[6161/8065] Linking CXX static library lib/libfmt.a
[6164/8065] Linking CXX static library lib/libdnnl.a
[6194/8065] Linking CXX static library lib/libkineto.a
[6267/8065] Linking CXX shared library lib/libc10.so
[6268/8065] Linking CXX executable bin/c10_CompileTimeFunctionPointer_test
[6269/8065] Linking CXX executable bin/c10_DeviceGuard_test
[6270/8065] Linking CXX executable bin/c10_Device_test
[6272/8065] Linking CXX executable bin/c10_StreamGuard_test
[6274/8065] Linking CXX executable bin/c10_SymInt_test
[6277/8065] Linking CXX executable bin/c10_Scalar_test
[6278/8065] Linking CXX executable bin/c10_InlineDeviceGuard_test
[6280/8065] Linking CXX executable bin/c10_DispatchKeySet_test
[6282/8065] Linking CXX executable bin/c10_Bitset_test
[6286/8065] Linking CXX executable bin/c10_ConstexprCrc_test
[6287/8065] Linking CXX executable bin/c10_SizesAndStrides_test
[6288/8065] Linking CXX executable bin/c10_InlineStreamGuard_test
[6290/8065] Linking CXX executable bin/c10_DeadlockDetection_test
[6292/8065] Linking CXX executable bin/c10_Half_test
[6294/8065] Linking CXX executable bin/c10_cow_test
[6296/8065] Linking CXX executable bin/c10_LeftRight_test
[6298/8065] Linking CXX executable bin/c10_Synchronized_test
[6300/8065] Linking CXX executable bin/c10_Metaprogramming_test
[6303/8065] Linking CXX executable bin/c10_ThreadLocal_test
[6304/8065] Linking CXX executable bin/c10_TypeIndex_test
[6307/8065] Linking CXX executable bin/c10_TypeList_test
[6308/8065] Linking CXX executable bin/c10_TypeTraits_test
[6310/8065] Linking CXX executable bin/c10_accumulate_test
[6312/8065] Linking CXX executable bin/c10_bit_cast_test
[6314/8065] Linking CXX executable bin/c10_bfloat16_test
[6317/8065] Linking CXX executable bin/c10_complex_math_test
[6318/8065] Linking CXX executable bin/c10_exception_test
[6320/8065] Linking CXX executable bin/c10_flags_test
[6322/8065] Linking CXX executable bin/c10_complex_test
[6324/8065] Linking CXX executable bin/c10_generic_math_test
[6326/8065] Linking CXX executable bin/c10_irange_test
[6328/8065] Linking CXX executable bin/c10_logging_test
[6330/8065] Linking CXX executable bin/c10_registry_test
[6332/8065] Linking CXX executable bin/c10_ordered_preserving_dict_test
[6334/8065] Linking CXX executable bin/c10_ssize_test
[6336/8065] Linking CXX executable bin/c10_optional_test
[6338/8065] Linking CXX executable bin/c10_string_util_test
[6340/8065] Linking CXX executable bin/c10_tempfile_test
[6342/8065] Linking CXX executable bin/c10_string_view_test
[6344/8065] Linking CXX executable bin/c10_intrusive_ptr_benchmark
[6346/8065] Linking C shared library lib/libtorch_global_deps.so
[6348/8065] Linking CXX executable bin/c10_typeid_test
[6353/8065] Linking C executable sleef/bin/addSuffix
[6357/8065] Linking CXX executable bin/c10_intrusive_ptr_test
[6360/8065] Linking C executable sleef/bin/mkrename
[6378/8065] Linking CXX static library lib/libcaffe2_protos.a
[6391/8065] Linking CXX executable bin/c10_small_vector_test
[6405/8065] Linking C executable sleef/bin/mkrename_gnuabi
[6407/8065] Linking C executable sleef/bin/mkmasked_gnuabi
[6409/8065] Linking C executable sleef/bin/mkalias
[6416/8065] Linking C executable sleef/bin/mkdisp
[7728/8065] Linking C static library sleef/lib/libsleef.a
[7729/8065] Linking CXX executable bin/vec_test_all_types_AVX2
[7730/8065] Linking CXX executable bin/vec_test_all_types_DEFAULT
[7731/8065] Linking CXX executable bin/vec_test_all_types_AVX512
[7732/8065] Linking CXX shared library lib/libtorch_cpu.so
[7733/8065] Linking CXX shared library lib/libtorch.so
[7734/8065] Linking CXX executable bin/NamedTensor_test
[7736/8065] Linking CXX executable bin/apply_utils_test
[7737/8065] Linking CXX executable bin/atest
[7738/8065] Linking CXX executable bin/basic
[7739/8065] Linking CXX executable bin/Dict_test
[7740/8065] Linking CXX executable bin/MaybeOwned_test
[7741/8065] Linking CXX executable bin/Dimname_test
[7742/8065] Linking CXX executable bin/broadcast_test
[7743/8065] Linking CXX executable bin/cpu_allocator_test
[7744/8065] Linking CXX executable bin/cpu_generator_test
[7745/8065] Linking CXX executable bin/cpu_profiling_allocator_test
[7746/8065] Linking CXX executable bin/dispatch_key_set_test
[7747/8065] Linking CXX executable bin/cpu_rng_test
[7748/8065] Linking CXX executable bin/half_test
[7749/8065] Linking CXX executable bin/dlconvertor_test
[7750/8065] Linking CXX executable bin/extension_backend_test
[7751/8065] Linking CXX executable bin/ivalue_test
[7752/8065] Linking CXX executable bin/lazy_tensor_test
[7753/8065] Linking CXX executable bin/math_kernel_test
[7755/8065] Linking CXX executable bin/memory_overlapping_test
[7756/8065] Linking CXX executable bin/memory_format_test
[7757/8065] Linking CXX executable bin/mobile_memory_cleanup
[7758/8065] Linking CXX executable bin/operator_name_test
[7759/8065] Linking CXX executable bin/native_test
[7760/8065] Linking CXX executable bin/operators_test
[7761/8065] Linking CXX executable bin/packedtensoraccessor_test
[7762/8065] Linking CXX executable bin/pow_test
[7763/8065] Linking CXX executable bin/quantized_test
[7764/8065] Linking CXX executable bin/reduce_ops_test
[7766/8065] Linking CXX executable bin/reportMemoryUsage_test
[7767/8065] Linking CXX executable bin/scalar_tensor_test
[7768/8065] Linking CXX executable bin/scalar_test
[7769/8065] Linking CXX executable bin/stride_properties_test
[7770/8065] Linking CXX executable bin/StorageUtils_test
[7771/8065] Linking CXX executable bin/tensor_iterator_test
[7772/8065] Linking CXX executable bin/test_parallel
[7773/8065] Linking CXX executable bin/thread_init_test
[7774/8065] Linking CXX executable bin/type_ptr_test
[7775/8065] Linking CXX executable bin/undefined_tensor_test
[7776/8065] Linking CXX executable bin/type_test
[7777/8065] Linking CXX executable bin/verify_api_visibility
[7778/8065] Linking CXX executable bin/legacy_vmap_test
[7779/8065] Linking CXX executable bin/weakref_test
[7780/8065] Linking CXX executable bin/wrapdim_test
[7781/8065] Linking CXX executable bin/xla_tensor_test
[7782/8065] Linking CXX executable bin/IListRef_test
[7783/8065] Linking CXX executable bin/KernelFunction_test
[7784/8065] Linking CXX executable bin/List_test
[7785/8065] Linking CXX executable bin/kernel_function_legacy_test
[7786/8065] Linking CXX executable bin/kernel_function_test
[7787/8065] Linking CXX executable bin/kernel_lambda_legacy_test
[7788/8065] Linking CXX executable bin/kernel_lambda_test
[7789/8065] Linking CXX executable bin/kernel_stackbased_test
[7790/8065] Linking CXX executable bin/make_boxed_from_unboxed_functor_test
[7791/8065] Linking CXX executable bin/CppSignature_test
[7792/8065] Linking CXX executable bin/backend_fallback_test
[7793/8065] Linking CXX static library lib/libunbox_lib.a
[7794/8065] Linking CXX executable bin/op_allowlist_test
[7795/8065] Linking CXX executable bin/op_registration_test
[7796/8065] Linking CXX executable bin/test_edge_op_registration
[7797/8065] Linking CXX executable bin/inline_container_test
[7798/8065] Linking CXX shared library lib/libtorchbind_test.so
[7799/8065] Linking CXX shared library lib/libjitbackend_test.so
[7800/8065] Linking CXX shared library lib/libbackend_with_compiler.so
[7801/8065] Linking CXX executable bin/test_jit
[7817/8065] Linking CXX executable bin/FileStoreTest
[7820/8065] Linking CXX executable bin/TCPStoreTest
[7823/8065] Linking CXX executable bin/tutorial_tensorexpr
[7824/8065] Linking CXX executable bin/HashStoreTest
[7826/8065] Linking CXX executable bin/example_allreduce
[7830/8065] Linking CXX executable bin/ProcessGroupGlooTest
[7831/8065] Linking CXX executable bin/ProcessGroupMPITest
[7835/8065] Linking CXX executable bin/test_tensorexpr
[7837/8065] Linking CXX executable bin/test_dist_autograd
[7842/8065] Linking CXX executable bin/test_cpp_rpc
[7886/8065] Linking CXX executable bin/parallel_benchmark
[7888/8065] Linking CXX executable bin/test_api
[7899/8065] Linking CXX shared library lib/libshm.so
[7903/8065] Linking CXX executable bin/torch_shm_manager
[7912/8065] Linking CXX executable bin/test_lazy
[8061/8065] Linking CXX shared library lib/libtorch_python.so
[8062/8065] Linking CXX shared library lib/libnnapi_backend.so
[8064/8065] Linking CXX shared module functorch/functorch.so

```