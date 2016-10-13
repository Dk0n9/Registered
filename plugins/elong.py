# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'elong'
    __title__ = '艺龙旅行网'
    __url__ = 'http://www.elong.com/'

    def register(self, target):
        self.information = {
            'email': {
                'url': 'https://secure.elong.com/passport/isajax/Register/ValidateMobileOrEmail',
                'method': 'get',
                'settings': {
                    'params': {
                        'mobile': target,
                    }
                },
                'result': {
                    'type': 'json',
                    'value': 'value=1'
                }
            }
        }