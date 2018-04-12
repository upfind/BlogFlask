import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# 项目绝对路径
baseDir = os.path.abspath(os.path.dirname(__file__))

DATABASE = baseDir + '/data.sqlite'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
