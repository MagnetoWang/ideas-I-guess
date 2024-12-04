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
1.  win11 wsl vscode开启
    1. 安装插件 wsl
    2. 输入命令
       1. wsl
       2. cd 任意目录
       3. code .
2. python 开发
   1. pyrcharm
3. c++
### wslconfig 配置
```

[wsl2]
memory=16G  #配置虚拟机最大使用内存，按需，默认Windows主机内存的1/2
networkingMode=mirrored # 开启镜像网络
dnsTunneling=true # 开启 DNS Tunneling
firewall=true # 开启 Windows 防火墙
autoProxy=true  # 开启自动同步代理
localhostForwarding=true  # 是否启用 localhost 转发
sparseVhd=true # 开启自动释放 WSL2 虚拟硬盘空间

[experimental]
# requires dnsTunneling but are also OPTIONAL
bestEffortDnsParsing=true
useWindowsDnsCache=true
```

### 网络配置
```

网络配置
 .wslconfig 文件配置 WSL2
 [experimental]
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true


win11 git代理加速 在clash代理机器上面看
git config --global http.proxy "http://127.0.0.1:7890"
git config --global https.proxy "http://127.0.0.1:7890"

wsl 需要通过win11访问
win11Ip=$(cat /etc/resolv.conf | grep -oP '(?<=nameserver\ ).*')
export HTTP_PROXY="http://${win11Ip}:7890"
export HTTPS_PROXY="http://${win11Ip}:7890"

不要设置 all_proxy就能git clone成本
export ALL_PROXY="http://${win11Ip}:7890"



curl http://172.24.112.1:7890
curl http://localhost

git config --global http.proxy "http://172.24.112.1:7890"
git config --global https.proxy "http://172.24.112.1:7890"





取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy

export ALL_PROXY=
export HTTP_PROXY=
export HTTPS_PROXY=

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


### 安装异常
1. https://blog.csdn.net/Desecrater/article/details/133581868
2. https://zhuanlan.zhihu.com/p/659727636
3. 代理配置：https://blog.csdn.net/eeemmm/article/details/136999284
4. wsl访问win11服务：https://www.cnblogs.com/netWild/p/18503950
   1. https://github.com/microsoft/WSL/issues/10753
   2. https://gist.github.com/libChan/3a804a46b532cc326a2ee55b27e8ac19?permalink_comment_id=4841732
5. 有代理的情况下
   1. 本机git要设置代理
   2. wsl环境也要设置

```
(myml) root@MagnetoWang:~/develop# git clone https://github.com/d2l-ai/d2l-zh.git
Cloning into 'd2l-zh'...
fatal: unable to access 'https://github.com/d2l-ai/d2l-zh.git/': Failed to connect to github.com port 443 after 49 ms: Connection refused


wslconfig 配置自动同步代理
[wsl2]
memory=16G  #配置虚拟机最大使用内存，按需，默认Windows主机内存的1/2
networkingMode=mirrored # 开启镜像网络
dnsTunneling=true # 开启 DNS Tunneling
firewall=true # 开启 Windows 防火墙
autoProxy=true  # 开启自动同步代理
localhostForwarding=true  # 是否启用 localhost 转发
sparseVhd=true # 开启自动释放 WSL2 虚拟硬盘空间
autoMemoryReclaim=gradual  # gradual  | dropcache | disabled


在wsl2 设置win11的代理ip和端口，但是不要设置 all_proxy
export hostip=$(ip route show | grep -i default | awk '{ print $3}')
export https_proxy="http://${hostip}:7890"
export http_proxy="http://${hostip}:7890"


```

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


## 模型开发

|     | Paddle | Pytorch | Numpy | TensorFlow |
| --- | ------ | ------- | ----- | ---------- |
|     |        |         |       |            |
| LTR |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |
|     |        |         |       |            |




### 模型开发 - LTR
1. https://github.com/PaddlePaddle/Research/blob/master/NLP/ACL2019-ARNOR/README.md


### 模型开发 - NLP


### 模型开发 - CV


### 模型开发 - DNN
1. https://aistudio.baidu.com/bd-cpu-01/user/707853/8622870/notebooks/8622870.ipynb
```

cd PaddleRec/models/rank/dnn
训练
python -u ../../../tools/trainer.py -m config.yaml

推理


产出结果
-rw-r--r-- 1 aistudio aistudio  71M Dec  3 20:16 rec.pdopt
-rw-r--r-- 1 aistudio aistudio  36M Dec  3 20:16 rec.pdparams
-rw-r--r-- 1 aistudio aistudio 321K Dec  3 19:42 rec_static.pdmodel
-rw-r--r-- 1 aistudio aistudio  73M Dec  3 19:42 rec_static.pdopt
-rw-r--r-- 1 aistudio aistudio  36M Dec  3 19:42 rec_static.pdparams


```

#### 训练
```

2024-12-03 20:16:32,184 - INFO - epoch: 2, batch_id: 0, auc:1.000000, loss:0.1101168, avg_reader_cost: 0.00158 sec, avg_batch_cost: 0.07763 sec, avg_samples: 1.00000, ips: 12.88137 ins/s
2024-12-03 20:16:32,481 - INFO - epoch: 2, batch_id: 2, auc:1.000000, loss:0.3321312, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14499 sec, avg_samples: 2.00000, ips: 13.79408 ins/s
2024-12-03 20:16:32,777 - INFO - epoch: 2, batch_id: 4, auc:0.937500, loss:0.7722418, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14477 sec, avg_samples: 2.00000, ips: 13.81498 ins/s
2024-12-03 20:16:33,072 - INFO - epoch: 2, batch_id: 6, auc:0.969697, loss:0.06091949, avg_reader_cost: 0.00032 sec, avg_batch_cost: 0.14414 sec, avg_samples: 2.00000, ips: 13.87510 ins/s
2024-12-03 20:16:33,368 - INFO - epoch: 2, batch_id: 8, auc:0.977778, loss:0.23176083, avg_reader_cost: 0.00037 sec, avg_batch_cost: 0.14511 sec, avg_samples: 2.00000, ips: 13.78244 ins/s
2024-12-03 20:16:33,663 - INFO - epoch: 2, batch_id: 10, auc:0.972222, loss:0.056122, avg_reader_cost: 0.00032 sec, avg_batch_cost: 0.14408 sec, avg_samples: 2.00000, ips: 13.88147 ins/s
2024-12-03 20:16:33,958 - INFO - epoch: 2, batch_id: 12, auc:0.971429, loss:0.11332353, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14444 sec, avg_samples: 2.00000, ips: 13.84703 ins/s
2024-12-03 20:16:34,254 - INFO - epoch: 2, batch_id: 14, auc:0.976000, loss:0.0185627, avg_reader_cost: 0.00033 sec, avg_batch_cost: 0.14462 sec, avg_samples: 2.00000, ips: 13.82909 ins/s
2024-12-03 20:16:34,549 - INFO - epoch: 2, batch_id: 16, auc:0.976190, loss:0.01627696, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14433 sec, avg_samples: 2.00000, ips: 13.85735 ins/s
2024-12-03 20:16:34,843 - INFO - epoch: 2, batch_id: 18, auc:0.979167, loss:0.03180037, avg_reader_cost: 0.00030 sec, avg_batch_cost: 0.14413 sec, avg_samples: 2.00000, ips: 13.87613 ins/s
2024-12-03 20:16:35,141 - INFO - epoch: 2, batch_id: 20, auc:0.979592, loss:0.00985625, avg_reader_cost: 0.00034 sec, avg_batch_cost: 0.14558 sec, avg_samples: 2.00000, ips: 13.73837 ins/s
2024-12-03 20:16:35,436 - INFO - epoch: 2, batch_id: 22, auc:0.960961, loss:1.0787587, avg_reader_cost: 0.00034 sec, avg_batch_cost: 0.14424 sec, avg_samples: 2.00000, ips: 13.86541 ins/s
2024-12-03 20:16:35,730 - INFO - epoch: 2, batch_id: 24, auc:0.967500, loss:0.00558221, avg_reader_cost: 0.00030 sec, avg_batch_cost: 0.14391 sec, avg_samples: 2.00000, ips: 13.89747 ins/s
2024-12-03 20:16:36,027 - INFO - epoch: 2, batch_id: 26, auc:0.972516, loss:0.11313634, avg_reader_cost: 0.00042 sec, avg_batch_cost: 0.14514 sec, avg_samples: 2.00000, ips: 13.78027 ins/s
2024-12-03 20:16:36,321 - INFO - epoch: 2, batch_id: 28, auc:0.975194, loss:0.75446916, avg_reader_cost: 0.00032 sec, avg_batch_cost: 0.14436 sec, avg_samples: 2.00000, ips: 13.85426 ins/s
2024-12-03 20:16:36,617 - INFO - epoch: 2, batch_id: 30, auc:0.978261, loss:0.04946108, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14483 sec, avg_samples: 2.00000, ips: 13.80919 ins/s
2024-12-03 20:16:36,912 - INFO - epoch: 2, batch_id: 32, auc:0.980792, loss:0.18857269, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14400 sec, avg_samples: 2.00000, ips: 13.88848 ins/s
2024-12-03 20:16:37,206 - INFO - epoch: 2, batch_id: 34, auc:0.979592, loss:0.7345889, avg_reader_cost: 0.00027 sec, avg_batch_cost: 0.14407 sec, avg_samples: 2.00000, ips: 13.88209 ins/s
2024-12-03 20:16:37,501 - INFO - epoch: 2, batch_id: 36, auc:0.981643, loss:0.06374952, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14394 sec, avg_samples: 2.00000, ips: 13.89511 ins/s
2024-12-03 20:16:37,793 - INFO - epoch: 2, batch_id: 38, auc:0.983399, loss:0.00642101, avg_reader_cost: 0.00031 sec, avg_batch_cost: 0.14285 sec, avg_samples: 2.00000, ips: 14.00105 ins/s
2024-12-03 20:16:37,943 - INFO - epoch: 2 done, auc: 0.983982,loss:0.01648083, epoch time: 5.92 s
2024-12-03 20:16:38,974 - INFO - Already save model in output_model_dnn/2

```

#### 推理
```


2024-12-03 20:19:34,752 - INFO - load model epoch 2
2024-12-03 20:19:34,752 - INFO - start load model from output_model_dnn/2
2024-12-03 20:19:34,922 - INFO - epoch: 2, batch_id: 0, auc: 0.864940, avg_reader_cost: 0.00135 sec, avg_batch_cost: 0.00535 sec, avg_samples: 2.00000, ips: 22.42 ins/s
2024-12-03 20:19:34,936 - INFO - epoch: 2, batch_id: 2, auc: 0.869480, avg_reader_cost: 0.00021 sec, avg_batch_cost: 0.00462 sec, avg_samples: 2.00000, ips: 289.71 ins/s
2024-12-03 20:19:34,950 - INFO - epoch: 2, batch_id: 4, auc: 0.874829, avg_reader_cost: 0.00024 sec, avg_batch_cost: 0.00451 sec, avg_samples: 2.00000, ips: 293.25 ins/s
2024-12-03 20:19:34,963 - INFO - epoch: 2, batch_id: 6, auc: 0.880327, avg_reader_cost: 0.00019 sec, avg_batch_cost: 0.00438 sec, avg_samples: 2.00000, ips: 300.39 ins/s
2024-12-03 20:19:34,977 - INFO - epoch: 2, batch_id: 8, auc: 0.884037, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00436 sec, avg_samples: 2.00000, ips: 301.14 ins/s
2024-12-03 20:19:34,990 - INFO - epoch: 2, batch_id: 10, auc: 0.888939, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00435 sec, avg_samples: 2.00000, ips: 302.15 ins/s
2024-12-03 20:19:35,004 - INFO - epoch: 2, batch_id: 12, auc: 0.893537, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00477 sec, avg_samples: 2.00000, ips: 284.50 ins/s
2024-12-03 20:19:35,018 - INFO - epoch: 2, batch_id: 14, auc: 0.896600, avg_reader_cost: 0.00019 sec, avg_batch_cost: 0.00459 sec, avg_samples: 2.00000, ips: 292.05 ins/s
2024-12-03 20:19:35,032 - INFO - epoch: 2, batch_id: 16, auc: 0.900460, avg_reader_cost: 0.00019 sec, avg_batch_cost: 0.00444 sec, avg_samples: 2.00000, ips: 297.94 ins/s
2024-12-03 20:19:35,045 - INFO - epoch: 2, batch_id: 18, auc: 0.903188, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00436 sec, avg_samples: 2.00000, ips: 301.93 ins/s
2024-12-03 20:19:35,058 - INFO - epoch: 2, batch_id: 20, auc: 0.906927, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00436 sec, avg_samples: 2.00000, ips: 302.38 ins/s
2024-12-03 20:19:35,072 - INFO - epoch: 2, batch_id: 22, auc: 0.909934, avg_reader_cost: 0.00021 sec, avg_batch_cost: 0.00435 sec, avg_samples: 2.00000, ips: 302.43 ins/s
2024-12-03 20:19:35,085 - INFO - epoch: 2, batch_id: 24, auc: 0.913265, avg_reader_cost: 0.00018 sec, avg_batch_cost: 0.00435 sec, avg_samples: 2.00000, ips: 302.17 ins/s
2024-12-03 20:19:35,099 - INFO - epoch: 2, batch_id: 26, auc: 0.916415, avg_reader_cost: 0.00022 sec, avg_batch_cost: 0.00437 sec, avg_samples: 2.00000, ips: 301.61 ins/s
2024-12-03 20:19:35,112 - INFO - epoch: 2, batch_id: 28, auc: 0.921896, avg_reader_cost: 0.00018 sec, avg_batch_cost: 0.00437 sec, avg_samples: 2.00000, ips: 300.63 ins/s
2024-12-03 20:19:35,126 - INFO - epoch: 2, batch_id: 30, auc: 0.924597, avg_reader_cost: 0.00021 sec, avg_batch_cost: 0.00437 sec, avg_samples: 2.00000, ips: 301.12 ins/s
2024-12-03 20:19:35,139 - INFO - epoch: 2, batch_id: 32, auc: 0.927159, avg_reader_cost: 0.00018 sec, avg_batch_cost: 0.00432 sec, avg_samples: 2.00000, ips: 303.48 ins/s
2024-12-03 20:19:35,152 - INFO - epoch: 2, batch_id: 34, auc: 0.931508, avg_reader_cost: 0.00020 sec, avg_batch_cost: 0.00439 sec, avg_samples: 2.00000, ips: 300.45 ins/s
2024-12-03 20:19:35,165 - INFO - epoch: 2, batch_id: 36, auc: 0.933735, avg_reader_cost: 0.00018 sec, avg_batch_cost: 0.00394 sec, avg_samples: 2.00000, ips: 321.80 ins/s
2024-12-03 20:19:35,176 - INFO - epoch: 2, batch_id: 38, auc: 0.935855, avg_reader_cost: 0.00021 sec, avg_batch_cost: 0.00307 sec, avg_samples: 2.00000, ips: 373.17 ins/s
2024-12-03 20:19:35,184 - INFO - epoch: 2 done, auc: 0.936605, epoch time: 0.43 s

```


## 应用开发
1. 课程
   1. 李宏毅课程-机器学习：https://aistudio.baidu.com/course/introduce/1978
