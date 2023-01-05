from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'my secret key123321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@oleksandr-Swift-SF314-41:7105/itService'
db =SQLAlchemy(app)
manager = LoginManager(app)

from flask_services import routes

