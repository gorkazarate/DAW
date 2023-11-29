from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Servicio(db.Model):
    servicio_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    foto = db.Column(db.String(255))
    descripcion = db.Column(db.String(1000))


db.create_all()
