# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'mangocity'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '芒果网'
    __url__ = 'http://www.mangocity.com/'

    def register(self, target):
        self.url = 'http://www.mangocity.com/mbrWebCenter/validate_new/validateUsername.action'
        self.method = 'post'
        self.settings = {
            'data': {
                'username': target
            }
        }
        self.resultType = 'str'
        self.resultValue = 'Y'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
