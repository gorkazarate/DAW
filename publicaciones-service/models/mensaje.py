from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base



class Mensaje(Base):
    __tablename__ = 'mensaje'

    id_mensaje = Column(Integer, primary_key=True)
    contenido = Column(String)
    emisor_id = Column(Integer)
    fecha_envio = Column(DateTime)
    conversacion_id = Column(Integer, ForeignKey('conversacion.id_conversacion'))

    conversacion = relationship('Conversacion')

db.create_all()
