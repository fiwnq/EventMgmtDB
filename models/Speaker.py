from sqlalchemy import func
from models.schemas import Speakers
from core import ma, db

def get_speakers(): 
    all_speakers = Speakers.query.all()
    return speakers_schema.dump(all_speakers)

def add_speaker(speaker_name, speaker_bio, speaker_info):
    a = Speakers(speaker_name = speaker_name, speaker_bio=speaker_bio, speaker_info = speaker_info)
    db.session.add(a)
    db.session.commit()

def delete_speaker(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Speakers.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class SpeakerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Speakers

speaker_schema = SpeakerSchema()
speakers_schema = SpeakerSchema(many=True)
