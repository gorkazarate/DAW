from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Conversacion(Base):
    __tablename__ = 'conversacion'

    id_conversacion = Column(Integer, primary_key=True)
    id_persona1 = Column(Integer, ForeignKey('perfil.Id_usuario'))
    id_persona2 = Column(Integer, ForeignKey('perfil.Id_usuario'))
    Creado = Column(DateTime)

    persona1 = relationship('Usuario', foreign_keys=[id_persona1])
    persona2 = relationship('Usuario', foreign_keys=[id_persona2])