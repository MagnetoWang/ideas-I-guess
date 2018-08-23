```mermaid
graph TD

api


web
service


web-->|调用|api
api-->|发送json字符串|service
service-->|解析|sort
service-->|解析|filter
service-->|解析|housecode
housecode-->|返回|data
filter-->|返回|data
sort-->|返回|data
data-->|渲染|web
```
