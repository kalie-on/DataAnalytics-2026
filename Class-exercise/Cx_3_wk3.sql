USE northwind;

SELECT ProductID, productname, unitprice, unitsinstock
FROM products
ORDER BY unitprice DESC;

SELECT customerID, companyname, contactname, country
FROM customers
ORDER BY country ASC, companyname ASC;


