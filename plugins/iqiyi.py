# coding: utf-8
__author__ = 'Stanla'

from common import base


class Plugin(base.BASE):

    __name__ = 'iqiyi'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '爱奇艺'
    __url__ = 'http://www.iqiyi.com/'

    def register(self, target):
        self.information = {
            'username': {
                'url': 'http://passport.iqiyi.com/apis/user/check_account.action',
                'method': 'get',
                'settings': {
                    'params': {
                        'account': target,
                    },
                    'headers': {
                        'user-agent': self.getRandomAgent(),
                        'referer': 'http://vip.iqiyi.com/'
                    }
                },
                'result': {
                    'type': 'json',
                    'value': 'data=true'
                }
            }
        }
