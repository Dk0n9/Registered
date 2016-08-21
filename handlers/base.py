# coding: utf-8

import time
import threading
from Queue import Queue

from bson import ObjectId
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

from Registered import database
from Registered.config import conf
from Registered.common import functions


PLUGINS = functions.loadPlugins()


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

    def on_connection_close(self):
        BaseHandler.db.close()

    @property
    def getUserIp(self):
        return self.request.remote_ip

    @property
    def getNowTime(self):
        return int(time.time())  # 取十位

    @property
    def getPluginCount(self):
        return len(PLUGINS)

    def formatTime(self, timestamp, format='%Y-%m-%d %H:%M:%S'):
        timeObj = time.localtime(int(timestamp))
        return time.strftime(format, timeObj)

    def getObjectID(self, _id):
        return ObjectId(_id)


class SocketHandler(WebSocketHandler):

    _first_running = True
    db = None
    status = True
    taskQueue = Queue()

    def __init__(self, application, request, **kwargs):
        if BaseHandler._first_running:
            self._after_prefork()
            BaseHandler._first_running = False

        super(WebSocketHandler, self).__init__(application, request, **kwargs)

    def _after_prefork(self):
        BaseHandler.db = database.connect()

    def on_close(self):
        SocketHandler.status = False
        SocketHandler.db.close()

    def start(self, target):
        for num in range(conf.THREADS):
            thread = threading.Thread(target=self.__run, args=(target, ))
            thread.setDaemon(False)
            thread.start()

    def __run(self, target):
        while True:
            if not SocketHandler.status:
                break
            if SocketHandler.taskQueue.empty():
                break
            data = SocketHandler.taskQueue.get(False)
            data.register(target)
            result = data.verify()
            if result:
                self.write_message({
                    'title': data.__title__,
                    'url': data.__url__
                })
                self._updateTarget(data.__name__)

    def _updateTarget(self, obj):
        pass

    @property
    def getPlugins(self):
        return PLUGINS
