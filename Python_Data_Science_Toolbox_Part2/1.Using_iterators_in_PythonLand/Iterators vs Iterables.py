'''
Let's do a quick recall of what you've learned about iterables and iterators. Recall from the video that an iterable is an object that can return an iterator, while an iterator is an object that keeps state and produces the next value when you call next() on it. In this exercise, you will identify which object is an iterable and which is an iterator.

The environment has been pre-loaded with the variables flash1 and flash2. Try printing out their values with print() and next() to figure out which is an iterable and which is an iterator.

'''


In [1]: print(type(flash1), type(flash2))
<class 'list'> <class 'list_iterator'>

# flash1 is an iterable and flash2 is an iterator.
