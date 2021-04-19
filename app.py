#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

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
		ins = 'INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (name, email, password, int(buildingNumber), street, city, state, int(phone), passportNumber,passportExp, passportCountry, dateOfBirth))
		conn.commit()
		cursor.close()
		return render_template('index.html')

def get_cust_credentials(): 
	username = request.form['customer-username']
	password = request.form['customer-password']
	return username, password

#Authenticates the login
@app.route('/CustomerLoginAuth', methods=['GET', 'POST'])
def customerLoginAuth():
	#grabs information from the forms
	#username = request.form['customer-username']
	#password = request.form['customer-password']
	username, password = get_cust_credentials()
	#print(username)
	#print(password)
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT CustomerName, CustomerEmail, CustomerPassword FROM customer WHERE CustomerEmail = %s and CustomerPassword = %s'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#print('data found')
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		'''
		getName = 'SELECT CustomerName FROM customer WHERE CustomerEmail = %s and CustomerPassword = %s'
		cursor.execute(getName, (username, password))
		customerName = cursor.fetchone()
		print(customerName)
		cursor.close()
		'''
		return render_template('Customer-Home.html', name = username)
		#return redirect(url_for('customerHome', username = username))
	else:
		#print("here")
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Customer-Login.html', error=error)


@app.route('/Customer-Home')
def customerHome(): 
	return render_template('Customer-Home.html', name = session['username'])
'''
@app.route('/View-Customer-Flights') #needs a query for this!!
def viewCustomerFlights(): 
	cursor = conn.cursor();
    query = 'SELECT AirlineName, FlightNumber, DepartureDate, DepartureTime, ArrivalDate, ArrivalTime, FlightStatus FROM Flight AS f NATURAL JOIN updates ORDER BY DepartureDate LIMIT 10'
    cursor.execute(query)
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['AirlineName'])
    cursor.close()
    return render_template('View-Customer-Flights.html', flights=data1)
	#return render_template('View-Customer-Flights.html')
'''
@app.route('/Customer-Search-Flights') #needs a query for this!! 
def searchCustomerFlights(): 
	return render_template('Customer-Search-Flights.html',)

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

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT AgentEmail, AgentPassword FROM bookingagent WHERE AgentEmail = %s and AgentPassword = %s'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return render_template('index.html')
		return redirect(url_for('viewFlightsPublic'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Booking-Agent-Login.html', error=error)

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
	query = 'SELECT Username, StaffPassword FROM airlinestaff WHERE Username = %s and StaffPassword = %s'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return render_template('index.html')
		#return redirect(url_for('viewFlightsPublic'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('Airline-Staff-Login.html', error=error)

'''
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
