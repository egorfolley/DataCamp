'''
In this exercise, you will use a CASE statement to create a new column which specifies whether the Country is USA or International.

'''


SELECT Country,
       CASE WHEN Country = 'us' THEN 'USA'
       ELSE 'International'
       END AS SourceCountry
FROM Incidents
