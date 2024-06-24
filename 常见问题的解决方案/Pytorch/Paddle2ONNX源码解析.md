## Paddle2ONNX
1. 代码：https://github.com/PaddlePaddle/Paddle2ONNX/tree/develop

## 源码编译 - 官方文档写的很好了
```shell

cmake >= 3.18.0
protobuf == 3.16.0

编译文档
https://github.com/PaddlePaddle/Paddle2ONNX/blob/develop/docs/zh/compile_local.md

# cmake
cur_dir=/docker/root/projects/demo/package
export PATH="$cur_dir/cmake-3.24.0-linux-x86_64/bin:$PATH"
export PATH="$cur_dir/lib:$cur_dir/bin:$PATH"


# protobuf
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v3.16.0
mkdir build_source && cd build_source
cmake ../cmake -DCMAKE_INSTALL_PREFIX=${PWD}/installed_protobuf_lib -Dprotobuf_BUILD_SHARED_LIBS=OFF -DCMAKE_POSITION_INDEPENDENT_CODE=ON -Dprotobuf_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release
make -j8
make install

# protobuf
export PATH=$cur_dir/protobuf/build_source/installed_protobuf_lib/bin:${PATH}

git clone https://github.com/PaddlePaddle/Paddle2ONNX.git
cd Paddle2ONNX
git submodule init
git submodule update


pip3 install setuptools wheel auditwheel auditwheel-symbols build
python3 -m build > p2onnx.log


cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1  -DPYTHON_INCLUDE_DIR=/usr/include/python3.8 -DPYTHON_EXECUTABLE=/usr/bin/python3 -DBUILD_PADDLE2ONNX_PYTHON=ON -DONNX_NAMESPACE=paddle2onnx -DPY_EXT_SUFFIX=.cpython-38-x86_64-linux-gnu.so -B /docker/root/projects/demo/github/Paddle2ONNX/build
```

### 需要自己生成编译树文件
```shell
mkdir build && cd build
cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1  -DPYTHON_INCLUDE_DIR=/usr/include/python3.8 -DPYTHON_EXECUTABLE=/usr/bin/python3 -DBUILD_PADDLE2ONNX_PYTHON=ON -DONNX_NAMESPACE=paddle2onnx -DPY_EXT_SUFFIX=.cpython-38-x86_64-linux-gnu.so -B /docker/root/projects/demo/github/Paddle2ONNX/build

```

## 源码拆解 - 横向角度
1. model proto结构
2. paddle2onnx_cpp2py_export
3. cpython 
4. onnx 模型结构
5. tensor 数据类型精度 区别
6. 张量对齐

### 张量结构
1. TensorProto
2. NodeProto
3. TensorProto_DataType
```


```

### 张量操作和对齐
```
数据类型转换：类中的方法可以将不同数据类型的数据进行转换，例如将字符串类型的数据转换为浮点数或整数类型。

数据剪裁（Clip）：提供了剪裁数据的方法，可以将数据限制在指定的范围内，超过范围的值将被截断。

数据压缩（Squeeze）：提供了压缩数据的方法，可以去除指定维度上大小为1的维度，减少数据的维度。

数据展开（Unsqueeze）：提供了展开数据的方法，可以在指定的维度上插入大小为1的维度，增加数据的维度。

数据重塑（Reshape）：提供了重塑数据形状的方法，可以将数据按照指定的形状进行重新排列。

数据扁平化（Flatten）：提供了将多维数据扁平化为一维数据的方法。

数据切片（Slice）：提供了对数据进行切片操作的方法，可以按照指定的轴和起始、结束位置对数据进行切片。

数据连接（Concat）：提供了将多个数据连接为一个数据的方法，可以按照指定的轴对数据进行连接。

数据转置（Transpose）：提供了对数据进行转置操作的方法，可以按照指定的轴进行数据转置。

数据分割（Split）：提供了将数据按照指定的轴和分割点进行分割的方法，将数据分割为多个子数据。

常量定义（Constant）：提供了定义常量数据的方法，可以定义具有指定形状和数值的常量数据。

数据赋值（Assign）：提供了对数据进行赋值操作的方法，可以将指定的数值赋给指定的数据。

```

### 张量函数
```
add_n.cc：对输入的多个张量进行逐元素相加的操作。

argmax.cc：返回输入张量在指定维度上的最大值的索引。

argmin.cc：返回输入张量在指定维度上的最小值的索引。

argsort.cc：返回输入张量在指定维度上按升序排列的索引。

assign.cc：将一个张量的值赋给另一个张量。

assign_value.cc：将指定的数值赋给张量。

atan2.cc：计算两个张量的元素的反正切值。

bmm.cc：对两个批次的矩阵进行批次矩阵乘法操作。

cast.cc：将张量的数据类型转换为指定的数据类型。

clip.cc：将张量的值限制在指定的范围内。

concat.cc：将多个张量在指定的维度上进行拼接。

cumsum.cc：对张量在指定维度上进行累加操作。

dist.cc：计算两个张量之间的距离。

dot.cc：计算两个张量的点积。

equal.cc：比较两个张量的元素是否相等。

expand.cc：将张量的维度进行扩展。

expand_as.cc：将张量的形状扩展为另一个张量的形状。

expand_v2.cc：将张量的形状扩展为指定形状。

eye.cc：创建一个单位矩阵。

fill_constant.cc：创建一个常量张量。

fill_constant_batch_size_like.cc：创建一个与指定张量形状相同的批次常量张量。

fill_like.cc：创建一个与指定张量形状相同的常量张量。

flatten.cc：将张量扁平化为一维张量。

flatten2.cc：将张量在指定维度之后的维度进行扁平化。

flip.cc：对张量的指定维度进行翻转操作。

gather.cc：根据索引从输入张量中收集元素。

gather_nd.cc：根据多维索引从输入张量中收集元素。

gaussian_random.cc：生成服从高斯分布的随机张量。

greater_equal.cc：比较两个张量的元素是否大于等于。

greater_than.cc：比较两个张量的元素是否大于。

grid_sampler.cc：对输入的特征图和采样网格进行双线性插值采样。

index_sample.cc：根据索引从输入张量中收集元素。

index_select.cc：根据索引从输入张量中收集元素。

less_equal.cc：比较两个张量的元素是否小于等于。

less_than.cc：比较两个张量的元素是否小于。

linspace.cc：生成指定范围内的等间距数值。

logical_not.cc：对张量的元素进行逻辑非操作。

logical_op.cc：对两个张量的元素进行逻辑操作。

lookup_table.cc：根据索引从查找表中获取值。

matmul.cc：计算两个矩阵的乘法。

matmul_v2.cc：计算两个矩阵的乘法。

mean.cc：计算张量在指定维度上的均值。

meshgrid.cc：生成一个网格矩阵。

mul.cc：对两个张量的元素进行逐元素相乘。

mv.cc：计算矩阵和向量的乘

```

### 模型结构
1. paddle模型
   1. wget https://bj.bcebos.com/paddle2onnx/model_zoo/mobilenetv3.tar.gz
   2. inference.pdiparams  inference.pdmodel
2. onnx模型
   1. wget https://bj.bcebos.com/paddle2onnx/model_zoo/mobilenetv3.onnx
3. 

### 模型参数

### opset7 opset9是什么意思
```
在深度学习框架中，例如PaddlePaddle和ONNX，每个版本都会引入新的操作，这些操作被组织成一个操作集合。每个操作集合都有一个版本号，称为"opset"，用来表示该版本中可用的操作。

在上述代码中，LogSoftmaxMapper 和 SoftShrinkMapper 是两个继承自 Mapper 的类，它们分别对应于不同的操作。在构造函数中，它们使用 GetAttr 方法获取了一些属性值，例如 axis 和 lambda。这些属性值可能用于在操作中指定一些参数或配置。

此外，SoftShrinkMapper 类还定义了一个名为 GetMinOpset 的方法，该方法返回当前操作所需的最低 opset 版本。在这个例子中，GetMinOpset 方法返回 9，表示该操作至少需要 opset 9 的版本才能正常运行。

```

## 源码拆解  - 目录角度
1. convert
2. parser
   1. TensorInfo
   2. Weight
3. mapper
   1. data_helper onnx_helper
   2. register_mapper.h 自动化注册技术
   3. nn
   4. quantize
   5. tensor
4. optimizer


### onnx.in.proto
```
Running gen_proto.py on onnx/onnx.in.proto


```


### detection模块
```
multiclass_nms.cc和multiclass_nms.h：这两个文件可能包含实现和定义多类非极大值抑制（Multiclass NMS）的类。Multiclass NMS是一种用于目标检测任务中去除冗余边界框的算法，它通过选择具有最高置信度的边界框，并消除与其重叠较大的其他边界框。

roi_align.cc和roi_align.h：这两个文件可能包含实现和定义ROI Align操作的类。ROI Align是一种用于在感兴趣区域（Region of Interest）内进行特征图采样的操作，它通过对感兴趣区域进行插值采样来获取固定大小的特征图。

yolo_box.cc和yolo_box.h：这两个文件可能包含实现和定义YOLO Box操作的类。YOLO Box是一种用于目标检测任务中从预测结果中提取边界框信息的操作，它将预测的边界框坐标、置信度和类别概率转换为真实坐标和类别标签。

```

### nn模块
```
affine_channel.h：定义了Affine Channel操作，用于对输入进行仿射变换。

batch_norm.h：定义了Batch Normalization操作，用于对输入进行批标准化。

conv2d.h：定义了二维卷积操作，用于对输入进行卷积运算。

conv2d_transpose.h：定义了二维转置卷积操作，用于对输入进行转置卷积运算。

conv3d.h：定义了三维卷积操作，用于对输入进行卷积运算。

data_norm.h：定义了数据标准化操作，用于对输入进行数据标准化。

dropout.h：定义了Dropout操作，用于在训练过程中随机丢弃部分神经元以防止过拟合。

group_norm.h：定义了Group Normalization操作，用于对输入进行组标准化。

instance_norm.h：定义了Instance Normalization操作，用于对输入进行实例标准化。

interpolate.h：定义了插值操作，用于对输入进行插值。

layer_norm.h：定义了Layer Normalization操作，用于对输入进行层标准化。

norm.h：定义了归一化操作，用于对输入进行归一化处理。

pad.h：定义了填充操作，用于对输入进行填充。

pad3d.h：定义了三维填充操作，用于对三维输入进行填充。

pool2d.h：定义了二维池化操作，用于对输入进行池化运算。

pool3d.h：定义了三维池化操作，用于对输入进行池化运算。

rnn.h：定义了循环神经网络（Recurrent Neural Network）的操作。

shape.h：定义了形状操作，用于获取输入的形状信息。

softmax_with_cross_entropy.h：定义了Softmax with Cross Entropy操作，用于计算Softmax概率和交叉熵损失。

```

## optimizer
### 优化策略
```
struct OptimizerOption {
  std::vector<std::string> passes;
  OptimizerOption() {
    passes.push_back("eliminate_identity");
    passes.push_back("eliminate_deadend");
    passes.push_back("fuse_constant_reshape");
    passes.push_back("fuse_constant_unsqueeze");
    passes.push_back("fuse_paddle_conv_bias");
    passes.push_back("fuse_consecutive_transposes");
    passes.push_back("eliminate_non_transpose");
    passes.push_back("replace_mul_to_identity");
    passes.push_back("replace_add_to_identity");
    passes.push_back("fuse_matmul_add_bias_into_gemm");
    passes.push_back("eliminate_identity");
    passes.push_back("eliminate_deadend");
  }
};

"eliminate_identity"：消除无用的 Identity 操作。Identity 操作是一种无操作，将输入直接复制到输出。

"eliminate_deadend"：消除无用的死结点。死结点是指没有输出连接到其他节点的节点。

"fuse_constant_reshape"：融合常量 Reshape 操作。将常量 Reshape 操作与其后的操作合并，以减少计算图中的不必要节点。

"fuse_constant_unsqueeze"：融合常量 Unsqueeze 操作。将常量 Unsqueeze 操作与其后的操作合并，以减少计算图中的不必要节点。

"fuse_paddle_conv_bias"：融合 PaddlePaddle 中的卷积和偏置操作。将卷积操作和偏置操作合并成一个更高效的操作。

"fuse_consecutive_transposes"：融合连续的转置操作。将连续的转置操作合并成一个等效的转置操作，以减少计算图中的不必要节点。

"eliminate_non_transpose"：消除非转置操作。将非转置操作转换为等效的转置操作，以减少计算图中的不必要节点。

"replace_mul_to_identity"：将乘法操作替换为等效的 Identity 操作。当乘法操作的一个输入为1时，可以将其替换为 Identity 操作。

"replace_add_to_identity"：将加法操作替换为等效的 Identity 操作。当加法操作的一个输入为0时，可以将其替换为 Identity 操作。

"fuse_matmul_add_bias_into_gemm"：将矩阵乘法、加法和偏置操作融合为更高效的矩阵乘法操作。

这些优化 pass 在优化器中被执行，目的是优化计算图的性能和效率，通过消除无用的操作、减少不必要的节点和融合操作来提高计算图的执行效率。每个 pass 都有不同的优化目标和策略，用于针对特定的计算图进行优化。

```

## 推理流程
1.  paddle.jit.load 加载模型
2.  paddle.to_tensor 将预处理后的数据转换为 PaddlePaddle 的张量形状
3.  output_result = model(input_tensor) 模型默认就是推理了