from sqlalchemy import func
from models.schemas import StationTopic
from core import ma, db

def get_stationtopics(): 
    all_stationtopics = StationTopic.query.all()
    return stationtopics_schema.dump(all_stationtopics)

def add_stationtopic(st_station_id, st_topic):
    a = StationTopic(st_station_id=st_station_id, st_topic=st_topic, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_stationtopic(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = StationTopic.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class StationTopicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StationTopic

stationtopic_schema = StationTopicSchema()
stationtopics_schema = StationTopicSchema(many=True)
