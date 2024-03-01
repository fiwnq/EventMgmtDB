-- 1. How many events have used the venue with ID 1?
SELECT COUNT(*) FROM BookedVenues
WHERE VenueID = 1;
-- 2. How many people from organization ID 2 went to event ID 1?
SELECT COUNT(*) FROM BookedAttendees, 
WHERE 
-- 3. What is the average amount of stations that an event has?