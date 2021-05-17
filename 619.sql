
select max(num) as num 
from (

  # getting single numbers
  SELECT num FROM my_numbers
  group by num having count(*) = 1) 
  	as t