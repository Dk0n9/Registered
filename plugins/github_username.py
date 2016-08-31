# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'github_username'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = 'GitHub'
    __url__ = 'https://github.com/'

    def register(self, target):
        self.url = 'https://github.com/signup_check/username'
        self.method = 'post'
        self.settings = {
            'data': {
                'value': target
            },
            'headers': {
                'X-Requested-With': 'XMLHttpRequest',
            },
        }
        self.safeMethod = 'get'
        self.safeURL = 'https://github.com/join?source=login'
        self.resultType = 'json'
        self.resultValue = 'success=1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
