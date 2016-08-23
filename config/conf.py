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
    'debug': True
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
TIMEOUT = 5  # (s)
PLUGIN_DIR = os.path.abspath(os.path.dirname(__file__) + '/../plugins/').replace('\\', '/')
