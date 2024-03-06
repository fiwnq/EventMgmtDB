-- Select Statements
-- 1. How many events have used the venue with ID 1?
SELECT COUNT(*) FROM BookedVenues
WHERE VenueID = 1;

-- 2. How many people from organization ID 2 went to event ID 1?
SELECT COUNT(*) AS AttendeeCount
FROM Attendees a
JOIN BookedAttendees ba ON a.ID = ba.AttendeeID
JOIN Events e ON ba.EventID = e.ID
WHERE a.OrganizationID = 2 AND e.ID = 1;

-- 3. What is the average amount of stations that an event has?
SELECT AVG(StationCount) AS AverageStations
FROM (
    SELECT COUNT(*) AS StationCount
    FROM Stations
    GROUP BY VenueID
) AS StationCounts;

-- 4. How many times has a business catered to an event?
SELECT b.Name AS BusinessName, COUNT(*) AS CateringCount
FROM Business b
JOIN Catering c ON b.ID = c.BusinessID
JOIN CateringService cs ON c.ID = cs.CateringID
GROUP BY b.Name;
