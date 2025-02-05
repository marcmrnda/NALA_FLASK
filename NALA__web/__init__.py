from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

db = SQLAlchemy()

def create_database(app):
    if not path.exists(f"./{os.getenv('DATABASE_NAME')}"):
        with app.app_context():
            db.create_all()  # Pass the app directly
            print("Database has been created")
    else:
        print(f"Database '{os.getenv('DATABASE_NAME')}' already exists.")

def main():
    from .view import view
    from .auth import auth
    

    app = Flask(__name__)
    
    load_dotenv()  
    mySecretKey = os.getenv('SECRET_KEY')
    database_URL = os.getenv('DATABASE_URL')
    debug = os.getenv('DEBUG')
    
   
    app.config['SQLALCHEMY_DATABASE_URI'] = database_URL
    app.config['SECRET_KEY'] = mySecretKey
    app.config["DEBUG"] = debug
    
    
   
    db.init_app(app)
  
    app.register_blueprint(view, url_prefix='/')  
    app.register_blueprint(auth, url_prefix='/')  
    

    from .model import User
    

    create_database(app)
    return app
