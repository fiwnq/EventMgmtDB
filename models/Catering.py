from models.schemas import Catering
from core import ma, db

def get_caterings(): 
    all_caterings = Catering.query.all()
    return caterings_schema.dump(all_caterings)

def add_catering(catering_business, catering_type, catering_event_id, catering_servings, catering_time):
    c = Catering(catering_business=catering_business, catering_type=catering_type, catering_event_id=catering_event_id, catering_servings=catering_servings, catering_time=catering_time)
    db.session.add(c)
    db.session.commit()

def delete_catering(id):
	data = Catering.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class CateringSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Catering
        include_fk = True

catering_schema = CateringSchema()
caterings_schema = CateringSchema(many=True)