# coding: utf-8
__author__ = 'DK'


def getConfig():
    return {
        'TITLE': u'当当网',  # 插件标题
        'URL': 'https://login.dangdang.com/p/mobile_checker.php',  # 请求地址
        'METHOD': 'POST',  # HTTP方法
        'HEADERS': {  # 请求头

        },
        'COOKIES': {  # 请求Cookie

        },
        'DATA': {  # 请求参数
            'mobile': '{0}'
        },
        # 返回结果的类型, 暂定为两种: json, str.
        # json: RESULT应为 key = success value. eg: result=success
        # 如果json存在多级关系应该这样: result.sub = success value
        # str: RESULT为指定的字符
        'TYPE': 'str',
        'RESULT': 'true',
    }
