'''
In this exercise, you will write a CASE statement to group the values in the DurationSeconds into 5 groups based on the following ranges:

DurationSeconds	SecondGroup
<= 120	1
> 120 and <= 600	2
> 600 and <= 1200	3
> 1201 and <= 5000	4
For all other values	5

'''


-- Complete the syntax for cutting the duration into different cases
SELECT DurationSeconds,
-- Start with the 2 TSQL keywords, and after the condition a TSQL word and a value
      CASE WHEN (DurationSeconds <= 120) THEN 1
-- The pattern repeats with the same keyword and after the condition the same word and next value
       WHEN (DurationSeconds > 120 AND DurationSeconds <= 600) THEN 2
-- Use the same syntax here
       WHEN (DurationSeconds > 601 AND DurationSeconds <= 1200) THEN 3
-- Use the same syntax here
       WHEN (DurationSeconds > 1201 AND DurationSeconds <= 5000) THEN 4
-- Specify a value
       ELSE 5
       END AS SecondGroup
FROM Incidents
