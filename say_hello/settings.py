'''
@Author: your name
@Date: 2020-05-23 09:05:25
@LastEditTime: 2020-05-23 09:13:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\settings.py
'''
import os

from sayhello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

