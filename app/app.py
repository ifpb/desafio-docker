from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_CONFIG_URI')
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return "Bem-vindo à minha aplicação web!"

@app.route('/users')
def get_users():
    users = Users.query.all()
    return jsonify([u.name for u in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0')