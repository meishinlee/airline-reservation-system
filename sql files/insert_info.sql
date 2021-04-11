#Insert Airline 
INSERT INTO Airline VALUES ("China Eastern"); 

#Insert 2 Airports
INSERT INTO Airport VALUES ('JFK','NYC'); 
INSERT INTO Airport VALUES ('PVG','Shanghai'); 

#Insert 2 Customers
INSERT INTO Customer VALUES ('Mei','msl608@nyu.edu','mei', 370, 'Jay', 'NYC', 'NY', 1193283722, '12345678', '2021-12-17', 'USA', '2000-12-15');
INSERT INTO Customer VALUES ('Ruhejami','rm4966@nyu.edu','ruhejami', 370, 'Jay', 'NYC', 'NY', 1234567890, '09876543', '2024-01-17', 'USA', '2000-12-29'); 

#Insert 1 BookingAgent
INSERT INTO BookingAgent VALUES ('bookingAgent@airline.com','agent1','agent1'); 

#Insert 2 Airplanes
INSERT INTO Airplane VALUES ('China Eastern', 001, 100);
INSERT INTO Airplane VALUES ('China Eastern', 002, 200);
#INSERT INTO Airplane VALUES ('China Eastern', 003, 200); Taken out of DB

#Insert 1 AirlineStaff for CE
INSERT INTO AirlineStaff VALUES ('CEairlineStaff1','CEAirlineStaff1','Bob','Smith','1995-02-24','China Eastern');

#Insering Flights (3)
INSERT INTO Flight VALUES ('China Eastern', '2021-03-28', '12:30', 001, 'PVG', 'JFK', '2021-03-29', '14:30', 700.20, 001); 
INSERT INTO Flight VALUES ('China Eastern', '2021-02-13', '10:00', 002, 'JFK', 'PVG', '2021-02-14', '16:39', 500.23, 002); 
INSERT INTO Flight VALUES ('China Eastern', '2022-01-11', '20:00', 003, 'PVG', 'JFK', '2022-02-14', '13:40', 670.90, 002); 

#Adding 2 Airline Staff and Phone Numbers 
INSERT INTO AirlineStaff VALUES ('ChinaEasternStaff1', 'ChinaEasternStaff1', 'Mary', 'Smith', '1995-03-05', 'China Eastern'); 
INSERT INTO PhoneNumber VALUES ('ChinaEasternStaff1', 1111111111); 
INSERT INTO PhoneNumber VALUES ('ChinaEasternStaff1', 1111111110); 
INSERT INTO AirlineStaff VALUES ('ChinaEasternStaff2', 'ChinaEasternStaff2', 'Amy', 'Jones', '1984-05-07', 'China Eastern');
INSERT INTO PhoneNumber VALUES ('ChinaEasternStaff2', 2222222222); 

#Inserting Statuses for Flights
INSERT INTO Updates VALUES ('ChinaEasternStaff1', 001,'2021-03-28', '12:30', 'Delayed'); 
INSERT INTO Updates VALUES ('ChinaEasternStaff2', 002,'2021-02-13', '10:00', 'On Time'); 
INSERT INTO Updates VALUES ('ChinaEasternStaff2', 003, '2022-01-11', '20:00', 'Delayed'); 

#Inserting Tickets 
INSERT INTO Ticket VALUES('1', 'msl608@nyu.edu', 'China Eastern', 001, 110.20, '2021-03-20', '10:24', NULL); 
INSERT INTO Ticket VALUES('2', 'msl608@nyu.edu', 'China Eastern', 002, 450.00, '2021-01-30', '11:14', 'agent1'); 
INSERT INTO Ticket VALUES('3', 'rm4966@nyu.edu', 'China Eastern', 002, 900.00, '2021-02-10', '06:54', 'agent1'); 

#Purchase Records 
INSERT INTO PurchasedFor VALUES ('2', 002, '2021-02-13', '10:00'); 
INSERT INTO PurchasedFor VALUES ('3', 002, '2021-02-13', '10:00'); 

#To complement Purchase Records‘
INSERT INTO creates VALUES ('bookingAgent@airline.com',002,10);
INSERT INTO creates VALUES ('bookingAgent@airline.com',003,20);
INSERT INTO cardInfo VALUES ( 1111111111, 'Credit','Mei', '2022-06-24'); 
INSERT INTO cardinfo VALUES ( 1234567890,'Debit', 'Ruhejami', '2024-11-12');
INSERT INTO providespersonalinfo VALUES (1111111111, 'msl608@nyu.edu'); 
INSERT INTO providespersonalinfo VALUES (1234567890,'rm4966@nyu.edu');
INSERT INTO paymentmethod VALUES (1111111111, 1); 
INSERT INTO paymentmethod VALUES (1111111111, 2); 
INSERT INTO paymentmethod VALUES (1234567890, 3); 
