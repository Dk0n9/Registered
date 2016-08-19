# coding: utf-8

import os
import time

from tornado.web import RequestHandler
from bson import ObjectId

from Registered import database


class BaseHandler(RequestHandler):

    _first_running = True
    db = None

    def __init__(self, application, request, **kwargs):
        if BaseHandler._first_running:
            self._after_prefork()
            BaseHandler._first_running = False

        super(BaseHandler, self).__init__(application, request, **kwargs)

    def _after_prefork(self):
        BaseHandler.db = database.connect()

    @property
    def getUserIp(self):
        return self.request.remote_ip

    @property
    def getNowTime(self):
        return int(time.time())  # 取十位

    @property
    def getPluginsCount(self):
        num = 0
        path = os.path.abspath('../plugins/').replace('\\', '/')
        for name in os.listdir(path):
            if not name.endswith('.py') or name == '__init__.py':
                continue
            num += 1
        return num

    def formatTime(self, timestamp, format='%Y-%m-%d %H:%M:%S'):
        timeObj = time.localtime(int(timestamp))
        return time.strftime(format, timeObj)

    def getObjectID(self, _id):
        return ObjectId(_id)
