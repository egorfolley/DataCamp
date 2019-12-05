'''
In this exercise, you will fit the fully connected neural network that you constructed in the previous exercise to image data. The training data is provided as two variables: train_data that contains the pixel data for 50 images of the three clothing classes and train_labels, which contains one-hot encoded representations of the labels for each one of these 50 images. Transform the data into the network's expected input and then fit the model on training data and training labels.

The model you compiled in the previous exercise, and train_data and train_labels are available in your workspace.

'''


# Reshape the data to two-dimensional array
train_data = train_data.reshape((train_data.shape[0], -1))

# Fit the model
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)