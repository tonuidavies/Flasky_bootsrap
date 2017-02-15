from flask import Flask
from flask sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost/flask_movies'

db = SQLAlchemy


# clear


if __name__ =="__main__":
    app.run()
    debug = True
