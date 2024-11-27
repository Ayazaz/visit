from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class VisaForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    education = SelectField('Education', choices=[
        ('high_school', 'High School'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD')
    ], validators=[DataRequired()])
    experience = IntegerField('Years of Work Experience', validators=[DataRequired()])
    language = SelectField('Language Proficiency', choices=[
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('fluent', 'Fluent')
    ], validators=[DataRequired()])
    country = SelectField('Country', choices=[
        ('australia', 'Australia'),
        ('switzerland', 'Switzerland'),
        ('japan', 'Japan'),
        ('turkey', 'Turkey'),
        ('usa', 'USA')
    ], validators=[DataRequired()])
    submit = SubmitField('Check Eligibility')
