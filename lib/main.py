# coding: utf-8
from time import sleep
import threading
import json

import requests

import load
import threadpool
__author__ = 'DK'


class Main:

    def __init__(self, target):
        # 要查询的账号
        self.target = target
        # 线程池对象
        self.__tp = threadpool.threadPoolManage(self.run)
        self.__tp.setMaxThreadSize(10)
        # 线程锁
        self.lock = threading.Lock()
        # 返回的结果集
        self.result = {}

    def start(self):
        self.loads()
        if not self.__tp.start():
            exit('Startup failed!')
        while True:
            if self.__tp.getThreadPoolRunState() == 2:
                break
            sleep(1)
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

    def run(self, stateObj, handle):
        """
        回调函数
        :param stateObj: object, 保存线程池状态的对象
        :param handle: object, 插件对象
        """
        if stateObj.getAction() in [2, 3]:
            return False
        config = handle.getConfig()
        temp = str(config).replace('{0}', self.target)
        config = eval(temp)
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
        # TODO: 支持正则匹配
        # 字符串结果匹配
        if config['TYPE'] == 'str':
            if config['RESULT'] in content:
                self.result[config['TITLE']] = 'success'
                return True
        if config['TYPE'] != 'json':
            return False
        # json结果匹配
        rawData = json.loads(content, object_hook=self.formatResult)
        key, value = config['RESULT'].split('=')
        if not key.count('.'):
            if rawData.get(key) == value:
                self.result[config['TITLE']] = 'success'
        else:
            if not self.getNodeValue(key, value, rawData):
                return False
            self.result[config['TITLE']] = 'success'

    def getNodeValue(self, keys, val, data):
        """
         多级节点遍历
        :param keys: list
        :param val: str
        :param data: dict
        :return: boolean
        """
        temp = data.get(keys[0])
        keys.pop(0)
        for k in keys:
            temp = temp.get(k)
            if temp is None:
                return False
        if temp == val:
            return True

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
    a = Main('test@qq.com')
    data = a.start()
    for k in data:
        print k
