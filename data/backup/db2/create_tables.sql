-- Drop tables if they exist
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS Person;

CREATE TABLE Person (
    PersonID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT
);

CREATE TABLE Address (
    AddressID INT PRIMARY KEY,
    PersonID INT,
    Street NVARCHAR(100),
    City NVARCHAR(50),
    State NVARCHAR(50),
    ZipCode NVARCHAR(10),
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);