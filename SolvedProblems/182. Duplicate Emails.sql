select distinct P1.email from Person P1 INNER JOIN Person P2 
ON (P1.email = P2.email AND P1.id != P2.id)
