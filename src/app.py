from flask import Flask, render_template, request
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from psql import User, Work, Education, PSQL, CheckedUser
import random

app = Flask(__name__, template_folder='./static', static_folder="./static", static_url_path="/src/static")
db = PSQL()
session = db.session
print(session)

@app.route('/components/<path:path>')
def serve_partial(path):
    return render_template('/components/{}'.format(path))

@app.route("/", methods=['GET'])
def index():
    errors = []
    results = {}
    if request.method == "GET":
        pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
