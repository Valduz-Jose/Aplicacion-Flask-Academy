from extensions import db
from models import Curso

class CursoService:
    @staticmethod
    def obtener_todos():
        return Curso.query.all()

    @staticmethod
    def obtener_por_id(id_curso):
        return Curso.query.get_or_404(id_curso)

    @staticmethod
    def agregar_curso(nombre, instructor, duracion):
        nuevo_curso = Curso(nombre=nombre, instructor=instructor, duracion=duracion)
        db.session.add(nuevo_curso)
        db.session.commit()
        return nuevo_curso

    @staticmethod
    def editar_curso(curso, nombre, instructor, duracion):
        curso.nombre = nombre
        curso.instructor = instructor
        curso.duracion = duracion
        db.session.commit()
        return curso

    @staticmethod
    def eliminar_curso(id_curso):
        curso = Curso.query.get_or_404(id_curso)
        db.session.delete(curso)
        db.session.commit()
        return True