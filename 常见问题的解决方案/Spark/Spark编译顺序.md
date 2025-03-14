## 开发
1. https://github.dev/apache/spark
```
mvn -DskipTests clean package > spark.log

```

## 编译包
```

[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Build Order:
[INFO] 
[INFO] Spark Project Parent POM                                           [pom]
[INFO] Spark Project Tags                                                 [jar]
[INFO] Spark Project Sketch                                               [jar]
[INFO] Spark Project Local DB                                             [jar]
[INFO] Spark Project Networking                                           [jar]
[INFO] Spark Project Shuffle Streaming Service                            [jar]
[INFO] Spark Project Unsafe                                               [jar]
[INFO] Spark Project Launcher                                             [jar]
[INFO] Spark Project Core                                                 [jar]
[INFO] Spark Project ML Local Library                                     [jar]
[INFO] Spark Project GraphX                                               [jar]
[INFO] Spark Project Streaming                                            [jar]
[INFO] Spark Project Catalyst                                             [jar]
[INFO] Spark Project SQL                                                  [jar]
[INFO] Spark Project ML Library                                           [jar]
[INFO] Spark Project Tools                                                [jar]
[INFO] Spark Project Hive                                                 [jar]
[INFO] Spark Project REPL                                                 [jar]
[INFO] Spark Project Assembly                                             [pom]
[INFO] Kafka 0.10+ Token Provider for Streaming                           [jar]
[INFO] Spark Integration for Kafka 0.10                                   [jar]
[INFO] Kafka 0.10+ Source for Structured Streaming                        [jar]
[INFO] Spark Project Examples                                             [jar]
[INFO] Spark Integration for Kafka 0.10 Assembly                          [jar]
[INFO] Spark Avro                                                         [jar]
[INFO] 
[INFO] -----------------< org.apache.spark:spark-parent_2.12 >-----------------
[INFO] Building Spark Project Parent POM 3.1.4-SNAPSHOT                  [1/25]
[INFO] --------------------------------[ pom ]---------------------------------
[INFO] 


[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary for Spark Project Parent POM 3.0.1:
[INFO] 
[INFO] Spark Project Parent POM ........................... SUCCESS [ 23.721 s]
[INFO] Spark Project Tags ................................. SUCCESS [ 10.784 s]
[INFO] Spark Project Sketch ............................... SUCCESS [  4.177 s]
[INFO] Spark Project Local DB ............................. SUCCESS [  1.018 s]
[INFO] Spark Project Networking ........................... SUCCESS [  2.669 s]
[INFO] Spark Project Shuffle Streaming Service ............ SUCCESS [  0.788 s]
[INFO] Spark Project Unsafe ............................... SUCCESS [  5.399 s]
[INFO] Spark Project Launcher ............................. SUCCESS [  8.413 s]
[INFO] Spark Project Core ................................. SUCCESS [01:39 min]
[INFO] Spark Project ML Local Library ..................... SUCCESS [ 25.422 s]
[INFO] Spark Project GraphX ............................... SUCCESS [ 30.981 s]
[INFO] Spark Project Streaming ............................ SUCCESS [ 51.274 s]
[INFO] Spark Project Catalyst ............................. SUCCESS [01:56 min]
[INFO] Spark Project SQL .................................. SUCCESS [03:57 min]
[INFO] Spark Project ML Library ........................... SUCCESS [02:31 min]
[INFO] Spark Project Tools ................................ SUCCESS [  3.666 s]
[INFO] Spark Project Hive ................................. SUCCESS [ 58.228 s]
[INFO] Spark Project REPL ................................. SUCCESS [ 13.596 s]
[INFO] Spark Project Assembly ............................. SUCCESS [  2.059 s]
[INFO] Kafka 0.10+ Token Provider for Streaming ........... SUCCESS [ 15.543 s]
[INFO] Spark Integration for Kafka 0.10 ................... SUCCESS [ 21.095 s]
[INFO] Kafka 0.10+ Source for Structured Streaming ........ SUCCESS [ 35.188 s]
[INFO] Spark Project Examples ............................. SUCCESS [ 26.068 s]
[INFO] Spark Integration for Kafka 0.10 Assembly .......... SUCCESS [  4.116 s]
[INFO] Spark Avro ......................................... SUCCESS [ 28.255 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  16:18 min
[INFO] Finished at: 2024-12-06T20:16:08+08:00
[INFO] ------------------------------------------------------------------------


```