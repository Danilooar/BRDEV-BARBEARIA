from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class FormCriarConta(FlaskForm):
    Nome = StringField('Nome e Sobrenome', validators=[DataRequired()])
    Telefone = StringField('Telefone', validators=[DataRequired(), Length(min=7, max=9)])
    Email = StringField('E-mail', validators=[DataRequired(), Email()])
    Senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    Confirmacao = PasswordField('Confirmação da Senha', validators=[DataRequired(), Length(min=6, max=20), EqualTo('Senha')])
    botao_submit_criarConta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    Email = StringField('E-mail', validators=[DataRequired(), Email()])
    Senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    botao_submit = SubmitField('Fazer Login')

