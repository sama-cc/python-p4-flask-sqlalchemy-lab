#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    return '<ul>Name.</ul><ul>Species.</ul><ul>Zookeeper</ul><ul>Enclosure</ul>'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return '<ul>Name.</ul><ul>Birthday.</ul><ul>Animal.</ul>'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return '<ul>Environment.</ul><ul>Open to Visitors.</ul><ul>Animal.</ul>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
