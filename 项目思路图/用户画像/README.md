## 用户画像

### 学习资料

- 用户画像是怎么生成出来的？ - 办办学苑的回答 - 知乎 https://www.zhihu.com/question/31429786/answer/417642875 
- https://www.zhihu.com/question/31429786
- https://www.jianshu.com/p/9f8a81040393









## 测试语句-针对日志回放

```
select * from   search.playbacktype where fb_query_id='75712027626627072'


select * from   search.playbacktype limit 10
select * from   search.playback limit 10

select * from search.playback where click_timestamp=1538028460006
select * from search.playback where uuid='bded08d2-f8f4-4213-b084-884df7ae76a2'
select count(*) from search.playback   9150643  9151343 10324227
select * from search.playback where pt>'2018-07-31' limit 100
select count(*) from search.playback where pt>='2018-08-07'  目前321条  412
select * from search.playbacktype where fb_query_id='75693518002647040'
select * from search.playback_all where fb_query_id='75693518002647040'

select operation_value from   search.playbacktype where operation_type=4

select * from search.playback where pt='2018-08-02' limit 10 
select * from search.playbacktype where operation_value='null' limit 10 
select * from   search.playback where  fb_query_id ='76957903493840896'




select count(*)  from   search.playbacktype where pt='2018-08-10' 3922 3804000
select count(*)  from   search.playback where pt='2018-08-08'  2988  184063 2780000
select * from   search.playbacktype where  fb_query_id ='76957903493840896'
select * from   search.playbacktype where operation_type=4 limit 10 
select count(*)  from   search.playback where summary='有点击行为'
select count(*)  from   search.playbacktype where operation_type=4
select count(*)  from   search.playbacktype where operation_value='null' and operation_type=4  173096  173837
select count(*)  from   search.playbacktype where operation_value='[]' 476734
select count(*)  from search.playback where create_timestamp=0 and pt='2018-08-01'    633241
select count(*)  from search.playback where create_timestamp!=0 and pt='2018-08-01'  
select *  from search.playback where pt='2018-08-01' limit 10 
select count(*) from search.playback where pt='2018-08-01' 
select * from search.playback where pt='0000-00-00'  limit 10

select count(*)  from search.playback where pt='0000-00-00'   1403



select  count(*) from search.playback where search_query!='null'  1120858

select count(*) from search.playback where pt<'2018-07-31' and pt>='2018-07-30'
select count(*) from search.playback where pt<='2018-07-28' 
select count(*) from search.playback where search_query!='null'   
select * from search.playback where search_query!='null' limit 100
select * from search.playback where search_query=='null' limit 100
select count(*) from search.playback where search_query==''
select  count(*) from search.playback where create_timestamp!=0 limit 100

select count(*) from search.playbacktype where operation_type=7

select count(*) from search.playbacktype where operation_value='[]'


select * from search.playbacktype where operation_value='上地' limit 10

insert into search.playback (dig_timestamp,click_housecode,fb_query_id,requestFunctionScores,queryFuzziness,search_query,fb_ab_test_flag,uuid,fb_service_id,returnRelativeScore,total,requestId,client,strategyId,cityIds,sorts,queryOperator,ucid,cost,click_fb_expo_id,search_docs,queryMinimumShouldMatch,filters,fls,search_index,route,size,page,sortedQueryMinimumShouldMatch,aggregations,qfs) values (1532876299000,'null','76085929632649217','[{"filter":{"and":[{"or":[{"field":"tags","action":"match","value":"is_vr"}]}]},"weight":1000.0}]',-1,'null','null','7d7ac5e16e61c1688553c8c97df52887','1011710017',0,334,'null','app','0','["500000"]','[{"field":"_score","order":"desc"},{"field":"houseQ","order":"desc"},{"field":"_uid","order":"asc"}]','OR','0','22','null','[{"strategy_info":{"fb_item_location":"0","fb_expo_id":"76085929641050112"}},{"strategy_info":{"fb_item_location":"1","fb_expo_id":"76085929641050113"}},{"strategy_info":{"fb_item_location":"2","fb_expo_id":"76085929641050114"}},{"strategy_info":{"fb_item_location":"3","fb_expo_id":"76085929641050115"}},{"strategy_info":{"fb_item_location":"4","fb_expo_id":"76085929641050116"}},{"strategy_info":{"fb_item_location":"5","fb_expo_id":"76085929641050117"}},{"strategy_info":{"fb_item_location":"6","fb_expo_id":"76085929641050118"}},{"strategy_info":{"fb_item_location":"7","fb_expo_id":"76085929641050119"}},{"strategy_info":{"fb_item_location":"8","fb_expo_id":"76085929641050120"}},{"strategy_info":{"fb_item_location":"9","fb_expo_id":"76085929641050121"}},{"strategy_info":{"fb_item_location":"10","fb_expo_id":"76085929641050122"}},{"strategy_info":{"fb_item_location":"11","fb_expo_id":"76085929641050123"}},{"strategy_info":{"fb_item_location":"12","fb_expo_id":"76085929641050124"}},{"strategy_info":{"fb_item_location":"13","fb_expo_id":"76085929641050125"}},{"strategy_info":{"fb_item_location":"14","fb_expo_id":"76085929641050126"}},{"strategy_info":{"fb_item_location":"15","fb_expo_id":"76085929641050127"}},{"strategy_info":{"fb_item_location":"16","fb_expo_id":"76085929641050128"}},{"strategy_info":{"fb_item_location":"17","fb_expo_id":"76085929641050129"}},{"strategy_info":{"fb_item_location":"18","fb_expo_id":"76085929641050130"}},{"strategy_info":{"fb_item_location":"19","fb_expo_id":"76085929641050131"}}]','-25%','{"and":[{"or":[{"field":"appid","action":"match","value":"104"},{"field":"appid","action":"match","value":"105"}]},{"or":[{"field":"cityId","action":"match","value":"500000"}]},{"or":[{"field":"houseType","action":"match","value":"107500000001"},{"field":"houseType","action":"match","value":"107500000002"},{"field":"houseType","action":"match","value":"107500000003"},{"field":"houseType","action":"match","value":"107500000004"},{"field":"houseType","action":"match","value":"107500000005"},{"field":"houseType","action":"match","value":"107500000009"},{"field":"houseType","action":"match","value":"107500000010"},{"field":"houseType","action":"match","value":"107500000012"},{"field":"houseType","action":"match","value":"107500000013"},{"field":"houseType","action":"match","value":"107500000014"},{"field":"houseType","action":"match","value":"107500000015"},{"field":"houseType","action":"match","value":"107500000017"},{"field":"houseType","action":"match","value":"107599999998"}]},{"or":[{"field":"priceTotal","action":"range","value":"[60,80)"}]},{"or":[{"field":"bedroomNum","action":"match","value":"2"},{"field":"bedroomNum","action":"match","value":"3"},{"field":"bedroomNum","action":"match","value":"4"}]},{"or":[{"field":"hasElevator","action":"match","value":"1"}]}]}','["houseCode"]','1011710017','null',20,1,'1','[]','["title","houseCode","resblockName"]');



SELECT
    table,
    formatReadableSize(sum(bytes)) AS size,
    min(min_date) AS min_date,
    max(max_date) AS max_date
FROM system.parts
WHERE active
GROUP BY table



```

