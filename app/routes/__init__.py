"""Blueprint is a bit overkill for this simple app but wnated to learn them"""
from flask import Blueprint
sp = Blueprint('sp', __name__)
def init_app(app):
    app.register_blueprint(sp)
from .import routes