from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import pymysql
from flask_restful import Resource

pymysql.install_as_MySQLdb()

class MensajeResource(Resource):
    def get(self, id_mensaje):
        mensaje = Mensaje.query.filter_by(id_mensaje=id_mensaje).first()
        if mensaje:
            return {'contenido': mensaje.contenido,
                    'emisor_id': mensaje.emisor_id,
                    'conversacion_id': mensaje.conversacion_id,
                    'fecha_envio': str(mensaje.fecha_envio)}, 200
        else:
            return {'message': 'Mensaje no encontrado'}, 404

    def post(self):
        data = request.get_json()

        # Obtener o crear la conversación entre dos usuarios
        conversacion = Conversacion.query.filter(
            (Conversacion.id_persona1 == data['id_persona1'] and Conversacion.id_persona2 == data['id_persona2']) |
            (Conversacion.id_persona1 == data['id_persona2'] and Conversacion.id_persona2 == data['id_persona1'])
        ).first()

        if not conversacion:
            nueva_conversacion = Conversacion(id_persona1=data['id_persona1'],
                                              id_persona2=data['id_persona2'],
                                              creado=data['creado'])
            db.session.add(nueva_conversacion)
            db.session.commit()
            conversacion = nueva_conversacion

        nuevo_mensaje = Mensaje(contenido=data['contenido'],
                               emisor_id=data['emisor_id'],
                               conversacion_id=conversacion.id_conversacion,
                               fecha_envio=data['fecha_envio'])

        db.session.add(nuevo_mensaje)
        db.session.commit()

        return {'message': 'Mensaje creado exitosamente'}, 201
