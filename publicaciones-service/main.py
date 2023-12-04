from flask import Flask, render_template, redirect, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
from models import perfil, likes, conversacion, mensaje, publicacion, servicio  # Ajusta esta importación según tu estructura de archivos

app = Flask(__name__)
api = Api(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/serviweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Ajusta las importaciones según la estructura de archivos
from services.perfil import PerfilResource
from services.likes import LikesResource
from services.conversacion import ConversacionResource
from services.mensaje import MensajeResource
from services.publicacion import PublicacionResource
from services.servicio import ServicioResource

# Añade los recursos a la API
api.add_resource(PerfilResource, '/services/perfil', endpoint='perfil')
api.add_resource(LikesResource, '/services/likes')
api.add_resource(ConversacionResource, '/services/conversacion')
api.add_resource(MensajeResource, '/services/mensaje')
api.add_resource(PublicacionResource, '/services/publicacion')
api.add_resource(ServicioResource, '/services/servicio')



def opciones():
    token = request.args.get('token', default='noToken', type=str)
    # Especifica el CLIENT_ID de la aplicación que accede al backend:
    response = requests.get('https://www.googleapis.com/oauth2/v2/tokeninfo?access_token=' + token)

    if response.status_code == 200:
        # El token de ID es válido. Obtén el ID de la cuenta de Google del token decodificado.
        return render_template('templates/opciones.html', SERVIWEB_API_KEY=keys["SERVIWEB_API_KEY"], TOKEN=token)
    else:
        # Token no válido
        return redirect('http://127.0.0.1:9090/')


with app.app_context():
    DBSession = sessionmaker(bind=db.engine)
    session = DBSession()
if __name__ == '__main__':
    app.run(debug=True, port=8000)