'''
You've seen how to use the dask framework and its DataFrame abstraction to do some calculations. However, as you've seen in the video, in the big data world Spark is probably a more popular choice for data processing.

In this exercise, you'll use the PySpark package to handle a Spark DataFrame. The data is the same as in previous exercises: participants of Olympic events between 1896 and 2016.

The Spark Dataframe, athlete_events_spark is available in your workspace.

The methods you're going to use in this exercise are:

.printSchema(): helps print the schema of a Spark DataFrame.
.groupBy(): grouping statement for an aggregation.
.mean(): take the mean over each group.
.show(): show the results.

'''


# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age"))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age").show())
