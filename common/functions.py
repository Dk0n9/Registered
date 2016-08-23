# coding: utf-8

import os
import imp
import json

from Registered.config import conf


def loadPlugins():
    """
    遍历目录动态加载插件
    :return:
    """
    # TODO: 定时监控目录插件变化并重载;
    result = {}
    for name in os.listdir(conf.PLUGIN_DIR):
        if not name.endswith('.py') or name == '__init__.py':
            continue
        name = name.replace('.py', '')
        fp = imp.find_module(name, [conf.PLUGIN_DIR])
        tempObj = imp.load_module(name, *fp)
        if hasattr(tempObj, 'Plugin'):
            classObj = getattr(tempObj, 'Plugin')()  # 初始化
            result[classObj.__name__] = classObj
    return result


def objectToJson(obj):
    try:
        data = json.dumps(obj)
        return data
    except Exception, e:
        return False


def jsonToObject(string):
    try:
        data = json.loads(string)
        return data
    except Exception, e:
        return False
