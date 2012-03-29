from flask import Flask, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.http_session import SqlAlchemySessionInterface
app.session_interface = SqlAlchemySessionInterface()
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
  if not 'test' in session:
    session['test'] = 0;
  else:
    session['test'] = session['test'] + 1
  return render_template("index.html")
