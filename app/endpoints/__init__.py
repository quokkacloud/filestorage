"""
    Registration of existing blueprints
"""
from app.endpoints.files import files_blueprint


def register_blueprints(app):
    """
        Register all blueprints
    """
    app.register_blueprint(files_blueprint)
