from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from flask_restful import Resource

import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'  # Ajusta este nombre según tu base de datos

    Id_usuario = Column(Integer, primary_key=True)
    nombre_completo = Column(String)
    cumpleaño = Column(Date)
    numerotlf = Column(String)
    dirección = Column(String)
    user_id = Column(Integer, unique=True)


class PerfilResource(Resource):
    def get(self, id_usuario):
        perfil = Usuario.query.filter_by(Id_usuario=id_usuario).first()
        if perfil:
            return {'nombre_completo': perfil.nombre_completo,
                    'cumpleaño': str(perfil.cumpleaño),
                    'numerotlf': perfil.numerotlf,
                    'dirección': perfil.dirección,
                    'user_id': perfil.user_id}, 200
        else:
            return {'message': 'Perfil no encontrado'}, 404

    def post(self):
        data = request.get_json()

        nuevo_perfil = Usuario(nombre_completo=data['nombre_completo'],
                               cumpleaño=data['cumpleaño'],
                               numerotlf=data['numerotlf'],
                               dirección=data['dirección'],
                               user_id=data['user_id'])

        db.session.add(nuevo_perfil)
        try:
            db.session.commit()
            return {'message': 'Perfil creado exitosamente'}, 201
        except exc.IntegrityError:
            db.session.rollback()
            return {'message': 'Error: Ya existe un perfil con ese user_id'}, 400

    def put(self, id_usuario):
        perfil = Usuario.query.filter_by(Id_usuario=id_usuario).first()
        if perfil:
            data = request.get_json()

            perfil.nombre_completo = data.get('nombre_completo', perfil.nombre_completo)
            perfil.cumpleaño = data.get('cumpleaño', perfil.cumpleaño)
            perfil.numerotlf = data.get('numerotlf', perfil.numerotlf)
            perfil.dirección = data.get('dirección', perfil.dirección)
            perfil.user_id = data.get('user_id', perfil.user_id)

            db.session.commit()

            return {'message': 'Perfil modificado exitosamente'}, 200
        else:
            return {'message': 'Perfil no encontrado'}, 404
