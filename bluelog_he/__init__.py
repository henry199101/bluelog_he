









from flask import Flask








from bluelog_he.blueprints.blog import blog_bp
from bluelog_he.blueprints.auth import auth_bp


app = Flask('bluelog_he')








app.register_blueprint(blog_bp)
app.register_blueprint(auth_bp)
