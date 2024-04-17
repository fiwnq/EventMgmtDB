DROP TABLE IF EXISTS Organizations, Attendees, Venues, Events, Speakers, 
	Catering, Stations, Bookings;

CREATE TABLE Speakers(
speaker_id INT UNSIGNED AUTO_INCREMENT,
speaker_name VARCHAR(50) UNIQUE NOT NULL,
speaker_bio VARCHAR(1000),
speaker_info VARCHAR(100),
PRIMARY KEY(speaker_id)
);

CREATE TABLE Events(
event_id INT UNSIGNED AUTO_INCREMENT,
event_name VARCHAR(100) UNIQUE NOT NULL,
event_datetime DATETIME UNIQUE,
event_desc VARCHAR(1000),
PRIMARY KEY(event_id)
);

CREATE TABLE Venues(
venue_id INT UNSIGNED AUTO_INCREMENT,
venue_name VARCHAR(100) UNIQUE NOT NULL,
venue_location VARCHAR(50) NOT NULL,
venue_capacity INT UNSIGNED,
venue_contact VARCHAR(100),
PRIMARY KEY(venue_id)
);

CREATE TABLE Organizations(
org_id INT UNSIGNED AUTO_INCREMENT,
org_name VARCHAR(50) UNIQUE NOT NULL,
org_desc VARCHAR(300),
PRIMARY KEY (org_id)
);

CREATE TABLE Attendees(
att_id INT UNSIGNED AUTO_INCREMENT,
att_name VARCHAR(50) UNIQUE NOT NULL,
att_email VARCHAR(100),
att_org_id INT UNSIGNED,
PRIMARY KEY(att_id),
FOREIGN KEY (att_org_id) REFERENCES Organizations(org_id)
ON UPDATE CASCADE
ON DELETE SET NULL
);

CREATE TABLE Bookings(
book_id INT UNSIGNED AUTO_INCREMENT,
book_att_id INT UNSIGNED NOT NULL,
book_event_id INT UNSIGNED NOT NULL,
book_venue_id INT UNSIGNED NOT NULL,
book_date DATE NOT NULL,
PRIMARY KEY(book_id),
FOREIGN KEY (book_att_id) REFERENCES Attendees(att_id)
ON UPDATE RESTRICT
ON DELETE CASCADE,
FOREIGN KEY (book_event_id) REFERENCES Events(event_id)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY (book_venue_id) REFERENCES Venues(venue_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);

CREATE TABLE Catering(
catering_id INT UNSIGNED AUTO_INCREMENT,
catering_business VARCHAR(100) UNIQUE,
catering_type VARCHAR(50),
catering_event_id INT UNSIGNED NOT NULL,
catering_servings INT UNSIGNED,
catering_time TIME,
PRIMARY KEY (catering_id),
FOREIGN KEY (catering_event_id) REFERENCES Events(event_id)
ON UPDATE CASCADE
ON DELETE CASCADE,
);

CREATE TABLE Stations(
station_id INT UNSIGNED AUTO_INCREMENT,
station_venue_id INT UNSIGNED NOT NULL,
station_speaker_id INT UNSIGNED NOT NULL,
station_topic VARCHAR(100) UNIQUE NOT NULL,
station_capacity INT UNSIGNED,
PRIMARY KEY (station_id),
FOREIGN KEY (station_venue_id) REFERENCES Venues(venue_id)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY (station_speaker_id) REFERENCES Speakers(speaker_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);