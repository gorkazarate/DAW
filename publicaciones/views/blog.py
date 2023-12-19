from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from werkzeug.exceptions import abort
from models.publicacion import Publicacion
from models.perfil import Perfil
from __init__ import db
from flask import current_app, session
from datetime import datetime
from flask_cors import CORS



blog = Blueprint('blog', __name__)

@blog.route('/opciones/<string:username>/<int:userid>')
def view_opciones(username,userid):
    username = session.get('username', None)
    userid= session.get('userid',None)
    print("Username in opciones:", username)

    return render_template('opciones.html', username=username,userid=userid)

@blog.route("/view_post")
def view_post():
    posts = Publicacion.query.order_by(Publicacion.empieza.desc()).all()
    return render_template('view_post.html', posts=posts)

@blog.route('/create_post', methods=['GET', 'POST'])
def create_post():
    
    username = session.get('username', None)
    userid= session.get('userid',None)

    print("Username in create_post:", username)

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

    return render_template('create_post.html', username=username, userid=userid)

def delete_post(id):
    post = Publicacion.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.view_post'))