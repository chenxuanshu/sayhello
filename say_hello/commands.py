'''
@Author: your name
@Date: 2020-05-23 10:51:40
@LastEditTime: 2020-05-23 18:24:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \sayhello\sayhello\commands.py
'''
import click
from sayhello import db, app
from sayhello.models import Message

@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized databse')

@app.cli.command()
@click.option('--count', default=20, help='a amount of messages, default is 20')
def forge(count):
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker()
    click.echo('working...')
    for i in range(count):
        message = Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('created %d messages' % count)