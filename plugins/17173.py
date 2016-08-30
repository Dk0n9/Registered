# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = '17173game_email'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '17173小游戏'
    __url__ = 'http://www.17173.com/'

    def register(self, target):
        domain = target.split('@')
        if len(domain) == 1 or len(domain) > 2:
            return False
        self.url = 'http://passport.17173.com/register/validate?field=username'
        self.method = 'get'
        self.settings = {
            'params': {
                'value': target,
                'domain': domain[1]
            }
        }
        self.resultType = 'json'
        self.resultValue = 'status=0'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
