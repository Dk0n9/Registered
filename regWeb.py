# coding: utf-8

from lib import main

from flask import Flask
from flask import render_template
__author__ = 'DK'


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<account>')
def getAccount(account):
    result = main.Main(account).start()
    return render_template('search.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
