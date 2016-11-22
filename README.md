---
# Registered V0.2.5

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/Dk0n9/Registered/master/LICENSE)

> 本程序使用Python + Tornado + MongoDB完成,
  用于查找手机号/邮箱/用户名所注册过的网站。

---
#### 更新日志
##### version 0.2.5
* 新添加了一个方便操作html元素的公共方法供插件使用(<b>需要安装pyquery模块, 或在本程序根目录下运行`pip install -r requirements.txt`</b>)
* 将`common/functions.py`的http请求方法移至基类。使用Session管理http请求, 提高连接复用性, 并且对插件开放
* 修复一处逻辑判断错误
* 插件抛异常时会打印出错误信息方便DEBUG

##### version 0.2.4
* 修改插件规范以方便编写及简化程序流程

##### version 0.2.3
* 添加用于测试插件是否可用的测试脚本，使用方法参考当前目录下的**pluginTest.py**文件

##### version 0.2.2
* 优化查询逻辑

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

在`config/conf.py`文件中配置web地址、数据库配置、插件配置后, 运行./start.py文件启动WEB服务。

---
#### 注意事项
- 如果已经使用pip安装了bson, 程序会抛出没有找到ObjectId模块的错误。

> 这是因为pymongo内的bson模块与pip安装的bson模块起了冲突所导致的。

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
<pre><code>def register(self, target):  # target用于接收用户名/手机号/邮箱
    self.information = {  # 将所有信息统一放到了self.information中
        # 建议一个接口用一个字典表示，字典内为接口相关的信息
        'email': {
            'url': 'http://www.xxx.com/xxx.php',  # 接口地址(必填)
            'method': 'post',  # HTTP请求方法(必填)
            'settings': {  # HTTP请求头信息(可选)
                'params': None,  # GET参数, 字典形式
                'data': None,  # POST参数
                'json': None,  # JSON内容
                'headers': None,  # HTTP头
                'cookies': None,  # Cookies
                ...  # 更多参数请参照requests模块
            },
            'safe' = {  # 安全请求设置(可选)
                'url': 'http://www.xxx.com/xxx.php',  # 安全页面地址
                'method': 'get',  # HTTP请求方法
                'settings': {  # HTTP请求头信息
                    ...
                }
            }，
            'result': {  # 返回结果信息设置(必填)
                'type': 'str',  ＃ 接口返回结果的格式(必填)
                # 目前支持: str:字符串对比、regex:正则匹配、json:json解析、xml:xml解析
                'value': 'true'  # 接口返回结果的筛选内容(必填)
                # 如果结果格式是字符串对比或正则匹配模式, value应该填写需要进行对比的字符。
                # json和xml解析模式时, value填写表达式, 例: result=yes 或 result!=no (只支持 = 和 !=)
                # 如果需要查找的内容在不同层级, 则可以用.表示下一级, 例: result.success=true 或 result.mobile.success!=false
            }
        },
        ...  # 如有其他接口可按上面格式继续添加，key名称无要求
    }</code></pre>
在基类中, 还有一些可供使用的公共方法:

- request
> HTTP请求方法, 用Session管理请求，减少连接数提高复用<br/>
> 必输参数: method; http请求使用的方法<br/>
> 必输参数: url; 请求的url地址<br/>
> 可选参数: settings; requests参数字典<br/>

- getPyquery
> 返回解析好内容的pyquery对象, 需要使用者对pyquery有一定了解。(可参考`plugins/github.py`)<br/>
> 必输参数: content; 网页内容<br/>

- getRandomAgent
> 随机获取一个User-Agent, 想添加或移除User-Agent可以在基类的代码中修改

- getNowTime
> 获取当前时间的时间戳(十位长度)

- getRandomStr
> 获取指定长度的随机字符串, 默认只返回随机字母组合<br/>
> 必输参数: length; 指定字符串的长度<br/>
> 可选参数: intger; 如果为True, 只返回随机数字组合<br/>
> 可选参数: mix; 如果为True, 返回随机数字+字母组合<br/>
