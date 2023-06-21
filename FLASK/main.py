from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__,template_folder='templates')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Aksh29@03sql',
    database='sample'
)


@app.route('/')

def new_goal():
    return render_template('form.html')

@app.route('/add_goals',methods=['POST'])

def add_goals():
    # if request.method =="POST":

        goalID = request.form['goalID']
        goalName = request.form['goalName']
        goalType = request.form['goalType']
        goalBeginDate = request.form['goalBeginDate']
        goalEndDate = request.form['goalEndDate']
        goalUrl = request.form['goalUrl']
        goalImageUrl = request.form['goalImageUrl']
        goalDescription = request.form['goalDescription']
        isPaid = request.form['isPaid']
        category = request.form['category']
        goalStatus = request.form['goalStatus']
        archived = request.form['archived']
        sharedInfo = request.form['sharedInfo']




        mycursor=db.cursor()

        query='INSERT INTO sample.kavigai_goal(goalID,goalName,goalType,goalBeginDate,goalEndDate,goalUrl,goalImageUrl,goalDescription,isPaid,category,goalStatus,archived,sharedInfo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (goalID,goalName,goalType,goalBeginDate,goalEndDate,goalUrl,goalImageUrl,goalDescription,isPaid,category,goalStatus,archived,sharedInfo)
        mycursor.execute(query,values)
        db.commit()
        # return redirect(url_for('/goals'))
        return "added"

    # a.commit()
    # # mycursor.close()
    # a.close()



# def get_goals():
#     a=mysql.connector.connect(user="root",password="Aksh29@03sql",host="localhost",database="sample")
#     mycursor=a.cursor()

if __name__ == '__main__':
    app.run(debug=True)