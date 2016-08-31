# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'elong'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '艺龙旅行网'
    __url__ = 'http://www.elong.com/'

    def register(self, target):
        self.url = 'https://secure.elong.com/passport/isajax/Register/ValidateMobileOrEmail'
        self.method = 'get'
        self.settings = {
            'params': {
                'mobile': target,
            }
        }
        self.resultType = 'json'
        self.resultValue = 'value=1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
