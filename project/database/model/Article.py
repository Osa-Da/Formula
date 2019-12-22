from datetime import datetime
from project import db
from flask_sqlalchemy import SQLAlchemy

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    text = db.Column(db.Text)
    date = db.Column(db.Date)
    images = db.Column(db.Text)
    region = db.Column(db.Integer)

    def __init__(self, title, description, text, date, images, region):
        self.title = title
        self.description = description
        self.text = text
        self.date = datetime.strptime(date, '%d.%m.%Y').date()
        self.images = images
        self.region = region


