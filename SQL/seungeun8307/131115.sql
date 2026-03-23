select *
from FOOD_PRODUCT
where price = (select MAX(PRICE) from FOOD_PRODUCT);