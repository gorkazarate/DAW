from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from flask_restful import Resource
from publicaciones-services import db

import pymysql
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from publicaciones_services import db


class Usuario(db.Model):
    __tablename__ = 'perfil'

    Id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String)
    cumpleaño = db.Column(db.Date)
    numerotlf = db.Column(db.String)
    dirección = db.Column(db.String)
    numlikes = db.Column(db.Integer)
    user_id = eb.Column(db.Integer, unique=True)

    def __init__(self, username, cumpleaño, numerotlf,numlikes, direccion, user_id):
        self.nombre_completo = username
        self.cumpleaño = cumpleaño
        self.numerotlf = numerotlf
        self.dirección = direccion
        self.numlikes = numlikes
        self.user_id = user_id

    def __repr__(self):
        return f'Usuario(Id_usuario={self.Id_usuario}, nombre_completo={self.nombre_completo}, cumpleaño={self.cumpleaño}, numerotlf={self.numerotlf}, dirección={self.dirección}, numlikes={self.numlikes}, user_id={self.user_id})'