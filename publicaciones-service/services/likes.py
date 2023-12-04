from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import pymysql
from flask_restful import Resource

pymysql.install_as_MySQLdb()


class LikesResource(Resource):
    def get(self, id_like):
        like = Like.query.filter_by(id_like=id_like).first()
        if like:
            return {'id_usuarioorigen': like.id_usuarioorigen,
                    'id_usuariodestino': like.id_usuariodestino,
                    'biografia': like.biografia,
                    'fecha': str(like.fecha)}, 200
        else:
            return {'message': 'Like no encontrado'}, 404

    def post(self):
        data = request.get_json()

        nuevo_like = Like(id_usuarioorigen=data['id_usuarioorigen'],
                          id_usuariodestino=data['id_usuariodestino'],
                          biografia=data['biografia'],
                          fecha=data['fecha'])

        db.session.add(nuevo_like)
        try:
            db.session.commit()
            return {'message': 'Like creado exitosamente'}, 201
        except exc.IntegrityError:
            db.session.rollback()
            return {'message': 'Error: Ya existe un like con esos usuarios'}, 400

    def put(self, id_like):
        like = Like.query.filter_by(id_like=id_like).first()
        if like:
            data = request.get_json()

            like.id_usuarioorigen = data.get('id_usuarioorigen', like.id_usuarioorigen)
            like.id_usuariodestino = data.get('id_usuariodestino', like.id_usuariodestino)
            like.biografia = data.get('biografia', like.biografia)
            like.fecha = data.get('fecha', like.fecha)

            db.session.commit()

            return {'message': 'Like modificado exitosamente'}, 200
        else:
            return {'message': 'Like no encontrado'}, 404
