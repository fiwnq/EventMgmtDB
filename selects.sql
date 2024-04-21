-- Select Statements
-- 1. How many events have used the venue with ID 1?
SELECT COUNT(*) FROM Bookings
WHERE Bookings.book_venue_id = 1;

-- 2. How many people from organization ID 2 went to event ID 1?
SELECT COUNT(*) AS AttendeeCount
FROM Attendees a
JOIN Bookings b ON a.att_id = b.book_att_id
JOIN Events e ON b.book_event_id = e.event_id
WHERE a.att_org_id = 2 AND e.event_id = 1;

-- 3. What is the average amount of stations that an event has?
-- SELECT AVG(StationCount) AS AverageStations
-- FROM (
--     SELECT COUNT(*) AS StationCount
--     FROM Stations
--     GROUP BY VenueID
-- ) AS StationCounts;

-- 4. How many times has a business catered to an event?
-- SELECT b.Name AS BusinessName, COUNT(*) AS CateringCount
-- FROM Business b
-- JOIN Catering c ON b.ID = c.BusinessID
-- JOIN CateringService cs ON c.ID = cs.CateringID
-- GROUP BY b.Name;
