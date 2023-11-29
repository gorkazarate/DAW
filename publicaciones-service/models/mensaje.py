from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Mensaje(Base):
    __tablename__ = 'mensaje'

    id_mensaje = Column(Integer, primary_key=True)
    contenido = Column(String)
    emisorid = Column(Integer, ForeignKey('perfil.Id_usuario'))
    conversacion_id = Column(Integer, ForeignKey('conversacion.id_conversacion'))
    fenvio = Column(DateTime)

    emisor = relationship('Usuario')
    conversacion = relationship('Conversacion')