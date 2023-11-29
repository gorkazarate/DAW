from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Mensaje(db.Model):
    id_mensaje = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.String(255))
    emisor_id = db.Column(db.Integer)
    conversacion_id = db.Column(db.Integer, db.ForeignKey('conversacion.id_conversacion'))
    fecha_envio = db.Column(db.DateTime)

    conversacion = db.relationship('Conversacion', backref=db.backref('mensajes', lazy=True))

db.create_all()
