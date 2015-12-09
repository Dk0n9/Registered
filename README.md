# Registered V0.1
查看你注册过哪些网站<br />
  <br>

使用Python+Flask完成<br />
  <br>
  
自己写了个简陋的WEB界面，直接运行regWeb.py，默认会在本地的8000端口开启WEB服务, 界面如下，轻喷。
<img src="http://ww2.sinaimg.cn/large/7c541441gw1eytu0l5xvgj211y0ij0t9.jpg"><br />
  <br>
现在已经加上了一些常用网站的插件供测试，以后也会不定时添加。
下面是插件的一些配置：（插件需放在plugins目录下）

**'TITLE': u'this is title',  # 插件标题，会显示在WEB**<br />
**'DESC': 'https://www.example.com/',  # 网站URL，会显示在WEB**<br />
**'URL': 'https://www.example.com/?check&phone={0}',  # 请求地址**<br />
**'SAFE_URL': 'https://www.example.com/',  # 安全请求地址**<br />
**'METHOD': 'GET',  # HTTP方法**<br />
**'HEADERS': {},  # 请求头**<br />
**'COOKIES': {},  # 请求Cookie**<br />
**'DATA': {},  # 请求参数**<br />
**\# 返回结果的类型, 暂定为两种: json, str**<br />
**\# json: RESULT应为 key = success value 或 key != success value. eg: result=success**<br />
**\# 如果json存在多级关系应该这样: result.sub = success value**<br />
**\# str: RESULT为指定的字符**<br />
**'TYPE': 'json',**<br />
**'RESULT': 'errInfo.no!=0'**<br />
  <br>
**{0}: 在程序中会自动将{0}替换成要查询的目标**<br />
**{UA}: 在程序中会自动替换成随机产生的User-Agent**<br />

具体的使用请参考plugins目录下的插件。<br />
  <br>

> 下一版本将会更新：
> 
>> 1. 解决网页内容乱码导致json解析失败的BUG
> 
>> 2. 支持正则和XML解析
