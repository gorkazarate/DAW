from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Servicio(Base):
    __tablename__ = 'servicio'  # Ajusta este nombre según tu base de datos

    servicio_id = Column(Integer, primary_key=True)
    titulo = Column(String)
    foto = Column(String)
    descripcion = Column(String)


