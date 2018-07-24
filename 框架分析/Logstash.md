![测试文档](https://github.com/MagnetoWang/ideas-I-guess/blob/master/markdown-for-document-organization-management/manage-pictures/logstash.png)



[TOC]

## Logstash

### 学习的过程

#### Choose Your Stash[edit](https://github.com/elastic/logstash/edit/6.3/docs/static/introduction.asciidoc)

Route your data where it matters most. Unlock various downstream analytical and operational use cases by storing, analyzing, and taking action on your data.

**Analysis**

- [Elasticsearch](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-elasticsearch.html)
- Data stores such as [MongoDB](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-mongodb.html) and [Riak](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-riak.html)

**Archiving**

- [HDFS](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-webhdfs.html)
- [S3](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-s3.html)

**Monitoring**

- [Nagios](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-nagios.html)
- [Ganglia](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-ganglia.html)
- [Zabbix](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-zabbix.html)
- [Graphite](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-graphite.html)
- [Datadog](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-datadog.html)
- [CloudWatch](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-cloudwatch.html)

**Alerting**

- [Watcher](https://www.elastic.co/products/watcher) with Elasticsearch
- [Email](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-email.html)
- [Pagerduty](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-pagerduty.html)
- [IRC](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-irc.html)
- [SNS](http://www.elastic.co/guide/en/logstash/6.3/plugins-outputs-sns.html)



#### 文件目录说明

| Type         | Description                                                  | Default Location                                             | Setting         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- |
| **home**     | Home directory of the Logstash installation.                 | `{extract.path}- Directory created by unpacking the archive` |                 |
| **bin**      | Binary scripts, including `logstash` to start Logstash and `logstash-plugin` to install plugins | `{extract.path}/bin`                                         |                 |
| **settings** | Configuration files, including `logstash.yml` and `jvm.options` | `{extract.path}/config`                                      | `path.settings` |
| **logs**     | Log files                                                    | `{extract.path}/logs`                                        | `path.logs`     |
| **plugins**  | Local, non Ruby-Gem plugin files. Each plugin is contained in a subdirectory. Recommended for development only. | `{extract.path}/plugins`                                     | `path.plugins`  |
| **data**     | Data files used by logstash and its plugins for any persistence needs. | `{extract.path}/data`                                        | `path.data`     |



#### 配置文件结构

- 我们大部分工作是在配置文件中操作。
- 配置文件名统一用logstash.conf。并且放在bin目录文件夹下
- 执行命令：.\logstash -f logstash.conf

##### 结构

```
# This is a comment. You should use comments to describe
# parts of your configuration.
input {
  ...
}

filter {
  ...
}

output {
  ...
}
```

##### 插件配置

```
input {
  file {
    path => "/var/log/messages"
    type => "syslog"
  }

  file {
    path => "/var/log/apache/access.log"
    type => "apache"
  }
}
```

##### 核心在过滤中

- 过滤插件

| Plugin                                                       | Description                                                  | Github repository                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [aggregate](https://www.elastic.co/guide/en/logstash/current/plugins-filters-aggregate.html) | Aggregates information from several events originating with a single task | [logstash-filter-aggregate](https://github.com/logstash-plugins/logstash-filter-aggregate) |
| [alter](https://www.elastic.co/guide/en/logstash/current/plugins-filters-alter.html) | Performs general alterations to fields that the `mutate` filter does not handle | [logstash-filter-alter](https://github.com/logstash-plugins/logstash-filter-alter) |
| [cidr](https://www.elastic.co/guide/en/logstash/current/plugins-filters-cidr.html) | Checks IP addresses against a list of network blocks         | [logstash-filter-cidr](https://github.com/logstash-plugins/logstash-filter-cidr) |
| [cipher](https://www.elastic.co/guide/en/logstash/current/plugins-filters-cipher.html) | Applies or removes a cipher to an event                      | [logstash-filter-cipher](https://github.com/logstash-plugins/logstash-filter-cipher) |
| [clone](https://www.elastic.co/guide/en/logstash/current/plugins-filters-clone.html) | Duplicates events                                            | [logstash-filter-clone](https://github.com/logstash-plugins/logstash-filter-clone) |
| [csv](https://www.elastic.co/guide/en/logstash/current/plugins-filters-csv.html) | Parses comma-separated value data into individual fields     | [logstash-filter-csv](https://github.com/logstash-plugins/logstash-filter-csv) |
| [date](https://www.elastic.co/guide/en/logstash/current/plugins-filters-date.html) | Parses dates from fields to use as the Logstash timestamp for an event | [logstash-filter-date](https://github.com/logstash-plugins/logstash-filter-date) |
| [de_dot](https://www.elastic.co/guide/en/logstash/current/plugins-filters-de_dot.html) | Computationally expensive filter that removes dots from a field name | [logstash-filter-de_dot](https://github.com/logstash-plugins/logstash-filter-de_dot) |
| [dissect](https://www.elastic.co/guide/en/logstash/current/plugins-filters-dissect.html) | Extracts unstructured event data into fields using delimiters | [logstash-filter-dissect](https://github.com/logstash-plugins/logstash-filter-dissect) |
| [dns](https://www.elastic.co/guide/en/logstash/current/plugins-filters-dns.html) | Performs a standard or reverse DNS lookup                    | [logstash-filter-dns](https://github.com/logstash-plugins/logstash-filter-dns) |
| [drop](https://www.elastic.co/guide/en/logstash/current/plugins-filters-drop.html) | Drops all events                                             | [logstash-filter-drop](https://github.com/logstash-plugins/logstash-filter-drop) |
| [elapsed](https://www.elastic.co/guide/en/logstash/current/plugins-filters-elapsed.html) | Calculates the elapsed time between a pair of events         | [logstash-filter-elapsed](https://github.com/logstash-plugins/logstash-filter-elapsed) |
| [elasticsearch](https://www.elastic.co/guide/en/logstash/current/plugins-filters-elasticsearch.html) | Copies fields from previous log events in Elasticsearch to current events | [logstash-filter-elasticsearch](https://github.com/logstash-plugins/logstash-filter-elasticsearch) |
| [environment](https://www.elastic.co/guide/en/logstash/current/plugins-filters-environment.html) | Stores environment variables as metadata sub-fields          | [logstash-filter-environment](https://github.com/logstash-plugins/logstash-filter-environment) |
| [extractnumbers](https://www.elastic.co/guide/en/logstash/current/plugins-filters-extractnumbers.html) | Extracts numbers from a string                               | [logstash-filter-extractnumbers](https://github.com/logstash-plugins/logstash-filter-extractnumbers) |
| [fingerprint](https://www.elastic.co/guide/en/logstash/current/plugins-filters-fingerprint.html) | Fingerprints fields by replacing values with a consistent hash | [logstash-filter-fingerprint](https://github.com/logstash-plugins/logstash-filter-fingerprint) |
| [geoip](https://www.elastic.co/guide/en/logstash/current/plugins-filters-geoip.html) | Adds geographical information about an IP address            | [logstash-filter-geoip](https://github.com/logstash-plugins/logstash-filter-geoip) |
| [grok](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html) | Parses unstructured event data into fields                   | [logstash-filter-grok](https://github.com/logstash-plugins/logstash-filter-grok) |
| [i18n](https://www.elastic.co/guide/en/logstash/current/plugins-filters-i18n.html) | Removes special characters from a field                      | [logstash-filter-i18n](https://github.com/logstash-plugins/logstash-filter-i18n) |
| [jdbc_static](https://www.elastic.co/guide/en/logstash/current/plugins-filters-jdbc_static.html) | Enriches events with data pre-loaded from a remote database  | [logstash-filter-jdbc_static](https://github.com/logstash-plugins/logstash-filter-jdbc_static) |
| [jdbc_streaming](https://www.elastic.co/guide/en/logstash/current/plugins-filters-jdbc_streaming.html) | Enrich events with your database data                        | [logstash-filter-jdbc_streaming](https://github.com/logstash-plugins/logstash-filter-jdbc_streaming) |
| [json](https://www.elastic.co/guide/en/logstash/current/plugins-filters-json.html) | Parses JSON events                                           | [logstash-filter-json](https://github.com/logstash-plugins/logstash-filter-json) |
| [json_encode](https://www.elastic.co/guide/en/logstash/current/plugins-filters-json_encode.html) | Serializes a field to JSON                                   | [logstash-filter-json_encode](https://github.com/logstash-plugins/logstash-filter-json_encode) |
| [kv](https://www.elastic.co/guide/en/logstash/current/plugins-filters-kv.html) | Parses key-value pairs                                       | [logstash-filter-kv](https://github.com/logstash-plugins/logstash-filter-kv) |
| [metricize](https://www.elastic.co/guide/en/logstash/current/plugins-filters-metricize.html) | Takes complex events containing a number of metrics and splits these up into multiple events, each holding a single metric | [logstash-filter-metricize](https://github.com/logstash-plugins/logstash-filter-metricize) |
| [metrics](https://www.elastic.co/guide/en/logstash/current/plugins-filters-metrics.html) | Aggregates metrics                                           | [logstash-filter-metrics](https://github.com/logstash-plugins/logstash-filter-metrics) |
| [mutate](https://www.elastic.co/guide/en/logstash/current/plugins-filters-mutate.html) | Performs mutations on fields                                 | [logstash-filter-mutate](https://github.com/logstash-plugins/logstash-filter-mutate) |
| [prune](https://www.elastic.co/guide/en/logstash/current/plugins-filters-prune.html) | Prunes event data based on a list of fields to blacklist or whitelist | [logstash-filter-prune](https://github.com/logstash-plugins/logstash-filter-prune) |
| [range](https://www.elastic.co/guide/en/logstash/current/plugins-filters-range.html) | Checks that specified fields stay within given size or length limits | [logstash-filter-range](https://github.com/logstash-plugins/logstash-filter-range) |
| [ruby](https://www.elastic.co/guide/en/logstash/current/plugins-filters-ruby.html) | Executes arbitrary Ruby code                                 | [logstash-filter-ruby](https://github.com/logstash-plugins/logstash-filter-ruby) |
| [sleep](https://www.elastic.co/guide/en/logstash/current/plugins-filters-sleep.html) | Sleeps for a specified time span                             | [logstash-filter-sleep](https://github.com/logstash-plugins/logstash-filter-sleep) |
| [split](https://www.elastic.co/guide/en/logstash/current/plugins-filters-split.html) | Splits multi-line messages into distinct events              | [logstash-filter-split](https://github.com/logstash-plugins/logstash-filter-split) |
| [syslog_pri](https://www.elastic.co/guide/en/logstash/current/plugins-filters-syslog_pri.html) | Parses the `PRI` (priority) field of a `syslog` message      | [logstash-filter-syslog_pri](https://github.com/logstash-plugins/logstash-filter-syslog_pri) |
| [throttle](https://www.elastic.co/guide/en/logstash/current/plugins-filters-throttle.html) | Throttles the number of events                               | [logstash-filter-throttle](https://github.com/logstash-plugins/logstash-filter-throttle) |
| [tld](https://www.elastic.co/guide/en/logstash/current/plugins-filters-tld.html) | Replaces the contents of the default message field with whatever you specify in the configuration | [logstash-filter-tld](https://github.com/logstash-plugins/logstash-filter-tld) |
| [translate](https://www.elastic.co/guide/en/logstash/current/plugins-filters-translate.html) | Replaces field contents based on a hash or YAML file         | [logstash-filter-translate](https://github.com/logstash-plugins/logstash-filter-translate) |
| [truncate](https://www.elastic.co/guide/en/logstash/current/plugins-filters-truncate.html) | Truncates fields longer than a given length                  | [logstash-filter-truncate](https://github.com/logstash-plugins/logstash-filter-truncate) |
| [urldecode](https://www.elastic.co/guide/en/logstash/current/plugins-filters-urldecode.html) | Decodes URL-encoded fields                                   | [logstash-filter-urldecode](https://github.com/logstash-plugins/logstash-filter-urldecode) |
| [useragent](https://www.elastic.co/guide/en/logstash/current/plugins-filters-useragent.html) | Parses user agent strings into fields                        | [logstash-filter-useragent](https://github.com/logstash-plugins/logstash-filter-useragent) |
| [uuid](https://www.elastic.co/guide/en/logstash/current/plugins-filters-uuid.html) | Adds a UUID to events                                        | [logstash-filter-uuid](https://github.com/logstash-plugins/logstash-filter-uuid) |
| [xml](https://www.elastic.co/guide/en/logstash/current/plugins-filters-xml.html) | Parses XML into fields                                       | [logstash-filter-xml](https://github.com/logstash-plugins/logstash-filter-xml) |

