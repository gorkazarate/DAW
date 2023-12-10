from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db=SQLAlchemy

db.create_all()
