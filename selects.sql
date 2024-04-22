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
SELECT AVG(StationCount) AS AverageStations
FROM (
	SELECT COUNT(*) AS StationCount
	FROM Stations
    GROUP BY station_venue_id
) AS StationCounts;

-- 4. How many events use catering?
SELECT COUNT(*) AS Total
FROM Events
JOIN Catering ON Events.event_id = Catering.catering_event_id;

-- 5. How many events were made in the year 2024?
SELECT COUNT(*) AS EventCount
FROM Events
WHERE Events.event_datetime > '2023-12-31' AND Events.event_datetime < '2025-01-01';


