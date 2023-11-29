from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Like(Base):
    __tablename__ = 'likes'

    id_like = Column(Integer, primary_key=True)
    id_usuarioorigen = Column(Integer)
    id_usuariodestino = Column(Integer)
    biografia = Column(String)
    fecha = Column(DateTime)


db.create_all()
