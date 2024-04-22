from models.schemas import Attendees
from core import ma, db

def get_atts(): 
    all_attendees = Attendees.query.all()
    return attendees_schema.dump(all_attendees)

def add_att(att_name, att_email, att_org_id):
    a = Attendees(att_name=att_name, att_email=att_email, att_org_id=att_org_id)
    db.session.add(a)
    db.session.commit()

def delete_att(id):
	data = Attendees.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class AttendeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendees
        include_fk = True

attendee_schema = AttendeeSchema()
attendees_schema = AttendeeSchema(many=True)
