## 推理引擎
1. 官方介绍：https://www.paddlepaddle.org.cn/inference/master/guides/introduction/workflow.html
2. 源码编译基础：https://www.paddlepaddle.org.cn/inference/master/guides/install/compile/compile_basic.html
3. 动态图：paddle.jit.save
4. 静态图：paddle.static.save_inference_model
5. 系统调优：https://www.paddlepaddle.org.cn/inference/master/guides/performance_tuning/index_performance_tuning.html
6. 架构设计：https://www.paddlepaddle.org.cn/inference/master/guides/introduction/design.html

### 基本概念
1. Paddle Inference：飞桨原生推理库，用于服务器端模型部署，支持Python、C/ C++等多语言。
2. Paddle Serving：飞桨服务化部署框架 ，用于云端服务化部署，可以将模型作为单独的预测服务。
3. Paddle Lite：飞桨轻量化推理引擎，用于 Mobile 及 IoT （如嵌入式设备芯片）等场景的部署。
4. Paddle.js：使用 JavaScript（Web）语言部署模型，在网页和小程序中便捷的部署模型。
5. 部署辅助工具1 - PaddleSlim：模型压缩，在保证模型精度的基础上减少模型尺寸，以得到更好的性能或便于放入存储较小的嵌入式芯片。
6. 部署辅助工具2 - X2 Paddle：将其他框架模型转换成Paddle模型，然后即可使用飞桨的一系列工具部署模型。

### 源码编译


### 性能优化

