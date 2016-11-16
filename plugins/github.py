# coding: utf8

from common import base


class Plugin(base.BASE):

    __name__ = 'github'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = 'GitHub'
    __url__ = 'https://github.com/'

    def register(self, target):
        self.information = {
            'username': {
                'url': 'https://github.com/signupCheck/username',
                'method': 'post',
                'settings': {
                    'data': {
                        'value': target
                    },
                    'headers': {
                        'X_Requested_With': 'XMLHttpRequest',
                    },
                },
                'safe': {
                    'url': 'https://github.com/join?source=login',
                    'method': 'get'
                },
                'result': {
                    'type': 'json',
                    'value': 'success=1'
                }
            }
        }
