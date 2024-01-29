CREATE TABLE Speakers (
SpeakerName VARCHAR(50),
Bio VARCHAR(1000),
ContactInfo VARCHAR(100)
);

CREATE TABLE Events (
Title VARCHAR(100),
DateAndTime DATETIME,
Description VARCHAR(1000)
);

CREATE TABLE Venues (
VenueName VARCHAR(100),
Location VARCHAR(50),
Capacity INT UNSIGNED,
ContactInfo VARCHAR(100)
);

CREATE TABLE Attendees (
AttendeeName VARCHAR(50),
Email VARCHAR(100),
RegistrationDate DATE,
EventAttended VARCHAR(100)
);