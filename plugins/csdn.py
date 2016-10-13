# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'csdn'
    __title__ = 'CSDN'
    __url__ = 'http://www.csdn.net/'

    def register(self, target):
        self.information = {
            'email': {
                'url': 'http://passport.csdn.net/account/register',
                'method': 'get',
                'settings': {
                    'params': {
                        'action': 'validateEmail',
                        'email': target
                    }
                },
                'result': {
                    'type': 'str',
                    'value': 'false'
                }
            }
        }


