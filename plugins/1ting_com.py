# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = '1ting_user'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '一听音乐网'
    __url__ = 'http://www.1ting.com/'

    def register(self, target):
        self.url = 'http://my.1ting.com/register/check'
        self.method = 'get'
        self.settings = {
            'params': {
                'user_login': target,
            }
        }
        self.resultType = 'str'
        self.resultValue = 'false'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
