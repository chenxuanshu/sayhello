'''
@Author: your name
@Date: 2020-05-23 09:05:16
@LastEditTime: 2020-05-23 11:09:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\forms.py
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
