DROP TABLE IF EXISTS Organizations, Business, Attendees, Venues, Events, Speakers, 
	Catering, Stations, StationTopics, BookedEvents, BookedAttendees;

CREATE TABLE Speakers(
ID INT UNSIGNED AUTO_INCREMENT,
Name VARCHAR(50) UNIQUE NOT NULL,
Bio VARCHAR(1000),
ContactInfo VARCHAR(100),
PRIMARY KEY(ID)
);

CREATE TABLE Events(
ID INT UNSIGNED AUTO_INCREMENT,
Title VARCHAR(100) UNIQUE NOT NULL,
DateTime DATETIME UNIQUE,
Description VARCHAR(1000),
PRIMARY KEY(ID)
);

CREATE TABLE Venues(
ID INT UNSIGNED AUTO_INCREMENT,
Name VARCHAR(100) UNIQUE NOT NULL,
Location VARCHAR(50),
Capacity INT UNSIGNED,
ContactInfo VARCHAR(100),
PRIMARY KEY(ID)
);

-- ALTERED
CREATE TABLE Business(
ID INT UNSIGNED AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Bio VARCHAR(500),
ContactInfo VARCHAR(100),
PRIMARY KEY (ID)
);

-- ALTERED 
CREATE TABLE Organizations(
ID INT UNSIGNED AUTO_INCREMENT,
Name VARCHAR(50) UNIQUE NOT NULL,
Description VARCHAR(300),
PRIMARY KEY (ID)
);

-- ALTERED
CREATE TABLE Attendees(
ID INT UNSIGNED AUTO_INCREMENT,
Name VARCHAR(50) UNIQUE NOT NULL,
Email VARCHAR(100),
OrganizationID INT UNSIGNED,
PRIMARY KEY(ID),
FOREIGN KEY (OrganizationID) REFERENCES Organizations(ID)
ON UPDATE CASCADE
ON DELETE SET NULL
);

CREATE TABLE BookedEvents(
ID INT UNSIGNED AUTO_INCREMENT,
EventID INT UNSIGNED,
VenueID INT UNSIGNED,
PRIMARY KEY(ID),
FOREIGN KEY (EventID) REFERENCES Events(ID)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY (VenueID) REFERENCES Venues(ID)
ON UPDATE CASCADE
ON DELETE CASCADE
);

CREATE TABLE BookedAttendees(
ID INT UNSIGNED AUTO_INCREMENT,
EventID INT UNSIGNED,
AttendeeID INT UNSIGNED,
RegistrationDate DATE,
FOREIGN KEY (EventID) REFERENCES Events(ID)
ON UPDATE RESTRICT
ON DELETE CASCADE,
FOREIGN KEY (AttendeeID) REFERENCES Attendees(ID)
ON UPDATE RESTRICT
ON DELETE CASCADE
);

-- ALTERED
CREATE TABLE Catering(
ID INT UNSIGNED AUTO_INCREMENT,
BusinessID INT UNSIGNED DEFAULT 1,
CateringType VARCHAR(50),
FOREIGN KEY (BusinessID) REFERENCES Business(ID)
ON UPDATE CASCADE
ON DELETE SET NULL
);


CREATE TABLE CateringService(
ID INT UNSIGNED AUTO_INCREMENT,
CateringID INT UNSIGNED,
EventID INT UNSIGNED,
Servings INT UNSIGNED,
Time TIME,
PRIMARY KEY (ID),
FOREIGN KEY (EventID) REFERENCES Events(ID)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY (CateringID) REFERENCES Catering(ID)
ON UPDATE CASCADE
ON DELETE CASCADE
);

-- ALTERED
CREATE TABLE Stations(
ID INT UNSIGNED AUTO_INCREMENT,
VenueID INT UNSIGNED,
SpeakerID INT UNSIGNED,
Capacity INT UNSIGNED,
PRIMARY KEY (ID),
FOREIGN KEY (VenueID) REFERENCES Venues(ID)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY (SpeakerID) REFERENCES Speakers(ID)
ON UPDATE CASCADE
ON DELETE CASCADE
);

-- ALTERED
CREATE TABLE StationTopics(
ID INT UNSIGNED AUTO_INCREMENT,
StationID INT UNSIGNED,
Topic VARCHAR(100) NOT NULL,
PRIMARY KEY (ID),
FOREIGN KEY (StationID) REFERENCES Stations(ID)
ON UPDATE CASCADE
ON DELETE SET NULL
);
