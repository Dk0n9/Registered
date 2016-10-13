# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = '17173game'
    __title__ = '17173小游戏'
    __url__ = 'http://www.17173.com/'

    def register(self, target):
        temp = target.split('@')
        if len(temp) == 1 or len(temp) > 2:
            return False
        self.information = {
            'username': {
                'url': 'http://passport.17173.com/register/validate?field=username',
                'method': 'get',
                'settings': {
                    'params': {
                        'value': target,
                        'domain': temp[1]
                    }
                },
                'result': {
                    'type': 'json',
                    'value': 'status=0'
                }
            }
        }