






import os


from flask import Flask

from bluelog_he.blueprints.admin import admin_bp
from bluelog_he.blueprints.auth import auth_bp
from bluelog_he.blueprints.blog import blog_bp
from bluelog_he.extensions import bootstrap, db, ckeditor, mail, moment
from bluelog_he.settings import config




def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('bluelog_he')
    app.config.from_object(config[config_name])











def register_logging(app):
    pass


def init_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)
