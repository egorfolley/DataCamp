'''
Dropout is a form of regularization that removes a different random subset of the units in a layer in each round of training. In this exercise, we will add dropout to the convolutional neural network that we have used in previous exercises:

Convolution (15 units, kernel size 2, 'relu' activation)
Dropout (20%)
Convolution (5 units, kernel size 2, 'relu' activation)
Flatten
Dense (3 units, 'softmax' activation)
A Sequential model along with Dense, Conv2D, Flatten, and Dropout objects are available in your workspace.

'''


# Add a convolutional layer
model.add(Conv2D(15, kernel_size=2, activation='relu', 
                 input_shape=(img_rows, img_cols, 1)))

# Add a dropout layer
model.add(Dropout(.2))

# Add another convolutional layer
model.add(Conv2D(5, kernel_size=2, activation='relu'))

# Flatten and feed to output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))