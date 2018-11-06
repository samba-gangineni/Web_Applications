from flask import Flask, render_template, request, session
from models.user import User
from models.database import Database

__author__ = 'Sambasiva Rao Gangineni'

app = Flask(__name__)
app.secret_key = "samba"

@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/login') #www.examplesite.com/api/
def login_template():
    return render_template('login.html')

@app.route('/register')
def register_template():
    return render_template('register.html')

@app.before_first_request
def intialize_database():
    Database.initialize()

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email,password):
        User.login(email)
    else:
        session['email']=None
        return render_template("register.html", message="User does not exsists! Sign Up")
    


    return render_template("profile.html", email=session['email'].split('@')[0])

@app.route('/auth/register',methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email,password)
 
    return render_template("profile.html", email=session['email'].split('@')[0])

if __name__ == "__main__":
    app.run()
