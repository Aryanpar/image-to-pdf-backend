import os
from werkzeug.utils import secure_filename
from app.config import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_file_name(filename):
    return secure_filename(filename)
