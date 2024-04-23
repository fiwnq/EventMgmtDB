INSERT INTO Events (event_name, event_datetime, event_desc)
VALUES ('Lipscomb TED Talks', '2024-02-13 12:30:00', 'Ted Talk Event'),
	('Importance of Motivational Quotes', '2024-07-07 13:00:00', 'A comprehensive talk from a life coach on his experience with motivational quotes affecting both his life and the lives of many others.'),
	('Cybersecurity Showcase', '2024-11-27 15:00:00', 'A knowledgeable IT professor will showcase popular hacking attack and how you can be safe on the internet.');

INSERT INTO Speakers(speaker_name, speaker_bio, speaker_info)
VALUES ('Kevin Hart', 'Comedian', 'email:kevinhart123@gmail.com'),
	('Christina Wallace','Writer and entrprenuer', 'email:cwallace345@gmail.com'),
    ('Steve Nordstorm', 'Cybersecurity Professional' , 'email:snordy01@gmail.com'),
    ('Stacey Abrams', 'Politician', 'imsostacy@gmail.com');

INSERT INTO Venues(venue_name, venue_location, venue_capacity, venue_contact)
VALUES ('Shinn Center', 'Lipscomb University', 600, 'email: lippy@gmail.com phone: 459394030'),
	('Swang Business Center','Lipscomb University', 200,'email: swangy@gmail.com phone: 39402034593'),
    ('Field Engineering Building','Lipscomb University', 100, 'email: fieldy@gmail.com phone: 39483840930');

INSERT INTO Organizations(org_name, org_desc) 
VALUES ('Student Activities Board', 'Organization on Lipscomb Universitys Campus.'),
	('Society of Women Engineers','Promotes women in the engineering field.'),
    ('Association of Computing Machinery', '...'),
    ('American Red Cross', '...'),
    ('Humane Society of the United States', '...');

INSERT INTO Attendees(att_name, att_email, att_org_id)
VALUES ('Lindsey Born', 'lborn@gmail.com', 2 ),
	('Ben Turner', 'imturner@gmail.com', 1 ),
    ('Fernandez Mario', 'Fernny@gmail.com', 1);

INSERT INTO Stations(station_venue_id, station_speaker_id, station_topic, station_capacity)
VALUES(1, 1, 'Sports', 200),
	 (1, 2, 'Motivational Words', 200),
	 (1, 3, 'Lipscomb Mission Trips', 200);

INSERT INTO Catering(catering_business, catering_type, catering_event_id, catering_servings, catering_time)
VALUES ( 'Canes', 'Lunch', 1, 150, '12:00'),
	('Dumpling House', 'Lunch', 2, 100, '12:00'),
	('Taco Mama', 'Dinner', 3, 100, '5:30');
    
INSERT INTO Bookings(book_att_id, book_event_id, book_venue_id, book_date)
VALUES (1, 2, 1, '2024-02-03'), 
	(2, 2, 1, '2024-02-20'), 
	(3, 1, 1, '2024-01-03');
