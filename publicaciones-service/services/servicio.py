from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


class ServicioResource(Resource):
    def get(self):
        servicios = Servicio.query.all()
        servicios_json = [{'servicio_id': servicio.servicio_id,
                            'titulo': servicio.titulo,
                            'foto': servicio.foto,
                            'descripcion': servicio.descripcion} for servicio in servicios]
        return {'servicios': servicios_json}

    def post(self):
        data = request.get_json()
        nuevo_servicio = Servicio(titulo=data['titulo'],
                                  foto=data['foto'],
                                  descripcion=data['descripcion'])
        db.session.add(nuevo_servicio)
        db.session.commit()
        return {'message': 'Servicio creado exitosamente'}, 201
