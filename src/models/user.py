from db import db

class UserModel(db.Model):
    __tablename__ = 'LINKEDINUSER'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    works = db.relationship('WORK', lazy='dynamic')
    educations = db.relationship('EDUCATION', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name':self.name,
                'work': [work.json() for work in self.works.all()],
                'education':[education.json() for education in self.educations.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
