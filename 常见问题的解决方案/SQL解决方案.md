## SQL解决方案

- 针对 SQL方面的问题进行深入探讨

### 资料

- SQL 语法教程：https://www.w3schools.com/sql/default.asp



### 语法问题

#### 左连接，右连接和内连接到区别

- https://blog.csdn.net/hj7jay/article/details/51749863
- tableA left join tableB on a.id = b.id
  - 把tableA全写下来，然后找B有无对应，有则赋值，没有则赋null
- tableA right join tableB on a.id = b.id
  - 把tableB全写下来，然后找A有无对应，有则赋值，没有则赋null
- tableA inner join tableB on a.id = b.id
  - 找A和B都存在的都相等的值才行
- tableA full join tableB on a.id = b.id
  - A和B全部写下来，有对应的合并成一条，没有对应的直接赋Null



#### 针对某个字段去重distinct

- select distinct SK_ID_BUREAU,MONTHS_BALANCE,STATUS from t2
- 使用例子：https://blog.csdn.net/boss2967/article/details/79019467



### 注意事项

#### 左连接问题

- 两张表要保证对应的字段是1：1。而不能出现1：N，或者 N：1
  - https://blog.csdn.net/fdipzone/article/details/45119551
- 问题发现来源：https://mapr.com/community/s/question/0D50L00006BItfbSAD/null-pointer-error-at-spark-count