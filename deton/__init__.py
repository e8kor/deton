"""
Main Application Entrypoint
"""
import os
from flask import Flask

def create_app(test_config = None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_envvar('APP_CONFIG')
    else:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from deton import cache, api
    cache.init_app(app)
    app.register_blueprint(api.bp)

    return app