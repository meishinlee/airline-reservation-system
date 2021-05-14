#Add airline name
INSERT INTO airline VALUES('Air China');

#add airline Staff
INSERT INTO airlinestaff VALUES ('admin', md5('abcd'), 'Roe', 'Jones', '1978-05-25', 'Air China');
#add phone numbers 
INSERT INTO phonenumber VALUES ('admin',11122223333);
INSERT INTO phonenumber VALUES ('admin',44455556666);

#add 3 airplanes
INSERT INTO airplane VALUES ('Air China', 1, 4);
INSERT INTO airplane VALUES ('Air China', 2, 4);
INSERT INTO airplane VALUES ('Air China', 3, 50);

#add 8 airports
INSERT INTO airport VALUES ('JFK', 'NYC');
INSERT INTO airport VALUES ('BOS', 'Boston');
INSERT INTO airport VALUES ('PVG', 'Shanghai');
INSERT INTO airport VALUES ('BEI', 'Beijing');
INSERT INTO airport VALUES ('SHEN', 'Shenzhen');
INSERT INTO airport VALUES ('SFO', 'San Francisco');
INSERT INTO airport VALUES ('LAX', 'Los Angeles');
INSERT INTO airport VALUES ('HKA', 'Hong Kong');

#booking Agent
INSERT INTO bookingagent VALUES ('ctrip@agent.com', md5('abcd1234'), 1);
INSERT INTO bookingagent VALUES ('expedia@agent.com', md5('abcd1234'), 2);

#customers 
INSERT INTO customer VALUES ('Test Customer 1', 'testcustomer@nyu.edu', md5('1234'), 1555, 'Jay St', 'Brooklyn', 'New York', 12343214321, 54321, '2025-12-24', 'USA', '1999-12-19');
INSERT INTO customer VALUES ('User 1', 'user1@nyu.edu', md5('1234'), 5405, 'Jay Street', 'Brooklyn', 'New York', 12343224322, 54322, '2025-12-25', 'USA', '1999-11-19');
INSERT INTO customer VALUES ('User 2', 'user2@nyu.edu', md5('1234'), 1702, 'Jay Street', 'Brooklyn', 'New York', 12343234323, 54323, '2025-10-24', 'USA', '1999-10-19');
INSERT INTO customer VALUES ('User 3', 'user3@nyu.edu', md5('1234'), 1890, 'Jay Street', 'Brooklyn', 'New York', 12343244324, 54324, '2025-09-24', 'USA', '1999-09-19');

#flights 
#flight 1
INSERT INTO flight VALUES ('Air China', '2021-04-12', '13:25:25', 102, 'SFO', 'LAX', '2021-04-12', '16:50:25', 300, 3);
INSERT INTO updates VALUES ('admin', 102, '2021-04-12', '13:25:25', 'on-time');
INSERT INTO departs VALUES ('SFO', 102, '2021-04-12', '13:25:25'); 
INSERT INTO arrives VALUES ('LAX', 102, '2021-04-12', '13:25:25');
#flight 2
INSERT INTO flight VALUES ('Air China', '2021-05-14', '13:25:25', 104, 'PVG', 'BEI', '2021-05-14', '16:50:25', 300, 3);
INSERT INTO updates VALUES ('admin', 104, '2021-05-14', '13:25:25', 'on-time');
INSERT INTO departs VALUES ('PVG', 104, '2021-05-14', '13:25:25'); 
INSERT INTO arrives VALUES ('BEI', 104, '2021-05-14', '13:25:25');
#flight 3 
INSERT INTO flight VALUES ('Air China', '2021-03-12', '13:25:25', 106, 'SFO', 'LAX', '2021-03-12', '16:50:25', 350, 3);
INSERT INTO updates VALUES ('admin', 106, '2021-03-12', '13:25:25', 'delayed');
INSERT INTO departs VALUES ('SFO', 106, '2021-03-12', '13:25:25'); 
INSERT INTO arrives VALUES ('LAX', 106, '2021-03-12', '13:25:25');
#flight 4
INSERT INTO flight VALUES ('Air China', '2021-06-12', '13:25:25', 206, 'SFO', 'LAX', '2021-06-12', '16:50:25', 400, 2);
INSERT INTO updates VALUES ('admin', 206, '2021-06-12', '13:25:25', 'on-time');
INSERT INTO departs VALUES ('SFO', 206, '2021-06-12', '13:25:25'); 
INSERT INTO arrives VALUES ('LAX', 206, '2021-06-12', '13:25:25');
#flight 5
INSERT INTO flight VALUES ('Air China', '2021-07-12', '13:25:25', 207, 'LAX', 'SFO', '2021-07-12', '16:50:25', 300, 2);
INSERT INTO updates VALUES ('admin', 207, '2021-07-12', '13:25:25', 'on time');
INSERT INTO departs VALUES ('LAX', 207, '2021-07-12', '13:25:25'); 
INSERT INTO arrives VALUES ('SFO', 207, '2021-07-12', '13:25:25');
#flight 6
INSERT INTO flight VALUES ('Air China', '2021-02-12', '13:25:25', 134, 'JFK', 'BOS', '2021-02-12', '16:50:25', 300, 3);
INSERT INTO updates VALUES ('admin', 134, '2021-02-12', '13:25:25', 'delayed');
INSERT INTO departs VALUES ('JFK', 134, '2021-02-12', '13:25:25'); 
INSERT INTO arrives VALUES ('BOS', 134, '2021-02-12', '13:25:25');
#flight 7
INSERT INTO flight VALUES ('Air China', '2021-06-01', '13:25:25', 296, 'PVG', 'SFO', '2021-06-01', '16:50:25', 3000, 1);
INSERT INTO updates VALUES ('admin', 296, '2021-06-01', '13:25:25', 'on-time');
INSERT INTO departs VALUES ('PVG', 296, '2021-06-01', '13:25:25'); 
INSERT INTO arrives VALUES ('SFO', 296, '2021-06-01', '13:25:25');
#flight 8
INSERT INTO flight VALUES ('Air China', '2021-04-28', '10:25:25', 715, 'PVG', 'BEI', '2021-04-28', '13:50:25', 500, 1);
INSERT INTO updates VALUES ('admin', 715, '2021-04-28', '10:25:25', 'delayed');
INSERT INTO departs VALUES ('PVG', 715, '2021-04-28', '10:25:25'); 
INSERT INTO arrives VALUES ('BEI', 715, '2021-04-28', '10:25:25');
#flight 9
INSERT INTO flight VALUES ('Air China', '2020-07-12', '13:25:25', 839, 'SHEN', 'BEI', '2020-07-12', '16:50:25', 300, 3);
INSERT INTO updates VALUES ('admin', 839, '2020-07-12', '13:25:25', 'on-time');
INSERT INTO departs VALUES ('SHEN', 839, '2020-07-12', '13:25:25'); 
INSERT INTO arrives VALUES ('BEI', 839, '2020-07-12', '13:25:25');

#add tickets ticket, create, purchasedfor, payment method, ProvidesPersonalInfo, cardInfo
#ticket 1
INSERT INTO ticket VALUES (1, 'testcustomer@nyu.edu', 'Air China', 102, 300, '2021-03-12', '11:55:55', 'ctrip@agent.com');
INSERT INTO creates VALUES ('ctrip@agent.com', 1, 30);
INSERT INTO purchasedfor VALUES (1, 102, '2021-04-12', '13:25:25');
INSERT INTO cardinfo VALUES ('1111-2222-3333-4444', 'credit', 'Test Customer 1', '2023-03-01');
INSERT INTO providespersonalinfo VALUES ('1111-2222-3333-4444', 'testcustomer@nyu.edu');
INSERT INTO paymentmethod VALUES ('1111-2222-3333-4444', 1);

#ticket 2
INSERT INTO ticket VALUES (2, 'user1@nyu.edu', 'Air China', 102, 300, '2021-03-11', '11:55:55', "NULL");
INSERT INTO purchasedfor VALUES (2, 102, '2021-04-12', '13:25:25');
INSERT INTO cardinfo VALUES ('1111-2222-3333-5555', 'credit', 'User 1', '2023-03-01');
INSERT INTO providespersonalinfo VALUES ('1111-2222-3333-5555', 'user1@nyu.edu');
INSERT INTO paymentmethod VALUES ('1111-2222-3333-5555', 2);

#ticket 3
INSERT INTO ticket VALUES (3, 'user2@nyu.edu', 'Air China', 102, 300, '2021-04-11', '11:55:55', "NULL");
INSERT INTO purchasedfor VALUES (3, 102, '2021-04-12', '13:25:25');
#INSERT INTO cardinfo VALUES ('1111-2222-3333-5555', 'credit', 'User 2', '2023-03-01'); #already added as user1
INSERT INTO providespersonalinfo VALUES ('1111-2222-3333-5555', 'user2@nyu.edu');
INSERT INTO paymentmethod VALUES ('1111-2222-3333-5555', 3);

#ticket 4
INSERT INTO ticket VALUES (4, 'user1@nyu.edu', 'Air China', 104, 300, '2021-03-21', '11:55:55', "NULL");
INSERT INTO purchasedfor VALUES (4, 104, '2021-05-14', '13:25:25');
#INSERT INTO cardinfo VALUES ('1111-2222-3333-5555', 'credit', 'User 2', '2023-03-01'); #already added as user1
INSERT INTO providespersonalinfo VALUES ('1111-2222-3333-5555', 'user1@nyu.edu');
INSERT INTO paymentmethod VALUES ('1111-2222-3333-5555', 4);

#ticket 5 (MustCheck)
INSERT INTO ticket VALUES (5, 'testcustomer@nyu.edu', 'Air China', 104, 300, '2021-04-28', '11:55:55', 'ctrip@agent.com');
INSERT INTO creates VALUES ('ctrip@agent.com', 5, 30);
INSERT INTO purchasedfor VALUES (5, 104, '2021-05-14', '13:25:25');
#INSERT INTO cardinfo VALUES ('1111-2222-3333-4444', 'credit', 'Test Customer 1', '2023-03-01');
#INSERT INTO providespersonalinfo VALUES ('1111-2222-3333-4444', 'testcustomer@nyu.edu');
INSERT INTO paymentmethod VALUES ('1111-2222-3333-4444', 5);

#ticket 6