# coding: utf-8
__author__ = 'DK'


def getConfig():
    return {
        'TITLE': u'顺丰速运',  # 插件标题
        'URL': 'https://i.sf-express.com/service/user/register/generalregister/mobile/same',  # 请求地址
        'METHOD': 'POST',  # HTTP方法
        'HEADERS': {  # 请求头

        },
        'COOKIES': {  # 请求Cookie

        },
        'DATA': {  # 请求参数
            'phone': '{0}'
        },
        # 返回结果的类型, 暂定为两种: json, str.
        # json: RESULT应为 key = success value. eg: result=success
        # 如果json存在多级关系应该这样: result.sub = success value
        # str: RESULT为指定的字符
        'TYPE': 'str',
        'RESULT': '\"Y\"',
    }
