'''
For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?

'''


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))
