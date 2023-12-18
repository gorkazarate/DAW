from flask import render_template, Blueprint, flash, redirect, request, url_for, session
from models.perfil import Usuario
from __init__ import db

perfil = Blueprint('perfil', __name__)

@perfil.route('/', methods=['GET', 'POST'])
@perfil.route('/perfil', methods=['GET', 'POST'])
def crear_perfil():
    print("llega")

    # Intenta obtener el nombre de usuario y el ID de usuario de la sesión
    username = session.get('username', None)
    userid = session.get('userid', None)

    # Si no se encuentran en la sesión, intenta obtenerlos de la solicitud
    if username is None or userid is None:
        username = request.args.get('username', default=None)
        userid = request.args.get('userid', default=None)

    if request.method == 'POST':
        print('entra')
        nombre_completo = request.form.get('nombre_completo')
        cumpleaños = request.form.get('cumpleaños')
        numerotlf = request.form.get('numerotlf')
        direccion = request.form.get('direccion')
        numlikes = request.form.get('numlikes')

        if username is not None and userid is not None:
            # Verifica si el usuario ya existe en la base de datos
            usuario = Usuario.query.filter_by(usuario_id=username).first()

            if usuario:
                # El usuario existe, almacena el username en la sesión
                session['username'] = username
                session['userid'] = userid
                print("Username in session (exists):", session['username'])
            else:
                # El usuario no existe, agrégalo a la tabla perfil
                nuevo_usuario = Usuario(
                    usuario_id=username,
                    Id_usuario=userid,
                    nombre_completo=nombre_completo,
                    cumpleaños=cumpleaños,
                    numerotlf=numerotlf,
                    direccion=direccion,
                    numlikes=numlikes
                ) 
                db.session.add(nuevo_usuario)
                db.session.commit()
                session['username'] = username
                session['userid'] = userid
                print("Username in session (added):", session['username'])

            # Redirige a la página 'opciones' del Blueprint 'blog'
            return redirect(url_for('blog.opciones'))

    return render_template('perfil.html', username=username)