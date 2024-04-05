from sqlalchemy import func
from models.schemas import Organization
from core import ma, db

def get_orgs(): 
    all_orgs = Organization.query.all()
    return actors_schema.dump(all_orgs)

def add_org(first_name, last_name):
    a = Organization(first_name=first_name, last_name=last_name, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_actor(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Organization.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class OrganizationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Organization

actor_schema = OrganizationSchema()
actors_schema = OrganizationSchema(many=True)
