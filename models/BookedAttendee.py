from sqlalchemy import func
from models.schemas import BookedAttendee
from core import ma, db

def get_bookedattendees(): 
    all_bookedattendees = BookedAttendee.query.all()
    return bookedattendees_schema.dump(all_bookedattendees)

def add_bookedattendee(ba_event_id, ba_att_id, ba_time):
    a = BookedAttendee(ba_event_id=ba_event_id, ba_att_id=ba_att_id, ba_time=ba_time, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_bookedattendee(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = BookedAttendee.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class BookedAttendeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookedAttendee

bookedattendee_schema = BookedAttendeeSchema()
bookedattendees_schema = BookedAttendeeSchema(many=True)
