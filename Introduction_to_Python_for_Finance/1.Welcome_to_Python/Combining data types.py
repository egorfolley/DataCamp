'''
Different types of data types have different properties. For example, strings and floats cannot be mathematically combined. To convert a variable x to an integer, you can use the command int(x). Similarly, to convert a variable y to a string, you can use the command str(y).

It's time for you to change some data types to complete and print a statement.

The variables company_1, year_1, and revenue_1 are available in your workspace.

'''


# Update data types
year_1_str = str(year_1)
revenue_1_str = str(revenue_1)

# Create a complete sentence combining only the string data types
sentence = 'The revenue of ' + company_1 + ' in ' + year_1_str + ' was $' + revenue_1_str + ' billion.'

# Print sentence
print(sentence)
