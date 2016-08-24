# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'pptv_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = 'PPTV'
    __url__ = 'http://www.pptv.com/'

    def register(self, target):
        self.url = 'http://passport.pptv.com/isPhoneExist.do'
        self.method = 'get'
        self.settings = {
            'params': {
                'phone': target
            }
        }
        self.resultType = 'str'
        self.resultValue = '1'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
