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
            'password': user[3],
            'confirm_password': user[4]
        }
        user_list.append(user_dict)

    return jsonify(user_list)
    
@app.route("/recipe_search_byname/<RecipeName>",methods=['GET'])
def recipe_search_byname(RecipeName):
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
    mycursor=db.cursor()
    
    RecipeName = request.json.get('RecipeName')
    sql="select * from `recipe_data` where `RecipeName`LIKE '{}'".format(RecipeName)

    mycursor.execute(sql)
    users=mycursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'RecipeId': user[0],
            'RecipeName': user[1],
            'Ingredients': user[2],
            'TotalTimeInMins': user[3],
            'Servings': user[4],
            'Cuisine':user[5],
            'Course':user[6],
            'Diet':user[7],
            'Instructions':user[8],
            'URL':user[9]
        }
        user_list.append(user_dict)

    return jsonify(user_list)   


@app.route("/recipe_search_by_ingredient/<ingredient>", methods=['GET'])
def recipe_search_by_ingredient(ingredient):
    db = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        database='recipe_app_db'
    )
    mycursor = db.cursor()

    sql = "SELECT * FROM `recipe_data` WHERE `Ingredients` LIKE %s"
    value = ('%' + ingredient + '%',)  # Using '%' for partial matching

    mycursor.execute(sql, value)
    recipes = mycursor.fetchall()
    recipe_list = []
    for recipe in recipes:
        recipe_dict = {
            'RecipeId': recipe[0],
            'RecipeName': recipe[1],
            'Ingredients': recipe[2],
            'TotalTimeInMins': recipe[3],
            'Servings': recipe[4],
            'Cuisine': recipe[5],
            'Course': recipe[6],
            'Diet': recipe[7],
            'Instructions': recipe[8],
            'URL': recipe[9]
        }
        recipe_list.append(recipe_dict)

    db.close()

    return jsonify(recipe_list)
  

@app.route("/dish")
def dish():
    return render_template('dish.html') 


if __name__ == "__main__":
    app.run(debug=True)