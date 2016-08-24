# coding: utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop

from config import conf
import route


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, route.route, **conf.SETTINGS)


def main():
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(conf.PORT, conf.HOST)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
