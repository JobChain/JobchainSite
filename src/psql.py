from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'LINKEDINUSER'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    def __repr__(self):
       return "<User(id='%s', name='%s')>" % (
                            self.id, self.name)

class Work(Base):
    __tablename__ = 'WORK'
    id = Column(Integer, Sequence('work_id_seq'), primary_key=True)
    company_name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    job_title = Column(String)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    current = Column(Boolean)

    def __repr__(self):
       return "<Work(name='%s', user id='%s', job title='%s')>" % (
                            self.company_name, self.user_id, self.job_title)

class Education(Base):
    __tablename__ = 'EDUCATION'
    id = Column(Integer, Sequence('education_id_seq'), primary_key=True)
    school_name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    program = Column(String)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    current = Column(Boolean)
    duration = Column(String)

    def __repr__(self):
       return "<Education(name='%s', user id='%s', program='%s')>" % (
                            self.school_name, self.user_id, self.program)

class CheckedUser(Base):
    __tablename__ = 'CHECKEDUSER'

    id = Column(String, primary_key=True)
    def __repr__(self):
       return "<User(id='%s')>" % (
                            self.id)

class PSQL:
    def __init__(self):
        print('Opening connection to PSQL DB')

        self.psql_username = os.getenv('PSQL_USERNAME')
        self.psql_password = os.getenv('PSQL_PASSWORD')
        self.psql_address = os.getenv('PSQL_ADDRESS')
        self.psql_db = os.getenv('PSQL_DB')
        self.verify_env_var()

        db_string = "postgresql://" + self.psql_username + ":" + self.psql_password + "@" + self.psql_address + ":5432/" + self.psql_db
        self.db = create_engine(db_string)
        self.Session = sessionmaker(self.db)
        self.session = self.Session()
        Base.metadata.create_all(self.db)
        print('Opened connection to PSQL DB')

    def verify_env_var(self):
        if not self.psql_username:
            print("Missing psql_username")
            sys.exit(0)
        elif not self.psql_password:
            print("Missing psql_password")
            sys.exit(0)
        elif not self.psql_address:
            print("Missing psql_address")
            sys.exit(0)
        elif not self.psql_db:
            print("Missing psql_db")
            sys.exit(0)
