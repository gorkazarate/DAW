from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from publicaciones_services import db  # Asegúrate de tener la importación correcta

Base = declarative_base()

class Mensaje(db.Model):
    __tablename__ = 'mensaje'

    id_mensaje = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.String)
    emisor_id = db.Column(db.Integer)
    fecha_envio = db.Column(db.DateTime, default=datetime.utcnow)
    conversacion_id = db.Column(db.Integer, db.ForeignKey('conversacion.id_conversacion'))

    conversacion = relationship('Conversacion')

    def __init__(self, contenido, emisor_id, conversacion_id):
        self.contenido = contenido
        self.emisor_id = emisor_id
        self.conversacion_id = conversacion_id

    def __repr__(self):
        return f'Mensaje(id_mensaje={self.id_mensaje}, contenido={self.contenido}, emisor_id={self.emisor_id}, fecha_envio={self.fecha_envio}, conversacion_id={self.conversacion_id})'
