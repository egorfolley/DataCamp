'''
You've seen from the videos that list comprehensions and generator expressions look very similar in their syntax, except for the use of parentheses () in generator expressions and brackets [] in list comprehensions.

In this exercise, you will recall the difference between list comprehensions and generators. To help with that task, the following code has been pre-loaded in the environment:

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)
Try to play around with fellow1 and fellow2 by figuring out their types and printing out their values. Based on your observations and what you can recall from the video, select from the options below the best description for the difference between list comprehensions and generators.

'''


In [1]: fellow1
Out[1]: ['samwise', 'aragorn', 'legolas', 'boromir']

In [2]: fello2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    fello2
NameError: name 'fello2' is not defined

In [3]: fellow2
Out[3]: <generator object <genexpr> at 0x7fc604588f10>

# A list comprehension produces a list as output, a generator produces a generator object.
