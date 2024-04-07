from sqlalchemy import func
from models.schemas import Speaker
from core import ma, db

def get_speakers(): 
    all_speakers = Speaker.query.all()
    return speakers_schema.dump(all_speakers)

def add_speaker(first_name, last_name):
    a = Speaker(first_name=first_name, last_name=last_name, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_speaker(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Speaker.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class SpeakerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Speaker

speaker_schema = SpeakerSchema()
speakers_schema = SpeakerSchema(many=True)
