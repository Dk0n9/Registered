# coding: utf-8

from handlers import base
from common import functions


class IndexHandler(base.BaseHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')


class InfoHandler(base.SocketHandler):

    def on_message(self, message):
        data = functions.jsonToObject(message)
        if not data:
            return None
        if not data.get('target') or not isinstance(data['target'], basestring):
            return self.write_message('done')
        base.SocketHandler.status = True  # 重置查询状态
        findRes = self.db.targets.find_one({'target': data['target']})
        if not findRes:
            result = self._insertTarget(data['target'])
            if not result:
                return self.write_message('done')
            findRes = {'plugins': []}
        # 如果数据库中存在某些插件的记录就先输出, 再校验不存在记录的插件
        for pluginName in findRes['plugins']:
            tempObj = self.getPlugins.get(pluginName)
            # 防止插件名变动后与数据库中的记录不统一,所以移除数据库中已发生变更的插件记录
            if not tempObj:
                self._removePlugin(data['target'], pluginName)
                continue
            self.write_message({
                'title': tempObj.__title__,
                'url': tempObj.__url__
            })
        # 计算差集,然后使用数据库中不存在记录的插件进行校验
        diffList = list(set(self.getPlugins.keys()).difference(set(findRes['plugins'])))
        if diffList:
            map(lambda x: self.taskQueue.put(self.getPlugins[x]), diffList)
            self.start(data['target'])
        else:
            self.write_message('done')

    def _insertTarget(self, target):
        insertRes = self.db.targets.insert_one({
            'target': target,
            'plugins': []
        })
        if insertRes.inserted_id:
            return True
        else:
            return False

    def _removePlugin(self, target, name):
        updateRes = self.db.targets.update_one({
            'target': target
        }, {
            '$pull': {
                'plugins': name
            }
        })
        if updateRes.modified_count:
            return True
        else:
            return False
