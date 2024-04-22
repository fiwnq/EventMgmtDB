from models.schemas import Venues
from core import ma, db

def get_venues():
    all_venues = Venues.query.all()
    return venues_schema.dump(all_venues)

def add_venue(venue_name, venue_location, venue_capacity, venue_contact):
    v = Venues(venue_name = venue_name, venue_location = venue_location, venue_capacity = venue_capacity, venue_contact = venue_contact)
    db.session.add(v)
    db.session.commit()

def delete_venue(id):
    data = Venues.query.get(id)
    db.session.delete(data)
    db.session.commit()
    
class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Venues

venue_schema = VenueSchema()
venues_schema = VenueSchema(many = True)
