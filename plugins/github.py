# coding: utf8

from common import base


class Plugin(base.BASE):

    __name__ = 'github'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = 'GitHub'
    __url__ = 'https://github.com/'

    def register(self, target):
        response = self.request('get', 'https://github.com/')
        html = self.getPyquery(response.content)
        token = html('input[name="authenticity_token"]').val()
        self.information = {
            'username': {
                'url': 'https://github.com/signup_check/username',
                'method': 'post',
                'settings': {
                    'data': {
                        'value': target,
                        'authenticity_token': token
                    },
                    'headers': {
                        'X_Requested_With': 'XMLHttpRequest',
                    },
                    'cookies': response.cookies
                },
                'result': {
                    'type': 'str',
                    'value': 'Username is already taken'
                }
            }
        }
