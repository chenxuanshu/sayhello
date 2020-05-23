'''
@Author: your name
@Date: 2020-05-23 09:04:57
@LastEditTime: 2020-05-23 14:33:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\__init__.py
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands
