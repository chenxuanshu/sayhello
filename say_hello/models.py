'''
@Author: your name
@Date: 2020-05-23 09:05:11
@LastEditTime: 2020-05-23 14:31:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\models.py
'''
from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

