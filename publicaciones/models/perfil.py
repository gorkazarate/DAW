from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from flask_restful import Resource
from __init__ import db

Base = declarative_base()
class Perfil(db.Model):
    __tablename__ = 'perfil'

    id_usuario = db.Column(String(20), primary_key=True) 
    nombre_completo = db.Column(db.String(255))
    cumpleaños = db.Column(db.Date)  # Corrected column name
    numerotlf = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    numlikes = db.Column(db.Integer)
    usuario_id = db.Column(db.String(250))

    def __init__(self, id_usuario, nombre_completo, cumpleaños, numerotlf, direccion, numlikes, usuario_id):
        self.id_usuario = id_usuario
        self.nombre_completo = nombre_completo
        self.cumpleaños = cumpleaños
        self.numerotlf = numerotlf
        self.direccion = direccion
        self.numlikes = numlikes
        self.usuario_id = usuario_id

    def obtener_likes(self):
        return db.session.query(func.sum(Perfil.numlikes)).filter_by(id_usuario=self.id_usuario).scalar() or 0

    def __repr__(self):
        return f'Perfil(id_usuario={self.id_usuario}, nombre_completo={self.nombre_completo}, cumpleaños={self.cumpleaños}, numerotlf={self.numerotlf}, direccion={self.direccion}, numlikes={self.numlikes}, usuario_id={self.usuario_id})'