# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'baidu_user'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '百度'
    __url__ = 'https://www.baidu.com/'

    def register(self, target):
        self.url = 'https://passport.baidu.com/v2/?regnamesugg'
        self.method = 'get'
        self.settings = {
            'params': {
                'tpl': 'mn',
                'apiver': 'v3',
                'username': target
            }
        }
        self.resultType = 'json'
        self.resultValue = 'data.userExsit=1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
