from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from werkzeug.exceptions import abort  # Corrige el error tipográfico en la declaración de importación

from models.publicacion import publicacion
from models.perfil import perfil
from publicaciones_services import db

blog = Blueprint('blog', __name__)

# Obtener 1 usuario
def get_user(id):
    user = perfil.query.get_or_404(id)
    return user

@blog.route("/")
def view_post():
    posts = publicacion.query.all()
    # Elimina el commit innecesario
    return render_template('opciones.html', posts=posts, get_user=get_user)

@blog.route('/create_post', methods=('GET', 'POST'))  # Corrige la ruta de la ruta
def crear_post():
    if request.method == 'POST':
        titulo = request.form.get('Titulo')  # Corrige el error tipográfico en request.form
        texto = request.form.get('texto')
        servicio_id = request.form.get('servicio_id')

        post = publicacion(user_id=g.user.id, Titulo=titulo, texto=texto, servicio_id=servicio_id)  # Corrige los nombres de las variables

        error = None
        if not titulo:
            error = 'Se requiere título '
        elif not texto:
            error = 'Se requiere texto'
        elif not servicio_id:
            error = 'Se requiere selección de servicio'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            # Corrige la URL de renderización del template
            return redirect(url_for('blog.view_post'))

    return render_template('create_post.html')

def get_post(id):
    post= publicacion.query.get_or_404
    return post


@blog.route('/blog/delete/<int:id>')
def delete(id):
    post=get_post(id)
    db.session.delete(post)
    db.session.commit()
