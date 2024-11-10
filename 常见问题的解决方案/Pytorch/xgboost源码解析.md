## xgboost
### 理解时间
```
2024年5月5号启动

永远带着问题/需求/目标/兴趣/收益看代码

完整理解xgboost项目
如果只是在搜索引擎 搜 xgboost是远远不够的
xgboost + 架构图

xgboost + 概念关键词

xgboost + 问题排查

xgboost + 面试汇总

xgboost + 极客挑战赛

xgboost + 论坛会议

xgboost + 论文

xgboost + 前沿分享

xgboost + 场景应用

xgboost + xgboost大佬名字

xgboost + 公司项目
等等才能完全熟悉xgboost


```

## 前置准备
### cmake安装
```
wget https://cmake.org/files/v3.24/cmake-3.24.0-linux-x86_64.tar.gz
tar xf cmake-3.24.0-linux-x86_64.tar.gz

cur_dir=/home/clouddev/software
cur_dir=/root/software
export PATH="$cur_dir/cmake-3.24.0-linux-x86_64/bin:$PATH"
export PATH="$cur_dir/lib:$cur_dir/bin:$PATH"


export PATH=$cur_dir/include:$cur_dir/bin:$cur_dir/cmake-3.24.0-linux-x86_64/bin:/root/.nvm/versions/node/v14.17.2/bin:/root/.nvm/versions/node/v14.17.2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export LD_LIBRARY_PATH=/usr/local/lib
export LIBRARY_PATH=/usr/local/lib:$cur_dir/lib:$cur_dir/include
export LAPACK_LIBRARIES=/usr/local/lib
```
### gcc > 8.1

### 源码安装
1. https://xgboost.readthedocs.io/en/stable/build.html
```
cd xgboost
git submodule init
git submodule update

mkdir build
cd build
cmake .. > cmake.txt
make -j10 > make.txt

gpu版本
安装cuda
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local


wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.6.2/local_installers/cuda-repo-ubuntu2204-12-6-local_12.6.2-560.35.03-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu2204-12-6-local_12.6.2-560.35.03-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6


mkdir build_gpu
cd build_gpu
CUDACXX=/usr/local/cuda-12/bin/nvcc cmake .. -DUSE_CUDA=ON > cmake.txt
make -j4 > make.txt

```

### 安装问题
```
CMake Error at /root/software/cmake-3.24.0-linux-x86_64/share/cmake-3.24/Modules/CMakeDetermineCUDACompiler.cmake:602 (message):
  Failed to detect a default CUDA architecture.

原因 有gpu但是无cuda，需要安装cuda



CMake Error at /root/software/cmake-3.24.0-linux-x86_64/share/cmake-3.24/Modules/CMakeDetermineCUDACompiler.cmake:277 (message):
  CMAKE_CUDA_ARCHITECTURES must be non-empty if set.
Call Stack (most recent call first):
  CMakeLists.txt:214 (enable_language)


解决
set(CMAKE_CUDA_ARCHITECTURES "native")
https://stackoverflow.com/questions/77727689/cmake-error-cmake-cuda-architectures-must-be-non-empty-if-set



CMake Error at CMakeLists.txt:214 (enable_language):
  No CMAKE_CUDA_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CUDACXX" or the CMake cache entry CMAKE_CUDA_COMPILER to the full
  path to the compiler, or to the compiler name if it is in the PATH.


解决
CUDACXX=/usr/local/cuda-12/bin/nvcc cmake .. -DUSE_CUDA=ON > cmake.txt

https://stackoverflow.com/questions/72278881/no-cmake-cuda-compiler-could-be-found-when-installing-pytorch

CUDACXX=/usr/local/cuda-11.7/bin/nvcc cmake -S /path/to/source/dir -B /path/to/build/dir


```