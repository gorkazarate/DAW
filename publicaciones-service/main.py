from flask import Flask, render_template, redirect, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from flask import (render_template,Blueprint,flash, g, redirect, request,url_for)
from __init__ import app
from views.blog import blog

import json
import os

with open('../keys.json') as f:
  keys = json.load(f)
   
api = Api(app)




app.register_blueprint(blog)

with app.app_context():
    DBSession = sessionmaker(bind=db.engine)
    session = DBSession()

if __name__ == '__main__':
    app.run(debug=True, port=8000)