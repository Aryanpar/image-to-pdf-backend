import os
import shutil
import time
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from app.config import *
from app.utils.security import allowed_file
from app.utils.pdf_builder import build_pdf, apply_password

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/convert", methods=["POST"])
def convert_pdf():
    files = request.files.getlist("files")
    password = request.form.get("password")
    watermark = request.form.get("watermark")
    quality = int(request.form.get("quality", 85))

    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    if len(files) > MAX_FILES:
        return jsonify({"error": "Too many files"}), 400

    upload_paths = []
    total_size = 0

    for f in files:
        if not allowed_file(f.filename):
            return jsonify({"error": "Invalid file type"}), 400

        filename = secure_filename(f.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)

        f.save(path)
        upload_paths.append(path)

        total_size += os.path.getsize(path)

    if total_size > MAX_TOTAL_SIZE_MB * 1024 * 1024:
        cleanup(upload_paths)
        return jsonify({"error": "Files too large"}), 400

    pdf_bytes = build_pdf(upload_paths, watermark_text=watermark, quality=quality)

    if password:
        pdf_bytes = apply_password(pdf_bytes, password)

    output_path = os.path.join(OUTPUT_FOLDER, f"output_{int(time.time())}.pdf")

    with open(output_path, "wb") as f:
        f.write(pdf_bytes.read())

    cleanup(upload_paths)

    return send_file(output_path, as_attachment=True)


def cleanup(paths):
    for p in paths:
        if os.path.exists(p):
            os.remove(p)


if __name__ == "__main__":
    app.run(debug=True)
