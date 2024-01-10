from flask import Flask, request, jsonify, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime
import io
import hashlib

# connect database
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://yuwei:StrongPassword0123!@localhost/file_server_db"

db = SQLAlchemy(app)  # enable SQLAlchemy to handle SQL
migrate = Migrate(app, db)

from app.models import File  # Import database scheme in models


# hash helper
def calculate_file_hash(file_stream, block_size=65536):  # 65536 = 64KB
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: file_stream.read(block_size), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


# file size convector
def convert_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} Bytes"
    elif size_bytes < 1024**2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes / (1024**2):.2f} MB"
    else:
        return f"{size_bytes / (1024**3):.2f} GB"


# index
@app.route("/")
def index():
    return render_template("index.html")


# APIs
# upload file
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify(message="No file part"), 400

    file = request.files["file"]

    # check empty file
    if file.filename == "":
        return jsonify(message="No selected file"), 400

    if file:
        # check file size (<= 4GB)
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        if file_size > 4 * 1024 * 1024 * 1024:  # 4GB
            return jsonify(message="File is too large"), 400
        file.seek(0)  # reset file pointer

        # save file into db
        file_hash = calculate_file_hash(file)

        # duplicate file check
        existing_file = File.query.filter_by(hash=file_hash).first()
        if existing_file:
            return jsonify(message="File already exists"), 409
        else:
            file.seek(0)  # reset file pointer
            file_data = file.read()
            new_file = File(
                name=file.filename,
                size=file_size,
                upload_date=datetime.utcnow(),
                mime_type=file.content_type,
                data=file_data,
                hash=file_hash,
            )
            db.session.add(new_file)
            db.session.commit()
            # return
            return (
                jsonify(
                    message="File uploaded successfully",
                    file_name=file.filename,
                    file_type=file.content_type,
                    file_size=file_size,
                ),
                200,
            )

    return jsonify(message="File upload failed"), 500


# get all file types
@app.route("/get-file-types", methods=["GET"])
def get_file_types():
    file_types = File.query.with_entities(File.mime_type).distinct().all()
    return jsonify([file_type.mime_type for file_type in file_types])


# list file by query
@app.route("/files", methods=["GET"])
def list_files():
    query_name = request.args.get("name")
    query_date = request.args.get("date")
    query_type = request.args.get("type")

    query = File.query

    # query by name
    if query_name:
        query = query.filter(File.name.contains(query_name))

    # query bt date and time
    if query_date:
        date = datetime.strptime(query_date, "%Y-%m-%d").date()
        query = query.filter(db.func.date(File.upload_date) == date)

    # query by file type
    if query_type:
        query = query.filter(File.mime_type.contains(query_type))

    files = query.all()
    files_data = [
        {
            "id": file.id,
            "name": file.name,
            "size": convert_size(file.size),
            "upload_date": file.upload_date.strftime("%Y-%m-%d %H:%M:%S")
            if file.upload_date
            else "Unknown",
            "type": file.mime_type,
        }
        for file in files
    ]
    if request.headers.get("Accept") == "application/json":
        return jsonify(files_data)  # return JSON for AJAX
    else:
        return render_template("index.html", files=files_data)


# download file
@app.route("/download/<int:file_id>", methods=["GET"])
def download_file(file_id):
    file = File.query.get(file_id)
    if file:
        file_data = io.BytesIO(file.data)

        return send_file(
            file_data,
            as_attachment=True,
            download_name=file.name,
            mimetype=file.mime_type,
        )
    else:
        return "Unknow Error", 404
