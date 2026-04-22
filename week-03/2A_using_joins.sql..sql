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