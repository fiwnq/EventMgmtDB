from sqlalchemy import func
from models.schemas import Organizations
from core import ma, db

def get_orgs(): 
    all_orgs = Organizations.query.all()
    return orgs_schema.dump(all_orgs)

def add_org(org_name, org_desc):
    a = Organizations(org_name=org_name, org_desc=org_desc, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_org(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Organizations.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class OrganizationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Organizations

org_schema = OrganizationSchema()
orgs_schema = OrganizationSchema(many=True)
