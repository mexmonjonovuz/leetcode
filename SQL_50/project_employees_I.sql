-- https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50


-- PostgresSQL , MYSQL,

-- v1
SELECT project_id,ROUND(AVG(experience_years),2)  as average_years From Project as pr
RIGHT JOIN Employee as emp ON emp.employee_id = pr.employee_id
GROUP BY project_id
HAVING project_id is not null
ORDER BY project_id ASC;


-- v2
SELECT project_id,ROUND(AVG(experience_years),2)  as average_years From Project as pr
LEFT JOIN Employee as emp ON emp.employee_id = pr.employee_id
GROUP BY project_id
HAVING project_id is not null
ORDER BY project_id ASC;

-- v3

SELECT project_id,ROUND(AVG(experience_years),2)  as average_years From Project as pr
LEFT JOIN Employee as emp ON emp.employee_id = pr.employee_id
GROUP BY project_id
HAVING project_id is not null;

-- v4

SELECT project_id, ROUND(AVG(experience_years), 2) as average_years
From Project as pr
         LEFT JOIN Employee as emp ON emp.employee_id = pr.employee_id
GROUP BY project_id;

-- v5

SELECT project_id,ROUND(AVG(experience_years),2)  as average_years From Project as pr
JOIN Employee as emp ON emp.employee_id = pr.employee_id
GROUP BY project_id;