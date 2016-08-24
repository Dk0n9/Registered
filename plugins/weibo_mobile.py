# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'weibo_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '微博'
    __url__ = 'http://www.weibo.com/'

    def register(self, target):
        self.url = 'http://weibo.com/signup/v5/formcheck'
        self.method = 'get'
        self.settings = {
            'params': {
                'type': 'mobilesea',
                'zone': '0086',
                'value': target,
                'from': ''
            },
            'headers': {
                'user-agent': self.getRandomAgent(),
                'referer': 'http://weibo.com/signup/signup.php'
            }
        }
        self.resultType = 'json'
        self.resultValue = 'code=600001'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
