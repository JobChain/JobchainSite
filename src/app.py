<<<<<<< HEAD
from flask import Flask, render_template, request
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from psql import User, Work, Education, PSQL, CheckedUser
import random

app = Flask(__name__, template_folder='./static')
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
=======
from flask import Flask, render_template
import random
app = Flask(__name__, template_folder='./static')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
>>>>>>> 15fd1f70cc9d43a264d316d3ad0fb5c22ad098e7
