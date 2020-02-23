from . import db


class Pollen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    level_text = db.Column(db.String(50))
    level = db.Column(db.String(50))
    city = db.Column(db.String(50))
    date = db.Column(db.DateTime)

    def __init__(self, name, level_text, level, city, date):
        self.name = name
        self.level_text = level_text
        self.level = level
        self.city = city
        self.date = date

    def __repr__(self):
        return '<Pollen %r>' % self.name


