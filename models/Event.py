from sqlalchemy import func
from models.schemas import Event
from core import ma, db

def get_events():
    all_events = Event.query.all()
    return events_schema.dump(all_events)

def add_event(event_title, event_datetime, event_desc):
    e = Event(event_title = event_title, date_time = event_datetime, event_desc = event_desc, last_update = func.now())
    db.session.add(e)
    db.session.commit()

def delete_event(id):
    data = Event.query.get(id)
    db.session.delete(data)
    db.session.commit()

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event

event_schema = EventSchema()
events_schema = EventSchema(many = True)