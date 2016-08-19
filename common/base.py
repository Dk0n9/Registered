# coding: utf-8
"""
插件基类
"""

import time
import random
import string

import requests

from Registered.common import analyze


class BASE(object):

    url = None
    method = None
    settings = {
        'params': None,
        'data': None,
        'headers': None,
        'cookies': None
    }
    safeMethod = None
    safeURL = None
    safeSettings = settings
    resultType = None
    resultValue = None
    _analyzer = analyze.Analyzer()

    def verify(self):
        if self.safeURL:
            safeRes = self.__request(self.safeMethod, self.safeURL, self.safeSettings)
            if not safeRes:
                return False
            self.settings['headers'] = safeRes.headers
            self.settings['cookies'] = safeRes.cookies
        requestRes = self.__request(self.method, self.url, self.settings)
        if not requestRes:
            return False
        self._analyzer.set(self.resultType, self.resultValue, requestRes.content)
        return self._analyzer.get()

    def __request(self, method, url, settings=None):
        try:
            response = requests.request(method, url, **settings)
            return response
        except requests.Timeout:
            return self.__request(method, url, **settings)
        except Exception, e:
            return False

    @property
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

    @property
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
