from app import db
from flask.sessions import SessionMixin
from datetime import datetime

class SqlAlchemyHttpSesssion(db.Model, SessionMixin):
    __tablename__ = 'http_session'

    sid = db.Column(db.String(36), primary_key=True, unique=True)
    session = db.Column(db.PickleType(mutable=True))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    ip = db.Column(db.String(15))

    def __init__(self, sid):
        self.sid = sid
        self.session = {}
	self.new = True
	self.created_at = datetime.now()

    def __repr__(self):
       return "<http_session('%s')>" % (self.sid)

    def __setitem__(self, key, value):
       self.session[key] = value

    def __getitem__(self, key):
       return self.session[key]

    def __contains__(self, key):
       return key in self.session

    def get(self, key, default=None):
      if key in self.session:
        return self.session[key]
      else:
        return default

    def items(self):
      return self.session.items()
