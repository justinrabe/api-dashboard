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


Use a dashboard app to display data. What Dashboard Apps do we want to use?
    Tableau
    PowerBI

Apache Airflow to run this daily