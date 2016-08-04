from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://localhost/dvdrental'
db = SQLAlchemy(app)

meta = db.metadata
engine = db.engine

import dbapp.models
import dbapp.views
import dbapp.utils
