# encoding:utf-8

from flask_sqlalchemy import SQLAlchemy
from  flask_login import LoginManager
from flask_openid import OpenID

db = SQLAlchemy()

lm = LoginManager
oid = OpenID()
