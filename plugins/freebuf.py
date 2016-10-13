# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'freebuf'
    __title__ = 'FreeBuf黑客与极客'
    __url__ = 'http://www.freebuf.com/'

    def register(self, target):
        self.information = {
            'username': {
                'url': 'https://account.tophant.com/register/sendmail',
                'method': 'post',
                'settings': {
                    'data': {
                        'mail': target,
                    },
                    'headers': {
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                },
                'result': {
                    'type': 'json',
                    'value': 'msg=\xe6\xb3\xa8\xe5\x86\x8c\xe9\x82\xae\xe7\xae\xb1\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8'
                }
            }
        }
