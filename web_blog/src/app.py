from flask import Flask

__author__ = 'Sambasiva Rao Gangineni'

app = Flask(__name__)

@app.route('/') #www.examplesite.com/api/
def hello_method():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
