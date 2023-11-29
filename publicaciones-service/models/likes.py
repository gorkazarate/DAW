from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Like(db.Model):
    id_like = db.Column(db.Integer, primary_key=True)
    id_usuarioorigen = db.Column(db.Integer)
    id_usuariodestino = db.Column(db.Integer)
    biografia = db.Column(db.String(255))
    fecha = db.Column(db.DateTime)

        
db.create_all()
