from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
# from app import app
# Forms
class SearchForm(FlaskForm):
  name = StringField('Pokemon Name', validators=[DataRequired()])
  submit = SubmitField('Seach!')