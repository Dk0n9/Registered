# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'nubia_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '努比亚'
    __url__ = 'http://www.nubia.com/'

    def register(self, target):
        self.url = 'https://login.dangdang.com/p/mobile_checker.php'
        self.method = 'post'
        self.settings = {
            'data': {
                'param': target,
                'name': 'mobile'
            }
        }
        self.resultType = 'str'
        self.resultValue = '{"status":"n","info":"\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7' \
                           '\xe7\xa0\x81\xe5\xb7\xb2\xe7\xbb\x8f\xe8\xa2\xab\xe6\xb3\xa8\xe5\x86\x8c!"}'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
