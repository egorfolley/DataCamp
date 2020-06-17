'''
This chapter uses data gathered by the National UFO Reporting Center. The data is contained in the Incidents table and in this lesson, you will be aggregating values in the DurationSeconds column.

'''


-- Calculate the average, minimum and maximum
SELECT avg(DurationSeconds) AS Average,
       min(DurationSeconds) AS Minimum,
       max(DurationSeconds) AS Maximum
FROM Incidents
