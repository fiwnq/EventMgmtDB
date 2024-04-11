from sqlalchemy import func
from models.schemas import Catering
from core import ma, db

def get_caterings(): 
    all_caterings = Catering.query.all()
    return caterings_schema.dump(all_caterings)

def add_catering(catering_bus_id):
    c = Catering(catering_bus_id = catering_bus_id, last_update=func.now())
    db.session.add(c)
    db.session.commit()

def delete_catering(id):
	data = Catering.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class CateringSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Catering

catering_schema = CateringSchema()
caterings_schema = CateringSchema(many=True)