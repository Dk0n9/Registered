# coding: utf-8
"""
结果内容解析模块
目前已完成:
字符串解析、正则解析、json解析、xml解析
"""

import re
import json
from xml.dom import minidom


class Analyzer(object):

    def __init__(self):
        self.__type = None
        self.__value = None
        self.__content = None

    def set(self, rtype, value, content):
        self.__type = rtype.lower()
        self.__value = value
        self.__content = content

    def get(self):
        if self.__type.startswith('_'):
            return False
        else:
            name = '_' + self.__type + 'Analyzer'
            if hasattr(self, name):
                return getattr(self, name).__call__()
            else:
                return False

    def _strAnalyzer(self):
        if self.__value in self.__content:
            return True
        else:
            return False

    def _regexAnalyzer(self):
        try:
            match = re.search(self.__value, self.__content, re.I)
            if match.group():
                return True
            return False
        except Exception, e:
            return False

    def _jsonAnalyzer(self):
        data = self.__value.split('!=')
        if len(data) > 1:
            compare = False
            condition, value = data
        else:
            compare = True
            condition, value = self.__value.split('=')
        cond = condition.split('.')
        try:
            data = json.loads(self.__content, object_hook=self._formatResult)
            condValue = self.__eachObject(cond, data)
            if condValue is False:
                return False
        except Exception, e:
            return False
        if compare and value.lower() == condValue.lower():
            return True
        if not compare and value.lower() != condValue.lower():
            return True
        return False

    def _xmlAnalyzer(self):
        data = self.__value.split('!=')
        if len(data) > 1:
            compare = False
            condition, value = data
        else:
            compare = True
            condition, value = self.__value.split('=')
        try:
            attrMatch = re.findall(r'\[(.*)\]+', condition)
            if not attrMatch:
                return False
        except Exception, e:
            return False
        xmlTagName = condition.replace(attrMatch[0], '')
        xmlObject = minidom.parseString(self.__content)
        data = self.__filterValue(xmlTagName, attrMatch[0], xmlObject)
        if data is False:
            return False
        if compare and value.lower() == data.lower():
            return True
        if not compare and value.lower() != data.lower():
            return True
        return False

    def __filterValue(self, tagName, value, element):
        attrMatch = re.findall(r'\[(.*)\]+', value)
        tags = element.getElementsByTagName(tagName)
        for nodeObject in tags:
            if value.startswith('name'):
                return nodeObject._get_attributes().get(attrMatch[0]).value
            else:
                return nodeObject.childNodes[0].nodeValue
        return False

    def __eachObject(self, keys, data):
        if not keys:
            return False
        for key in keys:
            if not isinstance(data, dict):
                return False
            if key not in data:  # 高效检索
                return False
            data = data[key]
        return data

    def _formatResult(self, result):

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
                value = self._formatResult(value)
            elif isinstance(value, object):
                value = value.__str__()
            else:
                value = str()
            rv[key] = value
        return rv


if __name__ == '__main__':
    test = Analyzer()
    test.set('json', 'result=true', '{"result":true}')
    print test.get()
