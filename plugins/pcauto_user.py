# coding: utf-8

from Registered.common import base


class Plugin(base.BASE):

    __name__ = 'pcauto_email'  # 只能使用字母、数字、英文下划线命名, 字母开头
    __title__ = '太平洋汽车网'
    __url__ = 'http://www.pcauto.com.cn/'

    def register(self, target):
        self.url = 'http://passport3.pcauto.com.cn/passport3/api/validate_account.jsp?req_enc=UTF-8'
        self.method = 'get'
        self.settings = {
            'data': {
                'username': target,
                'recommendNum': '4'
            }
        }
        self.resultType = 'json'
        self.resultValue = 'status=8'


if __name__ == '__main__':
    test = Plugin()
    test.register('xxx')
    print test.verify()
