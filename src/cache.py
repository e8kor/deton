"""
Redis Cache Management
"""
import functools
import click
import os

from flask import current_app, g
from flask.cli import with_appcontext
from redis import StrictRedis

def get_cache():
    """Connect to the application's configured redis. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if 'redis' not in g:
        redis = StrictRedis(
            host = current_app.config['REDIS_HOST'], 
            port = current_app.config['REDIS_PORT'], 
            ssl = current_app.config['REDIS_SSL'],
            password = os.environ['REDIS_PASSWORD']
        )
        g.redis = redis

    return g.redis

def close_cache(e=None):
    """If this request connected to the redis, close the
    connection.
    """
    redis_pool = g.pop('redis_pool', None)

    if redis_pool is not None:
        redis_pool.disconnect()

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_cache)
    app.cli.add_command(init_cache_command)

@click.command('init-cache')
@with_appcontext
def init_cache_command():
    """Clear existing data and create new tables."""
    get_cache()
    click.echo('Initialized the database.')