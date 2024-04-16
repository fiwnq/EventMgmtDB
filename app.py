from core import app
from flask import redirect, request 
from flask.templating import render_template
from models import Actor, Attendee, BookedAttendee, BookedEvent, Business, Catering, CateringService, Event, Organization, Speaker, Station, StationTopic, Venue

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



if __name__=='__main__': 
    app.run(port=8000, debug=True) 


