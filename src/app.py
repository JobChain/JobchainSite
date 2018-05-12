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

@app.route('/company_data', methods = ['GET'])
def get_company_data():
    with open('../WORK.json') as work_data:
        work = (json.load(work_data))['work']
    with open('../COMPANY.json') as company_data:
        company = (json.load(company_data))['company']

    companies = {}

    for w in work:
        c = w['company_name']
        if c in companies:
            companies[c]['userCount'] += 1
        elif c:
            companies[c] = {
                'company_name': c,
                'userCount': 1,
                'positions': [],
                'logo': '',
                'url': ''
            }

            company_data = None

            for com in company:
                if com['id'] == c:
                    company_data = com

            if company_data:
                companies[c]['logo'] = company_data['logo']
                companies[c]['url'] = company_data['url']
                if 'locations' in company_data:
                    loc = company_data['locations']
                    pretty = ""
                    for l in loc:
                        if l is not ("" or " "):
                            pretty = pretty + l
                            pretty = pretty + '*'
                    companies[c]['locations'] = pretty
                else:
                    companies[c]['locations'] = ''

    return json.dumps(companies)

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
            'location': w['location'],
            'job_title': w['job_title']
        }
        if 'companies' in users[w['user_id']]:
            users[w['user_id']]['companies'].append(c)
        else:
            users[w['user_id']]['companies'] = [c]

    return json.dumps(filterWastemans(users))

def filterWastemans(users):
    for u in users:
        if 'companies' in users[u]:
            users[u]['companies'].sort(key=lambda x: datetime.strptime(x['start_date'], "%Y-%m-%d"))

            filteredCompanies = []
            for c in users[u]['companies']:
                startDate = c['start_date']
                endDate = c['end_date']
                title = c['job_title'].lower()

                if endDate is not None:
                    duration = (datetime.strptime(endDate, "%Y-%m-%d") -  datetime.strptime(startDate, "%Y-%m-%d"))
                    start = datetime.strptime(startDate, "%Y-%m-%d").strftime('%B')
                    jan = datetime.strptime("January", "%B").strftime('%B')
                    may = datetime.strptime("May", "%B").strftime('%B')
                    sept = datetime.strptime("September", "%B").strftime('%B')

                    if duration.days < 93 and duration.days > 89:
                        if start == jan or start == may or start == sept:
                            filteredCompanies.append(c)
                    elif duration.days < 123 and duration.days > 119:
                        if start == jan or start == may or start == sept:
                            filteredCompanies.append(c)
                    elif duration.days < 248 and duration.days > 240:
                        if start == jan or start == may or start == sept:
                            filteredCompanies.append(c)
                    elif ('intern' in title.lower()) or ('coop' in title.lower()) or ('co-op' in title.lower()) or ('internship' in title.lower()):
                        filteredCompanies.append(c)
                else:
                    start = datetime.strptime(startDate, "%Y-%m-%d")
                    may = datetime.strptime("2018-05-01", "%Y-%m-%d")
                    duration = (may - start).days
                    if ('intern' in title.lower()) or ('coop' in title.lower()) or ('co-op' in title.lower()) or ('internship' in title.lower()):
                        filteredCompanies.append(c)
                    elif duration < 5:
                        filteredCompanies.append(c)
            users[u]['companies'] = filteredCompanies

    filteredUsers = {u:users[u] for u in users if 'companies' in users[u] and len(users[u]['companies']) > 1}
    return filteredUsers

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
