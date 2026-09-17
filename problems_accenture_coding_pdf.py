"""
68 (67 usable) coding problems sourced from the "Accenture Coding.pdf" question bank.
Every problem here is judged server-side against a Java program read via stdin.
All reference solutions were hand-verified by compiling and running a correct Java
program against each test's input and using its actual trimmed stdout as `expected`.
"""

T = "Accenture PDF Set"


def db_entry(name, hidden, schema, seed, reference_query):
    return {"name": name, "hidden": hidden, "schema": schema, "seed": seed, "reference_query": reference_query}

SQL_BOILERPLATE = "-- Write your SQLite query below\nSELECT\nFROM\nWHERE"
SQL_BOILERPLATE_GB = "-- Write your SQLite query below\nSELECT\nFROM\nWHERE\nGROUP BY"
SQL_BOILERPLATE_GBHO = "-- Write your SQLite query below\nSELECT\nFROM\nWHERE\nGROUP BY\nHAVING\nORDER BY"
SQL_BOILERPLATE_JOIN = "-- Write your SQLite query below\nSELECT\nFROM\nJOIN\nWHERE"
SQL_BOILERPLATE_JOIN_ORDER = "-- Write your SQLite query below\nSELECT\nFROM\nJOIN\nWHERE\nORDER BY"

# ---------------------------------------------------------------------------
# Schema/seed/reference-query clusters for the 30 SQL problems (3068-3097)
# sourced from "Accenture SQL.pdf". Verified directly against Python's
# sqlite3 module before being wired into problem dicts below.
# ---------------------------------------------------------------------------
# =========================================================================
# CLUSTER: Banking (Q1, Q2, Q12, Q13)
# =========================================================================
BANK_SCHEMA = """
CREATE TABLE customer (customer_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, contact TEXT, email TEXT);
CREATE TABLE branch (branch_id INTEGER PRIMARY KEY, name TEXT, address TEXT, contact TEXT);
CREATE TABLE account_type (account_type_id INTEGER PRIMARY KEY, account_type_name TEXT);
CREATE TABLE account (account_id INTEGER PRIMARY KEY, customer_id INTEGER, branch_id INTEGER, account_type_id INTEGER, balance REAL);
CREATE TABLE account_transaction (transaction_id INTEGER PRIMARY KEY, account_id INTEGER, transaction_date TEXT, amount REAL, transaction_type TEXT);
CREATE TABLE loan (loan_id INTEGER PRIMARY KEY, account_id INTEGER, loan_amount REAL, loan_date TEXT, due_date TEXT);
"""

BANK_VIS = {
    "account_type": [(1,'Savings'),(2,'Salary'),(3,'Current'),(4,'Fixed Deposit')],
    "branch": [(1,'MG Road','12 MG Rd, Blr','080-1111'),(2,'Koramangala','5th Blk, Blr','080-2222')],
    "customer": [(1,'Alice','Smith','9990001111','alice@x.com'),(2,'Bob','Johnson','9990002222','bob@x.com'),
                 (3,'Carol','White','9990003333','carol@x.com'),(4,'David','Brown','9990004444','david@x.com'),
                 (5,'Emma','Davis','9990005555','emma@x.com')],
    "account": [(101,1,1,1,75000.00),(102,2,1,3,20000.00),(103,3,2,2,60000.00),
                (104,4,2,4,90000.00),(105,5,1,1,30000.00),(106,1,2,3,55000.00)],
    "account_transaction": [
        (1001,101,'2025-01-05',15000.00,'Debit'),
        (1002,101,'2025-02-10',60000.00,'Debit'),
        (1003,102,'2025-01-15',5000.00,'Debit'),
        (1004,103,'2025-03-01',25000.00,'Credit'),
        (1005,103,'2025-03-05',12000.00,'Debit'),
        (1006,104,'2025-04-01',9999.00,'Debit'),
        (1007,105,'2025-05-01',49999.00,'Debit'),
        (1008,106,'2025-06-01',50000.00,'Debit'),
        (1009,102,'2025-07-01',30000.00,'Debit'),
    ],
    "loan": [(1,101,200000.00,'2024-01-01','2029-01-01'),(2,103,150000.00,'2024-06-01','2027-06-01')],
}

BANK_HID = {
    "account_type": [(1,'Savings'),(2,'Salary'),(3,'Current'),(4,'Fixed Deposit')],
    "branch": [(1,'Andheri','1 And Rd, Mum','022-1111'),(2,'Powai','2 Pow Rd, Mum','022-2222')],
    "customer": [(11,'Frank','Moore','8880001111','frank@x.com'),(12,'Grace','Lee','8880002222','grace@x.com'),
                 (13,'Henry','Walker','8880003333','henry@x.com'),(14,'Ivy','Clark','8880004444','ivy@x.com'),
                 (15,'Jack','Hall','8880005555','jack@x.com')],
    "account": [(201,11,1,1,48000.00),(202,12,1,2,52000.00),(203,13,2,3,80000.00),
                (204,14,2,4,45000.00),(205,15,1,1,95000.00),(206,12,2,3,15000.00)],
    "account_transaction": [
        (2001,201,'2025-01-01',11000.00,'Debit'),
        (2002,201,'2025-01-02',49000.00,'Debit'),
        (2003,202,'2025-02-01',10000.00,'Debit'),
        (2004,203,'2025-02-02',20000.00,'Credit'),
        (2005,203,'2025-03-01',35000.00,'Debit'),
        (2006,204,'2025-04-01',5000.00,'Debit'),
        (2007,205,'2025-05-01',50000.00,'Debit'),
        (2008,206,'2025-06-01',12345.00,'Debit'),
    ],
    "loan": [(11,201,100000.00,'2023-01-01','2028-01-01')],
}

Q1 = "SELECT transaction_id AS TRANSACTION_ID, amount AS AMOUNT, transaction_type AS TRANSACTION_TYPE FROM account_transaction WHERE transaction_type = 'Debit' AND amount > 10000 AND amount < 50000 ORDER BY transaction_id;"
Q2 = "SELECT c.first_name AS FIRST_NAME, c.contact AS CONTACT, a.balance AS BALANCE FROM customer c JOIN account a ON c.customer_id = a.customer_id JOIN account_type at ON a.account_type_id = at.account_type_id WHERE at.account_type_name LIKE 'Sa%' ORDER BY c.first_name, a.account_id;"
Q12 = "SELECT account_type_id AS Account_Type_ID, AVG(balance) AS Average FROM account GROUP BY account_type_id HAVING AVG(balance) >= 50000 ORDER BY account_type_id;"
Q13 = "SELECT c.first_name AS FIRST_NAME, c.last_name AS LAST_NAME, a.account_id AS ACCOUNT_ID FROM customer c JOIN account a ON c.customer_id = a.customer_id WHERE a.balance >= 50000 ORDER BY c.first_name, a.account_id;"

# =========================================================================
# CLUSTER: HR/Payroll (Q3, Q4, Q9, Q10, Q11)
# =========================================================================
HR_SCHEMA = """
CREATE TABLE department_info (deptid INTEGER PRIMARY KEY, deptname TEXT, location TEXT);
CREATE TABLE salary_info (employee_category TEXT PRIMARY KEY, basic REAL, travelling_allowance REAL, dearness_allowance REAL, house_rent_allowance REAL, location_allowance REAL, provident_fund REAL, medical_allowance REAL, proftax REAL, insurance REAL);
CREATE TABLE emp_info (empid INTEGER PRIMARY KEY, empname TEXT, deptid INTEGER, joining_dt TEXT, dob TEXT, yrs_of_exp INTEGER, employee_category TEXT);
CREATE TABLE emp_payroll (transno INTEGER PRIMARY KEY, empid INTEGER, month TEXT, year INTEGER, totalearning REAL, netpay REAL);
CREATE TABLE emp_leave_info (leaveid INTEGER PRIMARY KEY, empid INTEGER, from_date TEXT, to_date TEXT, total_leaves INTEGER, leave_type TEXT);
"""

HR_VIS = {
    "department_info": [(1,'HR','BANGALORE'),(2,'Finance','MUMBAI'),(3,'Engineering','COCHIN'),(4,'Sales','DELHI')],
    "salary_info": [
        ('A',8000,500,1000,2500,300,800,200,100,150),
        ('B',6000,400,800,1800,250,600,150,80,120),
        ('C',4000,300,600,1200,200,400,100,60,90),
        ('D',12000,700,1400,3000,400,1200,300,150,200),
    ],
    "emp_info": [
        (1,'Alice Rao',1,'1998-05-10','1975-01-01',12,'D'),
        (2,'Bob Nair',1,'2003-03-15','1980-02-02',8,'A'),
        (3,'Carol Iyer',2,'2010-07-01','1985-03-03',15,'D'),
        (4,'David Menon',3,'2015-09-09','1990-04-04',3,'B'),
        (5,'Emma Pillai',3,'2005-01-01','1992-05-05',6,'C'),
        (6,'Farhan Khan',4,'2000-01-01','1978-06-06',20,'D'),
        (7,'Gita Shah',1,'2012-11-11','1988-07-07',9,'B'),
    ],
    "emp_payroll": [
        (1,1,'Aug',2025,13000,11500),(2,2,'Aug',2025,9000,8000),(3,3,'Aug',2025,13500,12000),
        (4,4,'Aug',2025,7000,6200),(5,5,'Aug',2025,5000,4400),(6,6,'Aug',2025,13800,12300),
        (7,7,'Aug',2025,7200,6400),
    ],
    "emp_leave_info": [
        (1,1,'2025-01-01','2025-01-05',5,'CL'),
        (2,2,'2025-02-01','2025-02-15',12,'CL'),
        (3,3,'2025-03-01','2025-03-20',15,'ML'),
        (4,4,'2025-04-01','2025-04-10',8,'SL'),
        (5,5,'2025-05-01','2025-05-25',20,'ML'),
        (6,6,'2025-06-01','2025-06-03',3,'CL'),
        (7,7,'2025-07-01','2025-07-20',11,'CL'),
    ],
}

HR_HID = {
    "department_info": [(1,'HR','BANGALORE'),(2,'IT','PUNE'),(3,'Support','COCHIN'),(4,'Ops','CHENNAI')],
    "salary_info": [
        ('A',7000,450,900,2200,280,700,180,90,130),
        ('B',5500,380,750,1700,240,550,140,75,110),
        ('C',4500,320,650,1300,210,420,105,65,95),
        ('D',11000,680,1350,2800,390,1150,290,145,195),
    ],
    "emp_info": [
        (21,'Karan Mehta',1,'1999-06-01','1976-01-01',14,'D'),
        (22,'Lakshmi Rao',1,'2004-04-04','1981-02-02',7,'B'),
        (23,'Manoj Kumar',2,'2011-11-11','1986-03-03',10,'A'),
        (24,'Neha Verma',3,'2016-01-01','1991-04-04',2,'D'),
        (25,'Omkar Joshi',3,'2006-06-06','1993-05-05',9,'C'),
        (26,'Priya Nambiar',4,'1998-01-01','1979-06-06',18,'D'),
        (27,'Rahul Bose',1,'2013-09-09','1989-07-07',6,'A'),
    ],
    "emp_payroll": [
        (21,21,'Aug',2025,12500,11000),(22,22,'Aug',2025,8200,7300),(23,23,'Aug',2025,10800,9600),
        (24,24,'Aug',2025,13200,11800),(25,25,'Aug',2025,5600,4900),(26,26,'Aug',2025,13000,11600),
        (27,27,'Aug',2025,8400,7500),
    ],
    "emp_leave_info": [
        (21,21,'2025-01-01','2025-01-04',4,'CL'),
        (22,22,'2025-02-01','2025-02-20',18,'ML'),
        (23,23,'2025-03-01','2025-03-25',22,'CL'),
        (24,24,'2025-04-01','2025-04-06',5,'SL'),
        (25,25,'2025-05-01','2025-05-14',13,'ML'),
        (26,26,'2025-06-01','2025-06-02',2,'CL'),
        (27,27,'2025-07-01','2025-07-12',11,'CL'),
    ],
}

Q3 = "SELECT emp_info.empid AS EMPID, emp_info.empname AS EMPNAME, salary_info.basic AS BASIC, emp_payroll.netpay AS NETPAY FROM emp_info JOIN salary_info ON emp_info.employee_category = salary_info.employee_category JOIN emp_payroll ON emp_info.empid = emp_payroll.empid WHERE salary_info.basic > 5000 ORDER BY emp_info.empid;"
Q4 = "SELECT empid AS \"Employee ID\", empname AS \"Employee Name\" FROM emp_info WHERE yrs_of_exp > 5 AND joining_dt > '2001-01-01' ORDER BY empid;"
Q9 = "SELECT empid AS EMPID, leave_type AS LEAVE_TYPE, total_leaves AS TOTAL_LEAVES FROM emp_leave_info WHERE total_leaves > 10 AND leave_type IN ('CL','ML') ORDER BY empid;"
Q10 = "SELECT ei.empid AS EMPID, ei.empname AS EMPNAME, di.deptname AS DEPTNAME, si.basic AS BASIC FROM emp_info ei JOIN department_info di ON ei.deptid = di.deptid JOIN salary_info si ON ei.employee_category = si.employee_category WHERE di.deptname = 'HR' ORDER BY ei.empid;"
Q11 = "SELECT ei.empid AS EMPID, ei.empname AS EMPNAME, di.deptname AS DEPTNAME, si.house_rent_allowance AS HOUSE_RENT_ALLOWANCE FROM emp_info ei JOIN department_info di ON ei.deptid = di.deptid JOIN salary_info si ON ei.employee_category = si.employee_category WHERE di.location IN ('BANGALORE','COCHIN') ORDER BY ei.empid;"

# =========================================================================
# CLUSTER: School (Q5, Q18)
# =========================================================================
SCHOOL_SCHEMA = """
CREATE TABLE department (dept_id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE instructor (instructor_id INTEGER PRIMARY KEY, last_name TEXT, first_name TEXT, type TEXT, dept_id INTEGER);
CREATE TABLE course (course_id INTEGER PRIMARY KEY, name TEXT, type TEXT, term TEXT);
CREATE TABLE schedule (schedule_id INTEGER PRIMARY KEY, day TEXT, starttime TEXT, endtime TEXT);
CREATE TABLE section (section_id INTEGER PRIMARY KEY, course_id INTEGER, schedule_id INTEGER, instructor_id INTEGER, name TEXT);
CREATE TABLE student (student_id INTEGER PRIMARY KEY, last_name TEXT, first_name TEXT, email TEXT, phone TEXT);
CREATE TABLE registration (reg_id INTEGER PRIMARY KEY, reg_year INTEGER, reg_date TEXT, student_id INTEGER, section_id INTEGER, midterm_grade INTEGER, finalterm_grade INTEGER);
"""

SCHOOL_VIS = {
    "department": [(1,'Computer Science'),(2,'Mathematics')],
    "instructor": [(1,'Smith','John','Full-time',1),(2,'Doe','Jane','Part-time',2)],
    "course": [(1,'Database Systems','Lecture','Fall'),(2,'Calculus I','Lecture','Fall'),(3,'Data Structures','Lecture','Spring')],
    "schedule": [(1,'wed','09:00','10:30'),(2,'mon','11:00','12:30'),(3,'wed','14:00','15:30'),(4,'fri','10:00','11:30')],
    "section": [(1,1,1,1,'A'),(2,2,2,2,'A'),(3,3,3,1,'B'),(4,1,4,1,'C')],
    "student": [(1,'Kumar','Aditi','aditi@x.com','111'),(2,'Rao','Bala','bala@x.com','222'),
                (3,'Nair','Chitra','chitra@x.com','333'),(4,'Iyer','Deepak','deepak@x.com','444')],
    "registration": [(1,2012,'2012-08-15',1,1,80,85),(2,2013,'2013-08-20',2,1,70,75),
                      (3,2012,'2012-01-10',3,2,90,92),(4,2014,'2014-09-01',4,3,60,65)],
}

SCHOOL_HID = {
    "department": [(1,'Physics'),(2,'Chemistry')],
    "instructor": [(1,'Brown','Alan','Full-time',1),(2,'Green','Betty','Part-time',2)],
    "course": [(1,'Quantum Mechanics','Lecture','Fall'),(2,'Organic Chemistry','Lecture','Fall'),(3,'Thermodynamics','Lecture','Spring')],
    "schedule": [(1,'wed','10:00','11:30'),(2,'tue','09:00','10:30'),(3,'wed','13:00','14:30'),(4,'thu','15:00','16:30')],
    "section": [(1,1,1,1,'A'),(2,2,2,2,'A'),(3,3,3,1,'B'),(4,2,4,2,'C')],
    "student": [(11,'Patel','Esha','esha@x.com','555'),(12,'Shah','Farid','farid@x.com','666'),
                (13,'Joshi','Gauri','gauri@x.com','777'),(14,'Desai','Hemant','hemant@x.com','888')],
    "registration": [(11,2012,'2012-03-01',11,1,80,85),(12,2012,'2012-11-11',12,2,70,75),
                      (13,2015,'2015-01-01',13,3,90,92),(14,2011,'2011-05-05',14,1,60,65)],
}

Q5 = "SELECT c.course_id AS \"Course ID\", c.name AS \"Course Name\", s.day AS \"Day\", s.starttime AS \"Start Time\" FROM course c JOIN section sec ON c.course_id = sec.course_id JOIN schedule s ON sec.schedule_id = s.schedule_id WHERE s.day = 'wed' ORDER BY c.course_id, sec.section_id;"
Q18 = "SELECT s.last_name AS last_name FROM student s JOIN registration r ON s.student_id = r.student_id WHERE r.reg_date LIKE '2012%' ORDER BY s.last_name;"

# =========================================================================
# CLUSTER: Trains (Q8, Q22)
# =========================================================================
TRAIN_SCHEMA = """
CREATE TABLE train_type_tbl (train_type TEXT PRIMARY KEY, type_description TEXT);
CREATE TABLE train_stations_tbl (station_id TEXT PRIMARY KEY, station_name TEXT);
CREATE TABLE train_details_tbl (train_id TEXT PRIMARY KEY, train_name TEXT, train_type TEXT, train_time TEXT, train_from TEXT, train_to TEXT, train_speed INTEGER);
"""

TRAIN_VIS = {
    "train_type_tbl": [('EXP','Express'),('SF','Superfast'),('PASS','Passenger')],
    "train_stations_tbl": [('ST01','MUMBAI'),('ST02','PUNE'),('ST03','DELHI'),('ST04','CHENNAI')],
    "train_details_tbl": [
        ('T001','Mumbai Express','EXP','06:00','ST01','ST02',80),
        ('T002','Deccan Queen','SF','07:00','ST01','ST02',95),
        ('T003','Chennai Mail','PASS','08:00','ST03','ST04',40),
        ('T004','Malwa Express','EXP','09:00','ST03','ST01',45),
        ('T005','Mysore Express','SF','10:00','ST04','ST02',30),
        ('T006','Local Passenger','PASS','11:00','ST02','ST01',20),
    ],
}

TRAIN_HID = {
    "train_type_tbl": [('EXP','Express'),('SF','Superfast'),('PASS','Passenger')],
    "train_stations_tbl": [('ST01','PUNE'),('ST02','NAGPUR'),('ST03','GOA'),('ST04','KOLHAPUR')],
    "train_details_tbl": [
        ('T101','Mahalaxmi Express','EXP','05:00','ST02','ST01',70),
        ('T102','Konkan Kanya','SF','06:30','ST02','ST03',55),
        ('T103','Milind Superfast','SF','07:15','ST04','ST02',35),
        ('T104','Marathwada Express','EXP','08:45','ST03','ST01',48),
        ('T105','Goa Express','PASS','09:30','ST01','ST03',25),
    ],
}

Q8 = "SELECT td.train_id, td.train_name FROM train_details_tbl td JOIN train_stations_tbl ts ON td.train_to = ts.station_id WHERE td.train_name LIKE 'M%' AND ts.station_name = 'PUNE' ORDER BY td.train_id;"
Q22 = "SELECT train_name AS TRAIN_NAME, train_type AS TRAIN_TYPE FROM train_details_tbl WHERE train_speed < 50 ORDER BY train_id;"

# =========================================================================
# CLUSTER: Simple flights (Q16, Q17)
# =========================================================================
SFLIGHT_SCHEMA = """
CREATE TABLE Airline (airline_id INTEGER PRIMARY KEY, name TEXT, country TEXT);
CREATE TABLE Airplane (airplane_id INTEGER PRIMARY KEY, airline_id INTEGER, model TEXT, manufacturer TEXT, modelnumber TEXT, capacity INTEGER);
CREATE TABLE Flight (flight_id INTEGER PRIMARY KEY, airplane_id INTEGER, departure_date TEXT, departure_time TEXT, origin TEXT, destination TEXT);
"""

SFLIGHT_VIS = {
    "Airline": [(1,'Singapore Airlines','Singapore'),(2,'Emirates','UAE'),(3,'Qantas','Australia')],
    "Airplane": [(1,1,'A350','Airbus','A350-900',300),(2,1,'B777','Boeing','777-300ER',350),
                 (3,2,'A380','Airbus','A380-800',500),(4,3,'B787','Boeing','787-9',290)],
    "Flight": [(1,1,'2025-01-10','08:00','SIN','LHR'),(2,2,'2025-01-11','09:30','SIN','SYD'),
               (3,3,'2025-02-01','10:00','DXB','JFK'),(4,4,'2025-03-01','11:00','SYD','LAX')],
}

SFLIGHT_HID = {
    "Airline": [(1,'Singapore Airlines','Singapore'),(2,'Cathay Pacific','Hong Kong'),(3,'Lufthansa','Germany')],
    "Airplane": [(1,1,'A320','Airbus','A320-200',180),(2,2,'B747','Boeing','747-8',410),
                 (3,3,'A340','Airbus','A340-600',380),(4,1,'B737','Boeing','737-800',160)],
    "Flight": [(1,1,'2025-04-01','06:00','SIN','HKG'),(2,2,'2025-04-02','07:00','HKG','SIN'),
               (3,3,'2025-05-01','12:00','FRA','JFK'),(4,4,'2025-05-05','13:30','SIN','KUL')],
}

Q16 = "SELECT f.flight_id AS Flight_ID, f.departure_date AS Departure_date, f.departure_time AS Departure_Time FROM Flight f JOIN Airplane a ON f.airplane_id = a.airplane_id JOIN Airline al ON a.airline_id = al.airline_id WHERE al.name = 'Singapore Airlines' ORDER BY f.flight_id;"
Q17 = "SELECT airplane_id AS AIRPLANE_ID, modelnumber AS MODELNUMBER FROM Airplane WHERE manufacturer = 'Airbus' ORDER BY airplane_id;"

# =========================================================================
# CLUSTER: Flight crew/booking (Q19, Q20, Q23)
# =========================================================================
CREW_SCHEMA = """
CREATE TABLE flight (flight_id TEXT PRIMARY KEY, airplane_id TEXT, departure_date TEXT, departure_time TEXT, arrival_date TEXT, arrival_time TEXT, flight_from TEXT, flight_to TEXT);
CREATE TABLE cabincrew (cabincrew_id INTEGER PRIMARY KEY, flight_id TEXT, first_name TEXT, last_name TEXT, contact TEXT);
CREATE TABLE passenger (passenger_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT, contact TEXT);
CREATE TABLE boardingpass (boardingpass_id INTEGER PRIMARY KEY, flight_id TEXT, passenger_id INTEGER, gate TEXT, baggage INTEGER, meal TEXT);
"""

CREW_VIS = {
    "flight": [
        ('1','A1','2024-02-10','08:00','2024-02-11','20:00','Singapore','Paris'),
        ('2','A2','2024-02-11','09:00','2024-02-11','21:00','Tokyo','Paris'),
        ('3','A3','2024-02-11','10:00','2024-02-11','22:00','Sydney','London'),
        ('4','A4','2024-02-09','11:00','2024-02-11','19:00','Hong Kong','Dubai'),
        ('11','A5','2024-03-01','12:00','2024-03-02','23:00','Singapore','Paris'),
    ],
    "cabincrew": [
        (1,'1','Anna','Lee','111'),(2,'2','Ben','Tan','222'),(3,'1','Alex','Wong','333'),
        (4,'3','Amy','Chan','444'),(5,'11','Aiden','Kim','555'),(6,'4','Brian','Ong','666'),
    ],
    "passenger": [
        (101,'Anna','Lee','anna@x.com','111'),(102,'Ben','Tan','ben@x.com','222'),
        (103,'Chloe','Ng','chloe@x.com','333'),(104,'Derek','Goh','derek@x.com','444'),
        (105,'Ella','Fox','ella@x.com','555'),(106,'Felix','Ong','felix@x.com','666'),
        (107,'Grace','Kim','grace@x.com','777'),(108,'Hannah','Lim','hannah@x.com','888'),
    ],
    "boardingpass": [
        (1,'1',101,'A1',2,'Vegetarian'),(2,'1',102,'A2',1,'Non-Veg'),(3,'2',103,'B1',3,'Vegetarian'),
        (4,'3',104,'C1',1,'Vegetarian'),(5,'4',105,'D1',2,'Vegetarian'),(6,'4',106,'D2',1,'Non-Veg'),
        (7,'11',107,'E1',2,'Vegetarian'),(8,'4',108,'D3',1,'Vegetarian'),
    ],
}

CREW_HID = {
    "flight": [
        ('5','B1','2024-02-10','07:00','2024-02-11','18:00','Bangkok','Paris'),
        ('6','B2','2024-02-11','08:30','2024-02-11','19:30','Seoul','Paris'),
        ('7','B3','2024-02-11','09:15','2024-02-11','20:15','Cairo','Rome'),
        ('4','B4','2024-02-09','10:00','2024-02-11','17:00','Hong Kong','Doha'),
        ('21','B5','2024-06-01','11:00','2024-06-02','22:00','Bangkok','Paris'),
        ('31','B6','2024-07-01','12:00','2024-07-02','23:00','Seoul','Tokyo'),
    ],
    "cabincrew": [
        (1,'5','Aria','Sato','111'),(2,'21','Aaron','Lim','222'),(3,'31','Bella','Cruz','333'),
        (4,'31','Amit','Shah','444'),(5,'4','Ana','Cruz','555'),(6,'6','Chris','Wong','666'),
    ],
    "passenger": [
        (201,'Ivy','Chan','ivy@x.com','111'),(202,'Jack','Tan','jack@x.com','222'),
        (203,'Kira','Lee','kira@x.com','333'),(204,'Leo','Ng','leo@x.com','444'),
        (205,'Mia','Park','mia@x.com','555'),(206,'Noah','Kim','noah@x.com','666'),
    ],
    "boardingpass": [
        (1,'5',201,'A1',2,'Vegetarian'),(2,'5',202,'A2',3,'Non-Veg'),(3,'6',203,'B1',1,'Vegetarian'),
        (4,'7',204,'C1',2,'Vegetarian'),(5,'4',205,'D1',1,'Vegetarian'),(6,'4',206,'D2',2,'Non-Veg'),
    ],
}

Q19 = "SELECT c.cabincrew_id AS CabinCrew_ID, c.first_name AS First_Name, c.last_name AS Last_Name, c.contact AS Contact, f.flight_id AS Flight_ID FROM cabincrew c JOIN flight f ON c.flight_id = f.flight_id WHERE c.first_name LIKE 'A%' AND f.flight_id LIKE '%1' ORDER BY c.cabincrew_id;"
Q20 = "SELECT f.flight_id AS Flight_ID, COUNT(bp.passenger_id) AS Total_Passengers, SUM(bp.baggage) AS Total_Baggage FROM flight f JOIN boardingpass bp ON f.flight_id = bp.flight_id WHERE f.flight_to = 'Paris' AND f.arrival_date = '2024-02-11' GROUP BY f.flight_id ORDER BY f.flight_id;"
Q23 = "SELECT DISTINCT p.first_name AS FIRST_NAME, p.contact AS CONTACT FROM passenger p JOIN boardingpass bp ON p.passenger_id = bp.passenger_id JOIN flight f ON bp.flight_id = f.flight_id WHERE f.flight_from = 'Hong Kong' AND bp.flight_id = '4' AND bp.meal = 'Vegetarian' ORDER BY p.first_name;"

# =========================================================================
# CLUSTER: E-commerce (Q21, Q24)
# =========================================================================
ECOM_SCHEMA = """
CREATE TABLE category (category_id INTEGER PRIMARY KEY, code TEXT, name TEXT);
CREATE TABLE product (product_id INTEGER PRIMARY KEY, code TEXT, name TEXT, unit_price REAL);
CREATE TABLE product_category (product_category_id INTEGER PRIMARY KEY, product_id INTEGER, category_id INTEGER);
CREATE TABLE order_delivery (order_delivery_id INTEGER PRIMARY KEY, order_id INTEGER, tracking_no TEXT, status TEXT);
CREATE TABLE order_item (order_item_id INTEGER PRIMARY KEY, order_id INTEGER, order_delivery_id INTEGER, product_id INTEGER, quantity INTEGER);
CREATE TABLE ecom_customer (customer_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, address TEXT, phone TEXT, email TEXT);
CREATE TABLE payment (payment_id INTEGER PRIMARY KEY, order_id INTEGER, status TEXT, cctype TEXT, ccname TEXT, ccdate TEXT);
"""

ECOM_VIS = {
    "category": [(1,'C-WOM','Women'),(2,'C-MEN','Men'),(3,'C-KID','Kids')],
    "product": [(1,'P001','Floral Dress',49.99),(2,'P002','Denim Jacket',79.99),(3,'P003','Men Shirt',39.99),
                (4,'P004','Kids Tee',15.99),(5,'P005','Women Handbag',89.99)],
    "product_category": [(1,1,1),(2,2,1),(3,3,2),(4,4,3),(5,5,1)],
    "order_delivery": [(1,101,'TRK1','In the transit hub'),(2,102,'TRK2','Delivered'),
                        (3,103,'TRK3','In the transit hub'),(4,104,'TRK4','Processing')],
    "order_item": [(1,101,1,1,2),(2,102,2,3,1),(3,103,3,2,1),(4,104,4,4,3),(5,103,3,5,2)],
    "ecom_customer": [(1,'Nina','Patel','123 St','555-0001','nina@x.com'),(2,'Omar','Farouk','456 Ave','555-0002','omar@x.com')],
    "payment": [(1,101,'Paid','Visa','Nina Patel','2025-01-01'),(2,102,'Paid','MC','Omar Farouk','2025-01-02')],
}

ECOM_HID = {
    "category": [(1,'C-WOM','Women'),(2,'C-MEN','Men'),(3,'C-KID','Kids')],
    "product": [(11,'P101','Summer Dress',44.99),(12,'P102','Men Jeans',59.99),(13,'P103','Women Scarf',19.99),
                (14,'P104','Kids Shorts',12.99),(15,'P105','Men Jacket',99.99)],
    "product_category": [(11,11,1),(12,12,2),(13,13,1),(14,14,3),(15,15,2)],
    "order_delivery": [(11,201,'TRK11','In the transit hub'),(12,202,'TRK12','In the transit hub'),
                        (13,203,'TRK13','Delivered'),(14,204,'TRK14','Cancelled')],
    "order_item": [(11,201,11,11,1),(12,202,12,12,2),(13,203,13,13,1),(14,204,14,14,1),(15,201,11,15,1)],
    "ecom_customer": [(11,'Peter','Diaz','1 Rd','555-0011','peter@x.com'),(12,'Queenie','Flores','2 Rd','555-0012','queenie@x.com')],
    "payment": [(11,201,'Paid','Visa','Peter Diaz','2025-02-01'),(12,202,'Paid','MC','Queenie Flores','2025-02-02')],
}

Q21 = "SELECT COUNT(*) AS product_count FROM product p JOIN product_category pc ON p.product_id = pc.product_id JOIN category c ON pc.category_id = c.category_id WHERE c.name = 'Women';"
Q24 = "SELECT DISTINCT p.product_id AS product_id, p.name AS name FROM product p JOIN order_item oi ON p.product_id = oi.product_id JOIN order_delivery od ON oi.order_delivery_id = od.order_delivery_id WHERE od.status = 'In the transit hub' ORDER BY p.product_id;"

# =========================================================================
# CLUSTER: Ride-hailing (Q27, Q28)
# =========================================================================
RIDE_SCHEMA = """
CREATE TABLE driver (driver_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, license_number TEXT, rating REAL);
CREATE TABLE vehicle (vehicle_id INTEGER PRIMARY KEY, driver_id INTEGER, plate_number TEXT, status TEXT);
CREATE TABLE booking (booking_id INTEGER PRIMARY KEY, vehicle_id INTEGER, status TEXT);
"""

RIDE_VIS = {
    "driver": [(1,'Raj','Kumar','LIC001',4.8),(2,'Simran','Kaur','LIC002',4.2),(3,'Tariq','Ali','LIC003',4.6),(4,'Uma','Devi','LIC004',3.9)],
    "vehicle": [(1,1,'KA01AB1230','In Use'),(2,2,'KA02CD4560','Idle'),(3,3,'KA03EF7890','In Use'),(4,4,'KA04GH1111','In Use')],
    "booking": [(1,1,'Completed'),(2,1,'Cancelled'),(3,2,'Completed'),(4,3,'Completed'),(5,4,'Cancelled'),(6,4,'Completed')],
}

RIDE_HID = {
    "driver": [(11,'Vikram','Shetty','LIC011',4.9),(12,'Wanda','Fernandes','LIC012',4.0),(13,'Xena','Rodrigues','LIC013',4.5),(14,'Yusuf','Sheikh','LIC014',3.5)],
    "vehicle": [(11,11,'MH12AB2340','In Use'),(12,12,'MH12CD5670','In Use'),(13,13,'MH12EF8900','Idle'),(14,14,'MH12GH1121','In Use')],
    "booking": [(11,11,'Completed'),(12,11,'Completed'),(13,12,'Cancelled'),(14,13,'Completed'),(15,14,'Cancelled'),(16,14,'Completed')],
}

Q27 = "SELECT d.first_name || ' ' || d.last_name AS Name, d.license_number AS License_Number, v.plate_number AS Plate_Number FROM driver d JOIN vehicle v ON d.driver_id = v.driver_id WHERE v.status = 'In Use' AND v.plate_number LIKE '%0' ORDER BY d.driver_id;"
Q28 = "SELECT d.license_number AS License_Number, v.vehicle_id AS Vehicle_ID, d.rating AS Rating, b.booking_id AS Booking_ID FROM driver d JOIN vehicle v ON d.driver_id = v.driver_id JOIN booking b ON v.vehicle_id = b.vehicle_id WHERE d.rating >= 4.5 AND b.status <> 'Cancelled' ORDER BY b.booking_id;"

# =========================================================================
# STANDALONE: Q6 books
# =========================================================================
BOOKS_SCHEMA = "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT, price REAL, isbn TEXT, published_date TEXT, category TEXT);"
BOOKS_VIS = {"books": [
    (1,'Intro to Algorithms',65.00,'ISBN001','1945-06-01','C102'),
    (2,'Ancient History',20.00,'ISBN002','1935-01-01','C102'),
    (3,'Modern Physics',55.00,'ISBN003','1950-03-03','C101'),
    (4,'Data Structures',45.00,'ISBN004','1999-09-09','C102'),
    (5,'World War History',30.00,'ISBN005','1938-01-01','C102'),
]}
BOOKS_HID = {"books": [
    (11,'Calculus Basics',40.00,'ISBN011','1960-01-01','C102'),
    (12,'Old Legends',15.00,'ISBN012','1920-01-01','C102'),
    (13,'Chemistry 101',35.00,'ISBN013','1970-01-01','C103'),
    (14,'Statistics Handbook',50.00,'ISBN014','1985-05-05','C102'),
]}
Q6 = "SELECT title AS Title, price AS Price, isbn AS ISBN FROM books WHERE published_date > '1940-01-01' AND category = 'C102' ORDER BY book_id;"

# =========================================================================
# STANDALONE: Q7 channelscategory
# =========================================================================
CHAN_SCHEMA = "CREATE TABLE channelscategory (categoryid INTEGER PRIMARY KEY, categoryname TEXT);"
CHAN_VIS = {"channelscategory": [(1,'Music'),(2,'Movies'),(3,'Sports'),(4,'Mystery'),(5,'News')]}
CHAN_HID = {"channelscategory": [(11,'Mythology'),(12,'Nature'),(13,'Motoring'),(14,'Cartoons'),(15,'Weather')]}
Q7 = "SELECT categoryid AS CATEGORYID, categoryname AS CATEGORYNAME FROM channelscategory WHERE categoryname LIKE 'M%' ORDER BY categoryid;"

# =========================================================================
# STANDALONE: Q14 staff
# =========================================================================
STAFF_SCHEMA = "CREATE TABLE staff (staff_id INTEGER PRIMARY KEY, firstname TEXT, position TEXT, salary REAL);"
STAFF_VIS = {"staff": [(1,'Nora','Manager',65000),(2,'Owen','Clerk',32000),(3,'Priya','Supervisor',55000),(4,'Quinn','Clerk',30000),(5,'Ravi','Director',90000)]}
STAFF_HID = {"staff": [(11,'Sara','Manager',48000),(12,'Tom','Director',85000),(13,'Uma','Supervisor',52000),(14,'Vik','Clerk',28000)]}
Q14 = "SELECT firstname AS \"STAFF FIRST NAME\", position AS \"POSITION\", salary AS \"SALARY\" FROM staff WHERE salary > 50000 ORDER BY staff_id;"

# =========================================================================
# STANDALONE: Q15/16 hospital
# =========================================================================
HOSP_SCHEMA = """
CREATE TABLE Patient (PatientID INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Email TEXT, AdmissionDate TEXT);
CREATE TABLE Billing (BillingID INTEGER PRIMARY KEY, PatientID INTEGER, TotalAmount REAL, PaymentStatus TEXT);
"""
HOSP_VIS = {
    "Patient": [(1,'John','Doe','john@x.com','2025-01-10'),(2,'Jane','Smith','jane@x.com','2025-02-15'),
                (3,'Sam','Lee','sam@x.com','2025-03-20'),(4,'Amy','Wong','amy@x.com','2025-04-25')],
    "Billing": [(1,1,1500.00,'Unpaid'),(2,2,2500.00,'Paid'),(3,3,3200.00,'Unpaid'),(4,4,900.00,'Unpaid')],
}
HOSP_HID = {
    "Patient": [(11,'Mark','Twain','mark@x.com','2025-05-01'),(12,'Nora','Jones','nora@x.com','2025-05-15'),
                (13,'Omar','Farid','omar@x.com','2025-06-01'),(14,'Pia','Kumar','pia@x.com','2025-06-20')],
    "Billing": [(11,11,4200.00,'Unpaid'),(12,12,1100.00,'Paid'),(13,13,3300.00,'Unpaid'),(14,14,700.00,'Unpaid')],
}
Q15 = "SELECT p.FirstName || ' ' || p.LastName AS PatientName, p.Email AS PatientEmail, p.AdmissionDate AS AdmissionDate, b.TotalAmount AS TotalBilling FROM Patient p JOIN Billing b ON p.PatientID = b.PatientID WHERE b.PaymentStatus = 'Unpaid' ORDER BY b.TotalAmount DESC;"

# =========================================================================
# STANDALONE: Q25 artist
# =========================================================================
ARTIST_SCHEMA = "CREATE TABLE artist (artist_id INTEGER PRIMARY KEY, name TEXT);"
ARTIST_VIS = {"artist": [(1,'Beethoven'),(2,'Blink182'),(3,'Adele'),(4,'U2'),(5,'Eminem')]}
ARTIST_HID = {"artist": [(11,'Sum41'),(12,'Coldplay'),(13,'Maroon5'),(14,'Adele'),(15,'Drake')]}
Q25 = "SELECT artist_id AS ARTIST_ID, name AS NAME FROM artist WHERE name LIKE '%0%' OR name LIKE '%1%' OR name LIKE '%2%' OR name LIKE '%3%' OR name LIKE '%4%' OR name LIKE '%5%' OR name LIKE '%6%' OR name LIKE '%7%' OR name LIKE '%8%' OR name LIKE '%9%' ORDER BY artist_id;"

# =========================================================================
# STANDALONE: Q26 message
# =========================================================================
MSG_SCHEMA = "CREATE TABLE message (message_id INTEGER PRIMARY KEY, content TEXT);"
MSG_VIS = {"message": [(1,'Hello world'),(2,'Good morning'),(3,'Hello there'),(4,'See you later'),(5,'hello again')]}
MSG_HID = {"message": [(11,'Hello team'),(12,'Meeting notes'),(13,'well hello there'),(14,'Random text'),(15,'HELLO ALL')]}
Q26 = "SELECT message_id AS MESSAGE_ID, content AS CONTENT FROM message WHERE content LIKE '%Hello%' ORDER BY message_id;"

# =========================================================================
# STANDALONE: Q29 viewer
# =========================================================================
VIEWER_SCHEMA = "CREATE TABLE viewer (viewer_id INTEGER PRIMARY KEY, viewername TEXT);"
VIEWER_VIS = {"viewer": [(1,'John'),(2,'Mary'),(3,'John'),(4,'Steve'),(5,'Mary'),(6,'Mary')]}
VIEWER_HID = {"viewer": [(11,'Alice'),(12,'Bob'),(13,'Alice'),(14,'Carol'),(15,'Bob'),(16,'Alice'),(17,'Dave')]}
Q29 = "SELECT viewername AS viewername, COUNT(*) AS name_count FROM viewer GROUP BY viewername ORDER BY viewername;"

# =========================================================================
# STANDALONE: Q30 users/contacts/jobs
# =========================================================================
USERS_SCHEMA = """
CREATE TABLE users (user_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT);
CREATE TABLE contacts (user_id INTEGER, contact_id INTEGER);
CREATE TABLE jobs (user_id INTEGER, job_title TEXT);
"""
USERS_VIS = {
    "users": [(1,'John','Doe'),(2,'Jane','Engineer'),(3,'Sam','Lee'),(4,'Amy','Wong'),(5,'Bob','Marley'),(6,'Cara','Kim')],
    "jobs": [(1,'Doctor'),(2,'Software Engineer'),(3,'Teacher'),(4,'Mechanical Engineer'),(5,'Artist'),(6,'Engineer')],
    "contacts": [(1,2),(3,1),(5,4),(1,3),(6,5)],
}
USERS_HID = {
    "users": [(11,'Tom','Hardy'),(12,'Uma','Patel'),(13,'Vik','Rao'),(14,'Wendy','Chu'),(15,'Xavier','Diaz'),(16,'Yara','Osei')],
    "jobs": [(11,'Nurse'),(12,'Civil Engineer'),(13,'Chef'),(14,'Engineer'),(15,'Pilot'),(16,'Data Engineer')],
    "contacts": [(11,12),(13,11),(15,14),(16,13)],
}
Q30 = "SELECT DISTINCT u.first_name || ' ' || u.last_name AS FULLNAME FROM users u JOIN contacts c ON u.user_id = c.user_id JOIN users cu ON c.contact_id = cu.user_id JOIN jobs j ON cu.user_id = j.user_id WHERE j.job_title LIKE '%Engineer%' ORDER BY FULLNAME;"



ACCENTURE_CODING_PDF_PROBLEMS = [

    # 3001. Absolute Difference
    {
        "id": 3001,
        "slug": "absolute-difference",
        "title": "Absolute Difference Count",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer array <code>arr</code> and two integers <code>num</code> and <code>diff</code>,
find the number of elements of <code>arr</code> whose absolute difference with <code>num</code> is
less than or equal to <code>diff</code>.</p>
<p>If no such element exists, print <code>-1</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>num</code>. Line 4: <code>diff</code>.</p>
<h3>Example:</h3>
<pre>Input:              Output:
6                    3
12 3 14 56 77 13
13
2</pre>
<p>Explanation: 12, 13 and 14 have an absolute difference &lt;= 2 with 13.</p>
""",
        "hint": "Loop through the array and count elements where Math.abs(num - arr[i]) <= diff. Return -1 if the count is 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int num = sc.nextInt();
        int diff = sc.nextInt();

        // TODO: count elements with |num - arr[i]| <= diff, return -1 if none
        int count = 0;

        System.out.println(count > 0 ? count : -1);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\nnum = read_int()\ndiff = read_int()\n\n# TODO: count elements with |num - arr[i]| <= diff, return -1 if none\ncount = 0\n\nprint(count if count > 0 else -1)",
        },
        "tests": [
            {"input": "6\n12 3 14 56 77 13\n13\n2", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3002. Anagram Check
    {
        "id": 3002,
        "slug": "anagram-check",
        "title": "Anagram Check",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given two strings <code>s</code> and <code>t</code>, determine whether the characters of
<code>s</code> can be rearranged to form <code>t</code>.</p>
<p>Print <code>True</code> if possible, otherwise print <code>False</code> (comparison is case-insensitive).</p>
<h3>Input format:</h3>
<p>Line 1: <code>s</code>. Line 2: <code>t</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
listen      True
silent</pre>
""",
        "hint": "Lowercase both strings, sort their characters, and compare the sorted arrays for equality.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String t = sc.nextLine();

        // TODO: check if s and t are anagrams (case-insensitive)
        boolean isAnagram = false;

        System.out.println(isAnagram ? "True" : "False");
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\nt = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: check if s and t are anagrams (case-insensitive)\nis_anagram = False\n\nprint(\"True\" if is_anagram else \"False\")",
        },
        "tests": [
            {"input": "listen\nsilent", "expected": "True", "hidden": False},
        ],
        "samples": [0],
    },

    # 3003. Autobiographical Number
    {
        "id": 3003,
        "slug": "autobiographical-number",
        "title": "Autobiographical Number",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>A number <code>N</code> (given as a digit string) is <b>autobiographical</b> if, for every position
<code>i</code> (0-indexed), the digit at position <code>i</code> equals the count of how many times the
digit <code>i</code> appears in <code>N</code>.</p>
<p>If <code>N</code> is autobiographical, print the count of <b>distinct</b> digits used in <code>N</code>.
Otherwise print <code>0</code>.</p>
<h3>Input format:</h3>
<p>A single line containing the digit string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1210        3</pre>
<p>Explanation: position 0 has value 1 = count of 0s in "1210" (one 0). Position 1 has value 2 = count of
1s (two 1s). Position 2 has value 1 = count of 2s (one 2). Position 3 has value 0 = count of 3s (zero).
It is autobiographical, and the distinct digits used are {0,1,2} = 3.</p>
""",
        "hint": "Build a frequency array of digits 0-9 first, then check position-by-position that the digit at i equals freq[i]. If it all checks out, count distinct characters in the string.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine().trim();

        // TODO: check if n is autobiographical, print distinct digit count or 0
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\nn = sys.stdin.readline().strip()\n\n# TODO: check if n is autobiographical, print distinct digit count or 0\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "1210", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3004. Binary Operations
    {
        "id": 3004,
        "slug": "binary-operations",
        "title": "Binary Operations",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>You are given a string made of binary digits ('0'/'1') separated by operator letters:
<code>A</code> = AND, <code>B</code> = OR, <code>C</code> = XOR.</p>
<p>Scanning left to right, apply each operation in order (no operator precedence) starting from the
first digit, and print the final integer result.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input:                 Output:
1C0C1C1A0B1            1</pre>
<p>Explanation: 1 XOR 0 XOR 1 XOR 1 AND 0 OR 1 = 1, evaluated strictly left to right.</p>
""",
        "hint": "The string alternates digit, operator, digit, operator, ... Start with the first digit as the running result, then for each (operator, digit) pair apply &, | or ^ in order.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();

        // TODO: scan left to right applying A=AND, B=OR, C=XOR
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\ns = sys.stdin.readline().strip()\n\n# TODO: scan left to right applying A=AND, B=OR, C=XOR\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "1C0C1C1A0B1", "expected": "1", "hidden": False},
            {"input": "0C1A1B1C1C1B0A0", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3005. Binary to Decimal
    {
        "id": 3005,
        "slug": "binary-to-decimal",
        "title": "Binary to Decimal",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a number made up only of binary digits (e.g. <code>1010</code>), print its decimal value.</p>
<h3>Input format:</h3>
<p>A single line containing the binary digits.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1010        10</pre>
""",
        "hint": "Read each digit from the right, multiplying by increasing powers of 2 and summing them up.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        // TODO: convert binary-digit number n to its decimal value
        int decimal = 0;

        System.out.println(decimal);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: convert binary-digit number n to its decimal value\ndecimal = 0\n\nprint(decimal)",
        },
        "tests": [
            {"input": "1010", "expected": "10", "hidden": False},
        ],
        "samples": [0],
    },

    # 3006. Bulb Switch
    {
        "id": 3006,
        "slug": "bulb-switch",
        "title": "Bulb Switch",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Greedy"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p><code>N</code> light bulbs are connected in a row. Pressing the switch of bulb <code>i</code> flips
bulb <code>i</code> itself and every bulb to its right (0 becomes 1, 1 becomes 0).</p>
<p>Given the initial 0/1 state array, find the minimum number of switch presses needed to turn
<b>all</b> bulbs on.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated 0/1 values.</p>
<h3>Example:</h3>
<pre>Input:      Output:
4           4
0 1 0 1</pre>
""",
        "hint": "Scan left to right. Whenever you hit a bulb that is currently 0, you must press its switch: flip it and everything to its right, and count the press. This greedy left-to-right simulation gives the minimum presses.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: greedily press switches left to right whenever a bulb is off
        int count = 0;

        System.out.println(count);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: greedily press switches left to right whenever a bulb is off\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "4\n0 1 0 1", "expected": "4", "hidden": False},
            {"input": "5\n1 0 0 0 0", "expected": "1", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3007. Chocolate Distribution
    {
        "id": 3007,
        "slug": "chocolate-distribution",
        "title": "Chocolate Distribution",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting", "Greedy"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array of chocolate packet sizes and an integer <code>m</code> (number of students),
distribute exactly <code>m</code> packets, one per student, so that the difference between the
largest and smallest packet given out is minimized. Print that minimum difference.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>m</code>.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       2
7 3 2 4 9 12 56
3</pre>
""",
        "hint": "Sort the array, then slide a window of size m across it, tracking the minimum of (window's last element - window's first element).",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int m = sc.nextInt();

        // TODO: sort arr, slide a window of size m, find the minimum (max-min) in any window
        int minDiff = 0;

        System.out.println(minDiff);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\nm = read_int()\n\n# TODO: sort arr, slide a window of size m, find the minimum (max-min) in any window\nmin_diff = 0\n\nprint(min_diff)",
        },
        "tests": [
            {"input": "7\n7 3 2 4 9 12 56\n3", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3008. Count Carry
    {
        "id": 3008,
        "slug": "count-carry",
        "title": "Count Carry Operations",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given two non-negative integers, count how many carries occur when adding them digit by digit
from right to left (elementary school addition).</p>
<h3>Input format:</h3>
<p>Line 1: <code>num1</code>. Line 2: <code>num2</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
451         2
349</pre>
""",
        "hint": "Repeatedly take the last digit of each number plus any carry from the previous step; if the sum exceeds 9, that's a carry.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int no1 = sc.nextInt();
        int no2 = sc.nextInt();

        // TODO: count carries produced while adding no1 + no2 digit by digit
        int count = 0;

        System.out.println(count);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nno1 = read_int()\nno2 = read_int()\n\n# TODO: count carries produced while adding no1 + no2 digit by digit\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "451\n349", "expected": "2", "hidden": False},
            {"input": "23\n563", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3009. Decimal to Binary
    {
        "id": 3009,
        "slug": "decimal-to-binary",
        "title": "Decimal to Binary",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a decimal integer <code>n</code>, print its binary representation (no leading zeros, and
<code>0</code> for input <code>0</code>).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
10          1010</pre>
""",
        "hint": "Repeatedly take n & 1 to get the next binary digit and shift n right by 1, then reverse the collected digits.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: convert n to its binary representation (string of 0/1)
        String binary = "0";

        System.out.println(binary);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: convert n to its binary representation (string of 0/1)\nbinary = \"0\"\n\nprint(binary)",
        },
        "tests": [
            {"input": "10", "expected": "1010", "hidden": False},
        ],
        "samples": [0],
    },

    # 3010. Palindrome Numbers in Range
    {
        "id": 3010,
        "slug": "palindrome-numbers-in-range",
        "title": "Palindrome Numbers in Range",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a lower bound and an upper bound (inclusive), print all palindrome numbers in that range,
space-separated, in increasing order.</p>
<h3>Input format:</h3>
<p>Line 1: <code>lower</code>. Line 2: <code>upper</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
10          11 22 33 44 55 66 77
80</pre>
""",
        "hint": "For each number in [lower, upper], reverse its digits and check if the reversed number equals the original.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lower = sc.nextInt();
        int upper = sc.nextInt();

        // TODO: print all palindrome numbers in [lower, upper], space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nlower = read_int()\nupper = read_int()\n\n# TODO: print all palindrome numbers in [lower, upper], space separated\nresult = []\n\nprint(\" \".join(result))",
        },
        "tests": [
            {"input": "10\n80", "expected": "11 22 33 44 55 66 77", "hidden": False},
            {"input": "100\n200", "expected": "101 111 121 131 141 151 161 171 181 191", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3011. Sum of Distances Between Three Points
    {
        "id": 3011,
        "slug": "sum-of-distances-three-points",
        "title": "Sum of Distances Between Three Points",
        "difficulty": "Easy",
        "topics": [T, "Math", "Geometry"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given three points <code>(x1,y1)</code>, <code>(x2,y2)</code>, <code>(x3,y3)</code>, compute the sum
of the three pairwise Euclidean distances (P1-P2 + P2-P3 + P1-P3), rounded to 2 decimal places.</p>
<h3>Input format:</h3>
<p>A single line with six space-separated numbers: <code>x1 y1 x2 y2 x3 y3</code>.</p>
<h3>Example:</h3>
<pre>Input:              Output:
1 1 2 4 3 6         10.78</pre>
""",
        "hint": "distance(P,Q) = sqrt((qx-px)^2 + (qy-py)^2). Sum all three pairwise distances and format with two decimal places.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x1 = sc.nextDouble(), y1 = sc.nextDouble();
        double x2 = sc.nextDouble(), y2 = sc.nextDouble();
        double x3 = sc.nextDouble(), y3 = sc.nextDouble();

        // TODO: sum the three pairwise distances between the points
        double sum = 0.0;

        System.out.printf("%.2f%n", sum);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nx1 = float(_data[_idx]); _idx += 1\ny1 = float(_data[_idx]); _idx += 1\nx2 = float(_data[_idx]); _idx += 1\ny2 = float(_data[_idx]); _idx += 1\nx3 = float(_data[_idx]); _idx += 1\ny3 = float(_data[_idx]); _idx += 1\n\n# TODO: sum the three pairwise distances between the points\ntotal = 0.0\n\nprint(\"%.2f\" % total)",
        },
        "tests": [
            {"input": "1 1 2 4 3 6", "expected": "10.78", "hidden": False},
        ],
        "samples": [0],
    },

    # 3012. Count Occurrences
    {
        "id": 3012,
        "slug": "count-occurrences-array",
        "title": "Count Occurrences (First-Appearance Order)",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, print the number of occurrences of each distinct value, one per line, in the
format <code>value - count</code>, ordered by each value's first appearance in the array.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       10 - 3
10 5 10 15 10 5         5 - 2
                        15 - 1</pre>
""",
        "hint": "Use a LinkedHashMap (or equivalent) to preserve first-insertion order while counting frequencies.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: print "value - count" per distinct value, in first-appearance order
        StringBuilder sb = new StringBuilder();

        System.out.print(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: print \"value - count\" per distinct value, in first-appearance order\nlines = []\n\nprint(\"\\n\".join(lines))",
        },
        "tests": [
            {"input": "6\n10 5 10 15 10 5", "expected": "10 - 3\n5 - 2\n15 - 1", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3013. Elevation Point
    {
        "id": 3013,
        "slug": "elevation-point",
        "title": "Elevation Point (Peak Value)",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Binary Search"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, find a "peak" value: an element that is strictly greater than both its neighbors
(or greater than its only neighbor, at either edge). Print that peak's <b>value</b>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       4
1 2 3 4 3 2 1</pre>
""",
        "hint": "Scan the array; an index i is a peak if (i==0 or arr[i]>arr[i-1]) and (i==n-1 or arr[i]>arr[i+1]). Print arr[i] for the first such i found.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find a peak element (value strictly greater than its neighbors) and print its value
        int peak = arr[0];

        System.out.println(peak);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find a peak element (value strictly greater than its neighbors) and print its value\npeak = arr[0]\n\nprint(peak)",
        },
        "tests": [
            {"input": "7\n1 2 3 4 3 2 1", "expected": "4", "hidden": False},
            {"input": "2\n5 3", "expected": "5", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3014. Encode Number
    {
        "id": 3014,
        "slug": "encode-number",
        "title": "Encode Number",
        "difficulty": "Easy",
        "topics": [T, "Math", "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer <code>N</code>, square each of its digits and concatenate the resulting decimal
strings to form the encoded number. Print the encoded number.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
34          916</pre>
<p>Explanation: 3^2 = 9, 4^2 = 16, concatenated: "9" + "16" = "916".</p>
""",
        "hint": "Process digits from the right, squaring each and prepending the square's decimal string to the accumulated result.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: square each digit of n and concatenate the results
        long encoded = 0;

        System.out.println(encoded);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: square each digit of n and concatenate the results\nencoded = 0\n\nprint(encoded)",
        },
        "tests": [
            {"input": "34", "expected": "916", "hidden": False},
        ],
        "samples": [0],
    },

    # 3015. Equilibrium Sum
    {
        "id": 3015,
        "slug": "equilibrium-sum",
        "title": "Equilibrium Index",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer array, find the index where the sum of elements strictly to its left equals the
sum of elements strictly to its right. Print that index, or <code>-1</code> if none exists.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   2
3 4 3 1 6</pre>
<p>Explanation: at index 2, left sum = 3+4 = 7 and right sum = 1+6 = 7.</p>
""",
        "hint": "Compute the total sum first. Then walk left to right tracking leftSum, and compute rightSum = total - leftSum - arr[i] at each index.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the equilibrium index (left sum == right sum), else -1
        int result = -1;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find the equilibrium index (left sum == right sum), else -1\nresult = -1\n\nprint(result)",
        },
        "tests": [
            {"input": "5\n3 4 3 1 6", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3016. Find the Missing Number
    {
        "id": 3016,
        "slug": "find-the-missing-number",
        "title": "Find the Missing Number",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>An array contains <code>n</code> distinct integers taken from the range <code>1</code> to
<code>n+1</code>, with exactly one number missing. Find and print the missing number.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code> (length of the given array). Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   3
1 2 4 5 6</pre>
""",
        "hint": "The full range 1..n+1 sums to (n+1)(n+2)/2. Subtract the actual array sum to get the missing number.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the missing number from range 1..n+1
        long missing = 0;

        System.out.println(missing);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find the missing number from range 1..n+1\nmissing = 0\n\nprint(missing)",
        },
        "tests": [
            {"input": "5\n1 2 4 5 6", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3017. First K Words
    {
        "id": 3017,
        "slug": "first-k-words",
        "title": "First K Words",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a sentence and an integer <code>k</code>, print the first <code>k</code> words of the
sentence, space-separated. If <code>k</code> is greater than or equal to the number of words, print
the whole sentence unchanged (trimmed).</p>
<h3>Input format:</h3>
<p>Line 1: the sentence. Line 2: <code>k</code>.</p>
<h3>Example:</h3>
<pre>Input:                              Output:
Hello I am a passionate developer   Hello I am a
4</pre>
""",
        "hint": "Split the sentence on whitespace and join the first k tokens with single spaces.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int k = Integer.parseInt(sc.nextLine().trim());

        // TODO: print the first k words of line, space separated
        System.out.println(line.trim());
    }
}""", "python": "import sys\nline = sys.stdin.readline().rstrip(\"\\n\")\nk = int(sys.stdin.readline().strip())\n\n# TODO: print the first k words of line, space separated\nprint(line.strip())",
        },
        "tests": [
            {"input": "Hello I am a passionate developer\n4", "expected": "Hello I am a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3018. Floyd's Triangle
    {
        "id": 3018,
        "slug": "floyds-triangle",
        "title": "Floyd's Triangle",
        "difficulty": "Easy",
        "topics": [T, "Math", "Patterns"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Print Floyd's Triangle with <code>n</code> rows: row <code>i</code> (1-indexed) contains
<code>i</code> numbers, continuing a running counter that starts at 1. Numbers in a row are
space-separated, and each row is on its own line.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 4        Output:
                 1
                 2 3
                 4 5 6
                 7 8 9 10</pre>
""",
        "hint": "Keep a running counter starting at 1. For row i, print i numbers from the counter, incrementing it each time.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print Floyd's triangle with n rows
        System.out.println();
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: print Floyd's triangle with n rows\nprint()",
        },
        "tests": [
            {"input": "4", "expected": "1\n2 3\n4 5 6\n7 8 9 10", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3019. Googly Prime Number
    {
        "id": 3019,
        "slug": "googly-prime-number",
        "title": "Googly Prime Number",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>A number is called "googly prime" if the sum of its digits is a prime number. Given an integer,
print <code>YES</code> if it is a googly prime, otherwise print <code>NO</code>.</p>
<h3>Input format:</h3>
<p>A single integer.</p>
<h3>Example:</h3>
<pre>Input:      Output:
43          YES</pre>
<p>Explanation: 4+3 = 7, which is prime.</p>
""",
        "hint": "Sum the digits, then check if the sum is prime with a simple trial-division check up to sqrt(sum).",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum digits of n, print YES if the sum is prime, else NO
        System.out.println("NO");
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: sum digits of n, print YES if the sum is prime, else NO\nprint(\"NO\")",
        },
        "tests": [
            {"input": "43", "expected": "YES", "hidden": False},
            {"input": "123", "expected": "NO", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3020. Intersection of Two Arrays
    {
        "id": 3020,
        "slug": "intersection-of-two-arrays",
        "title": "Intersection of Two Sorted Arrays",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Two Pointers"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given two arrays that are already sorted in non-decreasing order, print their intersection
(matching elements found via a two-pointer merge scan — duplicates are included exactly as many
times as the two-pointer walk matches them), space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n1</code>. Line 2: <code>n1</code> sorted integers. Line 3: <code>n2</code>. Line 4:
<code>n2</code> sorted integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   2 2 3
1 2 2 3 4
4
2 2 3 5</pre>
""",
        "hint": "Use two pointers i, j starting at 0. If arr1[i]==arr2[j] add it and advance both; if arr1[i]<arr2[j] advance i; else advance j.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int[] a1 = new int[n1];
        for (int i = 0; i < n1; i++) a1[i] = sc.nextInt();
        int n2 = sc.nextInt();
        int[] a2 = new int[n2];
        for (int i = 0; i < n2; i++) a2[i] = sc.nextInt();

        // TODO: two-pointer intersection of the two sorted arrays
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn1 = read_int()\na1 = [read_int() for _ in range(n1)]\nn2 = read_int()\na2 = [read_int() for _ in range(n2)]\n\n# TODO: two-pointer intersection of the two sorted arrays\nresult = []\n\nprint(\" \".join(str(x) for x in result))",
        },
        "tests": [
            {"input": "5\n1 2 2 3 4\n4\n2 2 3 5", "expected": "2 2 3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3021. Large Small Sum
    {
        "id": 3021,
        "slug": "large-small-sum",
        "title": "Large Small Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array (with all unique elements), split it into the elements at even 0-indexed positions
and the elements at odd 0-indexed positions. Print the sum of the <b>2nd-largest</b> element among the
even-position group and the <b>2nd-smallest</b> element among the odd-position group.</p>
<p>If the array has 3 or fewer elements (or is empty), print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       7
3 2 1 7 5 4</pre>
<p>Explanation: even positions (0,2,4) = [3,1,5], sorted [1,3,5], 2nd largest = 3. Odd positions
(1,3,5) = [2,7,4], sorted [2,4,7], 2nd smallest = 4. Sum = 3 + 4 = 7.</p>
""",
        "hint": "Split by index parity into two lists, sort each ascending. 2nd largest of the even list is at index size-2; 2nd smallest of the odd list is at index 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd largest of even-index elements + 2nd smallest of odd-index elements
        int result = (n <= 3) ? 0 : 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: 2nd largest of even-index elements + 2nd smallest of odd-index elements\nresult = 0 if n <= 3 else 0\n\nprint(result)",
        },
        "tests": [
            {"input": "6\n3 2 1 7 5 4", "expected": "7", "hidden": False},
            {"input": "7\n1 8 0 2 3 5 6", "expected": "8", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3022. Length of Last Word
    {
        "id": 3022,
        "slug": "length-of-last-word",
        "title": "Length of Last Word",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string possibly containing multiple/leading/trailing spaces, print the length of the
<b>last</b> word.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: " I am  a passionate   Developer  "     Output: 9</pre>
""",
        "hint": "Trim the string, split on one-or-more whitespace characters, and take the length of the last resulting token.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: find the length of the last word in s
        int length = 0;

        System.out.println(length);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: find the length of the last word in s\nlength = 0\n\nprint(length)",
        },
        "tests": [
            {"input": " I am  a passionate   Developer  ", "expected": "9", "hidden": False},
        ],
        "samples": [0],
    },

    # 3023. Linked List Palindrome
    {
        "id": 3023,
        "slug": "linked-list-palindrome",
        "title": "Linked List Palindrome",
        "difficulty": "Easy",
        "topics": [T, "Linked List"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given <code>n</code> values used to build a singly linked list in order, print <code>true</code>
if the list is a palindrome, otherwise print <code>false</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers (the list values, head to tail).</p>
<h3>Example:</h3>
<pre>Input:          Output:
4               true
1 2 2 1</pre>
""",
        "hint": "Build the linked list, then walk it collecting values into a list, and check the value list reads the same forwards and backwards.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    static class Node { int val; Node next; Node(int v) { val = v; } }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Node head = null, tail = null;
        for (int i = 0; i < n; i++) {
            int v = sc.nextInt();
            Node node = new Node(v);
            if (head == null) { head = node; tail = node; }
            else { tail.next = node; tail = node; }
        }

        // TODO: check if the linked list starting at head is a palindrome
        boolean isPalindrome = false;

        System.out.println(isPalindrome);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: check if the linked list represented by arr is a palindrome\nis_palindrome = False\n\nprint(str(is_palindrome).lower())",
        },
        "tests": [
            {"input": "4\n1 2 2 1", "expected": "true", "hidden": False},
        ],
        "samples": [0],
    },

    # 3024. Longest Substring Without Repeating Characters
    {
        "id": 3024,
        "slug": "longest-substring-without-repeat",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Sliding Window", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string <code>s</code>, find the length of the longest substring without repeating
characters.</p>
<h3>Input format:</h3>
<p>A single line containing <code>s</code>.</p>
<h3>Example:</h3>
<pre>Input: abcabcbb     Output: 3</pre>
""",
        "hint": "Use a sliding window with a set of characters currently in the window: expand the right edge, and shrink the left edge whenever you'd introduce a duplicate.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: length of the longest substring of s without repeating characters
        int maxLen = 0;

        System.out.println(maxLen);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: length of the longest substring of s without repeating characters\nmax_len = 0\n\nprint(max_len)",
        },
        "tests": [
            {"input": "abcabcbb", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3025. Longest Word
    {
        "id": 3025,
        "slug": "longest-word",
        "title": "Longest Word in a Sentence",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a line of space-separated words, print the longest one in the exact format
<code>The longest string is: &lt;word&gt;</code>.</p>
<h3>Input format:</h3>
<p>A single line of words.</p>
<h3>Example:</h3>
<pre>Input: yes no number     Output: The longest string is: number</pre>
""",
        "hint": "Split on whitespace, then scan for the word with the maximum length.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        // TODO: find the longest word in line
        String longest = "";

        System.out.println("The longest string is: " + longest);
    }
}""", "python": "import sys\nline = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: find the longest word in line\nlongest = \"\"\n\nprint(\"The longest string is: \" + longest)",
        },
        "tests": [
            {"input": "yes no number", "expected": "The longest string is: number", "hidden": False},
        ],
        "samples": [0],
    },

    # 3026. Magical Numbers
    {
        "id": 3026,
        "slug": "magical-numbers",
        "title": "Count Magical Numbers",
        "difficulty": "Medium",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>For a number, count how many even bits (i.e. 0-bits) appear in its binary representation. The
number is "magical" if that count of 0-bits is odd. Given <code>N</code>, print the count of magical
numbers in <code>[1, N]</code>.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 5     Output: 2</pre>
""",
        "hint": "For each number from 1 to N, count how many of its binary digits are 0 (using repeated division by 2), and check if that count is odd.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count numbers in [1,n] whose binary form has an odd count of 0-bits
        int count = 0;

        System.out.println(count);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: count numbers in [1,n] whose binary form has an odd count of 0-bits\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "5", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3027. Matrix Even Odd Split Sum
    {
        "id": 3027,
        "slug": "matrix-even-odd-split-sum",
        "title": "Even/Odd Position Split Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, split it into elements at even 0-indexed positions and elements at odd 0-indexed
positions. Sort each group ascending, then print the sum of the <b>2nd-largest</b> element of each
group.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   7
3 4 1 7 9</pre>
<p>Explanation: even positions [3,1,9] sorted [1,3,9], 2nd largest = 3. Odd positions [4,7] sorted
[4,7], 2nd largest = 4. Sum = 7.</p>
""",
        "hint": "Split by index parity, sort each list ascending, and take the element at index size-2 (the 2nd largest) from each.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "5\n3 4 1 7 9", "expected": "7", "hidden": False},
        ],
        "samples": [0],
    },

    # 3028. Max Exponent
    {
        "id": 3028,
        "slug": "max-exponent-range",
        "title": "Maximum Power-of-2 Exponent in Range",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a range <code>[a, b]</code> inclusive, find the number whose largest power-of-2 divisor has
the greatest exponent (i.e. the number with the most trailing factors of 2). On a tie, print the
smallest such number.</p>
<h3>Input format:</h3>
<p>A single line: <code>a b</code>.</p>
<h3>Example:</h3>
<pre>Input: 7 12     Output: 8</pre>
""",
        "hint": "For each number in [a,b], repeatedly divide by 2 while it's even, counting how many times you can. Track the number with the largest such count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // TODO: find the number in [a,b] with the largest power-of-2 exponent dividing it
        int best = a;

        System.out.println(best);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\na = read_int()\nb = read_int()\n\n# TODO: find the number in [a,b] with the largest power-of-2 exponent dividing it\nbest = a\n\nprint(best)",
        },
        "tests": [
            {"input": "7 12", "expected": "8", "hidden": False},
        ],
        "samples": [0],
    },

    # 3029. Max Favourite Song
    {
        "id": 3029,
        "slug": "max-favourite-song",
        "title": "Max Favourite Song",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Sliding Window"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string <code>S</code> and integer <code>K</code>, find the maximum number of occurrences
of the character <code>'a'</code> within any substring of <code>S</code> of length exactly
<code>K</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>S</code>. Line 2: <code>K</code>.</p>
<h3>Example:</h3>
<pre>Input:          Output:
acdbaaca        2
3</pre>
""",
        "hint": "Use a sliding window of size K: maintain a running count of 'a' characters in the window, adding the incoming character and removing the outgoing one as the window slides.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int k = Integer.parseInt(sc.nextLine().trim());

        // TODO: max count of 'a' in any window of length k
        int max = 0;

        System.out.println(max);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\nk = int(sys.stdin.readline().strip())\n\n# TODO: max count of 'a' in any window of length k\nbest = 0\n\nprint(best)",
        },
        "tests": [
            {"input": "acdbaaca\n3", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3030. Maximum and Its Index
    {
        "id": 3030,
        "slug": "maximum-and-its-index",
        "title": "Maximum Element and Its Index",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, print its maximum value on one line, then its (0-indexed) index on the next
line.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                                  Output:
10                                      86
23 45 82 27 66 12 78 13 71 86          9</pre>
""",
        "hint": "Track the maximum value and its index while scanning the array once.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the max value and its index
        int maxVal = 0, maxIdx = 0;

        System.out.println(maxVal);
        System.out.println(maxIdx);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find the max value and its index\nmax_val = 0\nmax_idx = 0\n\nprint(max_val)\nprint(max_idx)",
        },
        "tests": [
            {"input": "10\n23 45 82 27 66 12 78 13 71 86", "expected": "86\n9", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3031. Maximum With Index Format
    {
        "id": 3031,
        "slug": "maximum-with-index-format",
        "title": "Maximum With Index (Tuple Format)",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, find its maximum value and index, and print them formatted exactly as
<code>(max,index)</code> with no spaces.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:          Output:
5               (9,3)
1 8 4 9 6</pre>
""",
        "hint": "Track the max value and its index while scanning, then print \"(\" + max + \",\" + index + \")\" with no spaces.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the max value and its index, print as (max,index)
        int maxVal = 0, maxIdx = 0;

        System.out.println("(" + maxVal + "," + maxIdx + ")");
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find the max value and its index, print as (max,index)\nmax_val = 0\nmax_idx = 0\n\nprint(\"(\" + str(max_val) + \",\" + str(max_idx) + \")\")",
        },
        "tests": [
            {"input": "5\n1 8 4 9 6", "expected": "(9,3)", "hidden": False},
        ],
        "samples": [0],
    },

    # 3032. Merge Sorted Arrays
    {
        "id": 3032,
        "slug": "merge-sorted-arrays",
        "title": "Merge Two Sorted Arrays",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting", "Two Pointers"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given two arrays, each already sorted individually, print the merged sorted array, space
separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n1</code>. Line 2: <code>n1</code> sorted integers. Line 3: <code>n2</code>. Line 4:
<code>n2</code> sorted integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
5                       1 2 2 3 4 4 5 6 8 10
1 2 3 4 5
5
2 4 6 8 10</pre>
""",
        "hint": "Standard merge step from merge sort: use two pointers, always taking the smaller of the two current elements.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int[] a1 = new int[n1];
        for (int i = 0; i < n1; i++) a1[i] = sc.nextInt();
        int n2 = sc.nextInt();
        int[] a2 = new int[n2];
        for (int i = 0; i < n2; i++) a2[i] = sc.nextInt();

        // TODO: merge a1 and a2 into one sorted array
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn1 = read_int()\na1 = [read_int() for _ in range(n1)]\nn2 = read_int()\na2 = [read_int() for _ in range(n2)]\n\n# TODO: merge a1 and a2 into one sorted array\nresult = []\n\nprint(\" \".join(str(x) for x in result))",
        },
        "tests": [
            {"input": "5\n1 2 3 4 5\n5\n2 4 6 8 10", "expected": "1 2 2 3 4 4 5 6 8 10", "hidden": False},
        ],
        "samples": [0],
    },

    # 3033. Most Frequent Vowel
    {
        "id": 3033,
        "slug": "most-frequent-vowel",
        "title": "Most Frequent Vowel",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string, find the lowercase vowel (a, e, i, o, u) that occurs most frequently. You may
assume a unique most-frequent vowel exists.</p>
<h3>Input format:</h3>
<p>Line 1: length of the string (may be ignored). Line 2: the string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
6           a
xyuaab</pre>
""",
        "hint": "Count occurrences of each of a,e,i,o,u and print the one with the highest count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String s = sc.nextLine();

        // TODO: find the most frequent vowel in s
        char best = '?';

        System.out.println(best);
    }
}""", "python": "import sys\nsys.stdin.readline()\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: find the most frequent vowel in s\nbest = \"?\"\n\nprint(best)",
        },
        "tests": [
            {"input": "6\nxyuaab", "expected": "a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3034. Move Hyphens to Front
    {
        "id": 3034,
        "slug": "move-hyphens-to-front",
        "title": "Move Hyphens to Front",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string containing letters and hyphens, move all hyphens to the front of the string,
preserving the relative order of the remaining characters.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: Move-Hyphens-to-Front     Output: ---MoveHyphenstoFront</pre>
""",
        "hint": "Split the characters into two buffers as you scan: one for hyphens, one for everything else, then concatenate hyphens first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: move all '-' characters to the front, preserving order of the rest
        System.out.println(s);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: move all '-' characters to the front, preserving order of the rest\nprint(s)",
        },
        "tests": [
            {"input": "Move-Hyphens-to-Front", "expected": "---MoveHyphenstoFront", "hidden": False},
            {"input": "String-Compare", "expected": "-StringCompare", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3035. Negative Stock Price Days
    {
        "id": 3035,
        "slug": "negative-stock-price-days",
        "title": "Days With a Price Decrease",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array of daily closing stock prices, count the number of days where the price decreased
from the previous day.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       2
2 3 1 4 5 2</pre>
""",
        "hint": "Compare each element with the previous one and count strict decreases.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: count days where arr[i+1] < arr[i]
        int count = 0;

        System.out.println(count);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: count days where arr[i+1] < arr[i]\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "6\n2 3 1 4 5 2", "expected": "2", "hidden": False},
            {"input": "1\n6", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3036. Operation Choices
    {
        "id": 3036,
        "slug": "operation-choices",
        "title": "Operation Choices",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given three integers <code>c</code>, <code>a</code>, <code>b</code>, compute a result based on
<code>c</code>: if <code>c=1</code> print <code>a+b</code>, if <code>c=2</code> print
<code>a-b</code>, if <code>c=3</code> print <code>a*b</code>, if <code>c=4</code> print
<code>a/b</code> (integer division).</p>
<h3>Input format:</h3>
<p>Line 1: <code>c</code>. Line 2: <code>a</code>. Line 3: <code>b</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1           28
12
16</pre>
""",
        "hint": "Use a switch/if-else on c to select the operation.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        // TODO: apply the operation selected by c (1=+, 2=-, 3=*, 4=/)
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nc = read_int()\na = read_int()\nb = read_int()\n\n# TODO: apply the operation selected by c (1=+, 2=-, 3=*, 4=/)\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "1\n12\n16", "expected": "28", "hidden": False},
            {"input": "2\n16\n20", "expected": "-4", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3037. Pair Sum Max Product
    {
        "id": 3037,
        "slug": "pair-sum-max-product",
        "title": "Pair Sum With Maximum Product",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Two Pointers"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array and a target sum, find the pair of elements <code>(x, y)</code> with
<code>x + y == target</code> that has the <b>maximum product</b>. Print the pair formatted as
<code>[larger, smaller]</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>target</code>.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
8                               [10, 8]
11 1 2 8 10 11 15 7
18</pre>
""",
        "hint": "Check every pair (i, j) with i != j; among those summing to target, keep the one with the highest product, printing the larger value first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int target = sc.nextInt();

        // TODO: find the pair summing to target with the maximum product
        int bestX = 0, bestY = 0;

        System.out.println("[" + bestX + ", " + bestY + "]");
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\ntarget = read_int()\n\n# TODO: find the pair summing to target with the maximum product\nbest_x = 0\nbest_y = 0\n\nprint(\"[\" + str(best_x) + \", \" + str(best_y) + \"]\")",
        },
        "tests": [
            {"input": "8\n11 1 2 8 10 11 15 7\n18", "expected": "[10, 8]", "hidden": False},
        ],
        "samples": [0],
    },

    # 3038. Password Checker
    {
        "id": 3038,
        "slug": "password-checker-accenture",
        "title": "Password Validity Checker",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a candidate password string, print <code>1</code> if it is valid, otherwise print
<code>0</code>. A password is valid if:</p>
<ul>
  <li>its length is at least 4</li>
  <li>it contains at least one digit</li>
  <li>it contains at least one uppercase letter</li>
  <li>it contains no space and no <code>/</code> character</li>
  <li>it does not start with a digit</li>
</ul>
<h3>Input format:</h3>
<p>A single line containing the password (may contain spaces).</p>
<h3>Example:</h3>
<pre>Input: aA1_67           Output: 1
Input: a987 abC012       Output: 0  (contains a space)</pre>
""",
        "hint": "Scan the characters tracking whether a digit and an uppercase letter were seen, and whether a space or '/' appears; also check the first character isn't a digit.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: validate the password per the stated rules
        boolean valid = false;

        System.out.println(valid ? 1 : 0);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: validate the password per the stated rules\nvalid = False\n\nprint(1 if valid else 0)",
        },
        "tests": [
            {"input": "aA1_67", "expected": "1", "hidden": False},
            {"input": "a987 abC012", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3039. Print Even Odd Labels
    {
        "id": 3039,
        "slug": "print-even-odd-labels",
        "title": "Label Array Elements Even/Odd",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, print <code>"odd"</code> or <code>"even"</code> for each element in order,
space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       odd even odd even odd even
1 2 3 4 5 6</pre>
""",
        "hint": "For each element, append \"even\" or \"odd\" to a result buffer based on arr[i] % 2.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: label each element "odd" or "even", space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: label each element \"odd\" or \"even\", space separated\nlabels = []\n\nprint(\" \".join(labels))",
        },
        "tests": [
            {"input": "6\n1 2 3 4 5 6", "expected": "odd even odd even odd even", "hidden": False},
        ],
        "samples": [0],
    },

    # 3040. Product of Two Smallest
    {
        "id": 3040,
        "slug": "product-of-two-smallest",
        "title": "Product of Two Smallest Elements",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a target <code>sum</code> and an array, find the two smallest elements of the array. If
their sum is <code>&lt;= sum</code>, print their product; otherwise print <code>0</code>. If the
array has fewer than 2 elements, print <code>-1</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>sum</code>. Line 2: <code>n</code>. Line 3: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                      Output:
9                           2
7
5 2 4 3 9 7 1</pre>
""",
        "hint": "Sort a copy of the array; the two smallest are at index 0 and 1. Compare their sum to the given sum parameter before deciding what to print.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: product of the two smallest elements if their sum <= sum, else 0 (or -1 if n<2)
        int result = (n < 2) ? -1 : 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\ntarget_sum = read_int()\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: product of the two smallest elements if their sum <= sum, else 0 (or -1 if n<2)\nresult = -1 if n < 2 else 0\n\nprint(result)",
        },
        "tests": [
            {"input": "9\n7\n5 2 4 3 9 7 1", "expected": "2", "hidden": False},
            {"input": "4\n6\n9 8 3 -7 3 9", "expected": "-21", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3041. Rat Count House
    {
        "id": 3041,
        "slug": "rat-food-count-house",
        "title": "Houses Needed to Feed the Rats",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Greedy"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>There are <code>r</code> rats, each needing <code>unit</code> food. An array gives the food
available at each house, in order. Find the minimum number of houses (starting from the first) whose
cumulative food is enough to feed all the rats. If it's never enough, print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>r</code>. Line 2: <code>unit</code>. Line 3: <code>n</code> (number of houses). Line 4:
<code>n</code> space-separated integers (food per house).</p>
<h3>Example:</h3>
<pre>Input:                      Output:
7                           4
2
8
2 8 3 5 7 4 1 2</pre>
""",
        "hint": "Compute the total food needed as r*unit, then accumulate food house by house until the running total reaches that need, counting how many houses were used.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int unit = sc.nextInt();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: min number of houses (from the start) whose cumulative food >= r*unit, else 0
        int houses = 0;

        System.out.println(houses);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nr = read_int()\nunit = read_int()\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: min number of houses (from the start) whose cumulative food >= r*unit, else 0\nhouses = 0\n\nprint(houses)",
        },
        "tests": [
            {"input": "7\n2\n8\n2 8 3 5 7 4 1 2", "expected": "4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3042. Rearrangement of Bits
    {
        "id": 3042,
        "slug": "rearrangement-of-bits",
        "title": "Rearrangement of Bits for Minimum Value",
        "difficulty": "Easy",
        "topics": [T, "Bit Manipulation", "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a positive integer <code>N</code>, rearrange its binary bits so that all the set (1) bits
are moved to the least-significant end, forming the smallest possible resulting decimal value. Print
that minimum value.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 10     Output: 3</pre>
<p>Explanation: 10 = 1010 in binary, which has two set bits. The minimum arrangement is 0011 = 3.</p>
""",
        "hint": "Count the set bits c of N. The minimum value with c set bits, all packed at the low end, is (1 << c) - 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count set bits c, print (1<<c) - 1
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: count set bits c, print (1<<c) - 1\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "10", "expected": "3", "hidden": False},
            {"input": "2", "expected": "1", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3043. Repeat a String
    {
        "id": 3043,
        "slug": "repeat-a-string",
        "title": "Repeat a String N Times",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer <code>N</code> and a string <code>S</code>, print <code>S</code> repeated
<code>N</code> times, concatenated with no separator.</p>
<h3>Input format:</h3>
<p>Line 1: <code>N</code>. Line 2: <code>S</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
3           abcabcabc
abc</pre>
""",
        "hint": "Use a StringBuilder and append S in a loop N times.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String s = sc.nextLine();

        // TODO: repeat s, n times, concatenated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString());
    }
}""", "python": "import sys\nn = int(sys.stdin.readline().strip())\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: repeat s, n times, concatenated\nresult = \"\"\n\nprint(result)",
        },
        "tests": [
            {"input": "3\nabc", "expected": "abcabcabc", "hidden": False},
        ],
        "samples": [0],
    },

    # 3044. Replace Character
    {
        "id": 3044,
        "slug": "replace-character",
        "title": "Swap Two Characters in a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a lowercase string and two characters <code>ch1</code>, <code>ch2</code>, simultaneously
swap every occurrence of <code>ch1</code> with <code>ch2</code> and every occurrence of
<code>ch2</code> with <code>ch1</code> in the original string. Print the transformed string.</p>
<h3>Input format:</h3>
<p>Line 1: the string. Line 2: <code>ch1</code>. Line 3: <code>ch2</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
apples      paales
a
p</pre>
""",
        "hint": "For each character c in the string: if c==ch1 output ch2; else if c==ch2 output ch1; else output c unchanged. This must be a simultaneous swap, not sequential replacement.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char ch1 = sc.nextLine().trim().charAt(0);
        char ch2 = sc.nextLine().trim().charAt(0);

        // TODO: simultaneously swap ch1 and ch2 throughout s
        System.out.println(s);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\nch1 = sys.stdin.readline().strip()[0]\nch2 = sys.stdin.readline().strip()[0]\n\n# TODO: simultaneously swap ch1 and ch2 throughout s\nprint(s)",
        },
        "tests": [
            {"input": "apples\na\np", "expected": "paales", "hidden": False},
        ],
        "samples": [0],
    },

    # 3045. Replace Most Frequent Character
    {
        "id": 3045,
        "slug": "replace-most-frequent-character",
        "title": "Replace the Most Frequent Character",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string and a replacement character <code>c</code>, find the single most frequent
character in the string and replace <b>all</b> its occurrences with <code>c</code>. Print the
resulting string.</p>
<h3>Input format:</h3>
<p>Line 1: the string. Line 2: the replacement character.</p>
<h3>Example:</h3>
<pre>Input:              Output:
bbadbbababb         ttadttatatt
t</pre>
""",
        "hint": "Count character frequencies with a hash map, find the character with the highest count, then use String.replace to substitute it everywhere.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char repl = sc.nextLine().trim().charAt(0);

        // TODO: replace the most frequent character in s with repl
        System.out.println(s);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\nrepl = sys.stdin.readline().strip()[0]\n\n# TODO: replace the most frequent character in s with repl\nprint(s)",
        },
        "tests": [
            {"input": "bbadbbababb\nt", "expected": "ttadttatatt", "hidden": False},
        ],
        "samples": [0],
    },

    # 3046. Reverse String
    {
        "id": 3046,
        "slug": "reverse-string-accenture",
        "title": "Reverse a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string, print it reversed.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: hello     Output: olleh</pre>
""",
        "hint": "Use StringBuilder's reverse() method, or build the reversed string manually from the last character to the first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: reverse s
        System.out.println(s);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: reverse s\nprint(s)",
        },
        "tests": [
            {"input": "hello", "expected": "olleh", "hidden": False},
        ],
        "samples": [0],
    },

    # 3047. Reverse Words in a String
    {
        "id": 3047,
        "slug": "reverse-words-in-a-string",
        "title": "Reverse Words in a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a line of space-separated words, reverse the order of the words (not the letters within
each word), and print the result space-separated.</p>
<h3>Input format:</h3>
<p>A single line of words.</p>
<h3>Example:</h3>
<pre>Input: Hello World     Output: World Hello</pre>
""",
        "hint": "Split the line on whitespace, then join the resulting words back together in reverse order.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        // TODO: reverse the order of the words in line
        System.out.println(line);
    }
}""", "python": "import sys\nline = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: reverse the order of the words in line\nprint(line)",
        },
        "tests": [
            {"input": "Hello World", "expected": "World Hello", "hidden": False},
        ],
        "samples": [0],
    },

    # 3048. Roots of a Quadratic Equation
    {
        "id": 3048,
        "slug": "roots-of-quadratic-equation",
        "title": "Roots of a Quadratic Equation",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given coefficients <code>a</code>, <code>b</code>, <code>c</code> of the quadratic equation
<code>ax^2 + bx + c = 0</code> (assume the discriminant is non-negative), print its two real roots,
each rounded to 2 decimal places, separated by a space, with the "+" root first.</p>
<h3>Input format:</h3>
<p>A single line: <code>a b c</code>.</p>
<h3>Example:</h3>
<pre>Input: 1 -3 2     Output: 2.00 1.00</pre>
""",
        "hint": "Use the quadratic formula: root = (-b +/- sqrt(b^2 - 4ac)) / (2a). Print the plus root first, then the minus root, each formatted with two decimals.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        // TODO: compute the two roots using the quadratic formula
        double root1 = 0.0, root2 = 0.0;

        System.out.printf("%.2f %.2f%n", root1, root2);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\na = float(_data[_idx]); _idx += 1\nb = float(_data[_idx]); _idx += 1\nc = float(_data[_idx]); _idx += 1\n\n# TODO: compute the two roots using the quadratic formula\nroot1 = 0.0\nroot2 = 0.0\n\nprint(\"%.2f %.2f\" % (root1, root2))",
        },
        "tests": [
            {"input": "1 -3 2", "expected": "2.00 1.00", "hidden": False},
        ],
        "samples": [0],
    },

    # 3049. Rotate Array by K
    {
        "id": 3049,
        "slug": "rotate-array-by-k",
        "title": "Rotate Array by K Steps",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array and an integer <code>k</code>, rotate the array to the right by <code>k</code>
steps and print the result, space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>k</code>.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       5 6 7 1 2 3 4
1 2 3 4 5 6 7
3</pre>
""",
        "hint": "Each element at index i moves to index (i+k) mod n in the result array. Remember to take k modulo n first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int k = sc.nextInt();

        // TODO: rotate arr to the right by k steps
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\nk = read_int()\n\n# TODO: rotate arr to the right by k steps\nresult = []\n\nprint(\" \".join(str(x) for x in result))",
        },
        "tests": [
            {"input": "7\n1 2 3 4 5 6 7\n3", "expected": "5 6 7 1 2 3 4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3050. Second Largest Distinct Element
    {
        "id": 3050,
        "slug": "second-largest-distinct-element",
        "title": "Second Largest Distinct Element",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, find the second-largest <b>distinct</b> value.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       6
1 3 5 2 4 6 8</pre>
""",
        "hint": "Insert all values into a sorted set of unique values (e.g. TreeSet), then take the element just below the maximum.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the second-largest distinct value
        int result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: find the second-largest distinct value\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "7\n1 3 5 2 4 6 8", "expected": "6", "hidden": False},
        ],
        "samples": [0],
    },

    # 3051. Set Zero Matrix
    {
        "id": 3051,
        "slug": "set-zero-matrix",
        "title": "Set Zero Matrix",
        "difficulty": "Medium",
        "topics": [T, "Matrix", "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an <code>m x n</code> matrix, if any element is 0, set its entire row and column to 0
(using the original positions of the zeroes). Print the resulting matrix, one row per line,
space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: rows. Line 2: cols. Then <code>rows</code> lines of <code>cols</code> space-separated
integers.</p>
<h3>Example:</h3>
<pre>Input:          Output:
3               1 0 1
3               0 0 0
1 1 1           1 0 1
1 0 1
1 1 1</pre>
""",
        "hint": "First record which rows and columns contain a 0 (without modifying the matrix while scanning). Then in a second pass, zero out any cell whose row or column was flagged.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        int[][] m = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++) m[i][j] = sc.nextInt();

        // TODO: zero out entire row/column for every 0 found in the original matrix

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sb.append(m[i][j]);
                if (j < cols - 1) sb.append(" ");
            }
            sb.append("\\n");
        }
        System.out.print(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nrows = read_int()\ncols = read_int()\nm = [[read_int() for _ in range(cols)] for _ in range(rows)]\n\n# TODO: zero out entire row/column for every 0 found in the original matrix\n\nlines = []\nfor i in range(rows):\n    lines.append(\" \".join(str(m[i][j]) for j in range(cols)))\nprint(\"\\n\".join(lines))",
        },
        "tests": [
            {"input": "3\n3\n1 1 1\n1 0 1\n1 1 1", "expected": "1 0 1\n0 0 0\n1 0 1", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3052. Small Large Sum
    {
        "id": 3052,
        "slug": "small-large-sum",
        "title": "Small Large Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array (all unique elements), split it into elements at even 0-indexed positions and
elements at odd 0-indexed positions. Print the sum of the <b>2nd-largest</b> element of each group.
If the array has 3 or fewer elements (or is empty), print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       7
3 2 1 7 5 4</pre>
""",
        "hint": "Split by index parity, sort each group ascending, and take the element at index size-2 (2nd largest) from each group, then sum them.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements
        int result = (n <= 3) ? 0 : 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements\nresult = 0 if n <= 3 else 0\n\nprint(result)",
        },
        "tests": [
            {"input": "6\n3 2 1 7 5 4", "expected": "7", "hidden": False},
            {"input": "7\n4 0 7 9 6 4 2", "expected": "10", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3053. Standard Deviation
    {
        "id": 3053,
        "slug": "standard-deviation",
        "title": "Population Standard Deviation",
        "difficulty": "Easy",
        "topics": [T, "Math", "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a list of integers, print their population standard deviation, rounded to 2 decimal
places.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
8                               2.00
2 4 4 4 5 5 7 9</pre>
""",
        "hint": "Standard deviation = sqrt(mean of squared deviations from the mean). Compute the mean first, then average the squared differences, then take the square root.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextDouble();

        // TODO: compute the population standard deviation
        double sd = 0.0;

        System.out.printf("%.2f%n", sd);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [float(_data[_idx + i]) for i in range(n)]\n_idx += n\n\n# TODO: compute the population standard deviation\nsd = 0.0\n\nprint(\"%.2f\" % sd)",
        },
        "tests": [
            {"input": "8\n2 4 4 4 5 5 7 9", "expected": "2.00", "hidden": False},
        ],
        "samples": [0],
    },

    # 3054. String Decoder
    {
        "id": 3054,
        "slug": "string-decoder",
        "title": "Run-Length Binary String Decoder",
        "difficulty": "Medium",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a binary string (only '0's and '1's), each maximal run of consecutive '1's encodes one
uppercase letter: the letter's position in the alphabet equals the length of that run (one '1' =
'A', two '1's = 'B', etc.), and each run is terminated by a '0' or by the end of the string. Decode
the string into the resulting uppercase word.</p>
<h3>Input format:</h3>
<p>A single line containing the binary string.</p>
<h3>Example:</h3>
<pre>Input: 10110111     Output: ABC</pre>
<p>Explanation: "1" -> A, "11" -> B, "111" -> C.</p>
""",
        "hint": "Scan the string counting consecutive 1s; whenever you hit a 0 (or reach the end), convert the current run length into a letter ('A' + runLength - 1) and reset the counter.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: decode s into an uppercase word per the run-length rule
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString());
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: decode s into an uppercase word per the run-length rule\nresult = \"\"\n\nprint(result)",
        },
        "tests": [
            {"input": "10110111", "expected": "ABC", "hidden": False},
        ],
        "samples": [0],
    },

    # 3055. Sum of Multiples of 3 and 5
    {
        "id": 3055,
        "slug": "sum-of-multiples-of-3-and-5",
        "title": "Sum of Multiples of 15 in a Range",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given <code>m</code> and <code>n</code>, print the sum of all numbers in <code>[m, n]</code>
inclusive that are divisible by both 3 and 5 (i.e. by 15).</p>
<h3>Input format:</h3>
<p>Line 1: <code>m</code>. Line 2: <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
12          90
50</pre>
""",
        "hint": "Loop from m to n, summing every value divisible by 15.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();

        // TODO: sum values in [m,n] divisible by both 3 and 5
        long sum = 0;

        System.out.println(sum);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nm = read_int()\nn = read_int()\n\n# TODO: sum values in [m,n] divisible by both 3 and 5\ntotal = 0\n\nprint(total)",
        },
        "tests": [
            {"input": "12\n50", "expected": "90", "hidden": False},
            {"input": "100\n160", "expected": "510", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3056. Sum of Binary Digits (popcount)
    {
        "id": 3056,
        "slug": "sum-of-binary-digits-popcount",
        "title": "Sum of Binary Digits",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer <code>n</code>, convert it to binary and print the sum of its binary digits
(i.e. the count of set bits).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 15     Output: 4</pre>
<p>Explanation: 15 in binary is 1111, whose digits sum to 4.</p>
""",
        "hint": "Repeatedly check the lowest bit (n & 1) and shift right, counting how many bits are 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count the number of 1-bits in n's binary representation
        int count = 0;

        System.out.println(count);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: count the number of 1-bits in n's binary representation\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "15", "expected": "4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3057. Sum at Even Index After Reverse
    {
        "id": 3057,
        "slug": "sum-at-even-index-after-reverse",
        "title": "Sum at Even Index After Reversing",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array, reverse it, then sum the elements at even (0-indexed) positions of the
<b>reversed</b> array.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
6                               120
10 20 30 40 50 60</pre>
<p>Explanation: reversed = [60,50,40,30,20,10]. Even indices 0,2,4 hold 60,40,20, summing to 120.</p>
""",
        "hint": "Build the reversed array first (or index from the end), then sum every second element starting at index 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: reverse arr, then sum elements at even indices of the reversed array
        long sum = 0;

        System.out.println(sum);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: reverse arr, then sum elements at even indices of the reversed array\ntotal = 0\n\nprint(total)",
        },
        "tests": [
            {"input": "6\n10 20 30 40 50 60", "expected": "120", "hidden": False},
        ],
        "samples": [0],
    },

    # 3058. Sum of Divisors
    {
        "id": 3058,
        "slug": "sum-of-divisors",
        "title": "Sum of All Divisors",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a positive integer <code>N</code>, print the sum of all its positive divisors (including 1
and N itself).</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 12     Output: 28</pre>
<p>Explanation: 1+2+3+4+6+12 = 28.</p>
""",
        "hint": "Loop i from 1 to N and add i to the sum whenever N % i == 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum all divisors of n from 1 to n
        long sum = 0;

        System.out.println(sum);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: sum all divisors of n from 1 to n\ntotal = 0\n\nprint(total)",
        },
        "tests": [
            {"input": "12", "expected": "28", "hidden": False},
        ],
        "samples": [0],
    },

    # 3059. Sum of Primes Below N
    {
        "id": 3059,
        "slug": "sum-of-primes-below-n",
        "title": "Sum of Primes Below N",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer <code>N</code>, print the sum of all prime numbers strictly less than
<code>N</code>.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 10     Output: 17</pre>
<p>Explanation: 2+3+5+7 = 17.</p>
""",
        "hint": "For each number from 2 to N-1, check primality by trial division up to its square root, and sum the primes.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum all primes strictly less than n
        long sum = 0;

        System.out.println(sum);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: sum all primes strictly less than n\ntotal = 0\n\nprint(total)",
        },
        "tests": [
            {"input": "10", "expected": "17", "hidden": False},
        ],
        "samples": [0],
    },

    # 3060. Multiplication Table and Sum
    {
        "id": 3060,
        "slug": "multiplication-table-and-sum",
        "title": "Multiplication Table and Sum",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a number <code>n</code>, print its multiplication table from <code>n*1</code> through
<code>n*10</code> (space-separated) on one line, then the sum of those 10 multiples on the next
line.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 5     Output: 5 10 15 20 25 30 35 40 45 50
                      275</pre>
""",
        "hint": "Loop i from 1 to 10, computing n*i, appending it to the output line and adding it to a running sum. Print the sum on the next line.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print n*1..n*10 space separated, then the sum on the next line
        System.out.println();
        System.out.println(0);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: print n*1..n*10 space separated, then the sum on the next line\nprint()\nprint(0)",
        },
        "tests": [
            {"input": "5", "expected": "5 10 15 20 25 30 35 40 45 50\n275", "hidden": False},
            {"input": "12", "expected": "12 24 36 48 60 72 84 96 108 120\n660", "hidden": False},
        ],
        "samples": [0, 1],
        "io_style": "lines",
    },

    # 3061. Vowel Permutation Count
    {
        "id": 3061,
        "slug": "vowel-permutation-count",
        "title": "Vowel-Fixed Permutation Count",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Math"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string <code>S</code>, fix the positions of all vowels (A,E,I,O,U, either case) and count
the number of permutations formed by permuting only the remaining (non-vowel) characters, i.e. the
factorial of the non-vowel character count.</p>
<h3>Input format:</h3>
<p>A single line containing <code>S</code>.</p>
<h3>Example:</h3>
<pre>Input: ABC     Output: 2</pre>
<p>Explanation: A is the only vowel (fixed); B and C are non-vowels, permuting in 2! = 2 ways.</p>
""",
        "hint": "Count how many characters are NOT one of A,E,I,O,U,a,e,i,o,u, then compute that count's factorial.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: factorial of the count of non-vowel characters in s
        long result = 1;

        System.out.println(result);
    }
}""", "python": "import sys\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: factorial of the count of non-vowel characters in s\nresult = 1\n\nprint(result)",
        },
        "tests": [
            {"input": "ABC", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3062. Most Frequent Vowel II
    {
        "id": 3062,
        "slug": "most-frequent-vowel-ii",
        "title": "Most Frequent Vowel II",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a string, find the lowercase vowel (a, e, i, o, u) that occurs most frequently. You may
assume a unique most-frequent vowel exists.</p>
<h3>Input format:</h3>
<p>Line 1: length of the string (may be ignored). Line 2: the string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
7           a
xayuaba</pre>
""",
        "hint": "Count occurrences of each of a,e,i,o,u and print the one with the highest count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String s = sc.nextLine();

        // TODO: find the most frequent vowel in s
        char best = '?';

        System.out.println(best);
    }
}""", "python": "import sys\nsys.stdin.readline()\ns = sys.stdin.readline().rstrip(\"\\n\")\n\n# TODO: find the most frequent vowel in s\nbest = \"?\"\n\nprint(best)",
        },
        "tests": [
            {"input": "7\nxayuaba", "expected": "a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3063. Fibonacci Series
    {
        "id": 3063,
        "slug": "fibonacci-series-n-terms",
        "title": "Print Fibonacci Series (N Terms)",
        "difficulty": "Easy",
        "topics": [T, "Math", "Patterns"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer <code>N</code>, print the first <code>N</code> terms of the Fibonacci series
(starting <code>0, 1, 1, 2, ...</code>), space-separated.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code> (number of terms).</p>
<h3>Example:</h3>
<pre>Input: 9     Output: 0 1 1 2 3 5 8 13 21</pre>
""",
        "hint": "Keep two running variables a=0, b=1; print a, then advance (a, b) = (b, a+b), repeating N times.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print the first n Fibonacci numbers, space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: print the first n Fibonacci numbers, space separated\nresult = []\n\nprint(\" \".join(str(x) for x in result))",
        },
        "tests": [
            {"input": "9", "expected": "0 1 1 2 3 5 8 13 21", "hidden": False},
        ],
        "samples": [0],
    },

    # 3064. Max Difference Between Successive Elements
    {
        "id": 3064,
        "slug": "max-diff-successive-elements",
        "title": "Max Difference Between Successive Elements",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an integer array, sort it, and print the maximum difference between two consecutive
elements in the sorted array. If the array has fewer than 2 elements, print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
4                   3
3 6 9 1</pre>
""",
        "hint": "Sort the array, then scan adjacent pairs tracking the largest gap.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: sort arr, find the max difference between consecutive elements
        int maxDiff = 0;

        System.out.println(maxDiff);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: sort arr, find the max difference between consecutive elements\nmax_diff = 0\n\nprint(max_diff)",
        },
        "tests": [
            {"input": "4\n3 6 9 1", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3065. Nth Fibonacci Number
    {
        "id": 3065,
        "slug": "nth-fibonacci-number",
        "title": "Nth Fibonacci Number",
        "difficulty": "Easy",
        "topics": [T, "Math", "Dynamic Programming"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given <code>n</code>, print the <code>n</code>-th Fibonacci number (0-indexed: fib(0)=0,
fib(1)=1, fib(2)=1, ...).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 9     Output: 34</pre>
""",
        "hint": "Iteratively build up fib values from fib(0) and fib(1) to fib(n) using a simple loop; avoid plain recursion to prevent excessive recomputation.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: compute the n-th Fibonacci number (fib(0)=0, fib(1)=1)
        long result = 0;

        System.out.println(result);
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: compute the n-th Fibonacci number (fib(0)=0, fib(1)=1)\nresult = 0\n\nprint(result)",
        },
        "tests": [
            {"input": "9", "expected": "34", "hidden": False},
        ],
        "samples": [0],
    },

    # 3066. Remove Duplicates from Array
    {
        "id": 3066,
        "slug": "remove-duplicates-preserve-order",
        "title": "Remove Duplicates, Preserve Order",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Hash Table"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given an array of integers, remove duplicate values, keeping only the first occurrence of each
value and preserving the original relative order. Print the result space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       1 2 3 4 5
1 2 2 3 4 4 5</pre>
""",
        "hint": "Use an ordered set (e.g. LinkedHashSet) to collect values while preserving first-occurrence insertion order, then print its contents.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: remove duplicates, preserving first-occurrence order
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\narr = [read_int() for _ in range(n)]\n\n# TODO: remove duplicates, preserving first-occurrence order\nresult = []\n\nprint(\" \".join(str(x) for x in result))",
        },
        "tests": [
            {"input": "7\n1 2 2 3 4 4 5", "expected": "1 2 3 4 5", "hidden": False},
        ],
        "samples": [0],
    },

    # 3067. Rhyme Words
    {
        "id": 3067,
        "slug": "rhyme-words",
        "title": "Best Rhyming Word",
        "difficulty": "Medium",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java", "python"],
        "description": """
<p>Given a target word <code>S</code> and a list of candidate words <code>D</code>, find the word in
<code>D</code> (excluding <code>S</code> itself if present) whose <b>suffix</b> matches <code>S</code>'s
suffix for the greatest number of characters (comparing from the end of each word backwards). Print
that best-matching word, or <code>No Word</code> if no candidate shares any suffix character with
<code>S</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>S</code>. Line 2: the number of words in <code>D</code>. Line 3: the words of
<code>D</code>, space-separated.</p>
<h3>Example:</h3>
<pre>Input:                                          Output:
thunder                                         under
5
pukle thunder powder blender under</pre>
""",
        "hint": "For each candidate word (skipping one equal to S), compare characters from the end of both words backwards, counting how many match consecutively before the first mismatch. Track the candidate with the longest such run.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        int cnt = Integer.parseInt(sc.nextLine().trim());
        String[] d = sc.nextLine().trim().split("\\\\s+");

        // TODO: find the word in d (excluding s) with the longest matching suffix
        String best = "No Word";

        System.out.println(best);
    }
}""", "python": "import sys\ns = sys.stdin.readline().strip()\ncnt = int(sys.stdin.readline().strip())\nd = sys.stdin.readline().strip().split()\n\n# TODO: find the word in d (excluding s) with the longest matching suffix\nbest = \"No Word\"\n\nprint(best)",
        },
        "tests": [
            {"input": "thunder\n5\npukle thunder powder blender under", "expected": "under", "hidden": False},
        ],
        "samples": [0],
    },

    # ================================================================== #
    # SQL problems 3068-3097, sourced from "Accenture SQL.pdf"
    # ================================================================== #
    # ------------------------------------------------------------------ #
    # 3068. Debit Transactions in a Range (Banking cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3068,
        "slug": "debit-transactions-in-range",
        "title": "Debit Transactions in a Range",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: account_transaction</h3>
<pre>+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| transaction_id   | int     |
| account_id       | int     |
| transaction_date | date    |
| amount           | decimal |
| transaction_type | varchar |
+------------------+---------+</pre>
<p><code>transaction_id</code> is the unique identifier for this table. <code>transaction_type</code> is
either <code>'Debit'</code> or <code>'Credit'</code>.</p>

<h3>Problem:</h3>
<p>Write a query to display the transaction id, amount and transaction type of all the transactions whose:</p>
<ul>
  <li>transaction type is <code>'Debit'</code>, and</li>
  <li>transaction amount is greater than <code>10000</code> but less than <code>50000</code>.</li>
</ul>
<p>Name your output columns <code>TRANSACTION_ID</code>, <code>AMOUNT</code>, <code>TRANSACTION_TYPE</code>.</p>

<h3>Example Output:</h3>
<pre>+----------------+----------+-------------------+
| TRANSACTION_ID | AMOUNT   | TRANSACTION_TYPE  |
+----------------+----------+-------------------+
| 1001           | 15000.00 | Debit             |
| 1005           | 12000.00 | Debit             |
| 1007           | 49999.00 | Debit             |
| 1009           | 30000.00 | Debit             |
+----------------+----------+-------------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>The bounds are strict: exactly <code>10000</code> or exactly <code>50000</code> do not qualify.</li>
</ul>
""",
        "hint": "Filter on transaction_type = 'Debit' and amount > 10000 AND amount < 50000 — both bounds are strict inequalities.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, BANK_SCHEMA, BANK_VIS, Q1),
            db_entry("Hidden database", True, BANK_SCHEMA, BANK_HID, Q1),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3069. Savings-Type Account Holders (Banking cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3069,
        "slug": "savings-account-holders",
        "title": "Savings-Type Account Holders",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: customer</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| first_name    | varchar |
| last_name     | varchar |
| contact       | varchar |
| email         | varchar |
+---------------+---------+</pre>

<h3>Table: account</h3>
<pre>+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| account_id       | int     |
| customer_id      | int     |
| branch_id        | int     |
| account_type_id  | int     |
| balance          | decimal |
+------------------+---------+</pre>

<h3>Table: account_type</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| account_type_id    | int     |
| account_type_name  | varchar |
+--------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the first name, contact number and balance of all the customers whose
account type <b>name starts with "Sa"</b> (e.g. "Savings", "Salary"). A customer can hold more than one
qualifying account — return one row per matching account.</p>
<p>Order the result by the customer's first name. Name your output columns
<code>FIRST_NAME</code>, <code>CONTACT</code>, <code>BALANCE</code>.</p>

<h3>Example Output:</h3>
<pre>+------------+------------+----------+
| FIRST_NAME | CONTACT    | BALANCE  |
+------------+------------+----------+
| Alice      | 9990001111 | 75000.00 |
| Carol      | 9990003333 | 60000.00 |
| Emma       | 9990005555 | 30000.00 |
+------------+------------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Use <code>LIKE 'Sa%'</code> to match account type names starting with "Sa".</li>
</ul>
""",
        "hint": "Join customer -> account -> account_type, filter account_type_name LIKE 'Sa%', and ORDER BY first_name.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN_ORDER},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, BANK_SCHEMA, BANK_VIS, Q2),
            db_entry("Hidden database", True, BANK_SCHEMA, BANK_HID, Q2),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3070. Employees With High Basic Salary (HR cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3070,
        "slug": "high-value-basic-salary-employees",
        "title": "Employees With High Basic Salary",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: emp_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| empid              | int     |
| empname            | varchar |
| deptid             | int     |
| joining_dt         | date    |
| dob                | date    |
| yrs_of_exp         | int     |
| employee_category  | varchar |
+--------------------+---------+</pre>

<h3>Table: salary_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| employee_category  | varchar |
| basic              | decimal |
| ... (allowances)   | decimal |
+--------------------+---------+</pre>
<p><code>employee_category</code> is the unique identifier for this table, and every row in
<code>emp_info</code> references one via its own <code>employee_category</code> column.</p>

<h3>Table: emp_payroll</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| transno       | int     |
| empid         | int     |
| month         | varchar |
| year          | int     |
| totalearning  | decimal |
| netpay        | decimal |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the employee ID, name, basic salary and net pay for employees whose
<b>basic salary is greater than 5,000</b>.</p>
<p>Name your output columns <code>EMPID</code>, <code>EMPNAME</code>, <code>BASIC</code>, <code>NETPAY</code>.</p>

<h3>Example Output:</h3>
<pre>+-------+-------------+----------+----------+
| EMPID | EMPNAME     | BASIC    | NETPAY   |
+-------+-------------+----------+----------+
| 1     | Alice Rao   | 12000.00 | 11500.00 |
| 2     | Bob Nair    | 8000.00  | 8000.00  |
| 3     | Carol Iyer  | 12000.00 | 12000.00 |
+-------+-------------+----------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Join emp_info to salary_info via employee_category, and to emp_payroll via empid.</li>
</ul>
""",
        "hint": "Join emp_info to salary_info on employee_category and to emp_payroll on empid, then filter basic > 5000.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HR_SCHEMA, HR_VIS, Q3),
            db_entry("Hidden database", True, HR_SCHEMA, HR_HID, Q3),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3071. Experienced Employees Who Joined After 2001 (HR cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3071,
        "slug": "experienced-employees-after-2001",
        "title": "Experienced Employees Who Joined After 2001",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: emp_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| empid              | int     |
| empname            | varchar |
| deptid             | int     |
| joining_dt         | date    |
| dob                | date    |
| yrs_of_exp         | int     |
| employee_category  | varchar |
+--------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the names of employees who:</p>
<ul>
  <li>have more than <code>5</code> years of experience, and</li>
  <li>joined after <code>January 1, 2001</code>.</li>
</ul>
<p>Alias your output columns <code>"Employee ID"</code> and <code>"Employee Name"</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+-----------------+
| Employee ID | Employee Name   |
+-------------+-----------------+
| 2           | Bob Nair        |
| 3           | Carol Iyer      |
| 5           | Emma Pillai     |
+-------------+-----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>. Dates are stored as <code>'YYYY-MM-DD'</code> text, so
      lexicographic comparison with a literal date string works correctly.</li>
</ul>
""",
        "hint": "Filter emp_info WHERE yrs_of_exp > 5 AND joining_dt > '2001-01-01'.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HR_SCHEMA, HR_VIS, Q4),
            db_entry("Hidden database", True, HR_SCHEMA, HR_HID, Q4),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3072. Wednesday Course Schedule (School cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3072,
        "slug": "wednesday-course-schedule",
        "title": "Wednesday Course Schedule",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: course</h3>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| course_id   | int     |
| name        | varchar |
| type        | varchar |
| term        | varchar |
+-------------+---------+</pre>

<h3>Table: section</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| section_id    | int     |
| course_id     | int     |
| schedule_id   | int     |
| instructor_id | int     |
| name          | varchar |
+---------------+---------+</pre>

<h3>Table: schedule</h3>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| schedule_id | int     |
| day         | varchar |
| starttime   | varchar |
| endtime     | varchar |
+-------------+---------+</pre>
<p><code>day</code> stores a lowercase 3-letter abbreviation, e.g. <code>'wed'</code>, <code>'mon'</code>, <code>'fri'</code>.</p>

<h3>Problem:</h3>
<p>Write a query to display the course ID, course name, and schedule details (day and start time) of all
courses that are taught on <code>'wed'</code> (Wednesday).</p>
<p>Alias your output columns <code>"Course ID"</code>, <code>"Course Name"</code>, <code>"Day"</code>, <code>"Start Time"</code>.</p>

<h3>Example Output:</h3>
<pre>+-----------+-------------------+-----+------------+
| Course ID | Course Name       | Day | Start Time |
+-----------+-------------------+-----+------------+
| 1         | Database Systems  | wed | 09:00      |
| 3         | Data Structures   | wed | 14:00      |
+-----------+-------------------+-----+------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>A course can have several sections (e.g. one on Wednesday, another on Friday) — only the
      sections actually scheduled on Wednesday should appear.</li>
</ul>
""",
        "hint": "Join course -> section -> schedule, and filter schedule.day = 'wed'. A course with multiple sections may or may not have a Wednesday section.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, SCHOOL_SCHEMA, SCHOOL_VIS, Q5),
            db_entry("Hidden database", True, SCHOOL_SCHEMA, SCHOOL_HID, Q5),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3073. Books Published After 1940 (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3073,
        "slug": "books-published-after-1940",
        "title": "Books Published After 1940 in a Category",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: books</h3>
<pre>+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| book_id          | int     |
| title            | varchar |
| price            | decimal |
| isbn             | varchar |
| published_date   | date    |
| category         | varchar |
+------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the title, price, and ISBN of books that:</p>
<ul>
  <li>were published after <code>January 1, 1940</code>, and</li>
  <li>fall under the <code>"C102"</code> category.</li>
</ul>
<p>Name your output columns <code>Title</code>, <code>Price</code>, <code>ISBN</code>.</p>

<h3>Example Output:</h3>
<pre>+-----------------------+-------+---------+
| Title                 | Price | ISBN    |
+-----------------------+-------+---------+
| Intro to Algorithms   | 65.00 | ISBN001 |
| Data Structures       | 45.00 | ISBN004 |
+-----------------------+-------+---------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter books WHERE published_date > '1940-01-01' AND category = 'C102'.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, BOOKS_SCHEMA, BOOKS_VIS, Q6),
            db_entry("Hidden database", True, BOOKS_SCHEMA, BOOKS_HID, Q6),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3074. Channel Categories Starting With M (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3074,
        "slug": "channel-categories-starting-m",
        "title": "Channel Categories Starting With M",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: channelscategory</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| categoryid    | int     |
| categoryname  | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the category id and category name of every category whose
<b>name starts with 'M'</b>.</p>
<p>Name your output columns <code>CATEGORYID</code>, <code>CATEGORYNAME</code>.</p>

<h3>Example Output:</h3>
<pre>+------------+--------------+
| CATEGORYID | CATEGORYNAME |
+------------+--------------+
| 1          | Music        |
| 2          | Movies       |
| 4          | Mystery      |
+------------+--------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter channelscategory WHERE categoryname LIKE 'M%'.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, CHAN_SCHEMA, CHAN_VIS, Q7),
            db_entry("Hidden database", True, CHAN_SCHEMA, CHAN_HID, Q7),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3075. Trains to Pune Starting With M (Trains cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3075,
        "slug": "trains-to-pune-starting-m",
        "title": "Trains to Pune Starting With M",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: train_details_tbl</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| train_id      | varchar |
| train_name    | varchar |
| train_type    | varchar |
| train_time    | varchar |
| train_from    | varchar |
| train_to      | varchar |
| train_speed   | int     |
+---------------+---------+</pre>
<p><code>train_from</code> and <code>train_to</code> reference <code>train_stations_tbl.station_id</code>.</p>

<h3>Table: train_stations_tbl</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| station_id    | varchar |
| station_name  | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to find the train ID and name of all trains that:</p>
<ul>
  <li>have a name starting with the letter <code>'M'</code>, and</li>
  <li>go to the station named <code>'PUNE'</code>.</li>
</ul>
<p>Return the output columns in this order: <code>train_id</code>, <code>train_name</code>.</p>

<h3>Example Output:</h3>
<pre>+----------+------------------+
| train_id | train_name       |
+----------+------------------+
| T001     | Mumbai Express   |
| T005     | Mysore Express   |
+----------+------------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Join on <code>train_to = station_id</code>, then check the resolved station's name.</li>
</ul>
""",
        "hint": "Join train_details_tbl to train_stations_tbl on train_to = station_id, filter train_name LIKE 'M%' AND station_name = 'PUNE'.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, TRAIN_SCHEMA, TRAIN_VIS, Q8),
            db_entry("Hidden database", True, TRAIN_SCHEMA, TRAIN_HID, Q8),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3076. Employees With Excess Casual/Medical Leave (HR cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3076,
        "slug": "employees-with-excess-leaves",
        "title": "Employees With Excess Casual/Medical Leave",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: emp_leave_info</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| leaveid       | int     |
| empid         | int     |
| from_date     | date    |
| to_date       | date    |
| total_leaves  | int     |
| leave_type    | varchar |
+---------------+---------+</pre>
<p><code>leave_type</code> is a short code, e.g. <code>'CL'</code> (Casual Leave), <code>'ML'</code>
(Medical Leave), <code>'SL'</code> (Sick Leave).</p>

<h3>Problem:</h3>
<p>Write a query to display the employee ID, type of leave, and total number of leaves for employees who:</p>
<ul>
  <li>have taken <b>more than 10</b> leaves in a single record, and</li>
  <li>the leave type is either <code>'CL'</code> or <code>'ML'</code>.</li>
</ul>
<p>Name your output columns <code>EMPID</code>, <code>LEAVE_TYPE</code>, <code>TOTAL_LEAVES</code>.</p>

<h3>Example Output:</h3>
<pre>+-------+-------------+---------------+
| EMPID | LEAVE_TYPE  | TOTAL_LEAVES  |
+-------+-------------+---------------+
| 2     | CL          | 12            |
| 3     | ML          | 15            |
| 5     | ML          | 20            |
+-------+-------------+---------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter emp_leave_info WHERE total_leaves > 10 AND leave_type IN ('CL', 'ML').",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HR_SCHEMA, HR_VIS, Q9),
            db_entry("Hidden database", True, HR_SCHEMA, HR_HID, Q9),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3077. HR Department Employees (HR cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3077,
        "slug": "hr-department-employees",
        "title": "HR Department Employees",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: emp_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| empid              | int     |
| empname            | varchar |
| deptid             | int     |
| employee_category  | varchar |
+--------------------+---------+</pre>

<h3>Table: department_info</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| deptid        | int     |
| deptname      | varchar |
| location      | varchar |
+---------------+---------+</pre>

<h3>Table: salary_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| employee_category  | varchar |
| basic              | decimal |
+--------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the ID, name, department name, and base salary of employees working in
the <code>'HR'</code> department.</p>
<p>Name your output columns <code>EMPID</code>, <code>EMPNAME</code>, <code>DEPTNAME</code>, <code>BASIC</code>.</p>

<h3>Example Output:</h3>
<pre>+-------+------------+----------+----------+
| EMPID | EMPNAME    | DEPTNAME | BASIC    |
+-------+------------+----------+----------+
| 1     | Alice Rao  | HR       | 12000.00 |
| 2     | Bob Nair   | HR       | 8000.00  |
| 7     | Gita Shah  | HR       | 6000.00  |
+-------+------------+----------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Join emp_info to department_info on deptid, and to salary_info on employee_category, then filter deptname = 'HR'.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HR_SCHEMA, HR_VIS, Q10),
            db_entry("Hidden database", True, HR_SCHEMA, HR_HID, Q10),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3078. Employees in Bangalore or Cochin (HR cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3078,
        "slug": "employees-in-bangalore-cochin",
        "title": "Employees in Bangalore or Cochin",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: emp_info</h3>
<pre>+--------------------+---------+
| Column Name        | Type    |
+--------------------+---------+
| empid              | int     |
| empname            | varchar |
| deptid             | int     |
| employee_category  | varchar |
+--------------------+---------+</pre>

<h3>Table: department_info</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| deptid        | int     |
| deptname      | varchar |
| location      | varchar |
+---------------+---------+</pre>

<h3>Table: salary_info</h3>
<pre>+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| employee_category           | varchar |
| house_rent_allowance        | decimal |
+-----------------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the employee ID, name, department name, and house rent allowance for
employees who work in departments located in either <code>'BANGALORE'</code> or <code>'COCHIN'</code>.</p>
<p>Name your output columns <code>EMPID</code>, <code>EMPNAME</code>, <code>DEPTNAME</code>,
<code>HOUSE_RENT_ALLOWANCE</code>.</p>

<h3>Example Output:</h3>
<pre>+-------+---------------+-------------+-----------------------+
| EMPID | EMPNAME       | DEPTNAME    | HOUSE_RENT_ALLOWANCE  |
+-------+---------------+-------------+-----------------------+
| 1     | Alice Rao     | HR          | 3000.00               |
| 2     | Bob Nair      | HR          | 2500.00                |
| 4     | David Menon   | Engineering | 1800.00                |
+-------+---------------+-------------+-----------------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Join emp_info to department_info on deptid, and to salary_info on employee_category, filter location IN ('BANGALORE', 'COCHIN').",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HR_SCHEMA, HR_VIS, Q11),
            db_entry("Hidden database", True, HR_SCHEMA, HR_HID, Q11),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3079. Average Balance by Account Type (Banking cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3079,
        "slug": "average-balance-by-account-type",
        "title": "Average Balance by Account Type",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: account</h3>
<pre>+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| account_id       | int     |
| customer_id      | int     |
| branch_id        | int     |
| account_type_id  | int     |
| balance          | decimal |
+------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the account type id and average account balance for each account type,
where the <b>average balance is greater than or equal to 50000</b>.</p>
<p>Name your output columns <code>Account_Type_ID</code>, <code>Average</code>.</p>

<h3>Example Output:</h3>
<pre>+-----------------+----------+
| Account_Type_ID | Average  |
+-----------------+----------+
| 1               | 52500.00 |
| 2               | 60000.00 |
| 4               | 90000.00 |
+-----------------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Group by account type, then filter the aggregated average with <code>HAVING</code> (not <code>WHERE</code>).</li>
</ul>
""",
        "hint": "GROUP BY account_type_id, then HAVING AVG(balance) >= 50000.",
        "boilerplate": {"sql": SQL_BOILERPLATE_GBHO},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, BANK_SCHEMA, BANK_VIS, Q12),
            db_entry("Hidden database", True, BANK_SCHEMA, BANK_HID, Q12),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3080. Customers With High Balance (Banking cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3080,
        "slug": "customers-with-high-balance",
        "title": "Customers With High Balance",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: customer</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| first_name    | varchar |
| last_name     | varchar |
+---------------+---------+</pre>

<h3>Table: account</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| account_id    | int     |
| customer_id   | int     |
| balance       | decimal |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the first name, last name and account id of customers who have a bank
balance <b>greater than or equal to 50000</b>. A customer with multiple qualifying accounts should
appear once per account.</p>
<p>Order the result by the customer's first name. Name your output columns
<code>FIRST_NAME</code>, <code>LAST_NAME</code>, <code>ACCOUNT_ID</code>.</p>

<h3>Example Output:</h3>
<pre>+------------+-----------+------------+
| FIRST_NAME | LAST_NAME | ACCOUNT_ID |
+------------+-----------+------------+
| Alice      | Smith     | 101        |
| Alice      | Smith     | 106        |
| Carol      | White     | 103        |
+------------+-----------+------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Join customer to account, filter balance >= 50000, ORDER BY first_name (add a secondary sort key such as account_id to keep ties stable).",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN_ORDER},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, BANK_SCHEMA, BANK_VIS, Q13),
            db_entry("Hidden database", True, BANK_SCHEMA, BANK_HID, Q13),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3081. Staff With High Salary (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3081,
        "slug": "staff-with-high-salary",
        "title": "Staff With High Salary",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: staff</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| staff_id      | int     |
| firstname     | varchar |
| position      | varchar |
| salary        | decimal |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the first name, position and salary of staff members whose
<b>salary is greater than 50000</b>.</p>
<p>Alias your output columns <code>"STAFF FIRST NAME"</code>, <code>"POSITION"</code>, <code>"SALARY"</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------------+-------------+----------+
| STAFF FIRST NAME  | POSITION    | SALARY   |
+-------------------+-------------+----------+
| Nora              | Manager     | 65000.00 |
| Priya             | Supervisor  | 55000.00 |
| Ravi              | Director    | 90000.00 |
+-------------------+-------------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter staff WHERE salary > 50000.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, STAFF_SCHEMA, STAFF_VIS, Q14),
            db_entry("Hidden database", True, STAFF_SCHEMA, STAFF_HID, Q14),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3082. Unpaid Patient Bills (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3082,
        "slug": "unpaid-patient-bills",
        "title": "Unpaid Patient Bills",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Patient</h3>
<pre>+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| PatientID      | int     |
| FirstName      | varchar |
| LastName       | varchar |
| Email          | varchar |
| AdmissionDate  | date    |
+----------------+---------+</pre>

<h3>Table: Billing</h3>
<pre>+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| BillingID      | int     |
| PatientID      | int     |
| TotalAmount    | decimal |
| PaymentStatus  | varchar |
+----------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display, for each patient with an <b>unpaid</b> bill:</p>
<ul>
  <li>the full name (first + last, separated by a space),</li>
  <li>email,</li>
  <li>admission date, and</li>
  <li>total billing amount.</li>
</ul>
<p>Sort the result by total billing amount in <b>descending</b> order. Alias your output columns
<code>PatientName</code>, <code>PatientEmail</code>, <code>AdmissionDate</code>, <code>TotalBilling</code>.</p>

<h3>Example Output:</h3>
<pre>+--------------+---------------+----------------+--------------+
| PatientName  | PatientEmail  | AdmissionDate  | TotalBilling |
+--------------+---------------+----------------+--------------+
| Sam Lee      | sam@x.com     | 2025-03-20     | 3200.00      |
| John Doe     | john@x.com    | 2025-01-10     | 1500.00      |
| Amy Wong     | amy@x.com     | 2025-04-25     | 900.00       |
+--------------+---------------+----------------+--------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b> — use <code>||</code> to concatenate strings, e.g.
      <code>FirstName || ' ' || LastName</code>.</li>
</ul>
""",
        "hint": "Join Patient to Billing on PatientID, filter PaymentStatus = 'Unpaid', concatenate names with ||, and ORDER BY TotalAmount DESC.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN_ORDER},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, HOSP_SCHEMA, HOSP_VIS, Q15),
            db_entry("Hidden database", True, HOSP_SCHEMA, HOSP_HID, Q15),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3083. Singapore Airlines Flights (Simple-flights cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3083,
        "slug": "singapore-airlines-flights",
        "title": "Singapore Airlines Flights",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Airline</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| airline_id    | int     |
| name          | varchar |
| country       | varchar |
+---------------+---------+</pre>

<h3>Table: Airplane</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| airplane_id   | int     |
| airline_id    | int     |
| model         | varchar |
| manufacturer  | varchar |
| modelnumber   | varchar |
| capacity      | int     |
+---------------+---------+</pre>

<h3>Table: Flight</h3>
<pre>+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| flight_id       | int     |
| airplane_id     | int     |
| departure_date  | date    |
| departure_time  | varchar |
| origin          | varchar |
| destination     | varchar |
+-----------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the list of flights operated by <code>'Singapore Airlines'</code>, including
the flight ID, departure date and departure time.</p>
<p>Name your output columns <code>Flight_ID</code>, <code>Departure_date</code>, <code>Departure_Time</code>.</p>

<h3>Example Output:</h3>
<pre>+-----------+-----------------+-----------------+
| Flight_ID | Departure_date  | Departure_Time  |
+-----------+-----------------+-----------------+
| 1         | 2025-01-10      | 08:00           |
| 2         | 2025-01-11      | 09:30           |
+-----------+-----------------+-----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>An airline can own several airplanes, and each airplane can have several flights — join through
      Airplane to reach the airline name.</li>
</ul>
""",
        "hint": "Join Flight -> Airplane -> Airline, filter Airline.name = 'Singapore Airlines'.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, SFLIGHT_SCHEMA, SFLIGHT_VIS, Q16),
            db_entry("Hidden database", True, SFLIGHT_SCHEMA, SFLIGHT_HID, Q16),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3084. Airbus Airplanes (Simple-flights cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3084,
        "slug": "airbus-airplanes",
        "title": "Airbus Airplanes",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Airplane</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| airplane_id   | int     |
| airline_id    | int     |
| model         | varchar |
| manufacturer  | varchar |
| modelnumber   | varchar |
| capacity      | int     |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the airplane ID and model number for airplanes manufactured by
<code>'Airbus'</code>.</p>
<p>Name your output columns <code>AIRPLANE_ID</code>, <code>MODELNUMBER</code>.</p>

<h3>Example Output:</h3>
<pre>+--------------+--------------+
| AIRPLANE_ID  | MODELNUMBER  |
+--------------+--------------+
| 1            | A350-900     |
| 3            | A380-800     |
+--------------+--------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter Airplane WHERE manufacturer = 'Airbus'.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, SFLIGHT_SCHEMA, SFLIGHT_VIS, Q17),
            db_entry("Hidden database", True, SFLIGHT_SCHEMA, SFLIGHT_HID, Q17),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3085. Students Registered in 2012 (School cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3085,
        "slug": "students-registered-2012",
        "title": "Students Registered in 2012",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: student</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| last_name     | varchar |
| first_name    | varchar |
| email         | varchar |
| phone         | varchar |
+---------------+---------+</pre>

<h3>Table: registration</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| reg_id        | int     |
| reg_year      | int     |
| reg_date      | date    |
| student_id    | int     |
| section_id    | int     |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the last names of the students who registered during the year
<code>2012</code>.</p>
<p>Name your output column <code>last_name</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+
| last_name   |
+-------------+
| Kumar       |
| Nair        |
+-------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>, which has no <code>EXTRACT()</code> function. Since
      <code>reg_date</code> is stored as <code>'YYYY-MM-DD'</code> text, a prefix match
      (<code>reg_date LIKE '2012%'</code>) is the simplest way to test the year — you could also use
      <code>strftime('%Y', reg_date) = '2012'</code>.</li>
</ul>
""",
        "hint": "Join student to registration on student_id, filter reg_date LIKE '2012%' (or strftime('%Y', reg_date) = '2012').",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, SCHOOL_SCHEMA, SCHOOL_VIS, Q18),
            db_entry("Hidden database", True, SCHOOL_SCHEMA, SCHOOL_HID, Q18),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3086. Cabin Crew on Flights Ending in 1 (Flight-crew cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3086,
        "slug": "cabin-crew-flight-ending-1",
        "title": "Cabin Crew on Flights Ending in 1",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: cabincrew</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| cabincrew_id  | int     |
| flight_id     | varchar |
| first_name    | varchar |
| last_name     | varchar |
| contact       | varchar |
+---------------+---------+</pre>

<h3>Table: flight</h3>
<pre>+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| flight_id       | varchar |
| airplane_id     | varchar |
| departure_date  | date    |
| departure_time  | varchar |
| arrival_date    | date    |
| arrival_time    | varchar |
| flight_from     | varchar |
| flight_to       | varchar |
+-----------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the list of cabin crew members whose:</p>
<ul>
  <li>first name starts with the letter <code>'A'</code>, and</li>
  <li>are assigned to a flight whose flight number <b>ends with the digit '1'</b>.</li>
</ul>
<p>Name your output columns <code>CabinCrew_ID</code>, <code>First_Name</code>, <code>Last_Name</code>,
<code>Contact</code>, <code>Flight_ID</code>.</p>

<h3>Example Output:</h3>
<pre>+---------------+-------------+-------------+----------+------------+
| CabinCrew_ID  | First_Name  | Last_Name   | Contact  | Flight_ID  |
+---------------+-------------+-------------+----------+------------+
| 1             | Anna        | Lee         | 111      | 1          |
| 3             | Alex        | Wong        | 333      | 1          |
| 5             | Aiden       | Kim         | 555      | 11         |
+---------------+-------------+-------------+----------+------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>. <code>flight_id</code> is a text column here (e.g.
      <code>'1'</code>, <code>'11'</code>), so <code>LIKE '%1'</code> checks its last character.</li>
</ul>
""",
        "hint": "Join cabincrew to flight on flight_id, filter first_name LIKE 'A%' AND flight_id LIKE '%1'.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, CREW_SCHEMA, CREW_VIS, Q19),
            db_entry("Hidden database", True, CREW_SCHEMA, CREW_HID, Q19),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3087. Passengers and Baggage on Flights Arriving in Paris (Flight-crew cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3087,
        "slug": "passengers-arriving-paris",
        "title": "Passengers and Baggage on Flights Arriving in Paris",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: flight</h3>
<pre>+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| flight_id       | varchar |
| arrival_date    | date    |
| flight_from     | varchar |
| flight_to       | varchar |
+-----------------+---------+</pre>

<h3>Table: boardingpass</h3>
<pre>+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| boardingpass_id | int     |
| flight_id       | varchar |
| passenger_id    | int     |
| gate            | varchar |
| baggage         | int     |
| meal            | varchar |
+-----------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display, for every flight arriving in <code>'Paris'</code> on
<code>2024-02-11</code>, the total number of passengers and the total number of baggage items
checked in for that flight.</p>
<p>Name your output columns <code>Flight_ID</code>, <code>Total_Passengers</code>, <code>Total_Baggage</code>.</p>

<h3>Example Output:</h3>
<pre>+------------+--------------------+-----------------+
| Flight_ID  | Total_Passengers   | Total_Baggage   |
+------------+--------------------+-----------------+
| 1          | 2                  | 3               |
| 2          | 1                  | 3               |
+------------+--------------------+-----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Use <code>COUNT()</code> for passengers and <code>SUM()</code> for baggage, grouped per flight.</li>
</ul>
""",
        "hint": "Join flight to boardingpass on flight_id, filter flight_to='Paris' AND arrival_date='2024-02-11', GROUP BY flight_id, using COUNT(passenger_id) and SUM(baggage).",
        "boilerplate": {"sql": SQL_BOILERPLATE_GBHO},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, CREW_SCHEMA, CREW_VIS, Q20),
            db_entry("Hidden database", True, CREW_SCHEMA, CREW_HID, Q20),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3088. Count of Women's Products (E-commerce cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3088,
        "slug": "womens-product-count",
        "title": "Count of Women's Products",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: product</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| code          | varchar |
| name          | varchar |
| unit_price    | decimal |
+---------------+---------+</pre>

<h3>Table: product_category</h3>
<pre>+----------------------+---------+
| Column Name          | Type    |
+----------------------+---------+
| product_category_id  | int     |
| product_id           | int     |
| category_id          | int     |
+----------------------+---------+</pre>

<h3>Table: category</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| category_id   | int     |
| code          | varchar |
| name          | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the number of products available in the <code>'Women'</code> category.</p>
<p>Alias your output column <code>product_count</code>.</p>

<h3>Example Output:</h3>
<pre>+----------------+
| product_count  |
+----------------+
| 3              |
+----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Join product -> product_category -> category, filter category.name = 'Women', and COUNT(*).",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, ECOM_SCHEMA, ECOM_VIS, Q21),
            db_entry("Hidden database", True, ECOM_SCHEMA, ECOM_HID, Q21),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3089. Slow Trains Under 50 (Trains cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3089,
        "slug": "slow-trains-under-50",
        "title": "Slow Trains Under 50",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: train_details_tbl</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| train_id      | varchar |
| train_name    | varchar |
| train_type    | varchar |
| train_speed   | int     |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the train name and train type of trains whose <b>speed is less than
50</b>.</p>
<p>Name your output columns <code>TRAIN_NAME</code>, <code>TRAIN_TYPE</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------------+-------------+
| TRAIN_NAME        | TRAIN_TYPE  |
+-------------------+-------------+
| Chennai Mail      | PASS        |
| Malwa Express     | EXP         |
| Mysore Express    | SF          |
+-------------------+-------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
</ul>
""",
        "hint": "Filter train_details_tbl WHERE train_speed < 50.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, TRAIN_SCHEMA, TRAIN_VIS, Q22),
            db_entry("Hidden database", True, TRAIN_SCHEMA, TRAIN_HID, Q22),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3090. Vegetarian Meal Passengers From Hong Kong (Flight-crew cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3090,
        "slug": "vegetarian-meal-passengers-hongkong",
        "title": "Vegetarian Meal Passengers From Hong Kong",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: passenger</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| passenger_id  | int     |
| first_name    | varchar |
| last_name     | varchar |
| email         | varchar |
| contact       | varchar |
+---------------+---------+</pre>

<h3>Table: boardingpass</h3>
<pre>+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| boardingpass_id | int     |
| flight_id       | varchar |
| passenger_id    | int     |
| meal            | varchar |
+-----------------+---------+</pre>

<h3>Table: flight</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| flight_id     | varchar |
| flight_from   | varchar |
| flight_to     | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the distinct first names and contact numbers of passengers who:</p>
<ul>
  <li>are departing from <code>'Hong Kong'</code>,</li>
  <li>are boarding the flight with flight ID <code>'4'</code>, and</li>
  <li>have requested a <code>'Vegetarian'</code> meal.</li>
</ul>
<p>Name your output columns <code>FIRST_NAME</code>, <code>CONTACT</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+----------+
| FIRST_NAME  | CONTACT  |
+-------------+----------+
| Ella        | 555      |
| Hannah      | 888      |
+-------------+----------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>. <code>flight_id</code> is text — compare it against the
      quoted string <code>'4'</code>.</li>
</ul>
""",
        "hint": "Join passenger -> boardingpass -> flight, filter flight_from='Hong Kong' AND boardingpass.flight_id='4' AND meal='Vegetarian', use SELECT DISTINCT.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, CREW_SCHEMA, CREW_VIS, Q23),
            db_entry("Hidden database", True, CREW_SCHEMA, CREW_HID, Q23),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3091. Products in the Transit Hub (E-commerce cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3091,
        "slug": "products-in-transit-hub",
        "title": "Products in the Transit Hub",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: product</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| code          | varchar |
| name          | varchar |
| unit_price    | decimal |
+---------------+---------+</pre>

<h3>Table: order_item</h3>
<pre>+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| order_item_id       | int     |
| order_id            | int     |
| order_delivery_id   | int     |
| product_id          | int     |
| quantity            | int     |
+---------------------+---------+</pre>

<h3>Table: order_delivery</h3>
<pre>+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| order_delivery_id   | int     |
| order_id            | int     |
| tracking_no         | varchar |
| status              | varchar |
+---------------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the product id and product name of every product whose delivery status
is <code>'In the transit hub'</code>.</p>
<p>Name your output columns <code>product_id</code>, <code>name</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+----------------+
| product_id  | name           |
+-------------+----------------+
| 1           | Floral Dress   |
| 2           | Denim Jacket   |
| 5           | Women Handbag  |
+-------------+----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>A product can appear in more than one order/delivery — use <code>SELECT DISTINCT</code> so it's
      only listed once.</li>
</ul>
""",
        "hint": "Join product -> order_item -> order_delivery, filter status = 'In the transit hub', use SELECT DISTINCT.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, ECOM_SCHEMA, ECOM_VIS, Q24),
            db_entry("Hidden database", True, ECOM_SCHEMA, ECOM_HID, Q24),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3092. Artists With a Number in Their Name (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3092,
        "slug": "artists-with-numbers-in-name",
        "title": "Artists With a Number in Their Name",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: artist</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| artist_id     | int     |
| name          | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the artist id and name for every artist whose name contains
<b>at least one digit</b> (0-9).</p>
<p>Name your output columns <code>ARTIST_ID</code>, <code>NAME</code>.</p>

<h3>Example Output:</h3>
<pre>+------------+------------+
| ARTIST_ID  | NAME       |
+------------+------------+
| 2          | Blink182   |
| 4          | U2         |
+------------+------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>, which has no <code>REGEXP</code> operator registered by
      default. Chain ten <code>LIKE '%0%' OR LIKE '%1%' OR ...</code> conditions (one per digit)
      instead.</li>
</ul>
""",
        "hint": "OR together ten LIKE conditions, one per digit '0' through '9', e.g. name LIKE '%0%' OR name LIKE '%1%' OR ...",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, ARTIST_SCHEMA, ARTIST_VIS, Q25),
            db_entry("Hidden database", True, ARTIST_SCHEMA, ARTIST_HID, Q25),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3093. Messages Containing "Hello" (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3093,
        "slug": "messages-containing-hello",
        "title": "Messages Containing \"Hello\"",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: message</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| message_id    | int     |
| content       | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the message id and content of every message that has <code>"Hello"</code>
somewhere in it.</p>
<p>Name your output columns <code>MESSAGE_ID</code>, <code>CONTENT</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+-----------------+
| MESSAGE_ID  | CONTENT         |
+-------------+-----------------+
| 1           | Hello world     |
| 3           | Hello there     |
| 5           | hello again     |
+-------------+-----------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>. Its <code>LIKE</code> operator is case-insensitive for
      ASCII letters by default, so <code>content LIKE '%Hello%'</code> also matches lowercase
      "hello".</li>
</ul>
""",
        "hint": "Filter message WHERE content LIKE '%Hello%'.",
        "boilerplate": {"sql": SQL_BOILERPLATE},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, MSG_SCHEMA, MSG_VIS, Q26),
            db_entry("Hidden database", True, MSG_SCHEMA, MSG_HID, Q26),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3094. Drivers In Use With Plates Ending in 0 (Ride-hailing cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3094,
        "slug": "drivers-in-use-plate-ending-zero",
        "title": "Drivers In Use With Plates Ending in 0",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: driver</h3>
<pre>+-------------------+---------+
| Column Name       | Type    |
+-------------------+---------+
| driver_id         | int     |
| first_name        | varchar |
| last_name         | varchar |
| license_number    | varchar |
| rating            | decimal |
+-------------------+---------+</pre>

<h3>Table: vehicle</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| vehicle_id    | int     |
| driver_id     | int     |
| plate_number  | varchar |
| status        | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the full name, license number, and plate number of all drivers whose
vehicle:</p>
<ul>
  <li>has a status of <code>"In Use"</code>, and</li>
  <li>has a number plate ending with <code>"0"</code>.</li>
</ul>
<p>Full name = first name + a space + last name. Name your output columns <code>Name</code>,
<code>License_Number</code>, <code>Plate_Number</code>.</p>

<h3>Example Output:</h3>
<pre>+---------------+------------------+---------------+
| Name          | License_Number   | Plate_Number  |
+---------------+------------------+---------------+
| Raj Kumar     | LIC001           | KA01AB1230    |
| Tariq Ali     | LIC003           | KA03EF7890    |
+---------------+------------------+---------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b> — use <code>||</code> to concatenate the names.</li>
</ul>
""",
        "hint": "Join driver to vehicle on driver_id, filter status = 'In Use' AND plate_number LIKE '%0', concatenate first_name || ' ' || last_name.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, RIDE_SCHEMA, RIDE_VIS, Q27),
            db_entry("Hidden database", True, RIDE_SCHEMA, RIDE_HID, Q27),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3095. Top-Rated Drivers With Active Bookings (Ride-hailing cluster)
    # ------------------------------------------------------------------ #
    {
        "id": 3095,
        "slug": "top-rated-drivers-active-bookings",
        "title": "Top-Rated Drivers With Active Bookings",
        "difficulty": "Medium",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: driver</h3>
<pre>+-------------------+---------+
| Column Name       | Type    |
+-------------------+---------+
| driver_id         | int     |
| license_number    | varchar |
| rating            | decimal |
+-------------------+---------+</pre>

<h3>Table: vehicle</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| vehicle_id    | int     |
| driver_id     | int     |
+---------------+---------+</pre>

<h3>Table: booking</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| booking_id    | int     |
| vehicle_id    | int     |
| status        | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the license number, vehicle id, rating, and booking id of all bookings
made through drivers whose:</p>
<ul>
  <li>rating is <b>greater than or equal to 4.5</b>, and</li>
  <li>booking status is <b>other than</b> <code>"Cancelled"</code>.</li>
</ul>
<p>Name your output columns <code>License_Number</code>, <code>Vehicle_ID</code>, <code>Rating</code>,
<code>Booking_ID</code>.</p>

<h3>Example Output:</h3>
<pre>+------------------+-------------+---------+-------------+
| License_Number   | Vehicle_ID  | Rating  | Booking_ID  |
+------------------+-------------+---------+-------------+
| LIC001           | 1           | 4.80    | 1           |
| LIC003           | 3           | 4.60    | 4           |
+------------------+-------------+---------+-------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>A single high-rated driver can have several non-cancelled bookings — each should appear as its
      own row.</li>
</ul>
""",
        "hint": "Join driver -> vehicle -> booking, filter rating >= 4.5 AND status <> 'Cancelled'.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, RIDE_SCHEMA, RIDE_VIS, Q28),
            db_entry("Hidden database", True, RIDE_SCHEMA, RIDE_HID, Q28),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3096. Viewers With Duplicate Names (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3096,
        "slug": "viewers-with-duplicate-names",
        "title": "Viewers With Duplicate Names",
        "difficulty": "Easy",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: viewer</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| viewer_id     | int     |
| viewername    | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the number of viewers sharing the same name, for every distinct viewer
name.</p>
<p>Order the result by <code>viewername</code>. Name your output columns <code>viewername</code>,
<code>name_count</code>.</p>

<h3>Example Output:</h3>
<pre>+--------------+---------------+
| viewername   | name_count    |
+--------------+---------------+
| John         | 2             |
| Mary         | 3             |
| Steve        | 1             |
+--------------+---------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>Every name appears at least once, so names with a count of <code>1</code> should still be
      included.</li>
</ul>
""",
        "hint": "GROUP BY viewername and COUNT(*), then ORDER BY viewername for a deterministic order.",
        "boilerplate": {"sql": SQL_BOILERPLATE_GBHO},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, VIEWER_SCHEMA, VIEWER_VIS, Q29),
            db_entry("Hidden database", True, VIEWER_SCHEMA, VIEWER_HID, Q29),
        ],
    },

    # ------------------------------------------------------------------ #
    # 3097. Users Who Have an Engineer as a Contact (Standalone)
    # ------------------------------------------------------------------ #
    {
        "id": 3097,
        "slug": "users-with-engineer-contacts",
        "title": "Users Who Have an Engineer as a Contact",
        "difficulty": "Hard",
        "topics": [T, "SQL", "Database"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: users</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| first_name    | varchar |
| last_name     | varchar |
+---------------+---------+</pre>

<h3>Table: contacts</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| contact_id    | int     |
+---------------+---------+</pre>
<p>Each row means "the user with id <code>user_id</code> has, among their contacts, the user with id
<code>contact_id</code>". Both columns reference <code>users.user_id</code>.</p>

<h3>Table: jobs</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| job_title     | varchar |
+---------------+---------+</pre>

<h3>Problem:</h3>
<p>Write a query to display the full name of every user who has <b>at least one contact whose job
title contains the word "Engineer"</b> (e.g. "Software Engineer", "Mechanical Engineer", "Engineer" —
anyone with the keyword "Engineer" anywhere in their job title counts).</p>
<p>Full name format: <code>'John Doe'</code> (first + space + last). Order the result by full name.
Alias your output column <code>FULLNAME</code>.</p>

<h3>Example Output:</h3>
<pre>+---------------+
| FULLNAME      |
+---------------+
| Bob Marley    |
| John Doe      |
+---------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b> — use <code>||</code> to concatenate the names.</li>
  <li>This asks for users whose <b>contact</b> is an engineer, not users who are themselves engineers —
      join <code>users</code> to <code>contacts</code>, then join again to <code>users</code> (aliased)
      via <code>contact_id</code> to find that contact's job.</li>
</ul>
""",
        "hint": "Join users u to contacts c on u.user_id = c.user_id, join users again (aliased cu) on c.contact_id = cu.user_id, join jobs on cu.user_id, filter job_title LIKE '%Engineer%', SELECT DISTINCT.",
        "boilerplate": {"sql": SQL_BOILERPLATE_JOIN_ORDER},
        "tests": [],
        "samples": [0],
        "databases": [
            db_entry("Sample database", False, USERS_SCHEMA, USERS_VIS, Q30),
            db_entry("Hidden database", True, USERS_SCHEMA, USERS_HID, Q30),
        ],
    },
]
