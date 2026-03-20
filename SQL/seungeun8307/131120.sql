select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER like 'W' and date_format(DATE_OF_BIRTH, '%m') = '03' and TLNO IS NOT NULL
order by MEMBER_ID ASC;