# coding: utf-8

from MagicX.handlers.index import index
from MagicX.handlers.index import user


route = []
route.append((r'^/$|^/index$', index.IndexIndexHandler))
route.append((r'^/login$', user.UserLoginHandler))
route.append((r'^/logout$', user.UserLogoutHandler))
route.append((r'^/reset', user.UserResetHandler))
route.append((r'^/register$', user.UserRegisterHandler))
