import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# change that
ADMINS = frozenset(['mc@rybnet.pl'])  
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
#SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8
