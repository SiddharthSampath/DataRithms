from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, DateTimeField, BooleanField, ValidationError, FileField
from wtforms.validators import DataRequired, AnyOf, URL
from models import Category


class QuestionForm(Form):
    question_title = StringField(
        'question_title',
        validators=[DataRequired()]
    )
    question = TextAreaField(
        'question',
        validators=[DataRequired()]
    )
    answer = TextAreaField(
        'answer',
        validators=[DataRequired()]
    )
    