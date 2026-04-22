-- Ndfon Caleb Ndakina
-- April 20, 2026
-- SHOW DATABASE

use northwind;
SHOW TABLES;
SELECT ProductName, UnitPrice
FROM Products;
SELECT *
FROM products;


SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock AS 'Stock'
FROM Products;

-- Example 4: Using WHERE clause 
-- WHERE sets a condition to filter results 
-- Retrives all company names, cities, and country from Germany

SELECT CompanyName, City, Country
FROM customers
WHERE Country = 'Germany';

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;

SELECT OrderID, CustomerID, Shipcountry, Freight
FROM Orders
WHERE Shipcountry = 'france';


SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

-- CONDITIONAL LOGIG EXAMPLES 

SELECT OrderID, Freight 
FROM orders 
WHERE Freight >= 100;


SELECT ProductName, UnitPrice, UnitsInStock 
FROM products 
WHERE UnitPrice > 20 
AND UnitsInStock > 50;

-- Come BAck Here
SELECT CompanyName, Country
FROM customers
WHERE Country IN ('UK', 'Ireland');

SELECT Productname, CategoryID, Unitprice
FROM Products
WHERE (CategoryID = 1 OR CategoryID = 2 )
AND unitprice < 20;

SELECT CompanyName, Country
FROM Customers
WHERE Country  != 'USA';

SELECT ProductNAme, Discontinued
FROM products
WHERE Discontinued != 1;


SELECT CompanyName, Country
FROM customers
WHERE Country IN ('France', 'Germany', 'Spain');

SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);


SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;


SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS null;

SELECT LastName, FirstName, Region
FROM employees
WHERE Region IS NOT null;

SELECT Companyname
FROM Customers
WHERE CompanyName LIKE 'A%';

USE northwind;

SELECT OrderID, CustomerID, OrderDate 
FROM Orders
WHERE shippeddate = '1997-01-01';

SELECT OrderID, OrderDate
FROM Orders
WHERE YEAR (OrderDate) = 1997 AND month (OrderDate) = 6;

Select productname, unitprice
from products
order by unitprice DESC;



SELECT productname, UnitPrice AS 'Original Price',
UnitPrice / 100 * 90 AS '10% Discount' 
FROM products;

SELECT companyName, Country, city
FROM Customers
ORDER BY country ASC, CompanyName ASC;

SELECT 

