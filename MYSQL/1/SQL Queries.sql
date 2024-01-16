show tables;
desc sales;



-- Select query 

select * from sales;
select SaleDate, Amount, Customers from sales;
select Amount, Customers , GeoID from sales;


-- Alias
select saledate, amount, boxes , amount/boxes as "amount per box"
from sales;


-- where condition

select * 
from sales 
where amount > 10000;


-- order by 

select * 
from sales
where amount> 10000
order by amount;


select * 
from sales 
where geoid= "g1"
order by pid, amount desc;

-- And operator

select * 
from sales 
where amount> 10000 and saledate >= "2022-01-01";


select saledate ,amount 
from sales
where amount >10000 and year(SaleDate) = 2022
order by amount desc;


select * 
from sales 
where boxes > 0 and boxes <= 50;

-- Between operator

select * 
from sales 
where boxes between 0 and 50;













