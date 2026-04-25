USE northwind;

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. 
-- Order by product name.
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS 'Supplier Name'
FROM Products p
JOIN Suppliers s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName;

-- 3. Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name.

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName AS SupplierName
FROM ProductS P 
JOIN categories c
ON p.CategoryID = c.CategoryID
JOIN Suppliers s
ON p.supplierID = s.supplierID
ORDER BY p.productName;

-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.

SELECT o.OrderID, o.Shipname, o.shipAddress, s.companyname AS 'Shippers'
FROM Orders o 
JOIN shippers S
ON o.ShipVia = s.shipperID
WHERE o.Shipcountry = 'Germany'
ORDER BY Shippers, o.ShipName;

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name. 

SELECT o.Shipname, s.companyname AS 'Shippers', COUNT(*) AS Ordercount
FROM Orders o 
JOIN shippers S
ON o.ShipVia = s.shipperID
WHERE o.Shipcountry = 'Germany'
GROUP BY o.ShipName, s.CompanyName
ORDER BY Shippers, o.ShipName;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.
-- ∗ Hint: You will need to join on three tables to accomplish this. (One of these tables has a sneaky space in the name, so you will need to surround it with backticks, like this: `table name`)

SELECT o.OrderID, od.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders o 
jOIN `order details` od
ON o.orderID = od.orderid
JOIN products p
ON od.productID = p.productID
WHERE p.productName = 'sasquatch ale';
