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


## 