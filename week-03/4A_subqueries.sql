USE northwind;

-- 1. What is the product name(s) of the most expensive products?

SELECT productname
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- 2. What is the product name(s) and categories of the least expensive products?
SELECT p.productname, c.categoryname
FROM products p 
JOIN Categories c 
ON p.CategoryID = c.categoryID
WHERE p.unitprice = (SELECT MIN(unitprice) FROM products);		

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?

SELECT o.orderID, o.shipname, o.shipaddress
FROM orders o 
JOIN shippers s 
ON o.ShipVia = s.ShipperID
WHERE CompanyName = 'federal shipping';

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?

SELECT DISTINCT o.orderID
FROM orders o 
JOIN `order details` od 
ON o.OrderID = od.OrderID
JOIN products p 
ON od.productID = p.productID
WHERE p.ProductName = 'Sasquatch Ale';

-- 5. What is the name of the employee that sold order 10266?
 
 SELECT e.FirstName, e.LastName
 FROM employees e 
 JOIN orders o 
 ON e.EmployeeID = o.EmployeeID
 WHERE o.OrderID = 10266;

-- 6. What is the name of the customer that bought order 10266?

SELECT c.ContactName AS customername
FROM customers c 
JOIN Orders o 
ON c.CustomerID = o.CustomerID
WHERE o.orderID = 10266;
