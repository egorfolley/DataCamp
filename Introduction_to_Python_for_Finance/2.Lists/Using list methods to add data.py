'''
You can use the .append() and .extend() methods to add elements to a list.

The .append() method increases the length of the list by one, so if you want to add only one element to the list, you can use this method.

x = [1, 2, 3]
x.append(4)
x

[1, 2, 3, 4]
The .extend() method increases the length of the list by the number of elements that are provided to the method, so if you want to add multiple elements to the list, you can use this method.

x = [1, 2, 3]
x.append([4, 5])
x

[1, 2, 3, 4, 5]

'''


# Append a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)
