SELECT e.name as Employee from 
Employee e JOIN Employee m on e.managerId = m.id AND e.salary > m.salary;
