from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3033034242'

    from .routes import main  # importa o blueprint
    app.register_blueprint(main)

    return app


