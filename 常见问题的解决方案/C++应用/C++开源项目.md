

## GLog

- 日志的声明：http://www.voidcn.com/article/p-cfnlsnnv-os.html
- 基本操作：https://www.cppfans.org/1566.html
- 链接gtest 和 glog 两个库。直接运行下面代码

```
#include "gtest/gtest.h"
#include "glog/logging.h"

class GlogTest {};

TEST(GlogTest, InfoLog) {
    LOG(INFO) << "this is glog logging test " << std::endl;
}

int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    google::SetLogDestination(google::INFO,"/Users/magnetowang/Documents/GitHub/IcebergDB/ibdb/log/");  
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```



## Gflags

- 文档：https://gflags.github.io/gflags/#define

- 基本调用：http://dreamrunner.org/blog/2014/03/09/gflags-jian-ming-shi-yong/

- 主要两点
  - 在某个文件定义好所有的全局变量，统一管理
  - 在其他要使用该文件的代码中，加一条声明即可
  - 头文件
  - 比如
  - DEFINE_string(endpoint, "", "config the ip and port that rtidb serves for");
    - 变量名，变量值，变量说明
  - DECLARE_string(endpoint);
  - 掌握这两点即可！

- Gflags类型

- ```
  DEFINE_bool: boolean
  DEFINE_int32: 32-bit integer
  DEFINE_int64: 64-bit integer
  DEFINE_uint64: unsigned 64-bit integer
  DEFINE_double: double
  DEFINE_string: C++ string 
  
  头文件
  #include "gflags/gflags.h"
  
  使用Gflags
     if (FLAGS_consider_made_up_languages)
       FLAGS_languages += ",klingon";   // implied by --consider_made_up_languages
     if (FLAGS_languages.find("finnish") != string::npos)
       HandleFinnish();
       
  声明Gflags
  	DECLARE_bool(big_menu);
  ```

### 安装

```
git clone https://github.com/gflags/gflags.git

cd gflags
mkdir build && cd build
cmake .. && make
cp -r include/. xxxx
cp -r lib/. xxxx
```

### 使用

```
随意定义一个文件
#include <gflags/gflags.h>

   DEFINE_bool(big_menu, true, "Include 'advanced' options in the menu listing");
   DEFINE_string(languages, "english,french,german",
                 "comma-separated list of languages to offer in the 'lang' menu");
```



## GTest

- 基本使用：https://www.ibm.com/developerworks/aix/library/au-googletestingframework.html
- 文档：https://github.com/google/googletest/blob/master/googletest/docs/primer.md
- 基本操作
  - 引用头文件 "gtest/gtest.h"
  - 必须先创建一个Test类，然后继承GTest

```
#include "gtest/gtest.h"

TEST (SquareRootTest, PositiveNos) { 
    EXPECT_EQ (18.0, square-root (324.0));
    EXPECT_EQ (25.4, square-root (645.16));
    EXPECT_EQ (50.3321, square-root (2533.310224));
}
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

SquareRootTest 就是新建的Test类
PositiveNos 测试用例的函数名字
EXPECT_EQ 类似于assert 和 if 专门用于测试结果是否符合预期
square-root 这就是我们测试的函数

```

- 高级操作：http://www.cnblogs.com/coderzh/archive/2009/04/06/1426755.html

- 生成xml文档：https://stackoverflow.com/questions/8268584/generate-google-c-unit-test-xml-report

- TEST说明

- ```
  use the TEST_P macro to define as many test patterns using this fixture as you want. The _P suffix is for "parameterized" or "pattern", whichever you prefer to think.
  
  you can use INSTANTIATE_TEST_SUITE_P to instantiate the test suite with any set of parameters you want. googletest defines a number of functions for generating test parameters. They return what we call (surprise!) parameter generators. Here is a summary of them, which are all in the testing namespace
  ```

### 高级配置

```
INSTANTIATE_TEST_CASE_P：https://www.cnblogs.com/jycboy/p/6118073.html
实例化具有任何您想要的参数的测试用例。 Google Test定义了一些用于生成测试参数的函数。 它们返回我们所谓的参数生成器（surprise！）



```

## BRPC

### 文档

- memory_management
- consistent_hashing.md
- load_balancing.md
- lalb.md
- json2pb.md
- iobuf.md
- io.md
- http_service.md
- http_client.md
- circuit_breaker.md
- client.md
- case_ubrpc.md
- bvar.md
- execution_queue.md
- error_code.md
- builtin_service.md
- bthread.md
- bthread_or_not.md
- bthread_id.md
- baidu_std.md
- avalanche.md
- auto_concurrency_limiter.md
- server.md
- threading_overview.md
- streaming_rpc.md

### 概念

- brpc::Channel
  - 连接服务器的类，主要参数是服务器地址
- brpc::ChannelOptions
  - 设置rpc的管道相关参数
  - protocol
  - connection_type
  - timeout_ms
  - max_retry
- brpc::Controller
  - brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
- brpc::Stub
- brpc::ClosureGuard done_guard(done);
  - This object helps you to call done->Run() in RAII style

### 函数

- usleep

### 用法

#### 客户端

```
#include <gflags/gflags.h>
#include <butil/logging.h>
#include <butil/time.h>
#include <brpc/channel.h>
#include "echo.pb.h"


int main(int argc, char* argv[]) {
    // Parse gflags. We recommend you to use gflags as well.
    GFLAGS_NS::ParseCommandLineFlags(&argc, &argv, true);
    
    // A Channel represents a communication line to a Server. Notice that 
    // Channel is thread-safe and can be shared by all threads in your program.
    brpc::Channel channel;
    
    // Initialize the channel, NULL means using default options.
    brpc::ChannelOptions options;
    options.protocol = FLAGS_protocol;
    options.connection_type = FLAGS_connection_type;
    options.timeout_ms = FLAGS_timeout_ms/*milliseconds*/;
    options.max_retry = FLAGS_max_retry;
    if (channel.Init(FLAGS_server.c_str(), FLAGS_load_balancer.c_str(), &options) != 0) {
        LOG(ERROR) << "Fail to initialize channel";
        return -1;
    }

    // Normally, you should not call a Channel directly, but instead construct
    // a stub Service wrapping it. stub can be shared by all threads as well.
    example::EchoService_Stub stub(&channel);

    // Send a request and wait for the response every 1 second.
    int log_id = 0;
    while (!brpc::IsAskedToQuit()) {
        // We will receive response synchronously, safe to put variables
        // on stack.
        example::EchoRequest request;
        example::EchoResponse response;
        brpc::Controller cntl;

        request.set_message("hello world");

        cntl.set_log_id(log_id ++);  // set by user
        // Set attachment which is wired to network directly instead of 
        // being serialized into protobuf messages.
        cntl.request_attachment().append(FLAGS_attachment);

        // Because `done'(last parameter) is NULL, this function waits until
        // the response comes back or error occurs(including timedout).
        stub.Echo(&cntl, &request, &response, NULL);
        if (!cntl.Failed()) {
            LOG(INFO) << "Received response from " << cntl.remote_side()
                << " to " << cntl.local_side()
                << ": " << response.message() << " (attached="
                << cntl.response_attachment() << ")"
                << " latency=" << cntl.latency_us() << "us";
        } else {
            LOG(WARNING) << cntl.ErrorText();
        }
        usleep(FLAGS_interval_ms * 1000L);
    }

    LOG(INFO) << "EchoClient is going to quit";
    return 0;
}

```

#### 服务端

```
// A server to receive EchoRequest and send back EchoResponse.

#include <gflags/gflags.h>
#include <butil/logging.h>
#include <brpc/server.h>
#include "echo.pb.h"

// Your implementation of example::EchoService
// Notice that implementing brpc::Describable grants the ability to put
// additional information in /status.
namespace example {
class EchoServiceImpl : public EchoService {
public:
    EchoServiceImpl() {};
    virtual ~EchoServiceImpl() {};
    virtual void Echo(google::protobuf::RpcController* cntl_base,
                      const EchoRequest* request,
                      EchoResponse* response,
                      google::protobuf::Closure* done) {
        // This object helps you to call done->Run() in RAII style. If you need
        // to process the request asynchronously, pass done_guard.release().
        brpc::ClosureGuard done_guard(done);

        brpc::Controller* cntl =
            static_cast<brpc::Controller*>(cntl_base);

        // The purpose of following logs is to help you to understand
        // how clients interact with servers more intuitively. You should 
        // remove these logs in performance-sensitive servers.
        LOG(INFO) << "Received request[log_id=" << cntl->log_id() 
                  << "] from " << cntl->remote_side() 
                  << " to " << cntl->local_side()
                  << ": " << request->message()
                  << " (attached=" << cntl->request_attachment() << ")";

        // Fill response.
        response->set_message(request->message());

        // You can compress the response by setting Controller, but be aware
        // that compression may be costly, evaluate before turning on.
        // cntl->set_response_compress_type(brpc::COMPRESS_TYPE_GZIP);

        if (FLAGS_echo_attachment) {
            // Set attachment which is wired to network directly instead of
            // being serialized into protobuf messages.
            cntl->response_attachment().append(cntl->request_attachment());
        }
    }
};
}  // namespace example

int main(int argc, char* argv[]) {
    // Parse gflags. We recommend you to use gflags as well.
    GFLAGS_NS::ParseCommandLineFlags(&argc, &argv, true);

    // Generally you only need one Server.
    brpc::Server server;

    // Instance of your service.
    example::EchoServiceImpl echo_service_impl;

    // Add the service into server. Notice the second parameter, because the
    // service is put on stack, we don't want server to delete it, otherwise
    // use brpc::SERVER_OWNS_SERVICE.
    if (server.AddService(&echo_service_impl, 
                          brpc::SERVER_DOESNT_OWN_SERVICE) != 0) {
        LOG(ERROR) << "Fail to add service";
        return -1;
    }

    // Start the server.
    brpc::ServerOptions options;
    options.idle_timeout_sec = FLAGS_idle_timeout_s;
    if (server.Start(FLAGS_port, &options) != 0) {
        LOG(ERROR) << "Fail to start EchoServer";
        return -1;
    }

    // Wait until Ctrl-C is pressed, then Stop() and Join() the server.
    server.RunUntilAskedToQuit();
    return 0;
}

```

### 测试rpc功能

- 参考资料
  - 中文说明：<http://www.cnblogs.com/welkinwalker/archive/2011/11/29/2267225.html>
  - 使用说明：<https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md

#### 手动测试

- 编写客户端
- 编写服务端
- 然后查看消息传送的内容
- 非常传统，低效率

#### gmock

- 使用gtest里面的gmock

```

```

### brpc进阶

- 模块协议设计：https://www.cnblogs.com/xudong-bupt/p/9496887.html
- 

## ZooKeeper

### 入门

- 参考资料
  - 官方文档：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperProgrammers.html#sc_zkDataModel_znodes>
  - zk配置文件说明：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperStarted.html
  - 命令行文档（超级棒）：<http://www.corejavaguru.com/bigdata/zookeeper/cli>
  - zk内部实现原理文档：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperInternals.html>
  - zk实现生产者和消费者队列和进程的屏障类：<https://zookeeper.apache.org/doc/r3.1.2/zookeeperTutorial.html>
  - c++example：<https://github.com/tgockel/zookeeper-cpp>
  - zooCAPI使用：<http://www.cnblogs.com/haippy/archive/2013/02/21/2920426.html>
  - ACL控制权：<http://ifeve.com/zookeeper-access-control-using-acls/>
  - 书籍推荐
    - 从paxos到zookeeper分布式一致性原理与实践
    - ZooKeeper官方指南
- 问题
  - 集群模式和单机模式
    - 集群就是要配好多台机器的ip和端口。那么每台机器都要有zk程序才行
    - 单机只需要配置本机ip和端口即可
- 使用

```bash
zk的编程学习分三步，建议配合参考资料更详细的说明一起来入门zk
第一步，配置zk服务
第二步，启动zk服务
第三步，开始编程


前提:在zk目录下
第一步，配置zk服务
# 进入conf目录下
cd conf
cp zoo_sample.cfg zoo.cfg

# zoo.cfg服务器配置说明
# the first port is for synchronizing data and communication
# the second port is for leader election
server.1=127.0.0.1:2888:3888
server.2=127.0.0.1:2788:3788
server.3=127.0.0.1:2688:3688

# 单机版
# ip不变，端口一定要不一样
# 集群版
# ip一定要不一样，端口无所谓

# zoo.cfg 里面有DataDir目录，在这个目录下创建myid，myid里面写上id数字就行了

第二步，启动zk服务
# 进入bin目录下，启动服务脚本
cd bin
sh zkServer.sh start
# 验证服务
telnet 127.0.0.1 2181

第三步，开始编程
# 有三种方式，一种是编程语言，另一种是命令行对zk操作
# 先介绍命令行方式
sh zkCli.sh
# 输出所有命令行语法
help
create /zk_test my_data
get /zk_test
# get的结果说明
my_data :This line of text is the data that we stored in the znode.
cZxid = 0x8 :The zxid (ZooKeeper Transaction Id) of the change that caused this znode to be created.
ctime = Mon Nov 30 18:41:06 IST 2015 :The time when this znode was created.
mZxid = 0x8 :The zxid of the change that last modified this znode.
mtime = Mon Nov 30 18:41:06 IST 2015 :The time when this znode was last modified.
pZxid = 0x8 :The zxid of the change that last modified children of this znode.
cversion = 0 :The number of changes to the children of this znode.
dataVersion = 0 :The number of changes to the data of this znode.
aclVersion = 0 :The number of changes to the ACL of this znode.
ephemeralOwner = 0x0: The session id of the owner of this znode if the znode is an ephemeral node. If it is not an ephemeral node, it will be zero.
dataLength = 7 :The length of the data field of this znode.
numChildren = 0 :The number of children of this znode.
# 设置watch
# Watches show a notification when the specified znode’s data get changed
get /zk_test 1

# 编程语言方式
Java非常简单引入jar包，然后直接调接口就行了
直接看C语言编程怎么引入，这里专门放下面一栏
```

### C++ API使用

- 强烈建议先在命令行下体验zk的功能，然后再来编程封装适合自己业务的功能
- 参考资料
  - zk 状态说明：<http://www.cnblogs.com/haippy/archive/2013/02/21/2920241.html>
  - 接口设计参考：<http://www.throwable.club/2018/12/16/zookeeper-curator-usage/#Curator%E7%9A%84%E5%9F%BA%E6%9C%ACApi>
- 注意
  - zk命令行中不提供递归创建节点，同时也不提供创建无数据的节点

```
#include "zookeeper.h"
zhandle_t *zh;

```

- zookeeper状态码

```c++
/** zookeeper return constants **/

enum ZOO_ERRORS {
  ZOK = 0, /*!< Everything is OK */

  /** System and server-side errors.
   * This is never thrown by the server, it shouldn't be used other than
   * to indicate a range. Specifically error codes greater than this
   * value, but lesser than {@link #ZAPIERROR}, are system errors. */
  ZSYSTEMERROR = -1,
  ZRUNTIMEINCONSISTENCY = -2, /*!< A runtime inconsistency was found */
  ZDATAINCONSISTENCY = -3, /*!< A data inconsistency was found */
  ZCONNECTIONLOSS = -4, /*!< Connection to the server has been lost */
  ZMARSHALLINGERROR = -5, /*!< Error while marshalling or unmarshalling data */
  ZUNIMPLEMENTED = -6, /*!< Operation is unimplemented */
  ZOPERATIONTIMEOUT = -7, /*!< Operation timeout */
  ZBADARGUMENTS = -8, /*!< Invalid arguments */
  ZINVALIDSTATE = -9, /*!< Invliad zhandle state */

  /** API errors.
   * This is never thrown by the server, it shouldn't be used other than
   * to indicate a range. Specifically error codes greater than this
   * value are API errors (while values less than this indicate a 
   * {@link #ZSYSTEMERROR}).
   */
  ZAPIERROR = -100,
  ZNONODE = -101, /*!< Node does not exist */
  ZNOAUTH = -102, /*!< Not authenticated */
  ZBADVERSION = -103, /*!< Version conflict */
  ZNOCHILDRENFOREPHEMERALS = -108, /*!< Ephemeral nodes may not have children */
  ZNODEEXISTS = -110, /*!< The node already exists */
  ZNOTEMPTY = -111, /*!< The node has children */
  ZSESSIONEXPIRED = -112, /*!< The session has been expired by the server */
  ZINVALIDCALLBACK = -113, /*!< Invalid callback specified */
  ZINVALIDACL = -114, /*!< Invalid ACL specified */
  ZAUTHFAILED = -115, /*!< Client authentication failed */
  ZCLOSING = -116, /*!< ZooKeeper is closing */
  ZNOTHING = -117, /*!< (not error) no server responses to process */
  ZSESSIONMOVED = -118 /*!<session moved to another server, so operation is ignored */ 
};

/**
*  @name Debug levels
*/
typedef enum {ZOO_LOG_LEVEL_ERROR=1,ZOO_LOG_LEVEL_WARN=2,ZOO_LOG_LEVEL_INFO=3,ZOO_LOG_LEVEL_DEBUG=4} ZooLogLevel;

/**
 * @name ACL Consts
 */
extern ZOOAPI const int ZOO_PERM_READ;
extern ZOOAPI const int ZOO_PERM_WRITE;
extern ZOOAPI const int ZOO_PERM_CREATE;
extern ZOOAPI const int ZOO_PERM_DELETE;
extern ZOOAPI const int ZOO_PERM_ADMIN;
extern ZOOAPI const int ZOO_PERM_ALL;

/** This Id represents anyone. */
extern ZOOAPI struct Id ZOO_ANYONE_ID_UNSAFE;
/** This Id is only usable to set ACLs. It will get substituted with the
 * Id's the client authenticated with.
 */
extern ZOOAPI struct Id ZOO_AUTH_IDS;

/** This is a completely open ACL*/
extern ZOOAPI struct ACL_vector ZOO_OPEN_ACL_UNSAFE;
/** This ACL gives the world the ability to read. */
extern ZOOAPI struct ACL_vector ZOO_READ_ACL_UNSAFE;
/** This ACL gives the creators authentication id's all permissions. */
extern ZOOAPI struct ACL_vector ZOO_CREATOR_ALL_ACL;

/**
 * @name Interest Consts
 * These constants are used to express interest in an event and to
 * indicate to zookeeper which events have occurred. They can
 * be ORed together to express multiple interests. These flags are
 * used in the interest and event parameters of 
 * \ref zookeeper_interest and \ref zookeeper_process.
 */
// @{
extern ZOOAPI const int ZOOKEEPER_WRITE;
extern ZOOAPI const int ZOOKEEPER_READ;
// @}

/**
 * @name Create Flags
 * 
 * These flags are used by zoo_create to affect node create. They may
 * be ORed together to combine effects.
 */
// @{
extern ZOOAPI const int ZOO_EPHEMERAL;
extern ZOOAPI const int ZOO_SEQUENCE;
// @}

/**
 * @name State Consts
 * These constants represent the states of a zookeeper connection. They are
 * possible parameters of the watcher callback.
 */
// @{
extern ZOOAPI const int ZOO_EXPIRED_SESSION_STATE;
extern ZOOAPI const int ZOO_AUTH_FAILED_STATE;
extern ZOOAPI const int ZOO_CONNECTING_STATE;
extern ZOOAPI const int ZOO_ASSOCIATING_STATE;
extern ZOOAPI const int ZOO_CONNECTED_STATE;
// @}

/**
 * @name Watch Types
 * These constants indicate the event that caused the watch event. They are
 * possible values of the first parameter of the watcher callback.
 */
// @{
/**
 * \brief a node has been created.
 * 
 * This is only generated by watches on non-existent nodes. These watches
 * are set using \ref zoo_exists.
 */
extern ZOOAPI const int ZOO_CREATED_EVENT;
/**
 * \brief a node has been deleted.
 * 
 * This is only generated by watches on nodes. These watches
 * are set using \ref zoo_exists and \ref zoo_get.
 */
extern ZOOAPI const int ZOO_DELETED_EVENT;
/**
 * \brief a node has changed.
 * 
 * This is only generated by watches on nodes. These watches
 * are set using \ref zoo_exists and \ref zoo_get.
 */
extern ZOOAPI const int ZOO_CHANGED_EVENT;
/**
 * \brief a change as occurred in the list of children.
 * 
 * This is only generated by watches on the child list of a node. These watches
 * are set using \ref zoo_get_children or \ref zoo_get_children2.
 */
extern ZOOAPI const int ZOO_CHILD_EVENT;
/**
 * \brief a session has been lost.
 * 
 * This is generated when a client loses contact or reconnects with a server.
 */
extern ZOOAPI const int ZOO_SESSION_EVENT;

/**
 * \brief a watch has been removed.
 * 
 * This is generated when the server for some reason, probably a resource
 * constraint, will no longer watch a node for a client.
 */
extern ZOOAPI const int ZOO_NOTWATCHING_EVENT;
```



## Apache arrow

### 资料

- 介绍：<https://www.cnblogs.com/smartloli/p/6367719.html

### 常用功能

```
结构体转arrow的table类型
https://arrow.apache.org/docs/cpp/examples/tuple_range_conversion.html

table转结构体
https://arrow.apache.org/docs/cpp/examples/row_columnar_conversion.html

获取arrow的int,long,double类型方法
auto values = std::static_pointer_cast<arrow::Int32Array>(column_data.at(i)->chunk(0));
int32_t value = values->Value(j);

auto values = std::static_pointer_cast<arrow::Int64Array>(column_data.at(i)->chunk(0));
double value = values->Value(j);


```



## Hadoop

### 资料

- 官网：<https://hadoop.apache.org/>

### 安装

```
wget http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
tar -zxvf hadoop-3.1.2.tar.gz

mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.2.jar grep input output 'dfs[a-z.]+'
cat output/*


```

### hadoop命令

```
FS Shell
调用文件系统(FS)Shell命令应使用 bin/hadoop fs <args>的形式。 所有的的FS shell命令使用URI路径作为参数。URI格式是scheme://authority/path。对HDFS文件系统，scheme是hdfs，对本地文件系统，scheme是file。其中scheme和authority参数都是可选的，如果未加指定，就会使用配置中指定的默认scheme。一个HDFS文件或目录比如/parent/child可以表示成hdfs://namenode:namenodeport/parent/child，或者更简单的/parent/child（假设你配置文件中的默认值是namenode:namenodeport）。大多数FS Shell命令的行为和对应的Unix Shell命令类似，不同之处会在下面介绍各命令使用详情时指出。出错信息会输出到stderr，其他信息输出到stdout。

cat
使用方法：hadoop fs -cat URI [URI …]

将路径指定文件的内容输出到stdout。

示例：

hadoop fs -cat hdfs://host1:port1/file1 hdfs://host2:port2/file2
hadoop fs -cat file:///file3 /user/hadoop/file4
返回值：
成功返回0，失败返回-1。

chgrp
使用方法：hadoop fs -chgrp [-R] GROUP URI [URI …] Change group association of files. With -R, make the change recursively through the directory structure. The user must be the owner of files, or else a super-user. Additional information is in the Permissions User Guide. -->

改变文件所属的组。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。更多的信息请参见HDFS权限用户指南。

chmod
使用方法：hadoop fs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI …]

改变文件的权限。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户。更多的信息请参见HDFS权限用户指南。

chown
使用方法：hadoop fs -chown [-R] [OWNER][:[GROUP]] URI [URI ]

改变文件的拥有者。使用-R将使改变在目录结构下递归进行。命令的使用者必须是超级用户。更多的信息请参见HDFS权限用户指南。

copyFromLocal
使用方法：hadoop fs -copyFromLocal <localsrc> URI

除了限定源路径是一个本地文件外，和put命令相似。

copyToLocal
使用方法：hadoop fs -copyToLocal [-ignorecrc] [-crc] URI <localdst>

除了限定目标路径是一个本地文件外，和get命令类似。

cp
使用方法：hadoop fs -cp URI [URI …] <dest>

将文件从源路径复制到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。 
示例：

hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2
hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir
返回值：

成功返回0，失败返回-1。

du
使用方法：hadoop fs -du URI [URI …]

显示目录中所有文件的大小，或者当只指定一个文件时，显示此文件的大小。
示例：
hadoop fs -du /user/hadoop/dir1 /user/hadoop/file1 hdfs://host:port/user/hadoop/dir1 
返回值：
成功返回0，失败返回-1。 
dus
使用方法：hadoop fs -dus <args>

显示文件的大小。

expunge
使用方法：hadoop fs -expunge

清空回收站。请参考HDFS设计文档以获取更多关于回收站特性的信息。

get
使用方法：hadoop fs -get [-ignorecrc] [-crc] <src> <localdst> 
复制文件到本地文件系统。可用-ignorecrc选项复制CRC校验失败的文件。使用-crc选项复制文件以及CRC信息。

示例：

hadoop fs -get /user/hadoop/file localfile
hadoop fs -get hdfs://host:port/user/hadoop/file localfile
返回值：

成功返回0，失败返回-1。

getmerge
使用方法：hadoop fs -getmerge <src> <localdst> [addnl]

接受一个源目录和一个目标文件作为输入，并且将源目录中所有的文件连接成本地目标文件。addnl是可选的，用于指定在每个文件结尾添加一个换行符。

ls
使用方法：hadoop fs -ls <args>

如果是文件，则按照如下格式返回文件信息：
文件名 <副本数> 文件大小 修改日期 修改时间 权限 用户ID 组ID 
如果是目录，则返回它直接子文件的一个列表，就像在Unix中一样。目录返回列表的信息如下：
目录名 <dir> 修改日期 修改时间 权限 用户ID 组ID 
示例：
hadoop fs -ls /user/hadoop/file1 /user/hadoop/file2 hdfs://host:port/user/hadoop/dir1 /nonexistentfile 
返回值：
成功返回0，失败返回-1。 
lsr
使用方法：hadoop fs -lsr <args> 
ls命令的递归版本。类似于Unix中的ls -R。

mkdir
使用方法：hadoop fs -mkdir <paths> 
接受路径指定的uri作为参数，创建这些目录。其行为类似于Unix的mkdir -p，它会创建路径中的各级父目录。

示例：

hadoop fs -mkdir /user/hadoop/dir1 /user/hadoop/dir2
hadoop fs -mkdir hdfs://host1:port1/user/hadoop/dir hdfs://host2:port2/user/hadoop/dir
返回值：

成功返回0，失败返回-1。

movefromLocal
使用方法：dfs -moveFromLocal <src> <dst>

输出一个”not implemented“信息。

mv
使用方法：hadoop fs -mv URI [URI …] <dest>

将文件从源路径移动到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。不允许在不同的文件系统间移动文件。 
示例：

hadoop fs -mv /user/hadoop/file1 /user/hadoop/file2
hadoop fs -mv hdfs://host:port/file1 hdfs://host:port/file2 hdfs://host:port/file3 hdfs://host:port/dir1
返回值：

成功返回0，失败返回-1。

put
使用方法：hadoop fs -put <localsrc> ... <dst>

从本地文件系统中复制单个或多个源路径到目标文件系统。也支持从标准输入中读取输入写入目标文件系统。
hadoop fs -put localfile /user/hadoop/hadoopfile
hadoop fs -put localfile1 localfile2 /user/hadoop/hadoopdir
hadoop fs -put localfile hdfs://host:port/hadoop/hadoopfile
hadoop fs -put - hdfs://host:port/hadoop/hadoopfile 
从标准输入中读取输入。
返回值：

成功返回0，失败返回-1。

rm
使用方法：hadoop fs -rm URI [URI …]

删除指定的文件。只删除非空目录和文件。请参考rmr命令了解递归删除。
示例：

hadoop fs -rm hdfs://host:port/file /user/hadoop/emptydir
返回值：

成功返回0，失败返回-1。

rmr
使用方法：hadoop fs -rmr URI [URI …]

delete的递归版本。
示例：

hadoop fs -rmr /user/hadoop/dir
hadoop fs -rmr hdfs://host:port/user/hadoop/dir
返回值：

成功返回0，失败返回-1。

setrep
使用方法：hadoop fs -setrep [-R] <path>

改变一个文件的副本系数。-R选项用于递归改变目录下所有文件的副本系数。

示例：

hadoop fs -setrep -w 3 -R /user/hadoop/dir1
返回值：

成功返回0，失败返回-1。

stat
使用方法：hadoop fs -stat URI [URI …]

返回指定路径的统计信息。

示例：

hadoop fs -stat path
返回值：
成功返回0，失败返回-1。

tail
使用方法：hadoop fs -tail [-f] URI

将文件尾部1K字节的内容输出到stdout。支持-f选项，行为和Unix中一致。

示例：

hadoop fs -tail pathname
返回值：
成功返回0，失败返回-1。

test
使用方法：hadoop fs -test -[ezd] URI

选项：
-e 检查文件是否存在。如果存在则返回0。
-z 检查文件是否是0字节。如果是则返回0。 
-d 如果路径是个目录，则返回1，否则返回0。
示例：

hadoop fs -test -e filename
text
使用方法：hadoop fs -text <src> 
将源文件输出为文本格式。允许的格式是zip和TextRecordInputStream。

touchz
使用方法：hadoop fs -touchz URI [URI …] 
创建一个0字节的空文件。

示例：

hadoop -touchz pathname
返回值：
成功返回0，失败返回-1。
```



### Yarn

- hadoop的组件
- 概念介绍：<https://zhuanlan.zhihu.com/p/41151457>
- 常用命令：<https://yarn.bootcss.com/docs/usage/>

### 常用功能

```
命令行
https://blog.csdn.net/sunshingheavy/article/details/53227581
```

## RocksDB

### 资料

- 中文网：<https://rocksdb.org.cn/doc/Implement-Queue-Service-Using-RocksDB.html>



## Abseil 基础库
1. 源码：https://github.com/abseil/abseil-cpp
2. c++Tips：https://abseil.io/tips/

### 模块介绍

## RocksDB

### 资料

- 全面介绍：<http://alexstocks.github.io/html/rocksdb.html>



## Json-C++

### 资料

- nlohman库：https://github.com/nlohmann/json

### 文件读取json对象

```
https://blog.csdn.net/kuyu05/article/details/88561319
using json = nlohmann::json;

std::ifstream read("broker.json");
	json in = json::parse(read);
	cout << in.dump(4) << endl;
```

### json对象函数传入

```
using Json = nlohmann::json;

Json::iterator
Json
```

## Xgboost

### llvm RTTI

```
https://baike.baidu.com/item/RTTI
RTTI（Run-Time Type Identification)，通过运行时类型信息程序能够使用基类的指针或引用来检查这些指针或引用所指的对象的实际派生类型。
```
## Mxnet

```
base.h
只有枚举类

shape.h
声明ndarray数组维度和大小


operator symbol


ndarray.h

c_api_ndarray.cc
实现很多调用函数，比如
MXImperativeInvoke,MXImperativeInvokeImpl


```

## dmlc

```
有非常多工具库函数
CSVParser


```

## DCPMM

```
说明：https://blog.csdn.net/limanjihe/article/details/106158713
编程工具库：https://pmem.io/pmdk/
```

## asio网络库

### 资料

```
优点和缺点：https://zhuanlan.zhihu.com/p/37590580


```

### 配置

```
单线程设置
asio::io_context context(1); // one thread


transfer_at_least
```

### reactor模式和proactor模式

```

```



[TOC]

