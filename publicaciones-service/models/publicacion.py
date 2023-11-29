from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class Publicacion(Base):
    __tablename__ = 'publicacion'  # Ajusta este nombre según tu base de datos

    idpost = Column(Integer, primary_key=True)
    Titulo = Column(String)
    texto = Column(String)
    empieza = Column(DateTime)
    termina = Column(DateTime)
    usuario_id = Column(Integer, ForeignKey('perfil.Id_usuario'))
    servicio_id = Column(Integer)

    usuario = relationship('Usuario')
db.create_all()
