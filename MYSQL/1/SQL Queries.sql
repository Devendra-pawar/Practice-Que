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
where boxes between 0 and 50
order by boxes;

select count(boxes)
from sales 
where boxes between 0 and 1000;


-- Date

select saleDate, amount, boxes,weekday(saledate) as 'Day of week'
from sales
where weekday(SaleDate) = 4;


-- adding people table 

select * from people;

select * from people
where team = 'yummies' or team = 'delilsh';

select * from people
where team = 'yummies' and location = 'hyderabad';


-- in clause

select * 
from people 
where team in ( 'delish', 'jucies');


-- like operator


select * 
from people 
where salesperson like 'b%';

select * 
from people 
where salesperson like '%b%';


-- case operator

select * from sales;


select saledate, amount,
	case
		when amount < 1000 then 'under 1k'
        when amount <5000 then 'under 5k'
        when amount < 10000 then 'under 10k'
		else '10k or more'
	end as 'amount category'
from sales;
	

-- joins

select * from sales;


select * from people;

select p.Salesperson,s.spid, s.saledate , s.amount 
from sales s
join people p 
on p.SPID = s.SPID;


select * 
from sales s
join people p 
on p.SPID = s.SPID;


select s.saledate, s.amount, pr.product
from sales s
left join products pr 
on pr.pid=s.pid ;


select p.Salesperson,s.spid, s.saledate , s.amount , pr.product , p.team
from sales s
join people p 
	on p.SPID = s.SPID
join products pr 
	on pr.pid=s.pid ;


select p.Salesperson,s.spid, s.saledate , s.amount , pr.product , p.team
from sales s
join people p 
	on p.SPID = s.SPID
join products pr 
	on pr.pid=s.pid 
where s.amount < 500 and p.team = 'delish'
order by s.amount;


select p.Salesperson,s.spid, s.saledate , s.amount , pr.product , p.team, g.geo
from sales s
join people p 
	on p.SPID = s.SPID
join products pr 
	on pr.pid=s.pid 
join geo g 
	on g.geoid =s.geoid
where s.amount < 500 and p.team = 'delish' and g.geo in ('new zealand', 'india')
order by s.amount;


-- group by 


select g.Geo, sum(amount) , avg(amount),sum(boxes)
from sales s
join geo g
	on  g.geoid = s.geoid
group by g.geo
order by g.geo desc;


select  pr.category, p.team, sum(boxes), sum(amount)
from sales s 
join people p 
	on p.spid = s.spid
join products pr 
	on pr.pid = s.pid 
where p.team <> ''
group by pr.category, p.team
order by  pr.category, p.team;


-- limit

select pr.product,sum(s.amount) as 'total amount'
from sales s 
join products pr 
	on pr.pid = s.pid 
group by pr.product 
order by 'total amount'  
limit 10 ;















