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

USE northwind;

SELECT o.orderID, c.companyname AS 'customer', o.orderdate
FROM Orders o
JOIN customer c ON o.customerID = c.customerID
ORDER BY O.orderdate DESC
LIMIT 5;

SELECT Oderid, companyname, orderdate
FROM orders
JOIN customer USING (CUSTOMER)
ORDER BY orderdate
LIMIT 5;

SELECT p.productname, c.categoryname, p.unitprice
FROM Products 
INNER JOIN categiories c ON p.categoryID = c.categoryID
ORDER BY c.categoryname, p.productname
LIMIT 6;

SELECT c.CompanyName, COUNT(o.OrderID) AS 'Order Count'
FROM customers c
left join Orders o ON c.customerID = o.customerID
GROUP BY c.companyName
ORDER BY 'Order Count' ASC
LIMIT 5;