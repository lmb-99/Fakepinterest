from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fakepinterest.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Password Confirmation', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Create Account')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('This email is already being used, please register a different email or log in.')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Log In')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('This email does not exist, please create a new account.')

class FormFoto(FlaskForm):
    foto = FileField('Picture', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Send')