from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from publicaciones_services import db


class Conversacion(db.Model):
    __tablename__ = 'conversacion'

    id_conversacion = db.Column(db.Integer, primary_key=True)
    id_persona1 = db.Column(db.Integer, db.ForeignKey('perfil.id_usuario'))
    id_persona2 = db.Column(db.Integer, db.ForeignKey('perifl.id_usuario'))
    creado = db.Column(db.DateTime, default=datetime.utcnow)
  
    def __init__(self, id_persona1, id_persona2):
        self.id_persona1 = id_persona1
        self.id_persona2 = id_persona2

    def __repr__(self):
        return f'Conversacion(id_conversacion={self.id_conversacion}, id_persona1={self.id_persona1}, id_persona2={self.id_persona2}, creado={self.creado})'

db.create_all()
