from flask import render_template, Blueprint, flash, request, redirect, url_for, session, jsonify
from models.publicacion import Publicacion
from __init__ import db
from datetime import datetime


blog = Blueprint('blog', __name__)

@blog.route('/', methods=['GET', 'POST'])
@blog.route('/inicio', methods=['GET'])
def view_inicio():
    # Aquí deberías obtener el username y userid de alguna manera
    username = request.args.get('username')
    userid = request.args.get('userid')
    
    # Guardamos en sesión
    session['username'] = username
    session['userid'] = userid

    return render_template('inicio.html')

@blog.route('/opciones')
def view_opciones():
    username = session.get('username', None)
    userid = session.get('userid', None)

    # Almacena los valores en la sesión si se proporcionan en la URL
    if 'username' in request.args and 'userid' in request.args:
        username = request.args['username']
        userid = request.args['userid']
        session['username'] = username
        session['userid'] = userid

    return render_template('opciones.html', username=username, userid=userid)

@blog.route("/view_post", methods=['GET'])
def view_post():
    # Obtén el valor del parámetro 'filtroUsuario' de la URL
    filtro_usuario = request.args.get('filtroUsuario', None)

    if filtro_usuario:
        # Reemplaza los espacios en el usuario_id con "+"
        filtro_usuario = filtro_usuario.replace('+', ' ')
        # Filtra las publicaciones por usuario_id si el filtro está presente
        posts = Publicacion.query.filter_by(usuario_id=filtro_usuario).order_by(Publicacion.idpost.desc()).all()
    else:
        # Obtén todas las publicaciones si no hay filtro
        posts = Publicacion.query.order_by(Publicacion.idpost.desc()).all()

    print("Número de publicaciones:", len(posts))  # Agrega esta línea para depurar

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
            fechas = request.form.getlist('fechas')[0].split(', ')
            fechas_conjunto = []
            print(fechas)
            print('Antes de procesar fechas')

            # Procesar cada fecha seleccionada
            for fecha in fechas:
            
                print('Despues de procesar fechas')
                print(request.form)
                fecha = fecha.strip()  # Eliminar espacios en blanco adicionales
                id_elemento_inicio='hora_inicio_'+ fecha
                id_elemento_fin='hora_fin_'+ fecha

                #print(id_elemento)
    # Obtener las horas de inicio y fin
                hora_inicio_str = request.form.get(id_elemento_inicio)
                hora_fin_str = request.form.get(id_elemento_fin)


                if hora_inicio_str and hora_fin_str:
                    fechas_conjunto.append(f'{fecha} {hora_inicio_str} - {fecha} {hora_fin_str}')
                else:
                    print(f'Advertencia: No se seleccionaron horas para la fecha {fecha}')

                fechas_str = ', '.join(fechas_conjunto)
    # Verificar si ambas horas están presentes
            
            
            

            print('Fechas seleccionadas:', fechas)
            print('Fechas procesadas:', fechas_str)
            print('Hora de inicio:', hora_inicio_str)
            print('Hora de fin:', hora_fin_str)
            # Crear la instancia de Publicacion
            post = Publicacion(
                usuario_id=username,
                Titulo=titulo,
                texto=texto,
                servicio_id=servicio_id,
                fechas=fechas_str,
                empieza=empieza,
                marcada=False,
            )

            # Agregar y commit a la base de datos
            db.session.add(post)
            db.session.commit()

            flash('Publicación creada con éxito', 'success')

            return redirect('/view_post')

        except Exception as e:
            flash(f'Error al procesar la publicación: {str(e)}', 'error')
            print(f'Error al procesar la publicación: {str(e)}')

    return render_template('create_post.html', username=username, userid=userid)

@blog.route('/marcar_conversada/<idpost>', methods=['GET','POST'])
def marcar_conversada(idpost):
    if request.method == 'POST':
        post = Publicacion.query.get_or_404(idpost)
        post.marcada = not post.marcada  # Cambia el estado de conversación
        db.session.commit()
        # Simula enviar un correo al usuario y devuelve su ID
        return jsonify({'status': 'success', 'usuario_id': post.usuario_id})
    else:
        # Manejar otros métodos si es necesario
        return jsonify({'error': 'Método no permitido'}), 405

@blog.route('/mis_post', methods=['GET'])
def view_mis_conversaciones():
    # Obtén el usuario actual desde la sesión
    username = session.get('username', None)
    userid = session.get('userid', None)

    # Obtén las publicaciones del usuario que han sido marcadas como conversadas
    mis_conversaciones = Publicacion.query.filter_by(usuario_id=username, marcada=True).all()

    return render_template('mis_post.html', mis_conversaciones=mis_conversaciones)

