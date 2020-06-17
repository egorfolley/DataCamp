'''
You can calculate statistics for each group using GROUP BY. For example, you can calculate the maximum value for each state using the following query:

SELECT State, MAX(DurationSeconds)
FROM Incidents
GROUP BY State
To filter even further, for example, to find the values for states where the maximum value is greater than 10, you can use the HAVING clause.

'''


-- Calculate the aggregations by Shape
SELECT Shape,
       AVG(DurationSeconds) AS Average,
       MIN(DurationSeconds) AS Minimum,
       MAX(DurationSeconds) AS Maximum
FROM Incidents
GROUP BY Shape



-- Calculate the aggregations by Shape
SELECT Shape,
       AVG(DurationSeconds) AS Average,
       MIN(DurationSeconds) AS Minimum,
       MAX(DurationSeconds) AS Maximum
FROM Incidents
GROUP BY Shape
-- Return records where minimum of DurationSeconds is greater than 1
HAVING MIN(DurationSeconds) > 1
