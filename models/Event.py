from models.schemas import Events
from core import ma, db

def get_events():
    all_events = Events.query.all()
    return events_schema.dump(all_events)

def add_event(event_title, event_datetime, event_desc):
    e = Events(event_title = event_title, date_time = event_datetime, event_desc = event_desc)
    db.session.add(e)
    db.session.commit()

def delete_event(id):
    data = Events.query.get(id)
    db.session.delete(data)
    db.session.commit()

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Events

event_schema = EventSchema()
events_schema = EventSchema(many = True)