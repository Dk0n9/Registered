# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'qyer_phone'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '穷游网'
    __url__ = 'http://www.qyer.com/'

    def register(self, target):
        self.url = 'http://login.qyer.com/qcross/login/auth.php'
        self.method = 'get'
        self.settings = {
            'params': {
                'action': 'regcheck',
                'input': '86-' + target,
                'type': 'phone'
            }
        }
        self.resultType = 'json'
        self.resultValue = 'error_code=400002'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
