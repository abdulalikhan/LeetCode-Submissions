SELECT D.name AS Department, E.name AS Employee, E.Salary AS Salary
FROM EMPLOYEE E
INNER JOIN DEPARTMENT D
ON (E.departmentId=D.id)
WHERE E.Salary=(SELECT MAX(Salary) FROM EMPLOYEE WHERE departmentId=E.departmentId);