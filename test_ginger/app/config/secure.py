import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SECRET_KEY = '\xefa\xc6\xf9\xa4-\xf8X\xd3\xb4c4\xefr\x1b\xbd\x9b\xc9\xa1ua%Nn'
