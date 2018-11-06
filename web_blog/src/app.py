from flask import Flask, render_template, request, session
from models.user import User

__author__ = 'Sambasiva Rao Gangineni'

app = Flask(__name__)

@app.route('/') #www.examplesite.com/api/
def hello_method():
    return render_template('login.html')

@app.route('/login')
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email,password):
        User.login(email)

    return render_template("profile.html", email=session['email'].split('@')[0])

if __name__ == "__main__":
    app.run()
