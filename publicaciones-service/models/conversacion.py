from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class Conversacion(Base):
    __tablename__ = 'conversacion'

    id_conversacion = Column(Integer, primary_key=True)
    id_persona1 = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_persona2 = Column(Integer, ForeignKey('usuario.id_usuario'))
    creado = Column(DateTime, default=datetime.utcnow)
