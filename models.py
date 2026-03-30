from extensions import db

class Curso(db.Model):
    __tablename__ = 'cursos' # Nombre de la tabla en MySQL

    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Numeric(10, 2), nullable=False) # Decimal para horas (ej. 10.5)

    def __repr__(self):
        return f'<Curso {self.nombre}>'