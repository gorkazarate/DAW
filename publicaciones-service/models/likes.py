from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from publicaciones_services import db  # Asegúrate de tener la importación correcta

Base = declarative_base()

class Like(db.Model):
    __tablename__ = 'likes'

    id_like = db.Column(dbInteger, primary_key=True)
    id_usuarioorigen = db.Column(db.Integer, db.ForeignKey('perfil.id_usuario'))
    id_usuariodestino = db.Column(db.Integer, db.ForeignKey('perfil.id_usuario'))

    def __init__(self, id_usuarioorigen, id_usuariodestino, biografia):
        self.id_usuarioorigen = id_usuarioorigen
        self.id_usuariodestino = id_usuariodestino

    def __repr__(self):
        return f'Like(id_like={self.id_like}, id_usuarioorigen={self.id_usuarioorigen}, id_usuariodestino={self.id_usuariodestino})'