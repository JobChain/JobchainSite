from flask import Flask, Response, render_template, request, json, jsonify
# from flask_restful import Api
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from psql import User, Work, Education, PSQL, CheckedUser
# from security import authenticate, identity
# from resources.user import User

# from flask_jwt import JWT
from datetime import timedelta
import random
import json
from datetime import datetime

app = Flask(__name__, template_folder='./static', static_folder="./static", static_url_path="/src/static")
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.secret_key = 'scrappingboys'
# api = Api(app)

# Comment out DB for now
# db = PSQL()
# session = db.session

#Use {url}/auth to get jwt token for endpoints decorated with @jwt_required
#Payload = {username:str, password:str}
# jwt = JWT(app, authenticate, identity)

#look at /resources/user.py
# api.add_resource(User, '/user/<str:id>')

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

@app.route('/hardcoded_data', methods = ['GET'])
def get_json():
    with open('../LINKEDINUSER.json') as linkedinuser_data:
        linkedinuser = (json.load(linkedinuser_data))['linkedinuser']
    with open('../WORK.json') as work_data:
        work = (json.load(work_data))['work']

    users = {item['id']:item for item in linkedinuser}

    for w in work:
        c = {
            'company_name': w['company_name'],
            'start_date': w['start_date'],
            'end_date': w['end_date'],
            'location': w['location']
        }
        if 'companies' in users[w['user_id']]:
            users[w['user_id']]['companies'].append(c)
        else:
            users[w['user_id']]['companies'] = [c]

    for u in users:
        if 'companies' in users[u]:
            users[u]['companies'].sort(key=lambda x: datetime.strptime(x['start_date'], "%Y-%m-%d"))
        else:
            users[u]['companies'] = []

    return json.dumps(users)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
