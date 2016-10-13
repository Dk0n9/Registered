# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'baidu'
    __title__ = '百度'
    __url__ = 'https://www.baidu.com/'

    def register(self, target):
        self.information = {
            'username': {
                'url': 'https://passport.baidu.com/v2/?regnamesugg',
                'method': 'get',
                'settings': {
                    'params': {
                        'tpl': 'mn',
                        'apiver': 'v3',
                        'username': target
                    }
                },
                'result': {
                    'type': 'json',
                    'value': 'data.userExsit=1'
                }
            }
        }
