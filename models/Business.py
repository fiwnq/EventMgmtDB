from sqlalchemy import func
from models.schemas import Business
from core import ma, db

def get_businesses(): 
    all_businesses = Business.query.all()
    return businesses_schema.dump(all_businesses)

def add_business(business_name, business_bio, business_contact):
    b = Business(business_name, business_bio = business_bio, business_contact = business_contact, last_update=func.now())
    db.session.add(b)
    db.session.commit()

def delete_buisness(id):
	data = Business.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class BusinessSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Business

business_schema = BusinessSchema()
businesses_schema = BusinessSchema(many=True)