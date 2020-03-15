## 参考资料
- nodejs官网：https://www.runoob.com/nodejs
- next：http://theme-next.iissnan.com/

## 国内镜像源
```
https://www.jianshu.com/p/0deb70e6f395
https://developer.aliyun.com/mirror/NPM?from=tnpm

npm config set registry https://registry.npm.taobao.org
// 配置后可通过下面方式来验证是否成功
npm config get registry
// 或npm info express

```

## demo
### 执行hellow world
```
node demo/helloworld.js
```

### 创建服务器
```
node demo/server.js
```

### 阻塞方式读取文件
```
node demo/block.js
```

### 非阻塞方式读取文件-回调函数
```
node demo/unblock.js
```

### 事件循环
```
node demo/loopevent.js

Node.js 是单进程单线程应用程序，但是因为 V8 引擎提供的异步执行回调接口，通过这些接口可以处理大量的并发，所以性能非常高。

Node.js 几乎每一个 API 都是支持回调函数的。

Node.js 基本上所有的事件机制都是用设计模式中观察者模式实现。

Node.js 单线程类似进入一个while(true)的事件循环，直到没有事件观察者退出，每个异步事件都生成一个事件观察者，如果有事件发生就调用该回调函数.

 Node.js 使用事件驱动模型，当web server接收到请求，就把它关闭然后进行处理，然后去服务下一个web请求。

当这个请求完成，它被放回处理队列，当到达队列开头，这个结果被返回给用户。

这个模型非常高效可扩展性非常强，因为 webserver 一直接受请求而不等待任何读写操作。（这也称之为非阻塞式IO或者事件驱动IO）
在事件驱动模型中，会生成一个主循环来监听事件，当检测到事件时触发回调函数。
```


## npm
```
包管理
npm install <Module Name>

全局安装与本地安装
npm install express          # 本地安装，当前目录下
npm install express -g   # 全局安装

查看某个模块的版本号
npm list grunt

查看所有全局安装的模块
npm list -g

```

### 模块
```

```


## 报错
### throw er; // Unhandled 'error' event

```
端口号被占用了，换一个端口
```


## hexo
```
安装教程：https://hexo.io/zh-cn/index.html
```

