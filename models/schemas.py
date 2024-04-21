from sqlalchemy import ForeignKey
from core import db

class Speakers(db.Model):

    speaker_id = db.Column(db.Integer, primary_key = True)
    speaker_name = db.Column(db.String(50), unique = True, nullable = False)
    speaker_bio = db.Column(db.String(1000), unique = False, nullable = True)
    speaker_info = db.Column(db.String(100), unique = False, nullable = True)


class Events(db.Model):
    
    event_id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(100), unique = True, nullable = False)
    event_datetime = db.Column(db.DateTime, unique = True, nullable = False)
    event_desc = db.Column(db.String(1000), unique = False, nullable = True)


class Venues(db.Model):
    
    venue_id = db.Column(db.Integer, primary_key = True)
    venue_name = db.Column(db.String(100), unique = True, nullable = False)
    venue_location = db.Column(db.String(50), unique = False, nullable = False)
    venue_capacity = db.Column(db.Integer, unique = False, nullable = True)
    venue_contact = db.Column(db.String(100), unique = False, nullable = True)


class Organizations(db.Model):

    org_id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(50), unique=True, nullable=False)
    org_desc = db.Column(db.String(300), unique=False, nullable=True)


class Attendees(db.Model):

    att_id = db.Column(db.Integer, primary_key=True)
    att_name = db.Column(db.String(50), unique=True, nullable=False)
    att_email = db.Column(db.String(100), unique=False, nullable=True)
    att_org_id = db.Column(db.Integer, ForeignKey(Organizations.org_id), unique=False, nullable=True)


class Bookings(db.Model):

    book_id = db.Column(db.Integer, primary_key = True)
    book_att_id = db.Column(db.Integer, ForeignKey(Attendees.att_id), unique = False, nullable = False)
    book_event_id = db.Column(db.Integer, ForeignKey(Events.event_id), unique = False, nullable = False)
    book_venue_id = db.Column(db.Integer, ForeignKey(Venues.venue_id), unique = False, nullable = False)
    book_date = db.Column(db.Date, unique = False, nullable = False)


class Catering(db.Model):

    catering_id = db.Column(db.Integer, primary_key = True)
    catering_business = db.Column(db.String(100), unique = True, nullable = False)
    catering_type = db.Column(db.String(50), unique = False, nullable = True)
    catering_event_id = db.Column(db.Integer, ForeignKey(Events.event_id), unique = False, nullable = False)
    catering_servings = db.Column(db.Integer, unique = False, nullable = True)
    catering_time = db.Column(db.Time, unique = False, nullable = True)


class Stations(db.Model):

    station_id = db.Column(db.Integer, primary_key = True)
    station_venue_id = db.Column(db.Integer, ForeignKey(Venues.venue_id), unique = False, nullable = False)
    station_speaker_id = db.Column(db.Integer, ForeignKey(Speakers.speaker_id), unique = False, nullable = False)
    station_topic = db.Column(db.String(100), unique = True, nullable = False)
    station_capacity = db.Column(db.Integer, unique = False, nullable = True)
