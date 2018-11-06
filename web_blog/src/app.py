from flask import Flask, render_template

__author__ = 'Sambasiva Rao Gangineni'

app = Flask(__name__)

@app.route('/') #www.examplesite.com/api/
def hello_method():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
