from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import mydb
from datetime import datetime
from flask import render_template,request,url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/recipe_app_db'  # access to the SQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




class userdata(mydb.Model):
    userid = mydb.Column(mydb.Integer, primary_key=True)
    email = mydb.Column(mydb.String(20),unique=True)
    fullname = mydb.Column(mydb.String(20))
    password = mydb.Column(mydb.String(20))
    confirm_password = mydb.Column(mydb.String(20))
    createddate = mydb.Column(mydb.DateTime, default=datetime.utcnow)
    status = mydb.Column(mydb.String(10), default='active')

    def __init__(self, fullname, email, password):
        self.name = fullname
        self.email = email
        self.password = password
        


class review(mydb.Model):
    ratingid = mydb.Column(mydb.Integer, primary_key=True)
    userid = mydb.Column(mydb.Integer)
    recipeid = mydb.Column(mydb.Integer)
    rating = mydb.Column(mydb.Integer)
    
    def __init__(self, userid, recipeid, rating):
        self.userid = userid
        self.recipeid = recipeid
        self.rating = rating

if __name__ == "__main__":
    with app.app_context():
        mydb.init_app(app)
        mydb.create_all()
    app.run(debug=True)  
