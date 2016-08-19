# coding: utf-8

import pymongo

from Registered.common.exceptions import (DBConnectionError,
                                           DBAuthenticatedError)


class DB(object):

    def __init__(self, host, port='27017', user=None, pwd=None, database=''):
        try:
            self._conn = pymongo.MongoClient(host=host, port=int(port), serverSelectionTimeoutMS=3000)
        except Exception, error:
            self._conn = None
            raise DBConnectionError('Host: {0} connection error: {1}'.format(host, error))
        self._db = self._conn.get_database(database)
        if user:
            if not self._db.authenticate(user, pwd):
                raise DBAuthenticatedError('Authentication failure')

    def get(self):
        return self._db

    def close(self):
        if self._conn:
            self._conn.close()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    test = DB(host='192.168.10.4', user='magicx', pwd='magicx', database='magicx').get()
    import datetime
    import time
    # print test.users.find_one({'name': 'test26'})['_id']
    for i in range(150, 200):
        time.sleep(2)
        print test.users.insert_one({
            'name': 'admin',
            'email': 'admin@qq.com',
            'passwd': '2d9562d8e9f6d1241b659c76ce2ea2b7ae8a4f5ba87cb97f528eb6d66e1c287b',  # raw: admin
            'salt': 'abcdefgh'
        })
        break
    print test.users.count()
