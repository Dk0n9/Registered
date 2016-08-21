# coding: utf-8

from Registered.handlers import base
from Registered.common import functions


class IndexHandler(base.BaseHandler):

    def get(self, *args, **kwargs):
        pass


class InfoHandler(base.SocketHandler):

    def on_message(self, message):
        data = functions.jsonToObject(message)
        if not data:
            return None
        if not data.get('target') or not isinstance(data['target'], basestring):
            return None
        findRes = self.db.targets.find_one({'target': data['target']})
        if not findRes:
            result = self._insertTarget(data['target'])
            if not result:
                return None
        # 如果数据库中存在某些插件的记录就先输出, 再校验不存在记录的插件
        for pluginName in findRes['plugins']:
            tempObj = self.getPlugins.get(pluginName)
            # 防止插件名变动后与数据库中的记录不统一,所以移除数据库中已发生变更的插件记录
            if not tempObj:
                self._removePlugin(pluginName)
                continue
            self.write_message({
                'title': tempObj.__title__,
                'url': tempObj.__url__
            })
        diffList = list(set(self.getPlugins.keys()).difference(set(findRes['plugins'])))  # 差集
        if diffList:
            map(lambda x: self.taskQueue.put(self.getPlugins[x]), diffList)
            self.start(data['target'])

    def _insertTarget(self, target):
        insertRes = self.db.targets.insert_one({
            'target': target,
            'plugins': []
        })
        if insertRes.inserted_id:
            return True
        else:
            return False

    def _removePlugin(self, name):
        pass
