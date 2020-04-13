'''
Boolean arrays can be a very powerful way to subset arrays. In this exercise, you will identify the prices that are greater than average from a list of prices.

numpy is imported as np and the array prices is available in your workspace.

'''


# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (prices > price_mean)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)
