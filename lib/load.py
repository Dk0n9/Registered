# coding: utf-8
import imp
import os
__author__ = 'DK'


def load():
    """
    遍历 plugins目录下的所有文件并动态加载
    :return: dict
    """
    result = {}
    path = os.path.abspath('./plugins/').replace('\\', '/')
    for name in os.listdir(path):
        if not name.endswith('.py') or name == '__init__.py':
            continue
        name = name.replace('.py', '')
        fp = imp.find_module(name, [path])
        tempObj = imp.load_module(name, *fp)
        if hasattr(tempObj, 'getConfig'):
            result[name] = tempObj
    return result


def count():
    num = 0
    path = os.path.abspath('./plugins/').replace('\\', '/')
    for name in os.listdir(path):
        if not name.endswith('.py') or name == '__init__.py':
            continue
        num += 1
    return num
