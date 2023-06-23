from flask import Flask, render_template, request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json
import csv
import MySQLdb

with open('IndianFoodDatasetCSV.csv','r') as file:
    reader = csv.reader(file) 
    
    db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
)
    mycursor=db.cursor() 
    
    for row in reader:
        mycursor.execute('insert into recipe_data(RecipeName,Ingredients,TotalTimeInMins,Servings,Cuisine,Course,Diet,Instructions,URL)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
        
    db.commit()

mycursor.close()
    
    