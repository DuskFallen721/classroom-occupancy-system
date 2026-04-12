from .database import db

# Define your database models here

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
