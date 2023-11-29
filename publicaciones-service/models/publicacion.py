from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publicacion(Base):
    __tablename__ = 'publicacion'

    idpost = Column(Integer, primary_key=True)
    Titulo = Column(String)
    texto = Column(String)
    empieza = Column(DateTime)
    termina = Column(DateTime)
    usuario_id = Column(Integer, ForeignKey('perfil.Id_usuario'))
    servicio_id = Column(Integer)

    usuario = relationship('Usuario')