from app import db

"""
use Flask-Migrate to initial and migrate database

CREATE USER 'yuwei'@'localhost' IDENTIFIED BY 'StrongPassword0123!';
CREATE DATABASE file_server_db;
GRANT ALL PRIVILEGES ON file_server_db.* TO 'newusername'@'localhost';
FLUSH PRIVILEGES;

"""

"""
For Large file

solution 1: change max_allowed_packet
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf (in Linux)
max_allowed_packet = 64M
sudo systemctl restart mysql

solution 2: use Object-based Store, like Amazon S3 or GCS or 阿里云OSS

"""


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.BigInteger)
    upload_date = db.Column(db.DateTime)
    mime_type = db.Column(db.String(64))
    data = db.Column(db.dialects.mysql.LONGBLOB)  # support up to 4GB, but max_allowed_packet only support 64MB
    hash = db.Column(db.String(64))  # use hash to avoid duplicate files

