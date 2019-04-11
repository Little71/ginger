from app.app import Flask


def registe_blueprint(app: Flask):
    from app.api.v1 import create_blueprint
    app.register_blueprint(create_blueprint(), url_prefix='/v1')


def register_db(app: Flask):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    registe_blueprint(app)
    register_db(app)
    return app
