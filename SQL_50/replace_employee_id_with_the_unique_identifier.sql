-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50




-- PostgresSQL, MYSQL


-- v1
SELECT unique_id, name FROM Employees as emp
LEFT JOIN EmployeeUNI as eun ON eun.id = emp.id;


-- v2
SELECT unique_id, name FROM Employees as emp
LEFT JOIN EmployeeUNI as eun USING(id);


-- v3
SELECT unique_id, name FROM EmployeeUNI
RIGHT JOIN Employees USING(id);

-- v4
SELECT unique_id, name FROM EmployeeUNI as uni
RIGHT JOIN Employees as emp ON emp.id = uni.id;