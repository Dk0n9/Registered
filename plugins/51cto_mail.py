# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = '51cto_email'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '51CTO'
    __url__ = 'http://www.51cto.com/'

    def register(self, target):
        self.url = 'http://ucenter.51cto.com/checkemails.php'
        self.method = 'get'
        self.settings = {
            'params': {
                'email': target
            }
        }
        self.resultType = 'str'
        self.resultValue = 'font_green12'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
