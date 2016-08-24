# coding: utf-8

from handlers import index


route = []
route.append((r'^/$', index.IndexHandler))
route.append((r'^/info$', index.InfoHandler))
