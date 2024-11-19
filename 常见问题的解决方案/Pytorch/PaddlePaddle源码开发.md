## 基础入门 - 参考机器学习解决方案
1. 收集大量应用代码
2. 收集大量测试代码
3. 收集大量比赛代码
```
git clone https://github.com/PaddlePaddle/Paddle.git
cd Paddle
mkdir build && cd build
cmake .. -DPY_VERSION=3.8 -DWITH_GPU=OFF -DWITH_TESTING=ON -DCMAKE_EXPORT_COMPILE_COMMANDS=1
# 后台编译
make -j10 > paddle_compile_v1.log &



```

## 虚拟环境
### win11 - 默认pytorch开发环境
```

sudu  apt install python3.10-venv -y

python3 -m venv myml
source myml/bin/activate
python3 -m pip install requests

退出当前虚拟环境
deactivate
```

### win11 - paddle源码开发环境
```

python3 -m venv paddleDev
source paddleDev/bin/activate


```

### 镜像安装
1. docker：https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/Paddle%E9%85%8D%E7%BD%AETensorrt


## 


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


## 性能优化
1. 模型性能分析方法：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-performance-opt/model_perf.md
2. 案例
   1. Paddle2.0.0-rc0的模型预测效率比Torch低很多：https://github.com/PaddlePaddle/Paddle/issues/28774
      1. 调度的耗时占比确实会比较明显
3. 


## 算子开发
1. 官方文档：https://www.paddlepaddle.org.cn/documentation/docs/zh/develop/dev_guides/api_contributing_guides/new_cpp_op_cn.html
2. Paddle C++ 算子开发流程：https://space.keter.top/docs/high_performance/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/Paddle%E7%AE%97%E5%AD%90%E5%BC%80%E5%8F%91
### FeatureAlphaDropout - paddle 新增API
1. 报名：https://github.com/PaddlePaddle/Paddle/issues/62905
2. 新增流程：https://github.com/PaddlePaddle/community/blob/master/hackathon/hackathon_6th/%E3%80%90Hackathon%206th%E3%80%91%E5%BC%80%E6%BA%90%E8%B4%A1%E7%8C%AE%E4%B8%AA%E4%BA%BA%E6%8C%91%E6%88%98%E8%B5%9B%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91%E4%BB%BB%E5%8A%A1%E5%90%88%E9%9B%86.md#no8-%E4%B8%BA-paddle-%E6%96%B0%E5%A2%9E-featurealphadropout-api
3. 参考pr：https://github.com/PaddlePaddle/community/pull/848
4. 参考paddle 算子pr：https://github.com/PaddlePaddle/Paddle/pull/62934/files#diff-dd4ce82a4831b8c3f62aa1717373fce4dd62e1f42540bc8395df5e3c447a0475
5. 代码修改：Python 实现代码 & 英文 API 文档，在 Paddle repo 的 python/paddle/nn/layer/common.py 中实现 FeatureAlphaDropout 类，并在 python/paddle/nn/layer/init.py、python/paddle/nn/init.py 添加对应调用。
6. 单元测试：https://github.com/PaddlePaddle/Paddle/tree/develop/test
7. 中文api：https://github.com/PaddlePaddle/docs/tree/develop/docs/api/paddle


### FeatureAlphaDropout - dropout python冒烟调用
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

### FeatureAlphaDropout - dropout修改点
1. 
### FeatureAlphaDropout - dropout整理
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
