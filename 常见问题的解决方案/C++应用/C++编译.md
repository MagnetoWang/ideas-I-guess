


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

### 多个文件互相调用函数

```
使用extern 声明外部文件的函数

使用头文件方式，引入外部函数
```

### 多个文件互相调用同一个头文件的变量问题

```
a.h
std::vector<Value*> row

b.cpp
c.cpp
d.cpp
```

### 生成core文件，然后gdb调试

```
快速上手：https://blog.csdn.net/u011806486/article/details/81409992
调试详细文章：https://blog.csdn.net/hello2mao/article/details/79258471

查看core文件大小，默认为0
ulimit -a

core file size 为无限
ulimit -c unlimited

不产生core文件,注意，改回0以后，就无法再改成unlimited
ulimit -c 0

调试
gdb 可执行程序 core
gdb ./xxx/xxx执行程序  core.29373


进阶 进入gdb界面以后
直接打印问题代码堆栈
bt

动态编译的程序是不能直接gdb，需要在cmakelist中添加定义
add_definitions(-D_DEBUG)
```

### 安装GCC 5.4.0版本

```
https://www.jianshu.com/p/0caef3ce8e06

wget https://mirrors.ustc.edu.cn/gnu/gcc/gcc-5.4.0/gcc-5.4.0.tar.gz
tar -zxvf gcc-5.4.0.tar.gz
cd gcc-5.4.0
./contrib/download_prerequisites
mkdir build
./configure --prefix=/home/wangzixian/software/gcc-5.4.0/build --enable-languages=c,c++ --disable-multilib --enable-host-shared
make -j12 && make install

./configure --prefix=/home/wangzixian/ferrari/feql-jit/compatible-with-linux-1/pico/gcc/build --enable-threads=posix --disable-multilib --enable-languages=c,c++
```

### 安装bazel

```
wget https://github.com/bazelbuild/bazel/releases/download/0.29.0/bazel-0.29.0-installer-darwin-x86_64.sh
sh bazel-0.29.0-installer-darwin-x86_64.sh --prefix=/xxx/xxx/third_party

添加bin的环境路径
```



## Mac下的C++

### endian.h 配置路径

- vscode自动补全路径

```
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**",
                "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/machine"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```







## GCC && CMKAE

```
-Weffc++ 编译的时候用来判断变量是否初始化
```



## GDB的使用

- 参考资料
  - <https://www.cs.cmu.edu/~gilpin/tutorial/>
  - <https://blog.csdn.net/liigo/article/details/582231>

```
添加可以gdb调试的文件
gdb xxx

然后运行 也可以重新执行
run 或者 start


设置断点
b <行号>
b <函数名称>
b *<函数名称>
b *<代码地址>

跳下一个断点
c continue

删除断点
d [断点的编号]

函数判断
s: 执行一行源程序代码，如果此行代码中有函数调用，则进入该函数；
n: 执行一行源程序代码，此行代码中的函数调用也一并执行。 

打印变量
p <变量名称>

gdb disassemble
反汇编某个函数，然后排查地址是否变化
https://www.cnblogs.com/qiangxia/p/4683309.html
```

### 排查工具推荐

```
valgrind：https://my.oschina.net/u/269082/blog/832657

sanitizer：https://www.jianshu.com/p/3a2df9b7c353
```



### Unable to find Mach task port for process-id 801: (os/kern) failure (0x5)

- 参考资料：<https://stackoverflow.com/questions/11504377/gdb-fails-with-unable-to-find-mach-task-port-for-process-id-error>
- 最快的方法
- sudo gdb xxxx
- 长久的方法
  - <http://codelife.me/blog/2014/07/14/install-gdb-on-osx-mavericks/>
- 安装gdb证书

### During startup program terminated with signal SIG113 ?

- 编译被终止了在mac系统中

### During startup program terminated with signal SIGTRAP

- 

## lldb的使用

- 参考资料
  - <https://www.jianshu.com/p/087cd19d49ba>
- 下一步直接进入源码层 s
- 下一步但是不进入源码层 n
- 给某个文件设置断点
  - breakpoint set -f Foo.m -l 10
  - <https://www.jianshu.com/p/dcc8e647a501>
- 跳到下一个断点
  - c
- 打印变量内容
  - print 变量名 打印基本数据类型的内容
  - po 变量名 打印对象内容
  - <http://see.sl088.com/wiki/LLDB_%E6%89%93%E5%8D%B0%E5%8F%98%E9%87%8F>

```
Debugger commands:
  apropos           -- List debugger commands related to a word or subject.
  breakpoint        -- Commands for operating on breakpoints (see 'help b' for shorthand.)
  bugreport         -- Commands for creating domain-specific bug reports.
  command           -- Commands for managing custom LLDB commands.
  disassemble       -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  expression        -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  frame             -- Commands for selecting and examing the current thread's stack frames.
  gdb-remote        -- Connect to a process via remote GDB server.  If no host is specifed, localhost is assumed.
  gui               -- Switch into the curses based GUI mode.
  help              -- Show a list of all debugger commands, or give details about a specific command.
  kdp-remote        -- Connect to a process via remote KDP server.  If no UDP port is specified, port 41139 is assumed.
  language          -- Commands specific to a source language.
  log               -- Commands controlling LLDB internal logging.
  memory            -- Commands for operating on memory in the current target process.
  platform          -- Commands to manage and create platforms.
  plugin            -- Commands for managing LLDB plugins.
  process           -- Commands for interacting with processes on the current platform.
  quit              -- Quit the LLDB debugger.
  register          -- Commands to access registers for the current thread and stack frame.
  script            -- Invoke the script interpreter with provided code and display any results.  Start the interactive interpreter if no code is supplied.
  settings          -- Commands for managing LLDB settings.
  source            -- Commands for examining source code described by debug information for the current target process.
  statistics        -- Print statistics about a debugging session
  target            -- Commands for operating on debugger targets.
  thread            -- Commands for operating on one or more threads in the current process.
  type              -- Commands for operating on the type system.
  version           -- Show the LLDB debugger version.
  watchpoint        -- Commands for operating on watchpoints.
Current command abbreviations (type 'help command alias' for more info):
  add-dsym  -- Add a debug symbol file to one of the target's current modules by specifying a path to a debug symbols file, or using the options to specify a module to download symbols
               for.
  attach    -- Attach to process by ID or name.
  b         -- Set a breakpoint using one of several shorthand formats.
  bt        -- Show the current thread's call stack.  Any numeric argument displays at most that many frames.  The argument 'all' displays all threads.
  c         -- Continue execution of all threads in the current process.
  call      -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  continue  -- Continue execution of all threads in the current process.
  detach    -- Detach from the current target process.
  di        -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  dis       -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
  display   -- Evaluate an expression at every stop (see 'help target stop-hook'.)
  down      -- Select a newer stack frame.  Defaults to moving one frame, a numeric argument can specify an arbitrary number.
  env       -- Shorthand for viewing and setting environment variables.
  exit      -- Quit the LLDB debugger.
  f         -- Select the current stack frame by index from within the current thread (see 'thread backtrace'.)
  file      -- Create a target using the argument as the main executable.
  finish    -- Finish executing the current stack frame and stop after returning.  Defaults to current thread unless specified.
  image     -- Commands for accessing information for one or more target modules.
  j         -- Set the program counter to a new address.
  jump      -- Set the program counter to a new address.
  kill      -- Terminate the current target process.
  l         -- List relevant source code using one of several shorthand formats.
  list      -- List relevant source code using one of several shorthand formats.
  n         -- Source level single step, stepping over calls.  Defaults to current thread unless specified.
  next      -- Source level single step, stepping over calls.  Defaults to current thread unless specified.
  nexti     -- Instruction level single step, stepping over calls.  Defaults to current thread unless specified.
  ni        -- Instruction level single step, stepping over calls.  Defaults to current thread unless specified.
  p         -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  parray    -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  po        -- Evaluate an expression on the current thread.  Displays any returned value with formatting controlled by the type's author.
  poarray   -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  print     -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  q         -- Quit the LLDB debugger.
  r         -- Launch the executable in the debugger.
  rbreak    -- Sets a breakpoint or set of breakpoints in the executable.
  repl      -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
  run       -- Launch the executable in the debugger.
  s         -- Source level single step, stepping into calls.  Defaults to current thread unless specified.
  si        -- Instruction level single step, stepping into calls.  Defaults to current thread unless specified.
  sif       -- Step through the current block, stopping if you step directly into a function whose name matches the TargetFunctionName.
  step      -- Source level single step, stepping into calls.  Defaults to current thread unless specified.
  stepi     -- Instruction level single step, stepping into calls.  Defaults to current thread unless specified.
  t         -- Change the currently selected thread.
  tbreak    -- Set a one-shot breakpoint using one of several shorthand formats.
  undisplay -- Stop displaying expression at every stop (specified by stop-hook index.)
  up        -- Select an older stack frame.  Defaults to moving one frame, a numeric argument can specify an arbitrary number.
  x         -- Read from the memory of the current target process.
```

### 调试文件的过程

```
lldb xxxx.file
r // 执行程序，之后会开始跑程序，有些程序需要输入数据，才会开始启动
breakpoint set -f node_test.cpp -l 17

s 进入源码层
n 下一行代码，不进入源码层
```




## 脚本

### 编译运行单个c++文件

- sh xx.sh filename_without_suffix

```
cpp_file=$1
g++ $cpp_file.cpp -o $cpp_file
./$cpp_file
rm -rf $cpp_file
```






## 教你C++怎么找bug

### cout打印法

- 可能出的问题上，打印日志信息，然后后面程序运行查看信息

### 创建类出现段错误

- 一个类里面可能有多个类
- 那么这个时候要向指定哪里创建类出现问题
- 就可以单独拿出来创建查看

```
RandomAccessFileHandle::RandomAccessFileHandle(std::string& filename)
    :   filename_(filename),
        offset_(0),
        current_offset_(0),
        fd_(0),
        limiter_(nullptr),
        random_access_file_(nullptr),
        filestream_(nullptr) {
            filestream_ = fopen(filename.c_str(), "r+");
            assert(filestream_ != nullptr);
            fd_ = fileno(filestream_);
            assert(fd_ != -1);
            limiter_ = new Limiter(FLAGS_limiter_max_required);
            assert(limiter_ != nullptr);
            random_access_file_ = ibdb::log::NewRandomAccessFile(filename_, fd_, limiter_);
            assert(random_access_file_ != nullptr);
        }
        
这里有
limiter_
random_access_file_
两个类，可以单独创建定位问题
后面查出问题在
limiter_ = new Limiter(FLAGS_limiter_max_required);
limiter_不支持赋值语句!!!!
必须用列表初始化来构造Limiter对象
```

- 当然也可能是最愚蠢的问题
- 创建对象没有添加new

### 使用lldb或者gdb来查找segment fault

- 这是最有效的方法查找段错误，也就是内存错误。
- 因为可以一步一步单步调试，所以很方便
- 如何使用查询本方案目录栏

### 快速定位segment fault

```
两个print的方法
std::cout<< "ok 169" << std::endl;
std::cout<< "ok 122" << std::endl;
一头一尾，不断往中间靠拢，来定位哪一行的bug
```

