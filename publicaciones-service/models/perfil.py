from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(255))
    cumpleano = db.Column(db.Date)
    numerotlf = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    user_id = db.Column(db.Integer, unique=True)


db.create_all()
