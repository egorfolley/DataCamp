'''
In the previous exercise, you looked at the non-missing values in the IncidentState column. But what if you want to replace the missing values with another value instead of omitting them? You can do this using the ISNULL() function. Here we replace all the missing values in the Shape column using the word 'Saucer':

SELECT  Shape, ISNULL(Shape, 'Saucer') AS Shape2
FROM Incidents
You can also use ISNULL() to replace values from a different column instead of a specified word.

'''


-- Check the IncidentState column for missing values and replace them with the City column
SELECT IncidentState, ISNULL(IncidentState, City) AS Location
FROM Incidents
-- Filter to only return missing values from IncidentState
WHERE IncidentState IS NULL;
