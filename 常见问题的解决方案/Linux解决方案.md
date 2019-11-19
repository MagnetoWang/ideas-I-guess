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

## 系统工具

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
python -m SimpleHTTPServer 1234

在网页上 ip:1234 就可以访问服务器
```

### namespace隔离容器 

```
https://www.cnblogs.com/sammyliu/p/5878973.html
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

### for语法

- for element in $file
- do
- xxxxxxxxx
- done
- 扩展用法
- 循环1到100
  - for i in {1..100}
  - for i in `seq 1 100`

### 运算符

- http://www.runoob.com/linux/linux-shell-basic-operators.html

### export

### unset



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

### mv

- 修改文件夹名字
- mv source_name dest_name

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
https://blog.csdn.net/stepbystepto/article/details/52951849
grep -v *.sh 筛选掉不包含.sh的文件
```



### find

- find ./ -iname rtidb_mon.log
  - 只显示结果必须加 -iname
  - 这是从当前开始查询
- find /. -iname 营销*
  - 从根目录开始查询
- find ../ -iname 营销*
  - 从上一个目录开始查询

### wc

- 基本用法：http://www.cnblogs.com/peida/archive/2012/12/18/2822758.html
- wc -l filename 统计行数
- wc -c filename 统计字节数
- wc -w filenmae 统计字数

### hostname

- hostname -i显示ip
- hostname -f显示域名
- hostname -s显示主机名字
- 参考链接：https://codingstandards.iteye.com/blog/804648

### crontab

- 参考资料：https://www.cnblogs.com/0201zcr/p/4739207.html
- demo参考：http://einverne.github.io/post/2017/03/crontab-schedule-task.html
- 执行脚本出现Permission denied：https://stackoverflow.com/questions/21646551/permission-denied-with-bash-sh-to-run-cron

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



### tail

- 从第5行开始显示文件
  - tail -n +5 log2014.log
- 显示后5行
  - tail -n 5 log2014.log
- 持续更新文件内容
  - **tail -f test.log**

### tar

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
```



### which

- http://www.runoob.com/linux/linux-comm-which.html
- which指令会在环境变量$PATH设置的目录里查找符合条件的文件



### patch

- <https://www.runoob.com/linux/linux-comm-patch.html>
- 命令用于修补文件



### 通过端口查看进程pid

- netstat -an | grep port
- netstat -anp | grep port
- 一般p的参数有权限限制，有了p那么才会显示pid数字
- 参考资料：http://www.cnblogs.com/MacoLee/p/5664306.html

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

###  

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



## docker

```

```




[TOC]

