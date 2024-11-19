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

## 核心思考问题
1. 编译 测试 和 自动跳转功能
2. paddle和flink看的顺序不一样，flink是java，可以根据package，横向拆解，一层层看代码，有简单模块，看向复杂模块。但是paddle是c++，横向拆解不够粗粒度，只能纵向拆解，先串通整个流程设计的概念，再从源码编译顺序看看怎么横向分层
3. 

## 参考资料
1. 飞桨框架v2.4 API新升级！全面支持稀疏计算、图学习、语音处理等任务：https://mp.weixin.qq.com/s/8IYYEbJqIjyWd2zO7TGGFw
2. PaddleBox：百度基于GPU的超大规模离散DNN模型训练解决方案：https://mp.weixin.qq.com/s/o-ZoRnAMnINGHVALj7DQRA
3. 大模型时代的异构计算平台：https://mp.weixin.qq.com/s/ZAP_8ZwkZ295I225QTh9Yw
4. 委员会
   1. https://github.com/PaddlePaddle/community/tree/master/pposdwg
5. 技术分享
   1. 训练营：https://github.com/PFCCLab/Camp?tab=readme-ov-file
   2. 代码串讲：https://github.com/PFCCLab/Camp
   3. 读书会：https://github.com/PaddlePaddle/community/tree/master/pfcc/paddle-code-reading
   4. pfcc：https://pfcc.blog/
   5. 周会：https://github.com/PaddlePaddle/community/tree/master/pfcc
   6. code reading：https://github.com/PaddlePaddle/community/tree/master/pfcc/paddle-code-reading
6. 性能优化
   1. 模型优化：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-performance-opt/model_perf.md
   2. 编译器优化理论SSA
7. blog
   1. Zerorains：https://space.keter.top/docs/high_performance/%E7%AE%97%E5%AD%90%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96/Histogram
   2. State of PyTorch：https://pfcc.blog/posts/pytorch-conference-01
8. 黑客松
   1. Hackathon 1th：https://github.com/PaddlePaddle/Paddle/issues/35940
   2. Hackathon 2th：https://github.com/PaddlePaddle/Paddle/issues/40234
   3. Hackathon 3th：https://github.com/PaddlePaddle/Paddle/issues/43938
   4. Hackathon 4th：https://github.com/PaddlePaddle/Paddle/issues/51281
   5. Hackathon 5th：https://github.com/PaddlePaddle/docs/blob/release/2.5/docs/guides/10_contribution/hackathon_cn.md
   6. Hackathon 6th：https://github.com/PaddlePaddle/Paddle/issues/62907
   7. Hackathon 7th：https://github.com/PaddlePaddle/Paddle/issues/68242
9.  人物经历
    1. nknan：https://pfcc.blog/posts/nknan-story
       1. https://github.com/NKNaN
    2. https://pfcc.blog/posts/wangxin-story
    3. https://pfcc.blog/posts/tao-story
    4. https://pfcc.blog/posts/zhangyiqiao-story 说话挺搞笑的，哈哈哈
    5. https://pfcc.blog/posts/sanbu-story


## 文章分享
1. Pir Parser实现分享：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/01_PIR_OpTestFixingAndProgramTranslatorRefinement/pir_parser_implementation_sharing.md
2. PIR 组网 API：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/03_NewIRAPI_AutoDiffAndCoreComponentRefinement/CodeReading/Over_view_PIR_construct_API_As_CodeGen_perspective.md
3. codegen：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/code_gen/code_gen_ops.md
4. 算子组合机制：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/04_TheUnityOfOperatorForwardAndBackwardInCombinationFeatures/CodeReading/the_unity_of_operator_forward_and_backward_in_combination_features.md
5. Paddle静态图并行编排与执行流程：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/10_StaticGraph_Semi-AutomaticParallel_ExecutionFrameworkUpgrade/CodeReading/1-paddle_static_graph_pipelining.md
6. 代码层面熟悉 PIR：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/19_PIR_Adapt_CINN/CodeReading/PIR_source_code_reading_guide.md
7. ZB VPP 实现方案：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_6th/10_Static_Graph_semi-automatic_parallel_training_performance_optimization/zb_vpp_design.md


### sonder blog
1. 入门经历，按顺序看
   1. https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/Paddle%E9%85%8D%E7%BD%AETensorrt
   2. https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/Paddle%E7%AE%97%E5%AD%90%E5%BC%80%E5%8F%91
   3. https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/%E9%9D%99%E6%80%81%E5%9B%BE%E7%BB%84%E7%BD%91%E8%BF%87%E7%A8%8B
   4. https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/%E9%9D%99%E6%80%81%E5%9B%BE%E6%89%A7%E8%A1%8C%E8%BF%87%E7%A8%8B
   5. https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/TensorRT%E7%AE%97%E5%AD%90%E5%BC%80%E5%8F%91

## paddle vs pytorch
1. paddle所有运营活动在github，但是运营内容都是中文，没有通过微信或者官网得到很好关键词挖掘
   1. 搜 paddle 技术串讲 在google和baidu是两个不一样的结果。中国人其实更容易学paddle，但是获取相关信息渠道出了问题
2. 活动很多，但是没有统一首页管理

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

## pytorch字典
1. https://openmlsys.github.io/chapter_backend_and_runtime/compute_schedule_and_execute.html


## 流图

### 程序语言角度



### 数据流角度


### 算子图角度


### 数学公式角度


### TorchScript
1. ts教程：https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html
2. ts中文教程：https://pytorch.panchuang.net/EigthSection/torchScript/


### onnx
1. onnx文件及其结构：https://blog.csdn.net/Rolandxxx/article/details/127713806
2. pd文件：https://gitcode.com/gh_mirrors/onn/onnx/blob/main/onnx/onnx.proto
3. IR：https://github.com/onnx/onnx/blob/main/docs/IR.md

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

### 横向拆解 - 第三方依赖
1. extern_zlib
2. extern_threadpool
3. extern_dlpack
4. extern_gflags
5. extern_eigen3
6. extern_mklml
7. extern_mkldnn

### 横向拆解 - 协议结构
1. framework_proto
2. phi_profiler_proto
3. auto_parallel_proto


### 横向拆解 - 基础能力 flags & errors & monitor & pretty_log


### 横向拆解 - mkldnn

### 横向拆解 - phi_place


### 横向拆解 - data_type




### 横向拆解 - activation_functions


### 横向拆解 - phi_device_tracer


### 横向拆解 - phi_c_place

### 横向拆解 - eager_python_c_codegen

### 横向拆解 - op_def_api


### 横向拆解 - op_map_codegen


### 横向拆解 - eager_codegen


### 横向拆解 - tensor_base

### 横向拆解 - prune


### 横向拆解 - ddim


### 横向拆解 - mlu_tracer




### 纵向拆解 - 静态图执行
1. https://github.com/PFCCLab/Camp/blob/main/WeeklyReports/Hackathon_5th/01_xingmingyyj/xingmingyyj2023.10.10-2023.10.24.md


### 纵向拆解 - Pass 体系
1. Pass 的核心是子图匹配和替换（即图变换），是将一个 Program 通过某种规则转换为另一个新的 Program。IR 中包含了计算图中全局信息，如上下游算子的邻接关系等，更有利于进行图优化，比如常量折叠、算子融合，Inplace 策略等：
2. 提供了 2 种 Pass 开发范式：Pattern Rewriter 和 Declarative Rewrite Rule（简称 DRR）


### 纵向拆解 - 常量折叠方案
1. https://github.com/PFCCLab/Camp/blob/main/WeeklyReports/Hackathon_5th/02_zhangyuqin1998/%5BWeeklyReport%5D2023.11.10~2023.11.25.md


### 纵向拆解 - Pir设计 paddle ir
1. PIR 基本概念和开发：https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/paddle_v3_features/paddle_ir_cn.html 
2. 技术文章
   1. IR设计：https://github.com/PaddlePaddle/community/tree/master/pfcc/paddle-code-reading/IR_Dialect
   2. Pir Parser实现分享：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/01_PIR_OpTestFixingAndProgramTranslatorRefinement/pir_parser_implementation_sharing.md
   3. 从 CodeGen 视角看 PIR 组网 API：
3. 常见的深度学习 IR
   1. MLIR，TVM relay，MindIR，XLA hlo，TorchScript等。
4. 飞桨先后实现了两套 IR
   1. 一套是 Program 
   2. 一套是 Graph
   3. 新设计
      1. 坚持SSA(静态单赋值)原则，模型等价于一个有向无环图。 Operation 为节点，Value 为边
      2. 算子分层，分类。通过将算子和类型定义在不同的 Dialect 来实现算子和类型的分层分类
      3. 底层算子与算子库 Api 对齐
      4. 通过yaml + python脚本的形式，生成算子的 C++ 定义
   4. 优化
      1. 类型的本质是对内存的一种抽象，不同的类型，会有不同的内存布局和内存分配的策略
5. Operation 表示计算图中的节点：一个 Operation 表示一个算子，它里面包含了零个或多个 Region；Region 表示一个闭包，它里面包含了零个或多个 Block；Block 表示一个符合 SSA 的基本块，里面包含了零个或多个 Operation；三者循环嵌套，可以实现任意复杂的语法结构
6. Value 表示计算图中的有向边：用来将两个 Operaton 关联起来，描述了程序中的 UD 链（即 Use-Define 链）；OpResult 表示定义端，定义了一个 Value，OpOperand 表示使用端，描述了对一个 Value 的使用
7. 推理部署 ：简化抽象计算图，解决有环问题，降低 Pass 的开发成本
8.  分布式侧 ：多 Dialect 管理算子，支持分布式属性的灵活标记
9.  编译器侧 ：严格遵循 SSA 原则，灵活支撑编译优化鲁棒性
10. 完备且鲁邦的语义表达能力、训推全架构统一表示和高效可插拔的性能优化策略（Pass）开发机制
11. IR设计
   1. 控制流表示：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/IR_Dialect/control_flow.md
   2. 模型表示：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/IR_Dialect/ir_program.md
   3. 数据类型表示：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/IR_Dialect/control_flow.md
   4. 新 IR 适配编译器方案思路：https://github.com/PaddlePaddle/Paddle/issues/56879


#### IR基础库
1. Interface 、Trait、Type、Attribute、Op、Porgram
2. 新 IR Program 可以逐步替换当前框架中的 Program、Graph、Cinn Program、Cinn Graph
3. 支持List、Dict等复杂类型
4. 定义相应的Trait， 对 inplace 算子以及 View 类算子进行合理的抽象描述
5. 计算图严格遵守 SSA 原则
6. IR 基础库会抽象出一套 Pass 基础组件
7. 源码
   1. paddle/pir/src/core

#### 类型系统 - 对比Flink Spark Calcite

#### 模型结构
1. 问题
   1. 代码复用性
      1. 两种场景 Paddle 和 Cinn 。很多功能相能相同 Pass ，需要重复开发两次（ConstantFold、CSE等等）。
      2. IR 元素和具体的场景强绑定在一起，场景无关逻辑无法复用。
   2. 框架稳定性问题
      1. 目前的 paddle 模型结构 Program 存在序列式 IR 的隐式依赖。所有可能破坏算子顺序的模块，都是不完备的，都是存在风险的。
      2. 在 Pass中 ，图变换会对算子进行增删移动，改变算子顺序。因此，Pass 是存在风险的。
      3. 新执行器中，会对算子进行多流并行调度，相当于改变了算子的顺序。因此，执行器也是存在风险的。
   3. 能力不足
      1. 框架对 IR 元素的抽象相对都比较朴素，表达能力不足。
      2. 没有规范的类型系统，无法支持 List 、Dict等复杂类型，以及更近一步的类型嵌套表示。
      3. 缺乏严谨的 Tensor 别名机制。目前可以通过输入&输出同名来标志 inplace 算子，但是对于 share_date 、reshape (编译器算子)...这类view 类的别名算子是无法表达的。
      4. 计算图不符合 SSA 原则。编译器领域的很多成熟的优化理论无法直接应用。
2. 解决思路
   1. MLIR 的出现证明了可以用一套数据结构同时满足 Graph 和 Program 的功能，解决 Program & Graph 的二者同步问题。
3. 模型表示层
   1. Program 用来表示一个具体的模型。它包含两部分：计算图 和 权重 
   2. Weight 用来对模型的权重参数进行单独存储，这也是深度学习框架和传统编译器不一样的地方。传统编译器会将数据段内嵌到程序里面。这是因为传统编译器里面，数据和代码是强绑定的，不可分割。但是对神经网络而言，一个计算图的每个 epoch 都会存在一份权重参数，多个计算图也有可能共同一份权重参数，二者不是强绑定的。
   3. Value、Operation 用来对计算图进行抽象
4. 模型优化
   1. 图变换表示对一个 Program 进行优化，将其转换为另一个 Program 。里面包含了我们遇见的所有 Pass 。包括 Mapping``、Fusion、Pruning、Canonalization、CSE等等

```

```


#### 高阶特性
#### Pass升级
1. framework::ProgramDesc  =>  ir::Graph   =>  frontend::Program (NetBuilder 层)   =>  hlir::Graph =>    
Compute/Schedule()   =>  AST 层面   =>  Module::Builder  =>  CodeGen+NVRTC =>  Runtime::Program



#### MLIR设计借鉴

### 纵向拆解 - Program & Graph (CINN)
1. cinn  Compiler Infrastructure for Neural Networks：https://github.com/PaddlePaddle/CINN
2. Paddle 训练框架应用 CINN 进行编译优化加速：https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/cinn/paddle2cinn_intro_cn.html
3. CINN 神经网络编译器：https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/paddle_v3_features/cinn_cn.html



### 纵向拆解 - Codegen
1. paddle代码自动生成机制讲解：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/code_gen/code_gen_ops.md
2. 从 CodeGen 视角看 PIR 组网 API：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/03_NewIRAPI_AutoDiffAndCoreComponentRefinement/CodeReading/Over_view_PIR_construct_API_As_CodeGen_perspective.md
3. 框架静态图算子自动生成：https://github.com/PaddlePaddle/Paddle/issues/51842
4. 算子定义生成体系建设--静态图算子自动生成：https://github.com/PaddlePaddle/Paddle/issues/53267
5. 新 IR 下自动代码生成 ：https://github.com/PaddlePaddle/Paddle/issues/56849
6. infer_meta + Yaml文件自动生成算子代码
7. 存在三套 CodeGen 设计体系：即动态图、静态图、旧动态图，但旧动态图在完全退场后，旧动态图的CodeGen体系也预计会被完全清除。



#### 调用链路
1. python api -> python-c 转发 -> python-c 映射层 -> PIR op组网 API -> pir::Op 生成函数




### 纵向拆解 - 算子设计
1. 算子组合开发问题：https://github.com/PFCCLab/Camp/blob/main/Docs/Hackathon_5th/04_TheUnityOfOperatorForwardAndBackwardInCombinationFeatures/CodeReading/the_unity_of_operator_forward_and_backward_in_combination_features.md
2. 组合机制设计文档：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/operator_decomposition_mechanism/design.md
3. 问题背景
   1. NVIDIA数据公布， GPT-3 175B 使用1024块A100 训练34天，需要强大分布式训练能力。
   2. 科学计算微分方程求解如EulerBeam，前向运算四阶微分，加上一次反向传播过程，需要五阶微分。
   3. 编译器加速、国产硬件支持也近期深度学习框架演进重要方向。
4. 飞桨框架底层基于原生算子体系(1061个，正向 691个，反向 370个，且持续增长)构建，导致上述场景适配难度极大，具体原因如下：
   1. 分布式：需要基于原生算子体系手写自动并行策略。
   2. 高阶微分：需要手写高阶微分算子，如Matmul五阶代码行数超过3000。
   3. 编译器：需要将原生大算子拆解成细粒度编译器小算子，才能进一步融合优化。
   4. 新硬件：需要接入所有算子，才能正确运行。

#### 算子注册体系


#### PHI (Paddle HIgh reusability operator library)
1. 飞桨高可复用算子库 PHI 设计文档：https://github.com/PaddlePaddle/docs/blob/develop/docs/design/phi/design_cn.md
2. PHI注册：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/PHI_kernel_registration/PHI_kernel_registration.md

### 纵向拆解 - 动态图
1. 动态执行过程：https://www.paddlepaddle.org.cn/tutorials/projectdetail/4047189#anchor-7
2. 新动态图前向调用过程代码详解：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/Dygraph/20221201_dygraph_forward.md
3. 前向执行
4. 反向执行



### 纵向拆解 - 静态图
1. 官方概念：https://www.paddlepaddle.org.cn/tutorials/projectdetail/4047189
2. 执行过程：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/static_graph_execution/20221230_static_graph_execution.md

#### 核心概念
```
Variable：表示网络中的数据。
Operator：表示网络中的操作。
Block：表示编程语言中的控制流结构，如条件结构（if-else）、循环结构（while）等。
Program：基于Protobuf的序列化能力提供模型保存、加载功能。Protobuf是Google推出的一个结构化数据的序列化框架，可将结构化数据序列化为二进制流，或从二进制流中反序列化出结构化数据。飞桨模型的保存、加载功能依托于Protobuf的序列化和反序列化能力。
Transpiler：可选的编译步骤，作用是将一个Program转换为另一个Program。
Intermediate Representation：在执行前期，用户定义的Program会转换为一个统一的中间表达。
Executor：用于快速调度 Operator ，完成网络训练/预测。

```


### 纵向拆解 - Inplace
1. Inplace 介绍 & 使用介绍：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/Inplace/inplace_introduction.md
2. Paddle Inplace 使用指南：https://github.com/AndSonder/community/blob/ae18ba0d0b3b4ddd5ebc814c8190cd8f7a42b1bc/rfcs/Article/20240321_guide_to_using_Inplace.md

### 纵向拆解 - 微分规则 VJP

### 纵向拆解 - 自动并行 分布式




### 业务拆解 - 模型加载
1. jit load

#### paddle jit python模块
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

#### TranslatedLayer


### 业务拆解 - 训练
1. 单机多卡与多机多卡组网示例：https://aistudio.baidu.com/projectdetail/1222066
#### 单机单卡

   
#### 单机多卡 - 高层API
1. 建议使用spawn方式
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

#### 单机多卡 - 基础API
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




#### 多机多卡 - fleetrun启动分布式任务
1. 使用Fleet分布式训练方式
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


### 业务拆解 - 模型预估
1. TranslatedLayer






## 其他设计
### 垃圾回收器
1. github/Paddle/paddle/fluid/framework/new_executor/garbage_collector

### 任务队列
1. github/Paddle/paddle/fluid/framework/new_executor/workqueue


### 模型结构 和 可视化
1. https://www.paddlepaddle.org.cn/inference/master/guides/export_model/visual_model.html
2. 导出模型：https://www.paddlepaddle.org.cn/inference/master/guides/export_model/index_export_model.html



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



## 应用

### 稀疏计算 
1. 稀疏计算 使用指南
   1. https://github.com/AndSonder/community/blob/ae18ba0d0b3b4ddd5ebc814c8190cd8f7a42b1bc/rfcs/Article/20240412_guide_to_using_sparse.md
   2. https://github.com/PaddlePaddle/community/pull/880/files?short_path=71ec981#diff-71ec9818e57cd303cbc56336bcc80d7d6aa2a50c91a38a57a997202bd68a99c1
   3. https://github.com/PaddlePaddle/community/pull/883/files#diff-044bb5185eb6d238efea0f2eb7eb76648def35376960caea021c4dd6f9f2417d
2. COO 与 CSR 稀疏矩阵存取格式：https://cloud.tencent.com/developer/article/1766995
3. 存储效率：https://www.cnblogs.com/xbinworld/p/4273506.html
4. paddle
   1. 接口：paddle.sparse
   2. https://www.paddlepaddle.org.cn/documentation/docs/zh/develop/api/paddle/sparse/Overview_cn.html
5. 结构：COO 与 CSR 稀疏矩阵存取格式
   1. COO(Coordinate) 格式是最直接的稀疏存储方式,它将非零元素的值和对应的行列索引分别存储在两个向量中。
   2. CSR(Compressed Sparse Row) 格式按行存储压缩矩阵的非零元素。每一行中的非零元素用连续的储存空间存储, 从而可以高效地访问矩阵中同一行的数据。
```
待看
https://zhuanlan.zhihu.com/p/188700729
https://matteding.github.io/2019/04/25/sparse-matrices/
https://xie.infoq.cn/article/41ebc9e8a53bf4ba5fa14acca
https://github.com/PaddlePaddle/Paddle3D/blob/release/1.0/paddle3d/models/middle_encoders/sparse_resnet.py
https://github.com/PaddlePaddle/Paddle3D/blob/develop/docs/models/centerpoint/README.md

```


### 0维设计
1. Paddle框架的0-D设计全表：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/ZeroDim/all_zero_dim_api.md
2. 0维的判断标准：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/ZeroDim/judge_zero_dim.md
3. 0-D Tensor：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-code-reading/ZeroDim/zero_dim_concept.md
4. 0-d Tensor 使用指南：https://github.com/PaddlePaddle/community/pull/860/files?short_path=97dfe85#diff-97dfe85948dba8115a1ff933b2ebc047005fcc8b2dc22db542039663f5c800f8


### Paddle 概率分布基础及领域应用
1. Paddle 线性代数基础及其领域应用
   1. https://github.com/PaddlePaddle/community/pull/898/files?short_path=cf9bb59#diff-cf9bb59aeef3608b9a1a175149b7d583ba49fe4fd99febdc7577a9435bcfa351
   2. https://github.com/PaddlePaddle/community/pull/867/files#diff-005b97daccba370e0a0fcf462c6a63028d009a7aa91ade244e282d96a169d292
   3. https://github.com/PaddlePaddle/community/pull/861
   4. https://github.com/PaddlePaddle/community/pull/868

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