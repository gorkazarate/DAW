from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class Servicio(Base):
    __tablename__ = 'servicio'  # Ajusta este nombre según tu base de datos

    servicio_id = Column(Integer, primary_key=True)
    titulo = Column(String)
    foto = Column(String)
    descripcion = Column(String)


db.create_all()
