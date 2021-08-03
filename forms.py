from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class Formulario(FlaskForm):
    id = IntegerField('id')
    name = StringField('name')
    class_ = StringField('class')
