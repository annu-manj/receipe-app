from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RECIPEAPPDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Register(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(20))
    confirm_password = db.Column(db.String(20))
    
    def __repr__(self):
        return f"Register('{self.userid}','{self.fullname}', '{self.email}','{self.password}','{self.confirm_password}')"

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        new_register = Register(email=email, fullname=fullname, password=password, confirm_password=confirm_password)
        db.session.add(new_register)
        db.session.commit()

        return 'Signup successful!'

    return render_template('signup.html')

@app.route("/userdatabase")
def userdatabase():
    users =Register.query.all()
    return render_template('userdatabase.html',users=users)


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        login = Register.query.filter_by(username=email, password=password).first()
        if login is not None:
            return redirect(url_for("home"))
    return render_template("login.html")





def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)