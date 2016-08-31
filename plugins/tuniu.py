# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'tuniu_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '途牛旅行网'
    __url__ = 'http://www.tuniu.com/'

    def register(self, target):
        self.url = 'https://passport.tuniu.com/register/isPhoneAvailable'
        self.method = 'post'
        self.settings = {
            'data': {
                'tel': target
            }
        }
        self.resultType = 'json'
        self.resultValue = 'errno=-1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
