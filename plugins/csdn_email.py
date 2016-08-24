# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'csdn_email'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = 'CSDN'
    __url__ = 'http://www.csdn.net/'

    def register(self, target):
        self.url = 'http://passport.csdn.net/account/register'
        self.method = 'get'
        self.settings = {
            'params': {
                'action': 'validateEmail',
                'email': target
            }
        }
        self.resultType = 'str'
        self.resultValue = 'false'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
