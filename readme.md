Overall plan for this project:
Pull in Travel flight data from TravelPayouts daily, insert into MySQL DB
TODO:
    Write insertion proc in mySQL to insert a row. Python will pass in params.

SQL Database Schema Design

Prices:
    ID
    DepartAirport
    ArrivalAirport
    Flight Date
    Add Date

Airports:
    ID
    Name
    AirportCode
    AddDate
    UpdateDate

SQL Stored Procs and table functions:
    Stored proc to insert each of the above schemas, removes redundancies and doesn't insert if record already exists.
    
Use a dashboard app to display data. What Dashboard Apps do we want to use?
    Tableau
    PowerBI

Apache Airflow to run this daily. We want this running every morning.
Other options are a basic scheduler library, but I want to learn Apache.

