# coding: utf-8

import os
import imp


def loadPlugins():
    """
    遍历目录动态加载插件
    :return:
    """
    # TODO: 定时监控目录插件变化并重载;
    result = {}
    path = os.path.abspath(os.path.dirname(__file__) + '/../plugins/').replace('\\', '/')
    for name in os.listdir(path):
        if not name.endswith('.py') or name == '__init__.py':
            continue
        name = name.replace('.py', '')
        fp = imp.find_module(name, [path])
        tempObj = imp.load_module(name, *fp)
        if hasattr(tempObj, 'Plugin'):
            result[name] = getattr(tempObj, 'Plugin')
    return result


def getPluginCount():
    files = os.listdir(os.path.abspath(os.path.dirname(__file__) + '/../plugins/').replace('\\', '/'))
    result = []
    map(lambda x: result.append(x) if x.endswith('.py') and not x.startswith('__init__') else False, files)
    return len(result)

