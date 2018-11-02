"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
import src

if __name__ == '__main__':
    application = src.create_app()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    application.run(HOST, PORT)
