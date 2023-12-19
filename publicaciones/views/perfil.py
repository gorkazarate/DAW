from flask import render_template, Blueprint, redirect, request, url_for, session,jsonify
from models.perfil import Perfil
from __init__ import db

perfil = Blueprint('perfil', __name__)

@perfil.route('/', methods=['GET', 'POST'])
def crear_perfil():
    print("llega")

    # Intenta obtener el nombre de usuario y el ID de usuario de la sesión
    username = session.get('username', None)
    userid = session.get('userid', None)

    # Almacena los valores en la sesión si se proporcionan en la URL
    if 'username' in request.args and 'userid' in request.args:
        username = request.args['username']
        userid = request.args['userid']
        session['username'] = username
        session['userid'] = userid


    # Comprueba si el usuario ya existe en la base de datos
    usuario_existente = Perfil.query.filter_by(usuario_id=username).first()

    if usuario_existente:
        # El usuario ya existe, redirige a la página 'opciones' del Blueprint 'blog'
        return render_template('opciones.html', username=session['username'],userid=session['userid'])
    print('********1')


    if request.method == 'POST':
        print('entra')
        nombre_completo = request.form.get('nombre_completo')
        cumpleaños = request.form.get('cumpleaños')
        numerotlf = request.form.get('numerotlf')
        direccion = request.form.get('direccion')
        numlikes = request.form.get('numlikes')

        
        

        print("User ID:", userid)
        print("User name2:", username)
        # El usuario no existe, agrégalo a la tabla perfil
        nuevo_usuario = Perfil(
            usuario_id=username,
            id_usuario=userid,  
            nombre_completo=nombre_completo,
            cumpleaños=cumpleaños,
            numerotlf=numerotlf,
            direccion=direccion,
            numlikes=0 
)
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Almacena la información del usuario en la sesión después de procesar el formulario
        session['username'] = username
        session['userid'] = userid
        print("Username in session:", session['username'])

        # Redirige a la página 'opciones' del Blueprint 'blog'
        return render_template('opciones.html', username=session['username'],userid=session['userid'])
    # El usuario no existe y no se ha enviado el formulario, muestra la página de perfil
    return render_template('perfil.html', username=session['username'],userid=session['userid'])
    
@perfil.route('/ver_perfil/<username>', methods=['GET'])
def ver_perfil(username):
    usuario = Perfil.query.filter_by(usuario_id=username).first()
    return render_template('ver_perfil.html', perfil=usuario)


@perfil.route('/dar_like/<string:id_usuario>', methods=['POST'])
def dar_like(id_usuario):
    # Verificar si el usuario está autenticado
    print('id usuario'+id_usuario)
    usuario = Perfil.query.get(id_usuario)
    # Incrementar el número de likes del usuario
    usuario.numlikes += 1
    db.session.commit()

    # Agregar el perfil a la lista de perfiles que el usuario le dio like
    

    # Devolver el nuevo número de likes como respuesta
    return jsonify({' ':usuario.numlikes})