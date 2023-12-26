from flask import render_template, Blueprint, redirect, request, url_for, session,jsonify
from models.perfil import Perfil
from __init__ import db

perfil = Blueprint('perfil', __name__)

@perfil.route('/perfil/<string:username>/<int:userid>', methods=['GET', 'POST'])
def crear_perfil(username, userid):
    # Obtenemos el nombre de usuario y el ID de usuario de la sesión
    username_session = session.get('username', None)
    userid_session = session.get('userid', None)

    if request.method == 'POST':
        # Verifica si el perfil ya existe para este usuario
        nombre_completo = request.form.get('nombre_completo')
        cumpleaños = request.form.get('cumpleaños')
        numerotlf = request.form.get('numerotlf')
        direccion = request.form.get('direccion')

        nuevo_usuario = Perfil(
            usuario_id=username_session,
            id_usuario=userid_session,
            nombre_completo=nombre_completo,
            cumpleaños=cumpleaños,
            numerotlf=numerotlf,
            direccion=direccion,
            numlikes=0
        )

        # Aquí puedes realizar cualquier validación adicional
        # Antes de agregar el nuevo perfil

        db.session.add(nuevo_usuario)
        db.session.commit()
        return render_template('opciones.html', username=username_session, userid=userid_session)

    return render_template('perfil.html', username=username_session, userid=userid_session)

@perfil.route('/ver_perfil/<username>', methods=['GET'])
def ver_perfil(username):
    usuario = Perfil.query.filter_by(usuario_id=username).first()
    return render_template('ver_perfil.html', perfil=usuario)

@perfil.route('/dar_like/<string:id_usuario>', methods=['POST'])
def dar_like(id_usuario):
    # Verificar si el usuario está autenticado
    print('id usuario' + id_usuario)
    usuario = Perfil.query.get(id_usuario)
    # Incrementar el número de likes del usuario
    usuario.numlikes += 1
    db.session.commit()

    # Agregar el perfil a la lista de perfiles que el usuario le dio like

    # Devolver el nuevo número de likes como respuesta
    return jsonify({usuario.numlikes})