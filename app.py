import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
from extensions import db, migrate
import models 
# Importamos el servicio
from services.curso_service import CursoService
from forms import CursoForm

load_dotenv()

app = Flask(__name__)

# Configuración (Se mantiene igual que la Fase 2/3)
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def index():
    cursos = CursoService.obtener_todos()
    return render_template('index.html', cursos=cursos)

@app.route('/curso/nuevo', methods=['GET', 'POST'])
def agregar_curso():
    form = CursoForm()
    if form.validate_on_submit():
        CursoService.agregar_curso(
            nombre=form.nombre.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        flash("Curso agregado exitosamente", "success")
        return redirect(url_for('index'))
    return render_template('agregar_curso.html', form=form)

@app.route('/curso/editar/<int:id_curso>', methods=['GET', 'POST'])
def editar_curso(id_curso):
    # 1. Buscamos el curso o lanzamos error 404 si no existe
    curso = CursoService.obtener_por_id(id_curso)
    
    # 2. Pasamos el objeto 'obj' al formulario para que se carguen los datos actuales
    form = CursoForm(obj=curso)
    
    if form.validate_on_submit():
        # 3. Llamamos al servicio para actualizar
        CursoService.editar_curso(
            curso=curso,
            nombre=form.nombre.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        return redirect(url_for('index'))
        
    return render_template('editar_curso.html', form=form, curso=curso)

if __name__ == '__main__':
    app.run(debug=True)