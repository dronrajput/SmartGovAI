from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Citizen(db.Model):
    __tablename__ = 'citizens'
    citizen_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Feedback(db.Model):
    __tablename__ = 'feedback'
    feedback_id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.citizen_id'))
    feedback_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20))
    category = db.Column(db.String(50))
    urgency_level = db.Column(db.String(20))
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
