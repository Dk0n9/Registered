# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = '4399'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '4399小游戏'
    __url__ = 'http://www.4399.com/'

    def register(self, target):
        self.information = {
            'email': {
                'url': 'http://ptlogin.4399.com/ptlogin/isExist.do',
                'method': 'get',
                'settings': {
                    'params': {
                        'username': target,
                        'appId': 'www_home',
                        'regMode': 'reg_email',
                        'v': '2'
                    }
                },
                'result': {
                    'type': 'str',
                    'value': '\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe5\xb7\xb2\xe8\xa2\xab\xe6\xb3\xa8\xe5\x86\x8c'
                }
            },
            'username': {
                'url': 'http://ptlogin.4399.com/ptlogin/isExist.do',
                'method': 'get',
                'settings': {
                    'params': {
                        'username': target,
                        'appId': 'www_home',
                        'regMode': 'reg_normal',
                        'v': '1'
                    }
                },
                'result': {
                    'type': 'str',
                    'value': '\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe5\xb7\xb2\xe8\xa2\xab\xe6\xb3\xa8\xe5\x86\x8c'
                }
            }
        }
