






import os


from flask import Flask

from bluelog_he.blueprints.admin import admin_bp
from bluelog_he.blueprints.auth import auth_bp
from bluelog_he.blueprints.blog import blog_bp

from bluelog_he.settings import config




def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('bluelog_he')
    app.config.from_object(config[config_name])























def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
