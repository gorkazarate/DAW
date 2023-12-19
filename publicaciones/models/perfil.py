from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from flask_restful import Resource
from __init__ import db

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


class Usuario(db.Model):
    __tablename__ = 'perfil'

    Id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String)
    cumpleaños = db.Column(db.Date)
    numerotlf = db.Column(db.String)
    dirección = db.Column(db.String)
    numlikes = db.Column(db.Integer)
    usuario_id = db.Column(db.String, unique=True)

    def __init__(self, username, cumpleaños, numerotlf,numlikes, direccion, usuario_id):
        self.nombre_completo = username
        self.cumpleaños = cumpleaños
        self.numerotlf = numerotlf
        self.dirección = direccion
        self.numlikes = numlikes
        self.usuario_id = usuario_id

    def __repr__(self):
        return f'Usuario(Id_usuario={self.Id_usuario}, nombre_completo={self.nombre_completo}, cumpleaño={self.cumpleaño}, numerotlf={self.numerotlf}, dirección={self.dirección}, numlikes={self.numlikes}, usuario_id={self.usuario_id})'

