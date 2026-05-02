select count(*) as USERS
from USER_INFO
where 
(AGE >= 20 and AGE <= 29) and
(year(JOINED) like 2021)