select NAME, count(*) as COUNT
from ANIMAL_INS
where NAME is not null
group by NAME
HAVING count(*) >= 2
order by NAME