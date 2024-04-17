from sqlalchemy import func
from models.schemas import Booking
from core import ma, db

def get_books(): 
    all_bookings = Booking.query.all()
    return bookings_schema.dump(all_bookings)

def add_book(book_att_id, book_event_id, book_venue_id, book_date):
    a = Booking(book_att_id=book_att_id, book_event_id=book_event_id, book_venue_id=book_venue_id, book_date=book_date, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_book(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Booking.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)