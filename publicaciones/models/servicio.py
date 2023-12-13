from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from __init__ import db
from sqlalchemy import CheckConstraint


class Servicio(db.Model):
    __tablename__ = 'servicio'

    servicio_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    foto = db.Column(db.String)
    descripcion = db.Column(db.String)


    __table_args__ = (
        CheckConstraint('servicio_id IN (1, 2, 3)', name='check_servicio_id'),
    )

    def __init__(self, titulo, foto, descripcion):
        self.titulo = titulo
        self.foto = foto
        self.descripcion = descripcion

    def __repr__(self):
        return f"Servicio(servicio_id={self.servicio_id}, titulo='{self.titulo}', foto='{self.foto}', descripcion='{self.descripcion}')"

