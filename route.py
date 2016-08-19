# coding: utf-8

from Registered.handlers import index


route = []
route.append((r'^/$|^/index$', index.IndexHandler))
