'''
Multi-dimensional arrays can be useful for several tasks. In finance, for example, a 2D array may be used to store the prices and earnings for various companies. Let's create this 2D array, stock_array, from a list of prices and earnings.

numpy is imported as np and the two lists prices and earnings are available in your workspace.

'''


# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)


# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)
