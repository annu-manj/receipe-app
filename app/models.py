from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/recipe_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mydb=SQLAlchemy(app)

if __name__ == "__main__":
    with app.app_context():
        mydb.init_app(app)
        mydb.create_all()
    app.run(debug=True)