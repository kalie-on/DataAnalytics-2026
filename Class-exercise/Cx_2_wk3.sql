USE northwind;
SELECT CategoryID, CategoryName, Description
FROM categories;

SELECT productID, Productname, QuantityPerUnit
FROM products
WHERE QuantityPerUnit LIKE '%BOX%';

SELECT productID, productname, Discontinued
FROM products
WHERE Discontinued =1;

SELECT firstname * ' ' * lastname AS Fullname
FROM employees;

SELECT customerID, companyName, country
FROM customers
WHERE country IN ('germany', 'france');

SELECT COUNT(OrderID) AS TotalOrders
FROM orders; 

SELECT supplierID, CompanyName, ContactName, ContactTitle
FROM suppliers
WHERE ContactTitle IN ( 'sale representative', 'sale manager' );


SELECT COUNT(*) AS totalcount
FROM Orders;

SELECT orderID, customerID, shipcountry, shippeddate
FROM orders
WHERE shipcountry = 'USA';

SELECT OrderID, CustomerID, requireddate, shippeddate
FROM orders
WHERE ShippedDate > RequiredDate;

SELECT productID, productName, unitsinstock, reorderlevel,  discontinued
FROM products
WHERE UnitsInStock <= ReorderLevel
AND Discontinued = 0;