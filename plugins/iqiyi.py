# coding: utf-8
__author__ = 'Stanla'

from common import base


class Plugin(base.BASE):

    __name__ = 'iqiyi'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '爱奇艺'
    __url__ = 'http://www.iqiyi.com/'

    def register(self, target):
        self.url = 'http://passport.iqiyi.com/apis/user/check_account.action'
        self.method = 'get'
        self.settings = {
            'params': {
                'account': target,
            },
            'headers': {
                'user-agent': self.getRandomAgent(),
                'referer': 'http://vip.iqiyi.com/'
            }
        }
        self.resultType = 'json'
        self.resultValue = 'data=true'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
