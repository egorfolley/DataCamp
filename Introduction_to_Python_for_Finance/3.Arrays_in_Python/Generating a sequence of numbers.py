'''
You may want to create an array of a range of numbers (e.g., 1 to 10) without having to type in every single number. The NumPy function arange() is an efficient way to create numeric arrays of a range of numbers. The arguments for arange() include the start, stop, and step interval as shown below:

np.arange(start, stop, step)
numpy is imported as np.

'''


# Create and print company IDs
company_ids = np.arange(1, 8, 1)
print(company_ids)

# Use array slicing to select specific company IDs
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)
