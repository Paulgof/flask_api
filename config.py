import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_api@127.0.0.1:5432/apidraft.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
