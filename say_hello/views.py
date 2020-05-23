'''
@Author: your name
@Date: 2020-05-23 09:05:04
@LastEditTime: 2020-05-23 14:14:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\views.py
'''
from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form = form, messages=messages)
