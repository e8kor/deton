"""
This script runs the deton application using a development server.
"""

from os import environ
import src

app = src.create_app().run