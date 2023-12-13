from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from werkzeug.exceptions import abort
from models.publicacion import Publicacion
from models.perfil import Usuario
from __init__ import db
from flask import current_app, session
from datetime import datetime


blog = Blueprint('blog', __name__)


@blog.route('/')
@blog.route('/opciones')
def opciones():
    print("llega")
    return render_template('opciones.html')

#@blog.route('/api/receive-user-info', methods=['POST'])
#def receive_user_info():
    # Verify the authenticity of the incoming request
#    if is_request_valid(request):
#        user_info = request.json
#        # Process user information as needed
#        print(user_info)
#        return 'User information received successfully', 200
    

@blog.route("/view_post")
def view_post():
    posts = Publicacion.query.order_by(Publicacion.empieza.desc()).all()
    return render_template('view_post.html', posts=posts)

@blog.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        print('entra')
        titulo = request.form.get('Titulo')
        texto = request.form.get('texto')
        servicio_id = request.form.get('servicio_id')
        username = request.args.get('username')        
        empieza= datetime.utcnow()
        termina= request.form.get('termina')
        


        post = Publicacion(usuario_id=username, Titulo=titulo, texto=texto, servicio_id=servicio_id,empieza=empieza,termina=termina )

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