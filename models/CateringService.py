from sqlalchemy import func
from models.schemas import CateringService
from core import ma, db

def get_cateringServices(): 
    all_caterings = CateringService.query.all()
    return caterings_schema.dump(all_caterings)

def add_cateringService(cs_catering_id, cs_event_id, cs_servings, cs_type, cs_time):
    cs = CateringService(cs_catering_id = cs_catering_id, cs_event_id = cs_event_id, cs_servings = cs_servings, cs_type = cs_type, cs_time = cs_time, last_update=func.now())
    db.session.add(cs)
    db.session.commit()

def delete_cateringService(id):
	data = CateringService.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class CateringServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CateringService

catering_schema = CateringServiceSchema()
caterings_schema = CateringServiceSchema(many=True)