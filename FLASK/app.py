from flask import Flask, render_template, request,jsonify
import mysql.connector

app = Flask(__name__,template_folder='templates')

# Replace the values below with your MySQL database credentials
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Aksh29@03sql',
    database='sample'
)


@app.route('/')
def home():
    return render_template('new_goal.html')


@app.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    name = request.form['name']


    cursor = db.cursor()
    sql = 'INSERT INTO sample.testing (id,name) VALUES (%s,%s)'
    values = (id,name)
    cursor.execute(sql, values)
    db.commit()

    return 'added'

@app.route('/get', methods=['GET'])
def get_data():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aksh29@03sql',
        database='sample'
    )
    cursor=db.cursor()
    sql="SELECT *FROM sample.testing"
    cursor.execute(sql)
    result=cursor.fetchall()

    data=[]
    for row in result:
        data.append({
            'id':row[0],
            'name':row[1]

        })
    return jsonify(data)




if __name__== '__main__':
    app.run(debug=True)