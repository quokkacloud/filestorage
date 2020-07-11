"""
    This module contain helpful functions
"""

import hashlib
import os
from app.config import Config


def allowed_file(filename):
    """
        Check extension of the file

        :param filename: name of the file

        :return
            True or False
    """
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.lower() in Config.ALLOWED_EXTENSIONS:
        return True
    return False


def save_file_to_storage(file):
    """
        Get hash of the file and save it in storage

        :param file: file object

        :return
            Tuple
    """
    md5 = hashlib.md5()
    data = file.read()
    md5.update(data)
    hash_string = str(md5.hexdigest())
    files_path = f"{Config.UPLOAD_FOLDER}{hash_string[:2]}/"
    if not os.path.exists(files_path):
        os.makedirs(files_path)
    full_path = files_path + hash_string
    if not os.path.exists(full_path):
        with open(full_path, "wb") as file_desc:
            file_desc.write(data)
    return hash_string, files_path
