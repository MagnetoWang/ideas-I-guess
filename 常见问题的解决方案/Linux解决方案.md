![Linux解决方案](https://github.com/MagnetoWang/ideas-I-guess/blob/master/markdown-for-document-organization-management/manage-pictures/linux-how-to-use.png)



## 说明

- 作为Windows的老用户，不得不说，Linux真难用！
- 作为计算机专业的我来说，Linux不得不学！

## 使用感受

- linux更多是面向多人同时一台机器的操作系统，所以需要考虑到各种环境配置问题

[TOC]



## 命令行问题

- ls：显示文件目录
- ll：显示文件目录详细信息
- cd：打开文件夹或者返回

## 文件常用操作

- cat：打开并显示文件

- tail：指定显示文件的几行内容

  - 从第5行开始显示文件 ：tail -n +5 log2014.log 

  - 循环查看文件内容 ：tail -f test.log ：配合其他命令边写边显示。效果佳

  - 显示文件最新的内容：tail -f filename ：和上面一样。理解程度不一样，用法不一样

  - 显示文件末尾5行内容 ：tail -n 5 log2014.log 

```
    tail file （显示文件file的最后10行）
    tail +20 file （显示文件file的内容，从第20行至文件末尾）
    tail -c 10 file （显示文件file的最后10个字符）
```

- vim ：编辑文件，注意不要打开超大文件。非常吃内存

- more：http://man.linuxde.net/more：

  - 单开屏幕显示文件，更加详细查看内容

  - 按Space键：显示文本的下一屏内容。

  - 按Enier键：只显示文本的下一行内容。

  - 按斜线符`|`：接着输入一个模式，可以在文本中寻找下一个相匹配的模式。

  - 按H键：显示帮助屏，该屏上有相关的帮助信息。

  - 按B键：显示上一屏内容。

  - 按Q键：退出rnore命令。

```
    more -c -10 file
```

- less：http://man.linuxde.net/less

  - 类似more。但是more只能往下看，不能往上看
  - less可以向上和向下卡n

## Linux工具
1. 采集系统指标：https://github.com/aristocratos/btop?tab=readme-ov-file
2. 有哪些适合个人练手的中等规模的C++项目？ - Rocky0429的回答 - 知乎 https://www.zhihu.com/question/56579764/answer/3183916295
3. c++ debug日志工具：https://github.com/sharkdp/dbg-macro

- **系统**

```
  # uname -a               # 查看内核/操作系统/CPU信息
  # cat /proc/version  	 # 查看操作系统版本
  # cat /proc/cpuinfo      # 查看CPU信息
  # more /proc/cpuinfo     # 查看CPU信息 可以翻页
  # hostname               # 查看计算机名
  # lspci -tv              # 列出所有PCI设备
  # lsusb -tv              # 列出所有USB设备
  # lsmod                  # 列出加载的内核模块
  # lspci -tv                    # 查看环境变量
```


**资源**

```
  # free -m                # 查看内存使用量和交换区使用量
  # df -h                  # 查看各分区使用情况
  # du -sh <目录名>        # 查看指定目录的大小
  # grep MemTotal /proc/meminfo   # 查看内存总量
  # grep MemFree /proc/meminfo    # 查看空闲内存量
  # uptime                 # 查看系统运行时间、用户数、负载
  # cat /proc/loadavg      # 查看系统负载
```

**磁盘和分区**

```
  # mount | column -t      # 查看挂接的分区状态
  # fdisk -l               # 查看所有分区
  # swapon -s              # 查看所有交换分区
  # hdparm -i /dev/hda     # 查看磁盘参数(仅适用于IDE设备)
  # dmesg | grep IDE       # 查看启动时IDE设备检测状况
```

**网络**

```
  # ifconfig               # 查看所有网络接口的属性
  # iptables -L            # 查看防火墙设置
  # route -n               # 查看路由表
  # netstat -lntp          # 查看所有监听端口
  # netstat -antp          # 查看所有已经建立的连接
  # netstat -s             # 查看网络统计信息
```

**进程**

```
  # ps -ef                 # 查看所有进程
  # ps -xf				 # 查看个人权限下的进程
  # top                    # 实时显示进程状态
```

**用户**

```
  # w                      # 查看活动用户
  # id <用户名>            # 查看指定用户信息
  # last                   # 查看用户登录日志
  # cut -d: -f1 /etc/passwd   # 查看系统所有用户
  # cut -d: -f1 /etc/group    # 查看系统所有组
  # crontab -l             # 查看当前用户的计划任务
```

**服务**

```
  # chkconfig --list       # 列出所有系统服务
  # chkconfig --list | grep on    # 列出所有启动的系统服务
```

**程序**

```
  # rpm -qa                # 查看所有安装的软件包
```



## Linux目录说明

- https://www.jianshu.com/p/fe8da5d08e16

  ```
  简单说,/lib64是内核级的,/usr/lib64是系统级的,/usr/local/lib64是用户级的.
  ```

/lib/ — 包含许多被 /bin/ 和 /sbin/ 中的程序使用的库文件。目录 /usr/lib/ 中含有更多用于用户程序的库文件。/lib目录下放置的是/bin和/sbin目录下程序所需的库文件。/lib目录下的文件的名称遵循下面的格式： 
libc.so.* 
ld* 
仅仅被/usr目录下的程序所使用的共享库不必放到/lib目录下。只有/bin和/sbin下的程序所需要的库有必要放到/lib目录下。实际上，libm.so.*类型的库文件如果被是/bin和/sbin所需要的，也可以放到/usr/lib下。

/bin/ — 用来贮存用户命令。目录 /usr/bin 也被用来贮存用户命令。

/sbin/ — 许多系统命令（例如 shutdown）的贮存位置。目录 /usr/sbin 中也包括了许多系统命令。

/root/ — 根用户（超级用户）的主目录。

/mnt/ — 该目录中通常包括系统引导后被挂载的文件系统的挂载点。譬如，默认的光盘挂载点是 /mnt/cdrom/.

/boot/ — 包括内核和其它系统启动期间使用的文件。

/lost+found/ — 被 fsck 用来放置零散文件（没有名称的文件）。

/lib64/ — 包含许多被 /bin/ 和 /sbin/ 中的程序使用的库文件。目录 /usr/lib/ 中含有更多用于用户程序的库文件。

/dev/ — 贮存设备文件。

/etc/ — 包含许多配置文件和目录。

/var/ — 用于贮存variable（或不断改变的）文件，例如日志文件和打印机假脱机文件。

/usr/ — 包括与系统用户直接有关的文件和目录，例如应用程序及支持它们的库文件。

/proc/ — 一个虚拟的文件系统（不是实际贮存在磁盘上的），它包括被某些程序使用的系统信息。

/initrd/ — 用来在计算机启动时挂载 initrd.img 映像文件的目录以及载入所需设备模块的目录。


/usr/lib64/libstdc++.so.6
https://blog.csdn.net/xg123321123/article/details/78117162



```



## 排查线上问题

### 性能工具

- top
  - 查询cpu情况：https://blog.csdn.net/GitChat/article/details/79019454
- free
  - 查询内存：-m,-g
  - 返回MB，GB格式
- dstat
  - 查询网络情况
  - -c  cpu 情况    -d 磁盘读写        -n 网络状况        -l 显示系统负载        -m 显示形同内存状况        -p 显示系统进程信息        -r 显示系统 IO 情况 

### 排除工具

- https://my.oschina.net/leejun2005/blog/1524687

### 排查步骤

- 参考链接
  - https://tech.meituan.com/performance_tunning.html
  - https://blog.csdn.net/lipc_/article/details/52733651
- **紧急处理** 
  - **对于紧急的大面积故障，首先想到的不应该是检查问题。而是需要立刻追查最近线上系统是否有更改，我们的经验是****95%的故障都是在新代码上线后的12小时内发生的。此时应该立刻回滚新更改。另外5%****的故障大部分是由于业务扩展导致的。**互联网业有一个规律，线上系统每半年需要重构一次，否则无法对应业务量的增长。对于这种业务量增长造成的故障，通常可以通过重启服务来紧急处理。 
  - 因此，**紧急处理的首选是立刻回滚新更改。** 
- **添加监控** 
  - 紧急处理之后，服务已经恢复了，但是问题并没有找到。如果是新代码上线造成的故障，回滚之后，工程师会有各种手段，在测试环境追查问题。而针对系统容量不足造成的故障，需要特别添加监控作为追查问题的重要手段。因为互联网业务请求高峰和低谷差别非常明显，微博业务中的请求高峰往往出现在晚上10点左右，而且不是稳定的出现。 
- **JDK性能监控** 
- **分析源代码** 

## Java虚拟机排查问题

### 命令快速使用

- 打印进程使用虚拟机的每一代情况：jmap -J-d64 -heap pid

### 排查工具

- jps -m 
  - 快速定位当前服务器运行的java进程，并给出路径

### 排查指标

- gc time
- gc count
- 各个分代的内存大小变化
- 机器的Load值与CPU使用率
- JVM的线程数
- gc log
- jstat等命令的输出 

# 美团文档内容-非常值得反复多看！

### 怎么调？

- 如果发现高峰期CPU使用率与Load值偏大，这个时候可以观察一些JVM的thread count以及gc count（可能主要是young gc count），如果这两个值都比以往偏大（也可以和一个历史经验值作对比），基本上可以定位是young gc频率过高导致，这个时候可以通过适当增大young区大小或者占比的方式来解决。
- 如果发现关键接口响应时间很慢，可以结合gc time以及gc log中的stop the world的时间，看一下整个应用的stop the world的时间是不是比较多。如果是，可能需要减少总的gc time，具体可以从减小gc的次数和减小单次gc的时间这两个维度来考虑，一般来说，这两个因素是一对互斥因素，我们需要根据实际的监控数据来调整相应的参数（比如新生代与老生代比值、eden与survivor比值、MTT值、触发cms回收的old区比率阈值等）来达到一个最优值。
- 如果发生full gc或者old cms gc非常频繁，通常这种情况会诱发STW的时间相应加长，从而也会导致接口响应时间变慢。这种情况，大概率是出现了“内存泄露”，Java里的内存泄露指的是一些应该释放的对象没有被释放掉（还有引用拉着它）。那么这些对象是如何产生的呢？为啥不会释放呢？对应的代码是不是出问题了？问题的关键是搞明白这个，找到相应的代码，然后对症下药。所以问题的关键是转化成寻找这些对象。怎么找？综合使用**jmap和MAT**，基本就能定位到具体的代码。

### 多线程与分布式

### 使用场景

离线任务、异步任务、大数据任务、耗时较长任务的运行**，适当地利用，可达到加速的效果。

注意：**线上对响应时间要求较高的场合，尽量少用多线程，尤其是服务线程需要等待任务线程的场合（很多重大事故就是和这个息息相关）**，如果一定要用，可以对服务线程设置一个最大等待时间。

### 常见做法

如果单机的处理能力可以满足实际业务的需求，那么尽可能地使用单机多线程的处理方式，减少复杂性；反之，则需要使用多机多线程的方式。

对于**单机多线程**，可以引入**线程池**的机制，作用有二：

- **提高性能，节省线程创建和销毁的开销**
- **限流，给线程池一个固定的容量，达到这个容量值后再有任务进来，就进入队列进行排队，保障机器极限压力下的稳定处理能力**在使用JDK自带的线程池时，一定要仔细理解构造方法的各个参数的含义，如**core pool size、max pool size、keepAliveTime、worker queue**等，在理解的基础上通过不断地测试调整这些参数值达到最优效果。

如果单机的处理能力不能满足需求，这个时候需要使用**多机多线程**的方式。这个时候就需要一些分布式系统的知识了。首先就必须引入一个单独的节点，作为调度器，其他的机器节点都作为执行器节点。调度器来负责拆分任务，和分发任务到合适的执行器节点；执行器节点按照多线程的方式（也可能是单线程）来执行任务。这个时候，我们整个任务系统就由单击演变成一个集群的系统，而且不同的机器节点有不同的角色，各司其职，各个节点之间还有交互。这个时候除了有多线程、线程池等机制，像RPC、心跳等网络通信调用的机制也不可少。后续我会出一个简单的分布式调度运行的框架。

## 度量系统（监控、报警、服务依赖管理）

严格来说，度量系统不属于性能优化的范畴，但是这方面和性能优化息息相关，可以说为性能优化提供一个强有力的数据参考和支撑。没有度量系统，基本上就没有办法定位到系统的问题，也没有办法有效衡量优化后的效果。很多人不重视这方面，但我认为它是系统稳定性和性能保障的基石。

### 关键流程

如果要设计这套系统，总体来说有哪些关键流程需要设计呢？
① 确定指标
② 采集数据
③ 计算数据，存储结果
④ 展现和分析

### 需要监控和报警哪些指标数据？需要关注哪些？

按照需求出发，主要需要二方面的指标：

1. 接口性能相关，包括单个接口和全部的QPS、响应时间、调用量（统计时间维度越细越好；最好是，既能以节点为维度，也可以以服务集群为维度，来查看相关数据）。其中还涉及到服务依赖关系的管理，这个时候需要用到服务依赖管理系统
2. 单个机器节点相关，包括CPU使用率、Load值、内存占用率、网卡流量等。如果节点是一些特殊类型的服务（比如MySQL、Redis、Tair），还可以监控这些服务特有的一些关键指标。

### 数据采集方式

通常采用异步上报的方式，具体做法有两种：第一种，发到本地的Flume端口，由Flume进程收集到远程的Hadoop集群或者Storm集群来进行运算；第二种，直接在本地运算好以后，使用异步和本地队列的方式，发送到监控服务器。

### 数据计算

可以采用离线运算（MapReduce/Hive）或者实时/准实时运算（Storm/Spark）的方式，运算后的结果存入MySQL或者HBase；某些情况，也可以不计算，直接采集发往监控服务器。

### 展现和分析

提供统一的展现分析平台，需要带报表（列表/图表）监控和报警的功能。

# 真实案例分析

## 案例一：商家与控制区关系的刷新job

### 背景

这是一个每小时定期运行一次的job，作用是用来刷新商家与控制区的关系。具体规则就是根据商家的配送范围（多个）与控制区是否有交集，如果有交集，就把这个商家划到这个控制区的范围内。

### 业务需求

需要这个过程越短越好，最好保持在20分钟内。

### 优化过程

原有代码的主要处理流程是：

1. 拿到所有门店的配送范围列表和控制区列表。
2. 遍历控制区列表，针对每一个控制区：
   a. 遍历商家的配送范围列表，找到和这个控制区相交的配送范围列表。
   b. 遍历上述商家配送范围列表，对里面的商家ID去重，保存到一个集合里。
   c. 批量根据上述商家ID集合，取到对应的商家集合。
   d. 遍历上述商家集合，从中拿到每一个商家对象，进行相应的处理（根据是否已是热门商家、自营、在线支付等条件来判断是否需要插入或者更新之前的商家和控制区的关系）。
   e. 删除这个控制区当前已有的，但是不应该存在的商家关系列表。

分析代码，发现第2步的a步骤和b步骤，找出和某控制区相交的配送范围集合并对商家ID去重，可以采用R树空间索引的方式来优化。具体做法是：

- 任务开始先更新R树，然后利用R树的结构和匹配算法来拿到和控制区相交的配送范围ID列表。
- 再批量根据配送范围ID列表，拿到配送范围列表。
- 然后针对这一批配送范围列表（数量很小），用原始多边形相交匹配的方法做进一步过滤，并且对过滤后的商家ID去重。

这个优化已经在第一期优化中上线，整个过程耗时**由40多分钟缩短到20分钟以内**。

第一期优化改为R树以后，运行了一段时间，随着数据量增大，性能又开始逐渐恶化，一个月后已经恶化到50多分钟。于是继续深入代码分析，寻找了两个优化点，安排第二期优化并上线。

这两个优化点是：

- 第2步的c步骤，原来是根据门店ID列表从DB批量获取门店，现在可以改成mget的方式从缓存批量获取（此时商家数据已被缓存）；
- 第2步的d步骤，根据是否已是热门商家、自营、在线支付等条件来判断是否需要插入或者更新之前的商家和控制区的关系。

### 上线后效果

通过日志观察，执行时间**由50多分钟缩短到15分钟以内**，下图是截取了一天的4台机器的日志时间（单位：**毫秒**）：
![poi优化效果图](https://tech.meituan.com/img/poi%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE.png)
可以看到，效果还是非常明显的。

## 案例二：POI缓存设计与实现

### 背景

2014年Q4，数据库中关于POI（这里可以简单理解为外卖的门店）相关的数据的**读流量**急剧上升，虽然说加入从库节点可以解决一部分问题，但是毕竟节点的增加是会达到极限的，达到极限后主从复制会达到瓶颈，可能会造成数据不一致。所以此时，急需引入一种新的技术方案来分担数据库的压力，降低数据库POI相关数据的读流量。另外，任何场景都考虑加DB从库的做法，会对资源造成一定的浪费。

### 实现方案

基于已有的经过考验的技术方案，我选择Tair来作为缓存的存储方案，来帮DB分担来自于各应用端的POI数据的读流量的压力。理由主要是从**可用性、高性能、可扩展性、是否经过线上大规模数据和高并发流量的考验、是否有专业运维团队、是否有成熟工具**等几个方面综合考量决定。

### 详细设计

#### 第一版设计

缓存的更新策略，根据业务的特点、已有的技术方案和实现成本，选择了用MQ来接收POI改变的消息来触发缓存的更新，但是这个过程有可能失败；同时启用了key的过期策略，并且调用端会先判断是否过期，如过期，会从后端DB加载数据并回设到缓存，再返回。通过两个方面双保险确保了缓存数据的可用。

#### 第二版设计

第一版设计运行到一段时间以后，我们发现了两个问题：

1. 某些情况下不能保证数据的实时一致（比如技术人员手动改动DB数据、利用MQ更新缓存失败），这个时候只能等待5分钟的过期时间，有的业务是不允许的。
2. 加入了过期时间导致另外一个问题：Tair在缓存不命中的那一刻，会尝试从硬盘中Load数据，如果硬盘没有再去DB中Load数据。这无疑会进一步延长Tair的响应时间，这样不仅使得业务的超时比率加大，而且会导致Tair的性能进一步变差。

为了解决上述问题，我们从美团点评负责基础架构的同事那里了解到[Databus](https://github.com/linkedin/databus)可以解决缓存数据在某些情况下不一致的问题，并且可以去掉过期时间机制，从而提高查询效率，避免tair在内存不命中时查询硬盘。而且为了防止DataBus单点出现故障影响我们的业务，我们保留了之前接MQ消息更新缓存的方案，作了切换开关，利用这个方案作容错，整体架构如下：
![poi缓存设计图](https://tech.meituan.com/img/poi%E7%BC%93%E5%AD%98%E8%AE%BE%E8%AE%A1%E5%9B%BE.png)

### 上线后效果

上线后，通过持续地监控数据发现，随着调用量的上升，到DB的流量有了明显地减少，极大地减轻了DB的压力。同时这些数据接口的响应时间也有了明显地减少。缓存更新的双重保障机制，也基本保证了缓存数据的可用。见下图：
![poi缓存优化效果图_1](https://tech.meituan.com/img/poi%E7%BC%93%E5%AD%98%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE_1.png)
![poi缓存优化效果图](https://tech.meituan.com/img/poi%E7%BC%93%E5%AD%98%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE.png)

## 案例三：业务运营后台相关页面的性能优化

### 背景

随着业务的快速发展，带来的访问量和数据量的急剧上升，通过我们相应的监控系统可以发现，系统的某些页面的性能开始出现恶化。 从用户方的反馈，也证明了这点。此时此刻，有必要迅速排期，敏捷开发，对这些页面进行调优。

### 欢迎页

- 需求背景：欢迎页是地推人员乃至总部各种角色人员进入外卖运营后台的首页，会显示地推人员最想看到最关心的一些核心数据，其重要性不言而喻，所以该页面的性能恶化会严重影响到用户体验。因此，首先需要优化的就是欢迎页。通过相应定位和分析，发现导致性能恶化的主要原因有两个：数据接口层和计算展现层。
- 解决方案：对症下药，分而治之。经过仔细排查、分析定位，数据接口层采用接口调用批量化、异步RPC调用的方式来进行有效优化，计算展现层决定采用预先计算、再把计算好的结果缓存的方式来提高查询速度。其中，缓存方案根据业务场景和技术特点，选用Redis。定好方案后，快速开发上线。
- 上线效果：上线后性能对比图，如下：
  ![优化效果图_1](https://tech.meituan.com/img/%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE_1.png)

### 组织架构页

- 需求背景：组织架构页，采用了四层树形结构图，一起呈现加载，第一版上线后发现性能非常差。用户迫切希望对这个页面的性能进行调优。
- 解决方案：经过分析代码，定位到一个比较经典的问题：里面执行了太多次小数据量的SQL查询。于是采用多个SQL合并成大SQL的方式，然后使用本地缓存来缓存这些数据，合理预估数据量和性能，充分测试后上线。
- 上线效果：上线后性能对比图，如下：
  ![优化效果图_2](https://tech.meituan.com/img/%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE_2.png)

### 订单关联楼宇页

- 需求背景：随着订单量日益增大，订单表积累的数据日益增多，订单关联楼宇页的性能也日益变差（响应时间线性上升）。而这个页面和地推人员的业绩息息相关，所以地推人员使用该页面的频率非常高，性能日益恶化极大地影响了地推人员的用户体验。
- 解决方案：经过分析与设计，决定采用当时已有的订单二级索引月分表来代替原始的订单表来供前端的查询请求；并且限制住筛选的时间条件，使得筛选的开始时间和结束时间不能跨月（事先和用户沟通过，可以接受，能满足用户的基本需求），这样就只需一个月分索引表即可，通过适当的功能限制来达到性能的调优。这样从二级索引月分表中根据各种查询条件查到最终的分页的订单ID集合，然后再根据订单ID从订单库来查出相应的订单数据集合。
- 上线效果：上线后发现在调用量几乎没怎么变的情况下，性能提升明显，如下图：
  ![优化效果图_3](https://tech.meituan.com/img/%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C%E5%9B%BE_3.png)

## 其他

除了上面介绍的之外，优化还涉及前端、分布式文件系统、CDN、全文索引、空间索引等几方面。限于篇幅，我们留到未来再做介绍。

# Linux基础

## 基本概念

- POSIX：https://en.wikipedia.org/wiki/POSIX
  - The Portable Operating System Interface (POSIX)

### glibc

```
https://www.gnu.org/software/libc/
https://github.com/bminor/glibc

The GNU C Library project provides the core libraries for the GNU system and GNU/Linux systems, as well as many other systems that use Linux as the kernel. These libraries provide critical APIs including ISO C11, POSIX.1-2008, BSD, OS-specific APIs and more. These APIs include such foundational facilities as open, read, write, malloc, printf, getaddrinfo, dlopen, pthread_create, crypt, login, exit and more.

```

## 基本操作

- vim
  - 保存退出：:wq
  - 不保存退出：:q!
  - 
- make
  - 默认编译makefile
  - -j5：同时运行5个jobs
- cmake

  - 默认编译CMakeLists.txt
- 查看系统编码

  - locale：https://blog.csdn.net/jbxue123/article/details/17909913
- 一切皆文件

  - lsof ：https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/lsof.html
- top
  - 查看cpu占用率
- vscode同步服务器
  - https://www.jianshu.com/p/390c68a0cc58
- date -R
  - 查看当前时区
  - https://www.cnblogs.com/h2appy/archive/2008/11/27/1342029.html
- ip address
  - 查看本机ip地址
- kill -s 9 pid
  - 杀死进程
- netstat -an | grep 6181 

    - 查看端口
  - lsof -i;2181
      - 查看端口
  - Proto Recv-Q Send-Q Local Address           Foreign Address         State
- cp sourceDir destDir
  - 复制文件
  - 同时可以修改名字
- date +%s
  - 获取时间戳
- $(cd "$(dirname "$0")"; pwd)
  - 这个文件当前路径，shell脚本中使用
- touch file
  - 修改文件时间戳
- 批量删除进程
  - ps -ef | grep xxx | grep -v root | awk '{print $1}' | xargs kill -9
  - ps -ef | grep --zk_root_path=/onebox | awk '{print $1}' | xargs kill -9
  - awk 是核心把单列打印出来
  - xargs 一口气全部删除
- ps -xf 

  - 只显示自己的进程
- 创建文件

  - touch filename

## 基本功能

- 查询系统版本
  -  cat /proc/version
  - https://www.qiancheng.me/post/coding/show-linux-issue-version

- 安装java和配置路径

  - wget http://pkg.4paradigm.com/jdk/jdk-8u141-linux-x64.tar.gz
  - 解压：https://blog.csdn.net/FX677588/article/details/76100538
  - tar -zxvf ×××.tar.gz
  - vi ~/.bash_profile
  - export JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141/bin/java
  - export PATH=$PATH:/home/wangzixian/java/jdk1.8.0_141/bin
  - source ~/.bash_profile
  - https://www.cyberciti.biz/faq/linux-unix-set-java_home-path-variable/

- 安装和配置maven和路径

  - https://www.baeldung.com/install-maven-on-windows-linux-mac

  - http://maven.apache.org/download.cgi

  - ```
    export JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141
    export JRE_HOME=home/wangzixian/java/jdk1.8.0_141/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib
    export PATH=$PATH:/home/wangzixian/java/jdk1.8.0_141/bin
    
    export MAVEN_HOME=/home/wangzixian/maven/apache-maven-3.5.4
    export PATH=${MAVEN_HOME}/bin:${PATH}
```

  - mvn -X 可以查看settings.xml路径位置

- 打开文件

  - 显示行号：http://blog.sina.com.cn/s/blog_716844910100tfxv.html
  - cat -n filename

- 性能查找

  - https://www.cnblogs.com/emanlee/p/3587571.html

- 解压

  - tar -zxvf ×××.tar.gz
  - tar -jxvf ×××.tar.bz2
  - unrar x xxxxx.rar 需要安装rar软件 brew install carlocab/personal/unrar
  - https://blog.csdn.net/FX677588/article/details/76100538

- 安装zsh

  - https://harttle.land/2016/10/25/install-oh-my-zsh-locally.html
  - 全路径显示：https://blog.csdn.net/s_gy_zetrov/article/details/80158409

### 非root情况下安装python的nose

- python setup.py install --user
- 加一个user
- https://stackoverflow.com/questions/21093002/error-could-not-create-usr-local-lib-python2-7-dist-packages-virtualenv-suppo

### 修改系统编码

```bash
vi ~/.bash_profile
export LANG="en_US.UTF-8"
source ~/.bash_profile
```


## Linux下的C++

### 基本编译运行

- g++ helloworld.cpp -o helloworld
- ./helloworld

### 复杂文件编译运行

- 需要编写makefile

### 编译中的动态库和静态库

- 参考资料：
  - https://www.jianshu.com/p/63ea84c9666e
  - https://segmentfault.com/q/1010000005269977
- 静态库是指编译连接时，把库文件的代码全部加入到可执行文件中，所以生成的文件较大，但运行时，就不再需要库文件了。即，程序与静态库编译链接后，即使删除静态库文件，程序也可正常执行。
- 动态库正好相反，在编译链接时，没有把库文件的代码加入到可执行文件中，所以生成的文件较小，但运行时，仍需要加载库文件。即，程序只在执行启动时才加载动态库，如果删除动态库文件，程序将会因为无法读取动态库而产生异常。
- 静态库.a
- 动态库.so
- --enable-static 生成静态库a文件
- --enable-shared 生成共享库so文件

### 代码同步

```
sshfs 可以让本地目录同步到远程服务端，这样本地写代码，自动就能同步到远程编译，不需要vim
类似docker -v xxx
属于docker挂载方式，有个干净的编译环境

```



## Vim

### 基本操作

- 参考资料：https://zhuanlan.zhihu.com/p/60334138

```
j 向下
30j 向下移动30行
k 向上
h 向左
l 向右
0 到行首
^ 到行首第一个字符，如果前面有空格的话
$ 到行尾
gg 快速到文件头
G 快速到文件尾
100G 跳转到第100行

yy 复制一行
10yy 向下复制10行
yw 复制光标开始的一个单词
y$ 复制光标到行尾
yfB 复制光标到第一个大写B中间的内容
y2fB 复制光标到第二个大写B中间的内容

x 向剪切一个一个字符，如果是在行尾，则为向前剪切
3x 剪切三个
xp 非行尾交换两个字符，如从bs变成sb

dd 删除一行
200dd 删除200行
dw 删除一个单词 （最喜欢啦）
df" 删除到出现的第一个双引号


p 粘贴复制或剪切的内容
3p 将复制或剪切的内容粘贴三次

wq 保存当前文件并退出
wqa 保存所有文件并退出
q! 不保存，直接退出
qa! 有多个文件被打开，同时退出

```



## Linux功能

### 建立临时服务器

```
python2
python -m SimpleHTTPServer 1234

python3
python3 -m http.server 1234

在网页上 ip:1234 就可以访问服务器
```

### namespace隔离容器 

```
https://www.cnblogs.com/sammyliu/p/5878973.html
```

### vnc远程终端控制
```
在家自建linux服务器，mac远程控制屏幕即可。这样既有mac的轻薄，也能有linux可视化开发环境

瓶颈
需要一定网络带宽开销


 vncserver -geometry 1920x1080
 
 export LC_ALL="en_US.UTF-8"
export LANGUAGE="en_US.UTF-8"


安装VNC viewer
https://www.realvnc.com/en/connect/download/viewer/?lai_vid=dPx2b3bXRhrjv&lai_sr=0-4&lai_sl=l&lai_p=1

安装VNC Server
yum groups install "GNOME Desktop" -y




```

### 机器诊断

```
把脉

文件配置
ulimit -a
网络配置
sysctl -p
```



# Linux下的Shell

## 基础

### 待了解命令

```
popd pushd fg bg
ldd --version
```



### /dev/null 含义

- /dev/null ：代表空设备文件

- echo log > /dev/null 2>&1

  >  ：代表重定向到哪里，例如：echo "123" > /home/123.txt
  >  1  ：表示stdout标准输出，系统默认值是1，所以">/dev/null"等同于"1>/dev/null"
  >  2  ：表示stderr标准错误
  >  &  ：表示等同于的意思，2>&1，表示2的输出重定向等同于1

- https://blog.csdn.net/ithomer/article/details/9288353

### /dev/shm 虚拟目录

```
这个目录是把文件存在内存中的，重启后里面的文件都会消失
用与借用他人机器，但是又不希望留下痕迹的场景
```



### if语法

- https://blog.csdn.net/yf210yf/article/details/9207147
- 常用条件判断：https://blog.csdn.net/ithomer/article/details/5904632

```
#!/usr/bin/env bash
table_number=500
for ((i=0; i<table_number; i++)); do
	# touch test_$i.txt
    table_name=table_$i
    reminder=`expr $i % 3`
    echo $reminder
    if [ $reminder -eq 0 ]; then
	echo $reminder
    elif [ $reminder -eq 1 ]; then
        echo $reminder
    else
        echo $reminder
    fi
done


1 字符串判断

str1 = str2　　　　　　当两个串有相同内容、长度时为真 
str1 != str2　　　　　 当串str1和str2不等时为真 
-n str1　　　　　　　 当串的长度大于0时为真(串非空) 
-z str1　　　　　　　 当串的长度为0时为真(空串) 
str1　　　　　　　　   当串str1为非空时为真

2 数字的判断

int1 -eq int2　　　　两数相等为真 
int1 -ne int2　　　　两数不等为真 
int1 -gt int2　　　　int1大于int2为真 
int1 -ge int2　　　　int1大于等于int2为真 
int1 -lt int2　　　　int1小于int2为真 
int1 -le int2　　　　int1小于等于int2为真

3 文件的判断

-r file　　　　　用户可读为真 
-w file　　　　　用户可写为真 
-x file　　　　　用户可执行为真 
-f file　　　　　文件为正规文件为真 
-d file　　　　　文件为目录为真 
-c file　　　　　文件为字符特殊文件为真 
-b file　　　　　文件为块特殊文件为真 
-s file　　　　　文件大小非0时为真 
-t file　　　　　当文件描述符(默认为1)指定的设备为终端时为真

3 复杂逻辑判断

-a 　 　　　　　 与 
-o　　　　　　　 或 
!　　　　　　　　非

```

### while语法

- example：https://www.cyberciti.biz/faq/shell-script-while-loop-examples/

```

```



### for语法

- for element in $file
- do
- xxxxxxxxx
- done
- 扩展用法
- 循环1到100
  - for i in {1..100}
  - for i in `seq 1 100`

```
while是完全按行读取，不管行内有多少段文字；

for是按行读取，如果行内文字有空格，则分开读取，即一次读取一个字符串。

 core/xxx/ttt.java                
 core/xxx/{zz.java => kkk.java}      
 pom.xml    

因为=> 两边是空格，for打印这一行就是不完整的了
要用while


```



### 运算符

- http://www.runoob.com/linux/linux-shell-basic-operators.html

### export

```
    #设置历史命令记录数  
    export HISTSIZE=1000  
    #记录历史文件大小   
    export HISTFILESIZE=450  
```

### wget

```
wget -r -nH --cut-dirs=5 ftp://ftp.io/pub

wget 下载文件夹




wget 

递归下载：

wget -r -l1 --no-parent http://172.27.128.206:8080/rp/

拉取 http://172.27.128.206:8080/rp/ 下内容，其中

-r 递归模式

-l 递归深度，1表示当前目录，不会拉取次级目录。0表示最大深度。



```



### unset

```
unset 某个环境变量的名字 
置位空字符串这个环境变量
```

### alias

```
https://wangchujiang.com/linux-command/c/alias.html
# 显示全部已定义的别名
alias
alias -p

# 显示已定义的别名（假设当前环境存在以下别名）
alias ls
alias ls grep

# 定义或修改别名的值
alias ls='ls --color=auto'
alias ls='ls --color=never' grep='grep --color=never'


```



### ulimit -c unlimite

### cd

- cd - 可以返回上一次操作目录，不是上一个目录

### sed

- 修改文件内容，结合nl配合在文件的具体位置修改
- 详细用法：https://www.cnblogs.com/ggjucheng/archive/2013/01/13/2856901.html
- sed -i '73c DEFINE_int32\(make_snapshot_threshold_offset, 0, \"config the offset to reach the threshold\"\);' flags.cc
- sed -i '73c string' filename
  - -i 必须要加，表示原文件要修改。不加的话，不修改原文件，只是临时修改
  - 73c 表示73行要被替换，后面跟替换字符串，注意转义字符
- sed -n 4,8p file #打印file中的4-8行
- sed -n 4p file #打印file中的第4行

- 注意！！！
- 如果要把shell变量写入文件中
- 必须用双引号！！！
- 不能用单引号！！！
  - 参考链接：https://blog.csdn.net/geekcome/article/details/17741393

```
sed -i "44c "--headers \) HDRS_IN=\"$2\"; shift 2 ;;"" config_brpc.sh
```

- mac 使用这个命令似乎有问题啊！！
  - sed: 1: "config_brpc.sh": command c expects \ followed by text
  - 目前不好解决

```
基础说明：https://linux.cn/article-11367-1.html
常见的 sed 替换字符串的语法。

    sed -i 's/Search_String/Replacement_String/g' Input_File

首先我们需要了解 sed 语法来做到这一点。请参阅有关的细节。

    sed：这是一个 Linux 命令。
    -i：这是 sed 命令的一个选项，它有什么作用？默认情况下，sed 打印结果到标准输出。当你使用 sed 添加这个选项时，那么它会在适当的位置修改文件。当你添加一个后缀（比如，-i.bak）时，就会创建原始文件的备份。
    s：字母 s 是一个替换命令。
    Search_String：搜索一个给定的字符串或正则表达式。
    Replacement_String：替换的字符串。
    g：全局替换标志。默认情况下，sed 命令替换每一行第一次出现的模式，它不会替换行中的其他的匹配结果。但是，提供了该替换标志时，所有匹配都将被替换。
    /：分界符。
    Input_File：要执行操作的文件名。


获取指定哪几行的日志
file=xxx

first=`cat -n $file | grep "xxx" | head -1 | awk {'print $1}'`
last=`cat -n $file | grep "xxx" | tail -1 | awk {'print $1}'`

sed -n  "$first,${last}p" $file > test.log 



替换所有文件中的www.bcak.com.cn为bcak.com.cn
sed -i "s/www.bcak.com.cn/bcak.com.cn/g" `grep www.bcak.com.cn -rl /home`

old="import static org/.apache/.calcite/.supersql/.util/.func/.SuperSqlFuncUtil/.defineFunction;"
new="import static supersql/.utils/.UdfTools/.defineFunction;"
sed -i "s/$old/$new" `grep -rl $old .`


替换 20210922 字符串为 20210923
old="idex.date 20210922"
new="idex.date 20210923"
sed -i "s/$old/$new/g" select-spark.conf

打印哪些文件存在old字符串
grep -rl $old .
```



### gsed

```
mac上只能用gsed，不能用sed

安装命令
brew install gnu-sed
```



### nl

- 计算文件的行号
- 详细用法：http://www.cnblogs.com/peida/archive/2012/11/01/2749048.html

### mkdir -p build

- 如果存在不会返回错误。没有-p就会返回

### dirname

-  只是显示返回当前目录
- dirname /usr/bin/sort 
- 返回结果：/usr/bin
- 参考资料：https://blog.csdn.net/xiaofei125145/article/details/50620281

### cmake ..

- 编译上级目录的makefile

### cp

- 复制文件操作
  - cp source_name dest_name
- 复制目录
  - cp -r dir_name_source/.  dir_name_dest/ 只复制dir_name_source里面的子目录
  - cp -r dir_name_source  dir_name_dest 这样会把dir_name_source也复制进去

### scp

```
scp xxx.tar root@xxx:/mnt/disk02/xxx


scp文件夹
scp -P xxx端口号 -r xxxx  root@xxx:xxx
```

### rsync 文件夹增量更新

```
https://www.jianshu.com/p/07b3998e1f53

文件夹增量更新 已经有的文件，不会复制
rsync -avzh src dst
```



### mv

- 修改文件夹名字
- mv source_name dest_name

```
批量移动文件到一个文件夹
mv part-000* train_row
```



### Make -j8 rtidb

- 8个进程编译文件，并且最终可执行文件是名字叫rtidb

### ps命令详细说明以及目录说明

- stat：状态栏
  - 状态表：https://nigelzeng.iteye.com/blog/1186913
  - D    不可中断     Uninterruptible sleep (usually IO)  
  - R    正在运行，或在队列中的进程  
  - S    处于休眠状态  
  - T    停止或被追踪  
  - Z    僵尸进程  
  - W    进入内存交换（从内核2.6开始无效）  
  - X    死掉的进程    
  - <    高优先级  
  - N    低优先级  
  - L    有些页被锁进内存  
  - s    包含子进程  
  - \+    位于后台的进程组；  
  - l    多线程，克隆线程  multi-threaded (using CLONE_THREAD, like NPTL pthreads do) 
- Tty：设备连接
  - 连接电脑终端某个设备：https://stackoverflow.com/questions/7113770/what-does-tty-mean-in-the-unix-ps-command

```
目录
UID   PID  PPID   C STIME   TTY           TIME CMD




ps aux 
显示进程和目录

ps -xf
显示所有用户下的进程

ps -cf
显示本人用户下的进程
```



### echo妙用

- 文件后追加一条消息

  - echo 'export JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141/bin/java'>>~/.bash_profile
- 覆盖文件写消息

  - echo 'export JAVA_HOME=/home/wangzixian/java/jdk1.8.0_141/bin/java'>~/.bash_profile
- 参考资料：http://blog.sina.com.cn/s/blog_605f5b4f010154mn.html

### md5sum

- md5sum filename
- 用来判断两个文件的md5值是否相同

### grep

- 根据关键词提取改行数据
- 如果字符串匹配包含空格，那么一定要用转义符 \：https://blog.csdn.net/qq_30038111/article/details/83447045

```
参数说明：http://c.biancheng.net/view/946.html

https://blog.csdn.net/stepbystepto/article/details/52951849
grep -v *.sh 筛选掉不包含.sh的文件


全局搜索文件夹所有文件的内容
grep "#\[1234\]" -R .

搜索以某个数字为开头的一行
grep "^500147" -R .


获取当前行的上下200行内容
grep -A 200 xxx



    -A 数字：列出符合条件的行，并列出后续的 n 行；
    -B 数字：列出符合条件的行，并列出前面的 n 行；
    -c：统计找到的符合条件的字符串的次数；
    -i：忽略大小写；
    -n：输出行号；
    -v：反向査找；
    --color=auto：搜索出的关键字用颜色显示；
    
grep -r xxx dir/
搜索某个目录下所有文件

ripgrep xxx
递归搜索所有文件的内容



递归某个字符串在所有文件出现的地方
https://blog.csdn.net/BabyFish13/article/details/79709028

 grep -rn "xxxxx"  dir
 
 
 --递归查找目录下含有该字符串的所有文件
grep -rn "data_chushou_pay_info"  /home/hadoop/nisj/automationDemand/
 
--查找当前目录下后缀名过滤的文件
grep -Rn "data_chushou_pay_info" *.py
 
--当前目录及设定子目录下的符合条件的文件
grep -Rn "data_chushou_pay_info" /home/hadoop/nisj/automationDemand/ *.py
 
--结合find命令过滤目录及文件名后缀
find /home/hadoop/nisj/automationDemand/ -type f -name '*.py'|xargs grep -n 'data_chushou_pay_info'


-r 是递归查找
-n 是显示行号
-R 查找所有文件包含子目录
-i 忽略大小写 


有意思的命令行参数：
grep -i pattern files ：不区分大小写地搜索。默认情况区分大小写
grep -l pattern files ：只列出匹配的文件名,不列出路径
grep -L pattern files ：列出不匹配的文件名
grep -w pattern files ：只匹配整个单词，而不是字符串的一部分（如匹配‘magic’，而不是‘magical’）
grep -C number pattern files ：匹配的上下文分别显示[number]行
grep pattern1 | pattern2 files ：显示匹配 pattern1 或 pattern2 的行
grep pattern1 files | grep pattern2 ：显示既匹配 pattern1 又匹配 pattern2 的行 

```

### gunzip 解压gz文件

```
文件夹下所有文件批量解压
cd data && gunzip *.gz


unrar -x xxxxx.rar 
需要安装rar软件 brew install carlocab/personal/unrar
```



### find

- find ./ -iname rtidb_mon.log
  - 只显示结果必须加 -iname
  - 这是从当前开始查询
- find /. -iname 营销*
  - 从根目录开始查询
- find ../ -iname 营销*
  - 从上一个目录开始查询

```
找出某个文件的全路径
find  $PWD | xargs ls -ld | grep lz4

```



### wc

- 基本用法：http://www.cnblogs.com/peida/archive/2012/12/18/2822758.html
- wc -l filename 统计行数
- wc -c filename 统计字节数
- wc -w filenmae 统计字数

```
统计当前文件夹下所有文件的行数
wc -l `find . -name '*'`

打印每个文件的行数
wc -l `find . -name '*'` | awk '{print $1}'
 
求和
wc -l `find . -name '*'` | awk '{sum+=$1} END {print "Sum = ", sum}'
```



### hostname

- hostname -i显示ip
- hostname -f显示域名
- hostname -s显示主机名字
- 参考链接：https://codingstandards.iteye.com/blog/804648

### crontab
```
参考资料：https://www.cnblogs.com/0201zcr/p/4739207.html
demo参考：http://einverne.github.io/post/2017/03/crontab-schedule-task.html
执行脚本出现Permission denied：https://stackoverflow.com/questions/21646551/permission-denied-with-bash-sh-to-run-cron

查看当前用户的时程表
crontab -l

开始编辑定时任务
crontab -e

每分钟执行一次我的命令
* * * * * myCommand

```
### date

- 参考资料
  - https://blog.csdn.net/classhao1/article/details/8182733
  - https://blog.csdn.net/runming918/article/details/7384828
- date +%y-%m-%d
  - 打印年月日
- 标准格式
  -  date "+%Y-%m-%d %H:%M:%S" 
- 日期转换成时间戳
  - date -d "2019-01-16 17:17:43" +%s
- 时间戳转换成日期
  - date -d @1547630387"+%Y-%m-%d %H:%M:%S"

```
打印时间戳
date +%s

shell复制时间戳
xx=`date +%s`
```

### tee

- <https://linux.cn/article-9435-1.html>

```
输出的信息也同时能写入文件
ping google.com | tee output.txt

确保 tee 命令追加信息到文件中
[command] | tee -a [file]

让 tee 写入多个文件
[command] | tee [file1] [file2] [file3]

让 tee 命令的输出内容直接作为另一个命令的输入内容
ls file* | tee output.txt | wc -l

使用 tee 命令提升文件写入权限
:w !sudo tee %
```

### time

```
统计命令执行性能

time [command]
```

### ab 服务器压力测试

```
ab -v 10 -c 1 -n 1 -p xxxx -T xxxxx
```

### perf性能测试

```
perf 适合linux下检查程序性能
https://zhuanlan.zhihu.com/p/22194920

# 安装
yum install perf
   
# 分析程序调用函数占用比例
perf record ./my_app my_args
perf report
     
# 分析程序调用函数占用比例，包含函数调用关系
perf record --call-graph dwarf ./my_app my_args
perf report
  
# 实时追踪当前整个系统函数占用
perf top
  
# 实时追踪指定进程函数占用
perf top -p PID

容器里使用方式：
# 若宿主机没有开放profile权限
echo -1 > /proc/sys/kernel/perf_event_paranoid
  
# 容器run时候需要加上--privileged
docker run --privileged   ...
```

### 性能优化

```
intel vtune或者emon
```



### tail

- 从第5行开始显示文件
  - tail -n +5 log2014.log
- 显示后5行
  - tail -n 5 log2014.log
- 持续更新文件内容
  - **tail -f test.log**

### tar  zip

- <https://www.jb51.net/LINUXjishu/43356.html>

```
解压llvm压缩包
tar -xvf llvm-8.0.0.src.tar.xz

解压tar结尾的压缩包
tar -xf all.tar

解压gz结尾的压缩包
tar -zxvf ×××.tar.gz

将所有.jpg的文件打成一个名为all.tar的包。-c是表示产生新的包 ，-f指定包的文件名
tar -cf all.tar *.jpg


将所有.gif的文件增加到all.tar的包里面去。-r是表示增加文件的意思。
tar -rf all.tar *.gif

压缩一个tar备份文件，此时压缩文件的扩展名为.tar.gz
tar 只是整理文件在一个压缩包，并没有真正的压缩
gzip -r log.tar

https://man.linuxde.net/gzip
递归压缩文件夹的文件
gzip -rv test6

递归地解压目录
gzip -dr test6


zip方式压缩，一般window需要这个格式
将 /home/html/ 这个目录下所有文件和文件夹打包为当前目录下的 html.zip：

zip -q -r html.zip /home/html

如果在我们在 /home/html 目录下，可以执行以下命令：

zip -q -r html.zip *

从压缩文件 cp.zip 中删除文件 a.c

zip -dv cp.zip a.c

unzip 解压
unzip xx.zip


unrar -x xxxxx.rar 需要安装rar软件 brew install carlocab/personal/unrar

查看压缩文件中包含的文件
# unzip -l abc.zip 
Archive: abc.zip
 Length   Date  Time  Name
--------  ----  ----  ----
  94618 05-21-10 20:44  a11.jpg
  202001 05-21-10 20:44  a22.jpg
    16 05-22-10 15:01  11.txt
  46468 05-23-10 10:30  w456.JPG
  140085 03-14-10 21:49  my.asp
--------          -------
  483188          5 files

-v 参数用于查看压缩文件目录信息，但是不解压该文件。
# unzip -v abc.zip 
Archive: abc.zip
Length  Method  Size Ratio  Date  Time  CRC-32  Name
-------- ------ ------- -----  ----  ----  ------  ----
  94618 Defl:N  93353  1% 05-21-10 20:44 9e661437 a11.jpg
 202001 Defl:N  201833  0% 05-21-10 20:44 1da462eb a22.jpg
   16 Stored    16  0% 05-22-10 15:01 ae8a9910 ? +-|￥+-? (11).txt
  46468 Defl:N  39997 14% 05-23-10 10:30 962861f2 w456.JPG
 140085 Defl:N  36765 74% 03-14-10 21:49 836fcc3f my.asp
--------     ------- ---              -------
 483188      371964 23%              5 files
```



### which

- http://www.runoob.com/linux/linux-comm-which.html
- which指令会在环境变量$PATH设置的目录里查找符合条件的文件



### patch

- <https://www.runoob.com/linux/linux-comm-patch.html>
- 命令用于修补文件

### awk and 

```
根据每一行分号分割
awk -F ':' '{ print $1 }' demo.txt


根据  | 分割字符串
awk -F '|' '{ print $1 }'

拼接字符串
cat exception_log | awk -F ":" '{print "cp /data/idex/history/20220114/"$1" /data/idex/ngcp/."}'
cp /data/idex/history/20220114/18d362c8-fbca-46d8-9249-2fb7f70590a6.log /data/idex/ngcp/.

```

### chmod chown

```
chmod -R 777 文件名

修改用户号
chown 1003 ./ -R


修改用户名和用户组
chown [-R] xx:xxx filename
chown hdfs:hadoop log.txt

修改路径权限
sudo chown -R $(whoami) /usr/local/share/man/man8
```

### chage 
```
chage -M 99999 idex

设置的密码永久生效

```


## 进程管理

### 查看端口占用情况-更通用

```
netstat -ano | grep 8888
```

### 通过进程号，查看进程所在目录位置
```
pwdx 10769
```


### 通过端口查看进程pid

- netstat -an | grep port
- netstat -anp | grep port
- 一般p的参数有权限限制，有了p那么才会显示pid数字
- 参考资料：http://www.cnblogs.com/MacoLee/p/5664306.html

### 进程无法被kill
```

https://blog.csdn.net/u010416101/article/details/72331799



Reference
今天安装集群的时候，发现一个进程一直存在，kill -9 pid 也干不掉，就找找原因了。

kill -9发送SIGKILL信号将其终止，但是以下两种情况不起作用：

a、该进程处于”Zombie”状态（使用ps命令返回defunct的进程）。此时进程已经释放所有资源，但还未得到其父进程的确认。”zombie”进程要等到下次重启时才会消失，但它的存在不会影响系统性能。

b、 该进程处于”kernel mode”（核心态）且在等待不可获得的资源。处于核心态的进程忽略所有信号处理，因此对于这些一直处于核心态的进程只能通过重启系统实现。进程在AIX 中会处于两种状态，即用户态和核心态。只有处于用户态的进程才可以用“kill”命令将其终止。

用top命令查看发现zombie进程数是0，看来这三个进程不属于僵尸进程，应该是b这中情况，就是这些进程进入核心态等待磁盘资源时出现磁盘空间不足的故障，这时我强制关闭了数据库，所以这几个进程就一直处于核心态无法被杀除，看来只能重启了。
————————————————
版权声明：本文为CSDN博主「在风中的意志」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010416101/article/details/72331799



```


### 进程pid内存使用情况

```
https://www.cnblogs.com/sky-heaven/p/7654966.html

Linux中查看某个进程占用内存的情况，执行如下命令即可，将其中的[pid]替换成相应进程的PID号：

cat /proc/[pid]/status

回到顶部
说明

/proc/[pid]/status中所保存的信息除了内存信息，还包括进程IDs、信号等信息，此处暂时只介绍内存相关的信息。
字段	说明
VmPeak 	进程所使用的虚拟内存的峰值
VmSize 	进程当前使用的虚拟内存的大小
VmLck 	已经锁住的物理内存的大小（锁住的物理内存不能交换到硬盘）
VmHWM 	进程所使用的物理内存的峰值
VmRSS 	进程当前使用的物理内存的大小
VmData 	进程占用的数据段大小
VmStk 	进程占用的栈大小
VmExe 	进程占用的代码段大小（不包括库）
VmLib 	进程所加载的动态库所占用的内存大小（可能与其它进程共享）
VmPTE 	进程占用的页表大小（交换表项数量）
VmSwap 	进程所使用的交换区的大小

cat /proc/1161/status
```

### 批量删除进程

```
wangzixian/software/idea




ps -xf | grep wangzixian/software/idea | awk '{print $1}' | while read line; do kill -9 $line; done

```



### 命令结果保存在变量中

- 参考链接
  - https://blog.csdn.net/qq_29603999/article/details/78245736
  - https://blog.csdn.net/zwt0909/article/details/52813388
- `` 或者 $(xxx)
- rows=$(wc -l $monitor_file | awk '{print $1}')
- 但是结果默认是没有换行符，也就是结果会拼凑成一行
- 要想保证原来的格式需要加双引号：https://blog.csdn.net/CaspianSea/article/details/51228944
- "${string}"

### 字符串基本操作

- 参考资料：https://www.cnblogs.com/chengmo/archive/2010/10/02/1841355.html
- 查找
- 长度
- 赋值
- 删除

### 字符串拼接

- 直接拼凑即可
- var3={var1}{var2}

### 判断空字符串

- 字符串比较：https://blog.csdn.net/yf210yf/article/details/9207147

### 统计字符串里面有多少行

- count=$(echo "$result" | wc -l)

### 循环一行一行的打印字符串

- IFS=$'\n'
  for line in `echo "$string"`
- 逐行处理文本：https://www.cnblogs.com/dwdxdy/archive/2012/07/25/2608816.html

### 大小比较

- 参考资料：https://blog.csdn.net/jack_zyk/article/details/7325787
- if [ 1 -gt 2 ]
- -gt表示大于
  -lt表示小于
  -eq表示等于
  -ne表示不等于
  -ge表示大于等于
  -le表示小于等于

### 发邮件

- echo CONTEXT | mail -s TITLE RECEIVER
- 前提是from邮件已经配置完成，才能直接使用

### 统计文件行数

- wc -l filename
- wc -c filename 统计字节数
- wc -w filenmae 统计字数

### 统计当前目录下多少文件

```
ls -lR  | grep "^-" | wc -l
```



### 定义二维数组

- LOG_FILES=('nameserver.info.log,offline tablet with endpoint,Run OfflineEndpoint,Run RecoverEndpoint,reconnect zk,kFailed,time of op is too long'

  ​           'rtidb_mon.log,mon : kill,mon : exit'

  ​           'rtidb_ns_mon.log,mon : kill,mon : exit'

  ​           'tablet.info.log,reconnect zk')

- 括号里面是一维数组，里面包含的字符串，字符串可以选择分隔符

- 这里我使用逗号作为分割

- 间接使用二维数组吧

### 查看文件的第几行到第几行的内容

- sed -n '2363,2373p' src/cmd/rtidb.cc

### 自定义for循环切割符号

- SAVEIFS=$IFS

  IFS=$(echo -en ",")

  for element in $file

  do

  xxxxxxx

  done

  IFS=$SAVEIFS

- IFS=$(echo -en ",")  这一块可以修改分隔符。我使用的的是逗号

- 如果要空格的话改成\n\b

- 空行：\n

- 参考链接

  - https://www.cyberciti.biz/tips/handling-filenames-with-spaces-in-bash.html
  - https://blog.csdn.net/gg_18826075157/article/details/78077602

### shell数字自增

- https://www.cnblogs.com/iloveyoucc/archive/2012/07/11/2585559.html
- i =`expr $i + 1`;

### 打印结果的某一列

- 第一列：awk '{print $1}'
- rows=$(wc -l  $monitor_file | awk '{print $1}')

### 邮件的位置

- /var/spool/mail

### 网络请求

```
export proxy="http://192.168.5.14:8118"
export http_proxy=$proxy
export https_proxy=$proxy
export ftp_proxy=$proxy
export no_proxy="localhost, 127.0.0.1, ::1"

https://www.cnblogs.com/EasonJim/p/9826681.html
```



## 文件

### 统计大文件
```
sudo find /docker -type f -size +100M -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
```
### 统计大文件夹
```
sudo du -h /docker | grep '^[0-9\.]\+G' | sort -hr
```

### 对比两个文件内容

```
vimdiff 文件路径1 文件路径2
```

### 对比两个文件夹内容
```
diff -Naur <dir1> <dir2>

```
### 获取百万级别文件列表
```
获取文件列表大小
find `pwd` | xargs ls -lah 

find `pwd` | xargs ls -lah | awk '{print $5}' > ../txt

```


### 修改文件权限

```
chmod 数字 文件名 

chmod 777 xxx //  满权限
```

### chown 修改用户对某个文件的权限

```
chown 1003 xxx.java

1003 是用户id号
命令 id 就可以看到自己在服务器上的id号了
```



### 选取文件 某一行或指定范围

- sed -n 4,8p file #打印file中的4-8行
- sed -n 4p file #打印file中的第4行

### 替换文件的某一行内容

- sed -i '73c string' filename

```
sed -i '12c dataDir=ut_zookeeper' conf/zoo.cfg  写入dataDir=ut_zookeeper，没有双引号的
sed -i '12c "dataDir=ut_zookeeper"' conf/zoo.cfg 写入"dataDir=ut_zookeeper"，包含了双引号
下面是复杂的
sed -i "44c \"--headers ) HDRS_IN=\"\$2\"; shift 2 ;;\"" config_brpc.sh

sed -i '45c "--libs ) LIBS_IN="\$2"; shift 2 ;;"' config_brpc.sh
```

### 往文件结尾写入字符串

```
echo "xxx.27.128.37\ xx-xx" > /etc/hosts

特殊字符要加斜杆
```

### 找出某个文件的全路径

```
包含文件详细信息
find  $PWD | xargs ls -ld | grep lz4

纯文件路径
find  $PWD | grep target | grep .jar
```



### 文件文本处理大全

```
awk
https://www.runoob.com/linux/linux-comm-awk.html
高级用法：https://www.jianshu.com/p/2b101d072b7a

awk '{print $1,$2,$3,$4,$5,$6}' log
1066646 231846592837463974 3827260221581409832 2012-07-15 05:17:46.766
1302399 4260542096088094334 12371595234560663038 2014-12-10 03:46:53.732
打印log文件中的前6列

awk '{printf "%s,%s,%s,%s %s,%s\n", $1,$2,$3,$4,$5,$6}' log
1066646,231846592837463974,3827260221581409832,2012-07-15 05:17:46.766,1
1302399,4260542096088094334,12371595234560663038,2014-12-10 03:46:53.732,2
格式化输出，逗号隔开

1、打印文件的第一列(域)                 ： awk '{print $1}' filename
2、打印文件的前两列(域)                 ： awk '{print $1,$2}' filename
3、打印完第一列，然后打印第二列  ： awk '{print $1 $2}' filename
4、打印文本文件的总行数                ： awk 'END{print NR}' filename
5、打印文本第一行                          ：awk 'NR==1{print}' filename
6、打印文本第二行第一列                ：sed -n "2, 1p" filename | awk 'print $1'


输出某个路径下的所有文件夹，而没有文件
ls -l /usr/ | awk '/^d/ {print $NF}'


https://mp.weixin.qq.com/s/B9rSVxOgO0WipzzZvxfbKg
从第一行可以看到这个数据集包含6列：id  qid1    qid2    question1   question2   is_duplicate
但实际上我们单纯训练一个q-q文本匹配模型的话，只需要最后三列就够了。不懂linux的小伙伴可能会用python打开文件，然后一顿for循环和str.split了。
但实际上，用上cut之后配合管道只需要一行
cat train.tsv | cut -f 4,5,6 > train.tsv.cut


就把数据集的第4，5，6列提出来了，并且存储在了train.tsv.cut文件中。如果需要的数据来自于两个文件，可以分别cut出来再将这些列拼到一起（新文件是m+n列，可以理解成cat是纵向连接两个或若干个文件，而paste则是横向连接）
paste file1.txt file2.txt


最后，训练数据的去重和shuffle，也完全可以不用python去写，分别用uniq和shuf结合管道就能一行命令搞定
sort train.tsv.cut | uniq | shuf > train.tsv


单机并行数据预处理
for i in {0..99};
do
    python process.py train.tsv.part$i > train.tsv.part$i.tmp &
done
wait  // 会等待所有命令执行完

批量杀死包含某个名字的进程
pkill -f <xxx>
pkill -f 'process.py'





```

### 批量移动文件夹

```
mv part-000* train_row
```



### 当前目录按照文件大小排序

```
https://blog.csdn.net/sqiucheng/article/details/54093638

du -sh ./* |  sort -rn
```



### 给每个文件尾部加空行

```
单独文件加空行
echo -e "\n" >> sparta.yaml


所有文件加空行
for file in `ls`
do
    echo $file
    echo "\n" >> $file
#  mv $file `echo $file|sed 's/\(.*\)\(\..*\)/\1_aaa\2/g'`
done

```



### shell函数使用

- 参考资料
  - 函数基本操作http://www.runoob.com/linux/linux-shell-func.html
  - 返回字符串方法：https://blog.csdn.net/zycamym/article/details/45191093
  - 参数使用技巧：
- 函数返回
  - 只能返回正整数，不能返回字符串
  - 除非用echo间接获取
- 函数参数
  - 函数外部就和vi grep一样直接写入参数
  - 函数内部调用的时候用$1,2,3,4这样的序号来表示外部传入的参数

```
# 参考例子
messageControl(){
    current_date=$(echo `date "+%Y-%m-%d %H:%M:%S"`)
    log_date=$(echo `sed -n 1p $CONTEXT_FILE`)
    # echo $current_date
    # echo $log_date
    current_date=$(echo `date -d "$current_date" +%s`)
    log_date=$(echo `date -d "$log_date" +%s`)
    diff=$(expr $current_date - $log_date)
    # echo " "
    echo $diff
    if [ $diff -gt $MAX_DIFF ]; then
        return 1
    else
        return 2
    fi
}
messageControl
result=$?
echo $result


#参数例子
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

### 查找某个进程的pid并杀死它

```
ps -xf | grep xxx_name
kill -9 xx
```

### 查找某个进程的执行路径

```
cd /proc/pid号
// 就会显示文件夹目录
ls -ail
```



### 结束当前进程而不是停止当前进程

- ctrl + c

### 下载网络压缩包

```
curl -I url
或者
wget url
```



### 解压和压缩

```
https://jingyan.baidu.com/article/6d704a13f9981a28da51ca70.html
解压
tar -zxvf xxx.tar.gz
tar -zxvf xxx.tar
unzip xx.zip
压缩
tar czvf xxx.tar xxx



解压rpm包
rpm2cpio mysql-connector-java-8.0.24-1.fc33.src.rpm | cpio -div


解压报错：https://www.cnblogs.com/xqzt/p/5032865.html
gzip: stdin: not in gzip format 
tar: Child returned status 1 
tar: Error is not recoverable: exiting now

解决办法：
1.首先用 file 命令查看该文件的真实属性
[sa@cistest local]$ file rlwrap-0.30.tar.gz
rlwrap-0.30.tar.gz: tar archive
2.根据真实属性选择解压命令即可解决
[sa@cistest local]$ tar xvf rlwrap-0.30.tar.gz



```

### 环境变量和export的用法

- 参考资料：<https://www.runoob.com/linux/linux-comm-export.html>

```
可以在.bash_profile
用export声明变量和变量的值

在linux中
export -p 列举所有环境变量
export -n xxx 删除某个环境变量值
```

### 查看服务器默认编解码

```
locale


LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=en_US.UTF-8
```



### 查看服务器的ip地址

```
ifconig -a
```

### 添加域名映射

```
vi /etc/host

xxx.xxx.xxx.xxx  域名名字
```

### 杀死占用某个端口号的进程netstat

```
netstat -tunlp|grep 7600
kill -9 xxx
```



### 查看执行程序是否依赖动态库

```
ldd 执行程序名字
```

### 程序的前台后台切换

```
https://www.cnblogs.com/wangbin/archive/2009/05/07/1451502.html
Linux 技巧：bg和fg让程序在前台后台之间切换

让程序在前台后台之间切换。 Linux 提供了 fg 和 bg 命令，让你轻松调度正在运行的任务。
假设你发现前台运行的一个程序需要很长的时间，但是需要干其他的事情，你就可以用 Ctrl-Z ，挂起这个程序，然后可以看到系统提示：
[1]+ Stopped /root/bin/rsync.sh
然后我们可以把程序调度到后台执行：（bg 后面的数字为作业号）
#bg 1
[1]+ /root/bin/rsync.sh &

用 jobs 命令查看正在运行的任务：
#jobs
[1]+ Running /root/bin/rsync.sh &


如果想把它调回到前台运行，可以用
#fg 1
/root/bin/rsync.sh
这样，你在控制台上就只能等待这个任务完成了。
aliyun活动 https://www.aliyun.com/acts/limit-buy?userCode=re2o7acl
```

### 如何让程序在后台执行

```
tmux
可以让里面执行的命令一直在后台运行，不会中断

已经在前台的情况下
也可以ctrl + z 先停止进程
jobs 查看停止的进程号
bg 进程号 即可继续执行程序
fg %jobnumber（是命令编号，不是进程号）将选中的命令调出。
kill %1 1是jobs号，前面一定要是%


nohup命令
nohup python -m HTTPServer 8567 >log 2>&1 &

watch  -n 10 sh  test.sh  &  #每10s在后台执行一次test.sh脚本

```

### 用pid方式，让进城停止，继续运行

```
https://www.cnblogs.com/mfryf/archive/2012/09/24/2700042.html

16079 就是进程号

kill -STOP 16079
kill -CONT 16079
```



### 快速性能测试

```
time xxxx

xxx 可以使执行脚本也可以是执行程序

结果
real	0m10.135s
user	1m10.289s
sys	0m4.383s
```

### 日志输入指定文件

```
time sh run.sh > log 2>&1 &
tail -200f log

time 可以有也可以不要，因为它是用统计脚本运行的时间


更好的方法tee命令，可以查看更详细的tee说明哦
sh run.sh | tee log
同时也可以在输入流显示出来
```

### 打印日历

```
打印月
cal

打印年
cal -y
```

### 安装gcc

```
yum install gcc
yum install gcc-c++ libstdc++-devel

```

## 系统排查

```
查看磁盘空间 df -h
可视化看板磁盘工具：Baobab是一款分析磁盘使用情况的图形工具，它可以分析本地硬盘空间、分析挂载硬盘或设备空间，同时界面简单易操作，且分析结果以环状或树形状显示。
https://wiki.deepin.org/wiki/Baobab


du -sh 查看当前目录所占空间

du -ah --max-depth=1

du -sh : 查看当前目录总共占的容量。而不单独列出各子项占用的容量 

du -lh --max-depth=1 : 查看当前目录下一级子文件和子目录占用的磁盘容量
```

## 正则表达式

```
https://jingyan.baidu.com/article/eb9f7b6d452768869364e805.html
srt文件字幕提取中文
\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+[\r|\n]{1,2}([\w\W]*?)[\r|\n]{1,2}

全选字幕
\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+[\r|\n]{1,2}([\w\W]*?)[\r|\n]{2}

\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+[\r|\n]{1,2}[\w\W]*?[\r|\n]{1,2}([\w\W]*?)[\r|\n]{1,2}
```



## 常识

### redhat

```
redhat 就是 centos
用yum安装软件
```

### Linux的配置-bashrc 与 bash_profiler

```
https://stackoverflow.com/questions/415403/whats-the-difference-between-bashrc-bash-profile-and-environment
执行man bash可以看到每个bash文件的意义和作用

That's simple. It's explained in man bash:

/bin/bash
       The bash executable
/etc/profile
       The systemwide initialization file, executed for login shells
~/.bash_profile
       The personal initialization file, executed for login shells
~/.bashrc
       The individual per-interactive-shell startup file
~/.bash_logout
       The individual login shell cleanup file, executed when a login shell exits
~/.inputrc
       Individual readline initialization file
  
https://blog.csdn.net/xyqzki/article/details/41832875
简单来说
bashrc: 为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取（即每次新开一个终端，都会执行bashrc）
 ~/.bash_profile: 每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该文件仅仅执行一次。默认情况下,设置一些环境变量,执行用户的.bashrc文件。
 
 如果希望某个配置，长期有效，一开终端就能配置好，就选择bashrc
 
 注意，无论是什么配置，都要考虑到环境干净性！
```

### gcc的历史版本

```
gcc version >=5: gcc uses the new C++ ABI since version 

gcc4 that uses the older ABI.

If you compile your library with gcc>=5, add -D_GLIBCXX_USE_CXX11_ABI=0 to the command line to make the library compatible with the older abi.
```

### 多个shell执行顺序

```
直接在主shell脚本中执行一个子shell脚本，主shell是不会等待子shell结果，如果需要串行执行，可以用wait命令
https://linuxhint.com/wait_command_linux/
sh xxx | wait

```

### 后台模式

```
所有命令 后面可以加个  & 说明是放在后台执行
ls -l &
xxx &
```

### 颜色高亮配置

```
https://www.jianshu.com/p/4239d3ea72fe

PS1的常用参数以及含义:
　　\d ：代表日期，格式为weekday month date，例如："Mon Aug 1"
　　\H ：完整的主机名称
　　\h ：仅取主机名中的第一个名字
　　\t ：显示时间为24小时格式，如：HH：MM：SS
　　\T ：显示时间为12小时格式
　　\A ：显示时间为24小时格式：HH：MM
　　\u ：当前用户的账号名称
　　\v ：BASH的版本信息
　　\w ：完整的工作目录名称
　　\W ：利用basename取得工作目录名称，只显示最后一个目录名
　　# ：下达的第几个命令
　　$ ：提示字符，如果是root用户，提示符为 # ，普通用户则为 $





# 颜色设置
black=$'\[\e[1;30m\]'
red=$'\[\e[1;31m\]'
green=$'\[\e[1;32m\]'
yellow=$'\[\e[1;33m\]'
blue=$'\[\e[1;34m\]'
magenta=$'\[\e[1;35m\]'
cyan=$'\[\e[1;36m\]'
white=$'\[\e[1;37m\]'
normal=$'\[\e[m\]'


export LS_COLORS='no=00:fi=00:di=01;33:ln=01;36:pi=40;33:so=01;35:bd=40;33;01:cd=40;33;01:or=01;05;37;41:mi=01;05;37;41:ex=01;35:*.cmd=01;35:*.exe=01;35:*.com=01;35:*.btm=01;35:*.bat=01;35:*.sh=01;35:*.csh=01;35:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.gz=01;31:*.bz2=01;31:*.bz=01;31:*.tz=01;31:*.rpm=01;31:*.cpio=01;31:*.jpg=01;35:*.gif=01;35:*.bmp=01;35:*.xbm=01;35:*.xpm=01;35:*.png=01;35:*.tif=01;35:'

# export LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:'

黄色
export PS1='[\[\e[1;33m\]\u@\h \w \t]$ '


青色
export PS1='[\[\e[1;36m\]\u@\h \w \t]$ '


前面显示青色 后面显示黄色 色彩更加鲜明
export PS1='\[\e[1;36m\][\u@\h \w \t]$ \[\e[1;33m\]'


export PS1='\[\e[1;36m\][\u@\h \w \t]$ \[\e[1;33m\]'

export PS1='[\u@\h \w \t]'


PS1="[\e[37;1m][[\e[31;1m]\u [\e[36;1m]@ [\e[33;1m]\h [\e[35;40m]\W[\e[37;1m]] [\e[33;1m]\$[\e[0m] "


```

### 正则表达式

```
删除多余空行
^\s*(?=\r?$)\n

\s


\[Loaded.*


删除多余空格

^\s*

^\s+


```


### 定时任务cron
```

crontab -e 

* * * * * /usr/local/sa/agent/secu-tcs-agent-mon-safe.sh  > /dev/null 2>&1

* * * * * /root/wangzixian/cloud/script_tools/docker_stats.sh > /root/wangzixian/temp/docker_stats.log


* * * * * sh /root/wangzixian/my-tools/crontab_echo.sh  > /root/wangzixian/my-tools/crontab_echo.log
* * * * * sh /root/wangzixian/my-tools/docker_stats.sh  > /root/wangzixian/my-tools/docker_stats.log

* * * * * sh /data/idex/idex-tools/docker_stats.sh /data/idex/idex-tools/docker_stats.log
```

### 快速集成classpath-跑java
```

CLASSPATH=/usr/local/services/hybris-realview-1.0/log/temp/log4j.xml
JAVABIN=/usr/bin/java
ROOT=/usr/local/services/hybris-realview-1.0/lib

for f in $ROOT/*.jar; do \
  CLASSPATH=${CLASSPATH}:$f; \
done 

HIVE=/usr/local/services/hybris-realview-1.0/hive235
for f in $HIVE/*.jar; do \
  CLASSPATH=${CLASSPATH}:$f; \
done 


echo $CLASSPATH

$JAVABIN \
-Xms32m \
-Xmx128m \
-XX:+HeapDumpOnOutOfMemoryError \
-XX:HeapDumpPath=$ROOT/tmp \
-Dlogback.configurationFile=file:/usr/local/services/hybris-realview-1.0/log/temp/log4j2.xml \
-Dlog4j.configurationFile=file:/usr/local/services/hybris-realview-1.0/log/temp/log4j2.xml \
-DtaskType=126 \
-DtaskId_mould=98 \
-DtaskId=20220630012603998 \
-DcurRunDate=20220630190700 \
-Dtries=0 \
-DrunnerStateCode=9 \
-Dlhotse_taskState=key__state___9 \
-Djar.name=hybris-crawler-wedataUS-2.0.0-wedata-SNAPSHOT.jar \
-Dfile.encoding=UTF-8 \
-Dinstance_info=20220630012603998_20220630190700 \
-cp $CLASSPATH \
com.tencent.hybris.engine.crawler.hive.HbaseCrawlerTest

```

### 统计子文件夹磁盘占用并排序
```
➜  project du -h --max-depth=1 | sort -rh            
20G     .
8.4G    ./2023大模型知识库
6.4G    ./2023IKCEST
3.3G    ./chatglm
1.1G    ./doc_query
263M    ./lab
153M    ./speech_en
75M     ./runjava
42M     ./run_last
3.1M    ./2023数学建模C题

```

### 文件查找常用命令
```

关键词搜索
find . -maxdepth 2 -type d -name "confu-deps"

```

## HDFS
### 递归打印文件路径
```
hdfs dfs -ls -R viewfs://hadoop-meituan/user/hadoop-search > search_paths.txt


```

### 修改配置如何系统级生效，比如开启代理
```

注意拷贝源文件

代理配置复制到 /ect/profile 文件中
执行
source /ect/profile

系统级别生效


```


## 问题

### [: too many arguments

- 因为传递的字符串含有空格，所以出现这个问题
- 一开始比较难找到底哪里多了空格
- 所以后面直接加双引号保证整个字符串传进去
- 解决方案：https://stackoverflow.com/questions/13781216/meaning-of-too-many-arguments-error-from-if-square-brackets
- "$VARIABLE"

### 用ssh登录服务器

```
ssh-keygen -t rsa
s生成公钥和秘钥，公钥是可以随意发布的，秘钥只能你一个人持有


密钥写入到服务端
ssh-copy-id  root@xxxxxxx

```

### tar解压报错常见原因

```
https://blog.csdn.net/canglan211/article/details/84530216
账号权限不足造成的，使用sudo执行则解决
压缩包损坏
磁盘空间不足，可以df /home -h查看/home是否已满

空间不够用，该删除一些文件
du -sh /    // 统计根目录的系统空间大小
du -sh 目录名  // 统计某个目录空间大小
```

###  WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable

```
https://stackoverflow.com/questions/19943766/hadoop-unable-to-load-native-hadoop-library-for-your-platform-warning


```

### execvp: /bin/bash: Argument list too long

```
减少编译文件，拆分开来
```



### find: paths must precede expression

```
https://www.cnblogs.com/peter1994/p/7297656.html

ind /tmp  -maxdepth 1 -mtime 30 -name *.pdf 

find: paths must precede expression
Usage: find [-H] [-L] [-P] [path...] [expression]

然后就上网查了一下,结果搜索到一篇,大概是这样说的:多文件的查找的时候需要增加单引号,一直是使用的双引号,没想到找多文件的时候居然要单引号.好吧,又学了一招,修改后:
```

### Binary file (standard input) matches

```
https://blog.csdn.net/lastsweetop/article/details/4290545
grep "key" xxx.log时输出

Binary file xxx.log matches

百度了一下：grep认为这是二进制文件，解决方案：grep -a。

grep -a "key" xxx.log
```

### 代码风格问题

```
<module name="ImportOrder">
      <property name="groups" value="org.apache.calcite,org.apache,au.com.,com.,io.,mondrian.,net.,org.,scala.,/^javax?\./"/>
      <property name="ordered" value="true"/>
      <property name="separated" value="true"/>
      <property name="option" value="bottom"/>
    </module>
    
   

Extra separation in import group before 'org.yaml.snakeyaml.error.YAMLException' [ImportOrder]



'com.tencent.supersql.common.utils.jdbc.JdbcDriver.getJdbcDriver' should be separated from previous imports. [ImportOrder]
Audit done.


Open parentheses exceed closes by 2 or more [HydromaticFileSet]
不能连续两个括号在同一行


Extra separation in import group before 'org.yaml.snakeyaml.error.YAMLException' [ImportOrder]

Wrong order for 'com.tencent.supersql.common.utils.jdbc.JdbcDriver' import. [ImportOrder]

'com.tencent.supersql.common.utils.jdbc.JdbcDriver.getJdbcDriver' should be separated from previous imports. [ImportOrder]
Audit done.

检查导入包的顺序/分组。确保导入包的分组按照指定的顺序排列（例如，java.排在首位，javax.排在第二，以此类推），并且每个分组内导入的包都是按照字典序排列的。静态导入必须放在最后，并且也是按照字典序排列的。

中文说明：https://www.jianshu.com/p/9d6a6815ea52



 Checks the ordering/grouping of imports. Features are:

    groups type/static imports: ensures that groups of imports come in a specific order (e.g., java. comes first, javax. comes second, then everything else)
    adds a separation between type import groups : ensures that a blank line sit between each group
    type/static import groups aren't separated internally: ensures that each group aren't separated internally by blank line or comment
    sorts type/static imports inside each group: ensures that imports within each group are in lexicographic order
    sorts according to case: ensures that the comparison between imports is case sensitive, in ASCII sort order
    arrange static imports: ensures the relative order between type imports and static imports (see ImportOrderOption)

    Property option - specify policy on the relative order between type imports and static imports. Type is com.puppycrawl.tools.checkstyle.checks.imports.ImportOrderOption. Default value is under.
    Property groups - specify list of type import groups (every group identified either by a common prefix string, or by a regular expression enclosed in forward slashes (e.g. /regexp/). All type imports, which does not match any group, falls into an additional group, located at the end. Thus, the empty list of type groups (the default value) means one group for all type imports. Type is java.lang.String[]. Validation type is java.util.regex.Pattern. Default value is "".
    Property ordered - control whether type imports within each group should be sorted. It doesn't affect sorting for static imports. Type is boolean. Default value is true.
    Property separated - control whether type import groups should be separated by, at least, one blank line or comment and aren't separated internally. It doesn't affect separations for static imports. Type is boolean. Default value is false.
    Property separatedStaticGroups - control whether static import groups should be separated by, at least, one blank line or comment and aren't separated internally. This property has effect only when the property option is set to top or bottom and when property staticGroups is enabled. Type is boolean. Default value is false.
    Property caseSensitive - control whether string comparison should be case sensitive or not. Case sensitive sorting is in ASCII sort order. It affects both type imports and static imports. Type is boolean. Default value is true.
    Property staticGroups - specify list of static import groups (every group identified either by a common prefix string, or by a regular expression enclosed in forward slashes (e.g. /regexp/). All static imports, which does not match any group, falls into an additional group, located at the end. Thus, the empty list of static groups (the default value) means one group for all static imports. This property has effect only when the property option is set to top or bottom. Type is java.lang.String[]. Validation type is java.util.regex.Pattern. Default value is "".
    Property sortStaticImportsAlphabetically - control whether static imports located at top or bottom are sorted within the group. Type is boolean. Default value is false.
    Property useContainerOrderingForStatic - control whether to use container ordering (Eclipse IDE term) for static imports or not. Type is boolean. Default value is false.
    Property tokens - tokens to check Type is java.lang.String[]. Validation type is tokenSet. Default value is: STATIC_IMPORT.

To configure the check:

 <module name="ImportOrder"/>
 

Example:

 import java.io.IOException;
 import java.net.URL;

 import java.io.IOException; // violation, extra separation before import
                             // and wrong order, comes before 'java.net.URL'.
 import javax.net.ssl.TrustManager; // violation, extra separation due to above comment
 import javax.swing.JComponent;
 import org.apache.http.conn.ClientConnectionManager; // OK
 import java.util.Set; // violation, wrong order, 'java' should not come after 'org' imports
 import com.neurologic.http.HttpClient; // violation, wrong order, 'com' imports comes at top
 import com.neurologic.http.impl.ApacheHttpClient; // OK




 (whitespace) WhitespaceAfter: ',' is not followed by whitespace.
 
 
 Kotlin: Incompatible classes were found in dependencies. Remove them from the classpath or use '-Xskip-metadata-version-check' to suppress errors

```



### cpu抖动问题

```
https://zhuanlan.zhihu.com/p/172013683

该文章指出其中两个原因
1，内存读写频繁，导致内存不足，因为调用mmap函数次数太多
2. 内存碎片太多，导致调用compact_zone函数次数太多，需要不停整合内存碎片

对于数据库读写来说，cpu抖动会影响读写的成功率，就是写不进数据，读不出数据的情况

为什么会有内存读写频繁呢
因为es的索引

如何发现读写频繁问题
用perf工具


ElasticSearch稳定性排查过程简述
es读写经常失败
查看cpu利用率-尽量可视化成图
发现cpu抖动
排查user和system进程占用情况
es热点线程和gc是user进程，在抖动的时候，没有变化
system进程cpu增长很多
用perf排查，和相关工具查看内存
pgpgin 换入页字节数
pgpgout 换出页字节数
pgscand 直接扫描内存页数
pgscank 后台线程扫描内存

查看系统日志发现
内存不断回收
系统分配内存失败

查看内存占用情况
PageCache 内存由系统维护，可以被回收的
如果系统内存不足，则内核通过回收 PageCache 的内存即可提供足够的空闲内存

PageCache 回收问题
MMap 就可能导致 PageCache 不能正常回收，原因是 MMap 后应用程序会引用到这部分内存，则内核在回收内存时会忽略这部分内存。而 ES 节点读取文件的方式默认就是 MMap，整体的内存

方案一解决
替换 MMap 去访问文件，在 Java 中即可采用 NIO 方式读取文件

新问题
采用 NIO 访问文件也存在问题，即数据会多一次内存复制，会导致延迟方面比 MMap 方式的高，经过测试发现延迟会高 30%左右

方案二解决
两者结合起来，目的是加快内存回收的同时降低延迟，采取的策略是根据访问频率来确定文件的读写方式（即高频采用 MMap 方式，这样可以保证延迟低，低频采用 Nio 方式，这样可以加快内核回收 PageCache）
查询用mmap
排序用mmap
拿结果用 niofs
结果
延迟方面和 MMap 基本一致
内存回收方面也比 MMap 好

上线后抖动仍然存在！
老方法排查
perf发现 高阶内存不足
系统在进行内存碎片整合（即有 compact_zone()等函数调用），这就意味着此时系统高阶内存是不足，为了进一步验证当前的高阶内存不足，通过 cat/proc/buddyinfo 查看当前系统空闲内存的分布情况
空闲内存很多，但是大部分是碎片

优化 PageCache 间的内存碎片
1、释放内存：释放 PageCache 内存，保证新的空闲内存尽可能连续，具体的处理措施是 echo1 > /proc/sys/vm/drop_cache
2、保留一定空闲内存：目的是避免内存的不断申请和回收，导致内存碎片化再次变的严重，具体处理措施是限制 PageCache 的大小（这里依赖 tlinux 的实现），具体的命令是 echo36 > /proc/sys/vm/pagecache_limit_ratio
结果
此时的空闲也是在 4G 左右，但是大于等于 2 阶的高阶内存占比达到 95%左右，即高阶内存当前是非常充足的，并且机器的 CPU 几乎没有抖动



```

## Linux的内核

### 资料

```
物理页内存分配：https://www.kernel.org/doc/gorman/html/understand/understand009.html
物理内存管理：https://www.kernel.org/doc/gorman/html/understand/understand005.html
```



## 常用代码

### shell比较全的案例

```
ROOT_DIR=`pwd`
cd logs

RECEIVER='xxxx.com'
TITLE='title'
CONTEXT='context'
# logs/文件
# 用逗号作为分隔符，作为关键词的后续添加
LOG_FILES=('nameserver.info.log,offline tablet with endpoint,Run OfflineEndpoint,Run RecoverEndpoint,reconnect zk,kFailed,time of op is too long'
        #    'db_mon.log,mon : kill,mon : exit'
        #    'db_ns_mon.log,mon : kill,mon : exit'
           'tablet.info.log,reconnect zk'
           )
CONTEXT_FILE='context.log'
rm -rf $CONTEXT_FILE
touch $CONTEXT_FILE

双重循环
for file in "${LOG_FILES[@]}"
do
    index=0
    SAVEIFS=$IFS
    IFS=$(echo -en ",")
    for element in $file
        do
            if [ $index -eq 0 ]; then
                monitor_file=$element
                echo $monitor_file
                index=`expr $index + 1`
                else
                # echo $monitor_file
                cat $monitor_file -n | grep $element
                # rows=$(wc -l $monitor_file | awk '{print $1}')
                # echo $rows
            fi
        done
    IFS=$SAVEIFS
    echo " "
done

# echo $CONTEXT | mail -s $TITLE $RECEIVER
# KEYWORD="ERROR"
# ARRAY=($KEYWORD)
# echo ${ARRAY[0]}
# echo ${ARRAY[1]}

# for element in $KEYWORD
# do

# string=`cat -n $LOG_FILE | grep --color $element`
# echo "${string}">>$CONTEXT_FILE
# echo `date +%s`>>$CONTEXT_FILE

# done

# 发邮件shell命令
# echo $CONTEXT | mail -s $TITLE $RECEIVER
# mail -s $TITLE $RECEIVER < $CONTEXT_FILE
# echo "done"
# cd $ROOT_DIR
# cat -n $LOG_FILE | grep ${ARRAY[0]}


# for循环
for i in {1..20}
do
sleep 1
echo $i
done

# 字符串切割
string="2018-12-12 16:10:04.017481 I 5777 [impl.cc:492] offline tablet with"
echo ${string:0:19}
echo $string


# 一行一行打印string里面的值
string="
2018-12-12 16:10:04.017481 I 5777 [impl.cc:492] offline tablet with
2018-12-12 16:10:04.017481 I 5777 [impl.cc:492] offline tablet with"

SAVEIFS=$IFS
IFS=$'\n'
for line in `echo "$string"`
do
    echo "${line}"
    echo "next row"

done
IFS=$SAVEIFS

传入shell脚本外部的参数并打印 $1就是表示第一个参数
echo $1

用脚本测试一个程序运行时间
start_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`

to do sth

finish_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`
duration=$(($(($(date +%s -d "$finish_time")-$(date +%s -d "$start_time")))))
echo "this shell script execution duration: $duration"
```

### for循环遍历

```
https://www.cnblogs.com/EasonJim/p/8315939.html

list="rootfs usr data data2"  
for i in $list;  
do  
echo $i is appoint ;  
done  
```



### 执行当前目录下的test脚本

```
输入all 就运行所有test
输入指定test文件名 就运行指定TEST

if [ $1 = 'all' ]; then
        rows=$(ls | grep test | awk '{print $1}')
        echo $rows
        for test in $rows
        do
            ./$test
        done
    else
        ./$1
fi
```

### 镜像环境的搭建

```
ROOT_DIR=`pwd`

DEPS_SOURCE=`pwd`/thirdsrc
DEPS_PREFIX=`pwd`/thirdparty
DEPS_CONFIG="--prefix=${DEPS_PREFIX} --disable-shared --with-pic"

mkdir -p $DEPS_SOURCE
mkdir -p $DEPS_PREFIX
mkdir -p $DEPS_PREFIX/lib $DEPS_PREFIX/include

```

```
说明
比如安装bison的路径选择
If you need to have bison first in your PATH run:
  echo 'export PATH="/usr/local/opt/bison/bin:$PATH"' >> ~/.bash_profile

For compilers to find bison you may need to set:
  export LDFLAGS="-L/usr/local/opt/bison/lib"
```

```
安装包集合

bison


flex
```


## 常用工具
### mongo
···

mongodb的表就是集合
show collections

> help
        db.help()                    help on db methods
        db.mycoll.help()             help on collection methods
        sh.help()                    sharding helpers
        rs.help()                    replica set helpers
        help admin                   administrative help
        help connect                 connecting to a db help
        help keys                    key shortcuts
        help misc                    misc things to know
        help mr                      mapreduce

        show dbs                     show database names
        show collections             show collections in current database
        show users                   show users in current database
        show profile                 show most recent system.profile entries with time >= 1ms
        show logs                    show the accessible logger names
        show log [name]              prints out the last segment of log in memory, 'global' is default
        use <db_name>                set current database
        db.foo.find()                list objects in collection foo
        db.foo.find( { a : 1 } )     list objects in foo where a == 1
        it                           result of the last line evaluated; use to further iterate
        DBQuery.                                                                                        shellBatchSize = x   set default number of items to display on shell
        exit                         quit the mongo shell

db.c_idex_documents.find()

db.c_idex_documents.find({owner : 'huileihe'})

模糊查询
db.c_idex_documents.find({owner : 'huileihe', prefix_path: /5131/})

1.%xx%

   sql:

       select * from user where name like "%花%";

   mongo:

       db.user.find(name:/花/);

2.xx%

   sql:

      select * from user where name like "花%";

   mongo:

       db.user.find(name:/^花/);

3.不区分大小写

       db.user.find(name:/a/i);



多条件查询
https://segmentfault.com/a/1190000037451303
db.users.find({age: 18, sex: 'girl'})




MongoDB 特点

    面向集合存储：MongoDB 是面向集合的，数据以 collection 分组存储。每个 collection 在数据库中都有唯一的名称。
    模式自由：集合的概念类似 MySQL 里的表，但它不需要定义任何模式。
    结构松散：对于存储在数据库中的文档，不需要设置相同的字段，并且相同的字段不需要相同的数据类型，不同结构的文档可以存在同一个 collection 里。
    高效的二进制存储：存储在集合中的文档，是以键值对的形式存在的。键用于唯一标识一个文档，一般是 ObjectId 类型，值是以 BSON 形式存在的。BSON = Binary JSON， 是在 JSON 基础上加了一些类型及元数据描述的格式。
    支持索引：可以在任意属性上建立索引，包含内部对象。MongoDB 的索引和 MySQL 的索引基本一样，可以在指定属性上创建索引以提高查询的速度。除此之外，MongoDB 还提供创建基于地理空间的索引的能力。
    支持 mapreduce：通过分治的方式完成复杂的聚合任务。
    支持 failover：通过主从复制机制，可以实现数据备份、故障恢复、读扩展等功能。基于复制集的复制机制提供了自动故障恢复的功能，确保了集群数据不会丢失。
    支持分片：MongoDB 支持集群自动切分数据，可以使集群存储更多的数据，实现更大的负载，在数据插入和更新时，能够自动路由和存储。
    支持存储大文件：MongoDB 中 BSON 对象最大不能超过 16 MB。对于大文件的存储，BSON 格式无法满足。GridFS 机制提供了一个存储大文件的机制，可以将一个大文件分割成为多个较小的文档进行存储。

MongoDB 要素

    database: 数据库。
    collection: 数据集合，相当于 MySQL 的 table。
    document: 数据记录行，相当于 MySQL 的 row。
    field: 数据域，相当于 MySQL 的 column。
    index: 索引。
    primary key: 主键。

MongoDB ObjectId
ObjectId 可以快速生成并排序，长度为 12 个字节，包括：

    一个 4 字节的时间戳，表示 unix 时间戳
    5 字节随机值
    3 字节递增计数器，初始化为随机值

在 MongoDB 中，存储在集合中的每个文档都需要一个唯一的 _id 字段作为主键。如果插入的文档省略了 _id 字段，则自动为文档生成一个 _id。
···







[TOC]

