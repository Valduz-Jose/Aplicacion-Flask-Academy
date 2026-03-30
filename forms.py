from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CursoForm(FlaskForm):
    nombre = StringField('Nombre del Curso', validators=[DataRequired(message="El nombre es obligatorio")])
    instructor = StringField('Instructor', validators=[DataRequired(message="El instructor es obligatorio")])
    duracion = DecimalField('Duración (horas)', validators=[
        DataRequired(message="Ingresa un número válido"),
        NumberRange(min=0.1, message="La duración debe ser mayor a 0")
    ])
    submit = SubmitField('Guardar Curso')