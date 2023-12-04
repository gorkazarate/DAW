from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Mensaje(Base):
    __tablename__ = 'mensaje'

    id_mensaje = Column(Integer, primary_key=True)
    contenido = Column(String)
    emisor_id = Column(Integer)
    fecha_envio = Column(DateTime)
    conversacion_id = Column(Integer, ForeignKey('conversacion.id_conversacion'))

    conversacion = relationship('Conversacion')

