## 说明

## 目录

[TOC]



## Java解决方案



### 异常

#### 并发

- java.util.concurrent.TimeoutException
  - http://www.blogjava.net/xylz/archive/2011/07/12/354206.html	
  - 此异常是用来描述任务执行时间超过了期望等待时间，也许是一直没有获取到锁，也许是还没有执行完成。





### 代码规范

- 类名：每个单词首字母大写
- 方法名：动词+名词，动词小写，名词首字母大写
- 变量名：名词，首字母小写，多个单词的话，在后面单词每个首字母大写







### maven

- 发布jar包，跳过测试单元
  -  mvn install -Dmaven.test.skip=true