from flask import Flask, render_template, request, session, redirect, url_for
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
def register_templates(x="Join Us!"):
    return render_template('register.html', message=x)

@app.route('/register/<x>')
def register_template(x):
    return render_template('register.html', message=x)

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
        register_template(x="User does not exsists! Register here")
        return redirect(url_for('register_template',x="User does not exsists! Register here"))
    
    return render_template("profile.html", email=session['email'].split('@')[0] if session['email'] is not None and '@' in session['email'] else session['email'])

@app.route('/auth/register',methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email,password)
 
    return render_template("profile.html", email=session['email'].split('@')[0] if session['email'] is not None and '@' in session['email'] else session['email'])

if __name__ == "__main__":
    app.run()
