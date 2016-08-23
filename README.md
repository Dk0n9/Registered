---
# Registered V0.2 dev

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/Dk0n9/Registered/dev/LICENSE)

> 本程序使用Python + Tornado完成,
  用于查找手机号/邮箱/用户名所注册过的网站。

---
#### 更新日志
##### version 0.2
* 使用Python + Flask重写

##### version 0.1
* 使用Python + Flask完成了第一版

---
#### 使用方法
在./config/conf.py文件中配置web地址、数据库配置、插件配置后, 运行./start.py文件。

---
#### 插件编写规范
编写插件需要一定的Python基础。
插件脚本首先需要导入包
from Registered.common import base
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