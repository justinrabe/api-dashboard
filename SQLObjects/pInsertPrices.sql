CREATE PROCEDURE `pInsertPrices` (
    origin varchar(50)
    ,destination varchar(50)
    ,price INT
    ,depart_date datetime
    )
BEGIN
    IF origin NOT IN Airports
    BEGIN
        EXEC pInsertAirport(origin)
    END
    IF destination NOT IN Airports
    BEGIN
        EXEC pInsertAirport(origin)
    END

    INSERT INTO Prices (origin, destination, price, depart_date)
    --INSERT NEW AIRPORT
END