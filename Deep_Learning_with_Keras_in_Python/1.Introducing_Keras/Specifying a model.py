'''
You will build a simple regression model to forecast the orbit of the meteor!

Your training data consist of measurements taken at time steps from -10 minutes before the impact region to +10 minutes after. Each time step can be viewed as an X coordinate in our graph, which has an associated position Y for the meteor at that time step.

Note that you can view this problem as approximating a quadratic function via the use of neural networks.


This data is stored in two numpy arrays: one called time_steps , containing the features, and another called y_positions, with the labels.

Feel free to look at these arrays in the console anytime, then build your model! Keras Sequential model and Dense layers are available for you to use.

'''


# Instantiate a Sequential model
model = Sequential()

# Add a Dense layer with 50 neurons and an input of 1 neuron
model.add(Dense(50, input_shape=(1,), activation='relu'))

# Add two Dense layers with 50 neurons and relu activation
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))

# End your model with a Dense layer and no activation
model.add(Dense(1))