from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import pymysql
from flask_restful import Resource

pymysql.install_as_MySQLdb()

class ConversacionResource(Resource):
    def get(self, id_conversacion):
        conversacion = Conversacion.query.filter_by(id_conversacion=id_conversacion).first()
        if conversacion:
            return {'id_persona1': conversacion.id_persona1,
                    'id_persona2': conversacion.id_persona2,
                    'creado': str(conversacion.creado)}, 200
        else:
            return {'message': 'Conversación no encontrada'}, 404

    def post(self):
        data = request.get_json()

        nueva_conversacion = Conversacion(id_persona1=data['id_persona1'],
                                          id_persona2=data['id_persona2'],
                                          creado=data['creado'])

        db.session.add(nueva_conversacion)
        try:
            db.session.commit()
            return {'message': 'Conversación creada exitosamente'}, 201
        except exc.IntegrityError:
            db.session.rollback()
            return {'message': 'Error: Ya existe una conversación con esos participantes'}, 400

    def put(self, id_conversacion):
        conversacion = Conversacion.query.filter_by(id_conversacion=id_conversacion).first()
        if conversacion:
            data = request.get_json()

            conversacion.id_persona1 = data.get('id_persona1', conversacion.id_persona1)
            conversacion.id_persona2 = data.get('id_persona2', conversacion.id_persona2)
            conversacion.creado = data.get('creado', conversacion.creado)

            db.session.commit()

            return {'message': 'Conversación modificada exitosamente'}, 200
        else:
            return {'message': 'Conversación no encontrada'}, 404
