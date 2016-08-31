# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'mafengwo'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '蚂蜂窝'
    __url__ = 'http://www.mafengwo.cn/'

    def register(self, target):
        self.url = 'https://passport.mafengwo.cn/api.php/checkPassport'
        self.method = 'get'
        self.settings = {
            'params': {
                'passport': target
            }
        }
        self.resultType = 'str'
        self.resultValue = '178522'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
