'''
Arrays allow for efficient numerical manipulation of its elements. Let's explore element-wise mathematical operations by calculating price to earnings ratio using two arrays, prices_array and earnings_array from the previous exercise.

This price to earnings ratio, or PE ratio, is a financial indicator of the dollar amount an investor can expect to invest in a company in order to receive one dollar of that company’s earnings.

prices_array and earnings_array are available in your workspace.

'''


# Import numpy as np
import numpy as np

# Create PE ratio array
pe_array = np.array(prices_array/earnings_array)

# Print pe_array
print(pe_array)
