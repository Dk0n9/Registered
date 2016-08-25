# coding: utf-8

import logging

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.log import access_log

from config import conf
import route


class Application(tornado.web.Application):
    def __init__(self):
        if conf.SETTINGS.get('access_log'):
            access_log.setLevel(logging.INFO)
        tornado.web.Application.__init__(self, route.route, **conf.SETTINGS)


def main():
    print """
    ____             _      __                     __
   / __ \___  ____ _(_)____/ /____  ________  ____/ /
  / /_/ / _ \/ __ `/ / ___/ __/ _ \/ ___/ _ \/ __  /
 / _, _/  __/ /_/ / (__  ) /_/  __/ /  /  __/ /_/ /
/_/ |_|\___/\__, /_/____/\__/\___/_/   \___/\__,_/  v0.2.1
           /____/
"""
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(conf.PORT, conf.HOST)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
