from flask import render_template, Blueprint, flash, request, redirect, url_for, session
from models.publicacion import Publicacion
from __init__ import db
from datetime import datetime, timedelta

blog = Blueprint('blog', __name__)

@blog.route('/opciones')
def opciones():
    return render_template('opciones.html')

@blog.route('/opciones/<string:username>/<int:userid>')
def view_opciones(username, userid):
    username = session.get('username', None)
    userid = session.get('userid', None)
    print("Username in opciones:", username)

    return render_template('opciones.html', username=username, userid=userid)

@blog.route("/view_post",methods=['GET','POST'])
def view_post():
    posts = Publicacion.query.order_by(Publicacion.empieza.desc()).all()
    return render_template('view_post.html', posts=posts)

@blog.route('/create_post', methods=['GET', 'POST'])
def create_post():
    username = session.get('username', None)
    userid = session.get('userid', None)

    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            titulo = request.form.get('Titulo')
            texto = request.form.get('texto')
            servicio_id = request.form.get('servicio_id')
            empieza = datetime.utcnow()
            # Obtener las fechas seleccionadas
            fechas = request.form.getlist('fechas[]')

            print('antes de procesar fechas')
            # Procesar cada fecha seleccionada
            for fecha in fechas:
                print('después de procesar fechas')
                hora_inicio_str = request.form.get(f'hora_inicio_{fecha}')
                hora_fin_str = request.form.get(f'hora_fin_{fecha}')

                # Ajustar el formato al nuevo formato que incluye horas y minutos
                fecha_hora_inicio = datetime.strptime(f'{fecha} {hora_inicio_str}', '%Y-%m-%d %H:%M')
                fecha_hora_fin = datetime.strptime(f'{fecha} {hora_fin_str}', '%Y-%m-%d %H:%M')

                print(f'Fecha: {fecha}, Hora de inicio: {fecha_hora_inicio}, Hora de fin: {fecha_hora_fin}')

                # Crear la instancia de Publicacion
                post = Publicacion(
                    usuario_id=username,
                    Titulo=titulo,
                    texto=texto,
                    servicio_id=servicio_id,
                    fechas=f'{fecha_hora_inicio} - {fecha_hora_fin}',
                    empieza=empieza,
                )

                # Agregar y commit a la base de datos
                db.session.add(post)
                db.session.commit()

            flash('Publicación creada con éxito', 'success')
            return redirect(url_for('blog.view_post'))

        except Exception as e:
            flash(f'Error al procesar la publicación: {str(e)}', 'error')
            print(f'Error al procesar la publicación: {str(e)}')

    return render_template('create_post.html', username=username, userid=userid)

def delete_post(id):
    post = Publicacion.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.view_post'))