'''
Another useful list method is .index(), which returns the index of the element specified. For example, to get the index of 2 in x, you would use:

x = [1, 2, 3, 4]
x.index(2)

1
You can then use this result to subset another list, as you will do in this exercise.

The lists prices and names are available in your workspace.

'''


# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max_price)

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')
