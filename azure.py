"""
This script runs the Deton application using a development server.
"""
import src
import os 

os.environ["APP_CONFIG"] = "./config/app.cfg"

app = src.create_app()
