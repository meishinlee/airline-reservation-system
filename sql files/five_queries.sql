#Mei Shin Lee, Ruhejami Mustari
#a
SELECT FlightNumber, AirlineName, AirplaneID, DepartureDate, DepartureTime 
FROM Flight 
WHERE CURRENT_DATE < DepartureDate OR (CURRENT_DATE = DepartureDate AND CURRENT_TIME < DepartureTime);

#b 
SELECT FlightNumber, AirlineName, AirplaneID, DepartureDate, DepartureTime
FROM updates
NATURAL JOIN Flight 
WHERE FlightStatus = 'Delayed';

#c
#two diff customers may have the same name
SELECT CustomerName 
FROM Customer AS c
INNER JOIN ticket AS t
ON c.CustomerEmail = t.CustomerEmail
WHERE t.AgentID IS NULL;

#d
#two diff customers may have the same name
SELECT CustomerName 
FROM Customer AS c
INNER JOIN ticket AS t
ON c.CustomerEmail = t.CustomerEmail
WHERE t.AgentID IS NOT NULL;

#e
SELECT AirplaneID
FROM Airplane
WHERE AirlineName = 'China Eastern';
