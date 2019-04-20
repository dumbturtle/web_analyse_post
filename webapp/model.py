
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class lm_nlp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '{}'.format(self.text)


class class_nlp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '{} {}'.format(self.text, self.rating)
