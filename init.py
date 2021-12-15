from flask import Flask, redirect, url_for, render_template, request, redirect, session
import pandas as pd
from content_based import content_based_recommend
import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


def create_app():
    app = Flask(__name__)
    app.secret_key = "Game recommendation"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app(app)

    from views import views

    app.register_blueprint(views, url_prefix='/')
    
    db.create_all(app=app)

    

    return app

    