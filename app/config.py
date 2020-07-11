"""
    File with configuration of Flask, SQLAlchemy, e.t.c
"""
import os


class Config:
    """
        Class with default configuration
    """

    APP_NAME = "filestore"
    DEBUG = True
    SECRET_KEY = "VerySecretKey"
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/{APP_NAME}.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = f"{os.getcwd()}/store/"
    ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif", "doc"]
