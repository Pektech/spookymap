from flask import Flask
from app.instance.settings import app_config




# configuration , create instances of flask extetions(slqalchemy, flask-login
# , flask-migrate)



#### Application Factory Function ####

def create_app(config_name):
    from . import routes
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('instance/settings.py')
    #initialize extentions
    routes.init_app(app)
    #models.init_app(app)
    #main.init_app(app)
    return app