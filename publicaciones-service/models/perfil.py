from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Usuario(Base):
    __tablename__ = 'usuario'  # Ajusta este nombre según tu base de datos

    Id_usuario = Column(Integer, primary_key=True)
    nombre_completo = Column(String)
    cumpleaño = Column(Date)
    numerotlf = Column(String)
    dirección = Column(String)
    user_id = Column(Integer, unique=True)


db.create_all()
