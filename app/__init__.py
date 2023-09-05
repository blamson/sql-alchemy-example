# 3rd party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
db.init_app(app)

from app import models
with app.app_context():
    db.create_all()

from app import routes