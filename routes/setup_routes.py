from routes.products import products_blueprint
from flask import request

def setup_routes(app):
    app.register_blueprint(products_blueprint)