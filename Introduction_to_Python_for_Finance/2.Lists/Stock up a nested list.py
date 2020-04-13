'''
Lists can also contain other lists. In the example shown below, x is a nested list consisting of three lists:

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
You can use indexing to subset lists within a nested list. To extract the first list within x, you can use the following command:

x[0]

[1, 2, 3]
The two lists names and prices you created earlier are available in your workspace.

'''


# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[0])
