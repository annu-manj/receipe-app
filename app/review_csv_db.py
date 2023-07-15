from flask import Flask
import mysql.connector
from flask_marshmallow import Marshmallow
import csv
import MySQLdb

with open('recrate.csv','r') as file:
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
        mycursor.execute('insert into review(userid,recipeid,rating)values(%s,%s,%s)',row)
        
    db.commit()

mycursor.close()
    
    