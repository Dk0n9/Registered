# coding: utf-8
__author__ = 'DK'


def getConfig():
    return {
        'TITLE': u'360',  # 插件标题
        'DESC': 'http://www.360.com/',  # 网站URL
        'URL': 'http://login.360.cn/',  # 请求地址
        'METHOD': 'POST',  # HTTP方法
        'HEADERS': {  # 请求头

        },
        'COOKIES': {  # 请求Cookie

        },
        'DATA': {  # 请求参数
            'src': 'pcw_home',
            'from': 'pcw_home',
            'charset': 'UTF-8',
            'requestScema': 'http',
            'o': 'User',
            'm': 'checkmobile',
            'mobile': '{0}',
            'proxy': 'http://i.360.cn/psp_jump.html'
        },
        # 返回结果的类型, 暂定为两种: json, str.
        # json: RESULT应为 key = success value. eg: result=success
        # 如果json存在多级关系应该这样: result.sub = success value
        # str: RESULT为指定的字符
        'TYPE': 'str',
        'RESULT': 'http://i.360.cn/psp_jump.html',
    }
