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
cur_dir=/home/clouddev/software
export PATH="$cur_dir/cmake-3.24.0-linux-x86_64/bin:$PATH"
export PATH="$cur_dir/lib:$cur_dir/bin:$PATH"

wget https://cmake.org/files/v3.24/cmake-3.24.0-linux-x86_64.tar.gz
tar xf cmake-3.24.0-linux-x86_64.tar.gz
export PATH=$cur_dir/include:$cur_dir/bin:$cur_dir/cmake-3.24.0-linux-x86_64/bin:/root/.nvm/versions/node/v14.17.2/bin:/root/.nvm/versions/node/v14.17.2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export LD_LIBRARY_PATH=/usr/local/lib
export LIBRARY_PATH=/usr/local/lib:$cur_dir/lib:$cur_dir/include
export LAPACK_LIBRARIES=/usr/local/lib

### gcc > 8.1

### 源码安装
1. https://xgboost.readthedocs.io/en/stable/build.html
```
cd xgboost
mkdir build
cd build
cmake .. > cmake.txt
make -j10 > make.txt

```


```
