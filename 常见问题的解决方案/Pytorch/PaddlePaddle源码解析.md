## PaddlePaddle
### 理解时间
```
2024年3月28号启动

完整理解PaddlePaddle项目
如果只是在搜索引擎 搜 PaddlePaddle是远远不够的
PaddlePaddle + 架构图

PaddlePaddle + 概念关键词

PaddlePaddle + 问题排查

PaddlePaddle + 面试汇总

PaddlePaddle + 极客挑战赛

PaddlePaddle + 论坛会议

PaddlePaddle + 论文

PaddlePaddle + 前沿分享

PaddlePaddle + 场景应用

PaddlePaddle + PaddlePaddle大佬名字

PaddlePaddle + 公司项目
等等才能完全熟悉PaddlePaddle




```
## 参考资料
1. 飞桨框架v2.4 API新升级！全面支持稀疏计算、图学习、语音处理等任务：https://mp.weixin.qq.com/s/8IYYEbJqIjyWd2zO7TGGFw
2. PaddleBox：百度基于GPU的超大规模离散DNN模型训练解决方案：https://mp.weixin.qq.com/s/o-ZoRnAMnINGHVALj7DQRA
3. 大模型时代的异构计算平台：https://mp.weixin.qq.com/s/ZAP_8ZwkZ295I225QTh9Yw
4. 

## 基本概念
1. ao
2. amp
3. autograd
4. nn
5. layer
6. torch
7. aot
   1. Ahead-of-Time (AOT) 的缩写，它是一种编译技术，用于在运行之前将代码编译成机器代码。与即时编译（Just-in-Time, JIT）相反，AOT编译在程序运行之前完成，将源代码或中间表示（如抽象语法树）转换为机器代码。
8. jit
9. qat
   1. 量化感知训练（Quantization Aware Training），是一种用于量化神经网络的训练方法。在深度学习中，通常使用浮点数进行计算和训练，但浮点数计算需要较大的存储和计算资源。量化是一种将浮点数模型转换为定点数模型的技术，可以在一定程度上减少模型的存储空间和计算量，从而提高模型的效率。
10. sparse
11. pruning

## 基本函数
1. unsqueeze
2. unique
3. empty
4. randint
5. arange
6. clamp or clip
7. no_grad 禁止梯度计算

## 源码
### 编译
参考 机器学习解决方案



### 模块架构 - 目录
1. data_loader phi_dynamic_loader
2. dynamic_loader
3. tensor
   1. tensor_meta
   2. tensor_base
   3. tensor_array
   4. sparse_csr_tensor
4. 算法相关
   1. blas
5. 性能优化
   1. prune
   2. eigen_function
   3. pooling
   4. cross_entropy
   5. matrix_reduce
   6. cos_sim_functor
   7. fft
   8. elementwise
   9. fusion
6. 非核心
   1. workqueue_utils
   2. memory_utils
   3. profiler_utils
   4. op_version_registry
   5. threadpool
   6. place
   7. ddim
   8. mlu_tracer custom_tracer cuda_tracer

### 模块架构 - 横向分析
1. Op 和 Kernel 
2. layer
3. torchbind
4. jitbackend MIR
5. SSA Graph 
6. 推理引擎

### 图模块
1. 图拆解
   1. 动态图
      1. final_dygraph_node
      2. final_dygraph_function
      3. dygraph_function
      4. dygraph_node
   2. 静态图
   3. subgraph_util
   4. subgraph_detector
   5. graph_helper
   6. phi_dygraph_api
   7. graph_traits
   8. graph
   9. cuda_graph_with_memory_pool
   10. staticgraph_executor_statistics
2. 图并行
   1. fast_threaded_ssa_graph_executor
   2. scope_buffered_ssa_graph_executor
   3. bind_threaded_ssa_graph_executor
   4. threaded_ssa_graph_executor
   5. ssa_graph_executor
3. 图算子
   1. op_graph_view
   2. graph_khop_sampler_op
   3. graph_sample_neighbors_op
   4. graph_reindex_op
4. ir + pass
   1. ir_graph_build_pass
   2. ir_graph_to_program_pass
   3. graph_to_program_pass
5. pass
   1. multi_devices_graph_pass
   2. multi_devices_graph_print_pass
   3. multi_devices_graph_check_pass
   4. graph_pattern_detector
   
### 图代码
1. paddle/distributed/auto_parallel/graph.py
2. github/baidu_paddle/paddle/fluid/framework/ir/node.h
3. github/baidu_paddle/paddle/fluid/operators/graph_reindex_op.cc




### python模块
1. paddle
   1. autograd
   2. nn
   3. distributed distribution
   4. inference
2. cinn 自动调优框架
   1. https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/cinn/auto_schedule_cn.html
   2. CINN 在算子(融合算子)实现时采用的是 compute 与 schedule 分离的思想，compute 表示算子的朴素计算语义，schedule 表示具体的计算方式。auto-schedule 的作用是自动生成算子的 schedule 配置，降低新硬件接入编译器的人力成本和技术门槛，迎合追求极致性能场景的优化需求, 以下简要介绍自动调优框架在 CINN 整体架构中的位置和核心模块的功能。
   3. https://github.com/PaddlePaddle/CINN/tree/develop
   4. auto_schedule
   5. ir compiler runtime framework frontend


### 垃圾回收器
1. github/Paddle/paddle/fluid/framework/new_executor/garbage_collector

### 任务队列
1. github/Paddle/paddle/fluid/framework/new_executor/workqueue


### 模型结构 和 可视化
1. https://www.paddlepaddle.org.cn/inference/master/guides/export_model/visual_model.html
2. 导出模型：https://www.paddlepaddle.org.cn/inference/master/guides/export_model/index_export_model.html



## 测试开发流程
1. 插件和编译器 - 参考vscode解决方案
   1. 几乎无痛的VSCode+clangd+lldb+cmake配置C/C++开发环境指南 - 仿身泪滴的文章 - 知乎 https://zhuanlan.zhihu.com/p/566365173
   2. apt install clang clangd lldb -y
2. 编译注意 - 参考vscode解决方案
   1. ccache 加速编译
   2. cmake 必须加上 -DWITH_TESTING=ON，才能生成test目标文件
3. 编译后的python包路径
   1. Paddle/build/python/dist/paddlepaddle-0.0.0-cp38-cp38-linux_x86_64.whl
   2. pip install paddlepaddle-0.0.0-cp38-cp38-linux_x86_64.whl
4. 测试
   1. paddle 2.3.0
      1. 测试目录在 https://github.com/PaddlePaddle/Paddle/blob/v2.3.0/python/paddle/fluid/tests/unittests/test_accuracy_op.py
   2. paddle 2.6.0
      1. 测试目录在 https://github.com/PaddlePaddle/Paddle/blob/v2.6.0/test/legacy_test/test_accuracy_op.py
5. 运行单元测试
   1. cpp test bin路径 
      1. /docker/root/projects/demo/github/Paddle/build/test/cpp    
   2. python路径 根据 paddle版本来决定
   3. build 目录下，以 ctest ${test_name} 的命令运行
   4. ctest test_logsumexp
   5. ctest -R test_logsumexp 可以运行所有以 test_logsumexp 开头的单测 target.
   6. ctest -V -R test_logsumexp 单元测试输出更详细的信息以便 debug 时
6. 附录文档
   1. API 设计和命名规范：https://github.com/PaddlePaddle/docs/blob/develop/docs/dev_guides/api_contributing_guides/api_design_guidelines_standard_cn.md#api%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84%E8%A7%84%E8%8C%83
   2. python端开发指南：https://www.paddlepaddle.org.cn/documentation/docs/zh/2.3/dev_guides/api_contributing_guides/new_python_api_cn.html
   3. Op开发手册：https://github.com/PaddlePaddle/Paddle/wiki/Operator-Development-Manual-Index

### ccache 是否真的工作
```
ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /etc/ccache.conf
stats updated                       Sat May  4 03:14:18 2024
cache hit (direct)                     0
cache hit (preprocessed)               0
cache miss                             0
cache hit rate                      0.00 %
no input file                          2
cleanups performed                     0
files in cache                         0
cache size                           0.0 kB


正常工作的情况
ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /etc/ccache.conf
stats updated                       Sat May  4 09:33:51 2024
cache hit (direct)                  1058
cache hit (preprocessed)               0
cache miss                          2010
cache hit rate                     34.49 %
compile failed                         7
ccache internal error                  6
cache file missing                     1
no input file                         12
cleanups performed                   105
files in cache                       166
cache size                         625.6 MB
max cache size                       1.0 GB

```
### 异常 - 无法import paddle
```


```

### 快速验证 对比pytorch
```
python3.8

pip install -i https://mirrors.aliyun.com/pypi/simple paddlepaddle==2.6.0

pip install -i https://mirrors.aliyun.com/pypi/simple torch==2.3.0

```



## 重要第三方库
### mkldnn
1. graph_compiler
   1. 各种矩阵乘法 和 阶乘实现


## 代码串讲
### PIR 源码阅读指南
1. https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/IR_Dialect/first_step.md

### norm 区别
```
这么多norm函数，应该用哪个，平时怎么用，如何用？
返回结果有差异
linalg 实现上更丰富
nn.functional.norm 主要实现l1 l2


./paddle/distributed/auto_parallel/static/operators/dist_layer_norm.py
./paddle/distributed/auto_parallel/static/operators/dist_pnorm.py
./paddle/nn/initializer/normal.py
./paddle/nn/functional/norm.py
./paddle/nn/layer/norm.py
./paddle/nn/utils/spectral_norm_hook.py
./paddle/nn/utils/weight_norm_hook.py
./paddle/nn/utils/clip_grad_norm_.py
./paddle/distribution/multivariate_normal.py
./paddle/distribution/lognormal.py
./paddle/distribution/normal.py
./paddle/sparse/nn/layer/norm.py
./paddle/incubate/nn/functional/fused_rms_norm.py
./paddle/incubate/nn/functional/fused_layer_norm.py




11 results - 10 files

github/Paddle/python/paddle/nn/functional/norm.py:
  30  
  31: def normalize(x, p=2, axis=1, epsilon=1e-12, name=None):
  32      r"""

github/Paddle/python/paddle/nn/utils/spectral_norm_hook.py:
  23  
  24: def normal_(x, mean=0.0, std=1.0):
  25      temp_value = paddle.normal(mean, std, shape=x.shape)

github/Paddle/python/paddle/nn/utils/weight_norm_hook.py:
  48  
  49: def norm_except_dim(p, dim):
  50      shape = p.shape

github/Paddle/python/paddle/static/io.py:
  199  
  200: def normalize_program(program, feed_vars, fetch_vars, **kwargs):
  201      """

github/Paddle/python/paddle/tensor/linalg.py:
  938  
  939: def norm(x, p=None, axis=None, keepdim=False, name=None):
  940      """

github/Paddle/python/paddle/tensor/random.py:
  683  
  684: def normal(mean=0.0, std=1.0, shape=None, name=None):
  685      """

  791  @dygraph_only
  792: def normal_(x, mean=0.0, std=1.0, name=None):
  793      """

github/Paddle/python/paddle/utils/cpp_extension/extension_utils.py:
  532  
  533: def normalize_extension_kwargs(kwargs, use_cuda=False):
  534      """

github/Paddle/python/paddle/vision/transforms/functional_cv2.py:
  682  
  683: def normalize(img, mean, std, data_format='CHW', to_rgb=False):
  684      """Normalizes a ndarray image or image with mean and standard deviation.

github/Paddle/python/paddle/vision/transforms/functional_tensor.py:
  158  
  159: def normalize(img, mean, std, data_format='CHW'):
  160      """Normalizes a tensor image given mean and standard deviation.

github/Paddle/python/paddle/vision/transforms/functional.py:
  958  
  959: def normalize(img, mean, std, data_format='CHW', to_rgb=False):
  960      """Normalizes a tensor or image with mean and standard deviation.


```

### paddle.nn.functional normal章节
1. normalize 
   1. 归一化函数。它使用Lp范数来计算归一化的结果
   2. 在数学上，Lp范数是一个向量空间中的范数，用于衡量向量中元素的大小。
   3. p是范数的指数值，通常取大于等于1的实数。当p=2时，即为欧几里得范数（Euclidean Norm），也称为2-范数或L2范数。
   4. 当p=1时，即为曼哈顿范数（Manhattan Norm），也称为1-范数或L1范数。
2. batch_norm
3. layer_norm
4. instance_norm
5. local_response_norm
6. group_norm
7. 


### paddle.nn.functional loss章节
1. BCELoss
2. SampledSoftmaxLoss

### paddle.tensor math章节
1. 这里充分运用了python可解释性和语法解析的灵活性
2. 对比sql dsl来看，这样的设计灵活性更强
```
def logaddexp(x, y, name=None):
    """
    ..  math::

        Out=log(X.exp()+Y.exp())

    return paddle.log1p(paddle.exp(-paddle.abs(x - y))) + paddle.maximum(x, y)


```

### torch.clamp = paddle.clip
```
PyTorch 1.8 与 Paddle 2.0 API 映射表

https://www.paddlepaddle.org.cn/documentation/docs/zh/2.4/guides/model_convert/pytorch_api_mapping_cn.html

```

### optimizer 章节
```
github/Paddle/python/paddle/optimizer/optimizer.py

adagrad.py：AdaGrad优化器的实现。
adamax.py：Adamax优化器的实现。
asgd.py：平均随机梯度下降（Average Stochastic Gradient Descent）优化器的实现。
lbfgs.py：L-BFGS优化器的实现。
momentum.py：动量优化器的实现。
rmsprop.py：RMSProp优化器的实现。
sgd.py：随机梯度下降（Stochastic Gradient Descent）优化器的实现。
adadelta.py：AdaDelta优化器的实现。
adam.py：Adam优化器的实现。
adamw.py：AdamW优化器的实现。
lamb.py：LAMB（Layer-wise Adaptive Moments optimizer for Batch training）优化器的实现。
lr.py：学习率调度器的实现。
optimizer.py：优化器基类的实现。
rprop.py：Rprop（Resilient Backpropagation）优化器的实现。


梯度清零
pytorch opt.zero_grad()
paddle  opt.clear_grad()
```


### autograd 章节



## 模型加载
1. jit load

### paddle jit python模块
```
__init__.py: 这个文件通常用于将目录标记为Python包，可能还包含一些初始化代码。

api.py: 定义了PaddlePaddle JIT功能的API接口，允许用户以编程方式访问JIT相关功能。

dy2static 目录: 包含将动态图转换为静态图所需的工具和模块。

__init__.py: 初始化dy2static包。
ast_utils.py: 包含用于操作抽象语法树（AST）的实用工具。
convert_call_func.py: 用于转换函数调用。
convert_operators.py: 用于转换操作符。
error.py: 定义了转换过程中可能遇到的错误类型。
export_subgraph.py: 用于导出子图。
function_spec.py: 包含函数规范的描述。
logging_utils.py: 包含日志记录工具。
origin_info.py: 包含原始信息处理工具。
partial_program.py: 包含部分程序的表示。
pir_partial_program.py: 包含Paddle Intermediate Representation（PIR）的部分程序表示。
program_translator.py: 用于翻译程序的模块。
py_layer.py: 包含Python层的表示。
layer.py: 定义了深度学习层的抽象，这些层可以被JIT编译。


pir_dy2static 目录: 包含Paddle Intermediate Representation（PIR）到静态图转换相关的模块。

__init__.py: 初始化pir_dy2static包。
parameter_recorder.py: 用于记录参数信息。
sot 目录: 包含静态操作码翻译（Static Operation Translator）相关的模块。

__init__.py: 初始化sot包。
infer_meta.py: 用于推断元数据。
opcode_translator 目录: 包含操作码翻译相关的模块。
__init__.py: 初始化opcode_translator包。
breakpoint.py: 可能用于处理断点。
custom_code.py: 包含自定义代码的处理。
eval_frame_callback.py: 包含评估帧回调的处理。
executor 目录: 包含执行静态图所需的组件。
__init__.py: 初始化executor包。
其他文件包含执行器的内部组件，如分发函数、指令标志等。
instruction_utils 目录: 包含指令分析和转换的工具。
skip_files.py: 可能用于跳过某些文件的处理。
profiler.py: 用于性能分析。
psdb.py: 可能与性能数据库有关。
symbolic 目录: 包含符号执行相关的模块。
compile_cache.py: 可能用于编译缓存。
export.py: 用于导出符号表示。
interpreter.py: 包含解释器的实现。
statement_ir.py: 包含语句的中间表示。
symbolic_context.py: 包含符号执行上下文。
translate.py: 用于翻译的模块。
utils 目录: 包含实用工具。
__init__.py: 初始化utils包。
其他文件包含特定实用工具的实现。
translated_layer.py: 包含被JIT编译后的层的表示。

utils.py: 包含一些通用的实用工具。
```

### TranslatedLayer


## 训练
1. 单机多卡与多机多卡组网示例：https://aistudio.baidu.com/projectdetail/1222066
### 单机单卡


### 单机多卡
1. 建议使用spawn方式
   
#### 高层API
```

当调用paddle.Model高层API来实现训练时，想要启动单机多卡训练非常简单，代码不需要做任何修改，只需要在启动时增加一下参数-m paddle.distributed.launch。

  #单机单卡启动，默认使用第0号卡
  $ python train.py
  
  #单机多卡启动，默认使用当前可见的所有卡
  $ python -m paddle.distributed.launch train.py

  #单机多卡启动，设置当前使用的第0号和第1号卡
  $ python -m paddle.distributed.launch --selected_gpus='0,1' train.py

  #单机多卡启动，设置当前使用第0号和第1号卡
  $ export CUDA_VISIABLE_DEVICES='0,1'
  $ python -m paddle.distributed.launch train.py


```

#### 基础API
```
https://aistudio.baidu.com/projectdetail/1222066

修改三处：

#第1处改动，import库
import paddle.distributed as dist

#第2处改动，初始化并行环境
dist.init_parallel_env()

#第3处改动，增加paddle.DataParallel封装
net = paddle.DataParallel(paddle.vision.models.LeNet())


import paddle.distributed as dist
   
# 启动train多进程训练，默认使用所有可见的GPU卡
if __name__ == '__main__':
   dist.spawn(train)

# 启动train函数2个进程训练，默认使用当前可见的前2张卡
if __name__ == '__main__':
   dist.spawn(train, nprocs=2)

# 启动train函数2个进程训练，默认使用第4号和第5号卡
if __name__ == '__main__':
   dist.spawn(train, nprocs=2, selelcted_gpus='4,5')spawn方式

总结
spawn方式不需要去修改代码的内部部分，只是加上dist.spawn(train)这句，相当于给训练代码加了一个多进程的壳，简单方便，是推荐使用的单机多卡组网方式！

spawn方式下在notebook里报错的情况，猜测应该是notebook进程管理限制导致的。在命令行情况下或者cell里加叹号运行的时候，就没有问题。

在不支持spawn的情况下，再去考虑用launch方式启动单机多卡。

```



### 多机多卡
1. 使用Fleet分布式训练方式

#### fleetrun启动分布式任务
```
GPU单机多卡训练
若启动单机4卡的任务，只需通过--gpus指定空闲的4张卡即可。

    fleetrun --gpus=0,1,2,3 train.py

如果指定了export CUDA_VISIBLE_DEVICES=0,1,2,3，则可以直接使用：
export CUDA_VISIBLE_DEVICES=0,1,2,3
    fleetrun train.py



[示例一] 2机8卡 (每个节点4卡)
fleetrun --ips="xx.xx.xx.xx,yy.yy.yy.yy" --gpus=0,1,2,3 train.py


[示例二] 2机16卡（每个节点8卡，假设每台机器均有8卡可使用）
fleetrun --ips="xx.xx.xx.xx,yy.yy.yy.yy" train.py



```


## 模型预估
1. TranslatedLayer

## paddle 新增 FeatureAlphaDropout API
1. 报名：https://github.com/PaddlePaddle/Paddle/issues/62905
2. 新增流程：https://github.com/PaddlePaddle/community/blob/master/hackathon/hackathon_6th/%E3%80%90Hackathon%206th%E3%80%91%E5%BC%80%E6%BA%90%E8%B4%A1%E7%8C%AE%E4%B8%AA%E4%BA%BA%E6%8C%91%E6%88%98%E8%B5%9B%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91%E4%BB%BB%E5%8A%A1%E5%90%88%E9%9B%86.md#no8-%E4%B8%BA-paddle-%E6%96%B0%E5%A2%9E-featurealphadropout-api
3. 参考pr：https://github.com/PaddlePaddle/community/pull/848
4. 参考paddle 算子pr：https://github.com/PaddlePaddle/Paddle/pull/62934/files#diff-dd4ce82a4831b8c3f62aa1717373fce4dd62e1f42540bc8395df5e3c447a0475
5. 代码修改：Python 实现代码 & 英文 API 文档，在 Paddle repo 的 python/paddle/nn/layer/common.py 中实现 FeatureAlphaDropout 类，并在 python/paddle/nn/layer/init.py、python/paddle/nn/init.py 添加对应调用。
6. 单元测试：https://github.com/PaddlePaddle/Paddle/tree/develop/test
7. 中文api：https://github.com/PaddlePaddle/docs/tree/develop/docs/api/paddle


### dropout python冒烟调用
```py
import paddle
paddle.seed(2023)
x = paddle.to_tensor([[-1, 1], [-1, 1]], dtype="float32")
m = paddle.nn.AlphaDropout(p=0.5)
y_train = m(x)
print(y_train)

m.eval()  # switch the model to test phase
y_test = m(x)
print(y_test)

```

### paddle - dropout修改点
1. 
### dropout整理
1. pytorch注册
   1. dropout
   2. alpha_dropout
   3. feature_alpha_dropout
   4. dropout1d
   5. dropout2d
   6. dropout3d
   7. github/pytorch/aten/src/ATen/native/Dropout.cpp
   8. github/pytorch/torch/include/ATen/ops/feature_alpha_dropout.h
   9. github/pytorch/torch/include/ATen/ops/feature_alpha_dropout_ops.h
   10. github/pytorch/torch/include/ATen/ops/feature_alpha_dropout_meta.h
   11. github/pytorch/torch/include/ATen/ops/feature_alpha_dropout_native.h
   12. github/pytorch/torch/include/ATen/ops/feature_alpha_dropout_compositeimplicitautograd_dispatch.h
   13. github/pytorch/torch/include/torch/csrc/api/include/torch/nn/functional/dropout.h
   14. github/pytorch/torch/include/ATen/core/aten_interned_strings.h
   15. github/pytorch/torch/nn/modules/dropout.py
   16. github/pytorch/torch/share/ATen/Declarations.yaml
   17. github/pytorch/torch/onnx/symbolic_opset9.py
   18. github/pytorch/torch/nn/functional.pyi.in
   19. github/pytorch/torch/nn/functional.py
   20. github/pytorch/aten/src/ATen/functorch/BatchRulesDecompositions.cpp
   21. github/pytorch/aten/src/ATen/functorch/PyTorchOperatorHacks.cpp
   22. github/pytorch/torch/csrc/autograd/generated/python_torch_functionsEverything.cpp
   23. github/pytorch/aten/src/ATen/native/cuda/Dropout.cu
   24. github/pytorch/torch/csrc/api/include/torch/nn/functional/dropout.h
   25. github/pytorch/torch/csrc/api/include/torch/nn/options/dropout.h
   26. github/pytorch/torch/csrc/api/src/nn/modules/dropout.cpp
   27. github/pytorch/torch/nn/modules/__init__.py
   28. github/pytorch/torch/nn/modules/dropout.py
2. pytorch测试
   1. github/pytorch/torch/testing/_internal/dynamo_test_failures.py
   2. github/pytorch/torch/testing/_internal/jit_metaprogramming_utils.py
   3. github/pytorch/torch/testing/_internal/common_methods_invocations.py
   4. github/pytorch/test/functorch/test_vmap.py
   5. github/pytorch/test/cpp/api/functional.cpp
   6. github/pytorch/test/cpp/api/modules.cpp
   7. github/pytorch/test/nn/test_dropout.py
3. pytorch文档
   1. https://pytorch.org/docs/stable/generated/torch.nn.FeatureAlphaDropout.html
   2. https://pytorch.org/docs/stable/_modules/torch/nn/modules/dropout.html#FeatureAlphaDropout
4. 具体实现
   1. _dropout_impl 
   2. ALIAS_SPECIALIZATION，它接受三个参数：ALIAS_NAME、IS_FEATURE 和 IS_ALPHA
   3. _feature_alpha_dropout = IS_FEATURE=true IS_ALPHA=true




## 附录
### 静态库编译顺序
```

[ 12%] Linking CXX static library libstring_array.a
[ 12%] Linking CXX static library libtensor_base.a
[ 12%] Linking CXX static library libworkqueue_utils.a
[ 12%] Linking CXX static library libop_version_registry.a
[ 12%] Linking CXX static library libdevice_mesh.a
[ 12%] Linking CXX static library libtensor_meta.a
[ 12%] Linking CXX static library libphi_os_info.a
[ 12%] Linking CXX static library libprune.a
[ 12%] Linking CXX static library libattribute.a
[ 12%] Linking CXX static library libarg_map_context.a
[ 12%] Linking CXX static library libthreadpool.a
[ 12%] Linking CXX static library libplace.a
[ 12%] Linking CXX static library libddim.a
[ 12%] Linking CXX static library libmlu_tracer.a
[ 12%] Linking CXX static library libmemory_utils.a
[ 12%] Linking CXX static library libprofiler_utils.a
[ 12%] Linking CXX static library libextended_tensor.a
[ 13%] Linking CXX static library liblod_utils.a
[ 13%] Linking CXX static library libget_kerneltype_forvar_utils.a
[ 13%] Linking CXX static library libcustom_tracer.a
[ 14%] Linking CXX static library libcache.a
[ 15%] Linking CXX static library libcustom_device_resource_pool.a
[ 15%] Linking CXX static library libphi_profiler.a
[ 15%] Linking CXX static library libprocess_mesh.a
[ 15%] Linking CXX static library liboperants_manager.a
[ 15%] Linking CXX static library libtcp_store.a
[ 15%] Linking CXX static library libtask_loop_thread_pool.a
[ 15%] Linking CXX static library libshell.a
[ 16%] Linking CXX static library libworkqueue.a
[ 16%] Linking CXX static library libdata_loader.a
[ 16%] Linking CXX static library libpaddle_crypto.a
[ 16%] Linking CXX static library libbenchmark.a
[ 16%] Linking CXX static library libphi_dynamic_loader.a
[ 17%] Linking CXX static library libdist_mapper.a
[ 17%] Linking CXX static library libstaticgraph_executor_statistics.a
[ 17%] Linking CXX static library libop_utils.a
[ 17%] Linking CXX static library libsparse_coo_tensor.a
[ 17%] Linking CXX static library libphi_dynload_warprnnt.a
[ 17%] Linking CXX static library libphi_dynload_warpctc.a
[ 17%] Linking CXX static library libphi_dynload_lapack.a
[ 17%] Linking CXX static library libgenerator.a
[ 17%] Linking CXX static library libcuda_tracer.a
[ 17%] Linking CXX static library libtensor_api.a
[ 17%] Linking CXX static library libstats.a
[ 17%] Linking CXX static library libdynamic_loader.a
[ 17%] Linking CXX static library libcomm_context_manager.a
[ 17%] Linking CXX static library libphi_dynload_mklml.a
[ 17%] Linking CXX static library libswitch_autotune.a
[ 17%] Linking CXX static library libfs.a
[ 17%] Linking CXX static library libevent_node.a
[ 17%] Linking CXX static library libdynload_warpctc.a
[ 17%] Linking CXX static library libdynload_mklml.a
[ 17%] Linking CXX static library libcblas.a
[ 17%] Linking CXX static library libcpu_helper.a
[ 19%] Linking CXX static library libprofiler_logger.a
[ 19%] Linking CXX static library libphi_backends.a
[ 19%] Linking CXX static library libevent_bind.a
[ 19%] Linking CXX static library libconvert_utils.a
[ 20%] Linking CXX static library libphi_device_context.a
[ 20%] Linking CXX static library libselected_rows.a
[ 20%] Linking CXX static library libdense_tensor.a
[ 20%] Linking CXX static library libcpu_utilization.a
[ 20%] Linking CXX static library libops_extra_info.a
[ 20%] Linking CXX static library libtensor_array.a
[ 20%] Linking CXX static library libsparse_csr_tensor.a
[ 20%] Linking CXX static library libstring_tensor.a
[ 20%] Linking CXX static library libmeta_tensor.a
[ 20%] Linking CXX static library libblas.a
[ 21%] Linking CXX static library libphi_c_device_context.a
[ 21%] Linking CXX static library libkernel_context.a
[ 21%] Linking CXX static library libkernel_factory.a
[ 21%] Linking CXX static library libphi_c_data_type.a
[ 21%] Linking CXX static library libphi_c_tensor.a
[ 21%] Linking CXX static library libcomm_static_check.a
[ 21%] Linking CXX static library libphi_c_kernel_context.a
[ 21%] Linking CXX static library libphi_c_kernel_registry.a
[ 22%] Linking CXX static library libprocess_group.a
[ 22%] Linking CXX static library libsparse_backward_infermeta.a
[ 22%] Linking CXX static library libinfermeta_utils.a
[ 22%] Linking CXX static library libcustom_kernel.a
[ 22%] Linking CXX static library libphi_c_kernel_factory.a
[ 22%] Linking CXX static library libbackward_infermeta.a
[ 22%] Linking CXX static library libscope.a
[ 22%] Linking CXX static library libop_proto_maker.a
[ 22%] Linking CXX static library libsparse_infermeta.a
[ 22%] Linking CXX static library libstring_infermeta.a
[ 22%] Linking CXX static library libop_call_stack.a
[ 23%] Linking CXX static library libeigen_function.a
[ 23%] Linking CXX static library libvar_type_traits.a
[ 23%] Linking CXX static library libinfermeta.a
[ 23%] Linking CXX static library libscope_pool.a
[ 23%] Linking CXX static library libnan_inf_utils.a
[ 23%] Linking CXX static library libhost_tracer.a
[ 23%] Linking CXX static library libop_compat_infos.a
[ 23%] Linking CXX static library libnew_profiler.a
[ 23%] Linking CXX static library libselected_rows_utils.a
[ 23%] Linking CXX static library libshape_inference.a
[ 23%] Linking CXX static library libprofiler.a
[ 23%] Linking CXX static library libdevice_context.a
[ 24%] Linking CXX static library liballocator.a
[ 24%] Linking CXX static library libmalloc.a
[ 24%] Linking CXX static library libmaxouting.a
[ 24%] Linking CXX static library libgpc.a
[ 24%] Linking CXX static library libjit_kernel_base.a
[ 24%] Linking CXX static library libconcat_and_split_functor.a
[ 24%] Linking CXX static library libim2col.a
[ 24%] Linking CXX static library libmemcpy.a
[ 24%] Linking CXX static library liblstm_compute.a
[ 24%] Linking CXX static library liblapack_function.a
[ 24%] Linking CXX static library libno_need_buffer_vars_inference.a
[ 24%] Linking CXX static library libsequence_scale.a
[ 24%] Linking CXX static library libsequence_padding.a
[ 24%] Linking CXX static library libvol2col.a
[ 24%] Linking CXX static library libpooling.a
[ 24%] Linking CXX static library libcross_entropy.a
[ 24%] Linking CXX static library libdeformable_conv_functor.a
[ 24%] Linking CXX static library libop_kernel_type.a
[ 24%] Linking CXX static library libmatrix_bit_code.a
[ 24%] Linking CXX static library libinit.a
[ 24%] Linking CXX static library libmatrix_reduce.a
[ 24%] Linking CXX static library libheter_wrapper.a
[ 24%] Linking CXX static library libop_info.a
[ 24%] Linking CXX static library libmatrix_inverse.a
[ 24%] Linking CXX static library libtransfer_scope_cache.a
[ 24%] Linking CXX static library libcollective_helper.a
[ 24%] Linking CXX static library libcos_sim_functor.a
[ 24%] Linking CXX static library libconcat_and_split.a
[ 24%] Linking CXX static library libsequence2batch.a
[ 24%] Linking CXX static library libmemory.a
[ 24%] Linking CXX static library libsampler.a
[ 24%] Linking CXX static library libsample_prob.a
[ 24%] Linking CXX static library libsegment_pooling.a
[ 24%] Linking CXX static library libscope_buffered_monitor.a
[ 24%] Linking CXX static library libjit_kernel_intrinsic.a
[ 25%] Linking CXX static library libcuda_graph_with_memory_pool.a
[ 25%] Linking CXX static library libunpooling.a
[ 25%] Linking CXX static library libdevice_code.a
[ 25%] Linking CXX static library libjit_kernel_refer.a
[ 26%] Linking CXX static library libjit_kernel_mix.a
[ 26%] Linking CXX static library libjit_kernel_mkl.a
[ 26%] Linking CXX static library libunused_var_check.a
[ 26%] Linking CXX static library libfft.a
[ 26%] Linking CXX static library libphi_tensor_utils.a
[ 26%] Linking CXX static library libcontext_pool.a
[ 26%] Linking CXX static library libmask_util.a
[ 26%] Linking CXX static library libinit_phi.a
[ 26%] Linking CXX static library libjit_kernel_jitcode.a
[ 26%] Linking CXX static library libjit_kernel_helper.a
[ 26%] Linking CXX static library libgarbage_collector.a
[ 26%] Linking CXX static library libmixed_vector.a
[ 26%] Linking CXX static library libint_array.a
[ 26%] Linking CXX static library libscalar.a
[ 26%] Linking CXX static library libphi_c_int_array.a
[ 26%] Linking CXX static library libphi_c_scalar.a
[ 26%] Linking CXX static library libfc_functor.a
[ 26%] Linking CXX static library libtensor.a
[ 26%] Linking CXX static library libphi_capi.a
[ 26%] Linking CXX static library libprocess_group_custom.a
[ 26%] Linking CXX static library liblayout_autotune.a
[ 26%] Linking CXX static library libphi_tensor_raw.a
[ 26%] Linking CXX static library libdata_device_transform.a
[ 26%] Linking CXX static library libgather_scatter_functor.a
[ 26%] Linking CXX static library libphi_data_layout_transform.a
[ 27%] Linking CXX static library libdlpack_tensor.a
[ 28%] Linking CXX static library liblod_tensor.a
[ 28%] Linking CXX static library libapi_tensor_utils.a
[ 28%] Linking CXX static library libjit_property.a
[ 28%] Linking CXX static library libapi_gen_utils.a
[ 28%] Linking CXX static library libkernel_dispatch.a
[ 28%] Linking CXX static library libdata_type_transform.a
[ 28%] Linking CXX static library libvar_helper.a
[ 28%] Linking CXX static library libmkldnn_quantizer_config.a
[ 28%] Linking CXX static library libop_meta_info.a
[ 28%] Linking CXX static library libreader.a
[ 28%] Linking CXX static library libprocessgroup_comm_utils.a
[ 28%] Linking CXX static library libreset_tensor_array.a
[ 28%] Linking CXX static library libbox_wrapper.a
[ 28%] Linking CXX static library libpybind_util.a
[ 28%] Linking CXX static library liblod_rank_table.a
[ 28%] Linking CXX static library libvariable_visitor.a
[ 28%] Linking CXX static library libmath_function.a
[ 28%] Linking CXX static library libzero_copy_tensor.a
[ 28%] Linking CXX static library libdevice_worker.a
[ 28%] Linking CXX static library libfeed_fetch_method.a
[ 28%] Linking CXX static library libpy_reader.a
[ 28%] Linking CXX static library libvariable_helper.a
[ 28%] Linking CXX static library libanalysis_config.a
[ 28%] Linking CXX static library libjit_serializer.a
[ 28%] Linking CXX static library libbuffered_reader.a
[ 28%] Linking CXX static library libgru_compute.a
[ 28%] Linking CXX static library libdata_layout_transform.a
[ 28%] Linking CXX static library libcontext_project.a
[ 28%] Linking CXX static library libtree2col.a
[ 28%] Linking CXX static library libselected_rows_functor.a
[ 28%] Linking CXX static library libpaddle_infer_contrib.a
[ 28%] Linking CXX static library libsoftmax.a
[ 28%] Linking CXX static library libbeam_search.a
[ 28%] Linking CXX static library liblodtensor_printer.a
[ 28%] Linking CXX static library libmatrix_solve.a
[ 29%] Linking CXX static library libsequence_pooling.a
[ 29%] Linking CXX static library libgloo_wrapper.a
[ 29%] Linking CXX static library libfleet_wrapper.a
[ 29%] Linking CXX static library libdata_transform.a
[ 29%] Linking CXX static library libps_gpu_wrapper.a
[ 29%] Linking CXX static library libmetrics.a
[ 46%] Linking CXX static library libphi_cpu.a
[ 46%] Linking CXX static library libapi_int_array.a
[ 46%] Linking CXX static library libapi_scalar.a
[ 47%] Linking CXX static library libtensor_copy.a
[ 47%] Linking CXX static library libphi.a
[ 49%] Linking CXX static library libstrings_api.a
[ 49%] Linking CXX static library libphi_data_transform.a
[ 49%] Linking CXX static library libwrapped_infermeta.a
[ 49%] Linking CXX static library libphi_utils.a
[ 49%] Linking CXX static library libapi_custom_impl.a
[ 49%] Linking CXX static library libsparse_api.a
[ 49%] Linking CXX static library libsparse_bw_api.a
[ 49%] Linking CXX static library libinfershape_utils.a
[ 49%] Linking CXX static library libproto_desc.a
[ 49%] Linking CXX static library liboperator.a
[ 49%] Linking CXX static library libdist_attr.a
[ 49%] Linking CXX static library libnode.a
[ 49%] Linking CXX static library libprogram_utils.a
[ 49%] Linking CXX static library libop_compatible_info.a
[ 49%] Linking CXX static library libargument.a
[ 49%] Linking CXX static library libanalysis_pass.a
[ 49%] Linking CXX static library libstatic_global_utils.a
[ 49%] Linking CXX static library libop_variant.a
[ 49%] Linking CXX static library libauto_parallel.a
[ 49%] Linking CXX static library libget_expected_kernel_func.a
[ 49%] Linking CXX static library libcommon_infer_shape_functions.a
[ 49%] Linking CXX static library libmodel_utils.a
[ 49%] Linking CXX static library libop_registry.a
[ 49%] Linking CXX static library libvar_handle.a
[ 49%] Linking CXX static library libjit_function_utils.a
[ 49%] Linking CXX static library libjit_serializer_utils.a
[ 49%] Linking CXX static library libphi_function_api.a
[ 49%] Linking CXX static library libprim_utils.a
[ 49%] Linking CXX static library libop_handle_base.a
[ 49%] Linking CXX static library libwhile_op_helper.a
[ 49%] Linking CXX static library libstatic_utils.a
[ 49%] Linking CXX static library libgraph.a
[ 49%] Linking CXX static library libmemory_optim_pass.a
[ 49%] Linking CXX static library libprepared_operator.a
[ 49%] Linking CXX static library libdevice_event_base.a
[ 49%] Linking CXX static library libcustom_device_common_op_registry.a
[ 49%] Linking CXX static library libphi_tensor_operants.a
[ 49%] Linking CXX static library libshare_tensor_buffer_functor.a
[ 50%] Linking CXX static library libcomputation_op_handle.a
[ 50%] Linking CXX static library librpc_op_handle.a
[ 50%] Linking CXX static library libfetch_barrier_op_handle.a
[ 50%] Linking CXX static library libphi_tensor.a
[ 50%] Linking CXX static library libbroadcast_op_handle.a
[ 50%] Linking CXX static library libfetch_async_op_handle.a
[ 50%] Linking CXX static library libpy_func_op.a
[ 50%] Linking CXX static library libreduce_op_handle.a
[ 51%] Linking CXX static library libjit_function_schema.a
[ 51%] Linking CXX static library libgraph_traits.a
[ 51%] Linking CXX static library libphi_dygraph_api.a
[ 51%] Linking CXX static library libscale_loss_grad_op_handle.a
[ 51%] Linking CXX static library libgather_op_handle.a
[ 52%] Linking CXX static library libfused_all_reduce_op_handle.a
[ 52%] Linking CXX static library liball_reduce_op_handle.a
[ 52%] Linking CXX static library libreader_op_registry.a
[ 52%] Linking CXX static library libdevice_event_custom_device.a
[ 52%] Linking CXX static library libmanual_static_prim_api.a
[ 52%] Linking CXX static library libop_graph_view.a
[ 52%] Linking CXX static library libeager_nan_inf_utils.a
[ 52%] Linking CXX static library libfetch_op_handle.a
[ 52%] Linking CXX static library libfused_broadcast_op_handle.a
[ 52%] Linking CXX static library libgenerated_static_prim_api.a
[ 52%] Linking CXX static library libstatic_prim_api.a
[ 52%] Linking CXX static library libshare_tensor_buffer_op_handle.a
[ 52%] Linking CXX static library libgrad_merge_all_reduce_op_handle.a
[ 52%] Linking CXX static library libreference_count_pass_helper.a
[ 52%] Linking CXX static library liblayer.a
[ 52%] Linking CXX static library libstatic_tensor_operants.a
[ 52%] Linking CXX static library libop_desc_meta.a
[ 52%] Linking CXX static library libeager_deletion_op_handle.a
[ 52%] Linking CXX static library libgraph_helper.a
[ 52%] Linking CXX static library libamp.a
[ 52%] Linking CXX static library libgradient_accumulator.a
[ 52%] Linking CXX static library libload_combine_op.a
[ 52%] Linking CXX static library libwarpctc_op.a
[ 53%] Linking CXX static library libsave_combine_op.a
[ 53%] Linking CXX static library libquantize_linear_op.a
[ 53%] Linking CXX static library libbox_coder_op.a
[ 53%] Linking CXX static library libiou_similarity_op.a
[ 53%] Linking CXX static library libdensity_prior_box_op.a
[ 53%] Linking CXX static library libpolygon_box_transform_op.a
[ 53%] Linking CXX static library libbipartite_match_op.a
[ 53%] Linking CXX static library libyolo_box_op.a
[ 53%] Linking CXX static library libprior_box_op.a
[ 53%] Linking CXX static library libtarget_assign_op.a
[ 53%] Linking CXX static library libanchor_generator_op.a
[ 53%] Linking CXX static library libmine_hard_examples_op.a
[ 53%] Linking CXX static library librpn_target_assign_op.a
[ 53%] Linking CXX static library libbox_clip_op.a
[ 53%] Linking CXX static library libgenerate_proposal_labels_op.a
[ 53%] Linking CXX static library libmatrix_nms_op.a
[ 53%] Linking CXX static library liblocality_aware_nms_op.a
[ 53%] Linking CXX static library libmulticlass_nms_op.a
[ 54%] Linking CXX static library libbox_decoder_and_assign_op.a
[ 54%] Linking CXX static library libyolov3_loss_op.a
[ 55%] Linking CXX static library libsigmoid_focal_loss_op.a
[ 55%] Linking CXX static library libretinanet_detection_output_op.a
[ 55%] Linking CXX static library libgenerate_proposals_v2_op.a
[ 55%] Linking CXX static library libgenerate_proposals_op.a
[ 55%] Linking CXX static library libdistribute_fpn_proposals_op.a
[ 55%] Linking CXX static library libgenerate_mask_labels_op.a
[ 55%] Linking CXX static library libroi_perspective_transform_op.a
[ 55%] Linking CXX static library libcollect_fpn_proposals_op.a
[ 55%] Linking CXX static library libelementwise_floordiv_op.a
[ 55%] Linking CXX static library libelementwise_add_op.a
[ 55%] Linking CXX static library libelementwise_div_op.a
[ 55%] Linking CXX static library libelementwise_heaviside_op.a
[ 56%] Linking CXX static library libelementwise_mod_op.a
[ 56%] Linking CXX static library libelementwise_min_op.a
[ 56%] Linking CXX static library libelementwise_max_op.a
[ 56%] Linking CXX static library libfused_adam_op.a
[ 56%] Linking CXX static library libfused_conv2d_op.a
[ 56%] Linking CXX static library libelementwise_mul_op.a
[ 56%] Linking CXX static library libelementwise_pow_op.a
[ 56%] Linking CXX static library libelementwise_sub_op.a
[ 56%] Linking CXX static library libfused_elementwise_op.a
[ 56%] Linking CXX static library libfused_matmul_op.a
[ 56%] Linking CXX static library libfused_embedding_fc_lstm_op.a
[ 56%] Linking CXX static library libfused_softplus_op.a
[ 56%] Linking CXX static library libfused_embedding_seq_pool_op.a
[ 56%] Linking CXX static library libfusion_seqconv_eltadd_relu_op.a
[ 56%] Linking CXX static library libfused_transpose_op.a
[ 56%] Linking CXX static library libfusion_repeated_fc_relu_op.a
[ 56%] Linking CXX static library libfused_seqpool_cvm_op.a
[ 57%] Linking CXX static library libfusion_seqexpand_concat_fc_op.a
[ 57%] Linking CXX static library libfusion_seqpool_concat_op.a
[ 57%] Linking CXX static library libfusion_seqpool_cvm_concat_op.a
[ 57%] Linking CXX static library libfusion_squared_mat_sub_op.a
[ 57%] Linking CXX static library libaccuracy_op.a
[ 57%] Linking CXX static library libmulti_gru_op.a
[ 57%] Linking CXX static library libauc_op.a
[ 57%] Linking CXX static library libadadelta_op.a
[ 57%] Linking CXX static library libfusion_gru_op.a
[ 57%] Linking CXX static library libfusion_lstm_op.a
[ 57%] Linking CXX static library libfused_elemwise_activation_op.a
[ 57%] Linking CXX static library libprecision_recall_op.a
[ 57%] Linking CXX static library libadagrad_op.a
[ 57%] Linking CXX static library libadam_op.a
[ 57%] Linking CXX static library libadamax_op.a
[ 57%] Linking CXX static library libadamw_op.a
[ 57%] Linking CXX static library libdecayed_adagrad_op.a
[ 57%] Linking CXX static library libdistributed_fused_lamb_init_op.a
[ 57%] Linking CXX static library libdgc_momentum_op.a
[ 57%] Linking CXX static library libdpsgd_op.a
[ 57%] Linking CXX static library libdistributed_fused_lamb_op.a
[ 57%] Linking CXX static library libftrl_op.a
[ 57%] Linking CXX static library libmerged_adam_op.a
[ 57%] Linking CXX static library liblars_momentum_op.a
[ 57%] Linking CXX static library libmerged_momentum_op.a
[ 57%] Linking CXX static library libpow2_decay_with_linear_warmup_op.a
[ 57%] Linking CXX static library libmomentum_op.a
[ 57%] Linking CXX static library libproximal_gd_op.a
[ 57%] Linking CXX static library libproximal_adagrad_op.a
[ 57%] Linking CXX static library librmsprop_op.a
[ 57%] Linking CXX static library liblogsumexp_op.a
[ 57%] Linking CXX static library libreduce_amax_op.a
[ 57%] Linking CXX static library libreduce_any_op.a
[ 57%] Linking CXX static library libsparse_momentum_op.a
[ 57%] Linking CXX static library libreduce_amin_op.a
[ 57%] Linking CXX static library libreduce_max_op.a
[ 57%] Linking CXX static library libreduce_min_op.a
[ 57%] Linking CXX static library libreduce_mean_op.a
[ 57%] Linking CXX static library libreduce_prod_op.a
[ 57%] Linking CXX static library libreduce_sum_op.a
[ 57%] Linking CXX static library libsequence_concat_op.a
[ 57%] Linking CXX static library libsequence_erase_op.a
[ 57%] Linking CXX static library libsequence_enumerate_op.a
[ 57%] Linking CXX static library libsequence_expand_as_op.a
[ 57%] Linking CXX static library libsequence_mask_op.a
[ 57%] Linking CXX static library libsequence_conv_op.a
[ 57%] Linking CXX static library libsequence_pad_op.a
[ 57%] Linking CXX static library libsequence_reshape_op.a
[ 57%] Linking CXX static library libsequence_reverse_op.a
[ 58%] Linking CXX static library libsequence_expand_op.a
[ 58%] Linking CXX static library libsequence_pool_op.a
[ 59%] Linking CXX static library libsequence_scatter_op.a
[ 59%] Linking CXX static library libsequence_slice_op.a
[ 59%] Linking CXX static library libsequence_unpad_op.a
[ 59%] Linking CXX static library libsequence_softmax_op.a
[ 59%] Linking CXX static library libadd_p_op.a
[ 59%] Linking CXX static library libsequence_topk_avg_pooling_op.a
[ 59%] Linking CXX static library libabs_p_op.a
[ 59%] Linking CXX static library libbroadcast_p_op.a
[ 59%] Linking CXX static library libbernoulli_p_op.a
[ 59%] Linking CXX static library libfaster_tokenizer_op.a
[ 59%] Linking CXX static library libcast_p_op.a
[ 60%] Linking CXX static library libconcat_p_op.a
[ 60%] Linking CXX static library libcos_p_op.a
[ 60%] Linking CXX static library libdiv_p_op.a
[ 60%] Linking CXX static library libeq_p_op.a
[ 60%] Linking CXX static library liberf_p_op.a
[ 60%] Linking CXX static library libexp_p_op.a
[ 60%] Linking CXX static library libge_p_op.a
[ 60%] Linking CXX static library libfill_constant_p_op.a
[ 60%] Linking CXX static library libgt_p_op.a
[ 60%] Linking CXX static library libgather_p_op.a
[ 60%] Linking CXX static library libmatmul_p_op.a
[ 60%] Linking CXX static library libmax_p_op.a
[ 60%] Linking CXX static library liblog_p_op.a
[ 60%] Linking CXX static library libmul_p_op.a
[ 61%] Linking CXX static library libne_p_op.a
[ 61%] Linking CXX static library libpow_p_op.a
[ 61%] Linking CXX static library librsqrt_p_op.a
[ 61%] Linking CXX static library libreshape_p_op.a
[ 61%] Linking CXX static library libreduce_sum_p_op.a
[ 61%] Linking CXX static library libsin_p_op.a
[ 61%] Linking CXX static library libscatter_add_p_op.a
[ 61%] Linking CXX static library libselect_p_op.a
[ 61%] Linking CXX static library libslice_assign_p_op.a
[ 61%] Linking CXX static library libslice_select_p_op.a
[ 61%] Linking CXX static library libsqrt_p_op.a
[ 61%] Linking CXX static library libsplit_p_op.a
[ 61%] Linking CXX static library libtanh_p_op.a
[ 61%] Linking CXX static library libtranspose_p_op.a
[ 61%] Linking CXX static library libsub_p_op.a
[ 61%] Linking CXX static library liballoc_float_status_op.a
[ 61%] Linking CXX static library libuniform_random_p_op.a
[ 61%] Linking CXX static library libclear_float_status_op.a
[ 61%] Linking CXX static library libcheck_finite_and_unscale_op.a
[ 61%] Linking CXX static library libget_float_status_op.a
[ 61%] Linking CXX static library libcreate_double_buffer_reader_op.a
[ 61%] Linking CXX static library libcreate_py_reader_op.a
[ 61%] Linking CXX static library libread_op.a
[ 61%] Linking CXX static library libpass.a
[ 61%] Linking CXX static library libfuse_all_reduce_op_pass.a
[ 61%] Linking CXX static library libbasic_engine.a
[ 61%] Linking CXX static library libmulti_devices_helper.a
[ 61%] Linking CXX static library libcoalesce_grad_tensor_pass.a
[ 61%] Linking CXX static library libfuse_optimizer_op_pass.a
[ 61%] Linking CXX static library libplacement_pass_base.a
[ 61%] Linking CXX static library libprogram_desc_tracer.a
[ 61%] Linking CXX static library libpass_builder.a
[ 61%] Linking CXX static library libadd_reader_dependency_pass.a
[ 61%] Linking CXX static library libwhile_op_eager_deletion_pass.a
[ 61%] Linking CXX static library libreference_count_pass.a
[ 61%] Linking CXX static library libgraph_pattern_detector.a
[ 61%] Linking CXX static library libengine.a
[ 61%] Linking CXX static library libsequential_execution_pass.a
[ 61%] Linking CXX static library libmulti_devices_graph_check_pass.a
[ 61%] Linking CXX static library libfix_op_run_order_pass.a
[ 61%] Linking CXX static library liball_reduce_deps_pass.a
[ 61%] Linking CXX static library libbackward_optimizer_op_deps_pass.a
[ 63%] Linking CXX static library libop_compat_sensible_pass.a
[ 63%] Linking CXX static library libmodify_op_lock_and_record_event_pass.a
[ 63%] Linking CXX static library libmulti_devices_graph_print_pass.a
[ 63%] Linking CXX static library libpass_test_util.a
[ 63%] Linking CXX static library libfuse_adamw_op_pass.a
[ 63%] Linking CXX static library libmulti_devices_graph_pass.a
[ 63%] Linking CXX static library libfuse_sgd_op_pass.a
[ 63%] Linking CXX static library libfuse_adam_op_pass.a
[ 63%] Linking CXX static library libfuse_momentum_op_pass.a
[ 63%] Linking CXX static library libfuse_bn_add_act_pass.a
[ 63%] Linking CXX static library libmemory_reuse_pass.a
[ 63%] Linking CXX static library libfuse_relu_depthwise_conv_pass.a
[ 63%] Linking CXX static library libfuse_bn_act_pass.a
[ 63%] Linking CXX static library libfuse_elewise_add_act_pass.a
[ 64%] Linking CXX static library libset_reader_device_info_utils.a
[ 64%] Linking CXX static library libfuse_gemm_epilogue_pass.a
[ 64%] Linking CXX static library libfuse_pass_base.a
[ 64%] Linking CXX static library libtracer.a
[ 64%] Linking CXX static library libgraph_to_program_pass.a
[ 64%] Linking CXX static library libfused_feedforward_pass.a
[ 64%] Linking CXX static library libinplace_addto_op_pass.a
[ 64%] Linking CXX static library libfused_attention_pass.a
[ 64%] Linking CXX static library libbuffer_shared_cross_op_memory_reuse_pass.a
[ 64%] Linking CXX static library libskip_layernorm_fuse_pass.a
[ 64%] Linking CXX static library libsqueeze2_transpose2_onednn_fuse_pass.a
[ 64%] Linking CXX static library liboperator_scale_onednn_fuse_pass.a
[ 64%] Linking CXX static library libmulti_gru_seq_fuse_pass.a
[ 64%] Linking CXX static library libtrt_delete_weight_dequant_linear_op_pass.a
[ 64%] Linking CXX static library libunsqueeze2_eltwise_fuse_pass.a
[ 64%] Linking CXX static library libconv_elementwise_add_act_fuse_pass.a
[ 64%] Linking CXX static library libdelete_quant_dequant_filter_op_pass.a
[ 65%] Linking CXX static library libsimplify_with_basic_ops_pass.a
[ 65%] Linking CXX static library liboperator_unsqueeze2_onednn_fuse_pass.a
[ 65%] Linking CXX static library libdelete_c_identity_op_pass.a
[ 65%] Linking CXX static library libadaptive_pool2d_convert_global_pass.a
[ 65%] Linking CXX static library libembedding_fc_lstm_fuse_pass.a
[ 65%] Linking CXX static library libmap_op_to_another_pass.a
[ 65%] Linking CXX static library libruntime_context_cache_pass.a
[ 65%] Linking CXX static library libsync_batch_norm_pass.a
[ 66%] Linking CXX static library libgraph_viz_pass.a
[ 66%] Linking CXX static library libmulti_batch_merge_pass.a
[ 66%] Linking CXX static library liblock_free_optimize_pass.a
[ 66%] Linking CXX static library libmkldnn_placement_pass.a
[ 66%] Linking CXX static library libdelete_dropout_op_pass.a
[ 66%] Linking CXX static library libdense_fc_to_sparse_pass.a
[ 66%] Linking CXX static library libadd_support_int8_pass.a
[ 66%] Linking CXX static library libfc_lstm_fuse_pass.a
[ 66%] Linking CXX static library libshuffle_channel_detect_pass.a
[ 66%] Linking CXX static library libgpu_cpu_map_matmul_to_mul_pass.a
[ 66%] Linking CXX static library libdepthwise_conv_mkldnn_pass.a
[ 66%] Linking CXX static library libcpu_quantize_squash_pass.a
[ 66%] Linking CXX static library libseqconv_eltadd_relu_fuse_pass.a
[ 66%] Linking CXX static library libconv_affine_channel_mkldnn_fuse_pass.a
[ 66%] Linking CXX static library libcpu_quantize_pass.a
[ 67%] Linking CXX static library libinplace_op_var_pass.a
[ 67%] Linking CXX static library libconv_elementwise_add2_act_fuse_pass.a
[ 67%] Linking CXX static library libmatmul_scale_fuse_pass.a
[ 67%] Linking CXX static library libbatch_norm_act_fuse_pass.a
[ 67%] Linking CXX static library libyolo_box_fuse_pass.a
[ 67%] Linking CXX static library libdense_multihead_matmul_to_sparse_pass.a
[ 67%] Linking CXX static library libdelete_fill_constant_op_pass.a
[ 67%] Linking CXX static library libfc_elementwise_layernorm_fuse_pass.a
[ 68%] Linking CXX static library libauto_mixed_precision_pass.a
[ 68%] Linking CXX static library libseqpool_concat_fuse_pass.a
[ 68%] Linking CXX static library libconv_bias_mkldnn_fuse_pass.a
[ 68%] Linking CXX static library libparams_quantization_mkldnn_pass.a
[ 68%] Linking CXX static library libmatmul_activation_mkldnn_fuse_pass.a
[ 68%] Linking CXX static library libfused_multi_transformer_encoder_pass.a
[ 68%] Linking CXX static library libglobal_utils.a
[ 68%] Linking CXX static library libattention_lstm_fuse_pass.a
[ 68%] Linking CXX static library libconv_bn_fuse_pass.a
[ 68%] Linking CXX static library libquant_dequant_mkldnn_pass.a
[ 68%] Linking CXX static library libquant_transpose2_dequant_onednn_fuse_pass.a
[ 68%] Linking CXX static library liblayer_norm_onednn_optimization_pass.a
[ 68%] Linking CXX static library libfc_fuse_pass.a
[ 68%] Linking CXX static library libshuffle_channel_mkldnn_detect_pass.a
[ 68%] Linking CXX static library libtranspose_flatten_concat_fuse_pass.a
[ 69%] Linking CXX static library libquant_conv2d_dequant_fuse_pass.a
[ 69%] Linking CXX static library libscale_matmul_fuse_pass.a
[ 69%] Linking CXX static library libsoftplus_activation_onednn_fuse_pass.a
[ 70%] Linking CXX static library libconv_elementwise_add_fuse_pass.a
[ 70%] Linking CXX static library libint8_scale_calculation_mkldnn_pass.a
[ 70%] Linking CXX static library libconstant_folding_pass.a
[ 70%] Linking CXX static library libseqpool_cvm_concat_fuse_pass.a
[ 71%] Linking CXX static library libfc_mkldnn_pass.a
[ 71%] Linking CXX static library libvit_attention_fuse_pass.a
[ 71%] Linking CXX static library libreshape_transpose_matmul_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libinterpolate_mkldnn_pass.a
[ 71%] Linking CXX static library librepeated_fc_relu_fuse_pass.a
[ 71%] Linking CXX static library libsilu_fuse_pass.a
[ 71%] Linking CXX static library libpreln_residual_bias_fuse_pass.a
[ 71%] Linking CXX static library libnaive_executor.a
[ 71%] Linking CXX static library libcpu_bfloat16_pass.a
[ 71%] Linking CXX static library liblayer_norm_fuse_pass.a
[ 71%] Linking CXX static library libdelete_concat_op_pass.a
[ 71%] Linking CXX static library libmatmul_elementwise_add_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libfused_multi_transformer_decoder_pass.a
[ 71%] Linking CXX static library libidentity_scale_op_clean_pass.a
[ 71%] Linking CXX static library libdelete_quant_dequant_op_pass.a
[ 71%] Linking CXX static library libdelete_quant_dequant_linear_op_pass.a
[ 71%] Linking CXX static library libseq_concat_fc_fuse_pass.a
[ 71%] Linking CXX static library libdelete_op_device_pass.a
[ 71%] Linking CXX static library libconv_activation_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libfuse_multi_transformer_layer_pass.a
[ 71%] Linking CXX static library libcpu_quantize_placement_pass.a
[ 71%] Linking CXX static library libis_test_pass.a
[ 71%] Linking CXX static library libdelete_weight_dequant_linear_op_pass.a
[ 71%] Linking CXX static library liboperator_reshape2_onednn_fuse_pass.a
[ 71%] Linking CXX static library libfc_elementwise_add_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libsquared_mat_sub_fuse_pass.a
[ 71%] Linking CXX static library libconv2d_fusion_layout_transfer_pass.a
[ 71%] Linking CXX static library libelt_act_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libconv_elementwise_add_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libmulti_gru_fuse_pass.a
[ 71%] Linking CXX static library libmatmul_transpose_reshape_mkldnn_fuse_pass.a
[ 71%] Linking CXX static library libfc_gru_fuse_pass.a
[ 71%] Linking CXX static library libcpu_bfloat16_placement_pass.a
[ 71%] Linking CXX static library libir_graph_to_program_pass.a
[ 71%] Linking CXX static library libadjust_cudnn_workspace_size_pass.a
[ 71%] Linking CXX static library libfc_act_mkldnn_fuse_pass.a
[ 72%] Linking CXX static library libinference_op_replace_pass.a
[ 72%] Linking CXX static library libmultihead_matmul_roformer_fuse_pass.a
[ 72%] Linking CXX static library libcompute_propagate_scales_mkldnn_pass.a
[ 72%] Linking CXX static library libmultihead_matmul_fuse_pass.a
[ 72%] Linking CXX static library libgenerate_pass.a
[ 72%] Linking CXX static library libbuild_strategy.a
[ 72%] Linking CXX static library libinterpreter.a
[ 72%] Linking CXX static library librecurrent_op_helper.a
[ 72%] Linking CXX static library libconditional_block_op_helper.a
[ 72%] Linking CXX static library libphi_bw_function_api.a
[ 72%] Linking CXX static library libphi_api.a
[ 72%] Linking CXX static library libconditional_block_op.a
[ 72%] Linking CXX static library libautograd_meta.a
[ 72%] Linking CXX static library libgrad_node_info.a
[ 72%] Linking CXX static library libscale_node.a
[ 72%] Linking CXX static library libgrad_tensor_holder.a
[ 72%] Linking CXX static library librecurrent_op.a
[ 72%] Linking CXX static library libcustom_operator.a
[ 72%] Linking CXX static library libaccumulation_node.a
[ 72%] Linking CXX static library libpy_layer_node.a
[ 72%] Linking CXX static library libeager_scale.a
[ 72%] Linking CXX static library libinterpretercore_garbage_collector.a
[ 72%] Linking CXX static library libpaddle_inference_api.a
[ 72%] Linking CXX static library libtensor_utils.a
[ 72%] Linking CXX static library libcustom_operator_node.a
[ 72%] Linking CXX static library libinfer_io_utils.a
[ 72%] Linking CXX static library libstandalone_executor.a
[ 73%] Linking CXX static library libexecutor.a
[ 73%] Linking CXX static library libexecutor_gc_helper.a
[ 74%] Linking CXX static library libfleet_executor.a
[ 74%] Linking CXX static library libpaddle_framework.a
[ 74%] Linking CXX static library libsubgraph_detector.a
[ 74%] Linking CXX static library libbuffer_shared_inplace_op_pass.a
[ 74%] Linking CXX static library libconditional_block_op_eager_deletion_pass.a
[ 74%] Linking CXX static library librecurrent_op_eager_deletion_pass.a
[ 74%] Linking CXX static library libarg_max_op.a
[ 74%] Linking CXX static library libarg_min_op.a
[ 74%] Linking CXX static library libadd_position_encoding_op.a
[ 74%] Linking CXX static library libabs_op.a
[ 74%] Linking CXX static library libaffine_grid_op.a
[ 74%] Linking CXX static library libaffine_channel_op.a
[ 74%] Linking CXX static library libarray_to_lod_tensor_op.a
[ 74%] Linking CXX static library libascend_trigger_op.a
[ 74%] Linking CXX static library libassign_pos_op.a
[ 75%] Linking CXX static library libassert_op.a
[ 75%] Linking CXX static library libassign_value_op.a
[ 75%] Linking CXX static library libaverage_accumulates_op.a
[ 75%] Linking CXX static library libbatch_fc_op.a
[ 75%] Linking CXX static library libattention_lstm_op.a
[ 75%] Linking CXX static library libbce_loss_op.a
[ 75%] Linking CXX static library libbeam_search_op.a
[ 75%] Linking CXX static library libbeam_search_decode_op.a
[ 75%] Linking CXX static library libbilinear_tensor_product_op.a
[ 75%] Linking CXX static library libbatch_norm_op.a
[ 75%] Linking CXX static library libbilateral_slice_op.a
[ 75%] Linking CXX static library libbincount_op.a
[ 75%] Linking CXX static library libbpr_loss_op.a
[ 75%] Linking CXX static library libcheck_memory_continue_op.a
[ 75%] Linking CXX static library libcast_op.a
[ 75%] Linking CXX static library libchannel_shuffle_op.a
[ 75%] Linking CXX static library libclip_by_norm_op.a
[ 76%] Linking CXX static library libclass_center_sample_op.a
[ 76%] Linking CXX static library libchunk_eval_op.a
[ 76%] Linking CXX static library libcenter_loss_op.a
[ 76%] Linking CXX static library libcoalesce_tensor_op.a
[ 76%] Linking CXX static library libconcat_op.a
[ 76%] Linking CXX static library libcopy_cross_scope_op.a
[ 76%] Linking CXX static library libconv_shift_op.a
[ 76%] Linking CXX static library libcrf_decoding_op.a
[ 76%] Linking CXX static library libcorrelation_op.a
[ 76%] Linking CXX static library libcos_sim_op.a
[ 76%] Linking CXX static library libconv_op.a
[ 76%] Linking CXX static library libctc_align_op.a
[ 76%] Linking CXX static library libconv_transpose_op.a
[ 76%] Linking CXX static library libcrop_op.a
[ 76%] Linking CXX static library libcross_entropy_op.a
[ 76%] Linking CXX static library libdecode_jpeg_op.a
[ 76%] Linking CXX static library libcudnn_lstm_op.a
[ 76%] Linking CXX static library libcvm_op.a
[ 76%] Linking CXX static library libdelete_var_op.a
[ 76%] Linking CXX static library libcum_op.a
[ 76%] Linking CXX static library libdeformable_conv_op.a
[ 77%] Linking CXX static library libdequantize_abs_max_op.a
[ 77%] Linking CXX static library libdeformable_conv_v1_op.a
[ 77%] Linking CXX static library libdequantize_log_op.a
[ 77%] Linking CXX static library libdeformable_psroi_pooling_op.a
[ 77%] Linking CXX static library libdata_norm_op.a
[ 77%] Linking CXX static library libdequeue_op.a
[ 77%] Linking CXX static library libdequantize_op.a
[ 77%] Linking CXX static library libdiag_op.a
[ 77%] Linking CXX static library libdgc_clip_by_norm_op.a
[ 77%] Linking CXX static library libedit_distance_op.a
[ 78%] Linking CXX static library libempty_op.a
[ 78%] Linking CXX static library libenqueue_op.a
[ 78%] Linking CXX static library libeinsum_op.a
[ 78%] Linking CXX static library libdropout_op.a
[ 78%] Linking CXX static library libeigvalsh_op.a
[ 78%] Linking CXX static library libdetection_map_op.a
[ 78%] Linking CXX static library libexpand_as_v2_op.a
[ 78%] Linking CXX static library libexpand_as_op.a
[ 78%] Linking CXX static library libexpand_v2_op.a
[ 78%] Linking CXX static library libexponential_op.a
[ 78%] Linking CXX static library libfill_any_like_op.a
[ 78%] Linking CXX static library libfake_dequantize_op.a
[ 78%] Linking CXX static library libexpand_op.a
[ 78%] Linking CXX static library libfake_quantize_op.a
[ 78%] Linking CXX static library libfill_any_op.a
[ 78%] Linking CXX static library libfill_constant_batch_size_like_op.a
[ 79%] Linking CXX static library libfc_op.a
[ 80%] Linking CXX static library libfill_zeros_like_op.a
[ 80%] Linking CXX static library libfill_op.a
[ 80%] Linking CXX static library libfill_constant_op.a
[ 80%] Linking CXX static library libfilter_by_instag_op.a
[ 80%] Linking CXX static library libfused_softmax_mask_op.a
[ 80%] Linking CXX static library libfused_softmax_mask_upper_triangle_op.a
[ 80%] Linking CXX static library libfsp_op.a
[ 80%] Linking CXX static library libfused_token_prune_op.a
[ 81%] Linking CXX static library libflatten_op.a
[ 81%] Linking CXX static library libgaussian_random_batch_size_like_op.a
[ 81%] Linking CXX static library libgather_op.a
[ 81%] Linking CXX static library libgaussian_random_op.a
[ 81%] Linking CXX static library libget_tensor_from_selected_rows_op.a
[ 81%] Linking CXX static library libgraph_reindex_op.a
[ 81%] Linking CXX static library libgenerated_fused_op.a
[ 81%] Linking CXX static library libgraph_sample_neighbors_op.a
[ 81%] Linking CXX static library libgraph_khop_sampler_op.a
[ 81%] Linking CXX static library libgroup_norm_op.a
[ 81%] Linking CXX static library libgenerated_static_op.a
[ 81%] Linking CXX static library libhash_op.a
[ 81%] Linking CXX static library libgru_op.a
[ 82%] Linking CXX static library libhinge_loss_op.a
[ 82%] Linking CXX static library libidentity_loss_op.a
[ 82%] Linking CXX static library libhierarchical_sigmoid_op.a
[ 82%] Linking CXX static library libim2sequence_op.a
[ 82%] Linking CXX static library libincrement_op.a
[ 82%] Linking CXX static library libisfinite_op.a
[ 82%] Linking CXX static library libinstance_norm_op.a
[ 82%] Linking CXX static library libgru_unit_op.a
[ 82%] Linking CXX static library libl1_norm_op.a
[ 82%] Linking CXX static library libinplace_abn_op.a
[ 82%] Linking CXX static library libgenerated_sparse_op.a
[ 82%] Linking CXX static library liblayer_norm_op.a
[ 82%] Linking CXX static library liblimit_by_capacity_op.a
[ 82%] Linking CXX static library libinterpolate_op.a
[ 82%] Linking CXX static library liblod_array_length_op.a
[ 82%] Linking CXX static library liblod_rank_table_op.a
[ 82%] Linking CXX static library libload_op.a
[ 83%] Linking CXX static library liblogspace_op.a
[ 83%] Linking CXX static library liblod_tensor_to_array_op.a
[ 83%] Linking CXX static library liblinear_chain_crf_op.a
[ 83%] Linking CXX static library liblod_reset_op.a
[ 83%] Linking CXX static library libmargin_cross_entropy_op.a
[ 83%] Linking CXX static library liblookup_table_dequant_op.a
[ 83%] Linking CXX static library liblstm_unit_op.a
[ 83%] Linking CXX static library liblookup_table_v2_op.a
[ 84%] Linking CXX static library liblstsq_op.a
[ 84%] Linking CXX static library liblookup_table_op.a
[ 84%] Linking CXX static library liblrn_op.a
[ 84%] Linking CXX static library libmarker_op.a
[ 84%] Linking CXX static library liblu_op.a
[ 85%] Linking CXX static library liblstmp_op.a
[ 85%] Linking CXX static library libmargin_rank_loss_op.a
[ 85%] Linking CXX static library libmax_sequence_len_op.a
[ 85%] Linking CXX static library libmatch_matrix_tensor_op.a
[ 85%] Linking CXX static library libmatrix_rank_op.a
[ 86%] Linking CXX static library libmean_iou_op.a
[ 86%] Linking CXX static library libmean_op.a
[ 86%] Linking CXX static library libmemcpy_d2h_op.a
[ 86%] Linking CXX static library libmemcpy_h2d_op.a
[ 86%] Linking CXX static library libmatmul_v2_op.a
[ 86%] Linking CXX static library libmatmul_op.a
[ 86%] Linking CXX static library libmemcpy_op.a
[ 86%] Linking CXX static library libmoe_op.a
[ 86%] Linking CXX static library libminus_op.a
[ 86%] Linking CXX static library libmerge_lod_tensor_op.a
[ 86%] Linking CXX static library libnop_op.a
[ 86%] Linking CXX static library libmodified_huber_loss_op.a
[ 86%] Linking CXX static library libnumber_count_op.a
[ 86%] Linking CXX static library libmul_op.a
[ 86%] Linking CXX static library libnorm_op.a
[ 86%] Linking CXX static library libnce_op.a
[ 86%] Linking CXX static library libone_hot_op.a
[ 87%] Linking CXX static library libpad_op.a
[ 87%] Linking CXX static library libpad2d_op.a
[ 87%] Linking CXX static library libpad_constant_like_op.a
[ 88%] Linking CXX static library libpartial_concat_op.a
[ 88%] Linking CXX static library libpad3d_op.a
[ 88%] Linking CXX static library libpixel_unshuffle_op.a
[ 88%] Linking CXX static library libpartial_sum_op.a
[ 88%] Linking CXX static library libpool_op.a
[ 88%] Linking CXX static library libpositive_negative_pair_op.a
[ 88%] Linking CXX static library libpool_with_index_op.a
[ 89%] Linking CXX static library libprune_gate_by_capacity_op.a
[ 89%] Linking CXX static library libprint_op.a
[ 89%] Linking CXX static library libpsroi_pool_op.a
[ 89%] Linking CXX static library libpull_box_extended_sparse_op.a
[ 89%] Linking CXX static library libprroi_pool_op.a
[ 89%] Linking CXX static library libpull_gpups_sparse_op.a
[ 89%] Linking CXX static library libpull_box_sparse_op.a
[ 89%] Linking CXX static library libpush_dense_op.a
[ 89%] Linking CXX static library libpull_sparse_v2_op.a
[ 89%] Linking CXX static library libpull_sparse_op.a
[ 89%] Linking CXX static library libquantize_op.a
[ 89%] Linking CXX static library libqueue_generator_op.a
[ 89%] Linking CXX static library librandint_op.a
[ 89%] Linking CXX static library libpyramid_hash_op.a
[ 89%] Linking CXX static library librandom_crop_op.a
[ 89%] Linking CXX static library librandom_routing_op.a
[ 89%] Linking CXX static library librandperm_op.a
[ 89%] Linking CXX static library libread_file_op.a
[ 89%] Linking CXX static library librank_loss_op.a
[ 89%] Linking CXX static library librank_attention_op.a
[ 89%] Linking CXX static library libreorder_lod_tensor_by_rank_op.a
[ 89%] Linking CXX static library librequantize_op.a
[ 89%] Linking CXX static library librepeat_interleave_op.a
[ 89%] Linking CXX static library libreverse_op.a
[ 89%] Linking CXX static library librnn_memory_helper_op.a
[ 89%] Linking CXX static library libroi_pool_op.a
[ 89%] Linking CXX static library libreshape_op.a
[ 89%] Linking CXX static library librnn_op.a
[ 89%] Linking CXX static library librow_conv_op.a
[ 90%] Linking CXX static library libroi_align_op.a
[ 90%] Linking CXX static library libsampling_id_op.a
[ 90%] Linking CXX static library librrelu_op.a
[ 90%] Linking CXX static library libsample_logits_op.a
[ 90%] Linking CXX static library libsave_op.a
[ 90%] Linking CXX static library libseed_op.a
[ 90%] Linking CXX static library libselect_input_op.a
[ 91%] Linking CXX static library libselect_output_op.a
[ 91%] Linking CXX static library libshape_op.a
[ 91%] Linking CXX static library libshare_data_op.a
[ 91%] Linking CXX static library libsegment_pool_op.a
[ 91%] Linking CXX static library libshrink_rnn_memory_op.a
[ 91%] Linking CXX static library libshuffle_batch_op.a
[ 91%] Linking CXX static library libset_value_op.a
[ 91%] Linking CXX static library libshuffle_channel_op.a
[ 91%] Linking CXX static library libsimilarity_focus_op.a
[ 91%] Linking CXX static library libsparse_manual_op.a
[ 92%] Linking CXX static library libsoftmax_with_cross_entropy_op.a
[ 92%] Linking CXX static library libslice_op.a
[ 92%] Linking CXX static library libsmooth_l1_loss_op.a
[ 92%] Linking CXX static library libsoftmax_op.a
[ 92%] Linking CXX static library libsplit_lod_tensor_op.a
[ 92%] Linking CXX static library libspace_to_depth_op.a
[ 92%] Linking CXX static library libspp_op.a
[ 92%] Linking CXX static library libsplit_op.a
[ 92%] Linking CXX static library libsquared_l2_distance_op.a
[ 92%] Linking CXX static library libsquared_l2_norm_op.a
[ 92%] Linking CXX static library libstrided_slice_op.a
[ 92%] Linking CXX static library libsum_op.a
[ 92%] Linking CXX static library libtdm_child_op.a
[ 93%] Linking CXX static library libsqueeze_op.a
[ 93%] Linking CXX static library libstft_op.a
[ 93%] Linking CXX static library libteacher_student_sigmoid_loss_op.a
[ 93%] Linking CXX static library libtemporal_shift_op.a
[ 93%] Linking CXX static library libtensor_array_to_tensor_op.a
[ 93%] Linking CXX static library libtile_op.a
[ 93%] Linking CXX static library libtransfer_layout_op.a
[ 93%] Linking CXX static library libtdm_sampler_op.a
[ 93%] Linking CXX static library libtop_k_op.a
[ 93%] Linking CXX static library libtranspose_op.a
[ 93%] Linking CXX static library libtril_indices_op.a
[ 93%] Linking CXX static library libtriangular_solve_op.a
[ 93%] Linking CXX static library libtree_conv_op.a
[ 93%] Linking CXX static library libtriu_indices_op.a
[ 93%] Linking CXX static library libtril_triu_op.a
[ 93%] Linking CXX static library libuniform_random_batch_size_like_op.a
[ 93%] Linking CXX static library libtruncated_gaussian_random_op.a
[ 93%] Linking CXX static library libuniform_random_inplace_op.a
[ 93%] Linking CXX static library libuniform_random_op.a
[ 94%] Linking CXX static library libunique_op.a
[ 94%] Linking CXX static library libunzip_op.a
[ 94%] Linking CXX static library libunpool_op.a
[ 94%] Linking CXX static library libtensor_formatter.a
[ 94%] Linking CXX static library libunique_with_counts_op.a
[ 94%] Linking CXX static library libvar_conv_2d_op.a
[ 94%] Linking CXX static library libunsqueeze_op.a
[ 94%] Linking CXX static library libactivation_op.a
[ 94%] Linking CXX static library libdepend_op.a
[ 94%] Linking CXX static library libconditional_block_infer_op.a
[ 94%] Linking CXX static library liblstm_op.a
[ 94%] Linking CXX static library libfetch_op.a
[ 94%] Linking CXX static library libfeed_op.a
[ 94%] Linking CXX static library libget_places_op.a
[ 94%] Linking CXX static library libfetch_v2_op.a
[ 94%] Linking CXX static library liblogical_op.a
[ 94%] Linking CXX static library libjit_interpreter_engine.a
[ 94%] Linking CXX static library libtensor_array_read_write_op.a
[ 94%] Linking CXX static library libsubgraph_util.a
[ 95%] Linking CXX static library libcost_model.a
[ 95%] Linking CXX static library libwhile_op.a
[ 95%] Linking CXX static library libeager_deletion_pass.a
[ 95%] Linking CXX static library libssa_graph_executor.a
[ 95%] Linking CXX static library libgenerated_op.a
[ 95%] Linking CXX static library libbind_threaded_ssa_graph_executor.a
[ 95%] Linking CXX static library libthreaded_ssa_graph_executor.a
[ 95%] Linking CXX static library libscope_buffered_ssa_graph_executor.a
[ 95%] Linking CXX static library libfast_threaded_ssa_graph_executor.a
[ 95%] Linking CXX static library libhook_utils.a
[ 95%] Linking CXX static library libasync_ssa_graph_executor.a
[ 95%] Linking CXX static library libparallel_ssa_graph_executor.a
[ 95%] Linking CXX static library libutils.a
[ 95%] Linking CXX static library libparallel_executor.a
[ 95%] Linking CXX static library libeager_api.a
[ 95%] Linking CXX static library libbackward.a
[ 95%] Linking CXX static library libexecutor_cache.a
[ 95%] Linking CXX static library libjit_compilation_unit.a
[ 95%] Linking CXX static library libeager_reducer.a
[ 95%] Linking CXX static library libgenerated_eager_prim_api.a
[ 95%] Linking CXX static library librun_program_op.a
[ 95%] Linking CXX static library libeager_utils.a
[ 95%] Linking CXX static library libpaddle_inference_io.a
[ 95%] Linking CXX static library libmanual_eager_prim_api.a
[ 95%] Linking CXX static library libeager_prim_api.a
[ 95%] Linking CXX static library libanalysis_helper.a
[ 96%] Linking CXX static library libir_pass_manager.a
[ 96%] Linking CXX static library libir_params_sync_among_devices_pass.a
[ 96%] Linking CXX static library libir_graph_build_pass.a
[ 96%] Linking CXX static library libir_analysis_pass.a
[ 96%] Linking CXX static library libconvert_to_mixed_precision.a
[ 96%] Linking CXX static library libanalysis_passes.a
[ 96%] Linking CXX static library libanalysis.a
[ 97%] Linking CXX static library libdygraph_node.a
[ 97%] Linking CXX static library libanalysis_predictor.a
[ 97%] Linking CXX static library libdygraph_function.a
[ 97%] Linking CXX static library libjit_predictor_engine.a
[ 97%] Linking CXX static library libjit_function.a
[ 97%] Linking CXX static library libjit_layer.a
[ 97%] Linking CXX static library libfinal_dygraph_function.a
[ 97%] Linking CXX static library libfinal_dygraph_node.a
[ 97%] Linking CXX static library libprim_api.a
[ 97%] Linking CXX static library libeager_tensor_operants.a
[ 98%] Linking CXX static library libperformance_benchmark_utils.a
[ 98%] Linking CXX static library libpaddle_inference.a
[ 99%] Linking CXX static library libpaddle_inference_c.a

```