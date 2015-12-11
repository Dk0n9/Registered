# coding: utf-8
import re


def strFind(keyword, content):
    """
    字符串查找
    :param keyword: str, 关键字
    :param content: str, 网页数据
    :return: boolean
    """
    if keyword in content.strip(''):
        return True
    return False


def regParse(reg, content):
    """
    正则匹配
    :param reg: str, 正则表达式
    :param content: str, 网页数据
    :return: boolean
    """
    try:
        m = re.findall(reg, content)
        if m:
            return True
    except Exception, e:
        pass
    return False


def jsonParse(keys, val, obj, comparison):
    """
    json解析
    :param keys: list
    :param val: str
    :param obj: object
    :param comparison: boolean
    :return: boolean
    """
    data = obj.json(object_hook=formatResult)
    temp = data.get(keys[0])
    keys.pop(0)
    for k in keys:
        temp = temp.get(k)
        if temp is None:
            return False
    if comparison and temp.upper() == val.upper():
        return True
    if not comparison and temp.upper() != val.upper():
        return True


def formatResult(result):
    """
    处理原始数据(去掉结果中的 u'')
    """
    rv = {}
    for key, value in result.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, dict):
            value = formatResult(value)
        elif isinstance(value, list):
            value = decodeList(value)
        elif isinstance(value, object):
            value = value.__str__()
        else:
            pass
        rv[key] = value
    return rv


def decodeList(result):
    """
    处理原始数据(去掉结果中的 u'')
    """
    rv = []
    for value in result:
        if isinstance(value, unicode):
            value = str(value.encode('utf-8'))
        elif isinstance(value, dict):
            value = formatResult(value)
        elif isinstance(value, list):
            value = decodeList(value)
        elif isinstance(value, object):
            value = value.__str__()
        else:
            pass
        rv.append(value)
    return rv
