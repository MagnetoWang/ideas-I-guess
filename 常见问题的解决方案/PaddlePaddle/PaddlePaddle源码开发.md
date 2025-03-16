## 基础入门 - 参考机器学习解决方案
1. 收集大量应用代码
2. 收集大量测试代码
3. 收集大量比赛代码
4. 学习路径
   1. 已知公式
   2. 已知数据如何拟合公式
   3. 模型结构能拿到
      1. 依赖哪些paddle对外接口
      2. 仅仅几个接口，是如何串联整个paddle架构的
      3. 区分对外用户常用接口和不常用
      4. 在区分哪些就是内部使用的接口
      5. 高频接口链路梳理，并查看中间生成的代码
      6. 中低频接口按需梳理
      7. 类似方法整理pytorch，看看pytorch有没有一些不一样的地方
   4. 数据构造也能拿到
   5. 模型训练和推理都能跑 在 aistudio
   6. 怎么应用到业务场景，怎么优化指标
   7. 建模思想，每个模型设计总结
   8. 
```
git clone https://github.com/PaddlePaddle/Paddle.git
cd Paddle
mkdir build && cd build
cmake .. -DPY_VERSION=3.8 -DWITH_GPU=OFF -DWITH_TESTING=ON -DCMAKE_EXPORT_COMPILE_COMMANDS=1
# 后台编译
make -j10 > paddle_compile_v1.log &



```

### 应用代码
1. 推荐：https://github.com/PaddlePaddle/PaddleRec
2. 推理：https://github.com/PaddlePaddle/Paddle-Inference-Demo
3. learnpaddle：https://github.com/yeyupiaoling/LearnPaddle
4. 机器学习框架排名：https://paperswithcode.com/trends

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


### win11 - wsl2 - docker 一站式开发环境
1. 按照文档安装docker即可：https://docs.docker.com/engine/install/ubuntu/
2. cuda容器工具：https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
3. 以paddle为基础镜像：https://www.paddlepaddle.org.cn/documentation/docs/zh/install/docker/linux-docker.html
4. 解决 c++ go python rust 开发调试
5. https://docs.docker.com/desktop/features/wsl/
6. docker 无法启动：https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate
7.  sudo service docker start 
    1.  docker: unrecognized service
    2.  https://askubuntu.com/questions/1380051/docker-unrecognized-service-when-installing-cuda
```shell
前置条件 卸载历史不兼容docker包
开启 在 wslconfig
systemd=true


wsl
wsl --shutdown



二次加工
cuda工具安装
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

ssh服务
apt-get install openssh-client -y
apt-get install openssh-server -y

启动ssh服务
/etc/init.d/ssh start

/etc/init.d/ssh restart

以paddle为base
docker pull registry.baidubce.com/paddlepaddle/paddle:3.0.0b1-gpu-cuda12.3-cudnn9.0-trt8.6


docker pull registry.baidubce.com/paddlepaddle/paddle:3.0.0b2-gpu-cuda11.8-cudnn8.6-trt8.5

docker 






```


### paddle-cuda 源码开发环境 docker-compose.yml 
1. cpp 自动补全 + debug
   1. 加速编译速度：https://www.zhihu.com/question/266766131/answer/49321031151
2. python 自动补全 + debug
3. go 自动补全 + debug
4. coredump配置 --privileged
5. gpu配置
```
启动命令
docker-compose up -d

nvidia-docker pull registry.baidubce.com/paddlepaddle/paddle:latest-dev-cuda11.2-cuDNN8-gcc82



```


### paddle-cuda 纯python应用环境 docker-compose.yml 
```

version: "3"
services:
  one-develop:
    build: .
    image: registry.baidubce.com/paddlepaddle/paddle:3.0.0b1-gpu-cuda12.3-cudnn9.0-trt8.6
    container_name: paddle-cuda
    privileged: true
    ulimits:
      nproc: 65535
      nofile:
         soft: 40000
         hard: 80000
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    # 使用vscode的remote-container无需设置ports,它将自动代理端口,可直接访问。
    # ports:
    #   - 3000:3000
    working_dir: /develop
    network_mode: host  # 使用host网络模式
    volumes:
      - ".:/develop"
      - "./..:/wsl"
      - "./../project:/project"
    stdin_open: true   # 相当于-d 允许后台运行
    tty: true  # 相当于-i  允许交互

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
   2. ci测试
      1. https://www.paddlepaddle.org.cn/documentation/docs/zh/dev_guides/git_guides/paddle_ci_manual_cn.html
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

### 运行python脚本
```


```

### cpp 编译加速
1. ccache
2. Distcc 
3. 技术文章 
   1. C++服务编译耗时优化原理及实践：https://tech.meituan.com/2020/12/10/apache-kylin-practice-in-meituan.html
   2. Include-What-You-Use：


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

### 环境变量
```
        required_envs = {
            "FLAGS_fraction_of_gpu_memory_to_use": "0.15",
            "FLAGS_eager_delete_tensor_gb": "0.0",
            "PATH": os.getenv("PATH"),
            "PYTHONPATH": os.getenv("PYTHONPATH", ""),
            "LD_LIBRARY_PATH": os.getenv("LD_LIBRARY_PATH", ""),
            "LD_PRELOAD": os.getenv("LD_PRELOAD", ""),
            "FLAGS_call_stack_level": "2",
            "GLOG_v": "0", // 可以打印更详细的日志
            "NCCL_P2P_DISABLE": "1",
            "PADDLE_WITH_GLOO": "0",
            "BACKEND": backend,
            "PADDLE_DISTRI_BACKEND": backend,
            "PADDLE_USE_GPU": "1",
        }


```

## 性能优化
1. 模型性能分析方法：https://github.com/PaddlePaddle/community/blob/master/pfcc/paddle-performance-opt/model_perf.md
2. 案例
   1. Paddle2.0.0-rc0的模型预测效率比Torch低很多：https://github.com/PaddlePaddle/Paddle/issues/28774
      1. 调度的耗时占比确实会比较明显
3. 


## cinn测试

### 测试日志参考
1. /develop/Paddle/test/prim/model/test_bert_cinn.py
```
λ docker-desktop /develop/Paddle/test/prim/model python test_bert_cinn.py 
grep: warning: GREP_OPTIONS is deprecated; please use an alias or script
Hint: Your machine support AVX, but the installed paddlepaddle doesn't have avx core. Hence, no-avx core with worse performance will be imported.
If you like, you could reinstall paddlepaddle by 'python -m pip install --force-reinstall paddlepaddle-gpu[==version]' to get better performance.
Cache file /root/.cache/paddle/dataset/test_bert_prim_cinn/bert_training_data.npz not found, downloading https://paddle-ci.gz.bcebos.com/prim_cinn/bert_training_data.npz 
Begin to download
item 21/21 [============================>.] - ETA: 0s - 10ms/item 
Download finished
W1215 12:32:29.050781  2736 gpu_resources.cc:119] Please NOTE: device: 0, GPU Compute Capability: 8.9, Driver API Version: 12.6, Runtime API Version: 12.3
W1215 12:32:29.056697  2736 gpu_resources.cc:164] device: 0, cuDNN Version: 9.0.
<frozen importlib._bootstrap>:914: ImportWarning: _SixMetaPathImporter.find_spec() not found; falling back to find_module()
W1215 12:32:29.792915  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 10 times
W1215 12:32:29.871755  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.872679  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874212  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874294  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874372  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874436  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874886  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.874986  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.875038  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.875061  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.875378  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.875969  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876085  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876204  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876276  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876332  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876412  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876482  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876495  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.876684  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877157  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877266  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877382  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877451  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877506  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877568  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877633  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877660  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.877846  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878314  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878415  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878531  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878598  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878676  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878753  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878844  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.878857  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879024  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879489  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879592  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879707  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879779  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879851  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.879935  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880004  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880030  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880208  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880678  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880782  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880896  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.880967  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.881042  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.881124  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:29.881189  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
I1215 12:32:29.890808  2736 add_cinn_pass.cc:279] FusionOp count before lowering : *****[ 66 ]*****
I1215 12:32:34.385857  2736 add_cinn_pass.cc:293] Time of lowering and compiling program: ***** [ 4 ] ***** seconds.
I1215 12:32:34.385896  2736 add_cinn_pass.cc:297] Number of ops in the original program is: 538, after lowering it becomes: 482. (compression ratio: 482/538 = 0.895911)
W1215 12:32:34.420579  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420619  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420626  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420629  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420632  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420636  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420639  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420642  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420655  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.420714  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420730  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420737  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420739  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420743  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420747  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420751  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420754  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420759  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420763  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420765  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420768  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420780  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.420802  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420858  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420863  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420868  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420871  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420874  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420878  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420881  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420886  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420893  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420898  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420917  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.420943  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.421079  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421097  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421104  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421108  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421111  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421115  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421118  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421121  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421130  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.421198  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421214  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421222  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421226  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421229  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421234  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421237  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421241  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421247  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421249  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421252  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421257  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421267  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.421275  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421362  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421381  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421397  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421451  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421500  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421521  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421546  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421578  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421624  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421643  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421648  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421691  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.421967  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.421993  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422011  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422015  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422020  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422025  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422029  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422032  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422044  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.422310  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422320  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422325  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422328  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422331  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422397  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422420  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422425  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422431  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422434  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422438  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422441  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422466  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.422482  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422614  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422657  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422677  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422736  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422757  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422763  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422767  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422771  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422776  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422780  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422784  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.422850  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.423092  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423116  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423123  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423126  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423130  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423135  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423151  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423156  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423179  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.423367  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423393  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423413  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423447  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423524  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423640  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423660  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423664  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423728  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423846  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.423996  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424126  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424194  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.424232  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424408  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424454  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424471  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424476  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424494  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424510  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424526  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424542  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424548  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424553  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424557  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424572  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.424820  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424849  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424867  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424871  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424888  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424906  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424911  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424914  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.424923  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.424999  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425016  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425022  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425026  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425029  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425033  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425037  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425040  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425069  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425074  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425078  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425082  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425093  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.425240  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425452  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425472  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425499  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425518  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425534  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425550  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425567  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425573  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425578  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425582  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425587  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425612  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.425802  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425823  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425830  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425833  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425837  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425843  2736 shape_analysis.cc:533] pd_op.gelu_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425845  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425849  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425858  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.425938  2736 shape_analysis.cc:533] pd_op.layer_norm_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425967  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.425989  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426005  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426023  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426028  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426095  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426115  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426134  2736 shape_analysis.cc:533] pd_op.dropout_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426151  2736 shape_analysis.cc:533] pd_op.softmax_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426157  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426162  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426175  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
W1215 12:32:34.426242  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426468  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426487  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426492  2736 shape_analysis.cc:533] pd_op.transpose_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426496  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426499  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426503  2736 shape_analysis.cc:533] pd_op.reshape_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426506  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426510  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426514  2736 shape_analysis.cc:533] pd_op.add_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426518  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426522  2736 shape_analysis.cc:533] pd_op.matmul_grad DOES NOT have InferSymbolicShapeInterface!
W1215 12:32:34.426535  2736 pattern_rewrite_driver.cc:225] The pattern rewrite did not converge after scanning 1 times
I1215 12:32:34.427999  2736 add_cinn_pass.cc:279] FusionOp count before lowering : *****[ 18 ]*****
I1215 12:32:34.993058  2736 add_cinn_pass.cc:293] Time of lowering and compiling program: ***** [ 0 ] ***** seconds.
I1215 12:32:34.993103  2736 add_cinn_pass.cc:297] Number of ops in the original program is: 319, after lowering it becomes: 307. (compression ratio: 307/319 = 0.962382)
I1215 12:32:35.009244  2736 pir_interpreter.cc:1570] New Executor is Running ...
I1215 12:32:35.017033  2736 pir_interpreter.cc:1594] pir interpreter is running by multi-thread mode ...
I1215 12:32:35.471349  2736 pir_interpreter.cc:1591] pir interpreter is running by trace mode ...
step: 0, loss: 11.010979652404785, batch_cost: 6.4238
step: 1, loss: 10.31498908996582, batch_cost: 0.025815
step: 2, loss: 10.321041107177734, batch_cost: 0.011979
step: 3, loss: 10.267436027526855, batch_cost: 0.012836
step: 4, loss: 10.227202415466309, batch_cost: 0.016567
step: 5, loss: 10.16740608215332, batch_cost: 0.011665
step: 6, loss: 10.133904457092285, batch_cost: 0.010533
step: 7, loss: 10.06168270111084, batch_cost: 0.010892
step: 8, loss: 10.091561317443848, batch_cost: 0.010146
step: 9, loss: 9.947517395019531, batch_cost: 0.010192
[11.010979652404785, 10.31498908996582, 10.321041107177734, 10.267436027526855, 10.227202415466309, 10.16740608215332, 10.133904457092285, 10.06168270111084, 10.091561317443848, 9.947517395019531]
F
======================================================================
FAIL: test_cinn (__main__.TestBert)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/develop/Paddle/test/prim/model/test_bert_cinn.py", line 136, in test_cinn
    np.testing.assert_allclose(dy2st_cinn, DY2ST_CINN_GT, rtol=1e-5)
  File "/usr/local/lib/python3.10/dist-packages/numpy/testing/_private/utils.py", line 1504, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/usr/lib/python3.10/contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "/usr/local/lib/python3.10/dist-packages/numpy/testing/_private/utils.py", line 797, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=1e-05, atol=0

Mismatched elements: 10 / 10 (100%)
Max absolute difference: 0.3613472
Max relative difference: 0.03393049
 x: array([11.01098 , 10.314989, 10.321041, 10.267436, 10.227202, 10.167406,
       10.133904, 10.061683, 10.091561,  9.947517])
 y: array([10.649632, 10.333406, 10.335412, 10.260544, 10.219606, 10.176885,
       10.1247  , 10.07262 , 10.112164,  9.969394])

----------------------------------------------------------------------
Ran 1 test in 8.275s


```

### pir 打印log
1. https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/paddle_v3_features/cinn_cn.html#sanshiyongshili

### AST IR 打印示例
```
集合：语句实例 & 内存单元
  映射：
   访存关系：语句实例 <---> 内存单元
   依赖关系：语句实例 <---> 语句实例
   执行顺序：语句实例 -----> 语句实例

```


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





## Paddle Serving
1. 源码：https://github.com/PaddlePaddle/Serving/tree/v0.9.0
2. 设计：https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/Serving_Design_CN.md#21-%E8%AE%BE%E8%AE%A1%E9%80%89%E5%9E%8B
3. C++，参考《从零开始写一个预测服务》：https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/C++_Serving/Creat_C++Serving_CN.md
4. Java，参考《Paddle Serving Client Java SDK》
5. CTR服务：https://github.com/PaddlePaddle/Serving/blob/v0.9.0/doc/Cube_Local_CN.md

## 应用开发
1. 案例：https://aistudio.baidu.com/projectoverview/public







## 开发异常

### 梯度爆炸
1. https://aistudio.baidu.com/paddle/forum/topic/show/957441

### core dump
1. https://github.com/PaddlePaddle/Paddle/issues/69003
2. 用户的CPU对AVX的支持是不一样的，从AVX/AVX2/AVX 512都有可能。
3. 虽然在服务器CPU上AVX512非常常见，但是Intel桌面端CPU从13代开始，已经默认不支持AVX512了，只支持AVX2了。
4. https://github.com/PaddlePaddle/Paddle/issues/43181
```

Python 3.10.14 (main, Apr  6 2024, 18:45:05) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import paddle
Illegal instruction (core dumped)


查了一下，仅支持avx2
λ docker-desktop /develop lscpu | grep -o 'avx[^ ]*'
grep: warning: GREP_OPTIONS is deprecated; please use an alias or script
avx
avx2
avx_vnni

临时包
https://paddle-qa.bj.bcebos.com/paddle-pipeline/CompileServicing-LinuxCentos-Commit-Cuda123-WITH_PIP_CUDA_LIBRARIES_ON-WITH_AVX_OFF/59dba7a7b8b3f0f7cfa7cc4e5b4dd28a38b1f431/paddlepaddle_gpu-0.0.0-cp310-cp310-linux_x86_64.whl
```



### ImportError: libcuda.so.1: cannot open shared object file: No such file or directory
```
https://blog.csdn.net/SpadgerZ/article/details/127528618

添加 --gpus all 即可

```


###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```


###
```


```


###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```


###
```


```


###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```


###
```


```


###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```


###
```


```


###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```

###
```


```
