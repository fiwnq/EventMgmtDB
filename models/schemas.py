from sqlalchemy import ForeignKey, DateTime
from core import db
from sqlalchemy.sql import func

# Models
class Actor(db.Model):
 
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
 
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"


class Event(db.Model):
    
    event_id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(100), unique = True, nullable = False)
    event_datetime = db.Column(db.DateTime, unique = True, nullable = False)
    event_desc = db.Column(db.String(1000), unique = False, nullable = True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Venue(db.Model):
    
    venue_id = db.Column(db.Integer, primary_key = True)
    venue_name = db.Column(db.String(100), unique = True, nullable = False)
    venue_location = db.Column(db.String(50), unique = False, nullable = False)
    venue_capacity = db.Column(db.Integer, unique = False, nullable = False)
    venue_contact = db.Column(db.String(100), unique = False, nullable = True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Organization(db.Model):

    org_id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(50), unique=True, nullable=False)
    org_desc = db.Column(db.String(300), unique=False, nullable=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Attendee(db.Model):

    att_id = db.Column(db.Integer, primary_key=True)
    att_name = db.Column(db.String(50), unique=True, nullable=False)
    att_email = db.Column(db.String(100), unique=False, nullable=True)
    att_org_id = db.Column(db.Integer, ForeignKey(Organization.org_id), unique=False, nullable=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Business(db.Model):

    business_id = db.Column(db.Integer, primary_key = True)
    business_name = db.Column(db.String(50), unique = True, nullable = False)
    business_bio = db.Column(db.String(500), unique = True, nullable = True)
    business_contact = db.Column(db.String(100), unique = True, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class BookedEvent(db.Model):

    be_id = db.Column(db.Integer, primary_key = True)
    be_event_id = db.Column(db.Integer, ForeignKey(Event.event_id), unique = False, nullable = False)
    be_venue_id = db.Column(db.Integer, ForeignKey(Venue.venue_id), unique = False, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class BookedAttendee(db.Model):

    ba_id = db.Column(db.Integer, primary_key = True)
    ba_event_id = db.Column(db.Integer, ForeignKey(Event.event_id), unique = False, nullable = False)
    ba_att_id = db.Column(db.Integer, ForeignKey(Attendee.att_id), unique = False, nullable = False)
    ba_time = db.Column(db.Time, unique = False, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Catering(db.Model):

    catering_id = db.Column(db.Integer, primary_key = True)
    catering_bus_id = db.Column(db.Integer, ForeignKey(Business.business_id), unique = False, nullable = False, default = 1)
    catering_type = db.Column(db.String(50), unique = False, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class CateringService(db.Model):

    cs_id = db.Column(db.Integer, primary_key = True)
    cs_catering_id = db.Column(db.Integer, ForeignKey(Catering.catering_id), unique = False, nullable = False)
    cs_event_id = db.Column(db.Integer, ForeignKey(Event.event_id), unique = False, nullable = False)
    cs_servings = db.Column(db.Integer, unique = False, nullable = False)
    cs_time = db.Column(db.Time, unique = False, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Speaker(db.Model):

    speaker_id = db.Column(db.Integer, primary_key = True)
    speaker_name = db.Column(db.String(50), unique = True, nullable = False)
    speaker_bio = db.Column(db.String(1000), unique = False, nullable = True)
    speaker_info = db.Column(db.String(100), unique = False, nullable = True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class Station(db.Model):

    station_id = db.Column(db.Integer, primary_key = True)
    station_venue_id = db.Column(db.Integer, ForeignKey(Venue.venue_id), unique = False, nullable = False)
    station_speaker_id = db.Column(db.Integer, ForeignKey(Speaker.speaker_id), unique = False, nullable = False)
    station_capacity = db.Column(db.Integer, unique = False, nullable = True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())


class StationTopic(db.Model):
    
    st_id = db.Column(db.Integer, primary_key = True)
    st_station_id = db.Column(db.Integer, ForeignKey(Station.station_id), unique = False, nullable = False)
    st_topic = db.Column(db.String(100), unique = True, nullable = False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
