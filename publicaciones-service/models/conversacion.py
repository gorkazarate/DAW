from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Conversacion(Base):
    __tablename__ = 'conversacion'

    id_conversacion = Column(Integer, primary_key=True)
    id_persona1 = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_persona2 = Column(Integer, ForeignKey('usuario.id_usuario'))
    creado = Column(DateTime, default=datetime.utcnow)
