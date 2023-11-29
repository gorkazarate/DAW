from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import perfil, like, conversacion, mensaje, publicacion,servicio

app = Flask(__name__)
api = Api(app)

# Conectar con la base de datos

# Configuración de la base de datos (ajusta según tu entorno)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tu_basededatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api.add_resource(PerfilResource, '/perfil')
api.add_resource(ServicioResource, '/servicio')
api.add_resource(PublicacionResource, '/publicacion')
api.add_resource(MensajeResource, '/mensaje')
api.add_resource(LikeResource, '/like')
api.add_resource(ConversacionResource, '/conversacion')


DBSession = sessionmaker(bind=engine)
session = DBSession()




if __name__ == '__main__':
    app.run(debug=True, port=8000)





