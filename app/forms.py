from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
 photo = FileField ('name', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
 