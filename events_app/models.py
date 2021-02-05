"""Create database models to represent tables."""
from events_app import db
from datetime import datetime
from sqlalchemy.orm import backref


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    events_attending = db.relationship('Event', secondary = 'guest_event')

    def __str__(self):
        return f'<Name: {self.name}>'

    def __repr__(self):
        return f'<Name: {self.name}>'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    date_and_time = db.Column(db.Date)
    guests = db.relationship('Guest', secondary = 'guest_event')

    def __str__(self):
        return f'<Event Title: {self.title}>'

    def __repr__(self):
        return f'<Event Title: {self.title}>'

guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))

)


guest_event_table = None
