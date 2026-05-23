/**
 Join table jobs_salaries and postings with a inner join using job_id column
 **/
 SELECT 
 *
 FROM linkedin_jobs.jobs_salaries j1
 INNER JOIN linkedin_jobs.postings p2432432 ON j1.job_id=p2432432.job_id;
 
 
 
 /**
2) Join table companies_companies and postings with a right join using company_id
column. Select only columns job_id and title from postings table and from
companies_companies table just the columns name and description
**/
SELECT 
p.job_id,
p.title,
cc.name,
cc.description
FROM linkedin_jobs.companies_companies cc
RIGHT JOIN linkedin_jobs.postings p ON p.company_id=cc.company_id;


/**
1) Join table Products and ProductsLines, only with productLine with value ÔÇ£ShipsÔÇØ,
with a left join
**/
WITH 
ship_products AS (SELECT * FROM classicmodels.Products p WHERE productLine='Ships'),
ship_productslines AS (SELECT * FROM classicmodels.ProductLines WHERE productLine='Ships')
SELECT * 
FROM ship_products sp
LEFT JOIN ship_productslines pl ON sp.productLine=pl.productLine;

/**
Join table Payments and Customers, from USA country, with a left join using
2)
customerNumber column
**/
SELECT *
FROM (SELECT * FROM classicmodels.Customers WHERE country='USA') c
LEFT JOIN classicmodels.Payments p  ON p.customerNumber=c.customerNumber;


WITH 
usa_customers AS (SELECT * FROM classicmodels.Customers WHERE country='USA')
SELECT *
FROM usa_customers c
LEFT JOIN classicmodels.Payments p  ON p.customerNumber=c.customerNumber;



