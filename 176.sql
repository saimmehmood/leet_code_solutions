# nested select statement - the inner select
# statement gets the highest salary 
select max(Salary) as SecondHighestSalary 
from Employee 
where Salary not in 
	(select max(Salary) from Employee)