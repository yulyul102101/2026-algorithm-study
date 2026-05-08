select count(*) as FISH_COUNT, N.FISH_NAME

from FISH_INFO F
join FISH_NAME_INFO N
on F.FISH_TYPE = N.FISH_TYPE

group by F.FISH_TYPE

order by FISH_COUNT desc