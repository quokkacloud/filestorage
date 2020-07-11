"""
    Models of database
"""
from app import db


class Files(db.Model):
    """
        Files model
    """

    __tablename__ = "files"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    hash_str = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    directory = db.Column(db.String, nullable=False)

    @property
    def serialized(self):
        """
            Serialize data from Files

            :return:
                Dict
        """
        return {"name": self.name, "hash": self.hash_str}
