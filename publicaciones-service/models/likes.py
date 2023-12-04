from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Like(Base):
    __tablename__ = 'likes'

    id_like = Column(Integer, primary_key=True)
    id_usuarioorigen = Column(Integer)
    id_usuariodestino = Column(Integer)
    biografia = Column(String)
    fecha = Column(DateTime)


