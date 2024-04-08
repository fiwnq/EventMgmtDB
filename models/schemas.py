from sqlalchemy import DateTime
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
    
class ActorInfo(db.Model):

    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    film_info = db.Column(db.String(255), nullable=True)

class Organization(db.Model):

    org_id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(50), unique=True, nullable=True)
    org_desc = db.Column(db.String(300), unique=False, nullable=True)


class Attendee(db.Model):

    att_id = db.Column(db.Integer, primary_key=True)
    att_name = db.Column(db.String(50), unique=True, nullable=True)
    att_email = db.Column(db.String(100), unique=False, nullable=True)
    org_id = db.Column(db.Integer, unique=False, nullable=True) # foreign key, how do i implement this?

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(100), unique = True, nullable = False)
    event_datetime = db.Column(db.DateTime, unique = True, nullable = False)
    event_desc = db.Column(db.String(1000), unique = False, nullable = True)

class Venue(db.Model):
    venue_id = db.Column(db.Integer, primary_key = True)
    venue_title = db.Column(db.String(100), unique = True, nullable = False)
    venue_location = db.Column(db.String(50), unique = False, nullable = False)
    venue_capacity = db.Column(db.Integer, unique = False, nullable = False)
    venue_contact = db.Column(db.String(100), unique = False, nullable = True)
