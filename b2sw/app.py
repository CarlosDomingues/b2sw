"""
Main Flask app
"""
from flask import request
from flask_api import FlaskAPI


def create_app():
    """
    App factory
    """
    app = FlaskAPI(__name__, instance_relative_config=True)
    """
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    """

    @app.route("/", methods=['GET'])
    def help():
        return 'Usage'

    @app.route("/planet/<int:key>/", methods=['GET'])
    def planet(key):
        return {'planet id': str(key)}

    return app
