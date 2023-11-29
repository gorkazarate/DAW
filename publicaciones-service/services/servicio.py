from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Servicio(Base):
    __tablename__ = 'servicio'

    servicio_id = Column(Integer, primary_key=True)
    titulo = Column(String)
    foto = Column(String)
    descripcion = Column(String)