from flask import Flask, Response, render_template, request, json, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from psql import User, Work, Education, PSQL, CheckedUser
import random

app = Flask(__name__, template_folder='./static', static_folder="./static", static_url_path="/src/static")
db = PSQL()
session = db.session

@app.route('/components/<path:path>')
def serve_partial(path):
    return render_template('/components/{}'.format(path))

@app.route('/data', methods = ['GET'])
def api_data():
    import pdb
    query = (session
        .query(User, Work, Education)
        .filter(User.id == Work.user_id)
        .filter(Work.user_id == Education.user_id)
    )
    data = []
    data = [{'User': u.serialize, 'Work': w.serialize, 'Education': e.serialize} for u, w, e in query]
    js = json.dumps({
        'data': data
    })

    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
