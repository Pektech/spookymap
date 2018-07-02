from flask import Flask
import os




# configuration , create instances of flask extetions(slqalchemy, flask-login
# , flask-migrate)



#### Application Factory Function ####

def create_app(config=None):
    from . import routes
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config.settings')
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
        # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    #initialize extentions
    routes.init_app(app)
    #models.init_app(app)
    #main.init_app(app)
    return app