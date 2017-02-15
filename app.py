from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost/flask_movie'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

#now posting data to my site

@app.route('/')
def index():
    return  render_template('add_user.html')
@app.route('/post_user', methods=['POST'])
def post_user():
    return ("Welcome to my homepage ")

if __name__ =="__main__":
    app.run()
    debug = True
