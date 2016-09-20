# coding: utf-8
"""
插件测试脚本
注意：要测试的插件文件需要放置在config/conf.py文件中指定的插件存放路径
使用方法:
    python PluginTest.py -p "插件文件名(不需要后缀)" -t "需要测试的用户名/邮箱/手机"
"""

import imp
import argparse

from config import conf


def parse_args():
    parser = argparse.ArgumentParser()

    pluginHelp = 'plugin file name.'
    parser.add_argument('-p','--plugin', help=pluginHelp)

    targetHelp = 'your target.'
    parser.add_argument('-t', '--target', help=targetHelp)

    args = parser.parse_args()
    return args


def run(plugin, target):
    if plugin.endswith('.py'):
        plugin = plugin.replace('.py', '')
    try:
        fp = imp.find_module(plugin, [conf.PLUGIN_DIR])
        tempObj = imp.load_module(plugin, *fp)
    except ImportError:
        print '\033[1;31m[!] plugin: {0} not found!'.format(conf.PLUGIN_DIR + '/' + plugin + '.py')
        return False
    except Exception, e:
        print '\033[1;31m[!] Exception: {0}'.format(e)
        return False
    if hasattr(tempObj, 'Plugin'):
        classObj = getattr(tempObj, 'Plugin')()  # 初始化
        classObj.register(target)
        result = classObj.verify()
        if result:
            print '\033[1;32m[+] {0} is found!'.format(target)
        else:
            print '\033[1;33m[-] {0} not found!'.format(target)
    else:
        print '\033[1;31m[!] {0} ClassException: Plugin not found!'.format(plugin)
        return False


if __name__ == '__main__':
    args = parse_args()
    run(args.plugin, args.target)
