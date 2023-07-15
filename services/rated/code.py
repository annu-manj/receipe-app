#importing required modules
from flask import Blueprint,Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pandas as pd
import json
import csv

top_rated_blueprint = Blueprint('code', __name__, url_prefix="")

db = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='',
    database='recipe_app_db'
    )
#Fetching required data from db
@top_rated_blueprint.route('/toprate')
def get_top_rated():
    #def data():
    mycursor=db.cursor()
    
    # Execute a SELECT query to retrieve data from the 'review,recipedata' table
    mycursor.execute('SELECT r.userid,r.recipeid,r.rating,rc.recipename,rc.imageurl FROM review r,recipedata rc WHERE r.recipeid=rc.recipeid')
    
    # Fetch all rows returned by the query
    rows = mycursor.fetchall()
    # Convert the data into a list of dictionaries
    rates = []
    for row in rows:
        rate = {
            'userid':row[0],
            'recipeid': row[1],
            'rating': row[2],
            'recipename': row[3],
            'imageurl': row[4]
        }
        rates.append(rate)
   
    # Convert the list of dictionaries to a JSON string
    json_data = json.dumps(rates)

    # Specify the CSV file path
    csv_file_path = 'dbr.csv'

    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rates[0].keys())
    
        # Write the header row
        writer.writeheader()
    
        # Write each data row
        for rate in rates:
            writer.writerow(rate)
    
    #Top_Ratings calculation using Weighted_Average 

    #Reading csv as a dataframe
    combined_df=pd.read_csv(r"dbr.csv")
    
    #calculating total_rating_count that each recipe had
    no_of_votes=(combined_df.groupby(by=['recipeid'])['rating'].count().reset_index().
    rename(columns = {'rating': 'totalRatingCount'})
    [['recipeid', 'totalRatingCount']])

    #calculating avg(mean)_of_rating for each recipe--(r)
    ratings_avg=(combined_df.groupby(by=['recipeid'])['rating'].mean().reset_index().
    rename(columns = {'rating': 'avg'})
    [['recipeid', 'avg']])

    #copies recipename series from combined_df to no_of_votes df
    no_of_votes['recipename']=combined_df['recipename']

    #copies average series from ratings_avg df to no_of_votes df
    no_of_votes['average']=ratings_avg['avg']
    
    #copies imageurl series from combined_df to no_of_votes df
    no_of_votes['imageurl']=combined_df['imageurl']

    #weighted Rating calculation
    #'weighted_average'=((r*v)+(c*m))/(v+m)
    v=no_of_votes['totalRatingCount']#no.of votes for each recipe
    m=no_of_votes['totalRatingCount'].quantile(0.70)#minimum votes required for each recipe
    r=no_of_votes['average']#avg of the ratings for each recipe
    c=no_of_votes['totalRatingCount'].mean()#mean vote across the whole report

    #includes a weighted_avg series in no_of_votes df
    no_of_votes['weighted_avg']=((r*v)+(c*m))/(v+m)

    #listing out top_rated recipes
    recipe=no_of_votes.sort_values('weighted_avg',ascending=False)
    lists=recipe[['recipename','weighted_avg','recipeid']]
    list=recipe[['recipename','recipeid','imageurl']]
    
    #fetching top_rated 6 recipes
    top_list=list.head(6)

    #Convert the DataFrame to JSON
    json_response = top_list.to_json(orient='records')

    # Return the JSON response
    return jsonify(json_response)
