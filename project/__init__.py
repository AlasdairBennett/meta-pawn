import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template
from flask.logging import default_handler


def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Configure the Flask app
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    register_blueprints(app)
    configure_logging(app)
    register_app_callbacks(app)
    register_error_pages(app)
    return app


def register_blueprints(app):
    # Import the blueprints
    from project.stats import stats_blueprint

    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    app.register_blueprint(stats_blueprint)


def configure_logging(app):
    # Logging Configuration
    file_handler = RotatingFileHandler('instance/meta-pawn.log',
                                       maxBytes=16384,
                                       backupCount=20)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting Meta-Pawn...')


def register_app_callbacks(app):
    @app.before_request
    def app_before_request():
        app.logger.info('Calling before_request() for the Flask application...')

    @app.after_request
    def app_after_request(response):
        app.logger.info('Calling after_request() for the Flask application...')
        return response

    @app.teardown_request
    def app_teardown_request(error=None):
        app.logger.info('Calling teardown_request() for the Flask application...')

    @app.teardown_appcontext
    def app_teardown_appcontext(error=None):
        app.logger.info('Calling teardown_appcontext() for the Flask application...')


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405
