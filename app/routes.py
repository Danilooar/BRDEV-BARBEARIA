from flask import Blueprint, render_template
from Forms import FormCriarConta,FormLogin



main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')



@main.route('/login', methods=['POST', 'GET'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    return render_template('login.html',
                           Form_Login=form_login,
                           Form_CriarConta=form_criar_conta)

