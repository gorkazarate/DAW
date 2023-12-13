from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['STATIC_FOLDER'] = 'static'


db = SQLAlchemy(app)  # Crear la instancia de SQLAlchemy asociada a tu aplicación

# Aquí puedes realizar otras configuraciones si es necesario

from views.blog import blog

app.register_blueprint(blog)

# No ejecutes db.create_all() aquí

# En algún otro archivo o script (por ejemplo, manage.py)


# Asegúrate de ejecutar esto dentro del contexto de la aplicación Flask
with app.app_context():
    db.create_all()