from flask import Flask, request
from flask_restful import Resource, Api
from flask import url_for, redirect, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import perfil, like, conversacion, mensaje, publicacion,servicio

import requests
import json


with open('../keys.json') as f:
  keys = json.load(f)

def main():
    app = Flask(__name__)
    api = Api(app)

# Conectar con la base de datos

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

    api.add_resource(PerfilResource, '/services/perfil')
    api.add_resource(ServicioResource, '../services/servicio')
    api.add_resource(PublicacionResource, '../services/publicacion')
    api.add_resource(MensajeResource, '../services/mensaje')
    api.add_resource(LikeResource, '../services/like')
    api.add_resource(ConversacionResource, '../services/conversacion')


    def map():
        token = request.args.get('token', default = 'noToken', type = str)
        # Specify the CLIENT_ID of the app that accesses the backend:
        response = requests.get('https://www.googleapis.com/oauth2/v2/tokeninfo?access_token=' + token)
        
        if(response.status_code == 200):
            # ID token is valid. Get the user's Google Account ID from the decoded token.
            return render_template('opciones.html', SERVIWEB_API_KEY=keys["SERVIWEB_API_KEY"], TOKEN=token)
        else: 
            # Invalid token
            return redirect('http://127.0.0.1:9090/')


    DBSession = sessionmaker(bind=engine)
    session = DBSession()




if __name__ == '__main__':
    app.run(debug=True, port=8000)





