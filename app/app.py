from flask import Flask, render_template, request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json
import csv
import MySQLdb

app = Flask(__name__)
ma=Marshmallow(app)
db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
)
CORS(app)




@app.route("/",methods=['GET']) 
def index():
    return jsonify({"message":"working"})

@app.route("/signup", methods=[ 'POST'])
def signup():
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    fullname = request.json.get('fullname')
    email = request.json.get('email')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')
    
    check_query = "SELECT * FROM user_details WHERE email = %s"
    check_values = (email,)
    mycursor.execute(check_query, check_values)
    existing_user = mycursor.fetchone()

    if existing_user:
        return jsonify({"message": "User already exists"})


    sql="insert into user_details(fullname,email,password,confirm_password)values(%s,%s,%s,%s)"
    values=(fullname,email,password,confirm_password)
    mycursor.execute(sql,values)
    db.commit()
        
    return jsonify({"message":"signed up"})

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
    sql="select * from `user_details` where `email`LIKE '{}' and `password` LIKE'{}' ".format(email,password)

    mycursor.execute(sql)
    users=mycursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'user_id': user[0],
            'fullname': user[1],
            'email': user[2],
        }
        user_list.append(user_dict)

    return jsonify(user_list)
    
@app.route("/recipe_search_byname/<recipename>",methods=['GET'])
def recipe_search_byname(recipename):
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    recipename = request.json.get('recipename')
    sql="select * from `recipedata` where `recipename`LIKE '{}'".format(recipename)

    mycursor.execute(sql)
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
  

@app.route("/dish")
def dish():
    return render_template('dish.html') 


if __name__ == "__main__":
    app.run(debug=True)