from sqlalchemy import func
from models.schemas import BookedEvent
from core import ma, db

def get_bookedevents(): 
    all_bookedevents = BookedEvent.query.all()
    return bookedevents_schema.dump(all_bookedevents)

def add_bookedevent(be_event_id, be_venue_id):
    a = BookedEvent(be_event_id=be_event_id, be_venue_id=be_venue_id, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_bookedevent(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = BookedEvent.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class BookedEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookedEvent

bookedevent_schema = BookedEventSchema()
bookedevents_schema = BookedEventSchema(many=True)
