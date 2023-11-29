from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'perfil'

    Id_usuario = Column(Integer, primary_key=True)
    nombre_completo = Column(String)
    cumpleaño = Column(Date)
    numerotlf = Column(String)
    dirección = Column(String)
    user_id = Column(Integer, unique=True)