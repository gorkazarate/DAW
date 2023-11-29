from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

class PublicacionResource(Resource):
    def get(self):
        publicaciones = Publicacion.query.all()
        publicaciones_json = [{'idpost': publicacion.idpost,
                               'Titulo': publicacion.Titulo,
                               'texto': publicacion.texto,
                               'empieza': str(publicacion.empieza),
                               'termina': str(publicacion.termina),
                               'usuario_id': publicacion.usuario_id,
                               'servicio_id': publicacion.servicio_id} for publicacion in publicaciones]
        return {'publicaciones': publicaciones_json}

    def post(self):
        data = request.get_json()
        nueva_publicacion = Publicacion(Titulo=data['Titulo'],
                                        texto=data['texto'],
                                        empieza=datetime.strptime(data['empieza'], '%Y-%m-%dT%H:%M:%S'),
                                        termina=datetime.strptime(data['termina'], '%Y-%m-%dT%H:%M:%S'),
                                        usuario_id=data['usuario_id'],
                                        servicio_id=data['servicio_id'])
        db.session.add(nueva_publicacion)
        db.session.commit()
        return {'message': 'Publicación creada exitosamente'}, 201
