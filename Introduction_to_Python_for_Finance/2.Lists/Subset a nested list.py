'''
You can also extract an element from the list you extracted. To do this, you use two indices. The first index is the position of the list, and the second index is the position of the element within the list.

For example, if you want to extract 7 from x, you can use the following command:

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x[2][0]

7
Here the first index 2 refers to the third list in x and the second index 0 refers to the first element of the third list in x.

The nested list stocks you created in the last exercise is available in your workspace and is printed in the IPython shell on the right.

'''


# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])
