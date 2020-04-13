'''
You can use the NumPy package to create arrays. NumPy arrays are optimized for numerical analyses and contain only a single data type. To convert a list to an array, you can use the array() function from NumPy.

import numpy as np

a_list = [1, 2, 3, 4]
a_list

[1, 2, 3, 4]

an_array = np.array(a_list)
an_array

array([1, 2, 3, 4])

'''


# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)
