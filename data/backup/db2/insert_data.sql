-- Truncate tables before inserting data
TRUNCATE TABLE Address;
DELETE FROM Person;

-- Insert sample data into Person table
INSERT INTO Person (PersonID, FirstName, LastName, Age) VALUES
(1, 'John', 'Doe', 30),
(2, 'Jane', 'Doe', 25),
(3, 'Jim', 'Beam', 35),
(4, 'Jack', 'Daniels', 40),
(5, 'Johnny', 'Walker', 45),
(6, 'James', 'Bond', 50),
(7, 'Bruce', 'Wayne', 35),
(8, 'Clark', 'Kent', 30),
(9, 'Diana', 'Prince', 28),
(10, 'Barry', 'Allen', 27),
(11, 'Hal', 'Jordan', 32),
(12, 'Arthur', 'Curry', 33),
(13, 'Victor', 'Stone', 29),
(14, 'Oliver', 'Queen', 34),
(15, 'Dinah', 'Lance', 31),
(16, 'Ray', 'Palmer', 36),
(17, 'Sara', 'Lance', 28),
(18, 'Kara', 'Zor-El', 27),
(19, 'Jonn', 'Jonzz', 40),
(20, 'Zatanna', 'Zatara', 30),
(21, 'Wally', 'West', 26),
(22, 'John', 'Stewart', 35),
(23, 'Shayera', 'Hol', 32),
(24, 'Mari', 'McCabe', 29),
(25, 'Rex', 'Mason', 38);

-- Insert sample data into Address table
INSERT INTO Address (AddressID, PersonID, Street, City, State, ZipCode) VALUES
(1, 1, '123 Main St', 'Anytown', 'Anystate', '12345'),
(2, 2, '456 Elm St', 'Othertown', 'Otherstate', '67890'),
(3, 3, '789 Oak St', 'Sometown', 'Somestate', '11223'),
(4, 4, '101 Pine St', 'Smallville', 'Kansas', '54321'),
(5, 5, '202 Birch St', 'Gotham', 'New Jersey', '67812'),
(6, 6, '303 Cedar St', 'Metropolis', 'New York', '78901'),
(7, 7, '404 Maple St', 'Star City', 'California', '89012'),
(8, 8, '505 Walnut St', 'Central City', 'Missouri', '90123'),
(9, 9, '606 Chestnut St', 'Coast City', 'California', '01234'),
(10, 10, '707 Spruce St', 'Atlantis', 'Ocean', '12345'),
(11, 11, '808 Redwood St', 'Blüdhaven', 'New Jersey', '23456'),
(12, 12, '909 Sycamore St', 'National City', 'California', '34567'),
(13, 13, '1010 Willow St', 'Midway City', 'Michigan', '45678'),
(14, 14, '1111 Poplar St', 'Keystone City', 'Kansas', '56789'),
(15, 15, '1212 Aspen St', 'Hub City', 'Illinois', '67890'),
(16, 16, '1313 Fir St', 'Gateway City', 'California', '78901'),
(17, 17, '1414 Hemlock St', 'Opal City', 'Maryland', '89012'),
(18, 18, '1515 Hickory St', 'Fawcett City', 'Indiana', '90123'),
(19, 19, '1616 Magnolia St', 'Ivy Town', 'Massachusetts', '01234'),
(20, 20, '1717 Dogwood St', 'Happy Harbor', 'Rhode Island', '12345'),
(21, 21, 'UPDATED 1818 Cedar St', 'UPDATED Starling City', 'California', '23456'), -- Updated
(22, 22, '1919 Pine St', 'Gotham', 'New Jersey', '34567'),
(23, 23, '2020 Oak St', 'Metropolis', 'New York', '45678'),
(24, 24, '2121 Birch St', 'Central City', 'Missouri', '56789'),
(25, 25, '2222 Maple St', 'Coast City', 'California', '67890');