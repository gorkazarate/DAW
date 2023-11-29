from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


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