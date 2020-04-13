'''
In this exercise, you are provided the names of companies with their associated sector, and your goal is to find all companies that are associated with health care sector.

numpy is imported as np and the arrays names and sectors are available in your workspace.

'''


# Create boolean array
boolean_array = (sectors == 'Health Care')
print(boolean_array)

# Print only health care companies
health_care = names[boolean_array]
print(health_care)
