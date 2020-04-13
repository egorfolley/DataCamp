'''
Lists methods and functions are useful for analyses. Functions take objects as inputs or are "passed" an object. Methods, in contrast, act on objects. For lists, useful functions include max() and min(), which identify the maximum or minimum value in a list. A useful list method is .sort() which sorts the elements in a list.

'''


# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)


# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)
