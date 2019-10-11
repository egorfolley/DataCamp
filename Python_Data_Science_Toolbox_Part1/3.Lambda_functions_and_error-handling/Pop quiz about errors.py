'''
In the video, Hugo talked about how errors happen when functions are supplied arguments that they are unable to work with. In this exercise, you will identify which function call raises an error and what type of error is raised.

Take a look at the following function calls to len():

len('There is a beast in every man and it stirs when you put a sword in his hand.')

len(['robb', 'sansa', 'arya', 'eddard', 'jon'])

len(525600)

len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
Which of the function calls raises an error and what type of error is raised?

'''


In [0]: len(525600)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    len(525600)
TypeError: object of type 'int' has no len()