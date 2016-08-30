---
# Registered V0.2.1

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/Dk0n9/Registered/master/LICENSE)

> 本程序使用Python + Tornado完成,
  用于查找手机号/邮箱/用户名所注册过的网站。

---
#### 更新日志
##### version 0.2.1
* 修复若干bug

##### version 0.2
* 使用Python + Tornado重写
* 重新定义了插件的规范
* 重写前端页面, 并使用可靠性更高的websocket来传递信息

##### version 0.1
* 使用Python + Flask完成了第一版

---
#### 使用方法
在程序目录下运行:
<pre><code>pip install -r requirements.txt</code></pre>
安装程序所需的依赖包

在./config/conf.py文件中配置web地址、数据库配置、插件配置后, 运行./start.py文件启动WEB服务。

---
#### 注意事项
- 如果已经使用pip安装了bson, 程序会抛出没有找到ObjectId模块的错误。

> 这是因为pymongo内的bson模块与pip安装的bson起了冲突所导致的。

> 需要先把bson和pymongo(装了的话)模块卸载, 然后再使用pip安装回pymongo模块即可解决错误。

---
#### 插件编写规范
编写插件需要一定的Python基础。
插件脚本首先需要导入包
<pre><code>from common import base</code></pre>
编写一个Plugin类, 继承自base.BASE
<pre><code>class Plugin(base.BASE):</code></pre>
需要定义类的基本属性:
<pre><code>__name__ = 'xxx'  # 插件名, 不能与其他插件名重复, 且只能使用字母、数字、英文下划线命名, 字母开头
__title__ = 'xx网'  # 网站名
__url__ = 'http://www.xxx.com/'  # 网站地址</code></pre>
以及定义类的**register**方法:
<pre><code>def register(self, target):  # 用于接收用户名/手机号/邮箱
    self.url = 'http://www.xxx.com/xxx.php'  # 接口地址
    self.method = 'post'  # HTTP请求方法
    self.settings = {  # HTTP请求头
        'params': None,  # GET参数, 字典形式
        'data': None,  # POST参数
        'headers': None,  # HTTP头
        'cookies': None  # Cookies
    }
    safeMethod = None  # 安全请求方法
    safeURL = None  # 安全请求地址(在请求接口地址之前先访问安全请求地址)
    safeSettings = settings  # 安全请求的HTTP请求头, 与上面的HTTP请求头格式相同
    self.resultType = 'str'  # 接口返回结果的格式(目前支持: str:字符串对比、regex:正则匹配、json:json解析、xml:xml解析)
    self.resultValue = 'true'
    # 如果结果格式是字符串对比或正则匹配模式, resultValue应该填写需要进行对比的字符。
    # json和xml解析模式时, resultValue填写表达式, 样例: result=yes 或 result!=no (只支持 = 和 !=)
    # 如果需要查找的内容在不同层级, 则可以用.表示下一级, 样例: result.success=true 或 result.mobile.success!=false</code></pre>
在基类中, 还有一些可供使用的公共方法:

- getRandomAgent
> 随机获取一个User-Agent, 想添加或移除User-Agent可以在基类的代码中修改

- getNowTime
> 获取当前时间的时间戳(十位长度)

- getRandomStr
> 获取指定长度的随机字符串, 默认只返回随机字母组合<br/>
> 必输参数: length; 指定字符串的长度<br/>
> 可选参数: intger; 如果为True, 只返回随机数字组合<br/>
> 可选参数: mix; 如果为True, 返回随机数字+字母组合<br/>
