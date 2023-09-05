from app import db


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)