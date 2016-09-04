# coding: utf-8

from common import base


class Plugin(base.BASE):

    __name__ = 'jj_user'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '竞技世界'
    __url__ = 'http://www.jj.cn/'

    def register(self, target):
        self.url = 'http://a4.act.jj.cn/my/check_general_loginname.php'
        self.method = 'get'
        self.settings = {
            'params': {
                'loginname': target
            }
        }
        self.resultType = 'str'
        self.resultValue = '{"msg":1}'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
