# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'dangdang_mobile'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '当当网'
    __url__ = 'http://www.dangdang.com/'

    def register(self, target):
        self.information = {
            'email': {
                'url': 'https://login.dangdang.com/p/mobile_checker.php',
                'method': 'post',
                'settings': {
                    'data': {
                        'mobile': target
                    }
                },
                'result': {
                    'type': 'str',
                    'value': 'true'
                }
            }
        }



