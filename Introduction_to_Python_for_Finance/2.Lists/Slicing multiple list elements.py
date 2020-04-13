'''
Slicing operations on a list are used to subset multiple elements from a list. The syntax for list slicing is as follows:

list[start:end]
Remember, this syntax indicates subsetting all elements from the start and up to but not including the end element.

Also, you can use extended slicing to efficiently select multiple elements from a list. For example, the following command returns all elements from the list except the first (at index 0):

x = [1, 2, 3, 4, 5]
x[1:]

[2, 3, 4, 5]
Similarly, the following command returns all elements from the list except the last two:

x[:-2]

[1, 2, 3]

'''


# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = names[-2:]
print(names_subset)


# prices
prices = [159.54, 37.13, 71.17]

# Use extended slicing on the list prices
prices_subset = prices[:2]
print(prices_subset)
