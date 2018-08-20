## ElasticSearch

### 说明

- ES学习笔记
- 学习建议
- 多动手
- 多尝试



## Basic Concepts

### cluster  

- A cluster is a collection of one or more nodes (servers) that together holds your entire data and provides federated indexing and search capabilities across all nodes .



### node  

- A node is a single server that is part of your cluster, stores your data, and participates in the cluster’s indexing and search capabilities. 
- Just like a cluster, a node is identified by a name which by default is a random Universally Unique IDentifier (UUID) that is assigned to the node at startup.

### index  

- An index is a collection of documents that have somewhat similar characteristics. 



### document 

- A document is a basic unit of information that can be indexed. For example, you can have a document for a single customer, another document for a single product, and yet another for a single order. 

### shard  

- Elasticsearch provides the ability to subdivide your index into multiple pieces called shards.  
- Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster. 
- function
  - It allows you to horizontally split/scale your content volume
  - It allows you to distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput



### replica  

- Elasticsearch allows you to make one or more copies of your index’s shards into what are called replica shards, or replicas for short. 

- funciton

  - It provides high availability in case a shard/node fails. For this reason, it is important to note that a replica shard is never allocated on the same node as the original/primary shard that it was copied from.
  - It allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel.

   

### One more thing

- By default, each index in Elasticsearch is allocated 5 primary shards and 1 replica which means that if you have at least two nodes in your cluster, your index will have 5 primary shards and another 5 replica shards (1 complete replica) for a total of 10 shards per index. 



## Installation

- 下载：curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.0.1.tar.gz
- 解压：tar -xvf elasticsearch-6.0.1.tar.gz
- 进入执行目录：cd elasticsearch-6.0.1/bin
- 执行脚本：./elasticsearch



## Use The Rest API



- Check your cluster, node, and index health, status, and statistics

  - 检查服务器健康状况：curl -X GET "localhost:9200/_cat/health?v"
  - 查询所有节点运行情况：curl -X GET "localhost:9200/_cat/nodes?v"
  - Green - everything is good (cluster is fully functional)
  - Yellow - all data is available but some replicas are not yet allocated (cluster is fully functional)
  - Red - some data is not available for whatever reason (cluster is partially functional)

- Administer your cluster, node, and index data and metadata

- Perform CRUD (Create, Read, Update, and Delete) and search operations against your indexes

- Execute advanced search operations such as paging, sorting, filtering, scripting, aggregations, and many others

- LIst All indices

  - 列出所有索引情况：curl -X GET "localhost:9200/_cat/indices?v"

- Create an Index

  - curl -X PUT "localhost:9200/customer?pretty"
    curl -X GET "localhost:9200/_cat/indices?v"

- Create an index with document

  - curl -X PUT "localhost:9200/customer/doc/1?pretty" -H 'Content-Type: application/json' -d'
    {
      "name": "John Doe"
    }'
  - 搜索该文档：curl -X GET "localhost:9200/customer/doc/1?pretty"

- Delete an Index

  - curl -X DELETE "localhost:9200/customer?pretty"
    curl -X GET "localhost:9200/_cat/indices?v"
  - curl -X PUT "localhost:9200/customer"
    curl -X PUT "localhost:9200/customer/doc/1" -H 'Content-Type: application/json' -d'
    {
      "name": "John Doe"
    }
    '
    curl -X GET "localhost:9200/customer/doc/1"
    curl -X DELETE "localhost:9200/customer"

- 后面使用kibana平台，来执行命令。更方便，也更好用

- Modifying Your Data

  - ```json
    创建数据
    PUT /customer/doc/1?pretty
    {
      "name": "Jane Doe"
    }
    PUT /customer/doc/2?pretty
    {
      "name": "Jane Doe"
    }
    ```

  - ```json
    创建数据并随机生产ID
    POST /customer/doc?pretty
    {
      "name": "Jane Doe"
    }
    ```




```json
更新文档数据
POST /customer/doc/1/_update?pretty
{
  "doc": { "name": "Jane Doe" }
}
增加文档内容
POST /customer/doc/1/_update?pretty
{
  "doc": { "name": "Jane Doe", "age": 20 }
}
对age字段加5，数值类型才行， the current source document当前文档内容

POST /customer/doc/1/_update?pretty
{
  "script" : "ctx._source.age += 5"
}
删除文档
DELETE /customer/doc/2?pretty




```



### 批量处理

- https://www.elastic.co/guide/en/elasticsearch/reference/6.0/_batch_processing.html

- https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json

- ```
  curl -H "Content-Type: application/json" -XPOST 'localhost:9200/bank/account/_bulk?pretty&refresh' --data-binary "https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json"
  ```

   

### 搜索API

- GET /bank/_search?q=*&sort=account_number:asc&pretty

- ```
  GET /bank/_search
  {
    "query": { "match_all": {} },
    "sort": [
      { "account_number": "asc" }
    ]
  }
  ```

### the Query Language

- 匹配所有的结果
  - GET /bank/_search
    {
    "query": { "match_all": {} }
    }

- 返回的结果，只显示size数量的条数
  - GET /bank/_search
    {
    "query": { "match_all": {} },
    "size": 1
    }

- 返回的数量，从指定的位置开始。类似sql的offset
  - ```
    GET /bank/_search
    {
      "query": { "match_all": {} },
      "from": 10,
      "size": 10
    }
    ```

- 按指定顺序排序

  - ```
    GET /bank/_search
    {
      "query": { "match_all": {} },
      "sort": { "balance": { "order": "desc" } }
    }
    ```

- https://www.elastic.co/guide/en/elasticsearch/reference/current/_executing_searches.html


- 更多查询参考上面链接

  ### 聚合查询

  - https://www.elastic.co/guide/en/elasticsearch/reference/current/_executing_aggregations.html