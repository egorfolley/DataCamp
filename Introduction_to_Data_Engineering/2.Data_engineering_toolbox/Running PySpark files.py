'''
In this exercise, you're going to run a PySpark file using spark-submit. This tool can help you submit your application to a spark cluster.

For the sake of this exercise, you're going to work with a local Spark instance running on 4 threads. The file you need to submit is in /home/repl/spark-script.py. Feel free to read the file:

cat /home/repl/spark-script.py
You can use spark-submit as follows:

spark-submit \
  --master local[4] \
  /home/repl/spark-script.py
What does this output? Note that it may take a few seconds to get your results.

'''

# Picked up _JAVA_OPTIONS: -Xmx512m
# Picked up _JAVA_OPTIONS: -Xmx512m
# 19/09/28 15:16:47 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
# +----+------------------+
# |Year|       avg(Height)|
# +----+------------------+
# |1896| 172.7391304347826|
# |1900|176.63793103448276|
# |1904| 175.7887323943662|
# |1906|178.20622568093384|
# |1908|177.54315789473685|
# |1912| 177.4479889042996|
# |1920| 175.7522816166884|
# |1924|174.96303901437372|
# |1928| 175.1620512820513|
# |1932|174.22011541632315|
# |1936| 175.7239932885906|
# |1948|176.17279726261762|
# |1952|174.13893967093236|
# |1956|173.90096798212957|
# |1960|173.14128595600675|
# |1964|  173.448573701557|
# |1968| 173.9458648072826|
# |1972|174.56536284096757|
# |1976|174.92052773737794|
# |1980|175.52748832195473|
# +----+------------------+
# only showing top 20 rows
#
# None

# A DataFrame with with average Olympian heights by year.
