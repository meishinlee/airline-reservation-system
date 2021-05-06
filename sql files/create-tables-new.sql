CREATE TABLE IF NOT EXISTS Airline(
    AirlineName varchar(50),
    PRIMARY KEY (AirlineName)
    );

CREATE TABLE IF NOT EXISTS Airplane(
    AirlineName varchar(50) NOT NULL, 
    AirplaneID int(10) NOT NULL, 
    NumberOfSeats int(5) NOT NULL,
    PRIMARY KEY (AirlineName, AirplaneID)
    );

CREATE TABLE IF NOT EXISTS Flight(
    AirlineName varchar(50) NOT NULL, ###
    DepartureDate date NOT NULL, 
    DepartureTime time NOT NULL, 
    FlightNumber int(5) NOT NULL,
    DepartureAirport varchar(50) NOT NULL,
    ArrivalAirport varchar(50) NOT NULL, 
    ArrivalDate date NOT NULL, #need for ticket info
    ArrivalTime time NOT NULL, 
    BasePrice float(6,2) NOT NULL, 
    AirplaneID int(10) NOT NULL, ###
    PRIMARY KEY (FlightNumber, DepartureDate, DepartureTime),
    FOREIGN KEY (AirlineName) REFERENCES Airline(AirlineName)
	ON DELETE CASCADE
	ON UPDATE CASCADE
    #FOREIGN KEY (AirplaneID) REFERENCES Airplane(AirplaneID)
    #ON DELETE CASCADE
	#ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Airport(
    AirportName varchar(50), 
    AirportCity varchar(50) NOT NULL,
    PRIMARY KEY (AirportName)
    );

CREATE TABLE IF NOT EXISTS Arrives(
    #by default pk, all attributes are NOT NULL
    AirportName varchar(50), 
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time,
    PRIMARY KEY (AirportName, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (AirportName) REFERENCES Airport(AirportName)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (FlightNumber, DepartureDate, DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Departs(
    #by default pk, all attributes are NOT NULL
    AirportName varchar(50), 
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time, 
    PRIMARY KEY (AirportName, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (AirportName) REFERENCES Airport(AirportName) 
    ON DELETE CASCADE
    ON UPDATE CASCADE, 
    FOREIGN KEY (FlightNumber, DepartureDate, DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    ); 

CREATE TABLE IF NOT EXISTS AirlineStaff(
    Username varchar(50), 
    StaffPassword varchar(50) NOT NULL,
    Firstname varchar(50) NOT NULL, 
    Lastname varchar(50) NOT NULL, 
    DateOfBirth date NOT NULL, 
    AirlineName varchar(50) NOT NULL, ###
    PRIMARY KEY (Username), 
    FOREIGN KEY (AirlineName) REFERENCES Airline(AirlineName)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS PhoneNumber(
    Username varchar(50), 
    AirlineStaffPhoneNumber int(10) NOT NULL, 
    PRIMARY KEY (Username, AirlineStaffPhoneNumber), 
    FOREIGN KEY (Username) REFERENCES AirlineStaff(Username)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Updates(
    Username varchar(50), 
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time, 
    FlightStatus varchar(20) NOT NULL, 
    PRIMARY KEY (Username, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (Username) REFERENCES AirlineStaff(Username) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE, 
    FOREIGN KEY (FlightNumber, DepartureDate, DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS Customer(
    CustomerName varchar(50) NOT NULL, 
    CustomerEmail varchar(50),
    CustomerPassword varchar(50) NOT NULL, 
    BuildingNumber int(3) NOT NULL, 
    Street varchar(50) NOT NULL, 
    City varchar(50) NOT NULL, 
    State varchar(50) NOT NULL, 
    CustomerPhoneNumber varchar(10) NOT NULL,
    PassportNumber varchar(8) NOT NULL, 
    PassportExpiration date NOT NULL, 
    PassportCountry varchar(50) NOT NULL, 
    DateOfBirth date NOT NULL, 
    PRIMARY KEY (CustomerEmail)
    );

CREATE TABLE IF NOT EXISTS Suggested(
    CustomerEmail varchar(50),
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time, 
    CustomerComment text, #can rate w/o comment 
    Rate float(2,1) NOT NULL, 
    PRIMARY KEY (CustomerEmail, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (CustomerEmail) REFERENCES Customer(CustomerEmail) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE, 
    FOREIGN KEY (FlightNumber, DepartureDate, DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS Updates(
    Username varchar(50), 
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time, 
    FlightStatus varchar(20) NOT NULL, 
    PRIMARY KEY (Username, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (Username) REFERENCES AirlineStaff(Username) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE, 
    FOREIGN KEY (FlightNumber, DepartureDate, DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS BookingAgent(
    AgentEmail varchar(50), 
    AgentPassword varchar(50) NOT NULL,
    AgentID varchar(20) NOT NULL, 
    PRIMARY KEY (AgentEmail)
    );

CREATE TABLE IF NOT EXISTS Ticket(
    TicketID varchar(50), 
    CustomerEmail varchar(50) NOT NULL, 
    AirlineName varchar(50) NOT NULL, 
    FlightNumber int(5) NOT NULL, 
    SoldPrice float(6, 2) NOT NULL, 
    PuchaseDate date NOT NULL, 
    PurchasedTime time NOT NULL, 
    AgentID varchar(20), 
    PRIMARY KEY (TicketID), 
    FOREIGN KEY (CustomerEmail) REFERENCES Customer(CustomerEmail)
    ON UPDATE CASCADE 
    ON DELETE CASCADE,
    FOREIGN KEY (AirlineName) REFERENCES Airline(AirlineName)
    ON UPDATE CASCADE 
    ON DELETE CASCADE, 
    FOREIGN KEY (FlightNumber) REFERENCES Flight(FlightNumber)
    ON UPDATE CASCADE 
    ON DELETE CASCADE 
    #FOREIGN KEY (AgentID) REFERENCES BookingAgent(AgentID)
    ); 

CREATE TABLE IF NOT EXISTS PurchasedFor(
    TicketID varchar(50), 
    FlightNumber int(5), 
    DepartureDate date, 
    DepartureTime time, 
    PRIMARY KEY (TicketID, FlightNumber, DepartureDate, DepartureTime), 
    FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID)
    ON UPDATE CASCADE
    ON DELETE CASCADE, 
    FOREIGN KEY (FlightNumber, DepartureDate,DepartureTime) REFERENCES Flight(FlightNumber, DepartureDate, DepartureTime)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS Creates(
    AgentEmail varchar(50), 
    TicketID varchar(50), 
    CommissionAmount float(6,2), 
    PRIMARY KEY (AgentEmail, TicketID), 
    FOREIGN KEY (AgentEmail) REFERENCES BookingAgent(AgentEmail)
    ON UPDATE CASCADE 
    ON DELETE CASCADE, 
    FOREIGN KEY (TicketID) REFERENCES Ticket(TicketID)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
    ); 

CREATE TABLE IF NOT EXISTS CardInfo(
    CardNumber int(10), 
    CardType varchar(6) NOT NULL, 
    CardName varchar(50) NOT NULL, 
    ExpirationDate date NOT NULL, 
    PRIMARY KEY (CardNumber)
    );

CREATE TABLE IF NOT EXISTS ProvidesPersonalInfo(
    CardNumber int(10),
    CustomerEmail varchar(50), 
    PRIMARY KEY (CardNumber, CustomerEmail), 
    FOREIGN KEY (CardNumber) REFERENCES CardInfo(CardNumber)
    ON UPDATE CASCADE
    ON DELETE CASCADE, 
    FOREIGN KEY (CustomerEmail) REFERENCES Customer(CustomerEmail)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS PaymentMethod(
    CardNumber int(10), 
    TicketID varchar(50),
    PRIMARY KEY (CardNumber, TicketID),
    FOREIGN KEY (CardNumber) REFERENCES cardinfo(CardNumber)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (TicketID) REFERENCES ticket(TicketID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );


