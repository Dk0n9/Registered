# coding: utf-8
from time import sleep
import threading
import random

import requests

import load
import threadpool
import parse
__author__ = 'DK'


class Main:

    def __init__(self):
        # 要查询的账号
        self.target = ''
        # 线程池对象
        self.__tp = threadpool.threadPoolManage(self.run)
        self.__tp.setMaxThreadSize(20)
        # 线程锁
        self.lock = threading.Lock()
        # 返回的结果集
        self.current = 0
        self.maxCount = 1
        self.result = {}

    def start(self, target):
        self.__clear()  # 初始化
        self.target = target
        if not self.loads():
            return self.result
        if not self.__tp.start():
            exit('Startup failed!')
        while True:
            if self.__tp.getThreadPoolRunState() == 2:
                break
            if self.current >= self.maxCount:
                if self.__tp.stop():
                    break
        sleep(1)
        return self.result

    def loads(self):
        """
        将插件对象插入到线程池工作队列
        """
        tempRes = load.load()
        self.maxCount = len(tempRes)  # 赋值最大任务数
        if self.maxCount == 0:
            return False
        for mod in tempRes:
            self.__tp.addTask(tempRes[mod])
        return True

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
        # 进度
        self.lock.acquire()
        self.current += 1
        self.lock.release()

        if stateObj.getAction() in [2, 3]:
            return False

        config = handle.getConfig()
        configStr = str(config)
        configStr = configStr.replace('{0}', self.target)
        if '{UA}' in configStr:
            # 随机UserAgent
            configStr = configStr.replace('{UA}', self.__randomUserAgent())
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
                url=config.get('URL'),
                method=config.get('METHOD'),
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
        try:
            self.getResult(config, urlData)
        except Exception, e:
            print e

    def getResult(self, config, data):
        """
        比对结果
        :param config: dict
        :param data: object
        """
        # 字符串结果匹配
        if config['TYPE'] == 'str':
            if parse.strFind(config['RESULT'], data.content):
                self.result[config['TITLE']] = config['DESC']
                return True
        # 正则匹配
        if config['TYPE'] == 'reg':
            if parse.regParse(config['RESULT'], data.content):
                self.result[config['TITLE']] = config['DESC']
                return True
        # json结果匹配
        if config['TYPE'] == 'json':
            if '!=' in config['RESULT']:
                comp = False
                key, value = config['RESULT'].split('!=')
            else:
                comp = True
                key, value = config['RESULT'].split('=')
            if not key.count('.'):
                if parse.jsonParse([key], value, data, comp):
                    self.result[config['TITLE']] = config['DESC']
            else:
                if parse.jsonParse(key.split('.'), value, data, comp):
                    self.result[config['TITLE']] = config['DESC']
                    return True

    def __randomUserAgent(self):
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
        rnd = ua[random.randint(0, len(ua) - 1)]
        return rnd

    def __clear(self):
        self.current = 0
        self.maxCount = 1
        self.result = {}


if __name__ == '__main__':
    a = Main()
    data = a.start('test@example.com')
    print data
    for k in data:
        print k
