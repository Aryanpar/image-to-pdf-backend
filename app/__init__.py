from flask import Flask
from .config import UPLOAD_FOLDER, OUTPUT_FOLDER

def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER
    return app
