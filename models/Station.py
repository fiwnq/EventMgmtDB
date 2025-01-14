from sqlalchemy import func
from models.schemas import Stations
from core import ma, db

def get_stations(): 
    all_stations = Stations.query.all()
    return stations_schema.dump(all_stations)

def add_station(station_venue_id, station_speaker_id, station_topic, station_capacity):
    a = Stations(station_venue_id=station_venue_id, station_speaker_id=station_speaker_id, station_topic=station_topic, station_capacity=station_capacity)
    db.session.add(a)
    db.session.commit()

def delete_station(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Stations.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class StationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stations
        include_fk = True

station_schema = StationSchema()
stations_schema = StationSchema(many=True)
