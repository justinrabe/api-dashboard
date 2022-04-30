
CREATE TABLE prices 
(
ID INT NOT NULL auto_increment PRIMARY KEY,
origin VARCHAR(50),
destination VARCHAR(50),
price INT,
depart_date DATETIME
);
SELECT * FROM prices