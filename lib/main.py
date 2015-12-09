# coding: utf-8
from time import sleep
import threading
import json
import random

import requests

import load
import threadpool
__author__ = 'DK'


class Main:

    def __init__(self):
        # 要查询的账号
        self.target = ''
        # 线程池对象
        self.__tp = threadpool.threadPoolManage(self.run)
        self.__tp.setMaxThreadSize(10)
        # 线程锁
        self.lock = threading.Lock()
        # 返回的结果集
        self.result = {}

    def start(self, target):
        self.result = {}
        self.target = target
        self.loads()
        if not self.__tp.start():
            exit('Startup failed!')
        while True:
            if self.__tp.getThreadPoolRunState() == 2:
                break
            sleep(2)
            if not self.__tp.getTaskSize():
                self.__tp.stop()
        return self.result

    def loads(self):
        """
        将插件对象插入到线程池工作队列
        """
        tempRes = load.load()
        for mod in tempRes:
            self.__tp.addTask(tempRes[mod])

    def count(self):
        """
        获取插件数量
        """
        return load.count()

    def run(self, stateObj, handle):
        """
        回调函数
        :param stateObj: object, 保存线程池状态的对象
        :param handle: object, 插件对象
        """
        if stateObj.getAction() in [2, 3]:
            return False
        config = handle.getConfig()
        configStr = str(config)
        configStr = configStr.replace('{0}', self.target)
        if '{UA}' in configStr:
            # 随机UserAgent
            configStr = configStr.replace('{UA}', self.randomUserAgent())
        config = eval(configStr)
        # 如果需要请求安全地址
        if config.get('SAFE_URL'):
            try:
                tempUrlData = requests.request(
                    url=config['SAFE_URL'],
                    method='GET',
                    verify=False,
                    timeout=10
                )
                # 安全请求参数
                config['COOKIES'] = tempUrlData.cookies
            except Exception, e:
                pass
        try:
            urlData = requests.request(
                url=config['URL'],
                method=config['METHOD'],
                headers=config.get('HEADERS'),
                cookies=config.get('COOKIES', None),
                data=config.get('DATA'),
                verify=False,
                timeout=10
            )
        except Exception, e:
            return False
        if urlData.status_code != 200:
            return False
        self.getResult(config, urlData.content)

    def getResult(self, config, content):
        """
        比对结果
        :param config: dict
        :param content: str
        """
        # 字符串结果匹配
        # TODO: 支持正则匹配和XML匹配, 目前暂时用字符串查找的方式代替
        if config['TYPE'] == 'str':
            if config['RESULT'] in content.strip(''):
                self.result[config['TITLE']] = config['DESC']
                return True
        if config['TYPE'] != 'json':
            return False
        # json结果匹配
        # TODO: 解决返回数据乱码在json解码时的异常问题
        rawData = json.loads(content, object_hook=self.formatResult)
        if '!=' in config['RESULT']:
            comp = False
            key, value = config['RESULT'].split('!=')
        else:
            comp = True
            key, value = config['RESULT'].split('=')
        if not key.count('.'):
            if self.getNodeValue([key], value, rawData, comp):
                self.result[config['TITLE']] = config['DESC']
        else:
            if self.getNodeValue(key.split('.'), value, rawData, comp):
                self.result[config['TITLE']] = config['DESC']

    def getNodeValue(self, keys, val, data, comparison=True):
        """
         多级节点遍历
        :param keys: list
        :param val: str
        :param data: dict
        :param comparison: boolean
        :return: boolean
        """
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

    def randomUserAgent(self):
        """
        返回随机UserAgent
        :return: str
        """
        ua = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/46.0.2490.80 Safari/537.36',  # chrome
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',  # firefox
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR '
            '2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'  # IE9
        ]
        return ua[random.randint(0, len(ua))]

    def formatResult(self, result):
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
                value = self.formatResult(value)
            elif isinstance(value, list):
                value = self.decodeList(value)
            elif isinstance(value, object):
                value = value.__str__()
            else:
                pass
            rv[key] = value
        return rv

    def decodeList(self, result):
        """
        处理原始数据(去掉结果中的 u'')
        """
        rv = []
        for value in result:
            if isinstance(value, unicode):
                value = str(value.encode('utf-8'))
            elif isinstance(value, dict):
                value = self.formatResult(value)
            elif isinstance(value, list):
                value = self.decodeList(value)
            elif isinstance(value, object):
                value = value.__str__()
            else:
                pass
            rv.append(value)
        return rv

if __name__ == '__main__':
    a = Main()
    data = a.start('test@example.com')
    print data
    for k in data:
        print k
