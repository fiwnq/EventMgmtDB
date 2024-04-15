from sqlalchemy import func
from models.schemas import Attendee
from core import ma, db

def get_attendees(): 
    all_attendees = Attendee.query.all()
    return attendees_schema.dump(all_attendees)

def add_attendee(att_name, att_email, org_id):
    a = Attendee(att_name=att_name, att_email=att_email, org_id=org_id, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_attendee(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Attendee.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class AttendeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendee

attendee_schema = AttendeeSchema()
attendees_schema = AttendeeSchema(many=True)
