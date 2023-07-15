from flask import Flask, render_template, request,jsonify,session
import mysql.connector
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin
import json
import csv
import MySQLdb
from datetime import datetime
#from werkzeug.security import generate_password_hash,check_password_hash
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)
app.secret_key="ScpJIgjWVK_Xv-jD"
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app,supports_credentials=True)


#ma=Marshmallow(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/recipe_app_db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db=SQLAlchemy(app)


db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
)
CORS(app,supports_credentials=True)

@app.route("/",methods=['GET']) 
def index():
    return jsonify({"message":"working"})


#signup api
@app.route("/signup", methods=[ 'POST'])
def signup():
    #db_password=os.environ.get('DB_PASSWORD')
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    #password=db_password,
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    
    '''fullname = request.json.get('fullname')
    email = request.json.get('email')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')'''
    
    fullname = request.json['fullname']
    email = request.json['email']
    password = request.json['password']
    confirm_password = request.json['confirm_password']
    
    hashed_password = bcrypt.generate_password_hash(password)
    #bcrypt.check_password_hash(pw_hash, 'password')
    
    
    check_query = "SELECT * FROM userdata WHERE email = %s"
    check_values = (email,)
    mycursor.execute(check_query, check_values)
    existing_user = mycursor.fetchone()

    if existing_user:
        return jsonify({"message": "User already exists"})
    elif (password == confirm_password):
        #sql="insert into userdata(fullname,email,password,confirm_password,createddate,status)values(%s,%s,%s,%s,%s,%s)"
        sql="insert into userdata(fullname,email,password,createddate,status)values(%s,%s,%s,%s,%s)"
        values=(fullname,email,hashed_password,datetime.now(),"active")
        mycursor.execute(sql,values)
        db.commit()
        return jsonify({"status":"signed up"})
    else:
        return jsonify({"message":"password doesn't match"})
        
'''    
#login api
@app.route("/login",methods=['POST'])
def login():
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    email = request.json.get('email')
    password = request.json.get('password')
    sql="select * from `userdata` where `email`LIKE '{}' and `password` LIKE'{}' ".format(email,password)
    #sql="select * from `userdata` where `email`LIKE '{}'".format(email)
    mycursor.execute(sql)
    users=mycursor.fetchone()
    user_list = []
    for user in users:
        user_dict = {
            'userid': user[0],
            'fullname': user[1],
            'email': user[2],
            'createddate':user[5],
            'status':user[6]
        }
        user_list.append(user_dict)
    if users:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = users[2]
            # Redirect to home page
            return jsonify(users[2],{"login":"successfull"})
    else:
            # Account doesnt exist or username/password incorrect
            return jsonify({"login":"unsuccessfull"})
    
        
    return jsonify(user_list,{"login":"successfull"})
    #return jsonify({"login":"successfull"})'''
    
@app.route("/login",methods=['POST'])
def login():
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    email = request.json['email']
    password = request.json['password']
    sql="select * from `userdata` where `email`LIKE '{}'".format(email)
    mycursor.execute(sql)
    users=mycursor.fetchone()
    
    if users is None:
        return jsonify(users,{"error":"unauthorised access"})
    
    if not bcrypt.check_password_hash(users[3], password):
        return jsonify(users,{"error":"unauthorised access"})
    
    return jsonify({"login":"successfull"})

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop("username",None)
    return jsonify({"message":"loggedout"})

#search recipe by name
@app.route("/recipe/<recipename>",methods=['GET'])
def recipe_search_byname(recipename):
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    #recipename = request.args.get('recipename')
    #sql="select * from `recipedata` where `recipename`LIKE '{}'".format(recipename)
    sql = "SELECT * FROM `recipedata` WHERE `recipename` LIKE %s"
    params = ('%' + recipename + '%',)
    
    mycursor.execute(sql,params)
    users=mycursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'recipeid': user[0],
            'recipename': user[1],
            'ingredients': user[2],
            'totaltimeinmins': user[3],
            'servings': user[4],
            'cuisine':user[5],
            'course':user[6],
            'diet':user[7],
            'instructions':user[8],
            'imageurl':user[9]
        }
        user_list.append(user_dict)

    return jsonify(user_list)   



#search recipe by ingredient
@app.route("/recipe_search_by_ingredient/<ingredients>", methods=['GET'])
def recipe_search_by_ingredient(ingredients):
    db = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='recipe_app_db'
    )
    mycursor = db.cursor()

    ingredients = request.json.get('ingredients')
    
    sql = "SELECT * FROM `recipedata` WHERE `ingredients` LIKE %s"
    value = ('%' + ingredients + '%',)  # Using '%' for partial matching

    mycursor.execute(sql, value)
    recipes = mycursor.fetchall()
    recipe_list = []
    for recipe in recipes:
        recipe_dict = {
            'recipeid': recipe[0],
            'recipename': recipe[1],
            'ingredients': recipe[2],
            'totaltimeinmins': recipe[3],
            'servings': recipe[4],
            'cuisine': recipe[5],
            'course': recipe[6],
            'diet': recipe[7],
            'instructions': recipe[8],
            'imageurl': recipe[9]
        }
        recipe_list.append(recipe_dict)

    db.close()

    return jsonify(recipe_list)


# showing all recipes
@app.route("/recipes",methods=['GET'])
def explorenow():
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    
    sql="select * from `recipedata`"

    mycursor.execute(sql)
    users=mycursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'recipename': user[1],
            'imageurl':user[9]
        }
        user_list.append(user_dict)

    return jsonify(user_list)  

@app.route("/viewdetails", methods=['GET'])
def viewrecipe():
    db = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='recipe_app_db'
    )
    mycursor = db.cursor()

    recipename = request.args.get('recipename')
    
    print("recipename",recipename)
    
    sql="select * from `recipedata` where `recipename` LIKE '{}'".format(recipename)

    mycursor.execute(sql)
    recipes = mycursor.fetchall()
    recipe_list = []
    for recipe in recipes:
        recipe_dict = {
            'recipeid': recipe[0],
            'recipename': recipe[1],
            'ingredients': recipe[2],
            'totaltimeinmins': recipe[3],
            'servings': recipe[4],
            'cuisine': recipe[5],
            'course': recipe[6],
            'diet': recipe[7],
            'instructions': recipe[8],
            'imageurl': recipe[9]
        }
        recipe_list.append(recipe_dict)

    db.close()

    return jsonify(recipe_list)

# rating
@app.route("/setrate",methods=['POST'])
def raterecipe():
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    recipeid = request.json.get('recipeid')
    userid = request.json.get('userid')
    rating = request.json.get('rating')
    
    
    #checking for that recipe whether the user has already rated
    fetch="select * from `review` where `userid`='{}' and `recipeid` ='{}' ".format(userid,recipeid)
    mycursor.execute(fetch)
    user_exits=mycursor.fetchone()
    
    if user_exits:
        return jsonify({"message":"already rated"})
    
    else:
    
        usercount= "select count(ratingid) from review where recipeid = '{}'".format(recipeid)
        mycursor.execute(usercount)
        usercount = mycursor.fetchone()[0]
        
        # if rating exist for the recipe already
        if usercount>0:
            sumofrating="select sum(rating) from review where recipeid = '{}'".format(recipeid)
            mycursor.execute(sumofrating)
            sumofrating = mycursor.fetchone()[0]
            newrating = (int(sumofrating) + int(rating)) / (int(usercount) + 1)
            updatetable="insert into review(userid,recipeid,rating)values(%s,%s,%s)"
            values=(userid,recipeid,rating)
            mycursor.execute(updatetable,values)
            db.commit()
            return jsonify({"message": "rating added", "rating": int(newrating)})
        
        #if rating doesnt exist already
        else:
            updaterating="insert into review(userid,recipeid,rating)values(%s,%s,%s)"
            values=(userid,recipeid,rating)
            mycursor.execute(updaterating,values)
            db.commit()
            return jsonify({"message": "rating added(no existing ratings present)", "rating": rating})
        


    
  

@app.route("/dish")
def dish():
    return render_template('dish.html') 


if __name__ == "__main__":
    app.run(debug=True)