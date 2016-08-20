# coding: utf-8

from Registered.common import base


class Plugin(base.BASE):

    __title__ = '当当网'
    __domain__ = 'http://www.dangdang.com/'

    def register(self, target):
        self.url = 'https://login.dangdang.com/p/mobile_checker.php'
        self.method = 'post'
        self.settings = {
            'data': {
                'mobile': target
            }
        }
        self.resultType = 'str'
        self.resultValue = 'true'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
