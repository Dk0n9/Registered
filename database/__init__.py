# coding: utf-8

import importlib

from config import conf


def connect():
    driverModule = importlib.import_module('.' + conf.DATABASE_DRIVER, package='database')
    dbConfig = {
        'host': conf.DATABASE_HOST,
        'port': conf.DATABASE_PORT,
        'user': conf.DATABASE_USER,
        'pwd': conf.DATABASE_PASS,
        'database': conf.DATABASE_DB
    }
    driver = driverModule.DB(**dbConfig)
    return driver.get()
