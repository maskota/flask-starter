import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# change that
ADMINS = frozenset(['mc@rybnet.pl'])  
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8
