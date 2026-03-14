select round(sum(DAILY_FEE)/count(*),0)'AVERAGE_FEE'
from CAR_RENTAL_COMPANY_CAR 
where CAR_TYPE = "SUV"