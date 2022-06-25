from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('Config.Config')

    db.init_app(app)

    with app.app_context():

        from app import routes

        db.create_all()

        from app import migrate

        migrate.migrate_user_roles(app.config['USER_ROLES_FIXTURE_PATH'])
        migrate.users(app.config['USERS_FIXTURE_PATH'])

        return app



