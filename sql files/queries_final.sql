#Customer View One Way Flights (for search)

SELECT f.AirlineName, f.FlightNumber, f.DepartureDate, f.DepartureTime, ArrivalDate, FlightStatus, COUNT(ticketID) as booked, numberOfSeats 
FROM flight as f 
LEFT JOIN purchasedfor AS p 
ON p.FlightNumber = f.FlightNumber AND p.DepartureDate = f.DepartureDate AND p.DepartureTime = f.DepartureTime 
INNER JOIN updates AS u 
ON u.FlightNumber = f.FlightNumber AND u.DepartureDate = f.DepartureDate AND u.DepartureTime = f.DepartureTime 
INNER JOIN airplane 
ON f.AirplaneID = airplane.AirplaneID 
INNER JOIN airport AS a1 
ON a1.AirportName = f.DepartureAirport 
INNER JOIN airport AS a2 
ON a2.AirportName = f.ArrivalAirport 
WHERE f.FlightNumber NOT IN 
    (SELECT FlightNumber 
    FROM flight as f2 
    GROUP BY FlightNumber 
    HAVING COUNT(f2.FlightNumber) > 1) 
AND a1.AirportCity = 'Shanghai' AND f.DepartureAirport = 'PVG' AND a2.AirportCity = 'NYC' AND f.ArrivalAirport = 'JFK' AND f.DepartureDate = '2021-03-28' 
GROUP BY f.AirlineName, f.FlightNumber, f.DepartureDate, f.DepartureTime, ArrivalDate, FlightStatus 
HAVING booked < NumberOfSeats

#for purchasing tickets 
SELECT f.AirlineName, f.FlightNumber, f.DepartureDate, f.DepartureTime, f.BasePrice, COUNT(ticketID) as booked, numberOfSeats FROM flight as f LEFT JOIN purchasedfor AS p ON p.FlightNumber = f.FlightNumber AND p.DepartureDate = f.DepartureDate AND p.DepartureTime = f.DepartureTime INNER JOIN updates AS u ON u.FlightNumber = f.FlightNumber AND u.DepartureDate = f.DepartureDate AND u.DepartureTime = f.DepartureTime INNER JOIN airplane ON f.AirplaneID = airplane.AirplaneID INNER JOIN airport AS a1 ON a1.AirportName = f.DepartureAirport INNER JOIN airport AS a2 ON a2.AirportName = f.ArrivalAirport WHERE f.FlightNumber NOT IN (SELECT FlightNumber from flight as f2 GROUP BY FlightNumber HAVING COUNT(f2.FlightNumber) > 1) AND f.DepartureDate = '2021-03-28' AND f.DepartureTime = '12:30:00' AND f.FlightNumber = 1 GROUP BY f.AirlineName, f.FlightNumber, f.DepartureDate, f.DepartureTime, ArrivalDate, FlightStatus HAVING booked < NumberOfSeats