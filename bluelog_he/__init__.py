









from flask import Flask








from bluelog_he.blueprints.blog import blog_bp


app = Flask('bluelog_he')








app.register_blueprint(blog_bp)
