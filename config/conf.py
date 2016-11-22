# coding: utf-8

import os


# WEBSITE CONFIG #
HOST = 'localhost'
PORT = 8888

# APPLICATION CONFIG #
SETTINGS = {
    'template_path': os.path.join(os.path.dirname(__file__), '../templates'),
    'static_path': os.path.join(os.path.dirname(__file__), '../static'),
    'cookie_secret': '!@#$%^&*()_+',
    'xsrf_cookies': True,
    'debug': False,
    'access_log': True
}

# DATABASE CONFIG #
DATABASE_DRIVER = 'mongodb'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '27017'
DATABASE_USER = ''
DATABASE_PASS = ''
DATABASE_DB = 'registered'

# PLUGIN CONFIG #
THREADS = 5
REQUEST_TIMEOUT = 5  # (s)
REQUEST_RETRIES = 10
REQUEST_VERIFY = True
REQUEST_STREAM = False
PLUGIN_DIR = os.path.abspath(os.path.dirname(__file__) + '/../plugins/').replace('\\', '/')
