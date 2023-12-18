from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from werkzeug.exceptions import abort
from models.publicacion import Publicacion
from models.perfil import Usuario
from __init__ import db
from flask import current_app, session
from datetime import datetime
from flask_cors import CORS



blog = Blueprint('blog', __name__)


@blog.route('/', methods=['GET','POST'])
@blog.route('/opciones', methods=['GET', 'POST'])
def opciones():
    print("llega")
 
    username = request.args.get('username', default=None)
    userid = request.args.get('userid', default=None)
    if username is not None and userid is not None:
        # Almacena el username en la sesión
        session['username'] = username
        # Redirige a create_post incluyendo el username en la URL
        return redirect(url_for('blog.create_post'))
    else:
        return 'Param not provided'

    return render_template('opciones.html',username=username)



@blog.route("/view_post")
def view_post():
    posts = Publicacion.query.order_by(Publicacion.empieza.desc()).all()
    return render_template('view_post.html', posts=posts)

@blog.route('/create_post', methods=['GET', 'POST'])
def create_post():
    
    username = session.get('username', None)

    if request.method == 'POST':
        print('entra')
        titulo = request.form.get('Titulo')
        texto = request.form.get('texto')
        servicio_id = request.form.get('servicio_id')
        empieza= datetime.utcnow()
        termina= request.form.get('termina')
        


        post = Publicacion(usuario_id=username, Titulo=titulo, texto=texto, servicio_id=servicio_id,empieza=empieza,termina=termina, )

        error = None
        if not titulo or not texto or not servicio_id:
            error = 'Todos los campos son obligatorios'

        if error:
            flash(error)
        else:
            db.session.add(post)
            print('inserta')
            db.session.commit()
            return redirect(url_for('blog.view_post'))

    return render_template('create_post.html', username=username)

def delete_post(id):
    post = Publicacion.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.view_post'))