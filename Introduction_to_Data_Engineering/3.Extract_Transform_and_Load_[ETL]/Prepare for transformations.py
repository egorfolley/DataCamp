'''
As mentioned in the video, before you can do transformations using PySpark, you need to get the data into the Spark framework. You saw how to do this using PySpark. Can you choose the correct code?

(A)

spark.read.jdbc("jdbc:postgresql://repl:password@localhost:5432/pagila",
                "customer")
(B)

spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
                "customer",
                {"user":"repl","password":"password"})
(C)

spark.read.jdbc("jdbc:postgresql://repl:password@localhost:5432/pagila/customer")

'''


# B
