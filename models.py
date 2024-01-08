from app import db

"""
use Flask-Migrate to initial and migrate database

CREATE USER 'yuwei'@'localhost' IDENTIFIED BY 'StrongPassword0123!';
CREATE DATABASE file_server_db;
GRANT ALL PRIVILEGES ON file_server_db.* TO 'newusername'@'localhost';
FLUSH PRIVILEGES;

"""


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.BigInteger)
    upload_date = db.Column(db.DateTime)
    mime_type = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
