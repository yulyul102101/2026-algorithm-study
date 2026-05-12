select 
(PRICE DIV 10000) * 10000 as PRICE_GROUP,
count(*) as PRODUCTS

from PRODUCT

group by (PRICE DIV 10000) * 10000
order by PRICE DIV 10000 asc;