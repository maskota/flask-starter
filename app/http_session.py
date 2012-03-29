from flask.sessions import SessionInterface
from flask import request
from uuid import uuid4
from datetime import datetime
from app.models import SqlAlchemyHttpSesssion
from app import db

class SqlAlchemySessionInterface(SessionInterface):

  def generate_sid(self):
    return str(uuid4())
  
  def open_session(self, app, request):
    sid = request.cookies.get(app.session_cookie_name)
    if not sid:
      sid = self.generate_sid()
      sess = SqlAlchemyHttpSesssion(sid)
      return sess
    else:
      sess = SqlAlchemyHttpSesssion.query.get(sid)
      if sess is not None:
        return sess
      else: 
	return SqlAlchemyHttpSesssion(sid)

  def save_session(self, app, http_session, response):
    domain = self.get_cookie_domain(app)
    cookie_exp = self.get_expiration_time(app, http_session)
    response.set_cookie(app.session_cookie_name, http_session.sid,
                        expires=cookie_exp, httponly=True,
                        domain=domain)
    http_session.updated_at = datetime.now()
    http_session.ip = request.remote_addr
    if http_session.new:
      db.session.add(http_session)
    db.session.commit()
