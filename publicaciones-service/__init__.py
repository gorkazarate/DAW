from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)  # Crear la instancia de SQLAlchemy asociada a tu aplicación


from publicaciones_services.views.blog import blog

app.register_blueprint(blog)
