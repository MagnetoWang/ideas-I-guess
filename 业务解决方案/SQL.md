
## 参考
```
大数据私房菜公众号
https://mp.weixin.qq.com/s/Ki-x9NlUu2RWj4uFDt1NPA

```

## 面试题
### 同时最大在线人数问题
```
问题：如下为某直播平台各主播的开播及关播时间明细数据，现在需要计算出该平台最高峰期同时在线的主播人数。

user_id     start_date              end_date
1001    2021-06-14 12:12:12     2021-06-14 18:12:12
1003    2021-06-14 13:12:12     2021-06-14 16:12:12
1004    2021-06-14 13:15:12     2021-06-14 20:12:12
1002    2021-06-14 15:12:12     2021-06-14 16:12:12
1005    2021-06-14 15:18:12     2021-06-14 20:12:12
1001    2021-06-14 20:12:12     2021-06-14 23:12:12
1006    2021-06-14 21:12:12     2021-06-14 23:15:12
1007    2021-06-14 22:12:12     2021-06-14 23:10:12
SQL解答：

这是非常经典的一个面试题，不管大厂小厂都有问到过。解题思路也比较固定：就是用1代表开播(此时用开播时间)，-1代表关播(此时用关播时间)，然后开窗可以计算出到每个时间点时有多少主播同时在线，最后求最大值即可。

with tmp as
(
    select 1001 as user_id, '2021-06-14 12:12:12' as start_date , '2021-06-14 18:12:12' as end_date
    union all
    select 1003 as user_id, '2021-06-14 13:12:12' as start_date , '2021-06-14 16:12:12' as end_date
    union all
    select 1004 as user_id, '2021-06-14 13:15:12' as start_date , '2021-06-14 20:12:12' as end_date
    union all
    select 1002 as user_id, '2021-06-14 15:12:12' as start_date , '2021-06-14 16:12:12' as end_date
    union all
    select 1005 as user_id, '2021-06-14 15:18:12' as start_date , '2021-06-14 20:12:12' as end_date
    union all
    select 1001 as user_id, '2021-06-14 20:12:12' as start_date , '2021-06-14 23:12:12' as end_date
    union all
    select 1006 as user_id, '2021-06-14 21:12:12' as start_date , '2021-06-14 23:15:12' as end_date
    union all
    select 1007 as user_id, '2021-06-14 22:12:12' as start_date , '2021-06-14 23:10:12' as end_date
)
select
max(online_nums) as max_online_nums
from
(
    select
    user_id
    ,dt
    ,sum(flag) over(order by dt) as online_nums
    from
    (
        select
        user_id
        ,start_date as dt
        ,1 as flag  --开播记为1
        from tmp
        union all
        select
        user_id
        ,end_date as dt
        ,-1 as flag --关播记为-1
        from tmp
    )t1
)t1
;



```

### 打折日期交叉问题
```
问题：如下为某平台的商品促销数据，字段含义分别为品牌名称、打折开始日期、打折结束日期，现在要计算每个品牌的打折销售天数（注意其中的交叉日期）。比如vivo的打折销售天数就为17天。

brand   start_date  end_date
xiaomi  2021-06-05  2021-06-09
xiaomi  2021-06-11  2021-06-21
vivo    2021-06-05  2021-06-15
vivo    2021-06-09  2021-06-21 
honor   2021-06-05  2021-06-21 
honor   2021-06-09  2021-06-15
redmi   2021-06-17  2021-06-26
huawei  2021-06-05  2021-06-26
huawei  2021-06-09  2021-06-15
huawei  2021-06-17  2021-06-21
SQL解答：

第一种方式：根据每个品牌的促销开始时间和结束时间可以得到品牌每天促销的明细数据，然后，按品牌分组，日期去重就可以得到每个品牌打折销售天数。但此种方式适合数据量不大的情况，因为该方法会让数据膨胀的很厉害。

select
brand
,count(distinct dt) as dts
from
(
    select
    brand
    ,start_date
    ,end_date
    ,date_add(start_date,tmp.col_idx) as dt
    from
    (
        select 'xiaomi' as brand   ,'2021-06-05' as start_date,'2021-06-09' as end_date
        union all
        select 'xiaomi' as brand   ,'2021-06-11' as start_date,'2021-06-21' as end_date
        union all
        select 'vivo' as brand   ,'2021-06-05' as start_date,'2021-06-15' as end_date
        union all
        select 'vivo' as brand   ,'2021-06-09' as start_date,'2021-06-21' as end_date
        union all 
        select 'honor' as brand  ,'2021-06-05' as start_date,'2021-06-21' as end_date
        union all 
        select 'honor' as brand  ,'2021-06-09' as start_date,'2021-06-15' as end_date
        union all
        select 'honor' as brand  ,'2021-06-17' as start_date,'2021-06-26' as end_date
        union all
        select 'huawei' as brand ,'2021-06-05' as start_date,'2021-06-26' as end_date
        union all
        select 'huawei' as brand ,'2021-06-09' as start_date,'2021-06-15' as end_date
        union all
        select 'huawei' as brand ,'2021-06-17' as start_date,'2021-06-21' as end_date
    )t1
    lateral VIEW posexplode(split(repeat("#,",datediff(date(end_date), date(start_date))),'#')) tmp AS col_idx,col_val
)t1
group by brand
;

第二种方式：规避数据膨胀的情况，经过适当的处理，消除日期交叉的情况

select
brand
,sum(DATEDIFF(date(end_date),date(start_date),'dd')+1)
from
(
    select
    brand
    ,case
    when start_date<=max_date then dateadd(date(max_date),1,'dd')
    else start_date end
    as start_date
    ,end_date
    from
    (
        select
        brand
        ,start_date
        ,end_date
        ,max(end_date) over(partition by brand order by start_date rows between UNBOUNDED PRECEDING and 1 PRECEDING ) as max_date  --获取同一品牌内按开始日期排序后，取第一行到前一行的最大结束时间
        from
        (
            select 'xiaomi' as brand   ,'2021-06-05' as start_date,'2021-06-09' as end_date
            union all
            select 'xiaomi' as brand   ,'2021-06-11' as start_date,'2021-06-21' as end_date
            union all
            select 'oppo' as brand   ,'2021-06-23' as start_date,'2021-06-25' as end_date
            union all
            select 'vivo' as brand   ,'2021-06-05' as start_date,'2021-06-15' as end_date
            union all
            select 'vivo' as brand   ,'2021-06-09' as start_date,'2021-06-21' as end_date
            union all 
            select 'honor' as brand  ,'2021-06-05' as start_date,'2021-06-21' as end_date
            union all 
            select 'honor' as brand  ,'2021-06-09' as start_date,'2021-06-15' as end_date
            union all
            select 'honor' as brand  ,'2021-06-17' as start_date,'2021-06-26' as end_date
            union all
            select 'huawei' as brand ,'2021-06-05' as start_date,'2021-06-26' as end_date
            union all
            select 'huawei' as brand ,'2021-06-09' as start_date,'2021-06-15' as end_date
            union all
            select 'huawei' as brand ,'2021-06-17' as start_date,'2021-06-21' as end_date
            union all
            select 'apple' as brand ,'2021-06-18' as start_date,'2021-06-21' as end_date
            union all
            select 'apple' as brand ,'2021-06-20' as start_date,'2021-06-22' as end_date
        )t1
    )t1
)t1
where end_date>=start_date
group by brand
;

```


### 奖金瓜分问题(拼多多)
```
问题：在活动大促中，有玩游戏瓜分奖金环节。现有奖金池为3000元，代表奖金池中的初始额度。用户的分数信息如下：

user_id  score
101       45
102       40
103       35
104       30
105       25
表中的数据代表每一个用户和其对应的得分，user_id和score都不会有重复值。瓜分奖金的规则如下：按照score从高到低依次瓜分，每个人都能分走当前奖金池里面剩余奖金的一半，当奖金池里面剩余的奖金少于500时（不含），则停止瓜分奖金。

现在需要查询出所有分到奖金的user_id和其对应的奖金。

SQL解答：

这是拼多多的一个面试题，需要先进行一点数学层面的分析，把整个瓜分逻辑捋清楚之后不难。这里给出一种思考逻辑：假设奖金池的初始总奖金为n，那么第一名分到的奖金为n/2，第二名分到奖金n/4，第三名分到的奖金为n/8，依次类推第x名分到的奖金为n/2^x，然后计算即可。

select
user_id
,score
,1/power(2,rn)*3000 as prize
from
(
    select
    user_id
    ,score
    ,row_number() over(order by score desc) as rn
    from
    (
        select 101 as user_id,45 as score
        union all
        select 102 as user_id,40 as score
        union all
        select 103 as user_id,35 as score
        union all
        select 104 as user_id,30 as score
        union all
        select 105 as user_id,25 as score
    )t1
)t1
where 1/power(2,rn)*3000>=250
;

```

### 找出恶意购买用户
```
问题：下面是某电商网站的订单数据，包括order_id,user_id,order_status和operate_time四个字段，我们需要找出所有恶意购买的用户。恶意购买的用户定义是：同一个用户，在任意半小时内（含），取消订单次数>=3次的就被视为恶意买家。比如该样例数据中b用户就是恶意买家。

order_id    user_id    order_status     operate_time
1101         a         已支付        2023-01-01 10:00:00
1102         a         已取消        2023-01-01 10:10:00
1103         a         待支付        2023-01-01 10:20:00
1104         b         已取消        2023-01-01 10:30:00
1105         a         待确认        2023-01-01 10:50:00
1106         a         已取消        2023-01-01 11:00:00
1107         b         已取消        2023-01-01 11:40:00
1108         b         已取消        2023-01-01 11:50:00
1109         b         已支付        2023-01-01 12:00:00
1110         b         已取消        2023-01-01 12:11:00
1111         c         已取消        2023-01-01 12:20:00
1112         c         已取消        2023-01-01 12:30:00
1113         c         已取消        2023-01-01 12:55:00
1114         c         已取消        2023-01-01 13:00:00
SQL解答：

典型的滑动窗口的场景。可能我们平常在Flink中听滑动窗口比较多，其实Hive中也是有滑动窗口的功能的（按数据范围开窗）。针对这个例子，窗口大小就是半小时，然后按每条数据进行滑动，在窗口内判断该条数据对应的用户是否是恶意用户。

#这里设定tmp表中放的就是上面提供的样例数据
select
distinct user_id
from
(
    select
    order_id
    ,user_id
    ,order_status
    --通过range between以当前行为锚点，圈定数据范围为operate_time为近30分钟内，然后算该范围内的取消订单数
    ,count(case when order_status='已取消' then order_id end) over(partition by user_id order by operate_time range between 30*60 preceding and current row) as cancel_order_cnt
    from
    (
        select
        order_id
        ,user_id
        ,order_status
        ,unix_timestamp(operate_time) as operate_time  ---由于range...between只能整数比较，这里先转换为秒
        from tmp
    )t1
)t1
where cancel_order_cnt>=3
;


函数补充：关于range between...and...函数，表示以当前行为锚点，根据order by排序的字段和between...and给定的值得到窗口的上下界，从而圈定好窗口范围。比如count(distinct stu_id) over(partition by class_id order by score range between 30 and current row)就表示按class_id分组，按照score升序，以当前行为锚点，在[score-30，score]的分数范围内计算stu_id的数量。与rows不同的是，这个每一行的开窗的范围是固定的，但行数是不固定的。

```


### 
```


```


### 互相关注的人
```
问题：现在有一张relation表，里面只有两个字段：from_user和to_user，代表关注关系从from指向to，即from_user关注了to_user。现在要找出互相关注的所有人。

from_user    to_user
乔峰            段誉
乔峰            虚竹
虚竹            乔峰
徐风年          徐骁
徐骁            徐风年


SQL解答：

解答思路一：使用自关联即可，这种方式简单也最易理解。适合数据量不是很大的情况，因为会导致数据膨胀。

with tmp as
(
    select "乔峰" as from_user,"段誉" as to_user
    union all
    select "乔峰" as from_user,"虚竹" as to_user
    union all
    select "虚竹" as from_user,"乔峰" as to_user
    union all
    select "徐风年" as from_user,"徐骁" as to_user
    union all
    select "徐骁" as from_user,"徐风年" as to_user
)
select
a.from_user,
a.to_user,
if(b.from_user is not null, 1, 0) as is_friend -- 1：互相关注 
from tmp a
left join tmp b
on a.from_user=b.to_user and a.to_user=b.from_user
;
解答思路二：找到互相关注的人的规律，当他们是互相关注时，那么将from_user和to_user其中一个顺序调换位置后，from_user和to_user就一定会出现两条数据(源表提前已经去重)，所有出现两条数据的人就是有互相关注的。这种方式不会导致数据膨胀。

with tmp as
(
    select "乔峰" as from_user,"段誉" as to_user
    union all
    select "乔峰" as from_user,"虚竹" as to_user
    union all
    select "虚竹" as from_user,"乔峰" as to_user
    union all
    select "徐风年" as from_user,"徐骁" as to_user
    union all
    select "徐骁" as from_user,"徐风年" as to_user
)
select
from_user
,to_user
,count(1) over(partition by feature) as is_friend ---1：不是 2：是
from
(
    select
    from_user
    ,to_user
    --当有互相关注时，保证只将其中的一对用户调换from_user和to_user并拼接
    ,if(from_user>to_user,concat(from_user,to_user),concat(to_user,from_user)) as feature
    from tmp
)t1
;

```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```


### 
```


```



