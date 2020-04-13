'''
Not only can you perform elementwise calculations on NumPy arrays, you can also calculate summary stats such as mean and standard deviation of arrays using functions from NumPy.

numpy is imported as np and the array prices (from the previous exercise) is available in your workspace.

'''


# Calculate the mean
prices_mean = np.mean(prices)
print(prices_mean)


# Calculate the standard deviation
prices_std = np.std(prices)
print(prices_std)
