from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import perfil

Base = declarative_base()


class Conversacion(db.Model):
    id_conversacion = db.Column(db.Integer, primary_key=True)
    id_persona1 = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_persona1 = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_persona2 = db.Column(db.Integer)
    creado = db.Column(db.DateTime)

db.create_all()
