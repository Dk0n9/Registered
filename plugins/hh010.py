# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'hh010'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '鸿鹄论坛'
    __url__ = 'http://bbs.hh010.com/'

    def register(self, target):
        domain = target.split('@')
        if len(domain) == 1 or len(domain) > 2:
            return False
        self.information = {
            'username': {
                'url': 'http://bbs.hh010.com/forum.php',
                'method': 'get',
                'settings': {
                    'params': {
                        'mod': 'ajax',
                        'inajax': 'yes',
                        'infloat': 'register',
                        'handlekey': 'register',
                        'ajaxmenu': '1',
                        'action': 'checkusername',
                        'username': target
                    }
                },
                'result': {
                    'type': 'str',
                    'value': '\xb8\xc3\xd3\xc3\xbb\xa7\xc3'
                }
            }
        }
