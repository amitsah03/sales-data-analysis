-- 1. Total Sales by Online Store
SELECT Channel AS Online_Store, 
       SUM(Amount) AS Total_Sales
FROM sales_data
GROUP BY Channel
ORDER BY Total_Sales DESC;

-- 2. Order Count by Order Status
SELECT Status, 
       COUNT(Order_ID) AS Order_Count
FROM sales_data
GROUP BY Status;

-- 3. Sales Distribution by State
SELECT Ship_State, 
       SUM(Amount) AS Statewise_Sales
FROM sales_data
GROUP BY Ship_State
ORDER BY Statewise_Sales DESC
LIMIT 5;

-- 4. Gender-Based Sales
SELECT Gender, 
       SUM(Amount) AS Total_Sales
FROM sales_data
GROUP BY Gender;

-- 5. Sales by Month
SELECT Month, 
       SUM(Amount) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY STR_TO_DATE(CONCAT('2022-', Month, '-01'), '%Y-%b-%d');

-- 6. Age Group Analysis (20+ vs 40+)
SELECT AgeGroup, 
       COUNT(*) AS Order_Count,
       SUM(Amount) AS Total_Sales
FROM sales_data
GROUP BY AgeGroup;

-- 7. Total Quantity Sold by Product Category
SELECT Category, 
       SUM(Qty) AS Total_Quantity_Sold
FROM sales_data
GROUP BY Category
ORDER BY Total_Quantity_Sold DESC;
