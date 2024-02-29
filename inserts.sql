INSERT INTO Events (Title, DateTime, Description)
VALUES ('Lipscomb TED Talks', '2024-02-13', 'Ted Talk Event'),
	('Importance of Motivational Quotes', '2024-07-07', 'A comprehensive talk from a life coach on his experience with motivational quotes affecting both his life and the lives of many others.'),
	('Cybersecurity Showcase', '2024-11-27', 'A knowledgeable IT professor will showcase popular hacking attack and how you can be safe on the internet.');

INSERT INTO Speakers(Name, Bio, ContactInfo)
VALUES ('Kevin Hart', 'Comedian', 'email:kevinhart123@gmail.com phone: 345237654'),
	('Christina Wallace','Writer and entrprenuer', 'email:cwallace345@gmail.com phone: 49503958309'),
    ('Steve Nordstorm', 'Cybersecurity Professional' , 'email:snordy01@gmail.com phone:4569392049');

INSERT INTO Venues(Name, Location, Capacity, ContactInfo)
VALUES ('Shinn Center', 'Lipscomb University', 600, 'email: lippy@gmail.com phone: 459394030'),
	('Swang Business Center','Lipscomb University', 200,'email: swangy@gmail.com phone: 39402034593'),
    ('Field Engineering Building','Lipscomb University', 100, 'email: fieldy@gmail.com phone: 39483840930');

INSERT INTO Business(Name, Bio, ContactInfo)
VALUES ('Chickfila', 'fast food restaurant', 'email: chickyfila@gmail.com'),
	('Fruitsies and Snacksies','Small snack catering',' phone: 3459238457'),
	('Canes','fast food restaurant','email: canie@gmail.com');

INSERT INTO Organizations(Name, Description) 
VALUES ('Student Activities Board', 'Organization on Lipscomb Universitys Campus.'),
	('Society of Women Engineers','Promotes women in the engineering field.');

INSERT INTO Attendees(Name, Email, OrganizationID)
VALUES ('Lindsey Born', 'lborn@gmail.com', 2 ),
	('Ben Turner', 'imturner@gmail.com', 1 ),
    ('Fernandez Mario', 'Fernny@gmail.com', 1);

INSERT INTO Stations(VenueID, SpeakerID, Capacity)
VALUES(1, 1, 200), (1, 2, 200), (1, 3, 200);

INSERT INTO StationTopics(StationID, Topic)
VALUES (1, 'Lifestyles'),
	(1, 'How to create your own small business'),
	(1, 'memory-safe programming languages');

INSERT INTO Catering(BusinessID, EventID, Servings)
VALUES (1, 1, 300),
	(2, 3, 130),
	(3, 1, 400);
    
INSERT INTO BookedEvents(EventID, VenueID)
VALUES (1, 2),
	(2, 2),
    (3, 1);

INSERT INTO BookedAttendees(EventID, AttendeeID, RegistrationDate)
VALUES (1, 1, '2023-12-25'),
	(1, 2, '2024-01-15'),
    (1, 3, '2024-02-01');