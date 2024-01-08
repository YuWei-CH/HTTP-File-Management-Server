from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://yuwei:StrongPassword0123!@localhost/file_server_db'
db = SQLAlchemy(app) # enable SQLAlchemy to handle SQL
migrate = Migrate(app, db)

from models import File # Import database scheme in models