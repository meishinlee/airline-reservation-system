#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from datetime import datetime
from datetime import date
import hashlib

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='air ticket reservation system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
	return render_template('index.html')

#Define route for customer login
@app.route('/Customer-Login')
def customerLogin():
	return render_template('Customer-Login.html')

#Define route for register
@app.route('/Customer-Registration')
def customer_register():
	return render_template('Customer-Registration.html')

#Authenticates the register
@app.route('/customerRegisterAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
	name = request.form['name']
	phone = request.form['phone']
	email = request.form['email']
	password = request.form['password']
	buildingNumber = request.form['building-number']
	street = request.form['street']
	city = request.form['city']
	state = request.form['state']
	passportNumber = request.form['passport-number']
	passportExp = request.form['passport-expiration']
	passportCountry = request.form['passport-country']
	dateOfBirth = request.form['date-of-birth']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	noDupEmailQuery = 'SELECT CustomerEmail FROM customer WHERE CustomerEmail = %s'
	cursor.execute(noDupEmailQuery, (email))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		print('here')
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('Customer-Registration.html', error = error)
	else:
		#password = hashlib.md5(password.encode())
		ins = 'INSERT INTO customer VALUES(%s, %s, md5(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (name, email, password, int(buildingNumber), street, city, state, int(phone), passportNumber,passportExp, passportCountry, dateOfBirth))
		conn.commit()
		cursor.close()
		return render_template('index.html')


def isSessionLoggedIn(): 
	if len(session) > 0: 
		print(session)
		return True 
	return False

#Authenticates the login
@app.route('/CustomerLoginAuth', methods=['GET', 'POST'])
def customerLoginAuth():
	#grabs information from the forms
	username = request.form['customer-username']
	password = request.form['customer-password']
	#username, password = get_cust_credentials()
	#print(username)
	#print(password)
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT CustomerName, CustomerEmail, CustomerPassword FROM customer WHERE CustomerEmail = %s and CustomerPassword = md5(%s)'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	
	sessionRunning = isSessionLoggedIn()
	if (sessionRunning == True): 
		error = 'Other users signed in. Please sign out of current session.'
		return render_template('Customer-Login.html', error=error)
	
	if(data):
		#print('data found')
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return render_template('Customer-Home.html', name = username)
	else:
		#print("here")
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Customer-Login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('username')
	print(session)
	return redirect('/')
	#return render_template('index.html')

@app.route('/Customer-Home')
def customerHome(): 
	return render_template('Customer-Home.html', name = session['username'])

@app.route('/View-Customer-Flights') #needs a query for this!!
def viewCustomerFlights():
	username = session['username']
	cursor = conn.cursor()
	query = 'SELECT AirlineName, FlightNumber, DepartureDate, DepartureTime, ArrivalDate, ArrivalTime, FlightStatus FROM Flight NATURAL JOIN updates NATURAL JOIN purchasedfor NATURAL JOIN ticket NATURAL JOIN customer WHERE CustomerEmail = %s ORDER BY DepartureDate LIMIT 5'
	cursor.execute(query, (username))
	data1 = cursor.fetchall() 
	for each in data1:
		print(each['AirlineName'])
		cursor.close()
	return render_template('View-Customer-Flights.html', custFlights=data1)

@app.route('/Customer-Search-Flights') #needs a query for this!! 
def searchCustomerFlights(): 
	return render_template('Customer-Search-Flights.html')

@app.route('/Rate-my-Flights')
def rateCustomerFlights(): 
	return render_template('Rate-my-Flights.html')

@app.route('/RateFlightAuth', methods=['GET', 'POST'])
def rateFlightAuth(): 
	customerEmail = session['username']
	custTicketID = request.form['ticket-number']
	custRate = request.form['rate']
	custComment = request.form['comment']
	cursor = conn.cursor(); 
	checkCustFlightExist = 'SELECT FlightNumber, DepartureDate, DepartureTime FROM ticket NATURAL JOIN purchasedfor NATURAL JOIN customer WHERE CustomerEmail = %s AND TicketID = %s AND (CURRENT_DATE < DepartureDate OR (CURRENT_DATE = DepartureDate AND CURRENT_TIME < DepartureTime))'
	cursor.execute(checkCustFlightExist,(customerEmail, custTicketID))
	data1 = cursor.fetchone()
	checkNoRate = 'SELECT FlightNumber, DepartureDate, DepartureTime, TicketID FROM suggested NATURAL JOIN ticket WHERE CustomerEmail = %s AND TicketID = %s'
	cursor.execute(checkNoRate, (customerEmail, custTicketID))
	data2 = cursor.fetchone()
	print(data2)
	if(data1 and not(data2)): #customer was on the flight and there was no rating written 
		custFlightNum = data1['FlightNumber']
		custDeptDate = data1['DepartureDate']
		custDeptTime = data1['DepartureTime']
		ins = 'INSERT INTO suggested VALUES(%s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (customerEmail, custFlightNum, custDeptDate, custDeptTime, custComment, custRate))
		conn.commit()
		cursor.close()
		message = "Submitted Successfully! Click the back button to go home!"
		return render_template('Rate-my-Flights.html', message = message)
	elif (data2): 
		error = "Flight already given a rating"
		return render_template('Rate-my-Flights.html', error=error)
	else: 
		error = "Ticket ID does not exist"
		return render_template('Rate-my-Flights.html', error=error)
	

@app.route('/View-Flights')
def viewFlightsPublic():
    #username = session['username']
    cursor = conn.cursor();
    query = 'SELECT AirlineName, FlightNumber, DepartureDate, ArrivalDate, FlightStatus FROM Flight AS f NATURAL JOIN updates ORDER BY DepartureDate LIMIT 10'
    cursor.execute(query)
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['AirlineName'])
    cursor.close()
    return render_template('View-Flights.html', flights=data1)

@app.route('/Search-Flights')
def searchFlights():
	return render_template('Search-Flights.html')

#Define route for booking agent login
@app.route('/Booking-Agent-Login')
def bookingAgentlogin():
	return render_template('Booking-Agent-Login.html')

@app.route('/BookingAgentLoginAuth', methods=['GET', 'POST'])
def bookingAgentLoginAuth():
	#grabs information from the forms
	username = request.form['agent-email-login']
	password = request.form['agent-password']
	agent_id = request.form['agent-id']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT AgentEmail, AgentPassword, AgentID FROM bookingagent WHERE AgentEmail = %s and AgentPassword = md5(%s) AND AgentID = %s'
	cursor.execute(query, (username, password, agent_id))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	
	sessionRunning = isSessionLoggedIn()
	if (sessionRunning == True): 
		error = 'Other users signed in. Please sign out of current session.'
		return render_template('Booking-Agent-Login.html', error=error)
	
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return render_template('Booking-Agent-Home.html', username = session['username'])
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Booking-Agent-Login.html', error=error)

@app.route('/Booking-Agent-Home', methods=['GET', 'POST'])
def bookingAgentHome(): 
	return render_template('Booking-Agent-Home.html', username = session['username'])

@app.route('/Booking-Agent-View-Customer-Flights-first')
def bookingAgentViewCustFlights(): 
	username = 0
	cursor = conn.cursor()
	#executes query
	query = 'SELECT AirlineName, FlightNumber, DepartureDate, ArrivalDate, FlightStatus FROM ticket NATURAL JOIN purchasedfor NATURAL JOIN customer NATURAL JOIN flight NATURAL JOIN updates WHERE CustomerEmail = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data1 = cursor.fetchall()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	return render_template('Booking-Agent-View-Customer-Flights-first.html')

@app.route('/Booking-Agent-View-Customer-Flights-second', methods=['GET','POST'])
def bookingAgentViewCustFlightssecond(): 
	#print("here")
	username = request.form['customer-username']
	print(username)
	cursor = conn.cursor()
	queryUser = 'SELECT customeremail FROM customer WHERE customeremail = %s'
	cursor.execute(queryUser, (username))
	userData = cursor.fetchone()
	#executes query
	print(userData)
	if(userData): 
		print("user data found")
		query = 'SELECT AirlineName, FlightNumber, DepartureDate, DepartureTime, ArrivalDate, ArrivalTime, FlightStatus FROM ticket NATURAL JOIN purchasedfor NATURAL JOIN customer NATURAL JOIN flight NATURAL JOIN updates WHERE CustomerEmail = %s'
		cursor.execute(query, (username))
		#stores the results in a variable
		data1 = cursor.fetchall()
		print(data1) 
		#use fetchall() if you are expecting more than 1 data row
		cursor.close()
		error = None
		return render_template('Booking-Agent-View-Customer-Flights-second.html', flights=data1, error = error)
	else:
		data1= ""
		#print("here error")
		error = "User does not exist" 
		return render_template('Booking-Agent-View-Customer-Flights-second.html', flights = data1, error = error)#, flights=data1, error = error)


@app.route('/Booking-Agent-Registration')
def booking_agent_register():
	return render_template('Booking-Agent-Registration.html')

@app.route('/BookingAgentRegisterAuth', methods=['GET', 'POST'])
def bookingAgentRegisterAuth():
	#grabs information from the forms
	agent_id= request.form['agent-id']
	email = request.form['email']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	noExistingUserQuery = 'SELECT AgentEmail FROM bookingagent WHERE AgentEmail = %s'
	cursor.execute(noExistingUserQuery, (email))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('Booking-Agent-Registration.html', error = error)
	else:
		ins = 'INSERT INTO bookingagent VALUES(%s, md5(%s), %s)'
		cursor.execute(ins, (email, password, agent_id))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/Booking-Agent-Top-Customers')
def topCusts(): 
	username = session['username']
	cursor = conn.cursor()
	#topCusts = 'SELECT customerEmail, SUM(CommissionAmount) AS commission FROM customer NATURAL JOIN ticket NATURAL JOIN creates WHERE agentemail = %s GROUP BY customerEmail ORDER BY commission DESC LIMIT 5'
	topCustsx = 'SELECT customerEmail FROM customer NATURAL JOIN ticket NATURAL JOIN creates WHERE agentemail = %s GROUP BY customerEmail ORDER BY SUM(CommissionAmount) DESC LIMIT 5'
	cursor.execute(topCustsx, (username))
	datax = cursor.fetchall()
	print(username)
	print(datax)
	labels = [] 
	for elem in datax: 
		for key in elem: 
			labels.append(elem[key])
	print(labels)

	topCustsy = 'SELECT SUM(CommissionAmount) AS commission FROM customer NATURAL JOIN ticket NATURAL JOIN creates WHERE agentemail = %s GROUP BY customerEmail ORDER BY commission DESC LIMIT 5'
	cursor.execute(topCustsy, (username))
	datay = cursor.fetchall()
	values = [] 
	for elem in datay: 
		for key in elem: 
			values.append(elem[key])
	print(values)
	cursor.close()
	print(datay)
	return render_template('Booking-Agent-Top-Customers.html',  title='Top Customers by Commission', max=50, labels=labels, values=values)

@app.route('/View-Commissions')
def view_commissions_main(): 
	username = session['username']
	cursor = conn.cursor() 
	statistics = 'SELECT SUM(commissionAmount) AS totalcom, SUM(commissionAmount)/COUNT(*) as avgcom, COUNT(ticketID) AS numtickets FROM creates NATURAL JOIN ticket WHERE AgentEmail = %s AND CURRENT_DATE - 30 <= puchaseDate'
	cursor.execute(statistics, (username))
	comStats = cursor.fetchone() 
	print(comStats)
	cursor.close()
	return render_template("View-Commissions.html", stats = comStats)

@app.route('/Booking-Agent-Date-Coms', methods=['GET', 'POST'])
def bookingAgentDatesCommissions(): 
	start_date = request.form['start-date']
	end_date = request.form['end-date']
	username = session['username']
	cursor = conn.cursor() 
	statistics = 'SELECT SUM(commissionAmount) AS totalcom, SUM(commissionAmount)/COUNT(*) as avgcom, COUNT(ticketID) AS numtickets FROM creates NATURAL JOIN ticket WHERE AgentEmail = %s AND PuchaseDate >= %s AND PuchaseDate <= %s'
	cursor.execute(statistics, (username, start_date, end_date))
	comStats = cursor.fetchone() 
	cursor.close()
	return render_template('Booking-Agent-Date-Coms.html', stats = comStats, given_start_date = start_date, given_end_date = end_date)

@app.route('/Airline-Staff-Login')
def AirlineStafflogin():
	return render_template('Airline-Staff-Login.html')

@app.route('/AirlineStaffLoginAuth', methods=['GET', 'POST'])
def AirlineStaffLoginAuth():
	#grabs information from the forms
	username = request.form['airline-staff-username']
	password = request.form['airline-staff-password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT Username, StaffPassword FROM airlinestaff WHERE Username = %s and StaffPassword = md5(%s)'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	
	sessionRunning = isSessionLoggedIn()
	if (sessionRunning == True): 
		error = 'Other users signed in. Please sign out of current session.'
		return render_template('Airline-Staff-Login.html', error=error)
	
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return render_template('Airline-Staff-Home.html')
		#return redirect(url_for('viewFlightsPublic'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Airline-Staff-Login.html', error=error)

@app.route('/Airline-Staff-Home')
def airline_staff_home(): 
	return render_template('Airline-Staff-Home.html')

@app.route('/Airline-Staff-Registration')
def airline_staff_register():
	return render_template('Airline-Staff-Registration.html')

#Authenticates the register
@app.route('/AirlineStaffRegisterAuth', methods=['GET', 'POST'])
def airlineStaffRegisterAuth():
	#grabs information from the forms
	fname = request.form['first-name']
	lname = request.form['last-name']
	username = request.form['username']
	password = request.form['password']
	dob = request.form['date-of-birth']
	airline = request.form['airline']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	noExistingUserQuery = 'SELECT username FROM airlinestaff WHERE username = %s'
	cursor.execute(noExistingUserQuery, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('Airline-Staff-Registration.html', error = error)
	else:
		ins = 'INSERT INTO airlinestaff VALUES(%s, md5(%s), %s, %s, %s, %s)'
		cursor.execute(ins, (username, password, fname, lname, dob, airline))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/Airline-Staff-View-Flights', methods = ['GET','POST'])
def airline_staff_view_flights(): 
	username = session['username']
	cursor = conn.cursor() 
	findAirlineName = 'SELECT AirlineName FROM airlinestaff WHERE Username = %s'
	cursor.execute(findAirlineName, (username))
	airlineName = cursor.fetchone()
	currAirlineName = airlineName['AirlineName']
	findFlights = 'SELECT DISTINCT FlightNumber, DepartureDate, DepartureTime, DepartureAirport, ArrivalDate, ArrivalTime FROM airlinestaff NATURAL JOIN flight WHERE AirlineName = %s AND (DepartureDate <= CURRENT_DATE + INTERVAL 30 DAY AND (DepartureDate > CURRENT_DATE)) OR (DepartureDate = CURRENT_DATE AND DepartureTime > CURRENT_TIME) ORDER BY DepartureDate ASC'
	cursor.execute(findFlights, (currAirlineName))
	data = cursor.fetchall()
	cursor.close()
	return render_template('Airline-Staff-View-Flights.html', flights = data)

@app.route('/Airline-Staff-View-Flights-Custom-Date', methods = ['GET','POST'])
def view_flights_custom_date(): 
	start_date = request.form['start-date']
	end_date = request.form['end-date']
	cursor = conn.cursor() 
	username = session['username']
	findAirlineName = 'SELECT AirlineName FROM airlinestaff WHERE Username = %s'
	cursor.execute(findAirlineName, (username))
	airlineName = cursor.fetchone()['AirlineName']
	findFlights = 'SELECT FlightNumber, DepartureDate, DepartureTime FROM flight WHERE airlineName = %s AND DepartureDate > %s AND DepartureDate < %s'
	cursor.execute(findFlights, (airlineName, start_date, end_date))
	data = cursor.fetchall()
	cursor.close()
	if (data): 
		return render_template('Airline-Staff-View-Flights-Custom.html', flights = data)
	else: 
		error = "No flights found"
		return render_template('Airline-Staff-View-Flights-Custom.html', flights = data, error = error)



@app.route('/Airline-Staff-Top-Agents-Frequent-Customers')
def top_agent_frequent_cust(): 
	cursor = conn.cursor()
	findTopAgentMonth = 'SELECT AgentEmail, COUNT(*) AS ticketSold FROM ticket NATURAL JOIN creates WHERE puchaseDate >= CURRENT_DATE - INTERVAL 1 MONTH GROUP BY AgentEmail ORDER BY COUNT(AgentID) DESC LIMIT 5'
	cursor.execute(findTopAgentMonth)
	topAgentMonth = cursor.fetchall()
	#print(topAgent)
	findTopAgentYear = 'SELECT AgentEmail, COUNT(*) AS ticketSold FROM ticket NATURAL JOIN creates WHERE puchaseDate >= CURRENT_DATE - INTERVAL 1 YEAR GROUP BY AgentEmail ORDER BY COUNT(AgentID) DESC LIMIT 5'
	cursor.execute(findTopAgentYear)
	topAgentYear = cursor.fetchall()
	findTopAgentComsYear = 'SELECT AgentEmail, SUM(commissionAmount) AS commission FROM ticket NATURAL JOIN creates WHERE puchaseDate >= CURRENT_DATE - INTERVAL 1 YEAR GROUP BY AgentEmail ORDER BY commission DESC LIMIT 5'
	cursor.execute(findTopAgentComsYear)
	topAgentYearComs = cursor.fetchall()
	username = session['username']
	staffAirline = 'SELECT AirlineName FROM airlinestaff WHERE username = %s'
	cursor.execute(staffAirline, (username))
	staffAirlineName = cursor.fetchone()['AirlineName']
	print(staffAirlineName)
	findTopCustomer = 'SELECT CustomerEmail, COUNT(*) AS numFlights FROM ticket WHERE AirlineName = %s GROUP BY CustomerEmail ORDER BY numFlights DESC LIMIT 1'
	cursor.execute(findTopCustomer, (staffAirlineName))
	topCustomer = cursor.fetchone()
	cursor.close()
	return render_template('Airline-Staff-Top-Agents-Frequent-Customers.html', topAgentMonth = topAgentMonth, topAgentYear = topAgentYear, topAgentYearComs = topAgentYearComs, topCustomer = topCustomer)

@app.route('/Airline-Staff-View-Customer-Flights', methods = ["GET", 'POST'])
def airline_staff_view_cust_flights(): 
	custEmail = request.form["customer-email"]
	cursor = conn.cursor()
	username = session['username']
	staffAirline = 'SELECT AirlineName FROM airlinestaff WHERE username = %s'
	cursor.execute(staffAirline, (username))
	staffAirlineName = cursor.fetchone()['AirlineName']
	getFlights = 'SELECT FlightNumber, DepartureDate, DepartureTime FROM Flight NATURAL JOIN updates NATURAL JOIN purchasedfor NATURAL JOIN ticket NATURAL JOIN customer WHERE CustomerEmail = %s AND airlineName = %s ORDER BY DepartureDate'
	cursor.execute(getFlights, (custEmail, staffAirlineName))
	custFlights = cursor.fetchall()
	cursor.close()
	if custFlights: 
		return render_template('Airline-Staff-View-Customer-Flights.html', custFlights = custFlights, custEmail = custEmail)
	else: 
		error = "Customer Not Found, please go back to homepage"
		return render_template('Airline-Staff-View-Customer-Flights.html', error = error)

@app.route('/Airline-Staff-Create')
def airline_staff_create(): 
	return render_template('Airline-Staff-Create.html')


@app.route('/Airline-Staff-Create-Flight', methods = ['GET', 'POST'])
def airline_staff_create_flight(): 
	airline_name = request.form["fl-airline-name"]
	flight_number = request.form["fl-flight-number"]
	departure_air = request.form["fl-dept-airport"]
	departure_date = request.form["fl-dept-date"]
	departure_time = request.form["fl-dept-time"] #input type = 'time'
	arrival_air = request.form["fl-arr-airport"]
	arrival_date = request.form["fl-arr-date"]
	arrival_time = request.form["fl-arr-time"]
	base_price = request.form["price"]
	airplane_id = request.form["fl-airplane-id"]
	
	#primary key for flight is deptDate, deptTime, flightNum
	cursor = conn.cursor() 
	noExistFlight = 'SELECT * FROM flight WHERE FlightNumber = %s AND DepartureDate = %s AND DepartureTime = %s'
	cursor.execute(noExistFlight, (flight_number, departure_date, departure_time))
	data = cursor.fetchone()

	if(data): #if exists
		error = "Flight not added. Flight Already Exists"
		return render_template('Failure.html', error = error)
	else: 
		ins = 'INSERT INTO flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (airline_name, departure_date, departure_time, flight_number, departure_air, arrival_air, arrival_date, arrival_time, base_price, airplane_id))
		conn.commit()
		insArrives = 'INSERT INTO arrives VALUES (%s, %s, %s, %s)'
		cursor.execute(insArrives, (arrival_air, flight_number, departure_date, departure_time))
		conn.commit() 
		insDeparts = 'INSERT INTO departs VALUES (%s, %s, %s, %s)'
		cursor.execute(insDeparts, (departure_air, flight_number, departure_date, departure_time))
		conn.commit()
		username = session['username']
		insUpdates = 'INSERT INTO updates VALUES (%s, %s, %s, %s, %s)'
		cursor.execute(insUpdates, (username, flight_number, departure_date, departure_time, 'On Time'))
		conn.commit()
		cursor.close()
		error = "Flight successfully added."
		return render_template('Success.html', error = error)

@app.route('/Update-Flight-Status', methods = ['GET', 'POST'])
def update_flight_status():
	username = session['username'] 
	flight_number = request.form['up-flight-number']
	departure_date = request.form['up-dept-date']
	departure_time = request.form['up-dept-time']
	flight_status = request.form['up-flight-status']

	cursor = conn.cursor()
	flightExists = 'SELECT * FROM updates WHERE FlightNumber = %s AND DepartureDate = %s AND DepartureTime = %s'
	cursor.execute(flightExists, (flight_number, departure_date, departure_time))
	data = cursor.fetchone()
	if(data): 
		updateFlight = 'UPDATE updates SET FlightStatus = %s, Username = %s WHERE FlightNumber = %s AND DepartureDate = %s AND DepartureTime = %s'
		cursor.execute(updateFlight, (flight_status, username, flight_number, departure_date, departure_time))
		conn.commit() 
		cursor.close()
		error = "Flight Status Updated Successfully"
		return render_template("Success.html", error = error)
	else: 
		error = 'Update Flight Status Failed. Flight does not exist'
		return render_template("Failure.html", error = error)

@app.route('/Add-Airplane', methods = ['GET', 'POST'])
def add_airplane(): 
	airline_name = request.form['air-airline-name']
	airplane_id = request.form['air-airplane-ID']
	num_seats = request.form['air-num-seats']

	cursor = conn.cursor() 
	airplaneDNE = 'SELECT * FROM airplane WHERE AirlineName = %s AND AirplaneID = %s'
	cursor.execute(airplaneDNE, (airline_name, airplane_id))
	data = cursor.fetchone()
	if(data): 
		error = 'Airplane not added. Airplane already exists'
		return render_template('Failure.html', error=error)
	else: 
		addAirplane = 'INSERT INTO airplane VALUES(%s, %s, %s)'
		cursor.execute(addAirplane, (airplane_id, airline_name, num_seats))
		conn.commit()
		cursor.close()
		error = "Airplane added successfully"
		return render_template('Success.html', error = error)

@app.route('/Add-Airport', methods = ['GET', 'POST'])
def add_airport(): 
	airport_name = request.form['airport-name']
	airport_city = request.form['airport-city']

	cursor = conn.cursor()
	airportDNE = 'SELECT * FROM airport WHERE AirportName = %s'
	cursor.execute(airportDNE, (airport_name))
	data = cursor.fetchone()
	if(data): 
		error = 'Airport not added. Airport already exists'
		return render_template('Failure.html', error = error)
	else: 
		addAirport = 'INSERT INTO airport VALUES(%s, %s)'
		cursor.execute(addAirport, (airport_name, airport_city))
		conn.commit()
		cursor.close()
		error = 'Airport successfully added'
		return render_template('Success.html', error = error)

@app.route('/Airline-Staff-Rating-Destination-Revenue')
def rate_dest_rev():
	username = session['username']
	cursor = conn.cursor()
	getAirlineName = 'SELECT AirlineName FROM airlinestaff WHERE username = %s'
	cursor.execute(getAirlineName, (username))
	airline_name = cursor.fetchone()
	getAvgRatings = 'SELECT AirlineName, FlightNumber, DepartureDate, DepartureTime, AVG(Rate) as averageRating FROM suggested NATURAL JOIN Flight WHERE AirlineName = %s GROUP BY AirlineName, FlightNumber, DepartureDate, DepartureTime' 
	cursor.execute(getAvgRatings, (airline_name['AirlineName']))
	avgRatings = cursor.fetchall()
	conn.commit()

	getTopThreeDest = 'SELECT AirportCity FROM ticket NATURAL JOIN purchasedfor NATURAL JOIN flight INNER JOIN airport ON arrivalAirport = airport.AirportName WHERE AirlineName = %s AND arrivalDate >= CURRENT_DATE - INTERVAL 3 MONTH  GROUP BY AirportName ORDER BY COUNT(airportName) DESC LIMIT 3'
	cursor.execute(getTopThreeDest, (airline_name['AirlineName']))
	topThreeDests = cursor.fetchall()
	conn.commit() 
	if len(topThreeDests) < 3: 
		n1 = len(topThreeDests)
	else: 
		n1 = 3

	getTopDestYear = 'SELECT AirportCity FROM ticket NATURAL JOIN purchasedfor NATURAL JOIN flight INNER JOIN airport ON arrivalAirport = airport.AirportName WHERE AirlineName = %s AND arrivalDate >= CURRENT_DATE - INTERVAL 1 YEAR GROUP BY AirportName ORDER BY COUNT(airportName) DESC LIMIT 3'
	cursor.execute(getTopDestYear, (airline_name['AirlineName']))
	topDestYear = cursor.fetchall()
	conn.commit()
	cursor.close()
	if len(topDestYear) < 3: 
		n2 = len(topDestYear)
	else: 
		n2 = 3
	return render_template('Airline-Staff-Rating-Destination-Revenue.html', avgRatings = avgRatings, topThreeDests = topThreeDests, n1 = int(n1), n2 = int(n2), topDestYear = topDestYear)

@app.route('/Airline-Staff-View-Flight-Rating', methods = ['GET', 'POST'])
def view_specific_flight_rating(): 
	flight_number = request.form['flight-number']
	dept_date = request.form['dept-date']
	dept_time = request.form['dept-time']
	print("hi")
	cursor = conn.cursor()
	getFlightRatingComments = 'SELECT Rate, CustomerComment FROM suggested WHERE FlightNumber = %s AND DepartureDate = %s AND DepartureTime = %s'
	cursor.execute(getFlightRatingComments, (flight_number, dept_date, dept_time))
	data = cursor.fetchall()
	print("Fetched Data")
	if(data): 
		print("ifdata")
		return render_template('Airline-Staff-View-Flight-Rating.html', flights = data, flight = flight_number, date = dept_date, time = dept_time)
	else: 
		print("nodata")
		data = ""
		error = "Flight does not exist, or has no ratings"
		return render_template('Airline-Staff-View-Flight-Rating.html', flights = data, error = error, flight= flight_number, date = dept_date, time = dept_time)


'''
@app.route('/Airline-Staff-View-Agents-Customers')
def airline_staff_view_people():
	return render_template('Airline-Staff-View-Agents-Customers.html')

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM user WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = 'INSERT INTO user VALUES(%s, %s)'
		cursor.execute(ins, (username, password))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/home')
def home():
    
    username = session['username']
    cursor = conn.cursor();
    query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['blog_post'])
    cursor.close()
    return render_template('home.html', username=username, posts=data1)

		
@app.route('/post', methods=['GET', 'POST'])
def post():
	username = session['username']
	cursor = conn.cursor();
	blog = request.form['blog']
	query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
	cursor.execute(query, (blog, username))
	conn.commit()
	cursor.close()
	return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')

'''
	
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
