#import packages
import sqlite3

#connect to sqlite
connect = sqlite3.connect('patients.db')

#db object
db = connect.cursor()

#delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

#create table
table = """CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            age INTEGER NOT NULL,
            gender CHAR(25) NOT NULL,
            ethnicity CHAR(25) NOT NULL,
            insurance VARCHAR(255) NOT NULL
        ); """

db.execute(table)
connect.commit() #commit changes

#insert data into table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, gender, ethnicity, insurance) values('12345', 'John', 'Smith', '01/01/1997', '25', 'Male', 'White', 'Aetna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, gender, ethnicity, insurance) values('23456', 'Jane', 'Doe', '02/02/1988', '34', 'Female', 'White', 'BCBS')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, gender, ethnicity, insurance) values('34567', 'Mary', 'Suarez', '03/03/1957', '65', 'Female', 'Hispanic', 'United')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, gender, ethnicity, insurance) values('45678', 'John', 'Park', '04/04/1975', '47', 'Male', 'Asian', 'Cigna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, age, gender, ethnicity, insurance) values('56789', 'Jane', 'Doe', '05/05/1985', '37', 'Female', 'White', 'Aetna')")

connect.commit()

#close connection
connect.close()