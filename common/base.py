# coding: utf-8
"""
插件基类
"""

import time
import random
import string

from common import analyze
from common import functions


class BASE(object):

    information = {
        'phone': {},
        'email': {},
        'username': {}
    }
    _analyzer = analyze.Analyzer()

    def verify(self):
        for key in self.information.keys():
            if not self.information[key]:
                continue
            tempDict = self.information[key]
            tempSafeDict = tempDict.get('safe')
            if tempSafeDict:
                safeResponse = functions.request(**tempSafeDict)
                if not safeResponse:
                    return False
                tempDict.setdefault('settings', {})
                if 'headers' not in tempDict['settings']:
                    tempDict['settings']['headers'] = safeResponse.headers
                if 'cookies' not in self.information[key]['settings']:
                    tempDict['settings']['cookies'] = safeResponse.cookies
            response = functions.request(tempDict['method'], tempDict['url'], tempDict['settings'])
            if not response:
                return False
            self._analyzer.set(response.content, tempDict['result'])
            result = self._analyzer.get()
            if result:
                return True
        return False

    def getRandomAgent(self):
        """
        获取随机User-Agent
        :return:
        """
        userAgents = [
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;', # IE
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', # safari
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36', # chrome
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11' # opera
        ]
        return random.choice(userAgents)

    def getNowTime(self):
        """
        获得当前时间的时间戳(十位)
        :return:
        """
        return str(int(time.time()))

    def getRandomStr(self, length, intger=False, mix=False):
        """
        获取指定长度的随机字符串
        :param length: 指定字符串长度
        :type length: int
        :param intger: 如果指定了intger参数,则字符串全为数字
        :param mix: 如果指定了mix参数,则字符串为数字+字母混合
        :return:
        """
        randomStr = string.ascii_lowercase
        if intger and not mix:
            randomStr = '1234567890'
        if mix:
            randomStr += '1234567890'
        return ''.join(random.sample(randomStr, int(length)))
