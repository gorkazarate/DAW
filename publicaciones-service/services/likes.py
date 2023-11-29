from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Like(Base):
    __tablename__ = 'likes'

    Id_like = Column(Integer, primary_key=True)
    Id_usuarioorigen = Column(Integer)
    Id_usuariodestino = Column(Integer)
    biografia = Column(String)
    Fecha = Column(DateTime)