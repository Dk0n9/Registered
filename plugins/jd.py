# coding: utf-8

from Registered.common import base


class Plugin(base.BASE):

    __name__ = 'jingdong'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '京东商城'
    __url__ = 'http://www.jd.com/'

    def register(self, target):
        self.url = 'https://reg.jd.com/validateuser/isPinEngaged'
        self.method = 'post'
        self.settings = {
            'data': {
                'regName': target,
                'pin': target
            },
            'headers': {
                'X-Requested-With': 'XMLHttpRequest',
            },
        }
        self.safeMethod = 'get'
        self.safeURL = 'https://reg.jd.com/reg/person'
        self.resultType = 'json'
        self.resultValue = 'success=1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
