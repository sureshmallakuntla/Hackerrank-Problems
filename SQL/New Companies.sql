# New Companies

select c.company_code, c.founder, count(distinct e.lead_manager_code) as leads, count(distinct e.senior_manager_code) as seniors, count(distinct e.manager_code) as managers, count(distinct e.employee_code) as employees
from Company c, Employee e where e.company_code=c.company_code group by 1,2
order by 1;
