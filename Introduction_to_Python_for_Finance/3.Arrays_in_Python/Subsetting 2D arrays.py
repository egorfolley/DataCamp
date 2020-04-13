'''
Subsetting 2D arrays is similar to subsetting nested lists. In a 2D array, the indexing or slicing must be specific to the dimension of the array:

array[row_index, column_index]
numpy is imported as np and the 2D array stock_array_transposed (from the previous exercise) is available in your workspace.

'''


# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)


# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:, 1]
print(earnings)


# Subset the price and earning for first company
company_1 = stock_array_transposed[0, :]
print(company_1)
