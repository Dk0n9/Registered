# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'meizu_user'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '魅族'
    __url__ = 'http://meizu.com/'

    def register(self, target):
        self.url = 'https://i.flyme.cn/uc/system/webjsp/member/isValidFlyme'
        self.method = 'get'
        self.settings = {
            'params': {
                'account': target
            }
        }
        self.resultType = 'json'
        self.resultValue = 'value=False'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
