# coding: utf-8
import urllib2

from lib import main

from flask import Flask
from flask import render_template
from flask import request
__author__ = 'DK'


app = Flask(__name__)
handle = main.Main()
handle.loads()


@app.route('/', methods=['GET'])
def index():
    if request.args.get('keyword'):
        result = handle.start(request.args.get('keyword'))
        return render_template('index.html', count=handle.count(), result=result)
    return render_template('index.html', count=handle.count())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8000)
