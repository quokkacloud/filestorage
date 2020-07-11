"""
    Module with endpoints for /files
"""

import os
from flask import (
    Blueprint,
    jsonify,
    request,
    make_response,
    send_from_directory,
)
from app import db
from app.models.store import Files
from app.utils import allowed_file, save_file_to_storage

files_blueprint = Blueprint("files", __name__)


@files_blueprint.route("/files", methods=["GET"])
def get_all_authors():
    """
        Get all files from storage

        :return:
            Response in Json format
    """
    return make_response(
        jsonify([elem.serialized for elem in Files.query.all()]), 200
    )


@files_blueprint.route("/files", methods=["POST"])
def upload_file():
    """
        Upload file on server

        :return:
            Response in Json format
    """
    if "file" not in request.files:
        return make_response(
            jsonify({"error": "No file part in request"}), 400
        )
    file = request.files["file"]
    file_name = file.filename
    if not file_name:
        return make_response(
            jsonify({"error": "No name of the file to upload"}), 400
        )
    if not allowed_file(file_name):
        return make_response(jsonify({"error": "Bad file extension"}), 400)
    file_hash, file_path = save_file_to_storage(file)
    if Files.query.filter_by(hash_str=file_hash).first():
        return make_response(
            jsonify({"error": "File is already in storage"}), 400
        )
    element = Files(name=file_name, hash_str=file_hash, directory=file_path)
    db.session.add(element)
    db.session.commit()
    return make_response(jsonify({"result": file_hash}), 201)


@files_blueprint.route("/files/<string:file_hash>", methods=["DELETE"])
def delete_file(file_hash):
    """
        Delete file from storage

        :return:
            Response in Json format
    """
    element = Files.query.filter_by(hash_str=file_hash).first()
    if not element:
        return make_response(
            jsonify({"error": "No file with such hash in storage"}), 404
        )
    file_path = f"{element.directory}{element.hash_str}"
    if os.path.exists(file_path):
        os.remove(file_path)
    db.session.delete(element)
    db.session.commit()
    return make_response(jsonify({"result": "File deleted"}), 200)


@files_blueprint.route("/files/<string:file_hash>", methods=["GET"])
def download_file(file_hash):
    """
        Download file from server

        :return:
            Response in Json format
    """
    element = Files.query.filter_by(hash_str=file_hash).first()
    if not element:
        return make_response(
            jsonify({"error": "No file with such hash in storage"}), 404
        )
    return send_from_directory(element.directory, element.hash_str)
