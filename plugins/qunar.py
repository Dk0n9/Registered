# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'qunar_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '去哪儿网'
    __url__ = 'http://www.qunar.com/'

    def register(self, target):
        self.url = 'https://user.qunar.com/ajax/validator.jsp'
        self.method = 'post'
        self.settings = {
            'data': {
                'method': target,
                'prenum': '86'
            }
        }
        self.resultType = 'json'
        self.resultValue = 'errCode=11009'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
