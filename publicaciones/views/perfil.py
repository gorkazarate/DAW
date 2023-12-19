from flask import render_template, Blueprint, redirect, request, url_for, session
from models.perfil import Usuario
from __init__ import db

perfil = Blueprint('perfil', __name__)

@perfil.route('/', methods=['GET', 'POST'])
def crear_perfil():
    print("llega")

    # Intenta obtener el nombre de usuario y el ID de usuario de la sesión
    username = session.get('username', None)
    userid = session.get('userid', None)

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

            if not usuario:
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

            # Almacena la información del usuario en la sesión
            session['username'] = username
            session['userid'] = userid
            print("Username in session:", session['username'])

            # Redirige a la página 'opciones' del Blueprint 'blog'
            return redirect(url_for('blog.opciones', username=username))

    session['username'] = username
    session['userid'] = userid
    return render_template('perfil.html', username=username, userid=userid)

@perfil.route('/ver_perfil/<int:Id_usuario>', methods=['GET'])
def ver_perfil(Id_usuario):
    usuario = Usuario.query.filter_by(Id_usuario=Id_usuario).first()
    return render_template('ver_perfil.html', usuario=usuario)


@perfil.route('/dar_like/<int:Id_usuario>', methods=['POST'])
def dar_like(Id_usuario):
    usuario = Usuario.query.get(Id_usuario)

    if usuario:
        # Incrementar el número de likes del usuario
        usuario.numLikes += 1
        db.session.commit()

        # Devolver el nuevo número de likes como respuesta
        return redirect(url_for('perfil.ver_perfil', Id_usuario=usuario.Id_usuario))
    else:
        # Manejar el caso en que el usuario no existe
        return jsonify({'error': 'Usuario no encontrado'}), 404