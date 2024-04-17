from core import app
from flask import redirect, request 
from flask.templating import render_template
from models import Actor, Attendee, Booking, Catering, CateringService, Event, Organization, Speaker, Station, Venue

@app.route('/hello')
def hello():
	return 'HELLO'

@app.route('/')
def home():
	return render_template('home.html')

# -------------------------- ACTORS --------------------------------

# unused?
@app.route('/get_actors', methods=['GET','POST']) 
def get_results(): 
    actors = Actor.get_actors()  
    return actors 

# APP ROUTE TO RENDER INDEX PAGE WITH LIST OF ACTORS
@app.route('/actor_index')
def actor_index():
	# Query all data and then pass it to the template
	actors = Actor.get_actors()
	return render_template('actor_index.html', actors=actors)

# APP ROUTE TO RENDER FORM TO ADD ACTOR DATA
@app.route('/add_actor_data')
def add_actor_data():
	return render_template('add_actor.html')

# APP ROUTE TO CALL FUNCTION TO ADD ACTOR
@app.route('/add_actor', methods=["POST"])
def add_actor():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")

	# call model function that will store data as a row in our datatable
	if first_name != '' and last_name != '':
		Actor.add_actor(first_name, last_name)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE ACTOR
@app.route('/delete_actor/<int:id>')
def delete_actor(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	Actor.delete_actor(id)
	return redirect('/')

# -------------------------- EVENTS --------------------------------

@app.route('/add_event', methods=["POST"])
def add_event():
	
	event_name = request.form.get("event_name")
	event_datetime = request.form.get("event_datetime")
	event_desc = request.form.get("event_desc")

	if event_name != '' and event_datetime != '':
		Event.add_event(event_name, event_datetime, event_desc)
		return redirect('/')
	else:
		return redirect('/')
	
@app.route('/event_index')
def event_index():
	events = Event.get_events()
	return render_template('event_index.html', events=events)

@app.route('/add_event_data')
def add_event_data():
	return render_template('add_event.html')

@app.route('/delete_event/<int:id>')
def delete_event(id):
	Event.delete_event(id)
	return redirect('/')

# -------------------------- VENUES --------------------------------

@app.route('/add_venue', methods=["POST"])
def add_venue():
	
	venue_name = request.form.get("venue_name")
	venue_location = request.form.get("venue_location")
	venue_capacity = request.form.get("venue_capacity")
	venue_contact = request.form.get("venue_contact")

	if venue_name != '' and venue_location != '':
		Venue.add_venue(venue_name, venue_location, venue_capacity, venue_contact)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/venue_index')
def venue_index():
	venues = Venue.get_venues()
	return render_template('venue_index.html', venues=venues)

@app.route('/add_venue_data')
def add_venue_data():
	return render_template('add_venue.html')

@app.route('/delete_venue/<int:id>')
def delete_venue(id):
	Venue.delete_venue(id)
	return redirect('/')

# -------------------------- ORGS --------------------------------

@app.route('/add_org', methods=["POST"])
def add_org():
	
	org_name = request.form.get("org_name")
	org_desc = request.form.get("org_desc")
	
	if org_name != '':
		Organization.add_org(org_name, org_desc)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/org_index')
def org_index():
	orgs = Organization.get_orgs()
	return render_template('org_index.html', orgs=orgs)

@app.route('/add_org_data')
def add_org_data():
	return render_template('add_org.html')

@app.route('/delete_org/<int:id>')
def delete_org(id):
	Organization.delete_org(id)
	return redirect('/')

# -------------------------- ATTENDEES --------------------------------

@app.route('/add_att', methods=["POST"])
def add_att():
	
	att_name = request.form.get("att_name")
	att_email = request.form.get("att_email")
	att_org_id = request.form.get("att_org_id")
	
	if att_name != '' and att_email != '' and att_org_id != '':
		Attendee.add_att(att_name, att_email, att_org_id)
		return redirect('/')
	else:
		return redirect('/')
	
@app.route('/att_index')
def att_index():
	atts = Attendee.get_atts()
	return render_template('att_index.html', atts=atts)

@app.route('/add_att_data')
def add_att_data():
	return render_template('add_att.html')

@app.route('/delete_att/<int:id>')
def delete_att(id):
	Attendee.delete_att(id)
	return redirect('/')

# -------------------------- BOOKINGS --------------------------------

@app.route('/add_book', methods=["POST"])
def add_book():
	
	book_att_id = request.form.get("book_att_id")
	book_event_id = request.form.get("book_event_id")
	book_venue_id = request.form.get("book_venue_id")
	book_date = request.form.get("book_date")

	if book_att_id != '' and book_event_id != '' and book_venue_id != '' and book_date != '':
		Booking.add_book(book_att_id, book_event_id, book_venue_id, book_date)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/book_index')
def book_index():
	books = Booking.get_books()
	return render_template('book_index.html', books=books)

@app.route('/add_book_data')
def add_book_data():
	return render_template('add_book.html')

@app.route('/delete_book/<int:id>')
def delete_book(id):
	Booking.delete_book(id)
	return redirect('/')

# -------------------------- SPEAKERS --------------------------------

@app.route('/add_speaker', methods=["POST"])
def add_speaker():
	
	speaker_name = request.form.get("speaker_name")
	speaker_bio = request.form.get("speaker_bio")
	speaker_info = request.form.get("speaker_info")

	if speaker_name != '':
		Speaker.add_speaker(speaker_name, speaker_bio, speaker_info)
		return redirect('/')
	else:
		return redirect('/')
	
@app.route('/speaker_index')
def speaker_index():
	speakers = Speaker.get_speakers()
	return render_template('speaker_index.html', speakers=speakers)

@app.route('/add_speaker_data')
def add_speaker_data():
	return render_template('add_speaker.html')

@app.route('/delete_speaker/<int:id>')
def delete_speaker(id):
	Speaker.delete_speaker(id)
	return redirect('/')

# -------------------------- CATERING --------------------------------

@app.route('/add_catering', methods=["POST"])
def add_catering():
	
	catering_business = request.form.get("catering_business")
	catering_type = request.form.get("catering_type")
	catering_event_id = request.form.get("catering_event_id")
	catering_servings = request.form.get("catering_servings")
	catering_time = request.form.get("catering_time")

	if catering_business != '' and catering_event_id != '':
		Catering.add_catering(catering_business, catering_type, catering_event_id, catering_servings, catering_time)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/catering_index')
def catering_index():
	caterings = Catering.get_caterings()
	return render_template('catering_index.html', caterings=caterings)

@app.route('/add_catering_data')
def add_catering_data():
	return render_template('add_catering.html')

@app.route('/delete_catering/<int:id>')
def delete_catering(id):
	Catering.delete_catering(id)
	return redirect('/')

# -------------------------- STATIONS --------------------------------

@app.route('/add_station', methods=["POST"])
def add_station():
	
	station_venue_id = request.form.get("station_venue_id")
	station_speaker_id = request.form.get("station_speaker_id")
	station_topic = request.form.get("station_topic")
	station_capacity = request.form.get("station_capacity")

	if station_venue_id != '' and station_speaker_id != '' and station_topic != '':
		Station.add_station(station_venue_id, station_speaker_id, station_topic, station_capacity)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/station_index')
def station_index():
	stations = Station.get_stations()
	return render_template('station_index.html', stations=stations)

@app.route('/add_station_data')
def add_station_data():
	return render_template('add_station.html')

@app.route('/delete_station/<int:id>')
def delete_station(id):
	Station.delete_station(id)
	return redirect('/')


if __name__=='__main__': 
    app.run(port=8000, debug=True) 
