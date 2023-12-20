from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from __init__ import db
from models.servicio import Servicio 
from models.perfil import Perfil 


class Publicacion(db.Model):
    __tablename__ = 'publicacion'  # Ajusta este nombre según tu base de datos

    idpost = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Titulo = db.Column(db.String)
    texto = db.Column(db.String)
    fechas = db.Column(db.String)
    empieza = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.String, db.ForeignKey('perfil.usuario_id'))
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicio.servicio_id'))
    servicio = db.relationship('Servicio', backref=db.backref('publicaciones', lazy=True))




    def __init__(self, Titulo, texto,empieza, fechas,usuario_id, servicio_id):
        self.Titulo = Titulo
        self.texto = texto
        self.fechas = fechas
        self.empieza=empieza
        self.usuario_id = usuario_id
        self.servicio_id = servicio_id

    def __repr__(self):
        return f"Publicacion(idpost={self.idpost}, Titulo='{self.Titulo}',empieza='{self.empieza}' texto='{self.texto}', fechas={self.fechas}, usuario_id={self.usuario_id}, servicio_id={self.servicio_id})"

