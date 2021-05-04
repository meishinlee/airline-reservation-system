Mei Shin Lee, Ruhejami Mustari 

Finished: 
- All MD5s hashed
- Customer Login -> finished
- Customer Registration OK, works fine
- Index -> Not linked to booking reg, airline staff reg
- Booking Agent Login -> finished
- View Flights (Mei), completely finished
- Airline Staff Register -> Finished linking completely

- Airline Staff Login -> linked to auth in db, not linked to airline staff homepage 
- Booking Agent Register -> OK
- Airline Staff Home (Ruhejami, Finished. Pages Unlinked to backend)
    - Airline staff form submitted but not written in backend  
- Booking Agent Home Page (finished)

Concerns: 
- Passport number duplicates in database despite different email IDs? 
- phone number can't exceed 2^10? 
- Forgot to add a row in purchased for (ticket 1)
- How to add foreign key for Flight-AirplaneID to Airplane-AirplaneID??**

In Progress: 
- Search flight - need query and need table designs. -> make 2 webpages here  
    - Perform another search, back to home. 
- Customer Homepage (Mei), finished 
    - View my Flights (Finished)
    - Search flights/Purchase Tickets (linked to customer home page, but whats a round trip)? 
    - Rate/Comment (finished). Added additional constraint where I checked for no dup ratings 
    - Track Spending (didn't start idk how to make a barchart) !!!
    - Logout (finished)
- Booking Agent Homepage 
    - View my Flights (finished)
    - Search my Flights/Purchase Tickets (Have not Started)
    - View my Commissions (Finished)
    - Top 5 Customers (DONE, but need to add more customers for test case)
    - Logout (finished)
- Airline Staff Homepage 
    - View flights <- All done 
    - Create flights (done)<--By default should i have a 'On time' Flight status (updates table)?
    - Update stuff (done)
    - Logout (Finished)
    - View ratings View Ratings of Flight done. Only thing not done here is revenue (Pie chart)
    - View top 5 booking agents by commission (Done)
    - View most frequent customer, list of flights a particular customer has taken on that airline (Done)
    - View reports (Chart) NOT DONE 

Flight 6 and 7 are round trips. Everything else is one way 

Total Not done: 
Customer: 
    - Search Flight Table (FINISHED)
    - Track Spending Chart 
Booking Agent: 
    - Search Flights + Purchase Tickets (FINISHED)
    - Top Commission = Charts not showing properly
Airline Staff: 
    - View Revenue Chart <-can't display chart>
    - View Reports 

*******SEE LINE 300

To Do: 
- Search Flights - with customer  
- Purchase Tickets 
- Booking Agent and Airline Staff Pages
