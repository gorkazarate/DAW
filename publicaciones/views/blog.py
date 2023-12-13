from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from werkzeug.exceptions import abort
from models.publicacion import Publicacion
from models.perfil import Usuario
from __init__ import db

blog = Blueprint('blog', __name__)


@blog.route('/')
@blog.route('/opciones')
def opciones():
    print("llega")
    return render_template('opciones.html')

@blog.route("/view_post")
def view_post():
    posts = Publicacion.query.all()
    return render_template('view_post.html', posts=posts)

@blog.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        print('entra')
        titulo = request.form.get('Titulo')
        texto = request.form.get('texto')
        servicio_id = request.form.get('servicio_id')
         username = current_app.extensions['oauth']['provider'].get_user()
        
        user = Usuario.query.filter_by(usuario_id=username).first()

        if not user:
            flash('No has iniciado sesión.')
            return redirect(url_for('blog.opciones'))

        post = Publicacion(user_id=user.id, Titulo=titulo, texto=texto, servicio_id=servicio_id)

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

    return render_template('create_post.html')

def delete_post(id):
    post = Publicacion.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.view_post'))