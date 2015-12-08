# coding: utf-8
__author__ = 'DK'


def getConfig():
    return {
        'TITLE': u'京东',  # 插件标题
        'DESC': 'https://jd.com',  # 网站URL
        'URL': 'https://reg.jd.com/validateuser/isMobileEngaged?mobile={0}',  # 请求地址
        'SAFE_URL': 'https://reg.jd.com/reg/person?ReturnUrl=http%3A//www.jd.com/',  # 安全请求地址
        'METHOD': 'GET',  # HTTP方法
        'HEADERS': {  # 请求头

        },
        'COOKIES': {  # 请求Cookie

        },
        'DATA': {  # 请求参数

        },
        # 返回结果的类型, 暂定为两种: json, str.
        # json: RESULT应为 key = success value. eg: result=success
        # 如果json存在多级关系应该这样: result.sub = success value
        # str: RESULT为指定的字符
        'TYPE': 'json',
        'RESULT': 'success=1',
    }
