## C++常用代码段

### 打印时间

- http://www.cnblogs.com/mfryf/archive/2012/02/13/2349360.html

```
#include <iostream>
#include <ctime>
using namespace std;
int main()
{
    time_t now_time;
    now_time = time(NULL);
    cout<<now_time;
    return 0;
}
```

### 打印毫秒级别的时间

- 资料
  - <https://stackoverflow.com/questions/19555121/how-to-get-current-timestamp-in-milliseconds-since-1970-just-the-way-java-gets>
- 文档
  - <https://en.cppreference.com/w/cpp/chrono>
  - <https://blog.csdn.net/u013390476/article/details/50209603>
  - <https://www.jianshu.com/p/80de04b41c31>
- 时间戳转换工具：<https://tool.lu/timestamp/>

```
#include <chrono> // for timestamp

static inline uint64_t GetMillisecondTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count();
    return ts;
}

static inline uint64_t GetMicrosecondsTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::microseconds>(now.time_since_epoch()).count();
    return ts;
}

static inline uint64_t GetSecondTimestamp() {
    auto now = std::chrono::system_clock::now();
    uint64_t ts = (uint64_t)std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count();
    return ts;
}
```



### 数字转字节

- 这个超级常用，数字写入文件的时候一定要压缩到规定4字节或者8字节。这样就能按字节大小读出文件

- 如果直接写数字到文件里面，那么就是1个数字符号1个字节。根本没有办法规定大小读取数字！！！

- 这个弄了我一个下午，后面发现levelDB里面

- ```c++
  inline void EncodeFixed32(char* buf, uint32_t value) {
      if (kLittleEndian) {
          memcpy(buf, &value, sizeof(value));
      } else {
          buf[0] = value & 0xff;
          buf[1] = (value >> 8) & 0xff;
          buf[2] = (value >> 16) & 0xff;
          buf[3] = (value >> 24) & 0xff;
      }
  }
  
  inline void EncodeFixed64(char* buf, uint64_t value) {
      if (kLittleEndian) {
          memcpy(buf, &value, sizeof(value));
      } else {
          buf[0] = value & 0xff;
          buf[1] = (value >> 8) & 0xff;
          buf[2] = (value >> 16) & 0xff;
          buf[3] = (value >> 24) & 0xff;
          buf[4] = (value >> 32) & 0xff;
          buf[5] = (value >> 40) & 0xff;
          buf[6] = (value >> 48) & 0xff;
          buf[7] = (value >> 56) & 0xff;
      }
  }
  
  inline uint32_t DecodeFixed32(const char* ptr) {
      if (kLittleEndian) {
          // Load the raw bytes
          uint32_t result;
          memcpy(&result, ptr, sizeof(result));  // gcc optimizes this to a plain load
          return result;
      } else {
          return ((static_cast<uint32_t>(static_cast<unsigned char>(ptr[0])))
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[1])) << 8)
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[2])) << 16)
          | (static_cast<uint32_t>(static_cast<unsigned char>(ptr[3])) << 24));
      }
  }
  
  inline uint64_t DecodeFixed64(const char* ptr) {
      if (kLittleEndian) {
          // Load the raw bytes
          uint64_t result;
          memcpy(&result, ptr, sizeof(result));  // gcc optimizes this to a plain load
          return result;
      } else {
          uint64_t lo = DecodeFixed32(ptr);
          uint64_t hi = DecodeFixed32(ptr + 4);
          return (hi << 32) | lo;
      }
  }
  ```

### 打印人类可读的存储大小

```
tensorflow/stream_executor代码中看到的
static string ToString(int64 num_bytes) {
    if (num_bytes == std::numeric_limits<int64>::min()) {
      // Special case for number with not representable nagation.
      return "-8E";
    }

    const char* neg_str = GetNegStr(&num_bytes);

    // Special case for bytes.
    if (num_bytes < 1024LL) {
      // No fractions for bytes.
      return port::Printf("%s%lldB", neg_str, num_bytes);
    }

    static const char units[] = "KMGTPE";  // int64 only goes up to E.
    const char* unit = units;
    while (num_bytes >= (1024LL) * (1024LL)) {
      num_bytes /= (1024LL);
      ++unit;
      assert(unit < units + sizeof(units));
    }

    return port::Printf(((*unit == 'K') ? "%s%.1f%c" : "%s%.2f%c"), neg_str,
                        num_bytes / 1024.0, *unit);
  }
  
  template <typename T>
  static const char* GetNegStr(T* value) {
    if (*value < 0) {
      *value = -(*value);
      return "-";
    } else {
      return "";
    }
  }
```



### 大小端检查

```c++
typedef signed char           int8_t;
typedef signed short          int16_t;
typedef signed int            int32_t;
typedef signed long long      int64_t;
typedef unsigned char         uint8_t;
typedef unsigned short        uint16_t;
typedef unsigned int          uint32_t;
typedef unsigned long long    uint64_t;
namespace ibdb {
namespace port {

inline const bool IsLittleEndian() {
    int a = 1;
    if (*(char*)&a == 1) {
      return true;
    } else {
      return false;
    }
}

static const bool kLittleEndian = IsLittleEndian();
```

### 字符串切割

```
inline void Split(const string& src, vector<string>& res, const string& pattern, size_t maxsplit = string::npos) {
  res.clear();
  size_t Start = 0;
  size_t end = 0;
  string sub;
  while(Start < src.size()) {
    end = src.find_first_of(pattern, Start);
    if(string::npos == end || res.size() >= maxsplit) {
      sub = src.substr(Start);
      res.push_back(sub);
      return;
    }
    sub = src.substr(Start, end - Start);
    res.push_back(sub);
    Start = end + 1;
  }
  return;
}
```

### 字母大小写

```
inline string& Upper(string& str) {
  transform(str.begin(), str.end(), str.begin(), (int (*)(int))toupper);
  return str;
}

inline string& Lower(string& str) {
  transform(str.begin(), str.end(), str.begin(), (int (*)(int))tolower);
  return str;
}
```

### 字符串拼接

```
template<class T>
void Join(T begin, T end, string& res, const string& connector) {
  if(begin == end) {
    return;
  }
  stringstream ss;
  ss<<*begin;
  begin++;
  while(begin != end) {
    ss << connector << *begin;
    begin ++;
  }
  res = ss.str();
}
```

### 数据类型的最大最小值

```
http://www.cplusplus.com/reference/climits/


```

### 打印服务器配置

```
#if defined(__linux)
    time_t now = time(nullptr);
    fprintf(stderr, "Date:       %s", ctime(&now));  // ctime() adds newline

    FILE* cpuinfo = fopen("/proc/cpuinfo", "r");
    if (cpuinfo != nullptr) {
      char line[1000];
      int num_cpus = 0;
      std::string cpu_type;
      std::string cache_size;
      while (fgets(line, sizeof(line), cpuinfo) != nullptr) {
        const char* sep = strchr(line, ':');
        if (sep == nullptr) {
          continue;
        }
        Slice key = TrimSpace(Slice(line, sep - 1 - line));
        Slice val = TrimSpace(Slice(sep + 1));
        if (key == "model name") {
          ++num_cpus;
          cpu_type = val.ToString();
        } else if (key == "cache size") {
          cache_size = val.ToString();
        }
      }
      fclose(cpuinfo);
      fprintf(stderr, "CPU:        %d * %s\n", num_cpus, cpu_type.c_str());
      fprintf(stderr, "CPUCache:   %s\n", cache_size.c_str());
    }
#endif

这里要切割根据空格字符串
#if defined(__linux)
static Slice TrimSpace(Slice s) {
  size_t start = 0;
  while (start < s.size() && isspace(s[start])) {
    start++;
  }
  size_t limit = s.size();
  while (limit > start && isspace(s[limit-1])) {
    limit--;
  }
  return Slice(s.data() + start, limit - start);
}
#endif
```

### 单例模式

```

static Classxxxx& singleton() {
        static Classxxxx classxxxx;
        return classxxxx;
}

```

### 编译c++文件

```
编译
g++ xxx.cpp -o xxx
执行
./xxx
```
